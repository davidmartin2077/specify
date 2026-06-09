# 人工复核包

这份文档把当前需要人工看的文件、复核目标、判断口径和反馈格式集中放在一起。当前复核只决定后续清洗方向，不直接修改正式 `data/processed/combined_candidates.jsonl`。

## 先看结论

优先级从高到低：

1. `docs/context_requirement_audit.md`
2. `docs/duplicate_text_review.md`
3. `docs/external_safety_import_review_sample.md`
4. `docs/context_audit_codebook.md`
5. `data/raw/combined_candidates_binary_preview.jsonl`
6. `data/raw/external_safety_binary_preview.jsonl`
7. `data/eval/risk_test_preview.jsonl`
8. `data/eval/normal_test_preview.jsonl`

如果只想先做一小时复核，先看第 1 和第 2 个文件。

## 文件清单

| 文件 | 审核什么 | 产出什么结论 |
|---|---|---|
| `docs/context_requirement_audit.md` | 看上下文是否硬凑、哪些样本可裸判、哪些重复文本疑似模板污染。 | 标出 `C01/F05` 可改 `context_required=false`；标出 `D03` 应删/重写/降权。 |
| `docs/duplicate_text_review.md` | 正式 860 条里的全部 53 组重复 text。 | 逐组判断保留、删掉、退回重写或降权。 |
| `docs/external_safety_import_review_sample.md` | 看外部真实评论是否值得重塑进入项目格式。 | 决定通过、退回、改标签、改 reasoning、删掉。 |
| `docs/context_audit_codebook.md` | 查数字码含义。 | 人工复核时统一用 `B/C/F/D` 代码。 |
| `data/raw/combined_candidates_binary_preview.jsonl` | 正式 860 条的二元标签和上下文审计预览。 | 后续生成清洗预览的输入，不直接手改正式数据。 |
| `data/raw/external_safety_binary_preview.jsonl` | 外部 340 条的二元标签和上下文审计预览。 | 筛出值得重塑的真实评论候选。 |
| `data/raw/context_requirement_audit.json` | 机器可读全量审计结果。 | 后续脚本读取用，不建议人工逐行看。 |
| `data/eval/risk_test_preview.jsonl` | 全 `B01/unsafe` 样本，899 条。 | 后续测 unsafe recall/封杀率。 |
| `data/eval/normal_test_preview.jsonl` | `B02/safe` 或 hard negative 样本，447 条。 | 后续测 false positive/误封率。 |

## 数字码速查

二元标签：

| 代码 | 含义 |
|---|---|
| `B01` | unsafe，风险样本；来自 high/medium/low。 |
| `B02` | safe，正常样本；来自 none。 |

上下文分层：

| 代码 | 含义 | 审核重点 |
|---|---|---|
| `C01` | direct_no_context，单条文本可直接判断。 | 不要硬凑上下文，考虑改 `context_required=false`。 |
| `C02` | contextual_required，必须依赖上下文。 | 检查上下文是否真实、自然、够用。 |
| `C03` | safe_without_context，单条文本正常。 | 不要为了制造风险而补上下文。 |

审计标记：

| 代码 | 含义 | 审核重点 |
|---|---|---|
| `F01` | generic_or_template_context，上下文泛泛或模板化。 | 看是否需要换成具体真实语境。 |
| `F02` | external_placeholder_context，外部数据占位上下文。 | 不要硬编评论链。 |
| `F03` | do_not_invent_context_review_needed，需要避免硬编上下文。 | 保留无上下文，或只补真实可得信息。 |
| `F04` | safe_sample_context_may_be_optional，安全样本上下文可能非必需。 | 可考虑改 `context_required=false`。 |
| `F05` | likely_direct_no_context，很可能单条文本可裸判。 | 优先人工确认。 |
| `F06` | context_required_but_empty，需要上下文但为空。 | 补真实上下文或改不需要上下文。 |
| `F07` | context_required_only_title，只有标题支撑。 | 判断标题是否足够。 |
| `F08` | reasoning_claims_context_but_context_thin，推理说依赖上下文但上下文很薄。 | 修 reasoning 或补真实上下文。 |

重复文本：

