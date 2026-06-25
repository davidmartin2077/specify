#!/usr/bin/env python3
"""
Baseline evaluation: test the base Qwen 4B model on the test set BEFORE fine-tuning.

Usage:
    python3 scripts/baseline_eval.py

Output goes to baseline_results/:
    - baseline_summary.json    → overall metrics
    - baseline_details.jsonl   → per-sample results
    - baseline_report.txt      → human-readable report
"""

from __future__ import annotations

import json
import re
import time
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TEST_FILE = ROOT / "fine_tune" / "test_chatml.jsonl"
OUT_DIR = ROOT / "baseline_results"
OUT_DIR.mkdir(parents=True, exist_ok=True)

MODEL_NAME = "Qwen/Qwen3-4B-Instruct-2507"

# ── config ──────────────────────────────────────────────────
MAX_NEW_TOKENS = 512
TEMPERATURE = 0.0          # greedy, deterministic
BATCH_SIZE = 1             # safer for local eval
LIMIT = None               # set to 50 to test quickly, None = all
# ─────────────────────────────────────────────────────────────


def load_model_and_tokenizer():
    """Load model with best available backend for this machine."""
    import torch
    from transformers import AutoModelForCausalLM, AutoTokenizer

    print(f"Loading {MODEL_NAME} ...")

    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, trust_remote_code=True)

    # Pick the right device / dtype
    if torch.cuda.is_available():
        print("  → CUDA (NVIDIA GPU)")
        model = AutoModelForCausalLM.from_pretrained(
            MODEL_NAME,
            torch_dtype=torch.float16,
            device_map="auto",
            trust_remote_code=True,
        )
    elif hasattr(torch.backends, "mps") and torch.backends.mps.is_available():
        print("  → MPS (Apple Silicon)")
        model = AutoModelForCausalLM.from_pretrained(
            MODEL_NAME,
            torch_dtype=torch.float16,
            device_map="mps",
            trust_remote_code=True,
        )
    else:
        print("  → CPU (slow, expect ~5-10s per sample)")
        model = AutoModelForCausalLM.from_pretrained(
            MODEL_NAME,
            torch_dtype=torch.float32,
            device_map="cpu",
            trust_remote_code=True,
        )

    model.eval()
    return model, tokenizer


def extract_fields(text: str) -> dict:
    """Pull risk_level / encoding / hard_negative out of generated text."""
    risk = re.search(r"风险等级:\s*(\S+)", text)
    enc = re.search(r"主要编码:\s*(\S+)", text)
    hn = re.search(r"硬负样本:\s*(\S+)", text)
    return {
        "risk_level": risk.group(1) if risk else "?",
        "encoding_primary": enc.group(1) if enc else "?",
        "hard_negative": hn.group(1) if hn else "?",
    }


def run_baseline():
    model, tokenizer = load_model_and_tokenizer()

    # Load test samples
    samples = []
    with open(TEST_FILE, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                samples.append(json.loads(line))

    if LIMIT:
        samples = samples[:LIMIT]

    print(f"Evaluating {len(samples)} test samples ...\n")

    results = []
    correct_risk = 0
    correct_enc = 0

    t0 = time.time()

    for idx, sample in enumerate(samples):
        messages = sample["messages"]

        # Ground truth from assistant
        gt_text = ""
        for msg in messages:
            if msg["role"] == "assistant":
                gt_text = msg["content"]
                break
        gt = extract_fields(gt_text)

        # Build input: system + user only
        input_msgs = [msg for msg in messages if msg["role"] in ("system", "user")]
        prompt = tokenizer.apply_chat_template(
            input_msgs,
            tokenize=False,
            add_generation_prompt=True,
        )

        inputs = tokenizer(prompt, return_tensors="pt").to(model.device)

        with torch.no_grad():
            outputs = model.generate(
                **inputs,
                max_new_tokens=MAX_NEW_TOKENS,
                temperature=TEMPERATURE,
                do_sample=False,
                pad_token_id=tokenizer.pad_token_id,
            )

        generated = tokenizer.decode(
            outputs[0][inputs["input_ids"].shape[1]:],
            skip_special_tokens=True,
        )
        pred = extract_fields(generated)

        # Compare
        risk_match = pred["risk_level"] == gt["risk_level"]
        enc_match = pred["encoding_primary"] == gt["encoding_primary"]

        if risk_match:
            correct_risk += 1
        if enc_match:
            correct_enc += 1

        results.append({
            "idx": idx,
            "gt_risk": gt["risk_level"],
            "pred_risk": pred["risk_level"],
            "risk_correct": risk_match,
            "gt_encoding": gt["encoding_primary"],
            "pred_encoding": pred["encoding_primary"],
            "enc_correct": enc_match,
            "gt_hard_negative": gt["hard_negative"],
            "pred_hard_negative": pred["hard_negative"],
            "generated": generated,
        })

        if (idx + 1) % 20 == 0:
            elapsed = time.time() - t0
            rate = (idx + 1) / elapsed
            eta = (len(samples) - idx - 1) / rate
            print(f"  [{idx+1}/{len(samples)}] "
                  f"risk_acc={correct_risk/(idx+1):.3f}  "
                  f"enc_acc={correct_enc/(idx+1):.3f}  "
                  f"eta={eta:.0f}s")

    elapsed = time.time() - t0
    n = len(samples)

    # ── summary ──
    summary = {
        "model": MODEL_NAME,
        "num_samples": n,
        "risk_accuracy": correct_risk / n,
        "encoding_accuracy": correct_enc / n,
        "elapsed_seconds": round(elapsed, 1),
        "samples_per_second": round(n / elapsed, 2),
    }

    # ── per-class breakdown ──
    from collections import Counter
    risk_matrix = Counter()
    for r in results:
        risk_matrix[(r["gt_risk"], r["pred_risk"])] += 1
    summary["risk_confusion"] = {
        f"{k[0]}→{k[1]}": v for k, v in sorted(risk_matrix.items())
    }

    # ── save ──
    with open(OUT_DIR / "baseline_summary.json", "w", encoding="utf-8") as f:
        json.dump(summary, f, ensure_ascii=False, indent=2)

    with open(OUT_DIR / "baseline_details.jsonl", "w", encoding="utf-8") as f:
        for r in results:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")

    # ── report ──
    report = f"""\
Baseline Evaluation Report
==========================
Model: {MODEL_NAME}
Samples: {n}
Time: {elapsed:.0f}s ({n/elapsed:.1f} samples/s)

Risk Level Accuracy: {correct_risk/n:.4f}  ({correct_risk}/{n})
Encoding Accuracy:   {correct_enc/n:.4f}  ({correct_enc}/{n})

Confusion Matrix (gt → pred):
"""
    for (gt, pred), count in sorted(risk_matrix.items()):
        report += f"  {gt:>6} → {pred:<6}  {count:>4}\n"

    report += f"\nDone. Full details in baseline_details.jsonl\n"

    with open(OUT_DIR / "baseline_report.txt", "w", encoding="utf-8") as f:
        f.write(report)

    print(f"\n{report}")


if __name__ == "__main__":
    import torch
    run_baseline()
