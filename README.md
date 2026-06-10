# 审查微调数据集

中文互联网语义风险推理数据集，用于微调/强化学习约 4B 模型。目标是让模型识别黑话、隐喻、反讽、历史影射、人物代指、规避写法和正常语境反证，不做简单敏感词匹配器。

## 核心文件

```
schemas/sample_schema.json          # 数据 schema
docs/annotation_guideline.md        # 标注规范
docs/encoding_taxonomy.md           # 编码方式分类手册
docs/risk_coverage_report.md        # 风险覆盖报告
data/processed/combined_candidates.jsonl  # 正式数据 (1255 条)
data/processed/splits/              # train/validation/test 切分
```

## 正式数据

| 指标 | 数值 |
|---|---|
| 总样本 | 1255 |
| high | 251 |
| medium | 460 |
| low | 162 |
| none | 382 |
| hard_negative | 509 |
| needs_context | 237 |

来源：grok(50) + user(7) + meme(35) + gemini(120) + lexicon(33) + phase2(100) + phase3(245+185) + ToxiCN/COLD/ChineseSafe(各160)

切分：train 1005 / validation 125 / test 125，607 个防泄漏 group，0 泄漏。

## 关键原则

- 单条文本能判断的，不硬凑上下文。
- 不把合成回复上下文作为强证据。
- high 不强制需要上下文；直白风险、强暗号、稳定代指可以裸判。
- 面向弹幕、应用评论、音乐评论等短文本场景。
- 已固化、出圈、高频的鉴证圈结构梗本身就是文本证据，可以无上下文判 high。
- 训练前所有正式 JSONL 必须通过 `python3 scripts/validate_dataset.py`。

## 常用命令

```bash
python3 scripts/validate_dataset.py data/processed/combined_candidates.jsonl
python3 scripts/build_sft_dataset.py
python3 scripts/split_dataset.py
python3 scripts/analyze_risk_coverage.py
```

## 下一步

1. 替换人机感强、模板感强的旧合成样本为真实评论口吻。
2. 建离线评测脚本，测 unsafe recall 和 false positive。
3. 后续外部数据入库走 `scripts/fuse_external_real_datasets.py`。
