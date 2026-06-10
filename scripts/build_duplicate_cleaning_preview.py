#!/usr/bin/env python3
"""Build a conservative duplicate-text cleaning preview from human feedback.

The preview never modifies official processed data in place. It removes or
keeps duplicate rows according to human review, and records label-change
suggestions as metadata instead of rewriting core labels automatically.
"""

from __future__ import annotations

import json
from collections import Counter
from copy import deepcopy
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
PROCESSED_JSONL = ROOT / "data/processed/combined_candidates.jsonl"
FEEDBACK_JSON = ROOT / "data/raw/duplicate_text_human_feedback.json"
PREVIEW_JSONL = ROOT / "data/processed/combined_candidates_duplicate_cleaning_preview.jsonl"
PREVIEW_JSON = ROOT / "data/processed/combined_candidates_duplicate_cleaning_preview.json"
REWRITE_JSON = ROOT / "data/raw/duplicate_text_rewrite_candidates.json"
REPORT_JSON = ROOT / "data/processed/duplicate_cleaning_preview_report.json"
REPORT_MD = ROOT / "docs/duplicate_cleaning_preview.md"

SUGGESTED_RISK_BY_DECISION = {
    "keep_relabel_high_no_context": "high",
    "keep_one_relabel_high": "high",
    "keep_relabel_medium_no_context": "medium",
    "keep_one_relabel_none": "none",
    "keep_relabel_none": "none",
    "keep_one_relabel_medium_or_high_style_statement": "medium_or_high",
    "keep_relabel_medium_or_high": "medium_or_high",
    "keep_one_relabel_high_no_reasoning_needed": "high",
    "keep_relabel_high_style_issue": "high",
    "keep_one_high": "high",
    "delete_or_relabel_none_low": "none_or_low",
}


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
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


def write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False, separators=(",", ":")) + "\n")


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2), encoding="utf-8")


def load_feedback() -> list[dict[str, Any]]:
    payload = json.loads(FEEDBACK_JSON.read_text(encoding="utf-8"))
    return payload["records"]


def choose_keep_ids(record: dict[str, Any]) -> set[str]:
    sample_ids = record["sample_ids"]
    action = record["normalized_action"]
    decision = record["human_decision"]

    if action == "delete_or_exclude":
        return set()
    if action == "rewrite":
        return set()
    if decision.startswith("keep_group"):
        return set(sample_ids)
    return {sample_ids[0]}


def append_note(existing: Any, addition: str) -> str:
    existing_text = str(existing or "").strip()
    if not existing_text:
        return addition
    return f"{existing_text}; {addition}"


def enrich_kept_row(row: dict[str, Any], record: dict[str, Any], keep_scope: str) -> dict[str, Any]:
    result = deepcopy(row)
    suggested_risk = SUGGESTED_RISK_BY_DECISION.get(record["human_decision"], "")
    result["duplicate_human_review_group"] = record["group"]
    result["duplicate_human_decision"] = record["human_decision"]
    result["duplicate_cleaning_action"] = "keep_after_duplicate_review"
    result["duplicate_keep_scope"] = keep_scope
    if suggested_risk:
        result["suggested_risk_level"] = suggested_risk
    result["review_notes"] = append_note(
        result.get("review_notes", ""),
        (
            f"duplicate_human_review_group={record['group']}; "
            f"duplicate_human_decision={record['human_decision']}; "
            f"duplicate_cleaning_action=keep_after_duplicate_review"
            + (f"; suggested_risk_level={suggested_risk}" if suggested_risk else "")
        ),
    )
    return result


def build_plan(records: list[dict[str, Any]]) -> tuple[dict[str, dict[str, Any]], list[dict[str, Any]]]:
    id_plan: dict[str, dict[str, Any]] = {}
    rewrite_candidates: list[dict[str, Any]] = []

    for record in records:
        keep_ids = choose_keep_ids(record)
        sample_ids = record["sample_ids"]
        keep_scope = "keep_group" if len(keep_ids) > 1 else "keep_one"
        for sample_id in sample_ids:
            if sample_id in keep_ids:
                id_plan[sample_id] = {"action": "keep", "record": record, "keep_scope": keep_scope}
            else:
                id_plan[sample_id] = {"action": "remove", "record": record, "keep_scope": "removed_duplicate"}
        if record["normalized_action"] == "rewrite":
            rewrite_candidates.append(record)

    return id_plan, rewrite_candidates


