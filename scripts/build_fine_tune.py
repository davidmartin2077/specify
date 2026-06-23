#!/usr/bin/env python3
"""
Build fine-tuning-ready datasets from combined_candidates.jsonl.
Outputs two formats:
  1. Alpaca (instruction/input/output) — compatible with LLaMA-Factory, Firefly, etc.
  2. ChatML (messages array) — compatible with Qwen, ChatGLM, OpenAI fine-tuning

Reads train/val/test assignments from data/processed/splits/ to ensure consistency.
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CANDIDATES = ROOT / "data/processed/combined_candidates.jsonl"
SPLITS_DIR = ROOT / "data/processed/splits"
OUT_DIR = ROOT / "fine_tune"
OUT_DIR.mkdir(parents=True, exist_ok=True)

SYSTEM_PROMPT = (
    "你是一个中文互联网语义风险推理模型。"
    "你的任务是根据文本内容判断是否存在隐晦风险表达，而非仅做关键词匹配。"
    "重点识别：黑话、隐喻、反讽、历史影射、人物代指、数字代指、谐音、语境触发表达。"
    "默认基于文本本身判断；仅当上下文明确可用且文本模糊时才使用上下文。"
    "证据不足时应降级判定。"
)

USER_TEMPLATE = "请判断以下文本是否存在隐晦风险：\n\n{text}"

def build_output(sample: dict) -> str:
    """Build compact but complete reasoning output."""
    r = sample.get("reasoning", {})
    if not isinstance(r, dict):
        r = {}

    def items(field: str) -> list[str]:
        v = r.get(field, [])
        if isinstance(v, str):
            return [v]
        return v if isinstance(v, list) else []

    lit = items("literal_analysis")
    enc = items("encoding_analysis")
    ctx = items("context_analysis")
    sup = items("supporting_evidence")
    cnt = items("counter_evidence")
    fr = r.get("final_rationale", "")

    es = sample.get("encoding_secondary", [])
    es_str = ", ".join(es) if es else "无"

    parts = []

    # Literal
    if lit:
        parts.append("【字面分析】\n" + "\n".join(f"· {x}" for x in lit))

    # Encoding
    if enc:
        parts.append("【编码分析】\n" + "\n".join(f"· {x}" for x in enc))

    # Context
    if ctx:
        parts.append("【语境分析】\n" + "\n".join(f"· {x}" for x in ctx))

    # Evidence
    if sup or cnt:
        ev_lines = []
        if sup:
            ev_lines.append("支持风险：")
            ev_lines.extend(f"  + {x}" for x in sup)
        if cnt:
            ev_lines.append("反证：")
            ev_lines.extend(f"  - {x}" for x in cnt)
        parts.append("【证据评估】\n" + "\n".join(ev_lines))

    # Judgment
    judgment = (
        f"【最终判定】\n"
        f"风险等级: {sample.get('risk_level', 'none')}\n"
        f"主要编码: {sample.get('encoding_primary', 'none')}\n"
        f"辅助编码: {es_str}\n"
        f"硬负样本: {'是' if sample.get('hard_negative') else '否'}\n"
        f"判定理由: {fr}"
    )
    parts.append(judgment)

    return "\n\n".join(parts)


def main():
    # Load samples
    with open(CANDIDATES, encoding="utf-8") as f:
        all_samples = [json.loads(line) for line in f if line.strip()]

    samples_by_id = {s["id"]: s for s in all_samples}

    for split_name in ("train", "validation", "test"):
        split_path = SPLITS_DIR / f"{split_name}.jsonl"
        with open(split_path, encoding="utf-8") as f:
            split_samples = [json.loads(line) for line in f if line.strip()]

        alpaca_records = []
        chatml_records = []

        for s in split_samples:
            text = s.get("text", "")
            needs_ctx = s.get("needs_context", False)
            ctx = s.get("context", {})
            if not isinstance(ctx, dict):
                ctx = {}

            # Build user input — only add context if needed
            user_input = USER_TEMPLATE.format(text=text)
            if needs_ctx and ctx.get("description"):
                user_input += f"\n\n补充上下文: {ctx['description']}"

            output = build_output(s)

            # Alpaca format
            alpaca_records.append({
                "instruction": SYSTEM_PROMPT,
                "input": user_input,
                "output": output,
            })

            # ChatML format
            chatml_records.append({
                "messages": [
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": user_input},
                    {"role": "assistant", "content": output},
                ]
            })

        # Write Alpaca
        alpaca_path = OUT_DIR / f"{split_name}_alpaca.jsonl"
        with open(alpaca_path, "w", encoding="utf-8") as f:
            for r in alpaca_records:
                f.write(json.dumps(r, ensure_ascii=False) + "\n")

        # Write ChatML
        chatml_path = OUT_DIR / f"{split_name}_chatml.jsonl"
        with open(chatml_path, "w", encoding="utf-8") as f:
            for r in chatml_records:
                f.write(json.dumps(r, ensure_ascii=False) + "\n")

        print(f"{split_name}: {len(alpaca_records)} records → {alpaca_path.name}, {chatml_path.name}")

    # Write a README
    readme = OUT_DIR / "README.md"
    readme.write_text(
        "# Fine-tuning Dataset\n\n"
        f"Source: {len(all_samples)} samples from combined_candidates.jsonl\n\n"
        "## Formats\n\n"
        "### Alpaca (`*_alpaca.jsonl`)\n"
        "Compatible with: LLaMA-Factory, Firefly, FastChat, Stanford Alpaca\n\n"
        "```json\n"
        '{"instruction": "系统提示...", "input": "请判断...", "output": "【字面分析】..."}\n'
        "```\n\n"
        "### ChatML (`*_chatml.jsonl`)\n"
        "Compatible with: Qwen, ChatGLM, OpenAI fine-tuning API\n\n"
        "```json\n"
        '{"messages": [{"role": "system", "content": "..."}, {"role": "user", "content": "..."}, {"role": "assistant", "content": "..."}]}\n'
        "```\n\n"
        "## Splits\n\n"
        f"| Split | Alpaca | ChatML |\n"
        f"|:--|:--|:--|\n"
        f"| train | train_alpaca.jsonl | train_chatml.jsonl |\n"
        f"| validation | validation_alpaca.jsonl | validation_chatml.jsonl |\n"
        f"| test | test_alpaca.jsonl | test_chatml.jsonl |\n\n"
        "## Output Structure\n\n"
        "每条回复包含：字面分析 → 编码分析 → 语境分析 → 证据评估 → 最终判定（风险等级+编码+硬负样本+判定理由）\n",
        encoding="utf-8",
    )
    print(f"\nWrote README to {readme}")


if __name__ == "__main__":
    main()
