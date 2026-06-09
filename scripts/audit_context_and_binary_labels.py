#!/usr/bin/env python3
"""Audit context dependency and build binary-label/eval previews.

This script is deliberately read-only for official processed data. It writes
audit artifacts and preview datasets that can be reviewed before any schema or
training-data migration.
"""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter, defaultdict
from copy import deepcopy
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
COMBINED_INPUT = ROOT / "data/processed/combined_candidates.jsonl"
EXTERNAL_INPUT = ROOT / "data/raw/external_safety_import_preview.jsonl"

AUDIT_JSON = ROOT / "data/raw/context_requirement_audit.json"
AUDIT_MD = ROOT / "docs/context_requirement_audit.md"
COMBINED_BINARY_JSONL = ROOT / "data/raw/combined_candidates_binary_preview.jsonl"
EXTERNAL_BINARY_JSONL = ROOT / "data/raw/external_safety_binary_preview.jsonl"
RISK_EVAL_JSONL = ROOT / "data/eval/risk_test_preview.jsonl"
NORMAL_EVAL_JSONL = ROOT / "data/eval/normal_test_preview.jsonl"

DIRECT_RISK_TERMS = (
    "强奸",
    "杀",
    "弄死",
    "家暴",
    "骚扰",
    "出货",
    "下单",
    "包过",
    "盘口",
    "下注",
    "网赌",
    "代充",
    "实名料",
    "开盒",
    "炸群",
    "木马",
    "破解",
    "枪",
    "刀",
    "炸药",
    "未成年",
    "裸",
    "约炮",
    "毒品",
    "冰",
    "麻",
)

CONTEXTUAL_ENCODING_MARKERS = (
    "E2_",
    "E3_",
    "C1_",
    "C2_",
    "C3_",
    "C4_",
    "D1_",
    "D2_",
    "D3_",
    "F_",
)

GENERIC_CONTEXT_PATTERNS = (
    "外部真实评论样本",
    "原始样本，尚未补充完整评论链",
    "社会趋势讨论话题",
    "争议视频评论区",
    "旧照片转发",
    "公共事件回顾剪辑",
    "热搜评论区",
    "普通生活帖",
    "课程/教程内容",
    "商品/美食测评",
    "美食/文具/娱乐分享",
)

PLACEHOLDER_CONTEXT_VALUES = {
    "",
    "无",
    "none",
    "null",
    "未知",
    "未提供",
    "无额外上下文",
    "暂无",
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
                raise ValueError(f"{path}:{line_number}: expected JSON object")
            rows.append(value)
    return rows


def write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False, sort_keys=False) + "\n")


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2), encoding="utf-8")


def normalize_text(text: str) -> str:
    return re.sub(r"\s+", "", text).lower()


def parse_notes(notes: Any) -> dict[str, str]:
    parsed: dict[str, str] = {}
    if not isinstance(notes, str):
        return parsed
    for part in notes.split(";"):
        part = part.strip()
        if "=" not in part:
            continue
        key, value = part.split("=", 1)
        parsed[key.strip()] = value.strip()
    return parsed


def source_bucket(sample_id: str, notes: str) -> str:
    if sample_id.startswith("EXT_"):
        parsed = parse_notes(notes)
        return parsed.get("source", "external")
    if sample_id.startswith("GROK_"):
        return "grok"
    if sample_id.startswith("USER_"):
        return "user"
    if sample_id.startswith("MEME_EXPAND_"):
        return "meme_expansion"
    if sample_id.startswith("GEMINI_EXPAND_"):
        return "gemini_expansion"
    if sample_id.startswith("LEXICON_SEED_"):
        return "sensitive_lexicon_seed"
    if sample_id.startswith("PHASE2_SEED_"):
        return "phase2_seed"
    if sample_id.startswith("PHASE3_W1_"):
        return "phase3_first_wave"
    if sample_id.startswith("PHASE3_W2_"):
        return "phase3_second_wave"
    return "unknown"


def context_values(sample: dict[str, Any]) -> dict[str, Any]:
    context = sample.get("context")
    return context if isinstance(context, dict) else {}


