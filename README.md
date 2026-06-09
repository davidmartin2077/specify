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
| 正式 processed 候选 | 860 条 |
| SFT 数据 | 860 条 |
| 默认 train/validation/test split | 已生成并校验 |
| 防泄漏 group | 281 个，0 个跨 split 泄漏 |
| 第三阶段第二波 | 185 条已正式入库 |
| 第二波人工复核清单 | 44 条，已按反馈重建并用于入库判断 |
| 覆盖分析 | 已基于 860 条重新生成 |
| 外部真实评论数据评估 | ToxiCN/COLD/ChineseSafe 已生成 340 条 raw 预览，尚未入库 |
| 上下文/二元标签审计 | 已生成审计报告、二元预览和 eval 草案 |

正式候选集：

- `data/processed/combined_candidates.jsonl`
- `data/processed/combined_candidates.json`

正式数据分布：

```text
high    167
medium  304
low     182
none    207

hard_negative        353
context_required     809
quality_status       全部 needs_revision
```

当前 split：

```text
train       688
validation   86
test         86
```

上下文与二元标签预览：

```text
combined binary preview   860
external binary preview   340
risk_test_preview         899
normal_test_preview       447

safety_binary: unsafe 899 / safe 301
context classes: contextual_required 846 / safe_without_context 301 / direct_no_context 53
```

## 当前最重要的注意事项

第二波 185 条已正式入库，但仍是 `needs_revision` 质量状态：

- `data/raw/phase3_second_wave_candidates.jsonl`
- raw 文件仍保留原始 `not_merged` 状态
- processed 入库副本已标记为 `merged_processed`
- 已通过 schema、ID/text 查重
- 已按人工反馈重写审核员语气、tips/宣传句、黑话教学口吻和部分上下文模板
- 当前风格审计 0 个标记

复核参考文件：

- `docs/phase3_second_wave_review_sample.md`
- `data/raw/phase3_second_wave_review_sample.json`

下一步不要重复执行第二波入库；应转向对正式 860 条做分层复核，或基于新版覆盖报告规划下一轮扩充。

## 外部真实评论数据评估

已对 ToxiCN、COLD 和 ChineseSafe 做外部接入评估，用于把数据风格往真实评论区靠拢，同时保留本项目的推理链优势。

相关文件：

- `scripts/analyze_external_safety_datasets.py`
- `docs/external_safety_datasets_review.md`
- `docs/external_safety_import_review_sample.md`
- `docs/duplicate_text_audit.md`
- `data/raw/external_safety_import_preview.jsonl`
- `data/raw/external_safety_import_preview.json`
- `data/raw/external_safety_datasets_report.json`
- `scripts/audit_context_and_binary_labels.py`
- `docs/manual_review_packet.md`
- `docs/context_audit_codebook.md`
- `docs/context_requirement_audit.md`
- `data/raw/context_requirement_audit.json`
- `data/raw/combined_candidates_binary_preview.jsonl`
- `data/raw/external_safety_binary_preview.jsonl`
- `data/eval/risk_test_preview.jsonl`
- `data/eval/normal_test_preview.jsonl`

外部 raw 预览组成：

```text
ToxiCN        120
COLD         120
ChineseSafe  100
合计          340
```

外部 raw 预览分布：

```text
high     36
medium  186
low      24
none     94

hard_negative 94
```

当前原则：

- 外部标签只作为候选信号，不替代本项目标注。
- 340 条全部为 `needs_revision/not_merged`，不进入正式 processed。
- 外部样本已纳入二元标签与上下文依赖预览，但仍未入库。
- 下一步应先人工抽查 `docs/external_safety_import_review_sample.md` 与 `docs/context_requirement_audit.md`。
- 适合保留的外部样本需要重塑 `context`、`reasoning`、`counter_evidence` 和风险等级。
- `docs/duplicate_text_audit.md` 已记录正式 860 条中的 53 组重复 text，后续需要判断哪些是有效语境对照，哪些是早期模板污染。

## 第二波正式入库状态

第二波入库前预览已经生成并校验，随后已正式 apply。当前正式 processed 为 860 条。

相关文件：

- `data/processed/combined_candidates_phase3_w2_preview.jsonl`
- `data/processed/combined_candidates_phase3_w2_preview.json`
- `docs/phase3_second_wave_coverage_delta.md`
- `data/processed/phase3_second_wave_coverage_delta.json`
- `scripts/import_phase3_second_wave.py`

