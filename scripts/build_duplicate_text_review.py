#!/usr/bin/env python3
"""Build a self-contained duplicate-text review checklist."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
AUDIT_JSON = ROOT / "data/raw/context_requirement_audit.json"
COMBINED_PREVIEW_JSONL = ROOT / "data/raw/combined_candidates_binary_preview.jsonl"
OUTPUT_MD = ROOT / "docs/duplicate_text_review.md"

STATUS_CN = {
    "D01": "可能有效同文不同标签对照",
    "D02": "同文同标签但不同上下文，待复核",
    "D03": "疑似模板污染，优先删/重写/降权",
}

STATUS_ACTION = {
    "D01": "看上下文是否真的让同一句变成不同标签；如果成立，可保留为对照。",
    "D02": "看是否只是重复造句；如果上下文差异没有训练价值，建议删/重写/降权。",
    "D03": "优先判为模板污染候选；建议退回重写或后续从高质量训练集中剔除。",
}


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    return rows


def list_text(values: Any) -> str:
    if not isinstance(values, list) or not values:
        return "无"
    return "；".join(str(item) for item in values if str(item).strip()) or "无"


def context_lines(sample: dict[str, Any]) -> list[str]:
    context = sample.get("context", {})
    if not isinstance(context, dict):
        context = {}
    reply_chain = context.get("reply_chain", [])
    lines = [
        f"  - title：{context.get('title') or '无'}",
        f"  - description：{context.get('description') or '无'}",
        f"  - parent_comment（旧字段，默认不作强证据）：{context.get('parent_comment') or '无'}",
        f"  - reply_chain（旧字段，默认不作强证据）：{list_text(reply_chain)}",
        f"  - time：{context.get('time') or '无'}",
        f"  - topic：{context.get('topic') or '无'}",
    ]
    return lines


def reasoning_lines(sample: dict[str, Any]) -> list[str]:
    reasoning = sample.get("reasoning", {})
    if not isinstance(reasoning, dict):
        reasoning = {}
    return [
        f"  - supporting_evidence：{list_text(reasoning.get('supporting_evidence'))}",
        f"  - counter_evidence：{list_text(reasoning.get('counter_evidence'))}",
        f"  - final_rationale：{reasoning.get('final_rationale') or '无'}",
    ]


def render_sample(sample: dict[str, Any]) -> list[str]:
    flags = sample.get("context_audit_flag_codes", [])
    flag_text = "+".join(flags) if isinstance(flags, list) and flags else "none"
    lines = [
        f"#### `{sample['id']}`",
        "",
        f"- 标签：risk_level=`{sample.get('risk_level')}`；binary=`{sample.get('safety_binary_code')} / {sample.get('safety_binary')}`；hard_negative=`{str(sample.get('hard_negative')).lower()}`",
        f"- 编码：primary=`{sample.get('encoding_primary')}`；secondary=`{list_text(sample.get('encoding_secondary'))}`",
        f"- 上下文审计：class=`{sample.get('context_audit_class_code')} / {sample.get('context_audit_class')}`；flags=`{flag_text}`；duplicate=`{sample.get('duplicate_text_status_code')} / {sample.get('duplicate_text_status')}`",
        f"- context_required：`{str(sample.get('context_required')).lower()}`",
        "- 上下文：",
        *context_lines(sample),
        "- 关键 reasoning：",
        *reasoning_lines(sample),
        f"- review_notes：{sample.get('review_notes') or '无'}",
        "",
    ]
    return lines


def main() -> int:
    audit = json.loads(AUDIT_JSON.read_text(encoding="utf-8"))
    samples = {row["id"]: row for row in load_jsonl(COMBINED_PREVIEW_JSONL)}
    groups = audit["combined_duplicate_groups"]

    lines = [
        "# 重复文本人工复核清单",
        "",
        "本文件从正式 `data/processed/combined_candidates.jsonl` 的 860 条样本中抽取全部重复 text 组，共 53 组。",
        "",
        "这里是自包含复核版：每个重复组已经列出涉及样本的标签、上下文、审计码和关键 reasoning，不需要再回 860 条正式数据里逐个查。",
        "",
        "## 怎么判断",
        "",
        "- `D01`：可能是有效同文不同标签对照。重点看上下文是否真的改变标签。",
        "- `D02`：同文同标签但上下文不同。重点看这些上下文差异是否有训练价值，还是普通重复。",
        "- `D03`：疑似模板污染。优先考虑删、重写或降权。",
        "",
        "判断时先看同组样本的 `上下文` 部分：如果只是换了泛泛场景名，但同一句话、同一标签、同一推理逻辑都差不多，多半是重复或模板污染；如果上下文真的改变了含义，才值得保留为对照。",
        "",
        "最新策略：`parent_comment` / `reply_chain` 是旧字段，除非来自真实原始数据，否则默认不作为强证据。如果风险主要靠“像，但别展开”“别说像谁”“懂就别打全称”“缩写就行”等合成回复链成立，直接按模板污染、退回重写或降权处理。",
        "",
        "建议反馈格式：",
        "",
        "```text",
        "重复组 01：保留 / 删掉 / 退回重写 / 降权，原因……",
        "MEME_EXPAND_0026_MEDIUM：退回重写，原因……",
        "```",
        "",
        "## 全部重复组",
        "",
    ]

    for index, group in enumerate(groups, start=1):
        code = group.get("status_code", "")
        group_samples = [samples[sample_id] for sample_id in group["ids"]]
        lines.extend(
            [
                f"### 重复组 {index:02d}",
                "",
                f"- 状态：`{code}` / `{group.get('status')}` / {STATUS_CN.get(code, '待复核')}",
                f"- 出现次数：{group['count']}",
                f"- 重复文本：{group['text']}",
                f"- 风险分布：{json.dumps(group.get('risk_levels', {}), ensure_ascii=False)}",
                f"- 来源分布：{json.dumps(group.get('source_buckets', {}), ensure_ascii=False)}",
                f"- 建议动作：{STATUS_ACTION.get(code, '人工判断是否保留。')}",
                "",
                "#### 本组怎么审",
                "",
                "1. 先看文本本身是否足以判断。",
                "2. 再比较标题、时间、话题等非回复链上下文是否真的不同。",
                "3. 不要把合成的 `parent_comment/reply_chain` 当强证据。",
                "4. 如果只是换标题/平台/泛泛场景，或靠假回复链撑风险，结论倾向 `删掉`、`退回重写` 或 `降权`。",
                "5. 如果确实构成同文不同语境对照，结论可写 `保留对照`。",
                "",
                "#### 涉及样本详情",
                "",
            ]
        )
        for sample in group_samples:
            lines.extend(render_sample(sample))
        lines.extend(["- 复核结论：待填写", ""])

    OUTPUT_MD.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    print(f"Wrote {len(groups)} duplicate groups to {OUTPUT_MD}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
