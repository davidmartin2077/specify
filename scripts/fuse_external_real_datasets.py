#!/usr/bin/env python3
"""Fuse high-quality external Chinese safety data into the simplified dataset."""

from __future__ import annotations

import argparse
import csv
import json
import random
import re
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT = ROOT / "data/processed/combined_candidates.jsonl"
DEFAULT_TOXICN = Path("/Users/davidchankong/Downloads/ToxiCN-main/ToxiCN_1.0.csv")
DEFAULT_COLD = Path("/Users/davidchankong/Downloads/COLDataset-main/COLDataset/train.csv")
DEFAULT_REPORT = ROOT / "data/processed/external_fusion_report.json"


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    rows = []
    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    return rows


def write_jsonl(rows: list[dict[str, Any]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False, separators=(",", ":")) + "\n")


def write_json(value: Any, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        json.dump(value, handle, ensure_ascii=False, indent=2)


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def norm(text: str) -> str:
    return re.sub(r"\s+", "", text).lower()


def clean_text(text: Any) -> str:
    return re.sub(r"\s+", " ", str(text or "")).strip()


BAD_TEXT_PATTERNS = (
    "参考上述上下文",
    "根据前面的段落",
    "以下是否是真的",
    "是的,不是,或也许",
    "真的,假的",
    "真的，假的",
    "问题：",
    "问题:",
    "我该怎么办",
    "应该跟",
    "是否是真的",
    "下划线处",
    "__",
    "生成一个",
    "替换这个句子",
    "应用简介",
    "产品特色",
    "个股行情",
    "行情分析",
    "借款APP",
    "请选择",
)

EXTERNAL_SOURCES = {"toxicn", "cold", "chinesesafe"}
CHINESAFE_KEEP_SUBJECTS = {"不违规", "淫秽色情", "违法犯罪", "偏见歧视", "脏话侮辱", "政治错误", "变体词"}


def usable_text(text: str) -> bool:
    if not text:
        return False
    length = len(text)
    if length < 4 or length > 180:
        return False
    return not any(pattern in text for pattern in BAD_TEXT_PATTERNS)


def usable_external_row(source: str, row: dict[str, Any], text: str) -> bool:
    if not usable_text(text):
        return False
    if source == "chinesesafe":
        subject = str(row.get("subject", ""))
        if subject not in CHINESAFE_KEEP_SUBJECTS:
            return False
        if "？" in text or "?" in text:
            return False
    return True


def risk_from_external(source: str, row: dict[str, Any]) -> tuple[str, str, bool, str, list[str], list[str]]:
    if source == "toxicn":
        toxic = str(row.get("toxic", "0"))
        topic = str(row.get("topic", ""))
        expression = str(row.get("expression", ""))
        if toxic == "0":
            return "none", "none", True, "weak", [], [f"ToxiCN 标注为 non-toxic；topic={topic}。"]
        text = str(row.get("content", ""))
        high_terms = ("弄死", "该死", "死光", "黑乐色", "丧尸", "暴力", "强奸", "婊子")
        risk = "high" if any(term in text for term in high_terms) else "medium"
        encoding = "D3_借代" if expression in {"2", "3"} else "literal_keyword"
        return risk, encoding, False, "strong" if risk == "high" else "moderate", [
            f"ToxiCN 标注为 toxic；topic={topic}。",
            "文本呈现群体攻击、侮辱或偏见表达。",
        ], ["需避免只因群体词出现就误判；本条风险来自完整表达。"]

    if source == "cold":
        label = str(row.get("label", "0"))
        topic = str(row.get("topic", ""))
        if label == "0":
            return "none", "none", True, "weak", [], [f"COLD 标注为 non-offensive；topic={topic}。"]
        text = str(row.get("TEXT", ""))
        high_terms = ("弄死", "死", "垃圾", "丧尸", "黑鬼", "绿绿", "婊子")
        risk = "high" if any(term in text for term in high_terms) else "medium"
        return risk, "literal_keyword", False, "strong" if risk == "high" else "moderate", [
            f"COLD 标注为 offensive；topic={topic}。",
            "文本呈现真实评论里的攻击、贬损或刻板印象。",
        ], ["仍需区分引用、反驳和真实攻击；本条按原始标签与文本整体判断。"]

    label = str(row.get("label", ""))
    subject = str(row.get("subject", ""))
    if label == "不违规" or subject == "不违规":
        return "none", "none", True, "weak", [], [f"ChineseSafe 标注为不违规；subject={subject}。"]
    high_subjects = {"违法犯罪"}
    encoding = "F_组合编码" if subject == "变体词" else "literal_keyword"
    sexual_terms = (
        "约炮",
        "口交",
        "颜射",
        "撸管",
        "高潮",
        "深喉",
        "坐脸",
        "骚水",
        "母狗",
        "卖淫",
        "裸聊",
        "淫妻",
        "肉棒",
        "后入",
        "兽欲",
        "绿帽献妻",
        "内部群见主页",
    )
    if subject == "淫秽色情" and any(term in str(row.get("text", "")) for term in sexual_terms):
        high_subjects.add("淫秽色情")
    risk = "high" if subject in high_subjects else "medium"
    return risk, encoding, False, "strong" if risk == "high" else "moderate", [
        f"ChineseSafe 标注为违规；subject={subject}。",
        "文本来自真实安全评测分布，语气比合成模板更接近实际输入。",
    ], ["外部标签不是最终真理，但该文本整体风险信号足够进入训练。"]


def make_sample(source: str, row: dict[str, Any], text: str) -> dict[str, Any]:
    risk, encoding, hard_negative, evidence, support, counter = risk_from_external(source, row)
    platform = str(row.get("platform", "") or ("ChineseSafe" if source == "chinesesafe" else source))
    topic = str(row.get("topic", "") or row.get("subject", "") or source)
    return {
        "id": "",
        "split": "train",
        "source_type": "real",
        "platform": platform,
        "text": text,
        "context": {"title": "", "description": "", "time": "", "topic": topic},
        "risk_level": risk,
        "encoding_primary": encoding,
        "encoding_secondary": [],
        "needs_context": False,
        "ambiguity": "low" if risk in {"high", "none"} else "medium",
        "evidence_strength": evidence,
        "freshness": "stable",
        "hard_negative": hard_negative,
        "target_known": False,
        "target_reference": "",
        "should_explain_target": False,
        "reasoning": {
            "literal_analysis": [f"字面上是在表达：{text}"],
            "encoding_analysis": [
                "真实外部评论/安全数据样本；优先按短文本本身判断，不编造额外上下文。"
                if risk != "none"
                else "未发现稳定风险编码；按短文本本身判断为普通表达。"
            ],
            "context_analysis": ["无明确上下文；按弹幕、应用评论、音乐评论等短文本场景做裸文本判断。"],
            "supporting_evidence": support,
            "counter_evidence": counter,
            "final_rationale": f"综合文本信号和反证，判为 {risk}。",
        },
        "quality_status": "needs_revision",
        "review_notes": f"source={source}; external_real_fusion; topic={topic}",
    }


def pick_rows(
    source: str,
    rows: list[dict[str, Any]],
    text_field: str,
    limit: int,
    existing: set[str],
    seed: int,
) -> list[dict[str, Any]]:
    rng = random.Random(seed)
    buckets: dict[str, list[tuple[dict[str, Any], str]]] = defaultdict(list)
    seen = set(existing)
    for row in rows:
        text = clean_text(row.get(text_field, ""))
        if not usable_external_row(source, row, text):
            continue
        key = norm(text)
        if key in seen:
            continue
        risk, *_ = risk_from_external(source, row)
        buckets[risk].append((row, text))
        seen.add(key)

    for values in buckets.values():
        rng.shuffle(values)

    quotas = {"high": int(limit * 0.2), "medium": int(limit * 0.4), "low": 0, "none": int(limit * 0.4)}
    selected: list[dict[str, Any]] = []
    selected_keys = set(existing)
    for risk in ("high", "medium", "none"):
        for row, text in buckets.get(risk, [])[: quotas.get(risk, 0)]:
            key = norm(text)
            if key not in selected_keys:
                selected.append(make_sample(source, row, text))
                selected_keys.add(key)

    leftovers = []
    for values in buckets.values():
        leftovers.extend(values)
    rng.shuffle(leftovers)
    for row, text in leftovers:
        if len(selected) >= limit:
            break
        key = norm(text)
        if key not in selected_keys:
            selected.append(make_sample(source, row, text))
            selected_keys.add(key)
    return selected[:limit]


def load_chinesesafe(split: str) -> list[dict[str, Any]]:
    from datasets import load_dataset  # type: ignore

    return [dict(row) for row in load_dataset("SUSTech/ChineseSafe", split=split)]


def renumber(rows: list[dict[str, Any]]) -> None:
    for index, row in enumerate(rows, start=1):
        row["id"] = f"{index:06d}"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Fuse external real Chinese safety datasets.")
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--toxicn", type=Path, default=DEFAULT_TOXICN)
    parser.add_argument("--cold", type=Path, default=DEFAULT_COLD)
    parser.add_argument("--limit-per-source", type=int, default=160)
    parser.add_argument("--chinesesafe-split", default="test")
    parser.add_argument("--seed", type=int, default=20260610)
    parser.add_argument("--report", type=Path, default=DEFAULT_REPORT)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    loaded = load_jsonl(args.input)
    current = [row for row in loaded if note_source(row) not in EXTERNAL_SOURCES]
    existing = {norm(str(row.get("text", ""))) for row in current}

    external: list[dict[str, Any]] = []
    toxicn = pick_rows("toxicn", read_csv(args.toxicn), "content", args.limit_per_source, existing, args.seed + 1)
    existing.update(norm(row["text"]) for row in toxicn)
    cold = pick_rows("cold", read_csv(args.cold), "TEXT", args.limit_per_source, existing, args.seed + 2)
    existing.update(norm(row["text"]) for row in cold)
    chinesesafe_rows = load_chinesesafe(args.chinesesafe_split)
    chinesesafe = pick_rows("chinesesafe", chinesesafe_rows, "text", args.limit_per_source, existing, args.seed + 3)

    external.extend(toxicn)
    external.extend(cold)
    external.extend(chinesesafe)

    fused = current + external
    renumber(fused)
    write_jsonl(fused, args.input)
    write_json(fused, args.input.with_suffix(".json"))

    report = {
        "previous_count": len(current),
        "removed_previous_external": len(loaded) - len(current),
        "added_count": len(external),
        "new_count": len(fused),
        "added_by_source": dict(Counter(note_source(row) for row in external)),
        "added_risk": dict(Counter(row["risk_level"] for row in external)),
        "total_risk": dict(Counter(row["risk_level"] for row in fused)),
        "total_source": dict(Counter(note_source(row) for row in fused)),
    }
    write_json(report, args.report)
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0


def note_source(row: dict[str, Any]) -> str:
    notes = str(row.get("review_notes", ""))
    for part in notes.split(";"):
        part = part.strip()
        if part.startswith("source="):
            return part.split("=", 1)[1]
    return "unknown"


if __name__ == "__main__":
    raise SystemExit(main())
