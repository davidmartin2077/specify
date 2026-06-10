#!/usr/bin/env python3
"""Record human feedback for the 53 duplicate-text review groups."""

from __future__ import annotations

import json
from collections import Counter
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
AUDIT_JSON = ROOT / "data/raw/context_requirement_audit.json"
OUTPUT_JSON = ROOT / "data/raw/duplicate_text_human_feedback.json"
OUTPUT_MD = ROOT / "docs/duplicate_text_human_feedback.md"


FEEDBACK: list[dict[str, Any]] = [
    {
        "group": 1,
        "decision": "rewrite_keep_one",
        "user_comment": "退回重写，且保留一条就够了。nb 是鞋款本身就是在对 nb 做解释，文本可以变成“这块 nb 真好看”，然后解读 nb 对意思，也就是这里出现的是审核视角的词，并非评论本身。其实这个例子很好，nb 可以理解成牛逼，可以理解成新百伦，但就是样例不太行。",
    },
    {"group": 2, "decision": "delete_group", "user_comment": "模板污染了，删。"},
    {"group": 3, "decision": "keep_one_delete_duplicates", "user_comment": "评论很好，但是上下文重复，删掉两个保留一个。"},
    {"group": 4, "decision": "delete_group", "user_comment": "模板污染，没有营养的训练，删掉。"},
    {"group": 5, "decision": "keep_one_delete_duplicates", "user_comment": "删 2 留 1。"},
    {"group": 6, "decision": "delete_group", "user_comment": "模板污染，都不要。"},
    {"group": 7, "decision": "delete_group", "user_comment": "不要了，质量不高。"},
    {"group": 8, "decision": "delete_group", "user_comment": "病句，不要。"},
    {"group": 9, "decision": "delete_or_rewrite", "user_comment": "审核员视角，且模板污染。"},
    {"group": 10, "decision": "keep_relabel_medium_or_high", "user_comment": "上下文没意义，评论本身很有意思，留着，判断为 medium 甚至 high 都没问题。"},
    {"group": 11, "decision": "delete_or_relabel_none_low", "user_comment": "模板污染，判 none 或者 low 都没问题。"},
    {"group": 12, "decision": "keep_one_delete_duplicates", "user_comment": "没什么问题，删除重复的，留一组。"},
    {"group": 13, "decision": "delete_group", "user_comment": "质量不高，删了吧。"},
    {"group": 14, "decision": "keep_relabel_high_no_context", "user_comment": "评论很有意思，但是上下文之类的可以不带，这个可以判 high 了，一眼都知道 64。"},
    {"group": 15, "decision": "delete_group", "user_comment": "不要了，质量不高。"},
    {"group": 16, "decision": "delete_group", "user_comment": "病句，不要。"},
    {"group": 17, "decision": "keep_one_relabel_high", "user_comment": "直接辱党，直接判 high，留一个。"},
    {"group": 18, "decision": "keep_one_relabel_none", "user_comment": "可以，但是判 none 就行，很日常的话。"},
    {"group": 19, "decision": "keep_relabel_medium_no_context", "user_comment": "例子可以，但是这句话也不用看上下文。但是在评论区说弹幕莫名其妙说自己生日也挺抽象的，判个中吧。"},
    {"group": 20, "decision": "delete_group", "user_comment": "质量不高，都不要了。"},
    {"group": 21, "decision": "delete_group", "user_comment": "质量不高。"},
    {"group": 22, "decision": "delete_or_rewrite", "user_comment": "审核视角，建议不要或者重写。"},
    {"group": 23, "decision": "keep_one_delete_duplicates", "user_comment": "没什么问题，删 2 留 1。"},
    {"group": 24, "decision": "delete_group", "user_comment": "质量不高。"},
    {"group": 25, "decision": "keep_one", "user_comment": "很有意思一个评论，留 1 个。"},
    {"group": 26, "decision": "keep_relabel_high_style_issue", "user_comment": "像个陈述句，不像是出现在弹幕和评论里的话，但是本身判 high 没毛病。"},
    {"group": 27, "decision": "keep_one", "user_comment": "没什么问题，留一个。"},
    {"group": 28, "decision": "keep_one_style_statement", "user_comment": "陈述句，留一个。"},
    {"group": 29, "decision": "keep_one_high", "user_comment": "直接高风险，留一个。"},
    {"group": 30, "decision": "keep_one", "user_comment": "没什么问题，留一个。"},
    {"group": 31, "decision": "keep_one_relabel_high_no_reasoning_needed", "user_comment": "看到卖车包子直接 high，不需要任何逻辑。"},
    {"group": 32, "decision": "delete_group", "user_comment": "病句，删了不要。"},
    {"group": 33, "decision": "keep_one_relabel_none", "user_comment": "判 none 没问题，留一个即可。"},
    {"group": 34, "decision": "keep_group", "user_comment": "没毛病。"},
    {"group": 35, "decision": "delete_group", "user_comment": "病句不要。"},
    {"group": 36, "decision": "delete_group", "user_comment": "病句不要。"},
    {"group": 37, "decision": "keep_one_relabel_none", "user_comment": "None 留一个。"},
    {"group": 38, "decision": "keep_one_relabel_none", "user_comment": "None 留一个。"},
    {"group": 39, "decision": "delete_or_rewrite", "user_comment": "审核员语气，模板污染。"},
    {"group": 40, "decision": "keep_relabel_none", "user_comment": "直接判 none 没问题。"},
    {"group": 41, "decision": "delete_group", "user_comment": "病句不要。"},
    {"group": 42, "decision": "rewrite_group", "user_comment": "病句，重写，不像正常评论。"},
    {"group": 43, "decision": "keep_one_relabel_medium_or_high_style_statement", "user_comment": "陈述句，但是评论本身可以当作中或者高，留一个。"},
    {"group": 44, "decision": "keep_group", "user_comment": "没问题，留。"},
    {"group": 45, "decision": "keep_one", "user_comment": "留一个。"},
    {"group": 46, "decision": "delete_group", "user_comment": "病句，模板污染，不要了。"},
    {"group": 47, "decision": "keep_one", "user_comment": "没问题，留一个。"},
    {"group": 48, "decision": "keep_one_relabel_high", "user_comment": "这个可以，可以判 high，并且留一个。"},
    {"group": 49, "decision": "keep_group_style_statement", "user_comment": "陈述句，本身没问题。"},
    {"group": 50, "decision": "delete_group", "user_comment": "低质量，不要。"},
    {"group": 51, "decision": "keep_one", "user_comment": "留一个。"},
    {"group": 52, "decision": "rewrite_style_statement", "user_comment": "陈述句，以后少点这种陈述句行不行，跟说明书一样。"},
    {"group": 53, "decision": "keep_one", "user_comment": "留一个。"},
]


