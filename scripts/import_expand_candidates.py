#!/usr/bin/env python3
"""Normalize external expansion candidates and merge them into processed data."""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
BASE_PATH = ROOT / "data/processed/combined_candidates.jsonl"
MEME_RAW_PATH = ROOT / "data/raw/meme_expand_candidates_120.jsonl"
GEMINI_RAW_PATH = ROOT / "data/raw/gemini_expand_candidates_120.jsonl"
EXPAND_OUTPUT_PATH = ROOT / "data/processed/expand_candidates_cleaned.jsonl"
COMBINED_JSONL_PATH = ROOT / "data/processed/combined_candidates.jsonl"
COMBINED_JSON_PATH = ROOT / "data/processed/combined_candidates.json"


RISK_TO_EVIDENCE = {
    "high": "strong",
    "medium": "moderate",
    "low": "weak",
    "none": "weak",
}

RISK_TO_AMBIGUITY = {
    "high": "medium",
    "medium": "medium",
    "low": "high",
    "none": "low",
}

PLATFORM_NORMALIZATION = {
    "weibo": "微博",
    "zhihu": "知乎",
    "tieba": "贴吧",
    "bilibili": "B站",
    "douyin": "抖音",
}


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as handle:
        for line_number, raw_line in enumerate(handle, start=1):
            line = raw_line.strip()
            if not line:
                continue
            try:
                value = json.loads(line)
            except json.JSONDecodeError as exc:
                raise ValueError(f"{path}:{line_number}: invalid JSON: {exc.msg}") from exc
            if not isinstance(value, dict):
                raise ValueError(f"{path}:{line_number}: expected a JSON object")
            rows.append(value)
    return rows