def non_empty_context_fields(sample: dict[str, Any]) -> list[str]:
    context = context_values(sample)
    fields: list[str] = []
    for field in ("title", "description", "parent_comment", "time", "topic"):
        value = str(context.get(field, "")).strip()
        if value and value.lower() not in PLACEHOLDER_CONTEXT_VALUES:
            fields.append(field)
    reply_chain = context.get("reply_chain")
    if isinstance(reply_chain, list) and any(str(item).strip() for item in reply_chain):
        fields.append("reply_chain")
    return fields


def joined_context(sample: dict[str, Any]) -> str:
    context = context_values(sample)
    parts: list[str] = []
    for field in ("title", "description", "parent_comment", "time", "topic"):
        value = str(context.get(field, "")).strip()
        if value:
            parts.append(value)
    reply_chain = context.get("reply_chain")
    if isinstance(reply_chain, list):
        parts.extend(str(item).strip() for item in reply_chain if str(item).strip())
    return "；".join(parts)


def reasoning_text(sample: dict[str, Any]) -> str:
    reasoning = sample.get("reasoning", {})
    if not isinstance(reasoning, dict):
        return ""
    parts: list[str] = []
    for value in reasoning.values():
        if isinstance(value, list):
            parts.extend(str(item) for item in value)
        else:
            parts.append(str(value))
    return "；".join(parts)


def has_direct_risk_signal(sample: dict[str, Any]) -> bool:
    text = str(sample.get("text", ""))
    if any(term in text for term in DIRECT_RISK_TERMS):
        return True
    risk_level = sample.get("risk_level")
    encoding_primary = str(sample.get("encoding_primary", ""))
    evidence_strength = sample.get("evidence_strength")
    if risk_level == "high" and evidence_strength == "strong" and encoding_primary == "literal_keyword":
        return True
    if risk_level == "high" and sample.get("ambiguity") == "low":
        return True
    return False


def has_contextual_signal(sample: dict[str, Any]) -> bool:
    encoding_values = [str(sample.get("encoding_primary", ""))]
    secondary = sample.get("encoding_secondary")
    if isinstance(secondary, list):
        encoding_values.extend(str(item) for item in secondary)
    encoding_text = " ".join(encoding_values)
    if any(marker in encoding_text for marker in CONTEXTUAL_ENCODING_MARKERS):
        return True
    context_text = joined_context(sample)
    if any(marker in context_text for marker in ("时间线", "日期", "回复", "楼上", "楼下", "别写全", "别打全称")):
        return True
    if len(non_empty_context_fields(sample)) >= 3:
        return True
    return False


def context_flags(sample: dict[str, Any], dataset: str) -> list[str]:
    flags: list[str] = []
    fields = non_empty_context_fields(sample)
    context_text = joined_context(sample)
    reasoning = reasoning_text(sample)

    if sample.get("context_required") is True and not fields:
        flags.append("context_required_but_empty")
    if sample.get("context_required") is True and fields == ["title"] and sample.get("risk_level") in {"high", "medium"}:
        flags.append("context_required_only_title")
    if any(pattern in context_text for pattern in GENERIC_CONTEXT_PATTERNS):
        flags.append("generic_or_template_context")
    if "外部真实评论样本" in context_text or "尚未补充完整评论链" in context_text:
        flags.append("external_placeholder_context")
    if (
        sample.get("context_required") is True
        and has_direct_risk_signal(sample)
        and not has_contextual_signal(sample)
    ):
        flags.append("likely_direct_no_context")
    if (
        sample.get("context_required") is True
        and sample.get("risk_level") == "none"
        and sample.get("hard_negative") is True
        and has_direct_risk_signal(sample) is False
    ):
        flags.append("safe_sample_context_may_be_optional")
    if "判断依赖标题、回复链或时间节点" in reasoning and len(fields) <= 1:
        flags.append("reasoning_claims_context_but_context_thin")
    if dataset == "external" and sample.get("context_required") is True and "external_placeholder_context" in flags:
        flags.append("do_not_invent_context_review_needed")
    return flags