| 代码 | 含义 | 审核重点 |
|---|---|---|
| `D00` | unique，文本唯一。 | 通常不用管重复。 |
| `D01` | effective_contrast_candidate，可能是有效同文不同标签对照。 | 确认上下文确实改变标签。 |
| `D02` | same_text_different_context_review，同文同标签不同上下文。 | 判断是否有训练价值。 |
| `D03` | template_pollution_candidate，疑似模板污染。 | 优先删、重写或降权。 |

## 第一轮怎么审

第一轮只做三件事：

1. 看 `C01/F05`：这些样本可能单条文本就能判断风险。
2. 看 `F02/F03`：这些外部样本缺真实上下文，不能为了 schema 硬编。
3. 看 `D03`：这些重复文本疑似模板污染，后续要删、重写或降权。

## 反馈格式

建议用一行一个样本或一组样本：

```text
MEME_EXPAND_0026_MEDIUM：D03，退回重写；同一句在多个语境重复，像模板污染。
EXT_TOXICN_0008_MEDIUM：通过重塑；真实评论感强，但 context 留空，不硬编回复链。
PHASE3_W2_0068_WEAPONS_EXPLOSIVES_DIRECT：C01/F05，通过；单条文本已足够判断，建议 context_required=false。
EXT_COLD_0010_MEDIUM：改标签 low；有群体刻板印象，但风险强度不够 medium。
```

允许的结论词：

| 结论 | 含义 |
|---|---|
| `通过` | 可保留当前方向。 |
| `通过重塑` | 语料有价值，但要重写 context/reasoning/counter_evidence。 |
| `改标签` | 风险等级、二元标签或 hard_negative 需要调整。 |
| `改上下文` | context 需要删、补真实信息或改为无上下文。 |
| `改 reasoning` | 推理链不贴合文本或夸大证据。 |
| `退回重写` | 文本/上下文/推理整体需要重写。 |
| `删掉` | 不值得进入后续训练或评测。 |

## 判断口径

`context_required=false` 的典型情况：

- 文本本身已经明确违法、辱骂、色情、导流、黑产、暴力、赌博等风险。
- 没有标题、回复链也能判断 unsafe。
- 当前上下文只是模板场景名，例如“热搜评论区”“普通生活帖”，不提供真实证据。

`context_required=true` 的典型情况：

- 单句有双关、暗号、日期、人物代指、历史影射，但普通解释仍很强。
- 必须靠标题、上级评论、回复链、发布时间或话题才能判断风险。
- 去掉上下文后，风险等级会明显下降。

`safe_without_context` 的典型情况：

- 文本本身正常。
- 外部数据标注安全，且没有明显项目风险信号。
- 不应为了构造 hard negative 而硬编一个风险场景。

## 外部样本怎么审

外部 340 条的价值是“真实评论语感”，不是它们的原始标签。审外部样本时按下面顺序：

1. 先看 text 是否像真实评论、私聊、弹幕或问答。
2. 再看外部标签是否大致可信。
3. 再判断项目里应该是 high/medium/low/none。
4. 最后决定是否值得重塑 reasoning。

外部样本不要硬补：

- 不要凭空编标题。
- 不要凭空编 parent_comment。
- 不要凭空编 reply_chain。
- 没有上下文就保留无上下文，让模型学习裸判。

## 会不会影响模型训练

当前不会影响训练。

原因：

1. 正式 `data/processed/combined_candidates.*` 没改。
2. 这些代码只写在 raw/eval 预览和审计报告里。
3. 后续训练时不要把 `B01/C01/F05/D03` 直接放进模型输入或输出。
4. 模型训练仍应学习中文解释、风险等级、证据、反证，而不是学习内部审计码。

如果以后要把这些字段正式入库，也应作为 metadata/review-only 字段，不进入 SFT 目标文本。

## 推荐复核顺序

第一批：

1. `docs/context_requirement_audit.md` 里的 `F05/C01` 样本。
2. `docs/duplicate_text_review.md` 里的 53 组正式重复文本。
3. `docs/external_safety_import_review_sample.md` 中每个来源先各看 20 条。

第二批：

1. `data/raw/external_safety_binary_preview.jsonl` 中 `F02/F03/B01` 样本。
2. `data/raw/combined_candidates_binary_preview.jsonl` 中 `F04/C03` 样本。
3. `data/eval/normal_test_preview.jsonl` 中容易误封的 hard negative。

第三批：

1. 生成清洗预览。
2. 重新校验。
3. 再决定是否 apply 到正式 processed。