def build_preview(rows: list[dict[str, Any]], id_plan: dict[str, dict[str, Any]]) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    preview: list[dict[str, Any]] = []
    removed: list[dict[str, Any]] = []

    for row in rows:
        sample_id = str(row.get("id", ""))
        plan = id_plan.get(sample_id)
        if not plan:
            preview.append(row)
            continue

        record = plan["record"]
        if plan["action"] == "remove":
            removed.append(
                {
                    "id": sample_id,
                    "group": record["group"],
                    "human_decision": record["human_decision"],
                    "normalized_action": record["normalized_action"],
                    "text": row.get("text", ""),
                    "risk_level": row.get("risk_level", ""),
                    "user_comment": record["user_comment"],
                }
            )
            continue

        preview.append(enrich_kept_row(row, record, str(plan["keep_scope"])))

    return preview, removed


def render_report(report: dict[str, Any]) -> str:
    lines = [
        "# 重复文本清洗预览",
        "",
        "本报告基于 `data/raw/duplicate_text_human_feedback.json` 生成，只是预览，不修改正式 `data/processed/combined_candidates.*`。",
        "",
        "## 总览",
        "",
        f"- 输入正式样本：{report['input_rows']}",
        f"- 预览输出样本：{report['preview_rows']}",
        f"- 预览删除样本：{report['removed_rows']}",
        f"- 需重写组数：{report['rewrite_group_count']}",
        f"- 保留样本中的标签建议数：{report['suggested_label_change_rows']}",
        "",
        "## 删除/保留动作",
        "",
        "| action | count |",
        "|---|---:|",
    ]
    for action, count in report["removed_by_action"].items():
        lines.append(f"| `{action}` removed | {count} |")
    lines.extend(
        [
            "",
            "## 需重写组",
            "",
        ]
    )
    if not report["rewrite_candidates"]:
        lines.append("- 无")
    else:
        for item in report["rewrite_candidates"]:
            lines.append(
                f"- 重复组 {item['group']:02d}：`{item['human_decision']}`；{item['duplicate_text']}；{item['user_comment']}"
            )
    lines.extend(
        [
            "",
            "## 输出文件",
            "",
            "- `data/processed/combined_candidates_duplicate_cleaning_preview.jsonl`",
            "- `data/processed/combined_candidates_duplicate_cleaning_preview.json`",
            "- `data/raw/duplicate_text_rewrite_candidates.json`",
            "- `data/processed/duplicate_cleaning_preview_report.json`",
            "",
            "下一步：人工确认本预览后，才能考虑 apply 到正式 processed，并重建 SFT/split。",
        ]
    )
    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    rows = load_jsonl(PROCESSED_JSONL)
    records = load_feedback()
    id_plan, rewrite_records = build_plan(records)
    preview, removed = build_preview(rows, id_plan)

    ids = [str(row.get("id", "")) for row in preview]
    duplicate_ids = [item for item, count in Counter(ids).items() if count > 1]
    if duplicate_ids:
        raise ValueError(f"Duplicate ids in preview: {duplicate_ids[:10]}")

    rewrite_jsonl_rows = [
        {
            "group": record["group"],
            "duplicate_text": record["duplicate_text"],
            "sample_ids": record["sample_ids"],
            "human_decision": record["human_decision"],
            "human_decision_label": record["human_decision_label"],
            "user_comment": record["user_comment"],
        }
        for record in rewrite_records
    ]
    suggested_label_change_rows = [
        row
        for row in preview
        if "suggested_risk_level" in row
    ]
    report = {
        "input_rows": len(rows),
        "preview_rows": len(preview),
        "removed_rows": len(removed),
        "removed_by_action": dict(Counter(item["normalized_action"] for item in removed).most_common()),
        "removed": removed,
        "rewrite_group_count": len(rewrite_records),
        "rewrite_candidates": rewrite_jsonl_rows,
        "suggested_label_change_rows": len(suggested_label_change_rows),
        "suggested_label_change_ids": [
            {
                "id": row["id"],
                "suggested_risk_level": row["suggested_risk_level"],
                "current_risk_level": row["risk_level"],
                "group": row["duplicate_human_review_group"],
            }
            for row in suggested_label_change_rows
        ],
    }

    write_jsonl(PREVIEW_JSONL, preview)
    write_json(PREVIEW_JSON, preview)
    write_json(REWRITE_JSON, rewrite_jsonl_rows)
    write_json(REPORT_JSON, report)
    REPORT_MD.write_text(render_report(report), encoding="utf-8")

    print(f"Input rows: {len(rows)}")
    print(f"Preview rows: {len(preview)}")
    print(f"Removed rows: {len(removed)}")
    print(f"Rewrite groups: {len(rewrite_records)}")
    print(f"Suggested label changes: {len(suggested_label_change_rows)}")
    print(f"Wrote {PREVIEW_JSONL}")
    print(f"Wrote {REPORT_MD}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