def write_jsonl(samples: list[dict[str, Any]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        for sample in samples:
            handle.write(json.dumps(sample, ensure_ascii=False, separators=(",", ":")) + "\n")


def write_json(samples: list[dict[str, Any]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        json.dump(samples, handle, ensure_ascii=False, indent=2)


def normalize_platform(platform: Any) -> str:
    text = str(platform or "unknown").strip()
    return PLATFORM_NORMALIZATION.get(text.lower(), text or "unknown")


def normalize_risk(value: Any) -> str:
    risk = str(value or "medium").strip().lower()
    return risk if risk in {"high", "medium", "low", "none"} else "medium"


def normalize_evidence(value: Any, risk: str) -> str:
    evidence = str(value or "").strip().lower()
    if evidence in {"weak", "moderate", "strong"}:
        return evidence
    return RISK_TO_EVIDENCE[risk]


def normalize_ambiguity(value: Any, risk: str) -> str:
    ambiguity = str(value or "").strip().lower()
    if ambiguity in {"low", "medium", "high"}:
        return ambiguity
    return RISK_TO_AMBIGUITY[risk]


def normalize_secondary(value: Any) -> list[str]:
    if isinstance(value, list):
        return [str(item).strip() for item in value if str(item).strip() and str(item).strip().lower() != "none"]
    if isinstance(value, str) and value.strip() and value.strip().lower() != "none":
        return [value.strip()]
    return []


def ensure_context(value: Any, text: str = "") -> dict[str, Any]:
    if isinstance(value, dict):
        return {
            "title": str(value.get("title", "")),
            "description": str(value.get("description", "")),
            "parent_comment": str(value.get("parent_comment", "")),
            "reply_chain": [str(item) for item in value.get("reply_chain", []) if str(item).strip()]
            if isinstance(value.get("reply_chain", []), list)
            else [],
            "time": str(value.get("time", "")),
            "topic": str(value.get("topic", "")),
        }

    context_text = str(value or "").strip()
    parent_comment = ""
    if "-> [回复]" in text:
        parent_comment, _ = text.split("-> [回复]", 1)

    return {
        "title": context_text,
        "description": "",
        "parent_comment": parent_comment.strip(),
        "reply_chain": [],
        "time": "",
        "topic": "",
    }


def extract_reply_text(text: str) -> str:
    if "-> [回复]" not in text:
        return text
    _, reply = text.split("-> [回复]", 1)
    return reply.strip()


def extract_cluster(sample: dict[str, Any]) -> str:
    notes = str(sample.get("review_notes", ""))
    match = re.search(r"meme_cluster=([^;]+)", notes)
    return match.group(1).strip() if match else ""


def topic_text(sample: dict[str, Any]) -> str:
    context = sample.get("context")
    if isinstance(context, dict):
        return str(context.get("topic", ""))
    return str(context or "")


def has_latin_abbrev(text: str) -> bool:
    return bool(re.search(r"\b[A-Za-z]{2,}\b", text))


def has_visual_split(text: str) -> bool:
    return bool(re.search(r"[\u200b\u200c\u200d]|[·*_/\\\\|]+|\S\s+\S", text))


def has_shape_variant(text: str) -> bool:
    return any(token in text for token in ["目田", "夶", "氏王", "申青", "氵", "口十", "金 戋", "木 头"])


def infer_primary(sample: dict[str, Any], risk: str, source: str) -> str:
    if risk == "none":
        return "none"

    primary = str(sample.get("encoding_primary") or "").strip()
    text = str(sample.get("text") or "")
    topic = topic_text(sample)
    signal = f"{text} {topic} {sample.get('review_notes', '')}"

    if primary == "A2_拼音/首字母缩写" and not has_latin_abbrev(text):
        primary = ""
    if primary == "B1_拆字" and not has_visual_split(text) and "拆" not in signal:
        primary = ""
    if primary == "B3_形近字替换" and not has_shape_variant(text):
        primary = ""
    if primary == "B4_符号/空格/Unicode 干扰" and not has_visual_split(text):
        primary = ""

    if primary:
        return primary

    if any(token in signal for token in ["zf", "jc", "dy", "sz", "hmd", "yy", "xdm"]):
        return "A2_拼音/首字母缩写"
    if has_shape_variant(text):
        return "B3_形近字替换"
    if has_visual_split(text):
        return "B4_符号/空格/Unicode 干扰"
    if any(token in signal for token in ["日期", "数字", "5·35", "五月三十五", "101", "64", "35页"]):
        return "C3_数字代指"
    if "历史人物" in signal or any(token in signal for token in ["崇祯", "司马", "末代", "黄轩", "王洪文"]):
        return "C1_历史人物类比"
    if "历史事件" in signal or any(token in signal for token in ["蜡烛", "白纸", "勇士", "广场"]):
        return "C2_历史事件影射"
    if any(token in signal for token in ["加速", "刹车", "倒车", "平台黑话", "自我审查", "捂嘴", "少说话"]):
        return "E1_平台黑话" if source == "gemini" else "C4_典故/物品/符号借用"
    if any(token in signal for token in ["回复链", "-> [回复]"]):
        return "E3_回复链/互动触发"
    if any(token in signal for token in ["时间节点", "纪念日", "这几天", "今天", "晚上"]):
        return "E2_时间节点触发"
    if any(token in signal for token in ["反讽", "阴阳", "好日子", "真棒"]):
        return "D1_反讽"
    if any(token in signal for token in ["组合编码", "叠加"]):
        return "F_组合编码"
    return "C4_典故/物品/符号借用"


def context_required(sample: dict[str, Any], risk: str, primary: str, context: dict[str, Any]) -> bool:
    if sample.get("context_required") is True:
        return True
    if primary in {"E2_时间节点触发", "E3_回复链/互动触发", "F_组合编码"}:
        return True
    if risk in {"high", "medium"}:
        return True
    return bool(context.get("title") or context.get("parent_comment") or context.get("reply_chain"))


def normalize_reasoning(
    sample: dict[str, Any],
    *,
    text: str,
    context: dict[str, Any],
    risk: str,
    primary: str,
    secondary: list[str],
    source: str,
) -> dict[str, Any]:
    existing = sample.get("reasoning")
    if isinstance(existing, dict):
        reasoning = {
            "literal_analysis": list(existing.get("literal_analysis", []))
            if isinstance(existing.get("literal_analysis", []), list)
            else [],
            "encoding_analysis": [],
            "context_analysis": list(existing.get("context_analysis", []))
            if isinstance(existing.get("context_analysis", []), list)
            else [],
            "supporting_evidence": list(existing.get("supporting_evidence", []))
            if isinstance(existing.get("supporting_evidence", []), list)
            else [],
            "counter_evidence": list(existing.get("counter_evidence", []))
            if isinstance(existing.get("counter_evidence", []), list)
            else [],
            "final_rationale": str(existing.get("final_rationale", "")).strip(),
        }
    else:
        raw_reasoning = str(existing or "").strip()
        reasoning = {
            "literal_analysis": [f"字面上是在表达：{text}"],
            "encoding_analysis": [],
            "context_analysis": [],
            "supporting_evidence": [raw_reasoning] if raw_reasoning and risk != "none" else [],
            "counter_evidence": [],
            "final_rationale": "",
        }

    if not reasoning["literal_analysis"]:
        reasoning["literal_analysis"] = [f"字面上是在表达：{text}"]

    if primary == "none":
        reasoning["encoding_analysis"] = ["未发现足够稳定的编码机制，风险解释不成立。"]
    else:
        pieces = [f"按项目分类归为 {primary}。"]
        if secondary:
            pieces.append(f"次要机制包括：{', '.join(secondary)}。")
        pieces.append("需结合文本、上下文和反证判断，避免只按关键词下结论。")
        reasoning["encoding_analysis"] = pieces

    if not reasoning["context_analysis"]:
        context_bits = [
            context.get("title", ""),
            context.get("parent_comment", ""),
            " / ".join(context.get("reply_chain", [])),
            context.get("time", ""),
            context.get("topic", ""),
        ]
        context_text = "；".join(bit for bit in context_bits if bit)
        reasoning["context_analysis"] = [f"可用上下文：{context_text}。" if context_text else "缺少明确上下文，需谨慎判断。"]

    if risk == "high":
        if not reasoning["supporting_evidence"]:
            reasoning["supporting_evidence"] = ["文本含较明确的编码信号。", "上下文对非字面解释形成支持。"]
        reasoning["counter_evidence"] = reasoning["counter_evidence"] or ["不直接还原具体目标名称，保留匿名化或概括表述。"]
    elif risk == "medium":
        if not reasoning["supporting_evidence"]:
            reasoning["supporting_evidence"] = ["存在可疑编码或语境信号。"]
        reasoning["counter_evidence"] = reasoning["counter_evidence"] or ["目标指向或上下文证据仍不充分，普通解释仍可能成立。"]
    elif risk == "low":
        if not reasoning["supporting_evidence"]:
            reasoning["supporting_evidence"] = ["存在弱暗示、关键词撞车或候选编码痕迹。"]
        reasoning["counter_evidence"] = reasoning["counter_evidence"] or [
            "上下文更支持普通解释。",
            "缺少规避意图、稳定目标映射或强语境共识。",
        ]
    else:
        reasoning["supporting_evidence"] = []
        reasoning["counter_evidence"] = reasoning["counter_evidence"] or [
            "上下文明确支持普通解释。",
            "没有规避检测意图、隐含目标或异常互动共识。",
        ]

    if not reasoning["final_rationale"]:
        reasoning["final_rationale"] = f"综合文本、上下文和反证，暂标为 {risk}；该条来自 {source} 扩写，仍需人工复核。"

    return reasoning


def normalize_sample(sample: dict[str, Any], *, source: str, index: int) -> dict[str, Any]:
    raw_text = str(sample.get("text", "")).strip()
    text = extract_reply_text(raw_text) if source == "gemini" else raw_text
    risk = normalize_risk(sample.get("risk_level"))
    context = ensure_context(sample.get("context", {}), raw_text)
    if not context.get("topic"):
        context["topic"] = extract_cluster(sample)
    primary = infer_primary({**sample, "text": raw_text}, risk, source)
    secondary = normalize_secondary(sample.get("encoding_secondary"))
    secondary = [item for item in secondary if item != primary]
    if risk == "none":
        primary = "none"
        secondary = []

    hard_negative = bool(sample.get("hard_negative")) and risk in {"none", "low"}
    if risk == "none":
        hard_negative = True

    prefix = "MEME_EXPAND" if source == "meme" else "GEMINI_EXPAND"
    original_id = str(sample.get("id") or f"EXPAND_{index:04d}").strip()

    return {
        "id": f"{prefix}_{index:04d}_{risk.upper()}",
        "split": "train",
        "source_type": "synthetic",
        "platform": normalize_platform(sample.get("platform")),
        "text": text,
        "context": context,
        "risk_level": risk,
        "encoding_primary": primary,
        "encoding_secondary": secondary,
        "context_required": context_required(sample, risk, primary, context),
        "ambiguity": normalize_ambiguity(sample.get("ambiguity"), risk),
        "evidence_strength": normalize_evidence(sample.get("evidence_strength"), risk),
        "freshness": "stable",
        "hard_negative": hard_negative,
        "target_known": risk == "high",
        "target_reference": "匿名化目标对象或事件" if risk in {"high", "medium"} else "",
        "should_explain_target": False,
        "reasoning": normalize_reasoning(
            sample,
            text=text,
            context=context,
            risk=risk,
            primary=primary,
            secondary=secondary,
            source=source,
        ),
        "quality_status": "needs_revision",
        "review_notes": (
            f"source={source}_expansion; original_id={original_id}; "
            f"generated_expansion; needs_human_review; "
            f"original_primary={sample.get('encoding_primary', '')}; "
            f"original_notes={sample.get('review_notes', '')}"
        ),
    }


def main() -> int:
    base_samples = [
        sample
        for sample in load_jsonl(BASE_PATH)
        if not str(sample.get("id", "")).startswith(("MEME_EXPAND_", "GEMINI_EXPAND_"))
    ]
    meme_samples = [
        normalize_sample(sample, source="meme", index=index)
        for index, sample in enumerate(load_jsonl(MEME_RAW_PATH), start=1)
    ]
    gemini_samples = [
        normalize_sample(sample, source="gemini", index=index)
        for index, sample in enumerate(load_jsonl(GEMINI_RAW_PATH), start=1)
    ]
    expansion_samples = meme_samples + gemini_samples
    merged_samples = base_samples + expansion_samples

    write_jsonl(expansion_samples, EXPAND_OUTPUT_PATH)
    write_jsonl(merged_samples, COMBINED_JSONL_PATH)
    write_json(merged_samples, COMBINED_JSON_PATH)

    print(f"Wrote {len(expansion_samples)} cleaned expansion samples to {EXPAND_OUTPUT_PATH}")
    print(f"Wrote {len(merged_samples)} merged samples to {COMBINED_JSONL_PATH}")
    print(f"Wrote {len(merged_samples)} merged samples to {COMBINED_JSON_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