DECISION_LABELS = {
    "rewrite_keep_one": "退回重写，最多保留一条",
    "delete_group": "整组删除/不进入高质量训练集",
    "keep_one_delete_duplicates": "留一条，删除重复项",
    "delete_or_rewrite": "删除或重写",
    "keep_relabel_medium_or_high": "保留，标签可调 medium/high",
    "delete_or_relabel_none_low": "删除，或仅作 none/low 边界",
    "keep_relabel_high_no_context": "保留，改 high，不需要上下文",
    "keep_one_relabel_high": "留一条，改 high",
    "keep_one_relabel_none": "留一条，改 none",
    "keep_relabel_medium_no_context": "保留，改 medium，不需要上下文",
    "keep_one": "留一条",
    "keep_relabel_high_style_issue": "保留或重写风格，风险可 high",
    "keep_one_style_statement": "留一条，但注意陈述句风格",
    "keep_one_high": "留一条，高风险",
    "keep_one_relabel_high_no_reasoning_needed": "留一条，直接 high",
    "keep_group": "保留",
    "keep_relabel_none": "保留，改 none",
    "rewrite_group": "整组重写",
    "keep_one_relabel_medium_or_high_style_statement": "留一条，可改 medium/high，但注意陈述句风格",
    "keep_group_style_statement": "保留，但注意陈述句风格",
    "rewrite_style_statement": "重写陈述句风格",
}


def load_groups() -> list[dict[str, Any]]:
    audit = json.loads(AUDIT_JSON.read_text(encoding="utf-8"))
    return audit["combined_duplicate_groups"]


