# 审查微调项目

本仓库用于构建中文互联网语义风险推理/审核微调数据集。目标不是训练敏感词匹配器，而是让约 4B 规模的小模型学习：

1. 识别黑话、隐喻、反讽、指桑骂槐、历史影射、人物代指等非字面表达。
2. 拆解谐音、拼音首字母、拆字、形近字、符号空格、数字代指、平台黑话和组合编码。
3. 结合标题、上级评论、回复链、时间节点和话题语境判断风险等级。
4. 输出可审计的证据、反证和简洁结论，避免只凭关键词误杀正常表达。

当前阶段仍是**数据准备与人工复核**，尚未进入正式训练配置、训练运行或模型评测阶段。

## 当前进度

截至当前提交：

| 项目 | 状态 |
|---|---:|
| 正式 processed 候选 | 675 条 |
| SFT 数据 | 675 条 |
| 默认 train/validation/test split | 已生成并校验 |
| 防泄漏 group | 226 个，0 个跨 split 泄漏 |
| 第三阶段第二波 raw | 185 条，尚未入库 |
| 第二波人工复核清单 | 44 条，等待人工点评 |

正式候选集：

- `data/processed/combined_candidates.jsonl`
- `data/processed/combined_candidates.json`

正式数据分布：

```text
high    126
medium  234
low     145
none    170

hard_negative        279
context_required     624
quality_status       全部 needs_revision
```

当前 split：

```text
train       541
validation   67
test         67
```

## 当前最重要的注意事项

第二波 185 条只是 raw 候选，**不要直接入库**：

- `data/raw/phase3_second_wave_candidates.jsonl`
- 全部为 `needs_revision/not_merged`
- 已通过 schema、ID/text 查重
- 但风格审计标出 10 条 `reviewer_voice`
- 问题集中在 `weak_signal`，部分 text 像审核分析，不像真实评论

请优先查看：

- `docs/phase3_second_wave_review_sample.md`
- `data/raw/phase3_second_wave_review_sample.json`

下一步应先人工点评这 44 条分层样本，再决定是否重写第二波问题样本。不要在人工确认前运行合并入库。

## 关键文档

- `agent.md`：项目交接记忆。新窗口接手时必须先读。
- `docs/encoding_taxonomy.md`：编码方式分类手册。
- `docs/annotation_guideline.md`：标注规范、JSONL 字段、风险等级、hard negative 规则。
- `docs/risk_coverage_report.md`：基于正式 675 条的风险覆盖分析。
- `docs/phase3_coverage_delta.md`：phase2 + phase3 第一波入库前后的覆盖增益。
- `docs/phase3_second_wave_review_sample.md`：第二波 44 条人工复核清单。
- `docs/high_recall_style_migration.md`：高召回风格迁移原则。
- `docs/data_expansion_plan.md`：扩充计划。

## 目录结构

```text
configs/           训练与强化学习配置占位
data/raw/          原始输入、raw 候选、预览和人工复核清单
data/processed/    正式候选、覆盖报告、split 和采样计划
data/mvp/          SFT 数据
data/eval/         专项评测集占位
docs/              规则、报告、复核清单和项目说明
schemas/           JSON schema
scripts/           生成、导入、校验、切分和覆盖分析脚本
```

## 常用命令

校验正式 processed：

```bash
python3 scripts/validate_dataset.py data/processed/combined_candidates.jsonl
```

校验三份 split：

```bash
python3 scripts/validate_dataset.py \
  data/processed/splits/train.jsonl \
  data/processed/splits/validation.jsonl \
  data/processed/splits/test.jsonl
```

重建 SFT：

```bash
python3 scripts/build_sft_dataset.py
```

重建防泄漏切分：

```bash
python3 scripts/split_dataset.py
```

重跑正式 675 条覆盖分析：

```bash
python3 scripts/analyze_risk_coverage.py
```

重建第二波 raw 候选：

```bash
python3 scripts/build_phase3_second_wave_candidates.py
python3 scripts/validate_dataset.py data/raw/phase3_second_wave_candidates.jsonl
python3 scripts/audit_text_style.py \
  --input data/raw/phase3_second_wave_candidates.jsonl \
  --output data/raw/phase3_second_wave_text_style_audit.json
```

重建第二波人工复核清单：

```bash
python3 scripts/build_phase3_second_wave_review_sample.py
```

## 数据入库原则

1. raw 候选先人工抽样确认，不直接进入 processed。
2. 入库前必须生成独立合并预览。
3. 合并预览必须校验：
   - schema 通过
   - ID 唯一
   - 原正式 processed 前缀逐条不变
   - 新增候选仍为 `needs_revision`
   - raw 文件仍保持 `not_merged`
   - 导入脚本重复运行不会重复追加
4. 入库后再重建 SFT 和 split。
5. split 必须按 meme cluster、词库 category、phase2 cluster、phase3 `category/cluster/contrast_mode` 防泄漏。

## 已完成的主要阶段

1. 初始化规则文档、schema、校验脚本和基础目录。
2. 整理 Grok、用户手写样本和两份模型扩写候选。
3. 接入并处理 `konsheng/Sensitive-lexicon` 作为能力地图和采样池。
4. 构建第一版正式候选 330 条。
5. 扩充 phase2 raw 100 条，并经用户确认后入库。
6. 扩充 phase3 第一波 245 条，并经用户抽样确认后入库。
7. 正式 processed 达到 675 条，SFT 与防泄漏 split 均已重建。
8. 基于 675 条重跑覆盖分析，得到下一波 185 条建议。
9. 生成 phase3 第二波 raw 185 条，但当前发现 10 条审核员口吻问题，等待人工反馈后重写。

## 当前下一步

优先处理：

1. 人工点评 `docs/phase3_second_wave_review_sample.md` 中的 44 条样本。
2. 根据反馈重写第二波中的 `reviewer_voice` 与其他人机感样本。
3. 重新运行 schema、重复和风格审计。
4. 人工确认第二波通过后，再生成覆盖增益报告和合并预览。

不要急着训练。当前 675 条仍只是数据骨架，第二波 raw 也还未通过人工复核。