正式组成：

```text
原正式 processed     675
phase3 第二波 raw    185
合计                 860
```

正式分布：

```text
high    167
medium  304
low     182
none    207

hard_negative 353
```

已完成校验：

- schema 通过
- 860 个 ID 唯一
- 原正式 675 条逐条不变
- 新增 185 条仍为 `needs_revision`
- processed 入库副本标记为 `merged_processed`
- raw 第二波仍保持 `not_merged`
- 重复运行预览不会重复追加
- SFT 已重建为 860 条
- train/validation/test 已重切为 688/86/86，0 个 group 泄漏

不要再次执行第二波 `--apply` 作为常规操作；如需复核，先查看正式 processed 与上述报告。

## 样本编号规则

样本 ID 主要用于追踪来源、批次、序号、类别和对照模式。最常见格式如下：

```text
PHASE3_W2_0020_SEXUAL_CONTENT_WEAK_SIGNAL
│      │  │    │              │
│      │  │    │              └─ 对照模式：weak_signal 弱信号边界
│      │  │    └─ 类别：sexual_content 色情低俗
│      │  └─ 批内流水号：第 20 条
│      └─ 波次：W2 = 第三阶段第二波
└─ 阶段：PHASE3 = 第三阶段扩充
```

当前主要前缀：

| 前缀 | 含义 | 是否已入正式 processed |
|---|---|---|
| `GROK_*` | Grok 生成候选规整样本 | 是 |
| `USER_*` | 用户手写候选规整样本 | 是 |
| `MEME_EXPAND_*` | 第一份外部扩写清洗样本 | 是 |
| `GEMINI_EXPAND_*` | 第二份外部扩写清洗样本 | 是 |
| `LEXICON_SEED_*` | 敏感词库 seed 候选 | 是 |
| `PHASE2_SEED_*` | 第二阶段语境边界扩充 | 是 |
| `PHASE3_W1_*` | 第三阶段第一波覆盖缺口扩充 | 是 |
| `PHASE3_W2_*` | 第三阶段第二波长尾/困难边界扩充 | 是 |

`PHASE3_W1_*` 和 `PHASE3_W2_*` 后半段通常由这些字段组成：

| 字段 | 示例 | 含义 |
|---|---|---|
| 阶段 | `PHASE3` | 第三阶段风险覆盖扩充 |
| 波次 | `W1` / `W2` | 第一波 / 第二波 |
| 流水号 | `0020` | 该波内部序号 |
| 类别 | `SEXUAL_CONTENT` | 风险类别 |
| 模式 | `WEAK_SIGNAL` | 对照模式 |

当前第二波类别代码：

| 类别代码 | 中文含义 |
|---|---|
| `SEXUAL_CONTENT` | 色情低俗 |
| `SPAM_ADS_FRAUD` | 广告/诈骗/导流 |
| `INSULTING_ABUSE` | 辱骂/群体攻击 |
| `WEAPONS_EXPLOSIVES` | 枪爆武器 |
| `PUBLIC_AFFAIRS` | 公共事务 |
| `POLITICAL_HISTORY` | 政治历史/鉴证梗 |
| `PLATFORM_CENSORSHIP_EVASION` | 平台规避/审查黑话 |
| `CYBER_ABUSE` | 网络黑产/安全风险 |
| `VIOLENCE_EXTREMISM` | 暴力极端 |
| `ILLEGAL_GOODS` | 违禁交易 |
| `GAMBLING` | 赌博 |

当前第二波对照模式：

| 模式 | 含义 | 通常标签 |
|---|---|---|
| `DIRECT` | 明确风险表达 | high |
| `OBFUSCATED` | 暗号、替代词、规避写法 | medium |
| `CONTEXTUAL` | 单句模糊，依赖上下文触发风险 | medium |
| `WEAK_SIGNAL` | 弱风险信号，普通解释较强 | low + hard negative |
| `SAFE_CONTEXT` | 新闻、科普、举报、正规业务等安全语境 | none + hard negative |

## 人工审核回复格式

请优先审核 `docs/phase3_second_wave_review_sample.md` 里的 44 条。你可以直接按编号回复，不需要复制整条样本。

最推荐格式：

