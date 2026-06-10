# 审查微调数据集

中文互联网语义风险推理数据集，用于后续微调/强化学习约 4B 模型。目标是让模型识别黑话、隐喻、反讽、历史影射、人物代指、规避写法和正常语境反证，不做简单敏感词匹配器。

## 当前状态

正式数据：

- `data/processed/combined_candidates.jsonl`
- `data/processed/combined_candidates.json`
- 样本数：775

分布：

```text
high    152
medium  272
low     163
none    188

hard_negative     315
context_required  724
```

训练格式：

- `data/mvp/sft_candidates.jsonl`
- `data/mvp/sft_candidates.json`
- 样本数：775

切分：

```text
train       621
validation   77
test         77
```

`data/processed/splits/split_report.json` 当前记录 281 个防泄漏 group，0 个跨 split 泄漏。

## 当前原则

- 单条文本能判断的，不硬凑上下文。
- 合成回复上下文不再作为强证据，也不进入 SFT 输入。
- 外部数据先保留为 raw 预览，不直接入正式训练集。
- 训练前所有正式 JSONL 必须通过 `scripts/validate_dataset.py`。

## 核心文件

- `schemas/sample_schema.json`
- `docs/annotation_guideline.md`
- `docs/encoding_taxonomy.md`
- `docs/risk_coverage_report.md`
- `docs/external_safety_datasets_review.md`
- `docs/external_safety_import_review_sample.md`
- `data/raw/external_safety_import_preview.jsonl`

## 常用命令

```bash
python3 scripts/validate_dataset.py data/processed/combined_candidates.jsonl
python3 scripts/build_sft_dataset.py
python3 scripts/split_dataset.py
python3 scripts/analyze_risk_coverage.py
```

## 下一步

1. 继续清理 `context_required`，把可裸判样本降为无上下文依赖。
2. 从外部 340 条真实评论预览中筛选可重塑样本。
3. 设计离线评测脚本，先测 unsafe recall 和 false positive。
