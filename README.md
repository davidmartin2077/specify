# 审查微调数据集

中文互联网语义风险推理数据集，用于微调/强化学习约 4B 模型。目标是让模型识别黑话、隐喻、反讽、历史影射、人物代指、规避写法和正常语境反证，不做简单敏感词匹配器。

## 核心文件

```
schemas/sample_schema.json          # 数据 schema
docs/annotation_guideline.md        # 标注规范
docs/encoding_taxonomy.md           # 编码方式分类手册
docs/risk_coverage_report.md        # 风险覆盖报告
data/processed/combined_candidates.jsonl  # 正式数据 (1295 条)
data/processed/sft/sft_candidates.jsonl   # SFT 训练格式
data/processed/splits/              # train/validation/test 切分
data/processed/manifest.json        # 当前数据与派生产物版本清单
```

## 正式数据

| 指标 | 数值 |
|---|---|
| 总样本 | 1295 |
| real / synthetic | 480 / 815 |
| high | 444 |
| medium | 383 |
| low | 131 |
| none | 337 |
| hard_negative | 405 |
| needs_context | 45 |
| quality_status | reviewed 1133 / approved 162 |

主要来源：ToxiCN/COLD/ChineseSafe 各 160，batch1-12 与 replace_phase3_v2 系列合成/替换样本，user 7。

切分：train 1037 / validation 129 / test 129，1292 个防泄漏 group，0 泄漏。

## 关键原则

- 单条文本能判断的，不硬凑上下文。
- 不把合成回复上下文作为强证据。
- high 不强制需要上下文；直白风险、强暗号、稳定代指可以裸判。
- 面向弹幕、应用评论、音乐评论等短文本场景。
- 已固化、出圈、高频的鉴证圈结构梗本身就是文本证据，可以无上下文判 high。
- 训练前所有正式 JSONL 必须通过 `python3 scripts/validate_dataset.py`。
- 训练只能使用从当前 `combined_candidates.jsonl` 重建后的 SFT；如 `manifest.json` 显示不同步，不要训练。

## 常用命令

```bash
python3 scripts/rebuild_dataset_artifacts.py

# 或逐步执行：
python3 scripts/validate_dataset.py data/processed/combined_candidates.jsonl
python3 scripts/build_sft_dataset.py
python3 scripts/split_dataset.py
python3 scripts/analyze_risk_coverage.py
python3 scripts/build_manifest.py
```

推荐在每个数据 batch 完成后按上方顺序刷新派生产物；`combined_candidates.jsonl` 是母版，SFT、split、coverage report 和 manifest 都是可重建产物。

## 微调前评测

先导出验证集和测试集 prompt：

```bash
python3 scripts/build_eval_set.py
```

让基座模型或微调模型对 `data/eval/validation_prompts.jsonl` 逐条生成预测，保存为 JSONL。每行至少包含 `id` 和以下任一种形式：

```json
{"id": "000001", "risk_level": "high", "encoding_primary": "A1_普通谐音", "hard_negative": false}
```

或包含可解析的模型原文输出：

```json
{"id": "000001", "output": "...\nrisk_level: high\nencoding_primary: A1_普通谐音\nhard_negative: false"}
```

然后计算指标：

```bash
python3 scripts/evaluate_predictions.py \
  --gold data/eval/validation_prompts.jsonl \
  --predictions data/eval/validation_predictions.jsonl \
  --output data/eval/validation_eval_report.json
```

## 下一步

1. 跑基座模型 baseline，保存 `data/eval/validation_predictions.jsonl` 并生成评测报告。
2. 继续补充 low、needs_context 与 hard_negative 边界样本。
3. 后续外部数据入库走 `scripts/fuse_external_real_datasets.py`。
