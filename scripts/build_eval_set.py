#!/usr/bin/env python3
"""Build model-facing evaluation prompts from split JSONL files."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SPLITS_DIR = ROOT / "data/processed/splits"
DEFAULT_OUTPUT_DIR = ROOT / "data/eval"

SYSTEM_PROMPT = (
    "你是一个中文互联网语义风险推理模型。"
    "你的任务是判断文本是否存在隐晦风险表达，而不是简单关键词匹配。"
    "请输出简短分析，并在最后给出：risk_level、encoding_primary、hard_negative。"
)

USER_TEMPLATE = "请判断以下文本是否存在隐晦风险：\n\n{text}"


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


def make_prompt(sample: dict[str, Any]) -> str:
    prompt = USER_TEMPLATE.format(text=sample.get("text", ""))
    context = sample.get("context", {})
    if sample.get("needs_context") and isinstance(context, dict) and context.get("description"):
        prompt += f"\n\n补充上下文: {context['description']}"
    return prompt


def build_record(sample: dict[str, Any]) -> dict[str, Any]:
    return {
        "id": sample.get("id"),
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": make_prompt(sample)},
        ],
        "gold": {
            "risk_level": sample.get("risk_level"),
            "encoding_primary": sample.get("encoding_primary"),
            "hard_negative": sample.get("hard_negative"),
            "needs_context": sample.get("needs_context"),
            "ambiguity": sample.get("ambiguity"),
            "evidence_strength": sample.get("evidence_strength"),
        },
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build model-facing evaluation JSONL files.")
    parser.add_argument("--splits-dir", type=Path, default=DEFAULT_SPLITS_DIR)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument(
        "--splits",
        default="validation,test",
        help="Comma-separated split names to export. Default: validation,test.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)

    for split in [part.strip() for part in args.splits.split(",") if part.strip()]:
        source = args.splits_dir / f"{split}.jsonl"
        rows = load_jsonl(source)
        output = args.output_dir / f"{split}_prompts.jsonl"
        with output.open("w", encoding="utf-8") as handle:
            for row in rows:
                handle.write(json.dumps(build_record(row), ensure_ascii=False) + "\n")
        print(f"{split}: wrote {len(rows)} prompts to {output.relative_to(ROOT)}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
