# Fine-tuning Dataset

Source: 4850 samples from combined_candidates.jsonl

## Formats

### Alpaca (`*_alpaca.jsonl`)
Compatible with: LLaMA-Factory, Firefly, FastChat, Stanford Alpaca

```json
{"instruction": "系统提示...", "input": "请判断...", "output": "【字面分析】..."}
```

### ChatML (`*_chatml.jsonl`)
Compatible with: Qwen, ChatGLM, OpenAI fine-tuning API

```json
{"messages": [{"role": "system", "content": "..."}, {"role": "user", "content": "..."}, {"role": "assistant", "content": "..."}]}
```

## Splits

| Split | Alpaca | ChatML |
|:--|:--|:--|
| train | train_alpaca.jsonl | train_chatml.jsonl |
| validation | validation_alpaca.jsonl | validation_chatml.jsonl |
| test | test_alpaca.jsonl | test_chatml.jsonl |

## Output Structure

每条回复包含：字面分析 → 编码分析 → 语境分析 → 证据评估 → 最终判定（风险等级+编码+硬负样本+判定理由）
