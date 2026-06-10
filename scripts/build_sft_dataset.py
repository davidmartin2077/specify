#!/usr/bin/env python3
"""Convert annotated risk-reasoning JSONL into SFT instruction data."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


DEFAULT_INSTRUCTION = (
    "请判断以下中文弹幕/评论是否存在隐晦风险表达。"
    "重点识别黑话、隐喻、反讽、指桑骂槐、历史影射、人物代指、数字代指、谐音或语境触发表达。"
    "默认先按文本本身判断；只有输入明确给出必要上下文时才使用上下文。"
    "请给出简短、可审计的分析，并输出风险等级和主要编码方式。"
)

SYSTEM_PROMPT = (
    "你是一个中文互联网语义风险推理模型。"
    "你的任务不是做关键词匹配，也不是强行脑补上下文；优先判断评论/弹幕本身是否有风险。"
    "只有文本本身模糊且上下文真实可用时，才把上下文作为证据。"
    "分析应简洁，避免过长推理；证据不足时降级。"
)

CONFIDENCE_BY_EVIDENCE = {
    "strong": {
        "high": 0.88,
        "medium": 0.74,
        "low": 0.42,
        "none": 0.18,
    },
    "moderate": {
        "high": 0.78,
        "medium": 0.66,
        "low": 0.36,
        "none": 0.14,
    },
    "weak": {
        "high": 0.62,
        "medium": 0.52,
        "low": 0.28,
        "none": 0.08,
    },
}


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    samples = []
    with path.open("r", encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, start=1):
            line = line.strip()
            if not line:
                continue
            try:
                sample = json.loads(line)
            except json.JSONDecodeError as exc:
                raise ValueError(f"{path}:{line_number}: invalid JSON: {exc.msg}") from exc
            if not isinstance(sample, dict):
                raise ValueError(f"{path}:{line_number}: expected a JSON object")
            samples.append(sample)
    return samples


def non_empty(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def format_context(context: dict[str, Any]) -> str:
    fields = [
        ("标题/场景", context.get("title", "")),
        ("简介", context.get("description", "")),
        ("时间", context.get("time", "")),
        ("话题", context.get("topic", "")),
    ]
    lines = [f"{label}: {value}" for label, value in fields if non_empty(value)]

    return "\n".join(lines) if lines else "无明确上下文"


def format_input(sample: dict[str, Any]) -> str:
    context = sample.get("context", {})
    if not isinstance(context, dict):
        context = {}
    needs_context = bool(sample.get("needs_context", False))
    context_text = format_context(context) if needs_context else "无明确上下文"

    return "\n".join(
        [
            f"平台: {sample.get('platform', 'unknown')}",
            f"文本: {sample.get('text', '')}",
            "上下文:",
            context_text,
        ]
    )


def bullet_lines(items: Any, fallback: str) -> list[str]:
    if isinstance(items, list):
        cleaned = [str(item).strip() for item in items if str(item).strip()]
        if cleaned:
            return [f"- {item}" for item in cleaned]
    return [f"- {fallback}"]


def confidence(sample: dict[str, Any]) -> float:
    evidence_strength = sample.get("evidence_strength", "weak")
    risk_level = sample.get("risk_level", "none")
    return CONFIDENCE_BY_EVIDENCE.get(evidence_strength, CONFIDENCE_BY_EVIDENCE["weak"]).get(risk_level, 0.5)


def format_output(sample: dict[str, Any]) -> str:
    reasoning = sample.get("reasoning", {})
    if not isinstance(reasoning, dict):
        reasoning = {}

    secondary = sample.get("encoding_secondary", [])
    if isinstance(secondary, list) and secondary:
        secondary_text = ", ".join(str(item) for item in secondary)
    else:
        secondary_text = "none"

    lines = [
        "## 字面层分析",
        *bullet_lines(reasoning.get("literal_analysis"), "文本字面含义需要结合原文判断。"),
        "",
        "## 编码机制分析",
        *bullet_lines(reasoning.get("encoding_analysis"), "未发现明确编码机制，或证据不足。"),
        "",
        "## 语境层分析",
        *bullet_lines(reasoning.get("context_analysis"), "缺少足够上下文，需要谨慎判断。"),
        "",
        "## 证据与反证",
        "支持风险:",
        *bullet_lines(reasoning.get("supporting_evidence"), "暂无强支持证据。"),
        "反证:",
        *bullet_lines(reasoning.get("counter_evidence"), "仍需考虑普通解释或上下文不足。"),
        "",
        "## 最终判定",
        f"risk_level: {sample.get('risk_level', 'none')}",
        f"encoding_primary: {sample.get('encoding_primary', 'none')}",
        f"encoding_secondary: {secondary_text}",
        f"needs_context: {str(sample.get('needs_context', False)).lower()}",
        f"confidence: {confidence(sample):.2f}",
        f"rationale: {reasoning.get('final_rationale', '综合判断见上。')}",
    ]
    return "\n".join(lines)


def build_record(sample: dict[str, Any]) -> dict[str, Any]:
    return {
        "instruction": DEFAULT_INSTRUCTION,
        "input": format_input(sample),
        "output": format_output(sample),
        "system": SYSTEM_PROMPT,
        "metadata": {
            "id": sample.get("id", ""),
            "risk_level": sample.get("risk_level", ""),
            "encoding_primary": sample.get("encoding_primary", ""),
            "encoding_secondary": sample.get("encoding_secondary", []),
            "needs_context": sample.get("needs_context", False),
            "ambiguity": sample.get("ambiguity", ""),
            "evidence_strength": sample.get("evidence_strength", ""),
            "hard_negative": sample.get("hard_negative", False),
            "quality_status": sample.get("quality_status", ""),
        },
    }


def write_jsonl(records: list[dict[str, Any]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        for record in records:
            handle.write(json.dumps(record, ensure_ascii=False, separators=(",", ":")) + "\n")


def write_json(records: list[dict[str, Any]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        json.dump(records, handle, ensure_ascii=False, indent=2)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build SFT instruction data from annotated JSONL samples.")
    parser.add_argument(
        "--input",
        type=Path,
        default=Path("data/processed/combined_candidates.jsonl"),
        help="Annotated JSONL file to convert.",
    )
    parser.add_argument(
        "--output-jsonl",
        type=Path,
        default=Path("data/mvp/sft_candidates.jsonl"),
        help="Output SFT JSONL path.",
    )
    parser.add_argument(
        "--output-json",
        type=Path,
        default=Path("data/mvp/sft_candidates.json"),
        help="Output SFT JSON array path.",
    )
    parser.add_argument(
        "--approved-only",
        action="store_true",
        help="Only include samples with quality_status=approved.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    samples = load_jsonl(args.input)
    if args.approved_only:
        samples = [sample for sample in samples if sample.get("quality_status") == "approved"]

    records = [build_record(sample) for sample in samples]
    write_jsonl(records, args.output_jsonl)
    write_json(records, args.output_json)

    print(f"Wrote {len(records)} SFT records to {args.output_jsonl}")
    print(f"Wrote {len(records)} SFT records to {args.output_json}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
