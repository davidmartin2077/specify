#!/usr/bin/env python3
"""
LoRA fine-tune Qwen 4B on the train split, validate on validation split.

Usage:
    python3 scripts/train_lora.py

Output goes to lora_output/:
    - adapter_model/          → LoRA weights (load with PEFT)
    - trainer_state/          → training logs (TensorBoard)
    - training_metrics.json   → final metrics
"""

from __future__ import annotations

import json
import os
from pathlib import Path

import torch
from datasets import Dataset
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    TrainingArguments,
    BitsAndBytesConfig,
)
from peft import LoraConfig, get_peft_model, prepare_model_for_kbit_training
from trl import SFTTrainer

ROOT = Path(__file__).resolve().parents[1]
TRAIN_FILE = ROOT / "fine_tune" / "train_chatml.jsonl"
VAL_FILE = ROOT / "fine_tune" / "validation_chatml.jsonl"
OUT_DIR = ROOT / "lora_output"
OUT_DIR.mkdir(parents=True, exist_ok=True)

MODEL_NAME = "Qwen/Qwen3-4B-Instruct-2507"

# ── hyperparameters ─────────────────────────────────────────
LORA_R = 16
LORA_ALPHA = 32
LORA_DROPOUT = 0.05
LEARNING_RATE = 5e-5
NUM_EPOCHS = 3
BATCH_SIZE = 2                # small for local GPU
GRADIENT_ACCUMULATION = 4     # effective batch = 2 × 4 = 8
MAX_SEQ_LENGTH = 2048
WARMUP_RATIO = 0.1
LOGGING_STEPS = 20
SAVE_STEPS = 200
EVAL_STEPS = 200
# ─────────────────────────────────────────────────────────────


def load_chatml_dataset(path: Path) -> Dataset:
    """Load a ChatML .jsonl file into a HuggingFace Dataset."""
    data = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                data.append(json.loads(line))
    return Dataset.from_list(data)


def formatting_func(example):
    """SFTTrainer expects tokenized text; we give it raw messages,
    and it handles the chat template for us."""
    return example["messages"]


def main():
    # ── detect device ──
    if torch.cuda.is_available():
        print("CUDA GPU detected — using 4-bit quantization")
        use_4bit = True
        device_map = "auto"
    elif hasattr(torch.backends, "mps") and torch.backends.mps.is_available():
        print("Apple Silicon (MPS) detected — using full precision")
        use_4bit = False
        device_map = "mps"
    else:
        print("CPU only — this will be very slow. Consider using a GPU.")
        use_4bit = False
        device_map = "cpu"

    # ── load model & tokenizer ──
    print(f"\nLoading {MODEL_NAME} ...")
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, trust_remote_code=True)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    if use_4bit:
        bnb_config = BitsAndBytesConfig(
            load_in_4bit=True,
            bnb_4bit_compute_dtype=torch.float16,
            bnb_4bit_use_double_quant=True,
        )
        model = AutoModelForCausalLM.from_pretrained(
            MODEL_NAME,
            quantization_config=bnb_config,
            device_map=device_map,
            trust_remote_code=True,
        )
        model = prepare_model_for_kbit_training(model)
    else:
        model = AutoModelForCausalLM.from_pretrained(
            MODEL_NAME,
            torch_dtype=torch.float16,
            device_map=device_map,
            trust_remote_code=True,
        )

    # ── LoRA ──
    lora_config = LoraConfig(
        r=LORA_R,
        lora_alpha=LORA_ALPHA,
        lora_dropout=LORA_DROPOUT,
        target_modules=["q_proj", "k_proj", "v_proj", "o_proj",
                        "gate_proj", "up_proj", "down_proj"],
        bias="none",
        task_type="CAUSAL_LM",
    )
    model = get_peft_model(model, lora_config)
    model.print_trainable_parameters()

    # ── load data ──
    print(f"\nLoading train: {TRAIN_FILE}")
    train_ds = load_chatml_dataset(TRAIN_FILE)
    print(f"Loading val:   {VAL_FILE}")
    val_ds = load_chatml_dataset(VAL_FILE)
    print(f"  train={len(train_ds)}  val={len(val_ds)}")

    # ── training args ──
    training_args = TrainingArguments(
        output_dir=str(OUT_DIR),
        per_device_train_batch_size=BATCH_SIZE,
        per_device_eval_batch_size=BATCH_SIZE,
        gradient_accumulation_steps=GRADIENT_ACCUMULATION,
        learning_rate=LEARNING_RATE,
        num_train_epochs=NUM_EPOCHS,
        warmup_ratio=WARMUP_RATIO,
        logging_steps=LOGGING_STEPS,
        save_steps=SAVE_STEPS,
        eval_steps=EVAL_STEPS,
        evaluation_strategy="steps",
        save_total_limit=2,
        load_best_model_at_end=True,
        metric_for_best_model="eval_loss",
        greater_is_better=False,
        fp16=use_4bit,          # only on CUDA
        bf16=False,
        remove_unused_columns=False,
        report_to="tensorboard",
    )

    # ── trainer ──
    trainer = SFTTrainer(
        model=model,
        args=training_args,
        train_dataset=train_ds,
        eval_dataset=val_ds,
        tokenizer=tokenizer,
        max_seq_length=MAX_SEQ_LENGTH,
        formatting_func=formatting_func,
    )

    # ── train ──
    print("\nStarting training ...\n")
    trainer.train()

    # ── save ──
    adapter_path = OUT_DIR / "adapter_model"
    trainer.model.save_pretrained(str(adapter_path))
    tokenizer.save_pretrained(str(adapter_path))
    print(f"\nLoRA adapter saved to {adapter_path}")

    # ── final metrics ──
    metrics = {}
    for log in trainer.state.log_history:
        if "eval_loss" in log:
            metrics[f"step_{log['step']}"] = {
                "eval_loss": log.get("eval_loss"),
                "learning_rate": log.get("learning_rate"),
            }
    with open(OUT_DIR / "training_metrics.json", "w") as f:
        json.dump(metrics, f, indent=2)

    best_eval = min(
        (v["eval_loss"] for v in metrics.values() if v.get("eval_loss")),
        default=None,
    )
    print(f"Best eval loss: {best_eval}")
    print("Done.")


if __name__ == "__main__":
    main()
