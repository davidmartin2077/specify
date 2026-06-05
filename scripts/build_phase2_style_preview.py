#!/usr/bin/env python3
"""Build a phase-2-style reasoning preview for the existing 330 candidates.

The preview preserves text, labels, encodings, context, and ids. It only
rewrites the reasoning into the more concrete phase-2 style. Output stays in
data/raw and must not be treated as a processed replacement without review.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
INPUT_PATH = ROOT / "data/processed/combined_candidates.jsonl"
OUTPUT_JSONL = ROOT / "data/raw/combined_candidates_phase2_style_preview.jsonl"
OUTPUT_JSON = ROOT / "data/raw/combined_candidates_phase2_style_preview.json"

GENERIC_EVIDENCE = {
    "存在可疑编码或语境信号。",
    "存在弱暗示、关键词撞车或候选编码痕迹。",
    "文本含编码或规避表达。",
    "上下文中的时间、回复链或话题提供独立支持。",
    "文本和上下文共同提供风险信号。",
}


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
    for raw_part in notes.split(";"):
        part = raw_part.strip()
        if "=" in part:
            key, value = part.split("=", 1)
            parsed[key.strip()] = value.strip()
    return parsed


def clean_list(value: Any) -> list[str]:
    if not isinstance(value, list):
        return []
    return [str(item).strip() for item in value if str(item).strip()]


def context_summary(sample: dict[str, Any]) -> str:
    context = sample.get("context", {})
    if not isinstance(context, dict):
        return "当前缺少可靠上下文，判断主要依赖文本本身。"

    parts = []
    for field, label in (
        ("title", "场景"),
        ("parent_comment", "上级评论"),
        ("topic", "话题"),
        ("time", "时间"),
    ):
        value = str(context.get(field, "")).strip()
        if value:
            parts.append(f"{label}为“{value}”")

    replies = clean_list(context.get("reply_chain"))
    if replies:
        parts.append(f"回复链出现“{' / '.join(replies[:3])}”")

    if not parts:
        return "当前缺少可靠上下文，判断主要依赖文本本身。"
    return "；".join(parts) + "。"


def mapping_hint(sample: dict[str, Any], notes: dict[str, str]) -> str:
    for key in ("original_note", "original_notes", "meme_cluster", "category"):
        value = notes.get(key, "").strip()
        if value and value not in {"generated_expansion", "needs_human_review"}:
            return value
    target = str(sample.get("target_reference", "")).strip()
    if target:
        return target
    return ""


def encoding_analysis(sample: dict[str, Any], notes: dict[str, str]) -> list[str]:
    risk = sample.get("risk_level")
    primary = sample.get("encoding_primary", "none")
    secondary = clean_list(sample.get("encoding_secondary"))
    hint = mapping_hint(sample, notes)

    if risk == "none":
        lines = ["当前未形成稳定风险编码；表面词、缩写、数字或符号仍可作为召回线索。"]
        if hint:
            lines.append(f"可能触发联想的语义簇为“{hint}”，但不能只凭该联想下结论。")
        return lines

    lines = [f"主要解构机制为 {primary}。"]
    if secondary:
        lines.append(f"同时存在 {'、'.join(secondary)} 等辅助机制。")
    if hint:
        lines.append(f"候选映射或语义簇为“{hint}”；需要结合语境判断该映射是否成立。")
    if risk in {"low", "medium"}:
        lines.append("该信号值得高召回关注，但单一机制不足以直接确认目标。")
    else:
        lines.append("编码机制与语境相互印证，普通字面解释的解释力较弱。")
    return lines


def specific_support(sample: dict[str, Any]) -> list[str]:
    reasoning = sample.get("reasoning", {})
    if not isinstance(reasoning, dict):
        reasoning = {}
    original = [
        item
        for item in clean_list(reasoning.get("supporting_evidence"))
        if item not in GENERIC_EVIDENCE and "按项目分类" not in item
    ]
    return original[:2]


def supporting_evidence(sample: dict[str, Any], notes: dict[str, str]) -> list[str]:
    risk = sample.get("risk_level")
    if risk == "none":
        return []

    evidence = specific_support(sample)
    primary = sample.get("encoding_primary", "none")
    if not evidence:
        evidence.append(f"文本存在可按 {primary} 解构的候选信号。")

    context = sample.get("context", {})
    if isinstance(context, dict):
        replies = clean_list(context.get("reply_chain"))
        parent = str(context.get("parent_comment", "")).strip()
        topic = str(context.get("topic", "")).strip()
        if parent or replies:
            evidence.append("上级评论或回复链提供了独立语境支持。")
        elif topic:
            evidence.append(f"话题“{topic}”使非字面解释值得召回复核。")

    hint = mapping_hint(sample, notes)
    if hint and len(evidence) < 3:
        evidence.append(f"现有标注提示的映射线索为“{hint}”。")
    return evidence[:3]


def counter_evidence(sample: dict[str, Any]) -> list[str]:
    risk = sample.get("risk_level")
    reasoning = sample.get("reasoning", {})
    if not isinstance(reasoning, dict):
        reasoning = {}
    original = clean_list(reasoning.get("counter_evidence"))

    if risk in {"none", "low"}:
        counters = [
            item
            for item in original
            if "仍需人工复核" not in item and "正式训练集" not in item
        ][:2]
        if not counters:
            counters.append("当前语境存在完整、自然的普通解释。")
        if not any("缺少" in item or "没有" in item for item in counters):
            counters.append("缺少明确目标映射、规避意图、交易招揽或异常互动共识。")
        return counters[:3]

    counters = [
        item
        for item in original
        if "仍需人工复核" not in item and "保留匿名化" not in item
    ][:2]
    if not counters:
        counters.append("若脱离当前标题、话题或回复链，部分表达仍可能有普通解释。")
    if risk == "medium" and not any("缺少" in item or "不足" in item for item in counters):
        counters.append("具体目标或行为链仍不完整，不宜直接判为最高风险。")
    return counters[:3]


def final_rationale(sample: dict[str, Any]) -> str:
    risk = sample.get("risk_level")
    if risk == "high":
        return "编码线索与语境相互印证，风险解释明显强于普通解释；按高召回目标标为 high。"
    if risk == "medium":
        return "存在值得解构和召回的非字面信号，但目标或行为链仍不完整，标为 medium 并建议复核。"
    if risk == "low":
        return "存在弱风险联想，保留召回价值；当前普通解释更强，标为 low，避免过度升级。"
    return "表面可能触发风险词或梗联想，但当前反证和普通语境更完整，标为 none，避免仅凭命中误判。"


def rewrite_reasoning(sample: dict[str, Any]) -> dict[str, Any]:
    notes = parse_notes(sample.get("review_notes", ""))
    return {
        "literal_analysis": [f"字面上是在表达：{sample.get('text', '')}"],
        "encoding_analysis": encoding_analysis(sample, notes),
        "context_analysis": [context_summary(sample)],
        "supporting_evidence": supporting_evidence(sample, notes),
        "counter_evidence": counter_evidence(sample),
        "final_rationale": final_rationale(sample),
    }


def rewrite_sample(sample: dict[str, Any]) -> dict[str, Any]:
    result = dict(sample)
    result["reasoning"] = rewrite_reasoning(sample)
    notes = str(result.get("review_notes", "")).strip()
    marker = "style_preview=phase2_reasoning_v1; high_recall_reasoning; not_merged_preview"
    result["review_notes"] = f"{notes}; {marker}" if notes else marker
    return result


def write_jsonl(rows: list[dict[str, Any]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False, separators=(",", ":")) + "\n")


def write_json(rows: list[dict[str, Any]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        json.dump(rows, handle, ensure_ascii=False, indent=2)


def main() -> int:
    rows = [rewrite_sample(sample) for sample in load_jsonl(INPUT_PATH)]
    write_jsonl(rows, OUTPUT_JSONL)
    write_json(rows, OUTPUT_JSON)
    print(f"Wrote {len(rows)} style-preview records to {OUTPUT_JSONL}")
    print(f"Wrote {len(rows)} style-preview records to {OUTPUT_JSON}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