def context_bucket(sample: dict[str, Any], flags: list[str]) -> str:
    risk_level = sample.get("risk_level")
    if risk_level == "none":
        return "safe_without_context"
    if has_contextual_signal(sample) and "likely_direct_no_context" not in flags:
        return "contextual_required"
    return "direct_no_context"


def safety_binary(sample: dict[str, Any]) -> str:
    return "safe" if sample.get("risk_level") == "none" else "unsafe"


def binary_preview_row(sample: dict[str, Any], dataset: str, duplicate_status: str) -> dict[str, Any]:
    row = deepcopy(sample)
    flags = context_flags(sample, dataset)
    bucket = context_bucket(sample, flags)
    row["safety_binary"] = safety_binary(sample)
    row["context_audit_class"] = bucket
    row["context_audit_flags"] = flags
    row["duplicate_text_status"] = duplicate_status
    row["review_notes"] = (
        f"{row.get('review_notes', '')}; "
        f"context_audit_class={bucket}; safety_binary={row['safety_binary']}; "
        f"duplicate_text_status={duplicate_status}; preview_only=true"
    ).strip("; ")
    return row


def duplicate_statuses(rows: list[dict[str, Any]]) -> dict[str, str]:
    by_text: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        by_text[normalize_text(str(row.get("text", "")))].append(row)

    statuses: dict[str, str] = {}
    for group in by_text.values():
        if len(group) == 1:
            statuses[str(group[0]["id"])] = "unique"
            continue
        contexts = {normalize_text(joined_context(row)) for row in group}
        risk_levels = {str(row.get("risk_level", "")) for row in group}
        encodings = {str(row.get("encoding_primary", "")) for row in group}
        if len(risk_levels) > 1:
            status = "effective_contrast_candidate"
        elif len(contexts) > 1 and len(encodings) <= 2:
            status = "same_text_different_context_review"
        else:
            status = "template_pollution_candidate"
        for row in group:
            statuses[str(row["id"])] = status
    return statuses


