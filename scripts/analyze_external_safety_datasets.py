#!/usr/bin/env python3
"""Evaluate external Chinese safety datasets and build a small raw preview.

This script is intentionally conservative: external labels are treated as
source signals, not as final project labels. Generated rows stay in raw with
quality_status=needs_revision and review_notes=not_merged.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
from collections import Counter, defaultdict
from pathlib import Path
from statistics import mean, median
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
PROCESSED = ROOT / "data/processed/combined_candidates.jsonl"
TOXICN_DEFAULT = Path("/Users/davidchankong/Downloads/ToxiCN-main/ToxiCN_1.0.csv")
COLD_DEFAULT = Path("/Users/davidchankong/Downloads/COLDataset-main/COLDataset/train.csv")

REPORT_JSON = ROOT / "data/raw/external_safety_datasets_report.json"
PREVIEW_JSONL = ROOT / "data/raw/external_safety_import_preview.jsonl"
PREVIEW_JSON = ROOT / "data/raw/external_safety_import_preview.json"
REPORT_MD = ROOT / "docs/external_safety_datasets_review.md"
REVIEW_SAMPLE_MD = ROOT / "docs/external_safety_import_review_sample.md"

RISK_TERMS = (
    "私聊",
    "主页",
    "进群",
    "群",
    "上车",
    "盘口",
    "下注",
    "庄",
    "料",
    "包过",
    "下单",
    "出货",
    "你懂",
    "暗号",
    "别打全称",
    "首字母",
    "谐音",
    "拆开",
    "空格",
    "避开",
    "屏蔽",
    "审核",
    "风控",
    "炸",
    "爆",
    "枪",
    "刀",
    "药",
    "资源",
    "未成年",
    "学生",
)

TEXT_FIELDS = (
    "content",
    "TEXT",
    "text",
    "prompt",
    "query",
    "question",
    "sentence",
    "input",
    "instruction",
)

LABEL_FIELDS = (
    "toxic",
    "label",
    "safety_label",
    "risk_label",
    "is_unsafe",
    "unsafe",
    "subject",
    "category",
    "sub_category",
    "class",
)


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    rows = []
    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    return rows


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def normalize(text: str) -> str:
    return re.sub(r"\s+", "", text).lower()


def text_flags(text: str) -> list[str]:
    return [term for term in RISK_TERMS if term in text]


def length_summary(values: list[int]) -> dict[str, float | int]:
    if not values:
        return {"avg": 0, "median": 0, "p90": 0, "max": 0}
    sorted_values = sorted(values)
    return {
        "avg": round(mean(values), 2),
        "median": median(values),
        "p90": sorted_values[min(len(sorted_values) - 1, int(len(sorted_values) * 0.9))],
        "max": max(values),
    }


def first_present(row: dict[str, Any], fields: tuple[str, ...]) -> str:
    for field in fields:
        value = row.get(field)
        if value is not None and str(value).strip():
            return field
    return ""


def dataset_summary(name: str, rows: list[dict[str, Any]], text_field: str, label_field: str = "") -> dict[str, Any]:
    texts = [str(row.get(text_field, "")) for row in rows]
    norm_counts = Counter(normalize(text) for text in texts)
    label_counts = Counter(str(row.get(label_field, "")) for row in rows) if label_field else Counter()
    topic_counts = Counter(str(row.get("topic", "")) for row in rows if row.get("topic"))
    subject_counts = Counter(str(row.get("subject", "")) for row in rows if row.get("subject"))
    flag_hits = sum(1 for text in texts if text_flags(text))
    return {
        "name": name,
        "rows": len(rows),
        "columns": sorted(rows[0].keys()) if rows else [],
        "text_field": text_field,
        "label_field": label_field,
        "label_counts": dict(label_counts.most_common()),
        "topic_counts": dict(topic_counts.most_common()),
        "subject_counts": dict(subject_counts.most_common()),
        "length": length_summary([len(text) for text in texts]),
        "unique_texts": len(norm_counts),
        "duplicate_extra_rows": sum(count - 1 for count in norm_counts.values() if count > 1),
        "risk_term_hit_rows": flag_hits,
    }


def source_signal_toxicn(row: dict[str, Any]) -> tuple[str, str, bool, str, str]:
    toxic = str(row.get("toxic", "0"))
    toxic_type = str(row.get("toxic_type", "0"))
    expression = str(row.get("expression", "0"))
    if toxic == "0":
        return "none", "none", True, "weak", "外部标签为 non-toxic，可作为真实评论区 safe/hard negative 候选。"
    if toxic_type == "1":
        return "low", "D1_反讽", False, "weak", "外部标签为 toxic，但类型较轻，先作为 low 边界候选。"
    if expression in {"2", "3"}:
        return "medium", "D3_借代", False, "moderate", "外部标签为 toxic，且表达可能带间接/隐含形式。"
    return "medium", "literal_keyword", False, "moderate", "外部标签为 toxic，先作为辱骂/歧视风险候选。"


def source_signal_cold(row: dict[str, Any]) -> tuple[str, str, bool, str, str]:
    label = str(row.get("label", "0"))
    if label == "0":
        return "none", "none", True, "weak", "COLD 标注为 non-offensive，可作为真实评论 hard negative 候选。"
    return "medium", "literal_keyword", False, "moderate", "COLD 标注为 offensive，先作为辱骂/歧视风险候选。"


def source_signal_chinesesafe(row: dict[str, Any]) -> tuple[str, str, bool, str, str]:
    joined = " ".join(str(row.get(field, "")) for field in LABEL_FIELDS).lower()
    label = str(row.get("label", ""))
    subject = str(row.get("subject", ""))
    if label == "不违规" or subject == "不违规":
        return "none", "none", True, "weak", "ChineseSafe 标注为不违规，可作为安全/反证候选。"
    if subject == "变体词":
        return "medium", "F_组合编码", False, "moderate", "ChineseSafe 变体词类别，贴近中文规避表达。"
    if subject == "淫秽色情":
        return "high", "literal_keyword", False, "strong", "ChineseSafe 淫秽色情类别。"
    if subject == "政治错误":
        return "medium", "E3_话题/热点触发", False, "moderate", "ChineseSafe 政治相关安全类别。"
    if subject in {"违法犯罪", "身体伤害", "财产隐私"}:
        return "high", "literal_keyword", False, "strong", f"ChineseSafe {subject} 类别。"
    if subject in {"偏见歧视", "脏话侮辱"}:
        return "medium", "literal_keyword", False, "moderate", f"ChineseSafe {subject} 类别。"
    if subject in {"心理健康", "道德伦理"}:
        return "medium", "E3_话题/热点触发", False, "moderate", f"ChineseSafe {subject} 类别。"
    if any(token in joined for token in ("safe", "安全", "0")) and not any(
        token in joined for token in ("unsafe", "不安全", "risk", "illegal")
    ):
        return "none", "none", True, "weak", "ChineseSafe 源标签倾向 safe，先作为安全候选。"
    if any(token in joined for token in ("variant", "homophonic", "谐音", "变体")):
        return "medium", "F_组合编码", False, "moderate", "ChineseSafe 变体/谐音类别，贴近中文规避表达。"
    if any(token in joined for token in ("porn", "erotic", "色情")):
        return "high", "literal_keyword", False, "strong", "ChineseSafe 色情/低俗类别。"
    if any(token in joined for token in ("politic", "政治")):
        return "medium", "E3_话题/热点触发", False, "moderate", "ChineseSafe 政治敏感类别。"
    return "medium", "literal_keyword", False, "moderate", "ChineseSafe unsafe 类别，需人工复核映射。"


def make_reasoning(
    text: str,
    dataset_name: str,
    row: dict[str, Any],
    risk_level: str,
    encoding_primary: str,
    signal_note: str,
) -> dict[str, Any]:
    label_bits = []
    for field in ("topic", "toxic", "toxic_type", "expression", "label", "subject", "category", "sub_category", "class"):
        if row.get(field) not in (None, ""):
            label_bits.append(f"{field}={row.get(field)}")
    label_text = "；".join(label_bits) if label_bits else "外部字段未提供明确标签。"
    flags = text_flags(text)

    if risk_level == "none":
        supporting = ["外部标签倾向安全或非冒犯。"]
        counter = [
            "仍需检查是否存在本项目关注的黑话、语境触发或二次回复风险。",
            "当前转换只使用外部粗标签，不等同于项目最终标注。",
        ]
    else:
        supporting = [signal_note, f"外部标签信息：{label_text}。"]
        if flags:
            supporting.append(f"文本命中若干风险提示词：{', '.join(flags[:5])}。")
        counter = [
            "外部数据通常缺少标题、话题和真实事件背景，需要补最小上下文后再定级。",
            "该条可能只是普通争论、引用或转述，需人工复核反证。",
        ]

    return {
        "literal_analysis": [f"字面文本为：{text}"],
        "encoding_analysis": [
            f"外部导入初步映射为 {encoding_primary}；该映射只是候选，不是最终标签。",
        ],
        "context_analysis": [
            f"来源数据集：{dataset_name}；外部字段：{label_text}。",
            "原始数据缺少完整评论链，本项目后续应补充或构造最小上下文。",
        ],
        "supporting_evidence": supporting,
        "counter_evidence": counter,
        "final_rationale": (
            f"根据外部标签和文本表层特征，暂标为 {risk_level}；"
            "该样本必须经过人工复核，并重塑更贴合项目标准的推理链。"
        ),
    }


def make_sample(
    sample_id: str,
    dataset_name: str,
    row: dict[str, Any],
    text: str,
    risk_level: str,
    encoding_primary: str,
    hard_negative: bool,
    evidence_strength: str,
    signal_note: str,
) -> dict[str, Any]:
    topic = str(row.get("topic", "")).strip()
    label_parts = []
    for field in ("toxic", "toxic_type", "expression", "label", "subject", "category", "sub_category", "class"):
        if row.get(field) not in (None, ""):
            label_parts.append(f"{field}={row.get(field)}")
    review_notes = "; ".join(
        [
            f"source={dataset_name}",
            "external_import_preview",
            "not_merged",
            *label_parts,
            f"topic={topic}" if topic else "",
        ]
    ).replace("; ;", ";").strip("; ")

    return {
        "id": sample_id,
        "split": "train",
        "source_type": "real",
        "platform": platform_for(dataset_name, row),
        "text": text,
        "context": {
            "title": f"{dataset_name} 外部真实评论样本",
            "description": "外部数据集原始样本，尚未补充最小上下文。",
            "time": "",
            "topic": topic or dataset_name,
        },
        "risk_level": risk_level,
        "encoding_primary": encoding_primary,
        "encoding_secondary": [],
        "context_required": risk_level != "none",
        "ambiguity": "high" if risk_level in {"low", "none"} else "medium",
        "evidence_strength": evidence_strength,
        "freshness": "stable",
        "hard_negative": hard_negative,
        "target_known": False,
        "target_reference": "",
        "should_explain_target": False,
        "reasoning": make_reasoning(text, dataset_name, row, risk_level, encoding_primary, signal_note),
        "quality_status": "needs_revision",
        "review_notes": review_notes,
    }


def platform_for(dataset_name: str, row: dict[str, Any]) -> str:
    if row.get("platform"):
        return str(row["platform"])
    if dataset_name == "COLD":
        return "中文评论区"
    if dataset_name == "ChineseSafe":
        return "ChineseSafe"
    return dataset_name


def stratified_pick(
    rows: list[dict[str, Any]],
    key_fields: tuple[str, ...],
    limit: int,
    text_field: str,
) -> list[dict[str, Any]]:
    buckets: dict[tuple[str, ...], list[dict[str, Any]]] = defaultdict(list)
    seen_texts: set[str] = set()
    for row in rows:
        text = str(row.get(text_field, "")).strip()
        if not text:
            continue
        normalized = normalize(text)
        if normalized in seen_texts:
            continue
        seen_texts.add(normalized)
        key = tuple(str(row.get(field, "")) for field in key_fields)
        buckets[key].append(row)

    picked: list[dict[str, Any]] = []
    keys = sorted(buckets)
    while len(picked) < limit and keys:
        progressed = False
        for key in list(keys):
            bucket = buckets[key]
            if bucket:
                picked.append(bucket.pop(0))
                progressed = True
                if len(picked) >= limit:
                    break
            else:
                keys.remove(key)
        if not progressed:
            break
    return picked


def convert_dataset(
    dataset_name: str,
    rows: list[dict[str, Any]],
    text_field: str,
    limit: int,
    id_prefix: str,
) -> list[dict[str, Any]]:
    if dataset_name == "ToxiCN":
        picked = stratified_pick(rows, ("topic", "toxic", "toxic_type", "expression"), limit, text_field)
        signal = source_signal_toxicn
    elif dataset_name == "COLD":
        picked = stratified_pick(rows, ("topic", "label"), limit, text_field)
        signal = source_signal_cold
    else:
        key_fields = tuple(field for field in ("subject", "category", "sub_category", "class", "label", "safety_label") if rows and field in rows[0])
        picked = stratified_pick(rows, key_fields or ("",), limit, text_field)
        signal = source_signal_chinesesafe

    samples = []
    for index, row in enumerate(picked, start=1):
        text = str(row.get(text_field, "")).strip()
        risk_level, encoding_primary, hard_negative, evidence_strength, note = signal(row)
        samples.append(
            make_sample(
                sample_id=f"{id_prefix}_{index:04d}_{risk_level.upper()}",
                dataset_name=dataset_name,
                row=row,
                text=text,
                risk_level=risk_level,
                encoding_primary=encoding_primary,
                hard_negative=hard_negative,
                evidence_strength=evidence_strength,
                signal_note=note,
            )
        )
    return samples


def duplicate_audit(samples: list[dict[str, Any]], limit: int = 80) -> dict[str, Any]:
    groups: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for sample in samples:
        groups[normalize(str(sample.get("text", "")))].append(sample)
    duplicate_groups = [rows for rows in groups.values() if len(rows) > 1]
    duplicate_groups.sort(key=lambda rows: (-len(rows), rows[0]["text"]))
    return {
        "duplicate_group_count": len(duplicate_groups),
        "duplicate_extra_rows": sum(len(rows) - 1 for rows in duplicate_groups),
        "groups": [
            {
                "text": rows[0]["text"],
                "count": len(rows),
                "items": [
                    {
                        "id": row["id"],
                        "risk_level": row.get("risk_level"),
                        "encoding_primary": row.get("encoding_primary"),
                        "context_title": row.get("context", {}).get("title", ""),
                        "review_notes": row.get("review_notes", ""),
                    }
                    for row in rows
                ],
            }
            for rows in duplicate_groups[:limit]
        ],
    }


def load_chinesesafe(enabled: bool, split: str) -> tuple[list[dict[str, Any]], str, str, str]:
    if not enabled:
        return [], "", "", "disabled"
    try:
        from datasets import load_dataset  # type: ignore
    except Exception as exc:
        return [], "", "", f"datasets import failed: {exc}"
    try:
        dataset = load_dataset("SUSTech/ChineseSafe", split=split)
    except Exception as exc:
        return [], "", "", f"load_dataset failed: {exc}"
    rows = [dict(row) for row in dataset]
    if not rows:
        return [], "", "", "empty"
    text_field = first_present(rows[0], TEXT_FIELDS)
    label_field = first_present(rows[0], LABEL_FIELDS)
    if not text_field:
        # Fall back to the longest string field in the first row.
        string_fields = [key for key, value in rows[0].items() if isinstance(value, str)]
        text_field = max(string_fields, key=lambda key: len(str(rows[0].get(key, ""))), default="")
    return rows, text_field, label_field, "loaded"


def write_jsonl(rows: list[dict[str, Any]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False, separators=(",", ":")) + "\n")


def write_json(value: Any, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        json.dump(value, handle, ensure_ascii=False, indent=2)


def write_markdown(
    summaries: list[dict[str, Any]],
    conversion_counts: Counter[str],
    chinesesafe_status: str,
    path: Path,
) -> None:
    lines = [
        "# 外部安全数据集接入评估",
        "",
        "本报告只评估外部数据，不修改正式 `data/processed/combined_candidates.*`。",
        "外部标签只作为候选信号，不能替代本项目的人工复核、语境判断和推理链重塑。",
        "",
        "## 数据集概览",
        "",
        "| 数据集 | 行数 | 文本字段 | 标签字段 | 唯一文本 | 重复额外行 | 平均长度 | P90 长度 | 风险提示词命中行 |",
        "|---|---:|---|---|---:|---:|---:|---:|---:|",
    ]
    for summary in summaries:
        length = summary["length"]
        lines.append(
            "| {name} | {rows} | `{text_field}` | `{label_field}` | {unique_texts} | {duplicate_extra_rows} | {avg} | {p90} | {risk_term_hit_rows} |".format(
                avg=length["avg"],
                p90=length["p90"],
                **summary,
            )
        )
    lines.extend(["", "## 标签/主题分布", ""])
    for summary in summaries:
        lines.append(f"### {summary['name']}")
        if summary["label_counts"]:
            lines.append("")
            lines.append("标签分布：")
            lines.append("")
            for key, value in summary["label_counts"].items():
                lines.append(f"- `{key}`：{value}")
        if summary["topic_counts"]:
            lines.append("")
            lines.append("主题分布：")
            lines.append("")
            for key, value in summary["topic_counts"].items():
                lines.append(f"- `{key}`：{value}")
        if summary["subject_counts"]:
            lines.append("")
            lines.append("subject 分布：")
            lines.append("")
            for key, value in summary["subject_counts"].items():
                lines.append(f"- `{key}`：{value}")
        lines.append("")

    lines.extend(
        [
            "## 转换预览",
            "",
            f"ChineseSafe 加载状态：`{chinesesafe_status}`。",
            "",
            "已生成 `data/raw/external_safety_import_preview.jsonl/.json`。这些样本全部保持：",
            "",
            "- `source_type=real`",
            "- `quality_status=needs_revision`",
            "- `review_notes` 包含 `external_import_preview` 与 `not_merged`",
            "- 不进入正式 processed",
            "",
            "预览来源计数：",
            "",
        ]
    )
    for key, value in sorted(conversion_counts.items()):
        lines.append(f"- {key}：{value}")

    lines.extend(
        [
            "",
            "## 初步判断",
            "",
            "1. ToxiCN/COLD 的真实评论质感明显优于当前项目中早期 AI 扩写样本，适合补充辱骂、歧视、地域/性别/race/lgbt 边界。",
            "2. ChineseSafe 更接近安全评测基准，适合补类别体系、变体/谐音和外部评测，不应直接全量转训练。",
            "3. 外部数据普遍缺少标题、话题、真实背景和反证；接入后必须重塑 `context` 与 `reasoning`。",
            "4. 下一步应人工抽查转换预览，再决定每个来源保留比例和映射规则。",
            "",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def write_duplicate_markdown(audit: dict[str, Any], path: Path) -> None:
    lines = [
        "# 正式数据重复文本审计",
        "",
        f"重复 text 分组：{audit['duplicate_group_count']}",
        f"额外重复行：{audit['duplicate_extra_rows']}",
        "",
        "说明：同一 text 在不同 context 下作为对照样本不一定错误，但需要人工判断是否属于有效语境对照，还是早期模板污染。",
        "",
        "## 重复组样例",
        "",
    ]
    for group in audit["groups"]:
        lines.append(f"### {group['text']}")
        lines.append("")
        lines.append(f"出现次数：{group['count']}")
        lines.append("")
        for item in group["items"]:
            lines.append(
                f"- `{item['id']}`：{item['risk_level']} / {item['encoding_primary']} / {item['context_title']}"
            )
        lines.append("")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def source_from_sample(sample: dict[str, Any]) -> str:
    return note_source(str(sample.get("review_notes", "")))


def compact_text(text: str, limit: int = 120) -> str:
    cleaned = " ".join(str(text).split())
    if len(cleaned) <= limit:
        return cleaned
    return cleaned[: limit - 1] + "…"


def write_review_sample(samples: list[dict[str, Any]], path: Path, per_source: int = 20) -> None:
    buckets: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for sample in samples:
        buckets[source_from_sample(sample)].append(sample)

    lines = [
        "# 外部 raw 转换预览抽样",
        "",
        "本清单用于人工判断外部真实评论是否适合进入下一步重塑，不代表正式入库。",
        "",
        "建议反馈格式：",
        "",
        "```text",
        "EXT_TOXICN_0001_MEDIUM：通过 / 退回 / 改标签 / 改 reasoning / 删掉，原因……",
        "```",
        "",
    ]
    for source in sorted(buckets):
        lines.append(f"## {source}")
        lines.append("")
        for sample in buckets[source][:per_source]:
            notes = str(sample.get("review_notes", ""))
            label_bits = [
                part.strip()
                for part in notes.split(";")
                if part.strip().startswith(("topic=", "label=", "toxic=", "toxic_type=", "expression=", "subject="))
            ]
            lines.append(f"### {sample['id']}")
            lines.append("")
            lines.append(f"- 初标：`{sample['risk_level']}` / `{sample['encoding_primary']}`")
            lines.append(f"- hard_negative：`{str(sample['hard_negative']).lower()}`")
            if label_bits:
                lines.append(f"- 外部标签：`{'; '.join(label_bits)}`")
            lines.append(f"- text：{compact_text(sample['text'])}")
            lines.append("")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Analyze external Chinese safety datasets.")
    parser.add_argument("--toxicn", type=Path, default=TOXICN_DEFAULT)
    parser.add_argument("--cold", type=Path, default=COLD_DEFAULT)
    parser.add_argument("--include-chinesesafe", action="store_true")
    parser.add_argument("--chinesesafe-split", default="test")
    parser.add_argument("--limit-toxicn", type=int, default=120)
    parser.add_argument("--limit-cold", type=int, default=120)
    parser.add_argument("--limit-chinesesafe", type=int, default=100)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    processed = load_jsonl(PROCESSED)
    existing_texts = {normalize(str(row.get("text", ""))) for row in processed}

    summaries: list[dict[str, Any]] = []
    preview: list[dict[str, Any]] = []

    toxicn_rows = read_csv(args.toxicn) if args.toxicn.exists() else []
    if toxicn_rows:
        summaries.append(dataset_summary("ToxiCN", toxicn_rows, "content", "toxic"))
        preview.extend(convert_dataset("ToxiCN", toxicn_rows, "content", args.limit_toxicn, "EXT_TOXICN"))

    cold_rows = read_csv(args.cold) if args.cold.exists() else []
    if cold_rows:
        summaries.append(dataset_summary("COLD", cold_rows, "TEXT", "label"))
        preview.extend(convert_dataset("COLD", cold_rows, "TEXT", args.limit_cold, "EXT_COLD"))

    chinesesafe_rows, chinesesafe_text_field, chinesesafe_label_field, chinesesafe_status = load_chinesesafe(
        args.include_chinesesafe,
        args.chinesesafe_split,
    )
    if chinesesafe_rows and chinesesafe_text_field:
        summaries.append(
            dataset_summary(
                "ChineseSafe",
                chinesesafe_rows,
                chinesesafe_text_field,
                chinesesafe_label_field,
            )
        )
        preview.extend(
            convert_dataset(
                "ChineseSafe",
                chinesesafe_rows,
                chinesesafe_text_field,
                args.limit_chinesesafe,
                "EXT_CHINESAFE",
            )
        )

    deduped_preview = []
    seen_preview_texts: set[str] = set()
    overlap_with_processed = 0
    for row in preview:
        normalized = normalize(row["text"])
        if normalized in existing_texts:
            overlap_with_processed += 1
            continue
        if normalized in seen_preview_texts:
            continue
        seen_preview_texts.add(normalized)
        deduped_preview.append(row)

    for index, row in enumerate(deduped_preview, start=1):
        row["review_notes"] += f"; preview_index={index}"

    conversion_counts = Counter(note_source(row.get("review_notes", "")) for row in deduped_preview)
    report = {
        "summaries": summaries,
        "chinesesafe_status": chinesesafe_status,
        "preview_count": len(deduped_preview),
        "preview_source_counts": dict(sorted(conversion_counts.items())),
        "overlap_with_processed_skipped": overlap_with_processed,
    }

    write_jsonl(deduped_preview, PREVIEW_JSONL)
    write_json(deduped_preview, PREVIEW_JSON)
    write_json(report, REPORT_JSON)
    write_markdown(summaries, conversion_counts, chinesesafe_status, REPORT_MD)
    write_review_sample(deduped_preview, REVIEW_SAMPLE_MD)

    print(f"Wrote {len(deduped_preview)} preview rows to {PREVIEW_JSONL}")
    print(f"Wrote report to {REPORT_MD}")
    print(f"Wrote review sample to {REVIEW_SAMPLE_MD}")
    print(f"ChineseSafe status: {chinesesafe_status}")
    return 0


def note_source(notes: str) -> str:
    for part in notes.split(";"):
        part = part.strip()
        if part.startswith("source="):
            return part.split("=", 1)[1]
    return "unknown"


if __name__ == "__main__":
    raise SystemExit(main())
