#!/usr/bin/env python3
"""Build a deterministic stratified human-review sample for phase3 wave 2."""

from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path
from typing import Any

from audit_text_style import flags_for


ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "data/raw/phase3_second_wave_candidates.jsonl"
OUTPUT_JSON = ROOT / "data/raw/phase3_second_wave_review_sample.json"
OUTPUT_MD = ROOT / "docs/phase3_second_wave_review_sample.md"

CATEGORY_NAMES = {
    "sexual_content": "色情低俗",
    "spam_ads_fraud": "广告/诈骗/导流",
    "insulting_abuse": "辱骂/群体攻击",
    "weapons_explosives": "枪爆武器",
    "public_affairs": "公共事务",
    "political_history": "政治历史/鉴证梗",
    "platform_censorship_evasion": "平台规避/审查黑话",
    "cyber_abuse": "网络黑产/安全风险",
    "violence_extremism": "暴力极端",
    "illegal_goods": "违禁交易",
    "gambling": "赌博",
}

RISK_MODES = ("direct", "obfuscated", "contextual")
BOUNDARY_MODES = ("weak_signal", "safe_context")


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    rows = []
    with path.open("r", encoding="utf-8") as handle:
        for line_number, raw_line in enumerate(handle, start=1):
            line = raw_line.strip()
            if not line:
                continue
            value = json.loads(line)
            if not isinstance(value, dict):
                raise ValueError(f"{path}:{line_number}: expected object")
            rows.append(value)
    return rows


def parse_notes(notes: Any) -> dict[str, str]:
    parsed: dict[str, str] = {}
    if not isinstance(notes, str):
        return parsed
    for part in notes.split(";"):
        part = part.strip()
        if "=" in part:
            key, value = part.split("=", 1)
            parsed[key.strip()] = value.strip()
    return parsed


def review_focus(mode: str) -> str:
    return {
        "direct": "风险意图是否足够明确，high 是否合理？",
        "obfuscated": "规避映射是否自然，medium 是否证据充分？",
        "contextual": "上下文是否真的提升风险解释，medium 是否过度？",
        "weak_signal": "普通解释是否更强，low 是否仍值得召回？",
        "safe_context": "反证是否完整，none 是否会造成漏判？",
    }[mode]


def compact_context(sample: dict[str, Any]) -> str:
    context = sample.get("context", {})
    if not isinstance(context, dict):
        return ""
    values = [
        str(context.get("title", "")),
        str(context.get("parent_comment", "")),
        " / ".join(str(item) for item in context.get("reply_chain", []) if str(item).strip()),
    ]
    return "；".join(value for value in values if value)


def build_sample(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    grouped: dict[str, dict[str, list[dict[str, Any]]]] = defaultdict(lambda: defaultdict(list))
    for row in rows:
        notes = parse_notes(row.get("review_notes", ""))
        grouped[notes["category"]][notes["contrast_mode"]].append(row)

    selected = []
    for category_index, category in enumerate(CATEGORY_NAMES):
        modes = [
            BOUNDARY_MODES[0],
            BOUNDARY_MODES[1],
            RISK_MODES[category_index % len(RISK_MODES)],
            RISK_MODES[(category_index + 1) % len(RISK_MODES)],
        ]
        for mode_index, mode in enumerate(modes):
            candidates = grouped[category][mode]
            if not candidates:
                raise ValueError(f"No candidates for {category}/{mode}")
            flagged_candidates = [row for row in candidates if "reviewer_voice" in flags_for(str(row["text"]))]
            if mode == "weak_signal" and flagged_candidates:
                row = flagged_candidates[category_index % len(flagged_candidates)]
            else:
                row = candidates[(category_index + mode_index) % len(candidates)]
            selected.append(
                {
                    "id": row["id"],
                    "category": category,
                    "category_name": CATEGORY_NAMES[category],
                    "contrast_mode": mode,
                    "text": row["text"],
                    "context": compact_context(row),
                    "proposed_risk_level": row["risk_level"],
                    "proposed_encoding_primary": row["encoding_primary"],
                    "hard_negative": row["hard_negative"],
                    "preliminary_style_flags": flags_for(str(row["text"])),
                    "review_focus": review_focus(mode),
                    "review_verdict": "",
                    "review_comment": "",
                }
            )
    return selected


def render_markdown(sample: list[dict[str, Any]]) -> str:
    lines = [
        "# 第三阶段第二波分层人工复核清单",
        "",
        "本清单从第二波 185 条 raw 中确定性抽取 44 条，每个类别 4 条。候选原始标签未被修改。",
        "",
        "复核回复格式建议：`ID：通过`，或 `ID：改为 medium，原因……`，或 `ID：退回，原因……`。",
        "",
    ]
    current_category = ""
    for index, item in enumerate(sample, start=1):
        if item["category"] != current_category:
            current_category = item["category"]
            lines.extend(["", f"## {item['category_name']} `{current_category}`", ""])
        lines.extend(
            [
                f"### {index}. `{item['id']}`",
                "",
                f"- 模式：`{item['contrast_mode']}`",
                f"- 文本：{item['text']}",
                f"- 上下文：{item['context']}",
                f"- 当前标签：`{item['proposed_risk_level']}` / `{item['proposed_encoding_primary']}`"
                f" / hard_negative=`{str(item['hard_negative']).lower()}`",
                f"- 初步风格标记：`{', '.join(item['preliminary_style_flags']) or 'none'}`",
                f"- 复核重点：{item['review_focus']}",
                "- 复核结论：待填写",
                "",
            ]
        )
    return "\n".join(lines).strip() + "\n"


def main() -> int:
    rows = load_jsonl(INPUT)
    sample = build_sample(rows)
    if len(sample) != 44:
        raise ValueError(f"Expected 44 review samples, got {len(sample)}")
    OUTPUT_JSON.write_text(json.dumps(sample, ensure_ascii=False, indent=2), encoding="utf-8")
    OUTPUT_MD.write_text(render_markdown(sample), encoding="utf-8")
    print(f"Wrote {len(sample)} review samples to {OUTPUT_JSON}")
    print(f"Wrote readable review checklist to {OUTPUT_MD}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