```text
1：退回，人机感，像审核说明，不像真实评论
2：通过
3：改 medium，理由是表达暧昧但没有明确交易链
4：退回，暗号太刻意，现实中不像这么说
```

也可以用样本 ID：

```text
PHASE3_W2_0020_SEXUAL_CONTENT_WEAK_SIGNAL：退回，像客服 tips，不像评论
PHASE3_W2_0022_SEXUAL_CONTENT_SAFE_CONTEXT：通过
```

审核结论建议使用这几类：

| 结论 | 含义 | 我后续会怎么处理 |
|---|---|---|
| `通过` | 文本自然，当前标签基本可接受 | 保留 |
| `退回` | 文本不自然、太人机、太像客服/tips/审核说明 | 重写 |
| `改 high/medium/low/none` | 文本可保留，但风险等级需调整 | 改标签并同步 reasoning |
| `改类别` | 类别不对，例如应从公共事务改到诈骗 | 改 category/encoding/reasoning |
| `改模式` | direct/obfuscated/contextual/weak_signal/safe_context 不合适 | 改 contrast_mode 与相关标签 |
| `删掉` | 样本方向不好，不值得救 | 后续从候选中移除或替换 |

请特别标注这些问题：

1. `人机感`：像模型生成的陈述句，不像真实评论/弹幕。
2. `客服/tips`：像平台提示、公益提示、医院/银行/学校官方提示。
3. `审核说明`：像“证据不足、需要核验、不能只看词”这类标注员分析。
4. `暗号太刻意`：黑话设计不自然，现实用户不太会这么说。
5. `过度联想`：风险解释牵强，应降级或改 none。
6. `漏召回`：看起来应该更高风险，当前标签偏低。

如果你只想快速给方向，也可以这样写：

```text
1、5、9、13 这种 weak_signal 都像审核说明，后续同类重写成真实用户吐槽。
safe_context 里医院/银行/学校官方提示太 tips，减少这类，改成评论区普通用户转述。
direct 基本可以，但诈骗类暗号要更像真实引流话术。
```

## 关键文档

- `agent.md`：项目交接记忆。新窗口接手时必须先读。
- `docs/encoding_taxonomy.md`：编码方式分类手册。
- `docs/annotation_guideline.md`：标注规范、JSONL 字段、风险等级、hard negative 规则。
- `docs/risk_coverage_report.md`：基于正式 860 条的风险覆盖分析。
- `docs/phase3_coverage_delta.md`：phase2 + phase3 第一波入库前后的覆盖增益。
- `docs/phase3_second_wave_review_sample.md`：第二波 44 条人工复核清单。
- `docs/external_safety_datasets_review.md`：ToxiCN/COLD/ChineseSafe 外部数据接入评估。
- `docs/external_safety_import_review_sample.md`：外部 raw 转换预览抽样。
- `docs/duplicate_text_audit.md`：正式 860 条重复 text 审计。
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

重跑正式 860 条覆盖分析：

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

重建外部数据评估与 raw 预览：

```bash
python3 scripts/analyze_external_safety_datasets.py --include-chinesesafe
python3 scripts/validate_dataset.py data/raw/external_safety_import_preview.jsonl
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
9. 生成 phase3 第二波 raw 185 条；首次人工抽样发现审核员口吻、tips、黑话教学等问题后，已按反馈重写并重建复核清单。
10. phase3 第二波 185 条已正式入库，processed/SFT 达到 860 条，防泄漏 split 已重建并校验。
11. 已评估 ToxiCN、COLD、ChineseSafe 三个外部真实评论/安全数据源，生成 340 条 raw 转换预览和重复 text 审计；正式 processed 未修改。

## 当前下一步

优先处理：

1. 对正式 860 条做分层人工复核，优先抽查第二波入库样本、hard negative、high/medium 边界和 safe_context。
2. 人工抽查 `docs/external_safety_import_review_sample.md`，判断三套外部数据哪些适合重塑推理链。
3. 基于新版 `docs/risk_coverage_report.md` 和外部数据评估结果规划下一轮扩充，不要逐词机械生成。
4. 后续新增候选仍先进入 raw，人工抽查、预览校验后再入库。

不要急着训练。当前 860 条仍只是数据骨架，质量状态全部为 `needs_revision`，还需要继续复核和分层扩充。