def normalized_action(decision: str) -> str:
    if decision.startswith("delete"):
        return "delete_or_exclude"
    if "rewrite" in decision:
        return "rewrite"
    if "relabel" in decision:
        return "keep_with_label_change"
    if decision.startswith("keep"):
        return "keep_or_keep_one"
    return "review"


def build_records(groups: list[dict[str, Any]]) -> list[dict[str, Any]]:
    by_group = {item["group"]: item for item in FEEDBACK}
    records: list[dict[str, Any]] = []
    for index, group in enumerate(groups, start=1):
        feedback = by_group[index]
        decision = feedback["decision"]
        records.append(
            {
                "group": index,
                "duplicate_text": group["text"],
                "sample_ids": group["ids"],
                "audit_status_code": group.get("status_code"),
                "audit_status": group.get("status"),
                "risk_levels": group.get("risk_levels", {}),
                "human_decision": decision,
                "human_decision_label": DECISION_LABELS[decision],
                "normalized_action": normalized_action(decision),
                "user_comment": feedback["user_comment"],
            }
        )
    return records


def render_markdown(records: list[dict[str, Any]]) -> str:
    action_counts = Counter(record["normalized_action"] for record in records)
    decision_counts = Counter(record["human_decision"] for record in records)
    lines = [
        "# 重复文本人工复核反馈",
        "",
        "本文件记录用户对 `docs/duplicate_text_review.md` 中 53 个重复文本组的人工复核结论。",
        "",
        "本反馈只作为清洗依据，不直接修改正式 `data/processed/combined_candidates.*`。",
        "",
        "## 总体倾向",
        "",
        f"- 复核组数：{len(records)}",
        f"- 删除/排除倾向：{action_counts.get('delete_or_exclude', 0)} 组",
        f"- 重写倾向：{action_counts.get('rewrite', 0)} 组",
        f"- 保留但改标签倾向：{action_counts.get('keep_with_label_change', 0)} 组",
        f"- 保留或留一条倾向：{action_counts.get('keep_or_keep_one', 0)} 组",
        "",
        "## 主要复核原则",
        "",
        "1. 合成回复链不再作为强证据，风险主要靠回复链成立的样本按模板污染处理。",
        "2. `nb`、`64`、`卖车包子` 这类评论本身可读、有真实评论感的样本可以保留或重写。",
        "3. 病句、审核员视角、说明书式陈述句、模板化上下文优先删除、重写或降权。",
        "4. 重复文本不必全留，很多组只留一个代表样本即可。",
        "",
        "## 决策分布",
        "",
        "| decision | count |",
        "|---|---:|",
    ]
    for decision, count in decision_counts.most_common():
        lines.append(f"| `{decision}` / {DECISION_LABELS[decision]} | {count} |")

    lines.extend(["", "## 逐组反馈", ""])
    for record in records:
        lines.extend(
            [
                f"### 重复组 {record['group']:02d}",
                "",
                f"- 重复文本：{record['duplicate_text']}",
                f"- 样本 ID：{', '.join(f'`{sample_id}`' for sample_id in record['sample_ids'])}",
                f"- 原审计：`{record['audit_status_code']}` / `{record['audit_status']}`",
                f"- 风险分布：{json.dumps(record['risk_levels'], ensure_ascii=False)}",
                f"- 人工结论：`{record['human_decision']}` / {record['human_decision_label']}",
                f"- 归一动作：`{record['normalized_action']}`",
                f"- 用户反馈：{record['user_comment']}",
                "",
            ]
        )
    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    groups = load_groups()
    if len(groups) != len(FEEDBACK):
        raise ValueError(f"Expected {len(groups)} feedback items, got {len(FEEDBACK)}.")
    records = build_records(groups)
    payload = {
        "source_review_file": "docs/duplicate_text_review.md",
        "status": "human_review_recorded",
        "records": records,
    }
    OUTPUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    OUTPUT_MD.write_text(render_markdown(records), encoding="utf-8")
    print(f"Wrote {len(records)} feedback records to {OUTPUT_JSON}")
    print(f"Wrote readable feedback to {OUTPUT_MD}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
