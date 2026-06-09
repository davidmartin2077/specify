# 上下文审计代码表

本文件解释 `scripts/audit_context_and_binary_labels.py` 生成的审计字段，并给出后续人工复核和数据集命名使用的数字码。

这些代码只用于人工复核、清洗预览、数据集命名和评测集管理。只要不把这些字段拼进 SFT 的用户指令或模型回答文本，就不会影响模型训练。它们目前写在 raw/eval 预览和 `review_notes` 中，正式 `data/processed/combined_candidates.*` 未修改。

## 命名规则

| 前缀 | 含义 | 示例 |
|---|---|---|
| `B` | binary，二元安全标签 | `B01` |
| `C` | context class，上下文依赖分层 | `C02` |
| `F` | flag，审计标记 | `F05` |
| `D` | duplicate，重复文本状态 | `D03` |

后续数据集命名建议使用数字码，例如：

```text
context_review_C01_F05.jsonl
external_review_F02_F03.jsonl
duplicate_review_D03.jsonl
risk_eval_B01.jsonl
normal_eval_B02_D00.jsonl
```

## 二元安全标签

| 代码 | 字段值 | 中文解释 | 用途 |
|---|---|---|---|
| `B01` | `unsafe` | 风险样本。当前规则为 `high/medium/low -> unsafe`。 | 用于 risk test，衡量 unsafe recall/封杀率。 |
| `B02` | `safe` | 正常样本。当前规则为 `none -> safe`。 | 用于 normal test，衡量 false positive/误封率。 |

说明：`B01/B02` 不替代原始 `risk_level`。训练和解释仍保留 `high/medium/low/none`，二元标签只服务高召回评测。

## 上下文依赖分层

| 代码 | 字段值 | 中文解释 | 人工复核动作 |
|---|---|---|---|
| `C01` | `direct_no_context` | 单条文本本身已有足够风险信号，不需要标题、上级评论、回复链也能判断。 | 优先考虑后续把 `context_required` 调为 `false`，不要硬编上下文。 |
| `C02` | `contextual_required` | 文本单看较模糊，需要标题、上级评论、时间、话题或回复链支撑当前风险解释。 | 保留上下文依赖，但检查上下文是否真实、自然、够用。 |
| `C03` | `safe_without_context` | 单条文本正常，或外部标签倾向安全；不应为了凑风险语境而补虚假上下文。 | 作为正常样本或 hard negative 复核，避免误杀训练。 |

## 审计标记

| 代码 | 字段值 | 中文解释 | 典型含义 |
|---|---|---|---|
| `F01` | `generic_or_template_context` | 上下文像模板或泛泛场景名。 | 例如“热搜评论区”“普通生活帖”，可能不是具体真实上下文。 |
| `F02` | `external_placeholder_context` | 外部数据集的占位上下文。 | ToxiCN/COLD/ChineseSafe 导入预览常见，表示原始数据缺少完整评论链。 |
| `F03` | `do_not_invent_context_review_needed` | 需要人工复核，不能为了补完整而硬编上下文。 | 通常与 `F02` 同时出现，提醒外部样本要保留“无上下文”或只补真实可得信息。 |
| `F04` | `safe_sample_context_may_be_optional` | 安全样本的上下文可能不是必须。 | 常见于 `risk_level=none` 且 hard negative 的样本，后续可考虑 `context_required=false`。 |
| `F05` | `likely_direct_no_context` | 很可能单条文本即可判断风险。 | 当前却标了 `context_required=true`，应优先人工复核。 |
| `F06` | `context_required_but_empty` | 标了需要上下文，但上下文字段为空。 | 数据一致性问题，需补真实上下文或改为不需要上下文。 |
| `F07` | `context_required_only_title` | 标了需要上下文，但只有标题字段支撑。 | 不一定错，但要确认标题是否足以支撑风险解释。 |
| `F08` | `reasoning_claims_context_but_context_thin` | reasoning 说依赖标题、回复链或时间节点，但实际上下文很薄。 | 需要检查推理链是否夸大了上下文证据。 |

优先复核顺序建议：

1. `F05`：直接决定哪些样本可改为裸判。
2. `F02 + F03`：外部样本不要硬编上下文。
3. `F08`：修 reasoning 和 context 的一致性。
4. `F06/F07`：修结构一致性。
5. `F01/F04`：作为批量清洗参考。

## 重复文本状态

| 代码 | 字段值 | 中文解释 | 人工复核动作 |
|---|---|---|---|
| `D00` | `unique` | 文本唯一。 | 无需重复文本处理。 |
| `D01` | `effective_contrast_candidate` | 同文不同标签，可能是有效语境对照。 | 保留价值较高，但要确认上下文真的造成标签差异。 |
| `D02` | `same_text_different_context_review` | 同文同标签但上下文不同，待复核。 | 判断是否有训练价值，或只是重复。 |
| `D03` | `template_pollution_candidate` | 疑似模板污染。 | 优先删、重写或降权，不建议原样进入高质量训练集。 |

## 训练影响

当前做法不影响模型训练，原因是：

1. 正式 `data/processed/combined_candidates.jsonl` 未修改。
2. 新字段只存在于 raw/eval 预览和审计 JSON 中。
3. 现有 `scripts/build_sft_dataset.py` 使用项目样本字段构造训练指令，不会自动把这些审计码变成模型要学习的自然语言内容。
4. 后续如果正式引入这些字段，应把它们当作 metadata 或 review-only 字段，不要放进模型输出目标。

可能影响训练的情况只有一种：如果后续把 `F05/C01/B01` 这类代码直接塞进 SFT prompt 或 assistant answer，模型可能学会输出内部审计码，降低自然解释质量。因此建议训练阶段继续使用中文解释、风险等级、证据和反证；审计码只用于人工筛选、文件命名和评测集管理。
