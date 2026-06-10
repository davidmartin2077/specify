# 审查微调数据集

中文互联网语义风险推理数据集，用于后续微调/强化学习约 4B 模型。目标是让模型识别黑话、隐喻、反讽、历史影射、人物代指、规避写法和正常语境反证，不做简单敏感词匹配器。

## 当前状态

正式数据：

- `data/processed/combined_candidates.jsonl`
- `data/processed/combined_candidates.json`
- 样本数：775

分布：

```text
high    155
medium  268
low     162
none    190

hard_negative     322
context_required  237
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
- high 不强制需要上下文；直白风险、强暗号、稳定代指可以裸判。
- 面向弹幕、应用评论、音乐评论等短文本场景；不可公开存在或不可观测的敏感背景不能用来抬高风险。
- 已固化、出圈、高频的鉴证圈结构梗本身就是文本证据，可以无上下文判 high。
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

1. 继续把陈述句、人机感、病句样本替换成真实评论口吻。
2. 从外部 340 条真实评论预览中筛选可重塑样本。
3. 设计离线评测脚本，先测 unsafe recall 和 false positive。