def duplicate_group_report(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    by_text: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        by_text[normalize_text(str(row.get("text", "")))].append(row)

    groups: list[dict[str, Any]] = []
    statuses = duplicate_statuses(rows)
    for group in by_text.values():
        if len(group) < 2:
            continue
        first = group[0]
        groups.append(
            {
                "text": first.get("text", ""),
                "count": len(group),
                "status": statuses[str(first["id"])],
                "ids": [row.get("id", "") for row in group],
                "risk_levels": dict(Counter(str(row.get("risk_level", "")) for row in group).most_common()),
                "source_buckets": dict(
                    Counter(source_bucket(str(row.get("id", "")), str(row.get("review_notes", ""))) for row in group).most_common()
                ),
            }
        )
    return sorted(groups, key=lambda item: (-int(item["count"]), str(item["text"])))


def build_previews(
    combined_rows: list[dict[str, Any]],
    external_rows: list[dict[str, Any]],
) -> tuple[list[dict[str, Any]], list[dict[str, Any]], dict[str, Any]]:
    combined_duplicate_status = duplicate_statuses(combined_rows)
    external_duplicate_status = duplicate_statuses(external_rows)

    combined_preview = [
        binary_preview_row(row, "combined", combined_duplicate_status[str(row["id"])]) for row in combined_rows
    ]
    external_preview = [
        binary_preview_row(row, "external", external_duplicate_status[str(row["id"])]) for row in external_rows
    ]

    all_preview = [*combined_preview, *external_preview]
    audit_items = [
        {
            "id": row["id"],
            "dataset": "external" if str(row["id"]).startswith("EXT_") else "combined",
            "source_bucket": source_bucket(str(row["id"]), str(row.get("review_notes", ""))),
            "risk_level": row.get("risk_level"),
            "safety_binary": row["safety_binary"],
            "context_required": row.get("context_required"),
            "context_audit_class": row["context_audit_class"],
            "context_audit_flags": row["context_audit_flags"],
            "duplicate_text_status": row["duplicate_text_status"],
            "text": row.get("text", ""),
            "context_fields": non_empty_context_fields(row),
        }
        for row in all_preview
    ]

    audit = {
        "inputs": {
            "combined": str(COMBINED_INPUT.relative_to(ROOT)),
            "external": str(EXTERNAL_INPUT.relative_to(ROOT)),
        },
        "counts": {
            "combined": len(combined_rows),
            "external": len(external_rows),
            "total": len(all_preview),
        },
        "binary_counts": dict(Counter(row["safety_binary"] for row in all_preview).most_common()),
        "context_audit_class_counts": dict(Counter(row["context_audit_class"] for row in all_preview).most_common()),
        "context_flag_counts": dict(
            Counter(flag for row in all_preview for flag in row["context_audit_flags"]).most_common()
        ),
        "combined_duplicate_groups": duplicate_group_report(combined_rows),
        "external_duplicate_groups": duplicate_group_report(external_rows),
        "source_breakdown": source_breakdown(all_preview),
        "audit_items": audit_items,
        "threshold_recommendation": {
            "phase1_risk_test_unsafe_recall_target": "80%-90%+",
            "phase1_normal_test_false_positive_tolerance": "about 30%",
            "note": "Use the binary previews for recall/false-positive measurement, while preserving risk_level and reasoning for governance and explanation.",
        },
    }
    return combined_preview, external_preview, audit


def source_breakdown(rows: list[dict[str, Any]]) -> dict[str, Any]:
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        grouped[source_bucket(str(row.get("id", "")), str(row.get("review_notes", "")))].append(row)

    output: dict[str, Any] = {}
    for source, items in sorted(grouped.items()):
        output[source] = {
            "count": len(items),
            "risk_level": dict(Counter(str(row.get("risk_level", "")) for row in items).most_common()),
            "safety_binary": dict(Counter(row["safety_binary"] for row in items).most_common()),
            "context_audit_class": dict(Counter(row["context_audit_class"] for row in items).most_common()),
            "flags": dict(Counter(flag for row in items for flag in row["context_audit_flags"]).most_common()),
        }
    return output


def eval_row(row: dict[str, Any], eval_name: str) -> dict[str, Any]:
    copied = deepcopy(row)
    copied["split"] = "eval"
    copied["eval_set"] = eval_name
    copied["eval_target"] = "unsafe_recall" if eval_name == "risk_test_preview" else "false_positive_rate"
    copied["review_notes"] = f"{copied.get('review_notes', '')}; eval_preview=true; eval_set={eval_name}".strip("; ")
    return copied


def build_eval_previews(combined_preview: list[dict[str, Any]], external_preview: list[dict[str, Any]]) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    all_rows = [*combined_preview, *external_preview]
    risk_rows = [eval_row(row, "risk_test_preview") for row in all_rows if row["safety_binary"] == "unsafe"]
    normal_rows = [
        eval_row(row, "normal_test_preview")
        for row in all_rows
        if row["safety_binary"] == "safe" or row.get("hard_negative") is True
    ]
    return risk_rows, normal_rows


def render_md(audit: dict[str, Any]) -> str:
    counts = audit["counts"]
    binary = audit["binary_counts"]
    classes = audit["context_audit_class_counts"]
    flags = audit["context_flag_counts"]
    duplicate_groups = audit["combined_duplicate_groups"]
    duplicate_status_counts = Counter(group["status"] for group in duplicate_groups)

    lines = [
        "# 上下文依赖与二元安全标签审计",
        "",
        "本报告只审计并生成预览，不修改正式 `data/processed/combined_candidates.jsonl`，也不把外部 340 条入库。",
        "",
        "## 输入范围",
        "",
        f"- 正式 processed：{counts['combined']} 条",
        f"- 外部 raw 预览：{counts['external']} 条",
        f"- 合计：{counts['total']} 条",
        "",
        "## 二元标签预览",
        "",
        "| binary | count |",
        "|---|---:|",
    ]
    for key, value in binary.items():
        lines.append(f"| {key} | {value} |")

    lines.extend(
        [
            "",
            "规则：`high/medium/low -> unsafe`，`none -> safe`。二元标签用于封杀率/召回评测，多级 `risk_level` 继续用于解释、分层治理和人工复核。",
            "",
            "## 上下文依赖分层",
            "",
            "| class | count |",
            "|---|---:|",
        ]
    )
    for key, value in classes.items():
        lines.append(f"| {key} | {value} |")

    lines.extend(
        [
            "",
            "- `direct_no_context`：单条文本本身已有足够风险信号，后续不应硬编标题、上级评论或回复链。",
            "- `contextual_required`：需要标题、上级评论、时间、话题或回复链才能支撑当前风险解释。",
            "- `safe_without_context`：单条文本正常或外部标签安全，不应为凑 schema 强行制造风险语境。",
            "",
            "## 主要审计标记",
            "",
            "| flag | count |",
            "|---|---:|",
        ]
    )
    for key, value in flags.items():
        lines.append(f"| {key} | {value} |")

    lines.extend(
        [
            "",
            "这些标记是启发式，不是自动判错。优先人工复核 `external_placeholder_context`、`likely_direct_no_context` 和 `reasoning_claims_context_but_context_thin`。",
            "",
            "## 重复文本判断",
            "",
            f"- 正式 860 条重复 text 组：{len(duplicate_groups)}",
            f"- 疑似有效同文不同语境对照：{duplicate_status_counts.get('effective_contrast_candidate', 0)} 组",
            f"- 同文不同语境待复核：{duplicate_status_counts.get('same_text_different_context_review', 0)} 组",
            f"- 疑似模板污染：{duplicate_status_counts.get('template_pollution_candidate', 0)} 组",
            "",
            "样例：",
            "",
        ]
    )
    for group in duplicate_groups[:12]:
        lines.extend(
            [
                f"- `{group['text']}`",
                f"  count={group['count']}；status=`{group['status']}`；ids={', '.join(group['ids'][:5])}",
            ]
        )

    lines.extend(
        [
            "",
            "## 评测集草案",
            "",
            "- `data/eval/risk_test_preview.jsonl`：全 unsafe 预览样本，用于衡量 unsafe recall/封杀率。",
            "- `data/eval/normal_test_preview.jsonl`：safe 或 hard negative 预览样本，用于衡量 false positive/误封率。",
            "",
            "第一阶段建议阈值：risk_test unsafe recall 目标 80%-90%+；normal_test 误封率暂可容忍约 30%，后续靠 hard negative 和真实安全评论继续压低。",
            "",
            "## 生成文件",
            "",
            "- `data/raw/context_requirement_audit.json`",
            "- `data/raw/combined_candidates_binary_preview.jsonl`",
            "- `data/raw/external_safety_binary_preview.jsonl`",
            "- `data/eval/risk_test_preview.jsonl`",
            "- `data/eval/normal_test_preview.jsonl`",
        ]
    )
    return "\n".join(lines).strip() + "\n"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--combined-input", type=Path, default=COMBINED_INPUT)
    parser.add_argument("--external-input", type=Path, default=EXTERNAL_INPUT)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    combined_rows = load_jsonl(args.combined_input)
    external_rows = load_jsonl(args.external_input)
    combined_preview, external_preview, audit = build_previews(combined_rows, external_rows)
    risk_eval, normal_eval = build_eval_previews(combined_preview, external_preview)

    write_jsonl(COMBINED_BINARY_JSONL, combined_preview)
    write_jsonl(EXTERNAL_BINARY_JSONL, external_preview)
    write_jsonl(RISK_EVAL_JSONL, risk_eval)
    write_jsonl(NORMAL_EVAL_JSONL, normal_eval)
    write_json(AUDIT_JSON, audit)
    AUDIT_MD.write_text(render_md(audit), encoding="utf-8")

    print(f"Wrote combined binary preview: {COMBINED_BINARY_JSONL} ({len(combined_preview)} rows)")
    print(f"Wrote external binary preview: {EXTERNAL_BINARY_JSONL} ({len(external_preview)} rows)")
    print(f"Wrote risk eval preview: {RISK_EVAL_JSONL} ({len(risk_eval)} rows)")
    print(f"Wrote normal eval preview: {NORMAL_EVAL_JSONL} ({len(normal_eval)} rows)")
    print(f"Wrote audit JSON: {AUDIT_JSON}")
    print(f"Wrote audit report: {AUDIT_MD}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
