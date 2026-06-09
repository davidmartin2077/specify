# 重复文本人工复核清单

本文件从正式 `data/processed/combined_candidates.jsonl` 的 860 条样本中抽取全部重复 text 组，共 53 组。

这里是自包含复核版：每个重复组已经列出涉及样本的标签、上下文、审计码和关键 reasoning，不需要再回 860 条正式数据里逐个查。

## 怎么判断

- `D01`：可能是有效同文不同标签对照。重点看上下文是否真的改变标签。
- `D02`：同文同标签但上下文不同。重点看这些上下文差异是否有训练价值，还是普通重复。
- `D03`：疑似模板污染。优先考虑删、重写或降权。

判断时先看同组样本的 `上下文` 部分：如果只是换了泛泛场景名，但同一句话、同一标签、同一推理逻辑都差不多，多半是重复或模板污染；如果上下文真的改变了含义，才值得保留为对照。

最新策略：`parent_comment` / `reply_chain` 是旧字段，除非来自真实原始数据，否则默认不作为强证据。如果风险主要靠“像，但别展开”“别说像谁”“懂就别打全称”“缩写就行”等合成回复链成立，直接按模板污染、退回重写或降权处理。

建议反馈格式：

```text
重复组 01：保留 / 删掉 / 退回重写 / 降权，原因……
MEME_EXPAND_0026_MEDIUM：退回重写，原因……
```

## 全部重复组

### 重复组 01

- 状态：`D02` / `same_text_different_context_review` / 同文同标签但不同上下文，待复核
- 出现次数：3
- 重复文本：NB 是 New Balance 的鞋款缩写，不是别的意思
- 风险分布：{"none": 3}
- 来源分布：{"meme_expansion": 3}
- 建议动作：看是否只是重复造句；如果上下文差异没有训练价值，建议删/重写/降权。

#### 本组怎么审

1. 先看文本本身是否足以判断。
2. 再比较标题、时间、话题等非回复链上下文是否真的不同。
3. 不要把合成的 `parent_comment/reply_chain` 当强证据。
4. 如果只是换标题/平台/泛泛场景，或靠假回复链撑风险，结论倾向 `删掉`、`退回重写` 或 `降权`。
5. 如果确实构成同文不同语境对照，结论可写 `保留对照`。

#### 涉及样本详情

#### `MEME_EXPAND_0091_NONE`

- 标签：risk_level=`none`；binary=`B02 / safe`；hard_negative=`true`
- 编码：primary=`none`；secondary=`无`
- 上下文审计：class=`C03 / safe_without_context`；flags=`F01+F04`；duplicate=`D02 / same_text_different_context_review`
- context_required：`true`
- 上下文：
  - title：普通生活帖
  - description：无
  - parent_comment（旧字段，默认不作强证据）：字面场景明确
  - reply_chain（旧字段，默认不作强证据）：无异常互动
  - time：2026-06-04
  - topic：平台黑话/自我审查
- 关键 reasoning：
  - supporting_evidence：无
  - counter_evidence：上下文明确指向普通生活、学习、商品、娱乐或技术场景。；没有规避检测意图、隐含目标或异常互动共识。；相关词语可由字面含义充分解释。
  - final_rationale：反证充分，风险解释不成立，标为none。
- review_notes：source=meme_expansion; original_id=EXPAND_0091; generated_expansion; needs_human_review; original_primary=C3_数字代指; original_notes=generated_expansion; needs_human_review; meme_cluster=平台黑话/自我审查; context_audit_class=safe_without_context; context_audit_class_code=C03; context_audit_flag_codes=F01+F04; safety_binary=safe; safety_binary_code=B02; duplicate_text_status=same_text_different_context_review; duplicate_text_status_code=D02; preview_only=true

#### `MEME_EXPAND_0105_NONE`

- 标签：risk_level=`none`；binary=`B02 / safe`；hard_negative=`true`
- 编码：primary=`none`；secondary=`无`
- 上下文审计：class=`C03 / safe_without_context`；flags=`F01+F04`；duplicate=`D02 / same_text_different_context_review`
- context_required：`true`
- 上下文：
  - title：商品/美食测评
  - description：无
  - parent_comment（旧字段，默认不作强证据）：只讨论购买和使用体验
  - reply_chain（旧字段，默认不作强证据）：没有隐含目标
  - time：2026-05-05
  - topic：平台黑话/自我审查
- 关键 reasoning：
  - supporting_evidence：无
  - counter_evidence：上下文明确指向普通生活、学习、商品、娱乐或技术场景。；没有规避检测意图、隐含目标或异常互动共识。；相关词语可由字面含义充分解释。
  - final_rationale：反证充分，风险解释不成立，标为none。
- review_notes：source=meme_expansion; original_id=EXPAND_0105; generated_expansion; needs_human_review; original_primary=B3_形近字替换; original_notes=generated_expansion; needs_human_review; meme_cluster=平台黑话/自我审查; context_audit_class=safe_without_context; context_audit_class_code=C03; context_audit_flag_codes=F01+F04; safety_binary=safe; safety_binary_code=B02; duplicate_text_status=same_text_different_context_review; duplicate_text_status_code=D02; preview_only=true

#### `MEME_EXPAND_0119_NONE`

- 标签：risk_level=`none`；binary=`B02 / safe`；hard_negative=`true`
- 编码：primary=`none`；secondary=`无`
- 上下文审计：class=`C03 / safe_without_context`；flags=`F01+F04`；duplicate=`D02 / same_text_different_context_review`
- context_required：`true`
- 上下文：
  - title：课程/教程内容
  - description：无
  - parent_comment（旧字段，默认不作强证据）：讨论学习或技术问题
  - reply_chain（旧字段，默认不作强证据）：上下文支持普通解释
  - time：2026-03-06
  - topic：平台黑话/自我审查
- 关键 reasoning：
  - supporting_evidence：无
  - counter_evidence：上下文明确指向普通生活、学习、商品、娱乐或技术场景。；没有规避检测意图、隐含目标或异常互动共识。；相关词语可由字面含义充分解释。
  - final_rationale：反证充分，风险解释不成立，标为none。
- review_notes：source=meme_expansion; original_id=EXPAND_0119; generated_expansion; needs_human_review; original_primary=C2_历史事件影射; original_notes=generated_expansion; needs_human_review; meme_cluster=平台黑话/自我审查; context_audit_class=safe_without_context; context_audit_class_code=C03; context_audit_flag_codes=F01+F04; safety_binary=safe; safety_binary_code=B02; duplicate_text_status=same_text_different_context_review; duplicate_text_status_code=D02; preview_only=true

- 复核结论：待填写

### 重复组 02

- 状态：`D03` / `template_pollution_candidate` / 疑似模板污染，优先删/重写/降权
- 出现次数：3
- 重复文本：一到这个日期，连普通蜡烛视频都有人刷懂
- 风险分布：{"medium": 3}
- 来源分布：{"meme_expansion": 3}
- 建议动作：优先判为模板污染候选；建议退回重写或后续从高质量训练集中剔除。

#### 本组怎么审

1. 先看文本本身是否足以判断。
2. 再比较标题、时间、话题等非回复链上下文是否真的不同。
3. 不要把合成的 `parent_comment/reply_chain` 当强证据。
4. 如果只是换标题/平台/泛泛场景，或靠假回复链撑风险，结论倾向 `删掉`、`退回重写` 或 `降权`。
5. 如果确实构成同文不同语境对照，结论可写 `保留对照`。

#### 涉及样本详情

#### `MEME_EXPAND_0026_MEDIUM`

- 标签：risk_level=`medium`；binary=`B01 / unsafe`；hard_negative=`false`
- 编码：primary=`C3_数字代指`；secondary=`E1_平台黑话；E3_回复链/互动触发`
- 上下文审计：class=`C02 / contextual_required`；flags=`F01`；duplicate=`D03 / template_pollution_candidate`
- context_required：`true`
- 上下文：
  - title：热搜评论区
  - description：无
  - parent_comment（旧字段，默认不作强证据）：这波是不是又要统一口径
  - reply_chain（旧字段，默认不作强证据）：缩写就行
  - time：2026-05-19
  - topic：食物/品牌/物品隐喻
- 关键 reasoning：
  - supporting_evidence：文本或上下文提供可疑编码线索。
  - counter_evidence：普通解释仍可成立，缺少直接目标或更完整上下文。
  - final_rationale：有明显复核价值，但证据不足以确定为high，标为medium。
- review_notes：source=meme_expansion; original_id=EXPAND_0026; generated_expansion; needs_human_review; original_primary=A2_拼音/首字母缩写; original_notes=generated_expansion; needs_human_review; meme_cluster=食物/品牌/物品隐喻; context_audit_class=contextual_required; context_audit_class_code=C02; context_audit_flag_codes=F01; safety_binary=unsafe; safety_binary_code=B01; duplicate_text_status=template_pollution_candidate; duplicate_text_status_code=D03; preview_only=true

#### `MEME_EXPAND_0040_MEDIUM`

- 标签：risk_level=`medium`；binary=`B01 / unsafe`；hard_negative=`false`
- 编码：primary=`E2_时间节点触发`；secondary=`C3_数字代指；C4_典故/物品/符号借用`
- 上下文审计：class=`C02 / contextual_required`；flags=`F01`；duplicate=`D03 / template_pollution_candidate`
- context_required：`true`
- 上下文：
  - title：社会趋势讨论话题
  - description：无
  - parent_comment（旧字段，默认不作强证据）：别说太满
  - reply_chain（旧字段，默认不作强证据）：像，但不敢说
  - time：2026-04-20
  - topic：食物/品牌/物品隐喻
- 关键 reasoning：
  - supporting_evidence：文本或上下文提供可疑编码线索。
  - counter_evidence：普通解释仍可成立，缺少直接目标或更完整上下文。
  - final_rationale：有明显复核价值，但证据不足以确定为high，标为medium。
- review_notes：source=meme_expansion; original_id=EXPAND_0040; generated_expansion; needs_human_review; original_primary=E2_时间节点触发; original_notes=generated_expansion; needs_human_review; meme_cluster=食物/品牌/物品隐喻; context_audit_class=contextual_required; context_audit_class_code=C02; context_audit_flag_codes=F01; safety_binary=unsafe; safety_binary_code=B01; duplicate_text_status=template_pollution_candidate; duplicate_text_status_code=D03; preview_only=true

#### `MEME_EXPAND_0054_MEDIUM`

- 标签：risk_level=`medium`；binary=`B01 / unsafe`；hard_negative=`false`
- 编码：primary=`C2_历史事件影射`；secondary=`D1_反讽；E2_时间节点触发`
- 上下文审计：class=`C02 / contextual_required`；flags=`none`；duplicate=`D03 / template_pollution_candidate`
- context_required：`true`
- 上下文：
  - title：历史剧二创
  - description：无
  - parent_comment（旧字段，默认不作强证据）：别说像谁
  - reply_chain（旧字段，默认不作强证据）：像，但别展开
  - time：2026-02-28
  - topic：食物/品牌/物品隐喻
- 关键 reasoning：
  - supporting_evidence：文本或上下文提供可疑编码线索。
  - counter_evidence：普通解释仍可成立，缺少直接目标或更完整上下文。
  - final_rationale：有明显复核价值，但证据不足以确定为high，标为medium。
- review_notes：source=meme_expansion; original_id=EXPAND_0054; generated_expansion; needs_human_review; original_primary=C2_历史事件影射; original_notes=generated_expansion; needs_human_review; meme_cluster=食物/品牌/物品隐喻; context_audit_class=contextual_required; context_audit_class_code=C02; context_audit_flag_codes=none; safety_binary=unsafe; safety_binary_code=B01; duplicate_text_status=template_pollution_candidate; duplicate_text_status_code=D03; preview_only=true

- 复核结论：待填写

### 重复组 03

- 状态：`D03` / `template_pollution_candidate` / 疑似模板污染，优先删/重写/降权
- 出现次数：3
- 重复文本：今天买了白纸，做手账真的很好用
- 风险分布：{"low": 3}
- 来源分布：{"meme_expansion": 3}
- 建议动作：优先判为模板污染候选；建议退回重写或后续从高质量训练集中剔除。

#### 本组怎么审

1. 先看文本本身是否足以判断。
2. 再比较标题、时间、话题等非回复链上下文是否真的不同。
3. 不要把合成的 `parent_comment/reply_chain` 当强证据。
4. 如果只是换标题/平台/泛泛场景，或靠假回复链撑风险，结论倾向 `删掉`、`退回重写` 或 `降权`。
5. 如果确实构成同文不同语境对照，结论可写 `保留对照`。

#### 涉及样本详情

#### `MEME_EXPAND_0061_LOW`

- 标签：risk_level=`low`；binary=`B01 / unsafe`；hard_negative=`true`
- 编码：primary=`C4_典故/物品/符号借用`；secondary=`D2_隐喻`
- 上下文审计：class=`C02 / contextual_required`；flags=`none`；duplicate=`D03 / template_pollution_candidate`
- context_required：`true`
- 上下文：
  - title：日常生活分享
  - description：无
  - parent_comment（旧字段，默认不作强证据）：只是普通记录
  - reply_chain（旧字段，默认不作强证据）：别过度联想
  - time：2026-06-04
  - topic：食物/品牌/物品隐喻
- 关键 reasoning：
  - supporting_evidence：存在关键词、缩写、数字或符号撞车。
  - counter_evidence：上下文提供普通生活、教学、娱乐或技术解释。；缺少规避意图、目标映射或敏感语境。
  - final_rationale：普通解释更强，仅保留低风险或困难负样本价值，标为low。
- review_notes：source=meme_expansion; original_id=EXPAND_0061; generated_expansion; needs_human_review; original_primary=C4_典故/物品/符号借用; original_notes=generated_expansion; needs_human_review; meme_cluster=食物/品牌/物品隐喻; context_audit_class=contextual_required; context_audit_class_code=C02; context_audit_flag_codes=none; safety_binary=unsafe; safety_binary_code=B01; duplicate_text_status=template_pollution_candidate; duplicate_text_status_code=D03; preview_only=true

#### `MEME_EXPAND_0075_LOW`

- 标签：risk_level=`low`；binary=`B01 / unsafe`；hard_negative=`true`
- 编码：primary=`C2_历史事件影射`；secondary=`无`
- 上下文审计：class=`C02 / contextual_required`；flags=`F01`；duplicate=`D03 / template_pollution_candidate`
- context_required：`true`
- 上下文：
  - title：美食/文具/娱乐分享
  - description：无
  - parent_comment（旧字段，默认不作强证据）：求链接
  - reply_chain（旧字段，默认不作强证据）：只讨论字面对象
  - time：2026-05-05
  - topic：食物/品牌/物品隐喻
- 关键 reasoning：
  - supporting_evidence：存在关键词、缩写、数字或符号撞车。
  - counter_evidence：上下文提供普通生活、教学、娱乐或技术解释。；缺少规避意图、目标映射或敏感语境。
  - final_rationale：普通解释更强，仅保留低风险或困难负样本价值，标为low。
- review_notes：source=meme_expansion; original_id=EXPAND_0075; generated_expansion; needs_human_review; original_primary=B3_形近字替换; original_notes=generated_expansion; needs_human_review; meme_cluster=食物/品牌/物品隐喻; context_audit_class=contextual_required; context_audit_class_code=C02; context_audit_flag_codes=F01; safety_binary=unsafe; safety_binary_code=B01; duplicate_text_status=template_pollution_candidate; duplicate_text_status_code=D03; preview_only=true

#### `MEME_EXPAND_0089_LOW`

- 标签：risk_level=`low`；binary=`B01 / unsafe`；hard_negative=`true`
- 编码：primary=`E2_时间节点触发`；secondary=`C3_数字代指`
- 上下文审计：class=`C02 / contextual_required`；flags=`none`；duplicate=`D03 / template_pollution_candidate`
- context_required：`true`
- 上下文：
  - title：教学/教程评论区
  - description：无
  - parent_comment（旧字段，默认不作强证据）：讨论的是具体技巧
  - reply_chain（旧字段，默认不作强证据）：普通解释更强
  - time：2026-03-16
  - topic：食物/品牌/物品隐喻
- 关键 reasoning：
  - supporting_evidence：存在关键词、缩写、数字或符号撞车。
  - counter_evidence：上下文提供普通生活、教学、娱乐或技术解释。；缺少规避意图、目标映射或敏感语境。
  - final_rationale：普通解释更强，仅保留低风险或困难负样本价值，标为low。
- review_notes：source=meme_expansion; original_id=EXPAND_0089; generated_expansion; needs_human_review; original_primary=E2_时间节点触发; original_notes=generated_expansion; needs_human_review; meme_cluster=食物/品牌/物品隐喻; context_audit_class=contextual_required; context_audit_class_code=C02; context_audit_flag_codes=none; safety_binary=unsafe; safety_binary_code=B01; duplicate_text_status=template_pollution_candidate; duplicate_text_status_code=D03; preview_only=true

- 复核结论：待填写

### 重复组 04

- 状态：`D03` / `template_pollution_candidate` / 疑似模板污染，优先删/重写/降权
- 出现次数：3
- 重复文本：他说‘35号见’，不像普通约饭，但也没更多上下文
- 风险分布：{"medium": 3}
- 来源分布：{"meme_expansion": 3}
- 建议动作：优先判为模板污染候选；建议退回重写或后续从高质量训练集中剔除。

#### 本组怎么审

1. 先看文本本身是否足以判断。
2. 再比较标题、时间、话题等非回复链上下文是否真的不同。
3. 不要把合成的 `parent_comment/reply_chain` 当强证据。
4. 如果只是换标题/平台/泛泛场景，或靠假回复链撑风险，结论倾向 `删掉`、`退回重写` 或 `降权`。
5. 如果确实构成同文不同语境对照，结论可写 `保留对照`。

#### 涉及样本详情

#### `MEME_EXPAND_0030_MEDIUM`

- 标签：risk_level=`medium`；binary=`B01 / unsafe`；hard_negative=`false`
- 编码：primary=`C3_数字代指`；secondary=`E3_回复链/互动触发；C1_历史人物类比`
- 上下文审计：class=`C02 / contextual_required`；flags=`none`；duplicate=`D03 / template_pollution_candidate`
- context_required：`true`
- 上下文：
  - title：历史剧二创
  - description：无
  - parent_comment（旧字段，默认不作强证据）：别说像谁
  - reply_chain（旧字段，默认不作强证据）：像，但别展开
  - time：2026-02-28
  - topic：日期/数字代指
- 关键 reasoning：
  - supporting_evidence：文本或上下文提供可疑编码线索。
  - counter_evidence：普通解释仍可成立，缺少直接目标或更完整上下文。
  - final_rationale：有明显复核价值，但证据不足以确定为high，标为medium。
- review_notes：source=meme_expansion; original_id=EXPAND_0030; generated_expansion; needs_human_review; original_primary=B1_拆字; original_notes=generated_expansion; needs_human_review; meme_cluster=日期/数字代指; context_audit_class=contextual_required; context_audit_class_code=C02; context_audit_flag_codes=none; safety_binary=unsafe; safety_binary_code=B01; duplicate_text_status=template_pollution_candidate; duplicate_text_status_code=D03; preview_only=true

#### `MEME_EXPAND_0044_MEDIUM`

- 标签：risk_level=`medium`；binary=`B01 / unsafe`；hard_negative=`false`
- 编码：primary=`E3_回复链/互动触发`；secondary=`E1_平台黑话；C4_典故/物品/符号借用`
- 上下文审计：class=`C02 / contextual_required`；flags=`F01`；duplicate=`D03 / template_pollution_candidate`
- context_required：`true`
- 上下文：
  - title：热搜评论区
  - description：无
  - parent_comment（旧字段，默认不作强证据）：这波是不是又要统一口径
  - reply_chain（旧字段，默认不作强证据）：缩写就行
  - time：2026-05-19
  - topic：日期/数字代指
- 关键 reasoning：
  - supporting_evidence：文本或上下文提供可疑编码线索。
  - counter_evidence：普通解释仍可成立，缺少直接目标或更完整上下文。
  - final_rationale：有明显复核价值，但证据不足以确定为high，标为medium。
- review_notes：source=meme_expansion; original_id=EXPAND_0044; generated_expansion; needs_human_review; original_primary=E3_回复链/互动触发; original_notes=generated_expansion; needs_human_review; meme_cluster=日期/数字代指; context_audit_class=contextual_required; context_audit_class_code=C02; context_audit_flag_codes=F01; safety_binary=unsafe; safety_binary_code=B01; duplicate_text_status=template_pollution_candidate; duplicate_text_status_code=D03; preview_only=true

#### `MEME_EXPAND_0058_MEDIUM`

- 标签：risk_level=`medium`；binary=`B01 / unsafe`；hard_negative=`false`
- 编码：primary=`F_组合编码`；secondary=`A2_拼音/首字母缩写；B4_符号/空格/Unicode 干扰`
- 上下文审计：class=`C02 / contextual_required`；flags=`F01`；duplicate=`D03 / template_pollution_candidate`
- context_required：`true`
- 上下文：
  - title：社会趋势讨论话题
  - description：无
  - parent_comment（旧字段，默认不作强证据）：别说太满
  - reply_chain（旧字段，默认不作强证据）：像，但不敢说
  - time：2026-04-20
  - topic：日期/数字代指
- 关键 reasoning：
  - supporting_evidence：文本或上下文提供可疑编码线索。
  - counter_evidence：普通解释仍可成立，缺少直接目标或更完整上下文。
  - final_rationale：有明显复核价值，但证据不足以确定为high，标为medium。
- review_notes：source=meme_expansion; original_id=EXPAND_0058; generated_expansion; needs_human_review; original_primary=F_组合编码; original_notes=generated_expansion; needs_human_review; meme_cluster=日期/数字代指; context_audit_class=contextual_required; context_audit_class_code=C02; context_audit_flag_codes=F01; safety_binary=unsafe; safety_binary_code=B01; duplicate_text_status=template_pollution_candidate; duplicate_text_status_code=D03; preview_only=true

- 复核结论：待填写

### 重复组 05

- 状态：`D02` / `same_text_different_context_review` / 同文同标签但不同上下文，待复核
- 出现次数：3
- 重复文本：倒车镜调低一点更适合我身高
- 风险分布：{"none": 3}
- 来源分布：{"meme_expansion": 3}
- 建议动作：看是否只是重复造句；如果上下文差异没有训练价值，建议删/重写/降权。

#### 本组怎么审

1. 先看文本本身是否足以判断。
2. 再比较标题、时间、话题等非回复链上下文是否真的不同。
3. 不要把合成的 `parent_comment/reply_chain` 当强证据。
4. 如果只是换标题/平台/泛泛场景，或靠假回复链撑风险，结论倾向 `删掉`、`退回重写` 或 `降权`。
5. 如果确实构成同文不同语境对照，结论可写 `保留对照`。

#### 涉及样本详情

#### `MEME_EXPAND_0092_NONE`

- 标签：risk_level=`none`；binary=`B02 / safe`；hard_negative=`true`
- 编码：primary=`none`；secondary=`无`
- 上下文审计：class=`C03 / safe_without_context`；flags=`F01+F04`；duplicate=`D02 / same_text_different_context_review`
- context_required：`true`
- 上下文：
  - title：课程/教程内容
  - description：无
  - parent_comment（旧字段，默认不作强证据）：讨论学习或技术问题
  - reply_chain（旧字段，默认不作强证据）：上下文支持普通解释
  - time：2026-03-06
  - topic：加速/刹车/倒车
- 关键 reasoning：
  - supporting_evidence：无
  - counter_evidence：上下文明确指向普通生活、学习、商品、娱乐或技术场景。；没有规避检测意图、隐含目标或异常互动共识。；相关词语可由字面含义充分解释。
  - final_rationale：反证充分，风险解释不成立，标为none。
- review_notes：source=meme_expansion; original_id=EXPAND_0092; generated_expansion; needs_human_review; original_primary=C3_数字代指; original_notes=generated_expansion; needs_human_review; meme_cluster=加速/刹车/倒车; context_audit_class=safe_without_context; context_audit_class_code=C03; context_audit_flag_codes=F01+F04; safety_binary=safe; safety_binary_code=B02; duplicate_text_status=same_text_different_context_review; duplicate_text_status_code=D02; preview_only=true

#### `MEME_EXPAND_0106_NONE`

- 标签：risk_level=`none`；binary=`B02 / safe`；hard_negative=`true`
- 编码：primary=`none`；secondary=`无`
- 上下文审计：class=`C03 / safe_without_context`；flags=`F01+F04`；duplicate=`D02 / same_text_different_context_review`
- context_required：`true`
- 上下文：
  - title：普通生活帖
  - description：无
  - parent_comment（旧字段，默认不作强证据）：字面场景明确
  - reply_chain（旧字段，默认不作强证据）：无异常互动
  - time：2026-06-04
  - topic：加速/刹车/倒车
- 关键 reasoning：
  - supporting_evidence：无
  - counter_evidence：上下文明确指向普通生活、学习、商品、娱乐或技术场景。；没有规避检测意图、隐含目标或异常互动共识。；相关词语可由字面含义充分解释。
  - final_rationale：反证充分，风险解释不成立，标为none。
- review_notes：source=meme_expansion; original_id=EXPAND_0106; generated_expansion; needs_human_review; original_primary=B3_形近字替换; original_notes=generated_expansion; needs_human_review; meme_cluster=加速/刹车/倒车; context_audit_class=safe_without_context; context_audit_class_code=C03; context_audit_flag_codes=F01+F04; safety_binary=safe; safety_binary_code=B02; duplicate_text_status=same_text_different_context_review; duplicate_text_status_code=D02; preview_only=true

#### `MEME_EXPAND_0120_NONE`

- 标签：risk_level=`none`；binary=`B02 / safe`；hard_negative=`true`
- 编码：primary=`none`；secondary=`无`
- 上下文审计：class=`C03 / safe_without_context`；flags=`F01+F04`；duplicate=`D02 / same_text_different_context_review`
- context_required：`true`
- 上下文：
  - title：商品/美食测评
  - description：无
  - parent_comment（旧字段，默认不作强证据）：只讨论购买和使用体验
  - reply_chain（旧字段，默认不作强证据）：没有隐含目标
  - time：2026-05-05
  - topic：加速/刹车/倒车
- 关键 reasoning：
  - supporting_evidence：无
  - counter_evidence：上下文明确指向普通生活、学习、商品、娱乐或技术场景。；没有规避检测意图、隐含目标或异常互动共识。；相关词语可由字面含义充分解释。
  - final_rationale：反证充分，风险解释不成立，标为none。
- review_notes：source=meme_expansion; original_id=EXPAND_0120; generated_expansion; needs_human_review; original_primary=none; original_notes=generated_expansion; needs_human_review; meme_cluster=加速/刹车/倒车; context_audit_class=safe_without_context; context_audit_class_code=C03; context_audit_flag_codes=F01+F04; safety_binary=safe; safety_binary_code=B02; duplicate_text_status=same_text_different_context_review; duplicate_text_status_code=D02; preview_only=true

- 复核结论：待填写

### 重复组 06

- 状态：`D03` / `template_pollution_candidate` / 疑似模板污染，优先删/重写/降权
- 出现次数：3
- 重复文本：单条懂没信息，但接在删前留名后就变味了
- 风险分布：{"medium": 3}
- 来源分布：{"meme_expansion": 3}
- 建议动作：优先判为模板污染候选；建议退回重写或后续从高质量训练集中剔除。

#### 本组怎么审

1. 先看文本本身是否足以判断。
2. 再比较标题、时间、话题等非回复链上下文是否真的不同。
3. 不要把合成的 `parent_comment/reply_chain` 当强证据。
4. 如果只是换标题/平台/泛泛场景，或靠假回复链撑风险，结论倾向 `删掉`、`退回重写` 或 `降权`。
5. 如果确实构成同文不同语境对照，结论可写 `保留对照`。

#### 涉及样本详情

#### `MEME_EXPAND_0028_MEDIUM`

- 标签：risk_level=`medium`；binary=`B01 / unsafe`；hard_negative=`false`
- 编码：primary=`C4_典故/物品/符号借用`；secondary=`E1_平台黑话；E3_回复链/互动触发`
- 上下文审计：class=`C02 / contextual_required`；flags=`F01`；duplicate=`D03 / template_pollution_candidate`
- context_required：`true`
- 上下文：
  - title：社会趋势讨论话题
  - description：无
  - parent_comment（旧字段，默认不作强证据）：别说太满
  - reply_chain（旧字段，默认不作强证据）：像，但不敢说
  - time：2026-04-20
  - topic：平台黑话/自我审查
- 关键 reasoning：
  - supporting_evidence：文本或上下文提供可疑编码线索。
  - counter_evidence：普通解释仍可成立，缺少直接目标或更完整上下文。
  - final_rationale：有明显复核价值，但证据不足以确定为high，标为medium。
- review_notes：source=meme_expansion; original_id=EXPAND_0028; generated_expansion; needs_human_review; original_primary=A2_拼音/首字母缩写; original_notes=generated_expansion; needs_human_review; meme_cluster=平台黑话/自我审查; context_audit_class=contextual_required; context_audit_class_code=C02; context_audit_flag_codes=F01; safety_binary=unsafe; safety_binary_code=B01; duplicate_text_status=template_pollution_candidate; duplicate_text_status_code=D03; preview_only=true

#### `MEME_EXPAND_0042_MEDIUM`

- 标签：risk_level=`medium`；binary=`B01 / unsafe`；hard_negative=`false`
- 编码：primary=`E3_回复链/互动触发`；secondary=`E1_平台黑话；C4_典故/物品/符号借用`
- 上下文审计：class=`C02 / contextual_required`；flags=`none`；duplicate=`D03 / template_pollution_candidate`
- context_required：`true`
- 上下文：
  - title：历史剧二创
  - description：无
  - parent_comment（旧字段，默认不作强证据）：别说像谁
  - reply_chain（旧字段，默认不作强证据）：像，但别展开
  - time：2026-02-28
  - topic：平台黑话/自我审查
- 关键 reasoning：
  - supporting_evidence：文本或上下文提供可疑编码线索。
  - counter_evidence：普通解释仍可成立，缺少直接目标或更完整上下文。
  - final_rationale：有明显复核价值，但证据不足以确定为high，标为medium。
- review_notes：source=meme_expansion; original_id=EXPAND_0042; generated_expansion; needs_human_review; original_primary=E3_回复链/互动触发; original_notes=generated_expansion; needs_human_review; meme_cluster=平台黑话/自我审查; context_audit_class=contextual_required; context_audit_class_code=C02; context_audit_flag_codes=none; safety_binary=unsafe; safety_binary_code=B01; duplicate_text_status=template_pollution_candidate; duplicate_text_status_code=D03; preview_only=true

#### `MEME_EXPAND_0056_MEDIUM`

- 标签：risk_level=`medium`；binary=`B01 / unsafe`；hard_negative=`false`
- 编码：primary=`D1_反讽`；secondary=`E3_回复链/互动触发`
- 上下文审计：class=`C02 / contextual_required`；flags=`F01`；duplicate=`D03 / template_pollution_candidate`
- context_required：`true`
- 上下文：
  - title：热搜评论区
  - description：无
  - parent_comment（旧字段，默认不作强证据）：这波是不是又要统一口径
  - reply_chain（旧字段，默认不作强证据）：缩写就行
  - time：2026-05-19
  - topic：平台黑话/自我审查
- 关键 reasoning：
  - supporting_evidence：文本或上下文提供可疑编码线索。
  - counter_evidence：普通解释仍可成立，缺少直接目标或更完整上下文。
  - final_rationale：有明显复核价值，但证据不足以确定为high，标为medium。
- review_notes：source=meme_expansion; original_id=EXPAND_0056; generated_expansion; needs_human_review; original_primary=D1_反讽; original_notes=generated_expansion; needs_human_review; meme_cluster=平台黑话/自我审查; context_audit_class=contextual_required; context_audit_class_code=C02; context_audit_flag_codes=F01; safety_binary=unsafe; safety_binary_code=B01; duplicate_text_status=template_pollution_candidate; duplicate_text_status_code=D03; preview_only=true

- 复核结论：待填写

### 重复组 07

- 状态：`D03` / `template_pollution_candidate` / 疑似模板污染，优先删/重写/降权
- 出现次数：3
- 重复文本：大家都说历史重演，但没有说明映射到哪件事
- 风险分布：{"medium": 3}
- 来源分布：{"meme_expansion": 3}
- 建议动作：优先判为模板污染候选；建议退回重写或后续从高质量训练集中剔除。

#### 本组怎么审

1. 先看文本本身是否足以判断。
2. 再比较标题、时间、话题等非回复链上下文是否真的不同。
3. 不要把合成的 `parent_comment/reply_chain` 当强证据。
4. 如果只是换标题/平台/泛泛场景，或靠假回复链撑风险，结论倾向 `删掉`、`退回重写` 或 `降权`。
5. 如果确实构成同文不同语境对照，结论可写 `保留对照`。

#### 涉及样本详情

#### `MEME_EXPAND_0032_MEDIUM`

- 标签：risk_level=`medium`；binary=`B01 / unsafe`；hard_negative=`false`
- 编码：primary=`C2_历史事件影射`；secondary=`E3_回复链/互动触发；C1_历史人物类比`
- 上下文审计：class=`C02 / contextual_required`；flags=`F01`；duplicate=`D03 / template_pollution_candidate`
- context_required：`true`
- 上下文：
  - title：热搜评论区
  - description：无
  - parent_comment（旧字段，默认不作强证据）：这波是不是又要统一口径
  - reply_chain（旧字段，默认不作强证据）：缩写就行
  - time：2026-05-19
  - topic：历史事件影射
- 关键 reasoning：
  - supporting_evidence：文本或上下文提供可疑编码线索。
  - counter_evidence：普通解释仍可成立，缺少直接目标或更完整上下文。
  - final_rationale：有明显复核价值，但证据不足以确定为high，标为medium。
- review_notes：source=meme_expansion; original_id=EXPAND_0032; generated_expansion; needs_human_review; original_primary=B1_拆字; original_notes=generated_expansion; needs_human_review; meme_cluster=历史事件影射; context_audit_class=contextual_required; context_audit_class_code=C02; context_audit_flag_codes=F01; safety_binary=unsafe; safety_binary_code=B01; duplicate_text_status=template_pollution_candidate; duplicate_text_status_code=D03; preview_only=true

#### `MEME_EXPAND_0046_MEDIUM`

- 标签：risk_level=`medium`；binary=`B01 / unsafe`；hard_negative=`false`
- 编码：primary=`C3_数字代指`；secondary=`E2_时间节点触发`
- 上下文审计：class=`C02 / contextual_required`；flags=`F01`；duplicate=`D03 / template_pollution_candidate`
- context_required：`true`
- 上下文：
  - title：社会趋势讨论话题
  - description：无
  - parent_comment（旧字段，默认不作强证据）：别说太满
  - reply_chain（旧字段，默认不作强证据）：像，但不敢说
  - time：2026-04-20
  - topic：历史事件影射
- 关键 reasoning：
  - supporting_evidence：文本或上下文提供可疑编码线索。
  - counter_evidence：普通解释仍可成立，缺少直接目标或更完整上下文。
  - final_rationale：有明显复核价值，但证据不足以确定为high，标为medium。
- review_notes：source=meme_expansion; original_id=EXPAND_0046; generated_expansion; needs_human_review; original_primary=C3_数字代指; original_notes=generated_expansion; needs_human_review; meme_cluster=历史事件影射; context_audit_class=contextual_required; context_audit_class_code=C02; context_audit_flag_codes=F01; safety_binary=unsafe; safety_binary_code=B01; duplicate_text_status=template_pollution_candidate; duplicate_text_status_code=D03; preview_only=true

#### `MEME_EXPAND_0060_MEDIUM`

- 标签：risk_level=`medium`；binary=`B01 / unsafe`；hard_negative=`false`
- 编码：primary=`F_组合编码`；secondary=`A2_拼音/首字母缩写；B4_符号/空格/Unicode 干扰`
- 上下文审计：class=`C02 / contextual_required`；flags=`none`；duplicate=`D03 / template_pollution_candidate`
- context_required：`true`
- 上下文：
  - title：历史剧二创
  - description：无
  - parent_comment（旧字段，默认不作强证据）：别说像谁
  - reply_chain（旧字段，默认不作强证据）：像，但别展开
  - time：2026-02-28
  - topic：历史事件影射
- 关键 reasoning：
  - supporting_evidence：文本或上下文提供可疑编码线索。
  - counter_evidence：普通解释仍可成立，缺少直接目标或更完整上下文。
  - final_rationale：有明显复核价值，但证据不足以确定为high，标为medium。
- review_notes：source=meme_expansion; original_id=EXPAND_0060; generated_expansion; needs_human_review; original_primary=F_组合编码; original_notes=generated_expansion; needs_human_review; meme_cluster=历史事件影射; context_audit_class=contextual_required; context_audit_class_code=C02; context_audit_flag_codes=none; safety_binary=unsafe; safety_binary_code=B01; duplicate_text_status=template_pollution_candidate; duplicate_text_status_code=D03; preview_only=true

- 复核结论：待填写

### 重复组 08

- 状态：`D03` / `template_pollution_candidate` / 疑似模板污染，优先删/重写/降权
- 出现次数：3
- 重复文本：这个末代角色被剪成现实感很强的混剪
- 风险分布：{"medium": 3}
- 来源分布：{"meme_expansion": 3}
- 建议动作：优先判为模板污染候选；建议退回重写或后续从高质量训练集中剔除。

#### 本组怎么审

1. 先看文本本身是否足以判断。
2. 再比较标题、时间、话题等非回复链上下文是否真的不同。
3. 不要把合成的 `parent_comment/reply_chain` 当强证据。
4. 如果只是换标题/平台/泛泛场景，或靠假回复链撑风险，结论倾向 `删掉`、`退回重写` 或 `降权`。
5. 如果确实构成同文不同语境对照，结论可写 `保留对照`。

#### 涉及样本详情

#### `MEME_EXPAND_0031_MEDIUM`

- 标签：risk_level=`medium`；binary=`B01 / unsafe`；hard_negative=`false`
- 编码：primary=`C1_历史人物类比`；secondary=`E3_回复链/互动触发`
- 上下文审计：class=`C02 / contextual_required`；flags=`F01`；duplicate=`D03 / template_pollution_candidate`
- context_required：`true`
- 上下文：
  - title：社会趋势讨论话题
  - description：无
  - parent_comment（旧字段，默认不作强证据）：别说太满
  - reply_chain（旧字段，默认不作强证据）：像，但不敢说
  - time：2026-04-20
  - topic：历史人物类比
- 关键 reasoning：
  - supporting_evidence：文本或上下文提供可疑编码线索。
  - counter_evidence：普通解释仍可成立，缺少直接目标或更完整上下文。
  - final_rationale：有明显复核价值，但证据不足以确定为high，标为medium。
- review_notes：source=meme_expansion; original_id=EXPAND_0031; generated_expansion; needs_human_review; original_primary=B1_拆字; original_notes=generated_expansion; needs_human_review; meme_cluster=历史人物类比; context_audit_class=contextual_required; context_audit_class_code=C02; context_audit_flag_codes=F01; safety_binary=unsafe; safety_binary_code=B01; duplicate_text_status=template_pollution_candidate; duplicate_text_status_code=D03; preview_only=true

#### `MEME_EXPAND_0045_MEDIUM`

- 标签：risk_level=`medium`；binary=`B01 / unsafe`；hard_negative=`false`
- 编码：primary=`E3_回复链/互动触发`；secondary=`E1_平台黑话`
- 上下文审计：class=`C02 / contextual_required`；flags=`none`；duplicate=`D03 / template_pollution_candidate`
- context_required：`true`
- 上下文：
  - title：历史剧二创
  - description：无
  - parent_comment（旧字段，默认不作强证据）：别说像谁
  - reply_chain（旧字段，默认不作强证据）：像，但别展开
  - time：2026-02-28
  - topic：历史人物类比
- 关键 reasoning：
  - supporting_evidence：文本或上下文提供可疑编码线索。
  - counter_evidence：普通解释仍可成立，缺少直接目标或更完整上下文。
  - final_rationale：有明显复核价值，但证据不足以确定为high，标为medium。
- review_notes：source=meme_expansion; original_id=EXPAND_0045; generated_expansion; needs_human_review; original_primary=E3_回复链/互动触发; original_notes=generated_expansion; needs_human_review; meme_cluster=历史人物类比; context_audit_class=contextual_required; context_audit_class_code=C02; context_audit_flag_codes=none; safety_binary=unsafe; safety_binary_code=B01; duplicate_text_status=template_pollution_candidate; duplicate_text_status_code=D03; preview_only=true

#### `MEME_EXPAND_0059_MEDIUM`

- 标签：risk_level=`medium`；binary=`B01 / unsafe`；hard_negative=`false`
- 编码：primary=`F_组合编码`；secondary=`A2_拼音/首字母缩写`
- 上下文审计：class=`C02 / contextual_required`；flags=`F01`；duplicate=`D03 / template_pollution_candidate`
- context_required：`true`
- 上下文：
  - title：热搜评论区
  - description：无
  - parent_comment（旧字段，默认不作强证据）：这波是不是又要统一口径
  - reply_chain（旧字段，默认不作强证据）：缩写就行
  - time：2026-05-19
  - topic：历史人物类比
- 关键 reasoning：
  - supporting_evidence：文本或上下文提供可疑编码线索。
  - counter_evidence：普通解释仍可成立，缺少直接目标或更完整上下文。
  - final_rationale：有明显复核价值，但证据不足以确定为high，标为medium。
- review_notes：source=meme_expansion; original_id=EXPAND_0059; generated_expansion; needs_human_review; original_primary=F_组合编码; original_notes=generated_expansion; needs_human_review; meme_cluster=历史人物类比; context_audit_class=contextual_required; context_audit_class_code=C02; context_audit_flag_codes=F01; safety_binary=unsafe; safety_binary_code=B01; duplicate_text_status=template_pollution_candidate; duplicate_text_status_code=D03; preview_only=true

- 复核结论：待填写

### 重复组 09

- 状态：`D02` / `same_text_different_context_review` / 同文同标签但不同上下文，待复核
- 出现次数：3
- 重复文本：这句感谢安排配上翻车现场，像阴阳但对象不明
- 风险分布：{"medium": 3}
- 来源分布：{"meme_expansion": 3}
- 建议动作：看是否只是重复造句；如果上下文差异没有训练价值，建议删/重写/降权。

#### 本组怎么审

1. 先看文本本身是否足以判断。
2. 再比较标题、时间、话题等非回复链上下文是否真的不同。
3. 不要把合成的 `parent_comment/reply_chain` 当强证据。
4. 如果只是换标题/平台/泛泛场景，或靠假回复链撑风险，结论倾向 `删掉`、`退回重写` 或 `降权`。
5. 如果确实构成同文不同语境对照，结论可写 `保留对照`。

#### 涉及样本详情

#### `MEME_EXPAND_0027_MEDIUM`

- 标签：risk_level=`medium`；binary=`B01 / unsafe`；hard_negative=`false`
- 编码：primary=`D1_反讽`；secondary=`E1_平台黑话`
- 上下文审计：class=`C02 / contextual_required`；flags=`none`；duplicate=`D02 / same_text_different_context_review`
- context_required：`true`
- 上下文：
  - title：历史剧二创
  - description：无
  - parent_comment（旧字段，默认不作强证据）：别说像谁
  - reply_chain（旧字段，默认不作强证据）：像，但别展开
  - time：2026-02-28
  - topic：反讽/阴阳怪气
- 关键 reasoning：
  - supporting_evidence：文本或上下文提供可疑编码线索。
  - counter_evidence：普通解释仍可成立，缺少直接目标或更完整上下文。
  - final_rationale：有明显复核价值，但证据不足以确定为high，标为medium。
- review_notes：source=meme_expansion; original_id=EXPAND_0027; generated_expansion; needs_human_review; original_primary=A2_拼音/首字母缩写; original_notes=generated_expansion; needs_human_review; meme_cluster=反讽/阴阳怪气; context_audit_class=contextual_required; context_audit_class_code=C02; context_audit_flag_codes=none; safety_binary=unsafe; safety_binary_code=B01; duplicate_text_status=same_text_different_context_review; duplicate_text_status_code=D02; preview_only=true

#### `MEME_EXPAND_0041_MEDIUM`

- 标签：risk_level=`medium`；binary=`B01 / unsafe`；hard_negative=`false`
- 编码：primary=`E2_时间节点触发`；secondary=`C3_数字代指`
- 上下文审计：class=`C02 / contextual_required`；flags=`F01`；duplicate=`D02 / same_text_different_context_review`
- context_required：`true`
- 上下文：
  - title：热搜评论区
  - description：无
  - parent_comment（旧字段，默认不作强证据）：这波是不是又要统一口径
  - reply_chain（旧字段，默认不作强证据）：缩写就行
  - time：2026-05-19
  - topic：反讽/阴阳怪气
- 关键 reasoning：
  - supporting_evidence：文本或上下文提供可疑编码线索。
  - counter_evidence：普通解释仍可成立，缺少直接目标或更完整上下文。
  - final_rationale：有明显复核价值，但证据不足以确定为high，标为medium。
- review_notes：source=meme_expansion; original_id=EXPAND_0041; generated_expansion; needs_human_review; original_primary=E2_时间节点触发; original_notes=generated_expansion; needs_human_review; meme_cluster=反讽/阴阳怪气; context_audit_class=contextual_required; context_audit_class_code=C02; context_audit_flag_codes=F01; safety_binary=unsafe; safety_binary_code=B01; duplicate_text_status=same_text_different_context_review; duplicate_text_status_code=D02; preview_only=true

#### `MEME_EXPAND_0055_MEDIUM`

- 标签：risk_level=`medium`；binary=`B01 / unsafe`；hard_negative=`false`
- 编码：primary=`D1_反讽`；secondary=`E3_回复链/互动触发`
- 上下文审计：class=`C02 / contextual_required`；flags=`F01`；duplicate=`D02 / same_text_different_context_review`
- context_required：`true`
- 上下文：
  - title：社会趋势讨论话题
  - description：无
  - parent_comment（旧字段，默认不作强证据）：别说太满
  - reply_chain（旧字段，默认不作强证据）：像，但不敢说
  - time：2026-04-20
  - topic：反讽/阴阳怪气
- 关键 reasoning：
  - supporting_evidence：文本或上下文提供可疑编码线索。
  - counter_evidence：普通解释仍可成立，缺少直接目标或更完整上下文。
  - final_rationale：有明显复核价值，但证据不足以确定为high，标为medium。
- review_notes：source=meme_expansion; original_id=EXPAND_0055; generated_expansion; needs_human_review; original_primary=D1_反讽; original_notes=generated_expansion; needs_human_review; meme_cluster=反讽/阴阳怪气; context_audit_class=contextual_required; context_audit_class_code=C02; context_audit_flag_codes=F01; safety_binary=unsafe; safety_binary_code=B01; duplicate_text_status=same_text_different_context_review; duplicate_text_status_code=D02; preview_only=true

- 复核结论：待填写

### 重复组 10

- 状态：`D03` / `template_pollution_candidate` / 疑似模板污染，优先删/重写/降权
- 出现次数：3
- 重复文本：这司机又说为了大家好，结果油门没松过
- 风险分布：{"medium": 3}
- 来源分布：{"meme_expansion": 3}
- 建议动作：优先判为模板污染候选；建议退回重写或后续从高质量训练集中剔除。

#### 本组怎么审

1. 先看文本本身是否足以判断。
2. 再比较标题、时间、话题等非回复链上下文是否真的不同。
3. 不要把合成的 `parent_comment/reply_chain` 当强证据。
4. 如果只是换标题/平台/泛泛场景，或靠假回复链撑风险，结论倾向 `删掉`、`退回重写` 或 `降权`。
5. 如果确实构成同文不同语境对照，结论可写 `保留对照`。

#### 涉及样本详情

#### `MEME_EXPAND_0029_MEDIUM`

- 标签：risk_level=`medium`；binary=`B01 / unsafe`；hard_negative=`false`
- 编码：primary=`C4_典故/物品/符号借用`；secondary=`E3_回复链/互动触发`
- 上下文审计：class=`C02 / contextual_required`；flags=`F01`；duplicate=`D03 / template_pollution_candidate`
- context_required：`true`
- 上下文：
  - title：热搜评论区
  - description：无
  - parent_comment（旧字段，默认不作强证据）：这波是不是又要统一口径
  - reply_chain（旧字段，默认不作强证据）：缩写就行
  - time：2026-05-19
  - topic：加速/刹车/倒车
- 关键 reasoning：
  - supporting_evidence：文本或上下文提供可疑编码线索。
  - counter_evidence：普通解释仍可成立，缺少直接目标或更完整上下文。
  - final_rationale：有明显复核价值，但证据不足以确定为high，标为medium。
- review_notes：source=meme_expansion; original_id=EXPAND_0029; generated_expansion; needs_human_review; original_primary=B1_拆字; original_notes=generated_expansion; needs_human_review; meme_cluster=加速/刹车/倒车; context_audit_class=contextual_required; context_audit_class_code=C02; context_audit_flag_codes=F01; safety_binary=unsafe; safety_binary_code=B01; duplicate_text_status=template_pollution_candidate; duplicate_text_status_code=D03; preview_only=true

#### `MEME_EXPAND_0043_MEDIUM`

- 标签：risk_level=`medium`；binary=`B01 / unsafe`；hard_negative=`false`
- 编码：primary=`E3_回复链/互动触发`；secondary=`E1_平台黑话`
- 上下文审计：class=`C02 / contextual_required`；flags=`F01`；duplicate=`D03 / template_pollution_candidate`
- context_required：`true`
- 上下文：
  - title：社会趋势讨论话题
  - description：无
  - parent_comment（旧字段，默认不作强证据）：别说太满
  - reply_chain（旧字段，默认不作强证据）：像，但不敢说
  - time：2026-04-20
  - topic：加速/刹车/倒车
- 关键 reasoning：
  - supporting_evidence：文本或上下文提供可疑编码线索。
  - counter_evidence：普通解释仍可成立，缺少直接目标或更完整上下文。
  - final_rationale：有明显复核价值，但证据不足以确定为high，标为medium。
- review_notes：source=meme_expansion; original_id=EXPAND_0043; generated_expansion; needs_human_review; original_primary=E3_回复链/互动触发; original_notes=generated_expansion; needs_human_review; meme_cluster=加速/刹车/倒车; context_audit_class=contextual_required; context_audit_class_code=C02; context_audit_flag_codes=F01; safety_binary=unsafe; safety_binary_code=B01; duplicate_text_status=template_pollution_candidate; duplicate_text_status_code=D03; preview_only=true

#### `MEME_EXPAND_0057_MEDIUM`

- 标签：risk_level=`medium`；binary=`B01 / unsafe`；hard_negative=`false`
- 编码：primary=`F_组合编码`；secondary=`A2_拼音/首字母缩写`
- 上下文审计：class=`C02 / contextual_required`；flags=`none`；duplicate=`D03 / template_pollution_candidate`
- context_required：`true`
- 上下文：
  - title：历史剧二创
  - description：无
  - parent_comment（旧字段，默认不作强证据）：别说像谁
  - reply_chain（旧字段，默认不作强证据）：像，但别展开
  - time：2026-02-28
  - topic：加速/刹车/倒车
- 关键 reasoning：
  - supporting_evidence：文本或上下文提供可疑编码线索。
  - counter_evidence：普通解释仍可成立，缺少直接目标或更完整上下文。
  - final_rationale：有明显复核价值，但证据不足以确定为high，标为medium。
- review_notes：source=meme_expansion; original_id=EXPAND_0057; generated_expansion; needs_human_review; original_primary=F_组合编码; original_notes=generated_expansion; needs_human_review; meme_cluster=加速/刹车/倒车; context_audit_class=contextual_required; context_audit_class_code=C02; context_audit_flag_codes=none; safety_binary=unsafe; safety_binary_code=B01; duplicate_text_status=template_pollution_candidate; duplicate_text_status_code=D03; preview_only=true

- 复核结论：待填写

### 重复组 11

- 状态：`D03` / `template_pollution_candidate` / 疑似模板污染，优先删/重写/降权
- 出现次数：3
- 重复文本：这游戏优化真棒，卡成PPT
- 风险分布：{"low": 3}
- 来源分布：{"meme_expansion": 3}
- 建议动作：优先判为模板污染候选；建议退回重写或后续从高质量训练集中剔除。

#### 本组怎么审

1. 先看文本本身是否足以判断。
2. 再比较标题、时间、话题等非回复链上下文是否真的不同。
3. 不要把合成的 `parent_comment/reply_chain` 当强证据。
4. 如果只是换标题/平台/泛泛场景，或靠假回复链撑风险，结论倾向 `删掉`、`退回重写` 或 `降权`。
5. 如果确实构成同文不同语境对照，结论可写 `保留对照`。

#### 涉及样本详情

#### `MEME_EXPAND_0062_LOW`

- 标签：risk_level=`low`；binary=`B01 / unsafe`；hard_negative=`true`
- 编码：primary=`C3_数字代指`；secondary=`无`
- 上下文审计：class=`C02 / contextual_required`；flags=`none`；duplicate=`D03 / template_pollution_candidate`
- context_required：`true`
- 上下文：
  - title：教学/教程评论区
  - description：无
  - parent_comment（旧字段，默认不作强证据）：讨论的是具体技巧
  - reply_chain（旧字段，默认不作强证据）：普通解释更强
  - time：2026-03-16
  - topic：反讽/阴阳怪气
- 关键 reasoning：
  - supporting_evidence：存在关键词、缩写、数字或符号撞车。
  - counter_evidence：上下文提供普通生活、教学、娱乐或技术解释。；缺少规避意图、目标映射或敏感语境。
  - final_rationale：普通解释更强，仅保留低风险或困难负样本价值，标为low。
- review_notes：source=meme_expansion; original_id=EXPAND_0062; generated_expansion; needs_human_review; original_primary=C3_数字代指; original_notes=generated_expansion; needs_human_review; meme_cluster=反讽/阴阳怪气; context_audit_class=contextual_required; context_audit_class_code=C02; context_audit_flag_codes=none; safety_binary=unsafe; safety_binary_code=B01; duplicate_text_status=template_pollution_candidate; duplicate_text_status_code=D03; preview_only=true

#### `MEME_EXPAND_0076_LOW`

- 标签：risk_level=`low`；binary=`B01 / unsafe`；hard_negative=`true`
- 编码：primary=`E2_时间节点触发`；secondary=`无`
- 上下文审计：class=`C02 / contextual_required`；flags=`none`；duplicate=`D03 / template_pollution_candidate`
- context_required：`true`
- 上下文：
  - title：日常生活分享
  - description：无
  - parent_comment（旧字段，默认不作强证据）：只是普通记录
  - reply_chain（旧字段，默认不作强证据）：别过度联想
  - time：2026-06-04
  - topic：反讽/阴阳怪气
- 关键 reasoning：
  - supporting_evidence：存在关键词、缩写、数字或符号撞车。
  - counter_evidence：上下文提供普通生活、教学、娱乐或技术解释。；缺少规避意图、目标映射或敏感语境。
  - final_rationale：普通解释更强，仅保留低风险或困难负样本价值，标为low。
- review_notes：source=meme_expansion; original_id=EXPAND_0076; generated_expansion; needs_human_review; original_primary=E2_时间节点触发; original_notes=generated_expansion; needs_human_review; meme_cluster=反讽/阴阳怪气; context_audit_class=contextual_required; context_audit_class_code=C02; context_audit_flag_codes=none; safety_binary=unsafe; safety_binary_code=B01; duplicate_text_status=template_pollution_candidate; duplicate_text_status_code=D03; preview_only=true

#### `MEME_EXPAND_0090_LOW`

- 标签：risk_level=`low`；binary=`B01 / unsafe`；hard_negative=`true`
- 编码：primary=`C4_典故/物品/符号借用`；secondary=`无`
- 上下文审计：class=`C02 / contextual_required`；flags=`F01`；duplicate=`D03 / template_pollution_candidate`
- context_required：`true`
- 上下文：
  - title：美食/文具/娱乐分享
  - description：无
  - parent_comment（旧字段，默认不作强证据）：求链接
  - reply_chain（旧字段，默认不作强证据）：只讨论字面对象
  - time：2026-05-05
  - topic：反讽/阴阳怪气
- 关键 reasoning：
  - supporting_evidence：存在关键词、缩写、数字或符号撞车。
  - counter_evidence：上下文提供普通生活、教学、娱乐或技术解释。；缺少规避意图、目标映射或敏感语境。
  - final_rationale：普通解释更强，仅保留低风险或困难负样本价值，标为low。
- review_notes：source=meme_expansion; original_id=EXPAND_0090; generated_expansion; needs_human_review; original_primary=C4_典故/物品/符号借用; original_notes=generated_expansion; needs_human_review; meme_cluster=反讽/阴阳怪气; context_audit_class=contextual_required; context_audit_class_code=C02; context_audit_flag_codes=F01; safety_binary=unsafe; safety_binary_code=B01; duplicate_text_status=template_pollution_candidate; duplicate_text_status_code=D03; preview_only=true

- 复核结论：待填写

### 重复组 12

- 状态：`D02` / `same_text_different_context_review` / 同文同标签但不同上下文，待复核
- 出现次数：2
- 重复文本：64号选手这把打得不错
- 风险分布：{"low": 2}
- 来源分布：{"meme_expansion": 2}
- 建议动作：看是否只是重复造句；如果上下文差异没有训练价值，建议删/重写/降权。

#### 本组怎么审

1. 先看文本本身是否足以判断。
2. 再比较标题、时间、话题等非回复链上下文是否真的不同。
3. 不要把合成的 `parent_comment/reply_chain` 当强证据。
4. 如果只是换标题/平台/泛泛场景，或靠假回复链撑风险，结论倾向 `删掉`、`退回重写` 或 `降权`。
5. 如果确实构成同文不同语境对照，结论可写 `保留对照`。

#### 涉及样本详情

#### `MEME_EXPAND_0072_LOW`

- 标签：risk_level=`low`；binary=`B01 / unsafe`；hard_negative=`true`
- 编码：primary=`C3_数字代指`；secondary=`无`
- 上下文审计：class=`C02 / contextual_required`；flags=`F01`；duplicate=`D02 / same_text_different_context_review`
- context_required：`true`
- 上下文：
  - title：美食/文具/娱乐分享
  - description：无
  - parent_comment（旧字段，默认不作强证据）：求链接
  - reply_chain（旧字段，默认不作强证据）：只讨论字面对象
  - time：2026-05-05
  - topic：日期/数字代指
- 关键 reasoning：
  - supporting_evidence：存在关键词、缩写、数字或符号撞车。
  - counter_evidence：上下文提供普通生活、教学、娱乐或技术解释。；缺少规避意图、目标映射或敏感语境。
  - final_rationale：普通解释更强，仅保留低风险或困难负样本价值，标为low。
- review_notes：source=meme_expansion; original_id=EXPAND_0072; generated_expansion; needs_human_review; original_primary=B4_符号/空格/Unicode 干扰; original_notes=generated_expansion; needs_human_review; meme_cluster=日期/数字代指; context_audit_class=contextual_required; context_audit_class_code=C02; context_audit_flag_codes=F01; safety_binary=unsafe; safety_binary_code=B01; duplicate_text_status=same_text_different_context_review; duplicate_text_status_code=D02; preview_only=true

#### `MEME_EXPAND_0086_LOW`

- 标签：risk_level=`low`；binary=`B01 / unsafe`；hard_negative=`true`
- 编码：primary=`F_组合编码`；secondary=`无`
- 上下文审计：class=`C02 / contextual_required`；flags=`none`；duplicate=`D02 / same_text_different_context_review`
- context_required：`true`
- 上下文：
  - title：教学/教程评论区
  - description：无
  - parent_comment（旧字段，默认不作强证据）：讨论的是具体技巧
  - reply_chain（旧字段，默认不作强证据）：普通解释更强
  - time：2026-03-16
  - topic：日期/数字代指
- 关键 reasoning：
  - supporting_evidence：存在关键词、缩写、数字或符号撞车。
  - counter_evidence：上下文提供普通生活、教学、娱乐或技术解释。；缺少规避意图、目标映射或敏感语境。
  - final_rationale：普通解释更强，仅保留低风险或困难负样本价值，标为low。
- review_notes：source=meme_expansion; original_id=EXPAND_0086; generated_expansion; needs_human_review; original_primary=F_组合编码; original_notes=generated_expansion; needs_human_review; meme_cluster=日期/数字代指; context_audit_class=contextual_required; context_audit_class_code=C02; context_audit_flag_codes=none; safety_binary=unsafe; safety_binary_code=B01; duplicate_text_status=same_text_different_context_review; duplicate_text_status_code=D02; preview_only=true

- 复核结论：待填写

### 重复组 13

- 状态：`D02` / `same_text_different_context_review` / 同文同标签但不同上下文，待复核
- 出现次数：2
- 重复文本：nb 这个缩写我只想说牛，别过度解读
- 风险分布：{"low": 2}
- 来源分布：{"meme_expansion": 2}
- 建议动作：看是否只是重复造句；如果上下文差异没有训练价值，建议删/重写/降权。

#### 本组怎么审

1. 先看文本本身是否足以判断。
2. 再比较标题、时间、话题等非回复链上下文是否真的不同。
3. 不要把合成的 `parent_comment/reply_chain` 当强证据。
4. 如果只是换标题/平台/泛泛场景，或靠假回复链撑风险，结论倾向 `删掉`、`退回重写` 或 `降权`。
5. 如果确实构成同文不同语境对照，结论可写 `保留对照`。

#### 涉及样本详情

#### `MEME_EXPAND_0063_LOW`

- 标签：risk_level=`low`；binary=`B01 / unsafe`；hard_negative=`true`
- 编码：primary=`C3_数字代指`；secondary=`无`
- 上下文审计：class=`C02 / contextual_required`；flags=`F01`；duplicate=`D02 / same_text_different_context_review`
- context_required：`true`
- 上下文：
  - title：美食/文具/娱乐分享
  - description：无
  - parent_comment（旧字段，默认不作强证据）：求链接
  - reply_chain（旧字段，默认不作强证据）：只讨论字面对象
  - time：2026-05-05
  - topic：平台黑话/自我审查
- 关键 reasoning：
  - supporting_evidence：存在关键词、缩写、数字或符号撞车。
  - counter_evidence：上下文提供普通生活、教学、娱乐或技术解释。；缺少规避意图、目标映射或敏感语境。
  - final_rationale：普通解释更强，仅保留低风险或困难负样本价值，标为low。
- review_notes：source=meme_expansion; original_id=EXPAND_0063; generated_expansion; needs_human_review; original_primary=C3_数字代指; original_notes=generated_expansion; needs_human_review; meme_cluster=平台黑话/自我审查; context_audit_class=contextual_required; context_audit_class_code=C02; context_audit_flag_codes=F01; safety_binary=unsafe; safety_binary_code=B01; duplicate_text_status=same_text_different_context_review; duplicate_text_status_code=D02; preview_only=true

#### `MEME_EXPAND_0077_LOW`

- 标签：risk_level=`low`；binary=`B01 / unsafe`；hard_negative=`true`
- 编码：primary=`E2_时间节点触发`；secondary=`C3_数字代指`
- 上下文审计：class=`C02 / contextual_required`；flags=`none`；duplicate=`D02 / same_text_different_context_review`
- context_required：`true`
- 上下文：
  - title：教学/教程评论区
  - description：无
  - parent_comment（旧字段，默认不作强证据）：讨论的是具体技巧
  - reply_chain（旧字段，默认不作强证据）：普通解释更强
  - time：2026-03-16
  - topic：平台黑话/自我审查
- 关键 reasoning：
  - supporting_evidence：存在关键词、缩写、数字或符号撞车。
  - counter_evidence：上下文提供普通生活、教学、娱乐或技术解释。；缺少规避意图、目标映射或敏感语境。
  - final_rationale：普通解释更强，仅保留低风险或困难负样本价值，标为low。
- review_notes：source=meme_expansion; original_id=EXPAND_0077; generated_expansion; needs_human_review; original_primary=E2_时间节点触发; original_notes=generated_expansion; needs_human_review; meme_cluster=平台黑话/自我审查; context_audit_class=contextual_required; context_audit_class_code=C02; context_audit_flag_codes=none; safety_binary=unsafe; safety_binary_code=B01; duplicate_text_status=same_text_different_context_review; duplicate_text_status_code=D02; preview_only=true

- 复核结论：待填写

### 重复组 14

- 状态：`D02` / `same_text_different_context_review` / 同文同标签但不同上下文，待复核
- 出现次数：2
- 重复文本：五月多出来的那几天，大家都学会闭麦了
- 风险分布：{"medium": 2}
- 来源分布：{"meme_expansion": 2}
- 建议动作：看是否只是重复造句；如果上下文差异没有训练价值，建议删/重写/降权。

#### 本组怎么审

1. 先看文本本身是否足以判断。
2. 再比较标题、时间、话题等非回复链上下文是否真的不同。
3. 不要把合成的 `parent_comment/reply_chain` 当强证据。
4. 如果只是换标题/平台/泛泛场景，或靠假回复链撑风险，结论倾向 `删掉`、`退回重写` 或 `降权`。
5. 如果确实构成同文不同语境对照，结论可写 `保留对照`。

#### 涉及样本详情

#### `MEME_EXPAND_0037_MEDIUM`

- 标签：risk_level=`medium`；binary=`B01 / unsafe`；hard_negative=`false`
- 编码：primary=`C3_数字代指`；secondary=`E1_平台黑话`
- 上下文审计：class=`C02 / contextual_required`；flags=`F01`；duplicate=`D02 / same_text_different_context_review`
- context_required：`true`
- 上下文：
  - title：社会趋势讨论话题
  - description：无
  - parent_comment（旧字段，默认不作强证据）：别说太满
  - reply_chain（旧字段，默认不作强证据）：像，但不敢说
  - time：2026-04-20
  - topic：日期/数字代指
- 关键 reasoning：
  - supporting_evidence：文本或上下文提供可疑编码线索。
  - counter_evidence：普通解释仍可成立，缺少直接目标或更完整上下文。
  - final_rationale：有明显复核价值，但证据不足以确定为high，标为medium。
- review_notes：source=meme_expansion; original_id=EXPAND_0037; generated_expansion; needs_human_review; original_primary=B4_符号/空格/Unicode 干扰; original_notes=generated_expansion; needs_human_review; meme_cluster=日期/数字代指; context_audit_class=contextual_required; context_audit_class_code=C02; context_audit_flag_codes=F01; safety_binary=unsafe; safety_binary_code=B01; duplicate_text_status=same_text_different_context_review; duplicate_text_status_code=D02; preview_only=true

#### `MEME_EXPAND_0051_MEDIUM`

- 标签：risk_level=`medium`；binary=`B01 / unsafe`；hard_negative=`false`
- 编码：primary=`C1_历史人物类比`；secondary=`D2_隐喻`
- 上下文审计：class=`C02 / contextual_required`；flags=`none`；duplicate=`D02 / same_text_different_context_review`
- context_required：`true`
- 上下文：
  - title：历史剧二创
  - description：无
  - parent_comment（旧字段，默认不作强证据）：别说像谁
  - reply_chain（旧字段，默认不作强证据）：像，但别展开
  - time：2026-02-28
  - topic：日期/数字代指
- 关键 reasoning：
  - supporting_evidence：文本或上下文提供可疑编码线索。
  - counter_evidence：普通解释仍可成立，缺少直接目标或更完整上下文。
  - final_rationale：有明显复核价值，但证据不足以确定为high，标为medium。
- review_notes：source=meme_expansion; original_id=EXPAND_0051; generated_expansion; needs_human_review; original_primary=C1_历史人物类比; original_notes=generated_expansion; needs_human_review; meme_cluster=日期/数字代指; context_audit_class=contextual_required; context_audit_class_code=C02; context_audit_flag_codes=none; safety_binary=unsafe; safety_binary_code=B01; duplicate_text_status=same_text_different_context_review; duplicate_text_status_code=D02; preview_only=true

- 复核结论：待填写

### 重复组 15

- 状态：`D02` / `same_text_different_context_review` / 同文同标签但不同上下文，待复核
- 出现次数：2
- 重复文本：今晚只发旧日历，不写具体日期
- 风险分布：{"high": 2}
- 来源分布：{"meme_expansion": 2}
- 建议动作：看是否只是重复造句；如果上下文差异没有训练价值，建议删/重写/降权。

#### 本组怎么审

1. 先看文本本身是否足以判断。
2. 再比较标题、时间、话题等非回复链上下文是否真的不同。
3. 不要把合成的 `parent_comment/reply_chain` 当强证据。
4. 如果只是换标题/平台/泛泛场景，或靠假回复链撑风险，结论倾向 `删掉`、`退回重写` 或 `降权`。
5. 如果确实构成同文不同语境对照，结论可写 `保留对照`。

#### 涉及样本详情

#### `MEME_EXPAND_0009_HIGH`

- 标签：risk_level=`high`；binary=`B01 / unsafe`；hard_negative=`false`
- 编码：primary=`E2_时间节点触发`；secondary=`C3_数字代指`
- 上下文审计：class=`C02 / contextual_required`；flags=`F01`；duplicate=`D02 / same_text_different_context_review`
- context_required：`true`
- 上下文：
  - title：争议视频评论区
  - description：无
  - parent_comment（旧字段，默认不作强证据）：评论怎么少了一半
  - reply_chain（旧字段，默认不作强证据）：夸就完事了
  - time：2026-05-09
  - topic：日期/数字代指
- 关键 reasoning：
  - supporting_evidence：文本含编码或规避表达。；上下文中的时间、回复链或话题提供独立支持。
  - counter_evidence：不直接还原具体目标名称；若脱离上下文，部分表达可能降级。
  - final_rationale：文本和上下文相互印证，风险解释明显强于普通解释，标为high。
- review_notes：source=meme_expansion; original_id=EXPAND_0009; generated_expansion; needs_human_review; original_primary=E2_时间节点触发; original_notes=generated_expansion; needs_human_review; meme_cluster=日期/数字代指; context_audit_class=contextual_required; context_audit_class_code=C02; context_audit_flag_codes=F01; safety_binary=unsafe; safety_binary_code=B01; duplicate_text_status=same_text_different_context_review; duplicate_text_status_code=D02; preview_only=true

#### `MEME_EXPAND_0023_HIGH`

- 标签：risk_level=`high`；binary=`B01 / unsafe`；hard_negative=`false`
- 编码：primary=`C4_典故/物品/符号借用`；secondary=`D2_隐喻`
- 上下文审计：class=`C02 / contextual_required`；flags=`F01`；duplicate=`D02 / same_text_different_context_review`
- context_required：`true`
- 上下文：
  - title：旧照片转发
  - description：无
  - parent_comment（旧字段，默认不作强证据）：这几天别发全日期
  - reply_chain（旧字段，默认不作强证据）：别补具体名
  - time：2026-06-03
  - topic：日期/数字代指
- 关键 reasoning：
  - supporting_evidence：文本含编码或规避表达。；上下文中的时间、回复链或话题提供独立支持。
  - counter_evidence：不直接还原具体目标名称；若脱离上下文，部分表达可能降级。
  - final_rationale：文本和上下文相互印证，风险解释明显强于普通解释，标为high。
- review_notes：source=meme_expansion; original_id=EXPAND_0023; generated_expansion; needs_human_review; original_primary=C4_典故/物品/符号借用; original_notes=generated_expansion; needs_human_review; meme_cluster=日期/数字代指; context_audit_class=contextual_required; context_audit_class_code=C02; context_audit_flag_codes=F01; safety_binary=unsafe; safety_binary_code=B01; duplicate_text_status=same_text_different_context_review; duplicate_text_status_code=D02; preview_only=true

- 复核结论：待填写

### 重复组 16

- 状态：`D02` / `same_text_different_context_review` / 同文同标签但不同上下文，待复核
- 出现次数：2
- 重复文本：他用某朝改革失败来类比今天，但证据只有一句话
- 风险分布：{"medium": 2}
- 来源分布：{"meme_expansion": 2}
- 建议动作：看是否只是重复造句；如果上下文差异没有训练价值，建议删/重写/降权。

#### 本组怎么审

1. 先看文本本身是否足以判断。
2. 再比较标题、时间、话题等非回复链上下文是否真的不同。
3. 不要把合成的 `parent_comment/reply_chain` 当强证据。
4. 如果只是换标题/平台/泛泛场景，或靠假回复链撑风险，结论倾向 `删掉`、`退回重写` 或 `降权`。
5. 如果确实构成同文不同语境对照，结论可写 `保留对照`。

#### 涉及样本详情

#### `MEME_EXPAND_0038_MEDIUM`

- 标签：risk_level=`medium`；binary=`B01 / unsafe`；hard_negative=`false`
- 编码：primary=`C1_历史人物类比`；secondary=`E1_平台黑话；E2_时间节点触发`
- 上下文审计：class=`C02 / contextual_required`；flags=`F01`；duplicate=`D02 / same_text_different_context_review`
- context_required：`true`
- 上下文：
  - title：热搜评论区
  - description：无
  - parent_comment（旧字段，默认不作强证据）：这波是不是又要统一口径
  - reply_chain（旧字段，默认不作强证据）：缩写就行
  - time：2026-05-19
  - topic：历史人物类比
- 关键 reasoning：
  - supporting_evidence：文本或上下文提供可疑编码线索。
  - counter_evidence：普通解释仍可成立，缺少直接目标或更完整上下文。
  - final_rationale：有明显复核价值，但证据不足以确定为high，标为medium。
- review_notes：source=meme_expansion; original_id=EXPAND_0038; generated_expansion; needs_human_review; original_primary=B4_符号/空格/Unicode 干扰; original_notes=generated_expansion; needs_human_review; meme_cluster=历史人物类比; context_audit_class=contextual_required; context_audit_class_code=C02; context_audit_flag_codes=F01; safety_binary=unsafe; safety_binary_code=B01; duplicate_text_status=same_text_different_context_review; duplicate_text_status_code=D02; preview_only=true

#### `MEME_EXPAND_0052_MEDIUM`

- 标签：risk_level=`medium`；binary=`B01 / unsafe`；hard_negative=`false`
- 编码：primary=`C1_历史人物类比`；secondary=`D2_隐喻；E3_回复链/互动触发`
- 上下文审计：class=`C02 / contextual_required`；flags=`F01`；duplicate=`D02 / same_text_different_context_review`
- context_required：`true`
- 上下文：
  - title：社会趋势讨论话题
  - description：无
  - parent_comment（旧字段，默认不作强证据）：别说太满
  - reply_chain（旧字段，默认不作强证据）：像，但不敢说
  - time：2026-04-20
  - topic：历史人物类比
- 关键 reasoning：
  - supporting_evidence：文本或上下文提供可疑编码线索。
  - counter_evidence：普通解释仍可成立，缺少直接目标或更完整上下文。
  - final_rationale：有明显复核价值，但证据不足以确定为high，标为medium。
- review_notes：source=meme_expansion; original_id=EXPAND_0052; generated_expansion; needs_human_review; original_primary=C1_历史人物类比; original_notes=generated_expansion; needs_human_review; meme_cluster=历史人物类比; context_audit_class=contextual_required; context_audit_class_code=C02; context_audit_flag_codes=F01; safety_binary=unsafe; safety_binary_code=B01; duplicate_text_status=same_text_different_context_review; duplicate_text_status_code=D02; preview_only=true

- 复核结论：待填写

### 重复组 17

- 状态：`D02` / `same_text_different_context_review` / 同文同标签但不同上下文，待复核
- 出现次数：2
- 重复文本：他这波真是英明神武，删评删到只剩彩虹屁
- 风险分布：{"high": 2}
- 来源分布：{"meme_expansion": 2}
- 建议动作：看是否只是重复造句；如果上下文差异没有训练价值，建议删/重写/降权。

#### 本组怎么审

1. 先看文本本身是否足以判断。
2. 再比较标题、时间、话题等非回复链上下文是否真的不同。
3. 不要把合成的 `parent_comment/reply_chain` 当强证据。
4. 如果只是换标题/平台/泛泛场景，或靠假回复链撑风险，结论倾向 `删掉`、`退回重写` 或 `降权`。
5. 如果确实构成同文不同语境对照，结论可写 `保留对照`。

#### 涉及样本详情

#### `MEME_EXPAND_0006_HIGH`

- 标签：risk_level=`high`；binary=`B01 / unsafe`；hard_negative=`false`
- 编码：primary=`D1_反讽`；secondary=`E1_平台黑话；B4_符号/空格/Unicode 干扰`
- 上下文审计：class=`C02 / contextual_required`；flags=`F01`；duplicate=`D02 / same_text_different_context_review`
- context_required：`true`
- 上下文：
  - title：争议视频评论区
  - description：无
  - parent_comment（旧字段，默认不作强证据）：评论怎么少了一半
  - reply_chain（旧字段，默认不作强证据）：夸就完事了
  - time：2026-05-09
  - topic：反讽/阴阳怪气
- 关键 reasoning：
  - supporting_evidence：文本含编码或规避表达。；上下文中的时间、回复链或话题提供独立支持。
  - counter_evidence：不直接还原具体目标名称；若脱离上下文，部分表达可能降级。
  - final_rationale：文本和上下文相互印证，风险解释明显强于普通解释，标为high。
- review_notes：source=meme_expansion; original_id=EXPAND_0006; generated_expansion; needs_human_review; original_primary=B3_形近字替换; original_notes=generated_expansion; needs_human_review; meme_cluster=反讽/阴阳怪气; context_audit_class=contextual_required; context_audit_class_code=C02; context_audit_flag_codes=F01; safety_binary=unsafe; safety_binary_code=B01; duplicate_text_status=same_text_different_context_review; duplicate_text_status_code=D02; preview_only=true

#### `MEME_EXPAND_0020_HIGH`

- 标签：risk_level=`high`；binary=`B01 / unsafe`；hard_negative=`false`
- 编码：primary=`C4_典故/物品/符号借用`；secondary=`D2_隐喻；E3_回复链/互动触发`
- 上下文审计：class=`C02 / contextual_required`；flags=`F01`；duplicate=`D02 / same_text_different_context_review`
- context_required：`true`
- 上下文：
  - title：旧照片转发
  - description：无
  - parent_comment（旧字段，默认不作强证据）：这几天别发全日期
  - reply_chain（旧字段，默认不作强证据）：别补具体名
  - time：2026-06-03
  - topic：反讽/阴阳怪气
- 关键 reasoning：
  - supporting_evidence：文本含编码或规避表达。；上下文中的时间、回复链或话题提供独立支持。
  - counter_evidence：不直接还原具体目标名称；若脱离上下文，部分表达可能降级。
  - final_rationale：文本和上下文相互印证，风险解释明显强于普通解释，标为high。
- review_notes：source=meme_expansion; original_id=EXPAND_0020; generated_expansion; needs_human_review; original_primary=C4_典故/物品/符号借用; original_notes=generated_expansion; needs_human_review; meme_cluster=反讽/阴阳怪气; context_audit_class=contextual_required; context_audit_class_code=C02; context_audit_flag_codes=F01; safety_binary=unsafe; safety_binary_code=B01; duplicate_text_status=same_text_different_context_review; duplicate_text_status_code=D02; preview_only=true

- 复核结论：待填写

### 重复组 18

- 状态：`D02` / `same_text_different_context_review` / 同文同标签但不同上下文，待复核
- 出现次数：2
- 重复文本：倒车入库练了一下午，教练说我终于会看镜子了
- 风险分布：{"low": 2}
- 来源分布：{"meme_expansion": 2}
- 建议动作：看是否只是重复造句；如果上下文差异没有训练价值，建议删/重写/降权。

#### 本组怎么审

1. 先看文本本身是否足以判断。
2. 再比较标题、时间、话题等非回复链上下文是否真的不同。
3. 不要把合成的 `parent_comment/reply_chain` 当强证据。
4. 如果只是换标题/平台/泛泛场景，或靠假回复链撑风险，结论倾向 `删掉`、`退回重写` 或 `降权`。
5. 如果确实构成同文不同语境对照，结论可写 `保留对照`。

#### 涉及样本详情

#### `MEME_EXPAND_0064_LOW`

- 标签：risk_level=`low`；binary=`B01 / unsafe`；hard_negative=`true`
- 编码：primary=`C1_历史人物类比`；secondary=`无`
- 上下文审计：class=`C02 / contextual_required`；flags=`none`；duplicate=`D02 / same_text_different_context_review`
- context_required：`true`
- 上下文：
  - title：日常生活分享
  - description：无
  - parent_comment（旧字段，默认不作强证据）：只是普通记录
  - reply_chain（旧字段，默认不作强证据）：别过度联想
  - time：2026-06-04
  - topic：加速/刹车/倒车
- 关键 reasoning：
  - supporting_evidence：存在关键词、缩写、数字或符号撞车。
  - counter_evidence：上下文提供普通生活、教学、娱乐或技术解释。；缺少规避意图、目标映射或敏感语境。
  - final_rationale：普通解释更强，仅保留低风险或困难负样本价值，标为low。
- review_notes：source=meme_expansion; original_id=EXPAND_0064; generated_expansion; needs_human_review; original_primary=C1_历史人物类比; original_notes=generated_expansion; needs_human_review; meme_cluster=加速/刹车/倒车; context_audit_class=contextual_required; context_audit_class_code=C02; context_audit_flag_codes=none; safety_binary=unsafe; safety_binary_code=B01; duplicate_text_status=same_text_different_context_review; duplicate_text_status_code=D02; preview_only=true

#### `MEME_EXPAND_0078_LOW`

- 标签：risk_level=`low`；binary=`B01 / unsafe`；hard_negative=`true`
- 编码：primary=`E3_回复链/互动触发`；secondary=`无`
- 上下文审计：class=`C02 / contextual_required`；flags=`F01`；duplicate=`D02 / same_text_different_context_review`
- context_required：`true`
- 上下文：
  - title：美食/文具/娱乐分享
  - description：无
  - parent_comment（旧字段，默认不作强证据）：求链接
  - reply_chain（旧字段，默认不作强证据）：只讨论字面对象
  - time：2026-05-05
  - topic：加速/刹车/倒车
- 关键 reasoning：
  - supporting_evidence：存在关键词、缩写、数字或符号撞车。
  - counter_evidence：上下文提供普通生活、教学、娱乐或技术解释。；缺少规避意图、目标映射或敏感语境。
  - final_rationale：普通解释更强，仅保留低风险或困难负样本价值，标为low。
- review_notes：source=meme_expansion; original_id=EXPAND_0078; generated_expansion; needs_human_review; original_primary=E3_回复链/互动触发; original_notes=generated_expansion; needs_human_review; meme_cluster=加速/刹车/倒车; context_audit_class=contextual_required; context_audit_class_code=C02; context_audit_flag_codes=F01; safety_binary=unsafe; safety_binary_code=B01; duplicate_text_status=same_text_different_context_review; duplicate_text_status_code=D02; preview_only=true

- 复核结论：待填写

### 重复组 19

- 状态：`D02` / `same_text_different_context_review` / 同文同标签但不同上下文，待复核
- 出现次数：2
- 重复文本：六月四号我生日，求祝福
- 风险分布：{"low": 2}
- 来源分布：{"meme_expansion": 2}
- 建议动作：看是否只是重复造句；如果上下文差异没有训练价值，建议删/重写/降权。

#### 本组怎么审

1. 先看文本本身是否足以判断。
2. 再比较标题、时间、话题等非回复链上下文是否真的不同。
3. 不要把合成的 `parent_comment/reply_chain` 当强证据。
4. 如果只是换标题/平台/泛泛场景，或靠假回复链撑风险，结论倾向 `删掉`、`退回重写` 或 `降权`。
5. 如果确实构成同文不同语境对照，结论可写 `保留对照`。

#### 涉及样本详情

#### `MEME_EXPAND_0065_LOW`

- 标签：risk_level=`low`；binary=`B01 / unsafe`；hard_negative=`true`
- 编码：primary=`C1_历史人物类比`；secondary=`D2_隐喻`
- 上下文审计：class=`C02 / contextual_required`；flags=`none`；duplicate=`D02 / same_text_different_context_review`
- context_required：`true`
- 上下文：
  - title：教学/教程评论区
  - description：无
  - parent_comment（旧字段，默认不作强证据）：讨论的是具体技巧
  - reply_chain（旧字段，默认不作强证据）：普通解释更强
  - time：2026-03-16
  - topic：日期/数字代指
- 关键 reasoning：
  - supporting_evidence：存在关键词、缩写、数字或符号撞车。
  - counter_evidence：上下文提供普通生活、教学、娱乐或技术解释。；缺少规避意图、目标映射或敏感语境。
  - final_rationale：普通解释更强，仅保留低风险或困难负样本价值，标为low。
- review_notes：source=meme_expansion; original_id=EXPAND_0065; generated_expansion; needs_human_review; original_primary=C1_历史人物类比; original_notes=generated_expansion; needs_human_review; meme_cluster=日期/数字代指; context_audit_class=contextual_required; context_audit_class_code=C02; context_audit_flag_codes=none; safety_binary=unsafe; safety_binary_code=B01; duplicate_text_status=same_text_different_context_review; duplicate_text_status_code=D02; preview_only=true

#### `MEME_EXPAND_0079_LOW`

- 标签：risk_level=`low`；binary=`B01 / unsafe`；hard_negative=`true`
- 编码：primary=`E3_回复链/互动触发`；secondary=`无`
- 上下文审计：class=`C02 / contextual_required`；flags=`none`；duplicate=`D02 / same_text_different_context_review`
- context_required：`true`
- 上下文：
  - title：日常生活分享
  - description：无
  - parent_comment（旧字段，默认不作强证据）：只是普通记录
  - reply_chain（旧字段，默认不作强证据）：别过度联想
  - time：2026-06-04
  - topic：日期/数字代指
- 关键 reasoning：
  - supporting_evidence：存在关键词、缩写、数字或符号撞车。
  - counter_evidence：上下文提供普通生活、教学、娱乐或技术解释。；缺少规避意图、目标映射或敏感语境。
  - final_rationale：普通解释更强，仅保留低风险或困难负样本价值，标为low。
- review_notes：source=meme_expansion; original_id=EXPAND_0079; generated_expansion; needs_human_review; original_primary=E3_回复链/互动触发; original_notes=generated_expansion; needs_human_review; meme_cluster=日期/数字代指; context_audit_class=contextual_required; context_audit_class_code=C02; context_audit_flag_codes=none; safety_binary=unsafe; safety_binary_code=B01; duplicate_text_status=same_text_different_context_review; duplicate_text_status_code=D02; preview_only=true

- 复核结论：待填写

### 重复组 20

- 状态：`D02` / `same_text_different_context_review` / 同文同标签但不同上下文，待复核
- 出现次数：2
- 重复文本：删前留名是抽奖梗，不是内容风险
- 风险分布：{"low": 2}
- 来源分布：{"meme_expansion": 2}
- 建议动作：看是否只是重复造句；如果上下文差异没有训练价值，建议删/重写/降权。

#### 本组怎么审

1. 先看文本本身是否足以判断。
2. 再比较标题、时间、话题等非回复链上下文是否真的不同。
3. 不要把合成的 `parent_comment/reply_chain` 当强证据。
4. 如果只是换标题/平台/泛泛场景，或靠假回复链撑风险，结论倾向 `删掉`、`退回重写` 或 `降权`。
5. 如果确实构成同文不同语境对照，结论可写 `保留对照`。

#### 涉及样本详情

#### `MEME_EXPAND_0070_LOW`

- 标签：risk_level=`low`；binary=`B01 / unsafe`；hard_negative=`true`
- 编码：primary=`C4_典故/物品/符号借用`；secondary=`无`
- 上下文审计：class=`C02 / contextual_required`；flags=`none`；duplicate=`D02 / same_text_different_context_review`
- context_required：`true`
- 上下文：
  - title：日常生活分享
  - description：无
  - parent_comment（旧字段，默认不作强证据）：只是普通记录
  - reply_chain（旧字段，默认不作强证据）：别过度联想
  - time：2026-06-04
  - topic：平台黑话/自我审查
- 关键 reasoning：
  - supporting_evidence：存在关键词、缩写、数字或符号撞车。
  - counter_evidence：上下文提供普通生活、教学、娱乐或技术解释。；缺少规避意图、目标映射或敏感语境。
  - final_rationale：普通解释更强，仅保留低风险或困难负样本价值，标为low。
- review_notes：source=meme_expansion; original_id=EXPAND_0070; generated_expansion; needs_human_review; original_primary=B1_拆字; original_notes=generated_expansion; needs_human_review; meme_cluster=平台黑话/自我审查; context_audit_class=contextual_required; context_audit_class_code=C02; context_audit_flag_codes=none; safety_binary=unsafe; safety_binary_code=B01; duplicate_text_status=same_text_different_context_review; duplicate_text_status_code=D02; preview_only=true

#### `MEME_EXPAND_0084_LOW`

- 标签：risk_level=`low`；binary=`B01 / unsafe`；hard_negative=`true`
- 编码：primary=`C2_历史事件影射`；secondary=`无`
- 上下文审计：class=`C02 / contextual_required`；flags=`F01`；duplicate=`D02 / same_text_different_context_review`
- context_required：`true`
- 上下文：
  - title：美食/文具/娱乐分享
  - description：无
  - parent_comment（旧字段，默认不作强证据）：求链接
  - reply_chain（旧字段，默认不作强证据）：只讨论字面对象
  - time：2026-05-05
  - topic：平台黑话/自我审查
- 关键 reasoning：
  - supporting_evidence：存在关键词、缩写、数字或符号撞车。
  - counter_evidence：上下文提供普通生活、教学、娱乐或技术解释。；缺少规避意图、目标映射或敏感语境。
  - final_rationale：普通解释更强，仅保留低风险或困难负样本价值，标为low。
- review_notes：source=meme_expansion; original_id=EXPAND_0084; generated_expansion; needs_human_review; original_primary=C2_历史事件影射; original_notes=generated_expansion; needs_human_review; meme_cluster=平台黑话/自我审查; context_audit_class=contextual_required; context_audit_class_code=C02; context_audit_flag_codes=F01; safety_binary=unsafe; safety_binary_code=B01; duplicate_text_status=same_text_different_context_review; duplicate_text_status_code=D02; preview_only=true

- 复核结论：待填写

### 重复组 21

- 状态：`D02` / `same_text_different_context_review` / 同文同标签但不同上下文，待复核
- 出现次数：2
- 重复文本：别再刷 j c 了，今天这条时间线已经够明显
- 风险分布：{"high": 2}
- 来源分布：{"meme_expansion": 2}
- 建议动作：看是否只是重复造句；如果上下文差异没有训练价值，建议删/重写/降权。

#### 本组怎么审

1. 先看文本本身是否足以判断。
2. 再比较标题、时间、话题等非回复链上下文是否真的不同。
3. 不要把合成的 `parent_comment/reply_chain` 当强证据。
4. 如果只是换标题/平台/泛泛场景，或靠假回复链撑风险，结论倾向 `删掉`、`退回重写` 或 `降权`。
5. 如果确实构成同文不同语境对照，结论可写 `保留对照`。

#### 涉及样本详情

#### `MEME_EXPAND_0007_HIGH`

- 标签：risk_level=`high`；binary=`B01 / unsafe`；hard_negative=`false`
- 编码：primary=`B4_符号/空格/Unicode 干扰`；secondary=`E1_平台黑话`
- 上下文审计：class=`C02 / contextual_required`；flags=`F01`；duplicate=`D02 / same_text_different_context_review`
- context_required：`true`
- 上下文：
  - title：公共事件回顾剪辑
  - description：无
  - parent_comment（旧字段，默认不作强证据）：别写全名
  - reply_chain（旧字段，默认不作强证据）：懂就别打全称
  - time：2026-06-04
  - topic：平台黑话/自我审查
- 关键 reasoning：
  - supporting_evidence：文本含编码或规避表达。；上下文中的时间、回复链或话题提供独立支持。
  - counter_evidence：不直接还原具体目标名称；若脱离上下文，部分表达可能降级。
  - final_rationale：文本和上下文相互印证，风险解释明显强于普通解释，标为high。
- review_notes：source=meme_expansion; original_id=EXPAND_0007; generated_expansion; needs_human_review; original_primary=B4_符号/空格/Unicode 干扰; original_notes=generated_expansion; needs_human_review; meme_cluster=平台黑话/自我审查; context_audit_class=contextual_required; context_audit_class_code=C02; context_audit_flag_codes=F01; safety_binary=unsafe; safety_binary_code=B01; duplicate_text_status=same_text_different_context_review; duplicate_text_status_code=D02; preview_only=true

#### `MEME_EXPAND_0021_HIGH`

- 标签：risk_level=`high`；binary=`B01 / unsafe`；hard_negative=`false`
- 编码：primary=`D1_反讽`；secondary=`E3_回复链/互动触发`
- 上下文审计：class=`C02 / contextual_required`；flags=`F01`；duplicate=`D02 / same_text_different_context_review`
- context_required：`true`
- 上下文：
  - title：争议视频评论区
  - description：无
  - parent_comment（旧字段，默认不作强证据）：评论怎么少了一半
  - reply_chain（旧字段，默认不作强证据）：夸就完事了
  - time：2026-05-09
  - topic：平台黑话/自我审查
- 关键 reasoning：
  - supporting_evidence：文本含编码或规避表达。；上下文中的时间、回复链或话题提供独立支持。
  - counter_evidence：不直接还原具体目标名称；若脱离上下文，部分表达可能降级。
  - final_rationale：文本和上下文相互印证，风险解释明显强于普通解释，标为high。
- review_notes：source=meme_expansion; original_id=EXPAND_0021; generated_expansion; needs_human_review; original_primary=D1_反讽; original_notes=generated_expansion; needs_human_review; meme_cluster=平台黑话/自我审查; context_audit_class=contextual_required; context_audit_class_code=C02; context_audit_flag_codes=F01; safety_binary=unsafe; safety_binary_code=B01; duplicate_text_status=same_text_different_context_review; duplicate_text_status_code=D02; preview_only=true

- 复核结论：待填写

### 重复组 22

- 状态：`D02` / `same_text_different_context_review` / 同文同标签但不同上下文，待复核
- 出现次数：2
- 重复文本：别发全称，写成 g·c·q 就行，这句本身有规避味
- 风险分布：{"medium": 2}
- 来源分布：{"meme_expansion": 2}
- 建议动作：看是否只是重复造句；如果上下文差异没有训练价值，建议删/重写/降权。

#### 本组怎么审

1. 先看文本本身是否足以判断。
2. 再比较标题、时间、话题等非回复链上下文是否真的不同。
3. 不要把合成的 `parent_comment/reply_chain` 当强证据。
4. 如果只是换标题/平台/泛泛场景，或靠假回复链撑风险，结论倾向 `删掉`、`退回重写` 或 `降权`。
5. 如果确实构成同文不同语境对照，结论可写 `保留对照`。

#### 涉及样本详情

#### `MEME_EXPAND_0035_MEDIUM`

- 标签：risk_level=`medium`；binary=`B01 / unsafe`；hard_negative=`false`
- 编码：primary=`B4_符号/空格/Unicode 干扰`；secondary=`E1_平台黑话`
- 上下文审计：class=`C02 / contextual_required`；flags=`F01`；duplicate=`D02 / same_text_different_context_review`
- context_required：`true`
- 上下文：
  - title：热搜评论区
  - description：无
  - parent_comment（旧字段，默认不作强证据）：这波是不是又要统一口径
  - reply_chain（旧字段，默认不作强证据）：缩写就行
  - time：2026-05-19
  - topic：平台黑话/自我审查
- 关键 reasoning：
  - supporting_evidence：文本或上下文提供可疑编码线索。
  - counter_evidence：普通解释仍可成立，缺少直接目标或更完整上下文。
  - final_rationale：有明显复核价值，但证据不足以确定为high，标为medium。
- review_notes：source=meme_expansion; original_id=EXPAND_0035; generated_expansion; needs_human_review; original_primary=B3_形近字替换; original_notes=generated_expansion; needs_human_review; meme_cluster=平台黑话/自我审查; context_audit_class=contextual_required; context_audit_class_code=C02; context_audit_flag_codes=F01; safety_binary=unsafe; safety_binary_code=B01; duplicate_text_status=same_text_different_context_review; duplicate_text_status_code=D02; preview_only=true

#### `MEME_EXPAND_0049_MEDIUM`

- 标签：risk_level=`medium`；binary=`B01 / unsafe`；hard_negative=`false`
- 编码：primary=`C4_典故/物品/符号借用`；secondary=`D2_隐喻`
- 上下文审计：class=`C02 / contextual_required`；flags=`F01`；duplicate=`D02 / same_text_different_context_review`
- context_required：`true`
- 上下文：
  - title：社会趋势讨论话题
  - description：无
  - parent_comment（旧字段，默认不作强证据）：别说太满
  - reply_chain（旧字段，默认不作强证据）：像，但不敢说
  - time：2026-04-20
  - topic：平台黑话/自我审查
- 关键 reasoning：
  - supporting_evidence：文本或上下文提供可疑编码线索。
  - counter_evidence：普通解释仍可成立，缺少直接目标或更完整上下文。
  - final_rationale：有明显复核价值，但证据不足以确定为high，标为medium。
- review_notes：source=meme_expansion; original_id=EXPAND_0049; generated_expansion; needs_human_review; original_primary=C4_典故/物品/符号借用; original_notes=generated_expansion; needs_human_review; meme_cluster=平台黑话/自我审查; context_audit_class=contextual_required; context_audit_class_code=C02; context_audit_flag_codes=F01; safety_binary=unsafe; safety_binary_code=B01; duplicate_text_status=same_text_different_context_review; duplicate_text_status_code=D02; preview_only=true

- 复核结论：待填写

### 重复组 23

- 状态：`D02` / `same_text_different_context_review` / 同文同标签但不同上下文，待复核
- 出现次数：2
- 重复文本：前面说那年夏天的别回了，楼已经被清过一轮
- 风险分布：{"high": 2}
- 来源分布：{"meme_expansion": 2}
- 建议动作：看是否只是重复造句；如果上下文差异没有训练价值，建议删/重写/降权。

#### 本组怎么审

1. 先看文本本身是否足以判断。
2. 再比较标题、时间、话题等非回复链上下文是否真的不同。
3. 不要把合成的 `parent_comment/reply_chain` 当强证据。
4. 如果只是换标题/平台/泛泛场景，或靠假回复链撑风险，结论倾向 `删掉`、`退回重写` 或 `降权`。
5. 如果确实构成同文不同语境对照，结论可写 `保留对照`。

#### 涉及样本详情

#### `MEME_EXPAND_0011_HIGH`

- 标签：risk_level=`high`；binary=`B01 / unsafe`；hard_negative=`false`
- 编码：primary=`E3_回复链/互动触发`；secondary=`E1_平台黑话`
- 上下文审计：class=`C02 / contextual_required`；flags=`F01`；duplicate=`D02 / same_text_different_context_review`
- context_required：`true`
- 上下文：
  - title：旧照片转发
  - description：无
  - parent_comment（旧字段，默认不作强证据）：这几天别发全日期
  - reply_chain（旧字段，默认不作强证据）：别补具体名
  - time：2026-06-03
  - topic：历史事件影射
- 关键 reasoning：
  - supporting_evidence：文本含编码或规避表达。；上下文中的时间、回复链或话题提供独立支持。
  - counter_evidence：不直接还原具体目标名称；若脱离上下文，部分表达可能降级。
  - final_rationale：文本和上下文相互印证，风险解释明显强于普通解释，标为high。
- review_notes：source=meme_expansion; original_id=EXPAND_0011; generated_expansion; needs_human_review; original_primary=E3_回复链/互动触发; original_notes=generated_expansion; needs_human_review; meme_cluster=历史事件影射; context_audit_class=contextual_required; context_audit_class_code=C02; context_audit_flag_codes=F01; safety_binary=unsafe; safety_binary_code=B01; duplicate_text_status=same_text_different_context_review; duplicate_text_status_code=D02; preview_only=true

#### `MEME_EXPAND_0025_HIGH`

- 标签：risk_level=`high`；binary=`B01 / unsafe`；hard_negative=`false`
- 编码：primary=`E2_时间节点触发`；secondary=`C3_数字代指`
- 上下文审计：class=`C02 / contextual_required`；flags=`F01`；duplicate=`D02 / same_text_different_context_review`
- context_required：`true`
- 上下文：
  - title：公共事件回顾剪辑
  - description：无
  - parent_comment（旧字段，默认不作强证据）：别写全名
  - reply_chain（旧字段，默认不作强证据）：懂就别打全称
  - time：2026-06-04
  - topic：历史事件影射
- 关键 reasoning：
  - supporting_evidence：文本含编码或规避表达。；上下文中的时间、回复链或话题提供独立支持。
  - counter_evidence：不直接还原具体目标名称；若脱离上下文，部分表达可能降级。
  - final_rationale：文本和上下文相互印证，风险解释明显强于普通解释，标为high。
- review_notes：source=meme_expansion; original_id=EXPAND_0025; generated_expansion; needs_human_review; original_primary=E2_时间节点触发; original_notes=generated_expansion; needs_human_review; meme_cluster=历史事件影射; context_audit_class=contextual_required; context_audit_class_code=C02; context_audit_flag_codes=F01; safety_binary=unsafe; safety_binary_code=B01; duplicate_text_status=same_text_different_context_review; duplicate_text_status_code=D02; preview_only=true

- 复核结论：待填写

### 重复组 24

- 状态：`D02` / `same_text_different_context_review` / 同文同标签但不同上下文，待复核
- 出现次数：2
- 重复文本：包子、茶杯和旧照片一起发，单看都正常
- 风险分布：{"medium": 2}
- 来源分布：{"meme_expansion": 2}
- 建议动作：看是否只是重复造句；如果上下文差异没有训练价值，建议删/重写/降权。

#### 本组怎么审

1. 先看文本本身是否足以判断。
2. 再比较标题、时间、话题等非回复链上下文是否真的不同。
3. 不要把合成的 `parent_comment/reply_chain` 当强证据。
4. 如果只是换标题/平台/泛泛场景，或靠假回复链撑风险，结论倾向 `删掉`、`退回重写` 或 `降权`。
5. 如果确实构成同文不同语境对照，结论可写 `保留对照`。

#### 涉及样本详情

#### `MEME_EXPAND_0033_MEDIUM`

- 标签：risk_level=`medium`；binary=`B01 / unsafe`；hard_negative=`false`
- 编码：primary=`C4_典故/物品/符号借用`；secondary=`E1_平台黑话`
- 上下文审计：class=`C02 / contextual_required`；flags=`none`；duplicate=`D02 / same_text_different_context_review`
- context_required：`true`
- 上下文：
  - title：历史剧二创
  - description：无
  - parent_comment（旧字段，默认不作强证据）：别说像谁
  - reply_chain（旧字段，默认不作强证据）：像，但别展开
  - time：2026-02-28
  - topic：食物/品牌/物品隐喻
- 关键 reasoning：
  - supporting_evidence：文本或上下文提供可疑编码线索。
  - counter_evidence：普通解释仍可成立，缺少直接目标或更完整上下文。
  - final_rationale：有明显复核价值，但证据不足以确定为high，标为medium。
- review_notes：source=meme_expansion; original_id=EXPAND_0033; generated_expansion; needs_human_review; original_primary=B3_形近字替换; original_notes=generated_expansion; needs_human_review; meme_cluster=食物/品牌/物品隐喻; context_audit_class=contextual_required; context_audit_class_code=C02; context_audit_flag_codes=none; safety_binary=unsafe; safety_binary_code=B01; duplicate_text_status=same_text_different_context_review; duplicate_text_status_code=D02; preview_only=true

#### `MEME_EXPAND_0047_MEDIUM`

- 标签：risk_level=`medium`；binary=`B01 / unsafe`；hard_negative=`false`
- 编码：primary=`C3_数字代指`；secondary=`E2_时间节点触发`
- 上下文审计：class=`C02 / contextual_required`；flags=`F01`；duplicate=`D02 / same_text_different_context_review`
- context_required：`true`
- 上下文：
  - title：热搜评论区
  - description：无
  - parent_comment（旧字段，默认不作强证据）：这波是不是又要统一口径
  - reply_chain（旧字段，默认不作强证据）：缩写就行
  - time：2026-05-19
  - topic：食物/品牌/物品隐喻
- 关键 reasoning：
  - supporting_evidence：文本或上下文提供可疑编码线索。
  - counter_evidence：普通解释仍可成立，缺少直接目标或更完整上下文。
  - final_rationale：有明显复核价值，但证据不足以确定为high，标为medium。
- review_notes：source=meme_expansion; original_id=EXPAND_0047; generated_expansion; needs_human_review; original_primary=C3_数字代指; original_notes=generated_expansion; needs_human_review; meme_cluster=食物/品牌/物品隐喻; context_audit_class=contextual_required; context_audit_class_code=C02; context_audit_flag_codes=F01; safety_binary=unsafe; safety_binary_code=B01; duplicate_text_status=same_text_different_context_review; duplicate_text_status_code=D02; preview_only=true

- 复核结论：待填写

### 重复组 25

- 状态：`D02` / `same_text_different_context_review` / 同文同标签但不同上下文，待复核
- 出现次数：2
- 重复文本：包子铺突然限评，大家却都在问馅儿是不是换了
- 风险分布：{"high": 2}
- 来源分布：{"meme_expansion": 2}
- 建议动作：看是否只是重复造句；如果上下文差异没有训练价值，建议删/重写/降权。

#### 本组怎么审

1. 先看文本本身是否足以判断。
2. 再比较标题、时间、话题等非回复链上下文是否真的不同。
3. 不要把合成的 `parent_comment/reply_chain` 当强证据。
4. 如果只是换标题/平台/泛泛场景，或靠假回复链撑风险，结论倾向 `删掉`、`退回重写` 或 `降权`。
5. 如果确实构成同文不同语境对照，结论可写 `保留对照`。

#### 涉及样本详情

#### `MEME_EXPAND_0005_HIGH`

- 标签：risk_level=`high`；binary=`B01 / unsafe`；hard_negative=`false`
- 编码：primary=`C4_典故/物品/符号借用`；secondary=`E1_平台黑话`
- 上下文审计：class=`C02 / contextual_required`；flags=`F01`；duplicate=`D02 / same_text_different_context_review`
- context_required：`true`
- 上下文：
  - title：旧照片转发
  - description：无
  - parent_comment（旧字段，默认不作强证据）：这几天别发全日期
  - reply_chain（旧字段，默认不作强证据）：别补具体名
  - time：2026-06-03
  - topic：食物/品牌/物品隐喻
- 关键 reasoning：
  - supporting_evidence：文本含编码或规避表达。；上下文中的时间、回复链或话题提供独立支持。
  - counter_evidence：不直接还原具体目标名称；若脱离上下文，部分表达可能降级。
  - final_rationale：文本和上下文相互印证，风险解释明显强于普通解释，标为high。
- review_notes：source=meme_expansion; original_id=EXPAND_0005; generated_expansion; needs_human_review; original_primary=B3_形近字替换; original_notes=generated_expansion; needs_human_review; meme_cluster=食物/品牌/物品隐喻; context_audit_class=contextual_required; context_audit_class_code=C02; context_audit_flag_codes=F01; safety_binary=unsafe; safety_binary_code=B01; duplicate_text_status=same_text_different_context_review; duplicate_text_status_code=D02; preview_only=true

#### `MEME_EXPAND_0019_HIGH`

- 标签：risk_level=`high`；binary=`B01 / unsafe`；hard_negative=`false`
- 编码：primary=`C2_历史事件影射`；secondary=`D1_反讽`
- 上下文审计：class=`C02 / contextual_required`；flags=`F01`；duplicate=`D02 / same_text_different_context_review`
- context_required：`true`
- 上下文：
  - title：公共事件回顾剪辑
  - description：无
  - parent_comment（旧字段，默认不作强证据）：别写全名
  - reply_chain（旧字段，默认不作强证据）：懂就别打全称
  - time：2026-06-04
  - topic：食物/品牌/物品隐喻
- 关键 reasoning：
  - supporting_evidence：文本含编码或规避表达。；上下文中的时间、回复链或话题提供独立支持。
  - counter_evidence：不直接还原具体目标名称；若脱离上下文，部分表达可能降级。
  - final_rationale：文本和上下文相互印证，风险解释明显强于普通解释，标为high。
- review_notes：source=meme_expansion; original_id=EXPAND_0019; generated_expansion; needs_human_review; original_primary=C2_历史事件影射; original_notes=generated_expansion; needs_human_review; meme_cluster=食物/品牌/物品隐喻; context_audit_class=contextual_required; context_audit_class_code=C02; context_audit_flag_codes=F01; safety_binary=unsafe; safety_binary_code=B01; duplicate_text_status=same_text_different_context_review; duplicate_text_status_code=D02; preview_only=true

- 复核结论：待填写

### 重复组 26

- 状态：`D02` / `same_text_different_context_review` / 同文同标签但不同上下文，待复核
- 出现次数：2
- 重复文本：历史书翻到这一页，弹幕都在说熟悉的配方
- 风险分布：{"high": 2}
- 来源分布：{"meme_expansion": 2}
- 建议动作：看是否只是重复造句；如果上下文差异没有训练价值，建议删/重写/降权。

#### 本组怎么审

1. 先看文本本身是否足以判断。
2. 再比较标题、时间、话题等非回复链上下文是否真的不同。
3. 不要把合成的 `parent_comment/reply_chain` 当强证据。
4. 如果只是换标题/平台/泛泛场景，或靠假回复链撑风险，结论倾向 `删掉`、`退回重写` 或 `降权`。
5. 如果确实构成同文不同语境对照，结论可写 `保留对照`。

#### 涉及样本详情

#### `MEME_EXPAND_0004_HIGH`

- 标签：risk_level=`high`；binary=`B01 / unsafe`；hard_negative=`false`
- 编码：primary=`C2_历史事件影射`；secondary=`E3_回复链/互动触发；C1_历史人物类比`
- 上下文审计：class=`C02 / contextual_required`；flags=`F01`；duplicate=`D02 / same_text_different_context_review`
- context_required：`true`
- 上下文：
  - title：公共事件回顾剪辑
  - description：无
  - parent_comment（旧字段，默认不作强证据）：别写全名
  - reply_chain（旧字段，默认不作强证据）：懂就别打全称
  - time：2026-06-04
  - topic：历史事件影射
- 关键 reasoning：
  - supporting_evidence：文本含编码或规避表达。；上下文中的时间、回复链或话题提供独立支持。
  - counter_evidence：不直接还原具体目标名称；若脱离上下文，部分表达可能降级。
  - final_rationale：文本和上下文相互印证，风险解释明显强于普通解释，标为high。
- review_notes：source=meme_expansion; original_id=EXPAND_0004; generated_expansion; needs_human_review; original_primary=B1_拆字; original_notes=generated_expansion; needs_human_review; meme_cluster=历史事件影射; context_audit_class=contextual_required; context_audit_class_code=C02; context_audit_flag_codes=F01; safety_binary=unsafe; safety_binary_code=B01; duplicate_text_status=same_text_different_context_review; duplicate_text_status_code=D02; preview_only=true

#### `MEME_EXPAND_0018_HIGH`

- 标签：risk_level=`high`；binary=`B01 / unsafe`；hard_negative=`false`
- 编码：primary=`C1_历史人物类比`；secondary=`D2_隐喻；E3_回复链/互动触发`
- 上下文审计：class=`C02 / contextual_required`；flags=`F01`；duplicate=`D02 / same_text_different_context_review`
- context_required：`true`
- 上下文：
  - title：争议视频评论区
  - description：无
  - parent_comment（旧字段，默认不作强证据）：评论怎么少了一半
  - reply_chain（旧字段，默认不作强证据）：夸就完事了
  - time：2026-05-09
  - topic：历史事件影射
- 关键 reasoning：
  - supporting_evidence：文本含编码或规避表达。；上下文中的时间、回复链或话题提供独立支持。
  - counter_evidence：不直接还原具体目标名称；若脱离上下文，部分表达可能降级。
  - final_rationale：文本和上下文相互印证，风险解释明显强于普通解释，标为high。
- review_notes：source=meme_expansion; original_id=EXPAND_0018; generated_expansion; needs_human_review; original_primary=C1_历史人物类比; original_notes=generated_expansion; needs_human_review; meme_cluster=历史事件影射; context_audit_class=contextual_required; context_audit_class_code=C02; context_audit_flag_codes=F01; safety_binary=unsafe; safety_binary_code=B01; duplicate_text_status=same_text_different_context_review; duplicate_text_status_code=D02; preview_only=true

- 复核结论：待填写

### 重复组 27

- 状态：`D02` / `same_text_different_context_review` / 同文同标签但不同上下文，待复核
- 出现次数：2
- 重复文本：历史总是相似，这句是影评里的主题概括
- 风险分布：{"low": 2}
- 来源分布：{"meme_expansion": 2}
- 建议动作：看是否只是重复造句；如果上下文差异没有训练价值，建议删/重写/降权。

#### 本组怎么审

1. 先看文本本身是否足以判断。
2. 再比较标题、时间、话题等非回复链上下文是否真的不同。
3. 不要把合成的 `parent_comment/reply_chain` 当强证据。
4. 如果只是换标题/平台/泛泛场景，或靠假回复链撑风险，结论倾向 `删掉`、`退回重写` 或 `降权`。
5. 如果确实构成同文不同语境对照，结论可写 `保留对照`。

#### 涉及样本详情

#### `MEME_EXPAND_0074_LOW`

- 标签：risk_level=`low`；binary=`B01 / unsafe`；hard_negative=`true`
- 编码：primary=`C2_历史事件影射`；secondary=`无`
- 上下文审计：class=`C02 / contextual_required`；flags=`none`；duplicate=`D02 / same_text_different_context_review`
- context_required：`true`
- 上下文：
  - title：教学/教程评论区
  - description：无
  - parent_comment（旧字段，默认不作强证据）：讨论的是具体技巧
  - reply_chain（旧字段，默认不作强证据）：普通解释更强
  - time：2026-03-16
  - topic：历史事件影射
- 关键 reasoning：
  - supporting_evidence：存在关键词、缩写、数字或符号撞车。
  - counter_evidence：上下文提供普通生活、教学、娱乐或技术解释。；缺少规避意图、目标映射或敏感语境。
  - final_rationale：普通解释更强，仅保留低风险或困难负样本价值，标为low。
- review_notes：source=meme_expansion; original_id=EXPAND_0074; generated_expansion; needs_human_review; original_primary=B3_形近字替换; original_notes=generated_expansion; needs_human_review; meme_cluster=历史事件影射; context_audit_class=contextual_required; context_audit_class_code=C02; context_audit_flag_codes=none; safety_binary=unsafe; safety_binary_code=B01; duplicate_text_status=same_text_different_context_review; duplicate_text_status_code=D02; preview_only=true

#### `MEME_EXPAND_0088_LOW`

- 标签：risk_level=`low`；binary=`B01 / unsafe`；hard_negative=`true`
- 编码：primary=`E3_回复链/互动触发`；secondary=`无`
- 上下文审计：class=`C02 / contextual_required`；flags=`none`；duplicate=`D02 / same_text_different_context_review`
- context_required：`true`
- 上下文：
  - title：日常生活分享
  - description：无
  - parent_comment（旧字段，默认不作强证据）：只是普通记录
  - reply_chain（旧字段，默认不作强证据）：别过度联想
  - time：2026-06-04
  - topic：历史事件影射
- 关键 reasoning：
  - supporting_evidence：存在关键词、缩写、数字或符号撞车。
  - counter_evidence：上下文提供普通生活、教学、娱乐或技术解释。；缺少规避意图、目标映射或敏感语境。
  - final_rationale：普通解释更强，仅保留低风险或困难负样本价值，标为low。
- review_notes：source=meme_expansion; original_id=EXPAND_0088; generated_expansion; needs_human_review; original_primary=E3_回复链/互动触发; original_notes=generated_expansion; needs_human_review; meme_cluster=历史事件影射; context_audit_class=contextual_required; context_audit_class_code=C02; context_audit_flag_codes=none; safety_binary=unsafe; safety_binary_code=B01; duplicate_text_status=same_text_different_context_review; duplicate_text_status_code=D02; preview_only=true

- 复核结论：待填写

### 重复组 28

- 状态：`D02` / `same_text_different_context_review` / 同文同标签但不同上下文，待复核
- 出现次数：2
- 重复文本：历史重演是小说主题，不是在指现实事件
- 风险分布：{"none": 2}
- 来源分布：{"meme_expansion": 2}
- 建议动作：看是否只是重复造句；如果上下文差异没有训练价值，建议删/重写/降权。

#### 本组怎么审

1. 先看文本本身是否足以判断。
2. 再比较标题、时间、话题等非回复链上下文是否真的不同。
3. 不要把合成的 `parent_comment/reply_chain` 当强证据。
4. 如果只是换标题/平台/泛泛场景，或靠假回复链撑风险，结论倾向 `删掉`、`退回重写` 或 `降权`。
5. 如果确实构成同文不同语境对照，结论可写 `保留对照`。

#### 涉及样本详情

#### `MEME_EXPAND_0095_NONE`

- 标签：risk_level=`none`；binary=`B02 / safe`；hard_negative=`true`
- 编码：primary=`none`；secondary=`无`
- 上下文审计：class=`C03 / safe_without_context`；flags=`F01+F04`；duplicate=`D02 / same_text_different_context_review`
- context_required：`true`
- 上下文：
  - title：课程/教程内容
  - description：无
  - parent_comment（旧字段，默认不作强证据）：讨论学习或技术问题
  - reply_chain（旧字段，默认不作强证据）：上下文支持普通解释
  - time：2026-03-06
  - topic：历史事件影射
- 关键 reasoning：
  - supporting_evidence：无
  - counter_evidence：上下文明确指向普通生活、学习、商品、娱乐或技术场景。；没有规避检测意图、隐含目标或异常互动共识。；相关词语可由字面含义充分解释。
  - final_rationale：反证充分，风险解释不成立，标为none。
- review_notes：source=meme_expansion; original_id=EXPAND_0095; generated_expansion; needs_human_review; original_primary=B1_拆字; original_notes=generated_expansion; needs_human_review; meme_cluster=历史事件影射; context_audit_class=safe_without_context; context_audit_class_code=C03; context_audit_flag_codes=F01+F04; safety_binary=safe; safety_binary_code=B02; duplicate_text_status=same_text_different_context_review; duplicate_text_status_code=D02; preview_only=true

#### `MEME_EXPAND_0109_NONE`

- 标签：risk_level=`none`；binary=`B02 / safe`；hard_negative=`true`
- 编码：primary=`none`；secondary=`无`
- 上下文审计：class=`C03 / safe_without_context`；flags=`F01+F04`；duplicate=`D02 / same_text_different_context_review`
- context_required：`true`
- 上下文：
  - title：普通生活帖
  - description：无
  - parent_comment（旧字段，默认不作强证据）：字面场景明确
  - reply_chain（旧字段，默认不作强证据）：无异常互动
  - time：2026-06-04
  - topic：历史事件影射
- 关键 reasoning：
  - supporting_evidence：无
  - counter_evidence：上下文明确指向普通生活、学习、商品、娱乐或技术场景。；没有规避检测意图、隐含目标或异常互动共识。；相关词语可由字面含义充分解释。
  - final_rationale：反证充分，风险解释不成立，标为none。
- review_notes：source=meme_expansion; original_id=EXPAND_0109; generated_expansion; needs_human_review; original_primary=C4_典故/物品/符号借用; original_notes=generated_expansion; needs_human_review; meme_cluster=历史事件影射; context_audit_class=safe_without_context; context_audit_class_code=C03; context_audit_flag_codes=F01+F04; safety_binary=safe; safety_binary_code=B02; duplicate_text_status=same_text_different_context_review; duplicate_text_status_code=D02; preview_only=true

- 复核结论：待填写

### 重复组 29

- 状态：`D02` / `same_text_different_context_review` / 同文同标签但不同上下文，待复核
- 出现次数：2
- 重复文本：又到那个 5·35 的晚上，评论区自动静音
- 风险分布：{"high": 2}
- 来源分布：{"meme_expansion": 2}
- 建议动作：看是否只是重复造句；如果上下文差异没有训练价值，建议删/重写/降权。

#### 本组怎么审

1. 先看文本本身是否足以判断。
2. 再比较标题、时间、话题等非回复链上下文是否真的不同。
3. 不要把合成的 `parent_comment/reply_chain` 当强证据。
4. 如果只是换标题/平台/泛泛场景，或靠假回复链撑风险，结论倾向 `删掉`、`退回重写` 或 `降权`。
5. 如果确实构成同文不同语境对照，结论可写 `保留对照`。

#### 涉及样本详情

#### `MEME_EXPAND_0002_HIGH`

- 标签：risk_level=`high`；binary=`B01 / unsafe`；hard_negative=`false`
- 编码：primary=`B4_符号/空格/Unicode 干扰`；secondary=`E1_平台黑话；E3_回复链/互动触发`
- 上下文审计：class=`C02 / contextual_required`；flags=`F01`；duplicate=`D02 / same_text_different_context_review`
- context_required：`true`
- 上下文：
  - title：旧照片转发
  - description：无
  - parent_comment（旧字段，默认不作强证据）：这几天别发全日期
  - reply_chain（旧字段，默认不作强证据）：别补具体名
  - time：2026-06-03
  - topic：日期/数字代指
- 关键 reasoning：
  - supporting_evidence：文本含编码或规避表达。；上下文中的时间、回复链或话题提供独立支持。
  - counter_evidence：不直接还原具体目标名称；若脱离上下文，部分表达可能降级。
  - final_rationale：文本和上下文相互印证，风险解释明显强于普通解释，标为high。
- review_notes：source=meme_expansion; original_id=EXPAND_0002; generated_expansion; needs_human_review; original_primary=A2_拼音/首字母缩写; original_notes=generated_expansion; needs_human_review; meme_cluster=日期/数字代指; context_audit_class=contextual_required; context_audit_class_code=C02; context_audit_flag_codes=F01; safety_binary=unsafe; safety_binary_code=B01; duplicate_text_status=same_text_different_context_review; duplicate_text_status_code=D02; preview_only=true

#### `MEME_EXPAND_0016_HIGH`

- 标签：risk_level=`high`；binary=`B01 / unsafe`；hard_negative=`false`
- 编码：primary=`C3_数字代指`；secondary=`E2_时间节点触发`
- 上下文审计：class=`C02 / contextual_required`；flags=`F01`；duplicate=`D02 / same_text_different_context_review`
- context_required：`true`
- 上下文：
  - title：公共事件回顾剪辑
  - description：无
  - parent_comment（旧字段，默认不作强证据）：别写全名
  - reply_chain（旧字段，默认不作强证据）：懂就别打全称
  - time：2026-06-04
  - topic：日期/数字代指
- 关键 reasoning：
  - supporting_evidence：文本含编码或规避表达。；上下文中的时间、回复链或话题提供独立支持。
  - counter_evidence：不直接还原具体目标名称；若脱离上下文，部分表达可能降级。
  - final_rationale：文本和上下文相互印证，风险解释明显强于普通解释，标为high。
- review_notes：source=meme_expansion; original_id=EXPAND_0016; generated_expansion; needs_human_review; original_primary=C3_数字代指; original_notes=generated_expansion; needs_human_review; meme_cluster=日期/数字代指; context_audit_class=contextual_required; context_audit_class_code=C02; context_audit_flag_codes=F01; safety_binary=unsafe; safety_binary_code=B01; duplicate_text_status=same_text_different_context_review; duplicate_text_status_code=D02; preview_only=true

- 复核结论：待填写

### 重复组 30

- 状态：`D02` / `same_text_different_context_review` / 同文同标签但不同上下文，待复核
- 出现次数：2
- 重复文本：崇祯时期财政问题很复杂，不能只怪一个人
- 风险分布：{"low": 2}
- 来源分布：{"meme_expansion": 2}
- 建议动作：看是否只是重复造句；如果上下文差异没有训练价值，建议删/重写/降权。

#### 本组怎么审

1. 先看文本本身是否足以判断。
2. 再比较标题、时间、话题等非回复链上下文是否真的不同。
3. 不要把合成的 `parent_comment/reply_chain` 当强证据。
4. 如果只是换标题/平台/泛泛场景，或靠假回复链撑风险，结论倾向 `删掉`、`退回重写` 或 `降权`。
5. 如果确实构成同文不同语境对照，结论可写 `保留对照`。

#### 涉及样本详情

#### `MEME_EXPAND_0073_LOW`

- 标签：risk_level=`low`；binary=`B01 / unsafe`；hard_negative=`true`
- 编码：primary=`C1_历史人物类比`；secondary=`E1_平台黑话`
- 上下文审计：class=`C02 / contextual_required`；flags=`none`；duplicate=`D02 / same_text_different_context_review`
- context_required：`true`
- 上下文：
  - title：日常生活分享
  - description：无
  - parent_comment（旧字段，默认不作强证据）：只是普通记录
  - reply_chain（旧字段，默认不作强证据）：别过度联想
  - time：2026-06-04
  - topic：历史人物类比
- 关键 reasoning：
  - supporting_evidence：存在关键词、缩写、数字或符号撞车。
  - counter_evidence：上下文提供普通生活、教学、娱乐或技术解释。；缺少规避意图、目标映射或敏感语境。
  - final_rationale：普通解释更强，仅保留低风险或困难负样本价值，标为low。
- review_notes：source=meme_expansion; original_id=EXPAND_0073; generated_expansion; needs_human_review; original_primary=B4_符号/空格/Unicode 干扰; original_notes=generated_expansion; needs_human_review; meme_cluster=历史人物类比; context_audit_class=contextual_required; context_audit_class_code=C02; context_audit_flag_codes=none; safety_binary=unsafe; safety_binary_code=B01; duplicate_text_status=same_text_different_context_review; duplicate_text_status_code=D02; preview_only=true

#### `MEME_EXPAND_0087_LOW`

- 标签：risk_level=`low`；binary=`B01 / unsafe`；hard_negative=`true`
- 编码：primary=`F_组合编码`；secondary=`无`
- 上下文审计：class=`C02 / contextual_required`；flags=`F01`；duplicate=`D02 / same_text_different_context_review`
- context_required：`true`
- 上下文：
  - title：美食/文具/娱乐分享
  - description：无
  - parent_comment（旧字段，默认不作强证据）：求链接
  - reply_chain（旧字段，默认不作强证据）：只讨论字面对象
  - time：2026-05-05
  - topic：历史人物类比
- 关键 reasoning：
  - supporting_evidence：存在关键词、缩写、数字或符号撞车。
  - counter_evidence：上下文提供普通生活、教学、娱乐或技术解释。；缺少规避意图、目标映射或敏感语境。
  - final_rationale：普通解释更强，仅保留低风险或困难负样本价值，标为low。
- review_notes：source=meme_expansion; original_id=EXPAND_0087; generated_expansion; needs_human_review; original_primary=F_组合编码; original_notes=generated_expansion; needs_human_review; meme_cluster=历史人物类比; context_audit_class=contextual_required; context_audit_class_code=C02; context_audit_flag_codes=F01; safety_binary=unsafe; safety_binary_code=B01; duplicate_text_status=same_text_different_context_review; duplicate_text_status_code=D02; preview_only=true

- 复核结论：待填写

### 重复组 31

- 状态：`D02` / `same_text_different_context_review` / 同文同标签但不同上下文，待复核
- 出现次数：2
- 重复文本：庆丰包子的素馅我觉得一般
- 风险分布：{"none": 2}
- 来源分布：{"meme_expansion": 2}
- 建议动作：看是否只是重复造句；如果上下文差异没有训练价值，建议删/重写/降权。

#### 本组怎么审

1. 先看文本本身是否足以判断。
2. 再比较标题、时间、话题等非回复链上下文是否真的不同。
3. 不要把合成的 `parent_comment/reply_chain` 当强证据。
4. 如果只是换标题/平台/泛泛场景，或靠假回复链撑风险，结论倾向 `删掉`、`退回重写` 或 `降权`。
5. 如果确实构成同文不同语境对照，结论可写 `保留对照`。

#### 涉及样本详情

#### `MEME_EXPAND_0103_NONE`

- 标签：risk_level=`none`；binary=`B02 / safe`；hard_negative=`true`
- 编码：primary=`none`；secondary=`无`
- 上下文审计：class=`C03 / safe_without_context`；flags=`F01+F04`；duplicate=`D02 / same_text_different_context_review`
- context_required：`true`
- 上下文：
  - title：普通生活帖
  - description：无
  - parent_comment（旧字段，默认不作强证据）：字面场景明确
  - reply_chain（旧字段，默认不作强证据）：无异常互动
  - time：2026-06-04
  - topic：食物/品牌/物品隐喻
- 关键 reasoning：
  - supporting_evidence：无
  - counter_evidence：上下文明确指向普通生活、学习、商品、娱乐或技术场景。；没有规避检测意图、隐含目标或异常互动共识。；相关词语可由字面含义充分解释。
  - final_rationale：反证充分，风险解释不成立，标为none。
- review_notes：source=meme_expansion; original_id=EXPAND_0103; generated_expansion; needs_human_review; original_primary=B4_符号/空格/Unicode 干扰; original_notes=generated_expansion; needs_human_review; meme_cluster=食物/品牌/物品隐喻; context_audit_class=safe_without_context; context_audit_class_code=C03; context_audit_flag_codes=F01+F04; safety_binary=safe; safety_binary_code=B02; duplicate_text_status=same_text_different_context_review; duplicate_text_status_code=D02; preview_only=true

#### `MEME_EXPAND_0117_NONE`

- 标签：risk_level=`none`；binary=`B02 / safe`；hard_negative=`true`
- 编码：primary=`none`；secondary=`无`
- 上下文审计：class=`C03 / safe_without_context`；flags=`F01+F04`；duplicate=`D02 / same_text_different_context_review`
- context_required：`true`
- 上下文：
  - title：商品/美食测评
  - description：无
  - parent_comment（旧字段，默认不作强证据）：只讨论购买和使用体验
  - reply_chain（旧字段，默认不作强证据）：没有隐含目标
  - time：2026-05-05
  - topic：食物/品牌/物品隐喻
- 关键 reasoning：
  - supporting_evidence：无
  - counter_evidence：上下文明确指向普通生活、学习、商品、娱乐或技术场景。；没有规避检测意图、隐含目标或异常互动共识。；相关词语可由字面含义充分解释。
  - final_rationale：反证充分，风险解释不成立，标为none。
- review_notes：source=meme_expansion; original_id=EXPAND_0117; generated_expansion; needs_human_review; original_primary=B4_符号/空格/Unicode 干扰; original_notes=generated_expansion; needs_human_review; meme_cluster=食物/品牌/物品隐喻; context_audit_class=safe_without_context; context_audit_class_code=C03; context_audit_flag_codes=F01+F04; safety_binary=safe; safety_binary_code=B02; duplicate_text_status=same_text_different_context_review; duplicate_text_status_code=D02; preview_only=true

- 复核结论：待填写

### 重复组 32

- 状态：`D02` / `same_text_different_context_review` / 同文同标签但不同上下文，待复核
- 出现次数：2
- 重复文本：感谢安排是婚礼流程顺利后的真诚感谢
- 风险分布：{"none": 2}
- 来源分布：{"meme_expansion": 2}
- 建议动作：看是否只是重复造句；如果上下文差异没有训练价值，建议删/重写/降权。

#### 本组怎么审

1. 先看文本本身是否足以判断。
2. 再比较标题、时间、话题等非回复链上下文是否真的不同。
3. 不要把合成的 `parent_comment/reply_chain` 当强证据。
4. 如果只是换标题/平台/泛泛场景，或靠假回复链撑风险，结论倾向 `删掉`、`退回重写` 或 `降权`。
5. 如果确实构成同文不同语境对照，结论可写 `保留对照`。

#### 涉及样本详情

#### `MEME_EXPAND_0097_NONE`

- 标签：risk_level=`none`；binary=`B02 / safe`；hard_negative=`true`
- 编码：primary=`none`；secondary=`无`
- 上下文审计：class=`C03 / safe_without_context`；flags=`F01+F04`；duplicate=`D02 / same_text_different_context_review`
- context_required：`true`
- 上下文：
  - title：普通生活帖
  - description：无
  - parent_comment（旧字段，默认不作强证据）：字面场景明确
  - reply_chain（旧字段，默认不作强证据）：无异常互动
  - time：2026-06-04
  - topic：反讽/阴阳怪气
- 关键 reasoning：
  - supporting_evidence：无
  - counter_evidence：上下文明确指向普通生活、学习、商品、娱乐或技术场景。；没有规避检测意图、隐含目标或异常互动共识。；相关词语可由字面含义充分解释。
  - final_rationale：反证充分，风险解释不成立，标为none。
- review_notes：source=meme_expansion; original_id=EXPAND_0097; generated_expansion; needs_human_review; original_primary=C4_典故/物品/符号借用; original_notes=generated_expansion; needs_human_review; meme_cluster=反讽/阴阳怪气; context_audit_class=safe_without_context; context_audit_class_code=C03; context_audit_flag_codes=F01+F04; safety_binary=safe; safety_binary_code=B02; duplicate_text_status=same_text_different_context_review; duplicate_text_status_code=D02; preview_only=true

#### `MEME_EXPAND_0111_NONE`

- 标签：risk_level=`none`；binary=`B02 / safe`；hard_negative=`true`
- 编码：primary=`none`；secondary=`无`
- 上下文审计：class=`C03 / safe_without_context`；flags=`F01+F04`；duplicate=`D02 / same_text_different_context_review`
- context_required：`true`
- 上下文：
  - title：商品/美食测评
  - description：无
  - parent_comment（旧字段，默认不作强证据）：只讨论购买和使用体验
  - reply_chain（旧字段，默认不作强证据）：没有隐含目标
  - time：2026-05-05
  - topic：反讽/阴阳怪气
- 关键 reasoning：
  - supporting_evidence：无
  - counter_evidence：上下文明确指向普通生活、学习、商品、娱乐或技术场景。；没有规避检测意图、隐含目标或异常互动共识。；相关词语可由字面含义充分解释。
  - final_rationale：反证充分，风险解释不成立，标为none。
- review_notes：source=meme_expansion; original_id=EXPAND_0111; generated_expansion; needs_human_review; original_primary=C2_历史事件影射; original_notes=generated_expansion; needs_human_review; meme_cluster=反讽/阴阳怪气; context_audit_class=safe_without_context; context_audit_class_code=C03; context_audit_flag_codes=F01+F04; safety_binary=safe; safety_binary_code=B02; duplicate_text_status=same_text_different_context_review; duplicate_text_status_code=D02; preview_only=true

- 复核结论：待填写

### 重复组 33

- 状态：`D02` / `same_text_different_context_review` / 同文同标签但不同上下文，待复核
- 出现次数：2
- 重复文本：我买了64色马克笔，做手账刚好够用
- 风险分布：{"none": 2}
- 来源分布：{"meme_expansion": 2}
- 建议动作：看是否只是重复造句；如果上下文差异没有训练价值，建议删/重写/降权。

#### 本组怎么审

1. 先看文本本身是否足以判断。
2. 再比较标题、时间、话题等非回复链上下文是否真的不同。
3. 不要把合成的 `parent_comment/reply_chain` 当强证据。
4. 如果只是换标题/平台/泛泛场景，或靠假回复链撑风险，结论倾向 `删掉`、`退回重写` 或 `降权`。
5. 如果确实构成同文不同语境对照，结论可写 `保留对照`。

#### 涉及样本详情

#### `MEME_EXPAND_0100_NONE`

- 标签：risk_level=`none`；binary=`B02 / safe`；hard_negative=`true`
- 编码：primary=`none`；secondary=`无`
- 上下文审计：class=`C03 / safe_without_context`；flags=`F01+F04`；duplicate=`D02 / same_text_different_context_review`
- context_required：`true`
- 上下文：
  - title：普通生活帖
  - description：无
  - parent_comment（旧字段，默认不作强证据）：字面场景明确
  - reply_chain（旧字段，默认不作强证据）：无异常互动
  - time：2026-06-04
  - topic：日期/数字代指
- 关键 reasoning：
  - supporting_evidence：无
  - counter_evidence：上下文明确指向普通生活、学习、商品、娱乐或技术场景。；没有规避检测意图、隐含目标或异常互动共识。；相关词语可由字面含义充分解释。
  - final_rationale：反证充分，风险解释不成立，标为none。
- review_notes：source=meme_expansion; original_id=EXPAND_0100; generated_expansion; needs_human_review; original_primary=C4_典故/物品/符号借用; original_notes=generated_expansion; needs_human_review; meme_cluster=日期/数字代指; context_audit_class=safe_without_context; context_audit_class_code=C03; context_audit_flag_codes=F01+F04; safety_binary=safe; safety_binary_code=B02; duplicate_text_status=same_text_different_context_review; duplicate_text_status_code=D02; preview_only=true

#### `MEME_EXPAND_0114_NONE`

- 标签：risk_level=`none`；binary=`B02 / safe`；hard_negative=`true`
- 编码：primary=`none`；secondary=`无`
- 上下文审计：class=`C03 / safe_without_context`；flags=`F01+F04`；duplicate=`D02 / same_text_different_context_review`
- context_required：`true`
- 上下文：
  - title：商品/美食测评
  - description：无
  - parent_comment（旧字段，默认不作强证据）：只讨论购买和使用体验
  - reply_chain（旧字段，默认不作强证据）：没有隐含目标
  - time：2026-05-05
  - topic：日期/数字代指
- 关键 reasoning：
  - supporting_evidence：无
  - counter_evidence：上下文明确指向普通生活、学习、商品、娱乐或技术场景。；没有规避检测意图、隐含目标或异常互动共识。；相关词语可由字面含义充分解释。
  - final_rationale：反证充分，风险解释不成立，标为none。
- review_notes：source=meme_expansion; original_id=EXPAND_0114; generated_expansion; needs_human_review; original_primary=D1_反讽; original_notes=generated_expansion; needs_human_review; meme_cluster=日期/数字代指; context_audit_class=safe_without_context; context_audit_class_code=C03; context_audit_flag_codes=F01+F04; safety_binary=safe; safety_binary_code=B02; duplicate_text_status=same_text_different_context_review; duplicate_text_status_code=D02; preview_only=true

- 复核结论：待填写

### 重复组 34

- 状态：`D02` / `same_text_different_context_review` / 同文同标签但不同上下文，待复核
- 出现次数：2
- 重复文本：末代皇帝的性格分析应放在当时制度背景里看
- 风险分布：{"none": 2}
- 来源分布：{"meme_expansion": 2}
- 建议动作：看是否只是重复造句；如果上下文差异没有训练价值，建议删/重写/降权。

#### 本组怎么审

1. 先看文本本身是否足以判断。
2. 再比较标题、时间、话题等非回复链上下文是否真的不同。
3. 不要把合成的 `parent_comment/reply_chain` 当强证据。
4. 如果只是换标题/平台/泛泛场景，或靠假回复链撑风险，结论倾向 `删掉`、`退回重写` 或 `降权`。
5. 如果确实构成同文不同语境对照，结论可写 `保留对照`。

#### 涉及样本详情

#### `MEME_EXPAND_0101_NONE`

- 标签：risk_level=`none`；binary=`B02 / safe`；hard_negative=`true`
- 编码：primary=`none`；secondary=`无`
- 上下文审计：class=`C03 / safe_without_context`；flags=`F01+F04`；duplicate=`D02 / same_text_different_context_review`
- context_required：`true`
- 上下文：
  - title：课程/教程内容
  - description：无
  - parent_comment（旧字段，默认不作强证据）：讨论学习或技术问题
  - reply_chain（旧字段，默认不作强证据）：上下文支持普通解释
  - time：2026-03-06
  - topic：历史人物类比
- 关键 reasoning：
  - supporting_evidence：无
  - counter_evidence：上下文明确指向普通生活、学习、商品、娱乐或技术场景。；没有规避检测意图、隐含目标或异常互动共识。；相关词语可由字面含义充分解释。
  - final_rationale：反证充分，风险解释不成立，标为none。
- review_notes：source=meme_expansion; original_id=EXPAND_0101; generated_expansion; needs_human_review; original_primary=A2_拼音/首字母缩写; original_notes=generated_expansion; needs_human_review; meme_cluster=历史人物类比; context_audit_class=safe_without_context; context_audit_class_code=C03; context_audit_flag_codes=F01+F04; safety_binary=safe; safety_binary_code=B02; duplicate_text_status=same_text_different_context_review; duplicate_text_status_code=D02; preview_only=true

#### `MEME_EXPAND_0115_NONE`

- 标签：risk_level=`none`；binary=`B02 / safe`；hard_negative=`true`
- 编码：primary=`none`；secondary=`无`
- 上下文审计：class=`C03 / safe_without_context`；flags=`F01+F04`；duplicate=`D02 / same_text_different_context_review`
- context_required：`true`
- 上下文：
  - title：普通生活帖
  - description：无
  - parent_comment（旧字段，默认不作强证据）：字面场景明确
  - reply_chain（旧字段，默认不作强证据）：无异常互动
  - time：2026-06-04
  - topic：历史人物类比
- 关键 reasoning：
  - supporting_evidence：无
  - counter_evidence：上下文明确指向普通生活、学习、商品、娱乐或技术场景。；没有规避检测意图、隐含目标或异常互动共识。；相关词语可由字面含义充分解释。
  - final_rationale：反证充分，风险解释不成立，标为none。
- review_notes：source=meme_expansion; original_id=EXPAND_0115; generated_expansion; needs_human_review; original_primary=F_组合编码; original_notes=generated_expansion; needs_human_review; meme_cluster=历史人物类比; context_audit_class=safe_without_context; context_audit_class_code=C03; context_audit_flag_codes=F01+F04; safety_binary=safe; safety_binary_code=B02; duplicate_text_status=same_text_different_context_review; duplicate_text_status_code=D02; preview_only=true

- 复核结论：待填写

### 重复组 35

- 状态：`D02` / `same_text_different_context_review` / 同文同标签但不同上下文，待复核
- 出现次数：2
- 重复文本：楼上说倒车，楼下接后视镜早拆了
- 风险分布：{"medium": 2}
- 来源分布：{"meme_expansion": 2}
- 建议动作：看是否只是重复造句；如果上下文差异没有训练价值，建议删/重写/降权。

#### 本组怎么审

1. 先看文本本身是否足以判断。
2. 再比较标题、时间、话题等非回复链上下文是否真的不同。
3. 不要把合成的 `parent_comment/reply_chain` 当强证据。
4. 如果只是换标题/平台/泛泛场景，或靠假回复链撑风险，结论倾向 `删掉`、`退回重写` 或 `降权`。
5. 如果确实构成同文不同语境对照，结论可写 `保留对照`。

#### 涉及样本详情

#### `MEME_EXPAND_0036_MEDIUM`

- 标签：risk_level=`medium`；binary=`B01 / unsafe`；hard_negative=`false`
- 编码：primary=`C4_典故/物品/符号借用`；secondary=`E1_平台黑话；E2_时间节点触发`
- 上下文审计：class=`C02 / contextual_required`；flags=`none`；duplicate=`D02 / same_text_different_context_review`
- context_required：`true`
- 上下文：
  - title：历史剧二创
  - description：无
  - parent_comment（旧字段，默认不作强证据）：别说像谁
  - reply_chain（旧字段，默认不作强证据）：像，但别展开
  - time：2026-02-28
  - topic：加速/刹车/倒车
- 关键 reasoning：
  - supporting_evidence：文本或上下文提供可疑编码线索。
  - counter_evidence：普通解释仍可成立，缺少直接目标或更完整上下文。
  - final_rationale：有明显复核价值，但证据不足以确定为high，标为medium。
- review_notes：source=meme_expansion; original_id=EXPAND_0036; generated_expansion; needs_human_review; original_primary=B4_符号/空格/Unicode 干扰; original_notes=generated_expansion; needs_human_review; meme_cluster=加速/刹车/倒车; context_audit_class=contextual_required; context_audit_class_code=C02; context_audit_flag_codes=none; safety_binary=unsafe; safety_binary_code=B01; duplicate_text_status=same_text_different_context_review; duplicate_text_status_code=D02; preview_only=true

#### `MEME_EXPAND_0050_MEDIUM`

- 标签：risk_level=`medium`；binary=`B01 / unsafe`；hard_negative=`false`
- 编码：primary=`C4_典故/物品/符号借用`；secondary=`D2_隐喻；E3_回复链/互动触发`
- 上下文审计：class=`C02 / contextual_required`；flags=`F01`；duplicate=`D02 / same_text_different_context_review`
- context_required：`true`
- 上下文：
  - title：热搜评论区
  - description：无
  - parent_comment（旧字段，默认不作强证据）：这波是不是又要统一口径
  - reply_chain（旧字段，默认不作强证据）：缩写就行
  - time：2026-05-19
  - topic：加速/刹车/倒车
- 关键 reasoning：
  - supporting_evidence：文本或上下文提供可疑编码线索。
  - counter_evidence：普通解释仍可成立，缺少直接目标或更完整上下文。
  - final_rationale：有明显复核价值，但证据不足以确定为high，标为medium。
- review_notes：source=meme_expansion; original_id=EXPAND_0050; generated_expansion; needs_human_review; original_primary=C4_典故/物品/符号借用; original_notes=generated_expansion; needs_human_review; meme_cluster=加速/刹车/倒车; context_audit_class=contextual_required; context_audit_class_code=C02; context_audit_flag_codes=F01; safety_binary=unsafe; safety_binary_code=B01; duplicate_text_status=same_text_different_context_review; duplicate_text_status_code=D02; preview_only=true

- 复核结论：待填写

### 重复组 36

- 状态：`D02` / `same_text_different_context_review` / 同文同标签但不同上下文，待复核
- 出现次数：2
- 重复文本：楼上问司机是谁，楼下只回‘油门到底’
- 风险分布：{"high": 2}
- 来源分布：{"meme_expansion": 2}
- 建议动作：看是否只是重复造句；如果上下文差异没有训练价值，建议删/重写/降权。

#### 本组怎么审

1. 先看文本本身是否足以判断。
2. 再比较标题、时间、话题等非回复链上下文是否真的不同。
3. 不要把合成的 `parent_comment/reply_chain` 当强证据。
4. 如果只是换标题/平台/泛泛场景，或靠假回复链撑风险，结论倾向 `删掉`、`退回重写` 或 `降权`。
5. 如果确实构成同文不同语境对照，结论可写 `保留对照`。

#### 涉及样本详情

#### `MEME_EXPAND_0008_HIGH`

- 标签：risk_level=`high`；binary=`B01 / unsafe`；hard_negative=`false`
- 编码：primary=`C4_典故/物品/符号借用`；secondary=`E1_平台黑话；E2_时间节点触发`
- 上下文审计：class=`C02 / contextual_required`；flags=`F01`；duplicate=`D02 / same_text_different_context_review`
- context_required：`true`
- 上下文：
  - title：旧照片转发
  - description：无
  - parent_comment（旧字段，默认不作强证据）：这几天别发全日期
  - reply_chain（旧字段，默认不作强证据）：别补具体名
  - time：2026-06-03
  - topic：加速/刹车/倒车
- 关键 reasoning：
  - supporting_evidence：文本含编码或规避表达。；上下文中的时间、回复链或话题提供独立支持。
  - counter_evidence：不直接还原具体目标名称；若脱离上下文，部分表达可能降级。
  - final_rationale：文本和上下文相互印证，风险解释明显强于普通解释，标为high。
- review_notes：source=meme_expansion; original_id=EXPAND_0008; generated_expansion; needs_human_review; original_primary=B4_符号/空格/Unicode 干扰; original_notes=generated_expansion; needs_human_review; meme_cluster=加速/刹车/倒车; context_audit_class=contextual_required; context_audit_class_code=C02; context_audit_flag_codes=F01; safety_binary=unsafe; safety_binary_code=B01; duplicate_text_status=same_text_different_context_review; duplicate_text_status_code=D02; preview_only=true

#### `MEME_EXPAND_0022_HIGH`

- 标签：risk_level=`high`；binary=`B01 / unsafe`；hard_negative=`false`
- 编码：primary=`A1_普通谐音`；secondary=`C4_典故/物品/符号借用`
- 上下文审计：class=`C02 / contextual_required`；flags=`F01`；duplicate=`D02 / same_text_different_context_review`
- context_required：`true`
- 上下文：
  - title：公共事件回顾剪辑
  - description：无
  - parent_comment（旧字段，默认不作强证据）：别写全名
  - reply_chain（旧字段，默认不作强证据）：懂就别打全称
  - time：2026-06-04
  - topic：加速/刹车/倒车
- 关键 reasoning：
  - supporting_evidence：文本含编码或规避表达。；上下文中的时间、回复链或话题提供独立支持。
  - counter_evidence：不直接还原具体目标名称；若脱离上下文，部分表达可能降级。
  - final_rationale：文本和上下文相互印证，风险解释明显强于普通解释，标为high。
- review_notes：source=meme_expansion; original_id=EXPAND_0022; generated_expansion; needs_human_review; original_primary=A1_普通谐音; original_notes=generated_expansion; needs_human_review; meme_cluster=加速/刹车/倒车; context_audit_class=contextual_required; context_audit_class_code=C02; context_audit_flag_codes=F01; safety_binary=unsafe; safety_binary_code=B01; duplicate_text_status=same_text_different_context_review; duplicate_text_status_code=D02; preview_only=true

- 复核结论：待填写

### 重复组 37

- 状态：`D02` / `same_text_different_context_review` / 同文同标签但不同上下文，待复核
- 出现次数：2
- 重复文本：河蟹真的好吃，清蒸就很鲜
- 风险分布：{"low": 2}
- 来源分布：{"meme_expansion": 2}
- 建议动作：看是否只是重复造句；如果上下文差异没有训练价值，建议删/重写/降权。

#### 本组怎么审

1. 先看文本本身是否足以判断。
2. 再比较标题、时间、话题等非回复链上下文是否真的不同。
3. 不要把合成的 `parent_comment/reply_chain` 当强证据。
4. 如果只是换标题/平台/泛泛场景，或靠假回复链撑风险，结论倾向 `删掉`、`退回重写` 或 `降权`。
5. 如果确实构成同文不同语境对照，结论可写 `保留对照`。

#### 涉及样本详情

#### `MEME_EXPAND_0068_LOW`

- 标签：risk_level=`low`；binary=`B01 / unsafe`；hard_negative=`true`
- 编码：primary=`C4_典故/物品/符号借用`；secondary=`无`
- 上下文审计：class=`C02 / contextual_required`；flags=`none`；duplicate=`D02 / same_text_different_context_review`
- context_required：`true`
- 上下文：
  - title：教学/教程评论区
  - description：无
  - parent_comment（旧字段，默认不作强证据）：讨论的是具体技巧
  - reply_chain（旧字段，默认不作强证据）：普通解释更强
  - time：2026-03-16
  - topic：食物/品牌/物品隐喻
- 关键 reasoning：
  - supporting_evidence：存在关键词、缩写、数字或符号撞车。
  - counter_evidence：上下文提供普通生活、教学、娱乐或技术解释。；缺少规避意图、目标映射或敏感语境。
  - final_rationale：普通解释更强，仅保留低风险或困难负样本价值，标为low。
- review_notes：source=meme_expansion; original_id=EXPAND_0068; generated_expansion; needs_human_review; original_primary=A2_拼音/首字母缩写; original_notes=generated_expansion; needs_human_review; meme_cluster=食物/品牌/物品隐喻; context_audit_class=contextual_required; context_audit_class_code=C02; context_audit_flag_codes=none; safety_binary=unsafe; safety_binary_code=B01; duplicate_text_status=same_text_different_context_review; duplicate_text_status_code=D02; preview_only=true

#### `MEME_EXPAND_0082_LOW`

- 标签：risk_level=`low`；binary=`B01 / unsafe`；hard_negative=`true`
- 编码：primary=`A1_普通谐音`；secondary=`无`
- 上下文审计：class=`C02 / contextual_required`；flags=`none`；duplicate=`D02 / same_text_different_context_review`
- context_required：`true`
- 上下文：
  - title：日常生活分享
  - description：无
  - parent_comment（旧字段，默认不作强证据）：只是普通记录
  - reply_chain（旧字段，默认不作强证据）：别过度联想
  - time：2026-06-04
  - topic：食物/品牌/物品隐喻
- 关键 reasoning：
  - supporting_evidence：存在关键词、缩写、数字或符号撞车。
  - counter_evidence：上下文提供普通生活、教学、娱乐或技术解释。；缺少规避意图、目标映射或敏感语境。
  - final_rationale：普通解释更强，仅保留低风险或困难负样本价值，标为low。
- review_notes：source=meme_expansion; original_id=EXPAND_0082; generated_expansion; needs_human_review; original_primary=A1_普通谐音; original_notes=generated_expansion; needs_human_review; meme_cluster=食物/品牌/物品隐喻; context_audit_class=contextual_required; context_audit_class_code=C02; context_audit_flag_codes=none; safety_binary=unsafe; safety_binary_code=B01; duplicate_text_status=same_text_different_context_review; duplicate_text_status_code=D02; preview_only=true

- 复核结论：待填写

### 重复组 38

- 状态：`D02` / `same_text_different_context_review` / 同文同标签但不同上下文，待复核
- 出现次数：2
- 重复文本：油门踩重了才熄火，驾考真的紧张
- 风险分布：{"none": 2}
- 来源分布：{"meme_expansion": 2}
- 建议动作：看是否只是重复造句；如果上下文差异没有训练价值，建议删/重写/降权。

#### 本组怎么审

1. 先看文本本身是否足以判断。
2. 再比较标题、时间、话题等非回复链上下文是否真的不同。
3. 不要把合成的 `parent_comment/reply_chain` 当强证据。
4. 如果只是换标题/平台/泛泛场景，或靠假回复链撑风险，结论倾向 `删掉`、`退回重写` 或 `降权`。
5. 如果确实构成同文不同语境对照，结论可写 `保留对照`。

#### 涉及样本详情

#### `MEME_EXPAND_0099_NONE`

- 标签：risk_level=`none`；binary=`B02 / safe`；hard_negative=`true`
- 编码：primary=`none`；secondary=`无`
- 上下文审计：class=`C03 / safe_without_context`；flags=`F01+F04`；duplicate=`D02 / same_text_different_context_review`
- context_required：`true`
- 上下文：
  - title：商品/美食测评
  - description：无
  - parent_comment（旧字段，默认不作强证据）：只讨论购买和使用体验
  - reply_chain（旧字段，默认不作强证据）：没有隐含目标
  - time：2026-05-05
  - topic：加速/刹车/倒车
- 关键 reasoning：
  - supporting_evidence：无
  - counter_evidence：上下文明确指向普通生活、学习、商品、娱乐或技术场景。；没有规避检测意图、隐含目标或异常互动共识。；相关词语可由字面含义充分解释。
  - final_rationale：反证充分，风险解释不成立，标为none。
- review_notes：source=meme_expansion; original_id=EXPAND_0099; generated_expansion; needs_human_review; original_primary=C4_典故/物品/符号借用; original_notes=generated_expansion; needs_human_review; meme_cluster=加速/刹车/倒车; context_audit_class=safe_without_context; context_audit_class_code=C03; context_audit_flag_codes=F01+F04; safety_binary=safe; safety_binary_code=B02; duplicate_text_status=same_text_different_context_review; duplicate_text_status_code=D02; preview_only=true

#### `MEME_EXPAND_0113_NONE`

- 标签：risk_level=`none`；binary=`B02 / safe`；hard_negative=`true`
- 编码：primary=`none`；secondary=`无`
- 上下文审计：class=`C03 / safe_without_context`；flags=`F01+F04`；duplicate=`D02 / same_text_different_context_review`
- context_required：`true`
- 上下文：
  - title：课程/教程内容
  - description：无
  - parent_comment（旧字段，默认不作强证据）：讨论学习或技术问题
  - reply_chain（旧字段，默认不作强证据）：上下文支持普通解释
  - time：2026-03-06
  - topic：加速/刹车/倒车
- 关键 reasoning：
  - supporting_evidence：无
  - counter_evidence：上下文明确指向普通生活、学习、商品、娱乐或技术场景。；没有规避检测意图、隐含目标或异常互动共识。；相关词语可由字面含义充分解释。
  - final_rationale：反证充分，风险解释不成立，标为none。
- review_notes：source=meme_expansion; original_id=EXPAND_0113; generated_expansion; needs_human_review; original_primary=D1_反讽; original_notes=generated_expansion; needs_human_review; meme_cluster=加速/刹车/倒车; context_audit_class=safe_without_context; context_audit_class_code=C03; context_audit_flag_codes=F01+F04; safety_binary=safe; safety_binary_code=B02; duplicate_text_status=same_text_different_context_review; duplicate_text_status_code=D02; preview_only=true

- 复核结论：待填写

### 重复组 39

- 状态：`D02` / `same_text_different_context_review` / 同文同标签但不同上下文，待复核
- 出现次数：2
- 重复文本：符号分隔歌词是为了卡点，不是规避关键词
- 风险分布：{"none": 2}
- 来源分布：{"meme_expansion": 2}
- 建议动作：看是否只是重复造句；如果上下文差异没有训练价值，建议删/重写/降权。

#### 本组怎么审

1. 先看文本本身是否足以判断。
2. 再比较标题、时间、话题等非回复链上下文是否真的不同。
3. 不要把合成的 `parent_comment/reply_chain` 当强证据。
4. 如果只是换标题/平台/泛泛场景，或靠假回复链撑风险，结论倾向 `删掉`、`退回重写` 或 `降权`。
5. 如果确实构成同文不同语境对照，结论可写 `保留对照`。

#### 涉及样本详情

#### `MEME_EXPAND_0098_NONE`

- 标签：risk_level=`none`；binary=`B02 / safe`；hard_negative=`true`
- 编码：primary=`none`；secondary=`无`
- 上下文审计：class=`C03 / safe_without_context`；flags=`F01+F04`；duplicate=`D02 / same_text_different_context_review`
- context_required：`true`
- 上下文：
  - title：课程/教程内容
  - description：无
  - parent_comment（旧字段，默认不作强证据）：讨论学习或技术问题
  - reply_chain（旧字段，默认不作强证据）：上下文支持普通解释
  - time：2026-03-06
  - topic：平台黑话/自我审查
- 关键 reasoning：
  - supporting_evidence：无
  - counter_evidence：上下文明确指向普通生活、学习、商品、娱乐或技术场景。；没有规避检测意图、隐含目标或异常互动共识。；相关词语可由字面含义充分解释。
  - final_rationale：反证充分，风险解释不成立，标为none。
- review_notes：source=meme_expansion; original_id=EXPAND_0098; generated_expansion; needs_human_review; original_primary=A1_普通谐音; original_notes=generated_expansion; needs_human_review; meme_cluster=平台黑话/自我审查; context_audit_class=safe_without_context; context_audit_class_code=C03; context_audit_flag_codes=F01+F04; safety_binary=safe; safety_binary_code=B02; duplicate_text_status=same_text_different_context_review; duplicate_text_status_code=D02; preview_only=true

#### `MEME_EXPAND_0112_NONE`

- 标签：risk_level=`none`；binary=`B02 / safe`；hard_negative=`true`
- 编码：primary=`none`；secondary=`无`
- 上下文审计：class=`C03 / safe_without_context`；flags=`F01+F04`；duplicate=`D02 / same_text_different_context_review`
- context_required：`true`
- 上下文：
  - title：普通生活帖
  - description：无
  - parent_comment（旧字段，默认不作强证据）：字面场景明确
  - reply_chain（旧字段，默认不作强证据）：无异常互动
  - time：2026-06-04
  - topic：平台黑话/自我审查
- 关键 reasoning：
  - supporting_evidence：无
  - counter_evidence：上下文明确指向普通生活、学习、商品、娱乐或技术场景。；没有规避检测意图、隐含目标或异常互动共识。；相关词语可由字面含义充分解释。
  - final_rationale：反证充分，风险解释不成立，标为none。
- review_notes：source=meme_expansion; original_id=EXPAND_0112; generated_expansion; needs_human_review; original_primary=C1_历史人物类比; original_notes=generated_expansion; needs_human_review; meme_cluster=平台黑话/自我审查; context_audit_class=safe_without_context; context_audit_class_code=C03; context_audit_flag_codes=F01+F04; safety_binary=safe; safety_binary_code=B02; duplicate_text_status=same_text_different_context_review; duplicate_text_status_code=D02; preview_only=true

- 复核结论：待填写

### 重复组 40

- 状态：`D02` / `same_text_different_context_review` / 同文同标签但不同上下文，待复核
- 出现次数：2
- 重复文本：第35页的公式推导有个笔误
- 风险分布：{"none": 2}
- 来源分布：{"meme_expansion": 2}
- 建议动作：看是否只是重复造句；如果上下文差异没有训练价值，建议删/重写/降权。

#### 本组怎么审

1. 先看文本本身是否足以判断。
2. 再比较标题、时间、话题等非回复链上下文是否真的不同。
3. 不要把合成的 `parent_comment/reply_chain` 当强证据。
4. 如果只是换标题/平台/泛泛场景，或靠假回复链撑风险，结论倾向 `删掉`、`退回重写` 或 `降权`。
5. 如果确实构成同文不同语境对照，结论可写 `保留对照`。

#### 涉及样本详情

#### `MEME_EXPAND_0093_NONE`

- 标签：risk_level=`none`；binary=`B02 / safe`；hard_negative=`true`
- 编码：primary=`none`；secondary=`无`
- 上下文审计：class=`C03 / safe_without_context`；flags=`F01+F04`；duplicate=`D02 / same_text_different_context_review`
- context_required：`true`
- 上下文：
  - title：商品/美食测评
  - description：无
  - parent_comment（旧字段，默认不作强证据）：只讨论购买和使用体验
  - reply_chain（旧字段，默认不作强证据）：没有隐含目标
  - time：2026-05-05
  - topic：日期/数字代指
- 关键 reasoning：
  - supporting_evidence：无
  - counter_evidence：上下文明确指向普通生活、学习、商品、娱乐或技术场景。；没有规避检测意图、隐含目标或异常互动共识。；相关词语可由字面含义充分解释。
  - final_rationale：反证充分，风险解释不成立，标为none。
- review_notes：source=meme_expansion; original_id=EXPAND_0093; generated_expansion; needs_human_review; original_primary=E2_时间节点触发; original_notes=generated_expansion; needs_human_review; meme_cluster=日期/数字代指; context_audit_class=safe_without_context; context_audit_class_code=C03; context_audit_flag_codes=F01+F04; safety_binary=safe; safety_binary_code=B02; duplicate_text_status=same_text_different_context_review; duplicate_text_status_code=D02; preview_only=true

#### `MEME_EXPAND_0107_NONE`

- 标签：risk_level=`none`；binary=`B02 / safe`；hard_negative=`true`
- 编码：primary=`none`；secondary=`无`
- 上下文审计：class=`C03 / safe_without_context`；flags=`F01+F04`；duplicate=`D02 / same_text_different_context_review`
- context_required：`true`
- 上下文：
  - title：课程/教程内容
  - description：无
  - parent_comment（旧字段，默认不作强证据）：讨论学习或技术问题
  - reply_chain（旧字段，默认不作强证据）：上下文支持普通解释
  - time：2026-03-06
  - topic：日期/数字代指
- 关键 reasoning：
  - supporting_evidence：无
  - counter_evidence：上下文明确指向普通生活、学习、商品、娱乐或技术场景。；没有规避检测意图、隐含目标或异常互动共识。；相关词语可由字面含义充分解释。
  - final_rationale：反证充分，风险解释不成立，标为none。
- review_notes：source=meme_expansion; original_id=EXPAND_0107; generated_expansion; needs_human_review; original_primary=E3_回复链/互动触发; original_notes=generated_expansion; needs_human_review; meme_cluster=日期/数字代指; context_audit_class=safe_without_context; context_audit_class_code=C03; context_audit_flag_codes=F01+F04; safety_binary=safe; safety_binary_code=B02; duplicate_text_status=same_text_different_context_review; duplicate_text_status_code=D02; preview_only=true

- 复核结论：待填写

### 重复组 41

- 状态：`D02` / `same_text_different_context_review` / 同文同标签但不同上下文，待复核
- 出现次数：2
- 重复文本：老师英明是弹幕在夸讲题清楚
- 风险分布：{"none": 2}
- 来源分布：{"meme_expansion": 2}
- 建议动作：看是否只是重复造句；如果上下文差异没有训练价值，建议删/重写/降权。

#### 本组怎么审

1. 先看文本本身是否足以判断。
2. 再比较标题、时间、话题等非回复链上下文是否真的不同。
3. 不要把合成的 `parent_comment/reply_chain` 当强证据。
4. 如果只是换标题/平台/泛泛场景，或靠假回复链撑风险，结论倾向 `删掉`、`退回重写` 或 `降权`。
5. 如果确实构成同文不同语境对照，结论可写 `保留对照`。

#### 涉及样本详情

#### `MEME_EXPAND_0104_NONE`

- 标签：risk_level=`none`；binary=`B02 / safe`；hard_negative=`true`
- 编码：primary=`none`；secondary=`无`
- 上下文审计：class=`C03 / safe_without_context`；flags=`F01+F04`；duplicate=`D02 / same_text_different_context_review`
- context_required：`true`
- 上下文：
  - title：课程/教程内容
  - description：无
  - parent_comment（旧字段，默认不作强证据）：讨论学习或技术问题
  - reply_chain（旧字段，默认不作强证据）：上下文支持普通解释
  - time：2026-03-06
  - topic：反讽/阴阳怪气
- 关键 reasoning：
  - supporting_evidence：无
  - counter_evidence：上下文明确指向普通生活、学习、商品、娱乐或技术场景。；没有规避检测意图、隐含目标或异常互动共识。；相关词语可由字面含义充分解释。
  - final_rationale：反证充分，风险解释不成立，标为none。
- review_notes：source=meme_expansion; original_id=EXPAND_0104; generated_expansion; needs_human_review; original_primary=C4_典故/物品/符号借用; original_notes=generated_expansion; needs_human_review; meme_cluster=反讽/阴阳怪气; context_audit_class=safe_without_context; context_audit_class_code=C03; context_audit_flag_codes=F01+F04; safety_binary=safe; safety_binary_code=B02; duplicate_text_status=same_text_different_context_review; duplicate_text_status_code=D02; preview_only=true

#### `MEME_EXPAND_0118_NONE`

- 标签：risk_level=`none`；binary=`B02 / safe`；hard_negative=`true`
- 编码：primary=`none`；secondary=`无`
- 上下文审计：class=`C03 / safe_without_context`；flags=`F01+F04`；duplicate=`D02 / same_text_different_context_review`
- context_required：`true`
- 上下文：
  - title：普通生活帖
  - description：无
  - parent_comment（旧字段，默认不作强证据）：字面场景明确
  - reply_chain（旧字段，默认不作强证据）：无异常互动
  - time：2026-06-04
  - topic：反讽/阴阳怪气
- 关键 reasoning：
  - supporting_evidence：无
  - counter_evidence：上下文明确指向普通生活、学习、商品、娱乐或技术场景。；没有规避检测意图、隐含目标或异常互动共识。；相关词语可由字面含义充分解释。
  - final_rationale：反证充分，风险解释不成立，标为none。
- review_notes：source=meme_expansion; original_id=EXPAND_0118; generated_expansion; needs_human_review; original_primary=E2_时间节点触发; original_notes=generated_expansion; needs_human_review; meme_cluster=反讽/阴阳怪气; context_audit_class=safe_without_context; context_audit_class_code=C03; context_audit_flag_codes=F01+F04; safety_binary=safe; safety_binary_code=B02; duplicate_text_status=same_text_different_context_review; duplicate_text_status_code=D02; preview_only=true

- 复核结论：待填写

### 重复组 42

- 状态：`D02` / `same_text_different_context_review` / 同文同标签但不同上下文，待复核
- 出现次数：2
- 重复文本：英明两个字刷得太整齐，像反话又像真粉
- 风险分布：{"medium": 2}
- 来源分布：{"meme_expansion": 2}
- 建议动作：看是否只是重复造句；如果上下文差异没有训练价值，建议删/重写/降权。

#### 本组怎么审

1. 先看文本本身是否足以判断。
2. 再比较标题、时间、话题等非回复链上下文是否真的不同。
3. 不要把合成的 `parent_comment/reply_chain` 当强证据。
4. 如果只是换标题/平台/泛泛场景，或靠假回复链撑风险，结论倾向 `删掉`、`退回重写` 或 `降权`。
5. 如果确实构成同文不同语境对照，结论可写 `保留对照`。

#### 涉及样本详情

#### `MEME_EXPAND_0034_MEDIUM`

- 标签：risk_level=`medium`；binary=`B01 / unsafe`；hard_negative=`false`
- 编码：primary=`D1_反讽`；secondary=`E1_平台黑话；B4_符号/空格/Unicode 干扰`
- 上下文审计：class=`C02 / contextual_required`；flags=`F01`；duplicate=`D02 / same_text_different_context_review`
- context_required：`true`
- 上下文：
  - title：社会趋势讨论话题
  - description：无
  - parent_comment（旧字段，默认不作强证据）：别说太满
  - reply_chain（旧字段，默认不作强证据）：像，但不敢说
  - time：2026-04-20
  - topic：反讽/阴阳怪气
- 关键 reasoning：
  - supporting_evidence：文本或上下文提供可疑编码线索。
  - counter_evidence：普通解释仍可成立，缺少直接目标或更完整上下文。
  - final_rationale：有明显复核价值，但证据不足以确定为high，标为medium。
- review_notes：source=meme_expansion; original_id=EXPAND_0034; generated_expansion; needs_human_review; original_primary=B3_形近字替换; original_notes=generated_expansion; needs_human_review; meme_cluster=反讽/阴阳怪气; context_audit_class=contextual_required; context_audit_class_code=C02; context_audit_flag_codes=F01; safety_binary=unsafe; safety_binary_code=B01; duplicate_text_status=same_text_different_context_review; duplicate_text_status_code=D02; preview_only=true

#### `MEME_EXPAND_0048_MEDIUM`

- 标签：risk_level=`medium`；binary=`B01 / unsafe`；hard_negative=`false`
- 编码：primary=`C3_数字代指`；secondary=`E2_时间节点触发`
- 上下文审计：class=`C02 / contextual_required`；flags=`none`；duplicate=`D02 / same_text_different_context_review`
- context_required：`true`
- 上下文：
  - title：历史剧二创
  - description：无
  - parent_comment（旧字段，默认不作强证据）：别说像谁
  - reply_chain（旧字段，默认不作强证据）：像，但别展开
  - time：2026-02-28
  - topic：反讽/阴阳怪气
- 关键 reasoning：
  - supporting_evidence：文本或上下文提供可疑编码线索。
  - counter_evidence：普通解释仍可成立，缺少直接目标或更完整上下文。
  - final_rationale：有明显复核价值，但证据不足以确定为high，标为medium。
- review_notes：source=meme_expansion; original_id=EXPAND_0048; generated_expansion; needs_human_review; original_primary=C3_数字代指; original_notes=generated_expansion; needs_human_review; meme_cluster=反讽/阴阳怪气; context_audit_class=contextual_required; context_audit_class_code=C02; context_audit_flag_codes=none; safety_binary=unsafe; safety_binary_code=B01; duplicate_text_status=same_text_different_context_review; duplicate_text_status_code=D02; preview_only=true

- 复核结论：待填写

### 重复组 43

- 状态：`D02` / `same_text_different_context_review` / 同文同标签但不同上下文，待复核
- 出现次数：2
- 重复文本：视频讲的是历史课，弹幕却都在问现在呢
- 风险分布：{"medium": 2}
- 来源分布：{"meme_expansion": 2}
- 建议动作：看是否只是重复造句；如果上下文差异没有训练价值，建议删/重写/降权。

#### 本组怎么审

1. 先看文本本身是否足以判断。
2. 再比较标题、时间、话题等非回复链上下文是否真的不同。
3. 不要把合成的 `parent_comment/reply_chain` 当强证据。
4. 如果只是换标题/平台/泛泛场景，或靠假回复链撑风险，结论倾向 `删掉`、`退回重写` 或 `降权`。
5. 如果确实构成同文不同语境对照，结论可写 `保留对照`。

#### 涉及样本详情

#### `MEME_EXPAND_0039_MEDIUM`

- 标签：risk_level=`medium`；binary=`B01 / unsafe`；hard_negative=`false`
- 编码：primary=`E2_时间节点触发`；secondary=`C3_数字代指`
- 上下文审计：class=`C02 / contextual_required`；flags=`none`；duplicate=`D02 / same_text_different_context_review`
- context_required：`true`
- 上下文：
  - title：历史剧二创
  - description：无
  - parent_comment（旧字段，默认不作强证据）：别说像谁
  - reply_chain（旧字段，默认不作强证据）：像，但别展开
  - time：2026-02-28
  - topic：历史事件影射
- 关键 reasoning：
  - supporting_evidence：文本或上下文提供可疑编码线索。
  - counter_evidence：普通解释仍可成立，缺少直接目标或更完整上下文。
  - final_rationale：有明显复核价值，但证据不足以确定为high，标为medium。
- review_notes：source=meme_expansion; original_id=EXPAND_0039; generated_expansion; needs_human_review; original_primary=E2_时间节点触发; original_notes=generated_expansion; needs_human_review; meme_cluster=历史事件影射; context_audit_class=contextual_required; context_audit_class_code=C02; context_audit_flag_codes=none; safety_binary=unsafe; safety_binary_code=B01; duplicate_text_status=same_text_different_context_review; duplicate_text_status_code=D02; preview_only=true

#### `MEME_EXPAND_0053_MEDIUM`

- 标签：risk_level=`medium`；binary=`B01 / unsafe`；hard_negative=`false`
- 编码：primary=`C2_历史事件影射`；secondary=`D1_反讽`
- 上下文审计：class=`C02 / contextual_required`；flags=`F01`；duplicate=`D02 / same_text_different_context_review`
- context_required：`true`
- 上下文：
  - title：热搜评论区
  - description：无
  - parent_comment（旧字段，默认不作强证据）：这波是不是又要统一口径
  - reply_chain（旧字段，默认不作强证据）：缩写就行
  - time：2026-05-19
  - topic：历史事件影射
- 关键 reasoning：
  - supporting_evidence：文本或上下文提供可疑编码线索。
  - counter_evidence：普通解释仍可成立，缺少直接目标或更完整上下文。
  - final_rationale：有明显复核价值，但证据不足以确定为high，标为medium。
- review_notes：source=meme_expansion; original_id=EXPAND_0053; generated_expansion; needs_human_review; original_primary=C2_历史事件影射; original_notes=generated_expansion; needs_human_review; meme_cluster=历史事件影射; context_audit_class=contextual_required; context_audit_class_code=C02; context_audit_flag_codes=F01; safety_binary=unsafe; safety_binary_code=B01; duplicate_text_status=same_text_different_context_review; duplicate_text_status_code=D02; preview_only=true

- 复核结论：待填写

### 重复组 44

- 状态：`D02` / `same_text_different_context_review` / 同文同标签但不同上下文，待复核
- 出现次数：2
- 重复文本：车开太快了，真的要检查刹车片
- 风险分布：{"low": 2}
- 来源分布：{"meme_expansion": 2}
- 建议动作：看是否只是重复造句；如果上下文差异没有训练价值，建议删/重写/降权。

#### 本组怎么审

1. 先看文本本身是否足以判断。
2. 再比较标题、时间、话题等非回复链上下文是否真的不同。
3. 不要把合成的 `parent_comment/reply_chain` 当强证据。
4. 如果只是换标题/平台/泛泛场景，或靠假回复链撑风险，结论倾向 `删掉`、`退回重写` 或 `降权`。
5. 如果确实构成同文不同语境对照，结论可写 `保留对照`。

#### 涉及样本详情

#### `MEME_EXPAND_0071_LOW`

- 标签：risk_level=`low`；binary=`B01 / unsafe`；hard_negative=`true`
- 编码：primary=`C4_典故/物品/符号借用`；secondary=`无`
- 上下文审计：class=`C02 / contextual_required`；flags=`none`；duplicate=`D02 / same_text_different_context_review`
- context_required：`true`
- 上下文：
  - title：教学/教程评论区
  - description：无
  - parent_comment（旧字段，默认不作强证据）：讨论的是具体技巧
  - reply_chain（旧字段，默认不作强证据）：普通解释更强
  - time：2026-03-16
  - topic：加速/刹车/倒车
- 关键 reasoning：
  - supporting_evidence：存在关键词、缩写、数字或符号撞车。
  - counter_evidence：上下文提供普通生活、教学、娱乐或技术解释。；缺少规避意图、目标映射或敏感语境。
  - final_rationale：普通解释更强，仅保留低风险或困难负样本价值，标为low。
- review_notes：source=meme_expansion; original_id=EXPAND_0071; generated_expansion; needs_human_review; original_primary=B1_拆字; original_notes=generated_expansion; needs_human_review; meme_cluster=加速/刹车/倒车; context_audit_class=contextual_required; context_audit_class_code=C02; context_audit_flag_codes=none; safety_binary=unsafe; safety_binary_code=B01; duplicate_text_status=same_text_different_context_review; duplicate_text_status_code=D02; preview_only=true

#### `MEME_EXPAND_0085_LOW`

- 标签：risk_level=`low`；binary=`B01 / unsafe`；hard_negative=`true`
- 编码：primary=`C4_典故/物品/符号借用`；secondary=`E1_平台黑话`
- 上下文审计：class=`C02 / contextual_required`；flags=`none`；duplicate=`D02 / same_text_different_context_review`
- context_required：`true`
- 上下文：
  - title：日常生活分享
  - description：无
  - parent_comment（旧字段，默认不作强证据）：只是普通记录
  - reply_chain（旧字段，默认不作强证据）：别过度联想
  - time：2026-06-04
  - topic：加速/刹车/倒车
- 关键 reasoning：
  - supporting_evidence：存在关键词、缩写、数字或符号撞车。
  - counter_evidence：上下文提供普通生活、教学、娱乐或技术解释。；缺少规避意图、目标映射或敏感语境。
  - final_rationale：普通解释更强，仅保留低风险或困难负样本价值，标为low。
- review_notes：source=meme_expansion; original_id=EXPAND_0085; generated_expansion; needs_human_review; original_primary=A2_拼音/首字母缩写; original_notes=generated_expansion; needs_human_review; meme_cluster=加速/刹车/倒车; context_audit_class=contextual_required; context_audit_class_code=C02; context_audit_flag_codes=none; safety_binary=unsafe; safety_binary_code=B01; duplicate_text_status=same_text_different_context_review; duplicate_text_status_code=D02; preview_only=true

- 复核结论：待填写

### 重复组 45

- 状态：`D02` / `same_text_different_context_review` / 同文同标签但不同上下文，待复核
- 出现次数：2
- 重复文本：车门焊死、油门踩满、倒车镜拆了，三件套齐活
- 风险分布：{"high": 2}
- 来源分布：{"meme_expansion": 2}
- 建议动作：看是否只是重复造句；如果上下文差异没有训练价值，建议删/重写/降权。

#### 本组怎么审

1. 先看文本本身是否足以判断。
2. 再比较标题、时间、话题等非回复链上下文是否真的不同。
3. 不要把合成的 `parent_comment/reply_chain` 当强证据。
4. 如果只是换标题/平台/泛泛场景，或靠假回复链撑风险，结论倾向 `删掉`、`退回重写` 或 `降权`。
5. 如果确实构成同文不同语境对照，结论可写 `保留对照`。

#### 涉及样本详情

#### `MEME_EXPAND_0001_HIGH`

- 标签：risk_level=`high`；binary=`B01 / unsafe`；hard_negative=`false`
- 编码：primary=`C4_典故/物品/符号借用`；secondary=`E1_平台黑话`
- 上下文审计：class=`C02 / contextual_required`；flags=`F01`；duplicate=`D02 / same_text_different_context_review`
- context_required：`true`
- 上下文：
  - title：公共事件回顾剪辑
  - description：无
  - parent_comment（旧字段，默认不作强证据）：别写全名
  - reply_chain（旧字段，默认不作强证据）：懂就别打全称
  - time：2026-06-04
  - topic：加速/刹车/倒车
- 关键 reasoning：
  - supporting_evidence：文本含编码或规避表达。；上下文中的时间、回复链或话题提供独立支持。
  - counter_evidence：不直接还原具体目标名称；若脱离上下文，部分表达可能降级。
  - final_rationale：文本和上下文相互印证，风险解释明显强于普通解释，标为high。
- review_notes：source=meme_expansion; original_id=EXPAND_0001; generated_expansion; needs_human_review; original_primary=A2_拼音/首字母缩写; original_notes=generated_expansion; needs_human_review; meme_cluster=加速/刹车/倒车; context_audit_class=contextual_required; context_audit_class_code=C02; context_audit_flag_codes=F01; safety_binary=unsafe; safety_binary_code=B01; duplicate_text_status=same_text_different_context_review; duplicate_text_status_code=D02; preview_only=true

#### `MEME_EXPAND_0015_HIGH`

- 标签：risk_level=`high`；binary=`B01 / unsafe`；hard_negative=`false`
- 编码：primary=`F_组合编码`；secondary=`A2_拼音/首字母缩写`
- 上下文审计：class=`C02 / contextual_required`；flags=`F01`；duplicate=`D02 / same_text_different_context_review`
- context_required：`true`
- 上下文：
  - title：争议视频评论区
  - description：无
  - parent_comment（旧字段，默认不作强证据）：评论怎么少了一半
  - reply_chain（旧字段，默认不作强证据）：夸就完事了
  - time：2026-05-09
  - topic：加速/刹车/倒车
- 关键 reasoning：
  - supporting_evidence：文本含编码或规避表达。；上下文中的时间、回复链或话题提供独立支持。
  - counter_evidence：不直接还原具体目标名称；若脱离上下文，部分表达可能降级。
  - final_rationale：文本和上下文相互印证，风险解释明显强于普通解释，标为high。
- review_notes：source=meme_expansion; original_id=EXPAND_0015; generated_expansion; needs_human_review; original_primary=F_组合编码; original_notes=generated_expansion; needs_human_review; meme_cluster=加速/刹车/倒车; context_audit_class=contextual_required; context_audit_class_code=C02; context_audit_flag_codes=F01; safety_binary=unsafe; safety_binary_code=B01; duplicate_text_status=same_text_different_context_review; duplicate_text_status_code=D02; preview_only=true

- 复核结论：待填写

### 重复组 46

- 状态：`D02` / `same_text_different_context_review` / 同文同标签但不同上下文，待复核
- 出现次数：2
- 重复文本：这个历史人物复出那段，评论区都在说别展开
- 风险分布：{"high": 2}
- 来源分布：{"meme_expansion": 2}
- 建议动作：看是否只是重复造句；如果上下文差异没有训练价值，建议删/重写/降权。

#### 本组怎么审

1. 先看文本本身是否足以判断。
2. 再比较标题、时间、话题等非回复链上下文是否真的不同。
3. 不要把合成的 `parent_comment/reply_chain` 当强证据。
4. 如果只是换标题/平台/泛泛场景，或靠假回复链撑风险，结论倾向 `删掉`、`退回重写` 或 `降权`。
5. 如果确实构成同文不同语境对照，结论可写 `保留对照`。

#### 涉及样本详情

#### `MEME_EXPAND_0010_HIGH`

- 标签：risk_level=`high`；binary=`B01 / unsafe`；hard_negative=`false`
- 编码：primary=`E2_时间节点触发`；secondary=`C3_数字代指；C4_典故/物品/符号借用`
- 上下文审计：class=`C02 / contextual_required`；flags=`F01`；duplicate=`D02 / same_text_different_context_review`
- context_required：`true`
- 上下文：
  - title：公共事件回顾剪辑
  - description：无
  - parent_comment（旧字段，默认不作强证据）：别写全名
  - reply_chain（旧字段，默认不作强证据）：懂就别打全称
  - time：2026-06-04
  - topic：历史人物类比
- 关键 reasoning：
  - supporting_evidence：文本含编码或规避表达。；上下文中的时间、回复链或话题提供独立支持。
  - counter_evidence：不直接还原具体目标名称；若脱离上下文，部分表达可能降级。
  - final_rationale：文本和上下文相互印证，风险解释明显强于普通解释，标为high。
- review_notes：source=meme_expansion; original_id=EXPAND_0010; generated_expansion; needs_human_review; original_primary=E2_时间节点触发; original_notes=generated_expansion; needs_human_review; meme_cluster=历史人物类比; context_audit_class=contextual_required; context_audit_class_code=C02; context_audit_flag_codes=F01; safety_binary=unsafe; safety_binary_code=B01; duplicate_text_status=same_text_different_context_review; duplicate_text_status_code=D02; preview_only=true

#### `MEME_EXPAND_0024_HIGH`

- 标签：risk_level=`high`；binary=`B01 / unsafe`；hard_negative=`false`
- 编码：primary=`F_组合编码`；secondary=`A2_拼音/首字母缩写；B4_符号/空格/Unicode 干扰`
- 上下文审计：class=`C02 / contextual_required`；flags=`F01`；duplicate=`D02 / same_text_different_context_review`
- context_required：`true`
- 上下文：
  - title：争议视频评论区
  - description：无
  - parent_comment（旧字段，默认不作强证据）：评论怎么少了一半
  - reply_chain（旧字段，默认不作强证据）：夸就完事了
  - time：2026-05-09
  - topic：历史人物类比
- 关键 reasoning：
  - supporting_evidence：文本含编码或规避表达。；上下文中的时间、回复链或话题提供独立支持。
  - counter_evidence：不直接还原具体目标名称；若脱离上下文，部分表达可能降级。
  - final_rationale：文本和上下文相互印证，风险解释明显强于普通解释，标为high。
- review_notes：source=meme_expansion; original_id=EXPAND_0024; generated_expansion; needs_human_review; original_primary=F_组合编码; original_notes=generated_expansion; needs_human_review; meme_cluster=历史人物类比; context_audit_class=contextual_required; context_audit_class_code=C02; context_audit_flag_codes=F01; safety_binary=unsafe; safety_binary_code=B01; duplicate_text_status=same_text_different_context_review; duplicate_text_status_code=D02; preview_only=true

- 复核结论：待填写

### 重复组 47

- 状态：`D02` / `same_text_different_context_review` / 同文同标签但不同上下文，待复核
- 出现次数：2
- 重复文本：这个朝代的改革失败，主要是财政和军制问题
- 风险分布：{"low": 2}
- 来源分布：{"meme_expansion": 2}
- 建议动作：看是否只是重复造句；如果上下文差异没有训练价值，建议删/重写/降权。

#### 本组怎么审

1. 先看文本本身是否足以判断。
2. 再比较标题、时间、话题等非回复链上下文是否真的不同。
3. 不要把合成的 `parent_comment/reply_chain` 当强证据。
4. 如果只是换标题/平台/泛泛场景，或靠假回复链撑风险，结论倾向 `删掉`、`退回重写` 或 `降权`。
5. 如果确实构成同文不同语境对照，结论可写 `保留对照`。

#### 涉及样本详情

#### `MEME_EXPAND_0067_LOW`

- 标签：risk_level=`low`；binary=`B01 / unsafe`；hard_negative=`true`
- 编码：primary=`C4_典故/物品/符号借用`；secondary=`无`
- 上下文审计：class=`C02 / contextual_required`；flags=`none`；duplicate=`D02 / same_text_different_context_review`
- context_required：`true`
- 上下文：
  - title：日常生活分享
  - description：无
  - parent_comment（旧字段，默认不作强证据）：只是普通记录
  - reply_chain（旧字段，默认不作强证据）：别过度联想
  - time：2026-06-04
  - topic：历史事件影射
- 关键 reasoning：
  - supporting_evidence：存在关键词、缩写、数字或符号撞车。
  - counter_evidence：上下文提供普通生活、教学、娱乐或技术解释。；缺少规避意图、目标映射或敏感语境。
  - final_rationale：普通解释更强，仅保留低风险或困难负样本价值，标为low。
- review_notes：source=meme_expansion; original_id=EXPAND_0067; generated_expansion; needs_human_review; original_primary=C4_典故/物品/符号借用; original_notes=generated_expansion; needs_human_review; meme_cluster=历史事件影射; context_audit_class=contextual_required; context_audit_class_code=C02; context_audit_flag_codes=none; safety_binary=unsafe; safety_binary_code=B01; duplicate_text_status=same_text_different_context_review; duplicate_text_status_code=D02; preview_only=true

#### `MEME_EXPAND_0081_LOW`

- 标签：risk_level=`low`；binary=`B01 / unsafe`；hard_negative=`true`
- 编码：primary=`D1_反讽`；secondary=`E3_回复链/互动触发`
- 上下文审计：class=`C02 / contextual_required`；flags=`F01`；duplicate=`D02 / same_text_different_context_review`
- context_required：`true`
- 上下文：
  - title：美食/文具/娱乐分享
  - description：无
  - parent_comment（旧字段，默认不作强证据）：求链接
  - reply_chain（旧字段，默认不作强证据）：只讨论字面对象
  - time：2026-05-05
  - topic：历史事件影射
- 关键 reasoning：
  - supporting_evidence：存在关键词、缩写、数字或符号撞车。
  - counter_evidence：上下文提供普通生活、教学、娱乐或技术解释。；缺少规避意图、目标映射或敏感语境。
  - final_rationale：普通解释更强，仅保留低风险或困难负样本价值，标为low。
- review_notes：source=meme_expansion; original_id=EXPAND_0081; generated_expansion; needs_human_review; original_primary=D1_反讽; original_notes=generated_expansion; needs_human_review; meme_cluster=历史事件影射; context_audit_class=contextual_required; context_audit_class_code=C02; context_audit_flag_codes=F01; safety_binary=unsafe; safety_binary_code=B01; duplicate_text_status=same_text_different_context_review; duplicate_text_status_code=D02; preview_only=true

- 复核结论：待填写

### 重复组 48

- 状态：`D02` / `same_text_different_context_review` / 同文同标签但不同上下文，待复核
- 出现次数：2
- 重复文本：这剧里的末代掌舵人，怎么越看越像今天的某些人
- 风险分布：{"high": 2}
- 来源分布：{"meme_expansion": 2}
- 建议动作：看是否只是重复造句；如果上下文差异没有训练价值，建议删/重写/降权。

#### 本组怎么审

1. 先看文本本身是否足以判断。
2. 再比较标题、时间、话题等非回复链上下文是否真的不同。
3. 不要把合成的 `parent_comment/reply_chain` 当强证据。
4. 如果只是换标题/平台/泛泛场景，或靠假回复链撑风险，结论倾向 `删掉`、`退回重写` 或 `降权`。
5. 如果确实构成同文不同语境对照，结论可写 `保留对照`。

#### 涉及样本详情

#### `MEME_EXPAND_0003_HIGH`

- 标签：risk_level=`high`；binary=`B01 / unsafe`；hard_negative=`false`
- 编码：primary=`C1_历史人物类比`；secondary=`E3_回复链/互动触发`
- 上下文审计：class=`C02 / contextual_required`；flags=`F01`；duplicate=`D02 / same_text_different_context_review`
- context_required：`true`
- 上下文：
  - title：争议视频评论区
  - description：无
  - parent_comment（旧字段，默认不作强证据）：评论怎么少了一半
  - reply_chain（旧字段，默认不作强证据）：夸就完事了
  - time：2026-05-09
  - topic：历史人物类比
- 关键 reasoning：
  - supporting_evidence：文本含编码或规避表达。；上下文中的时间、回复链或话题提供独立支持。
  - counter_evidence：不直接还原具体目标名称；若脱离上下文，部分表达可能降级。
  - final_rationale：文本和上下文相互印证，风险解释明显强于普通解释，标为high。
- review_notes：source=meme_expansion; original_id=EXPAND_0003; generated_expansion; needs_human_review; original_primary=B1_拆字; original_notes=generated_expansion; needs_human_review; meme_cluster=历史人物类比; context_audit_class=contextual_required; context_audit_class_code=C02; context_audit_flag_codes=F01; safety_binary=unsafe; safety_binary_code=B01; duplicate_text_status=same_text_different_context_review; duplicate_text_status_code=D02; preview_only=true

#### `MEME_EXPAND_0017_HIGH`

- 标签：risk_level=`high`；binary=`B01 / unsafe`；hard_negative=`false`
- 编码：primary=`C3_数字代指`；secondary=`E2_时间节点触发`
- 上下文审计：class=`C02 / contextual_required`；flags=`F01`；duplicate=`D02 / same_text_different_context_review`
- context_required：`true`
- 上下文：
  - title：旧照片转发
  - description：无
  - parent_comment（旧字段，默认不作强证据）：这几天别发全日期
  - reply_chain（旧字段，默认不作强证据）：别补具体名
  - time：2026-06-03
  - topic：历史人物类比
- 关键 reasoning：
  - supporting_evidence：文本含编码或规避表达。；上下文中的时间、回复链或话题提供独立支持。
  - counter_evidence：不直接还原具体目标名称；若脱离上下文，部分表达可能降级。
  - final_rationale：文本和上下文相互印证，风险解释明显强于普通解释，标为high。
- review_notes：source=meme_expansion; original_id=EXPAND_0017; generated_expansion; needs_human_review; original_primary=C3_数字代指; original_notes=generated_expansion; needs_human_review; meme_cluster=历史人物类比; context_audit_class=contextual_required; context_audit_class_code=C02; context_audit_flag_codes=F01; safety_binary=unsafe; safety_binary_code=B01; duplicate_text_status=same_text_different_context_review; duplicate_text_status_code=D02; preview_only=true

- 复核结论：待填写

### 重复组 49

- 状态：`D02` / `same_text_different_context_review` / 同文同标签但不同上下文，待复核
- 出现次数：2
- 重复文本：这是正常明史课程，不涉及现实类比
- 风险分布：{"none": 2}
- 来源分布：{"meme_expansion": 2}
- 建议动作：看是否只是重复造句；如果上下文差异没有训练价值，建议删/重写/降权。

#### 本组怎么审

1. 先看文本本身是否足以判断。
2. 再比较标题、时间、话题等非回复链上下文是否真的不同。
3. 不要把合成的 `parent_comment/reply_chain` 当强证据。
4. 如果只是换标题/平台/泛泛场景，或靠假回复链撑风险，结论倾向 `删掉`、`退回重写` 或 `降权`。
5. 如果确实构成同文不同语境对照，结论可写 `保留对照`。

#### 涉及样本详情

#### `MEME_EXPAND_0094_NONE`

- 标签：risk_level=`none`；binary=`B02 / safe`；hard_negative=`true`
- 编码：primary=`none`；secondary=`无`
- 上下文审计：class=`C03 / safe_without_context`；flags=`F01+F04`；duplicate=`D02 / same_text_different_context_review`
- context_required：`true`
- 上下文：
  - title：普通生活帖
  - description：无
  - parent_comment（旧字段，默认不作强证据）：字面场景明确
  - reply_chain（旧字段，默认不作强证据）：无异常互动
  - time：2026-06-04
  - topic：历史人物类比
- 关键 reasoning：
  - supporting_evidence：无
  - counter_evidence：上下文明确指向普通生活、学习、商品、娱乐或技术场景。；没有规避检测意图、隐含目标或异常互动共识。；相关词语可由字面含义充分解释。
  - final_rationale：反证充分，风险解释不成立，标为none。
- review_notes：source=meme_expansion; original_id=EXPAND_0094; generated_expansion; needs_human_review; original_primary=B1_拆字; original_notes=generated_expansion; needs_human_review; meme_cluster=历史人物类比; context_audit_class=safe_without_context; context_audit_class_code=C03; context_audit_flag_codes=F01+F04; safety_binary=safe; safety_binary_code=B02; duplicate_text_status=same_text_different_context_review; duplicate_text_status_code=D02; preview_only=true

#### `MEME_EXPAND_0108_NONE`

- 标签：risk_level=`none`；binary=`B02 / safe`；hard_negative=`true`
- 编码：primary=`none`；secondary=`无`
- 上下文审计：class=`C03 / safe_without_context`；flags=`F01+F04`；duplicate=`D02 / same_text_different_context_review`
- context_required：`true`
- 上下文：
  - title：商品/美食测评
  - description：无
  - parent_comment（旧字段，默认不作强证据）：只讨论购买和使用体验
  - reply_chain（旧字段，默认不作强证据）：没有隐含目标
  - time：2026-05-05
  - topic：历史人物类比
- 关键 reasoning：
  - supporting_evidence：无
  - counter_evidence：上下文明确指向普通生活、学习、商品、娱乐或技术场景。；没有规避检测意图、隐含目标或异常互动共识。；相关词语可由字面含义充分解释。
  - final_rationale：反证充分，风险解释不成立，标为none。
- review_notes：source=meme_expansion; original_id=EXPAND_0108; generated_expansion; needs_human_review; original_primary=E3_回复链/互动触发; original_notes=generated_expansion; needs_human_review; meme_cluster=历史人物类比; context_audit_class=safe_without_context; context_audit_class_code=C03; context_audit_flag_codes=F01+F04; safety_binary=safe; safety_binary_code=B02; duplicate_text_status=same_text_different_context_review; duplicate_text_status_code=D02; preview_only=true

- 复核结论：待填写

### 重复组 50

- 状态：`D02` / `same_text_different_context_review` / 同文同标签但不同上下文，待复核
- 出现次数：2
- 重复文本：这波操作太英明了，真是在夸修图教程
- 风险分布：{"low": 2}
- 来源分布：{"meme_expansion": 2}
- 建议动作：看是否只是重复造句；如果上下文差异没有训练价值，建议删/重写/降权。

#### 本组怎么审

1. 先看文本本身是否足以判断。
2. 再比较标题、时间、话题等非回复链上下文是否真的不同。
3. 不要把合成的 `parent_comment/reply_chain` 当强证据。
4. 如果只是换标题/平台/泛泛场景，或靠假回复链撑风险，结论倾向 `删掉`、`退回重写` 或 `降权`。
5. 如果确实构成同文不同语境对照，结论可写 `保留对照`。

#### 涉及样本详情

#### `MEME_EXPAND_0069_LOW`

- 标签：risk_level=`low`；binary=`B01 / unsafe`；hard_negative=`true`
- 编码：primary=`D1_反讽`；secondary=`E1_平台黑话`
- 上下文审计：class=`C02 / contextual_required`；flags=`F01`；duplicate=`D02 / same_text_different_context_review`
- context_required：`true`
- 上下文：
  - title：美食/文具/娱乐分享
  - description：无
  - parent_comment（旧字段，默认不作强证据）：求链接
  - reply_chain（旧字段，默认不作强证据）：只讨论字面对象
  - time：2026-05-05
  - topic：反讽/阴阳怪气
- 关键 reasoning：
  - supporting_evidence：存在关键词、缩写、数字或符号撞车。
  - counter_evidence：上下文提供普通生活、教学、娱乐或技术解释。；缺少规避意图、目标映射或敏感语境。
  - final_rationale：普通解释更强，仅保留低风险或困难负样本价值，标为low。
- review_notes：source=meme_expansion; original_id=EXPAND_0069; generated_expansion; needs_human_review; original_primary=A2_拼音/首字母缩写; original_notes=generated_expansion; needs_human_review; meme_cluster=反讽/阴阳怪气; context_audit_class=contextual_required; context_audit_class_code=C02; context_audit_flag_codes=F01; safety_binary=unsafe; safety_binary_code=B01; duplicate_text_status=same_text_different_context_review; duplicate_text_status_code=D02; preview_only=true

#### `MEME_EXPAND_0083_LOW`

- 标签：risk_level=`low`；binary=`B01 / unsafe`；hard_negative=`true`
- 编码：primary=`C2_历史事件影射`；secondary=`无`
- 上下文审计：class=`C02 / contextual_required`；flags=`none`；duplicate=`D02 / same_text_different_context_review`
- context_required：`true`
- 上下文：
  - title：教学/教程评论区
  - description：无
  - parent_comment（旧字段，默认不作强证据）：讨论的是具体技巧
  - reply_chain（旧字段，默认不作强证据）：普通解释更强
  - time：2026-03-16
  - topic：反讽/阴阳怪气
- 关键 reasoning：
  - supporting_evidence：存在关键词、缩写、数字或符号撞车。
  - counter_evidence：上下文提供普通生活、教学、娱乐或技术解释。；缺少规避意图、目标映射或敏感语境。
  - final_rationale：普通解释更强，仅保留低风险或困难负样本价值，标为low。
- review_notes：source=meme_expansion; original_id=EXPAND_0083; generated_expansion; needs_human_review; original_primary=C2_历史事件影射; original_notes=generated_expansion; needs_human_review; meme_cluster=反讽/阴阳怪气; context_audit_class=contextual_required; context_audit_class_code=C02; context_audit_flag_codes=none; safety_binary=unsafe; safety_binary_code=B01; duplicate_text_status=same_text_different_context_review; duplicate_text_status_code=D02; preview_only=true

- 复核结论：待填写

### 重复组 51

- 状态：`D02` / `same_text_different_context_review` / 同文同标签但不同上下文，待复核
- 出现次数：2
- 重复文本：这部历史剧的末代皇帝演得不错
- 风险分布：{"low": 2}
- 来源分布：{"meme_expansion": 2}
- 建议动作：看是否只是重复造句；如果上下文差异没有训练价值，建议删/重写/降权。

#### 本组怎么审

1. 先看文本本身是否足以判断。
2. 再比较标题、时间、话题等非回复链上下文是否真的不同。
3. 不要把合成的 `parent_comment/reply_chain` 当强证据。
4. 如果只是换标题/平台/泛泛场景，或靠假回复链撑风险，结论倾向 `删掉`、`退回重写` 或 `降权`。
5. 如果确实构成同文不同语境对照，结论可写 `保留对照`。

#### 涉及样本详情

#### `MEME_EXPAND_0066_LOW`

- 标签：risk_level=`low`；binary=`B01 / unsafe`；hard_negative=`true`
- 编码：primary=`C4_典故/物品/符号借用`；secondary=`无`
- 上下文审计：class=`C02 / contextual_required`；flags=`F01`；duplicate=`D02 / same_text_different_context_review`
- context_required：`true`
- 上下文：
  - title：美食/文具/娱乐分享
  - description：无
  - parent_comment（旧字段，默认不作强证据）：求链接
  - reply_chain（旧字段，默认不作强证据）：只讨论字面对象
  - time：2026-05-05
  - topic：历史人物类比
- 关键 reasoning：
  - supporting_evidence：存在关键词、缩写、数字或符号撞车。
  - counter_evidence：上下文提供普通生活、教学、娱乐或技术解释。；缺少规避意图、目标映射或敏感语境。
  - final_rationale：普通解释更强，仅保留低风险或困难负样本价值，标为low。
- review_notes：source=meme_expansion; original_id=EXPAND_0066; generated_expansion; needs_human_review; original_primary=C4_典故/物品/符号借用; original_notes=generated_expansion; needs_human_review; meme_cluster=历史人物类比; context_audit_class=contextual_required; context_audit_class_code=C02; context_audit_flag_codes=F01; safety_binary=unsafe; safety_binary_code=B01; duplicate_text_status=same_text_different_context_review; duplicate_text_status_code=D02; preview_only=true

#### `MEME_EXPAND_0080_LOW`

- 标签：risk_level=`low`；binary=`B01 / unsafe`；hard_negative=`true`
- 编码：primary=`D1_反讽`；secondary=`无`
- 上下文审计：class=`C02 / contextual_required`；flags=`none`；duplicate=`D02 / same_text_different_context_review`
- context_required：`true`
- 上下文：
  - title：教学/教程评论区
  - description：无
  - parent_comment（旧字段，默认不作强证据）：讨论的是具体技巧
  - reply_chain（旧字段，默认不作强证据）：普通解释更强
  - time：2026-03-16
  - topic：历史人物类比
- 关键 reasoning：
  - supporting_evidence：存在关键词、缩写、数字或符号撞车。
  - counter_evidence：上下文提供普通生活、教学、娱乐或技术解释。；缺少规避意图、目标映射或敏感语境。
  - final_rationale：普通解释更强，仅保留低风险或困难负样本价值，标为low。
- review_notes：source=meme_expansion; original_id=EXPAND_0080; generated_expansion; needs_human_review; original_primary=D1_反讽; original_notes=generated_expansion; needs_human_review; meme_cluster=历史人物类比; context_audit_class=contextual_required; context_audit_class_code=C02; context_audit_flag_codes=none; safety_binary=unsafe; safety_binary_code=B01; duplicate_text_status=same_text_different_context_review; duplicate_text_status_code=D02; preview_only=true

- 复核结论：待填写

### 重复组 52

- 状态：`D02` / `same_text_different_context_review` / 同文同标签但不同上下文，待复核
- 出现次数：2
- 重复文本：这部历史纪录片讲的是史料争议，不涉及现实类比
- 风险分布：{"none": 2}
- 来源分布：{"meme_expansion": 2}
- 建议动作：看是否只是重复造句；如果上下文差异没有训练价值，建议删/重写/降权。

#### 本组怎么审

1. 先看文本本身是否足以判断。
2. 再比较标题、时间、话题等非回复链上下文是否真的不同。
3. 不要把合成的 `parent_comment/reply_chain` 当强证据。
4. 如果只是换标题/平台/泛泛场景，或靠假回复链撑风险，结论倾向 `删掉`、`退回重写` 或 `降权`。
5. 如果确实构成同文不同语境对照，结论可写 `保留对照`。

#### 涉及样本详情

#### `MEME_EXPAND_0102_NONE`

- 标签：risk_level=`none`；binary=`B02 / safe`；hard_negative=`true`
- 编码：primary=`none`；secondary=`无`
- 上下文审计：class=`C03 / safe_without_context`；flags=`F01+F04`；duplicate=`D02 / same_text_different_context_review`
- context_required：`true`
- 上下文：
  - title：商品/美食测评
  - description：无
  - parent_comment（旧字段，默认不作强证据）：只讨论购买和使用体验
  - reply_chain（旧字段，默认不作强证据）：没有隐含目标
  - time：2026-05-05
  - topic：历史事件影射
- 关键 reasoning：
  - supporting_evidence：无
  - counter_evidence：上下文明确指向普通生活、学习、商品、娱乐或技术场景。；没有规避检测意图、隐含目标或异常互动共识。；相关词语可由字面含义充分解释。
  - final_rationale：反证充分，风险解释不成立，标为none。
- review_notes：source=meme_expansion; original_id=EXPAND_0102; generated_expansion; needs_human_review; original_primary=A2_拼音/首字母缩写; original_notes=generated_expansion; needs_human_review; meme_cluster=历史事件影射; context_audit_class=safe_without_context; context_audit_class_code=C03; context_audit_flag_codes=F01+F04; safety_binary=safe; safety_binary_code=B02; duplicate_text_status=same_text_different_context_review; duplicate_text_status_code=D02; preview_only=true

#### `MEME_EXPAND_0116_NONE`

- 标签：risk_level=`none`；binary=`B02 / safe`；hard_negative=`true`
- 编码：primary=`none`；secondary=`无`
- 上下文审计：class=`C03 / safe_without_context`；flags=`F01+F04`；duplicate=`D02 / same_text_different_context_review`
- context_required：`true`
- 上下文：
  - title：课程/教程内容
  - description：无
  - parent_comment（旧字段，默认不作强证据）：讨论学习或技术问题
  - reply_chain（旧字段，默认不作强证据）：上下文支持普通解释
  - time：2026-03-06
  - topic：历史事件影射
- 关键 reasoning：
  - supporting_evidence：无
  - counter_evidence：上下文明确指向普通生活、学习、商品、娱乐或技术场景。；没有规避检测意图、隐含目标或异常互动共识。；相关词语可由字面含义充分解释。
  - final_rationale：反证充分，风险解释不成立，标为none。
- review_notes：source=meme_expansion; original_id=EXPAND_0116; generated_expansion; needs_human_review; original_primary=F_组合编码; original_notes=generated_expansion; needs_human_review; meme_cluster=历史事件影射; context_audit_class=safe_without_context; context_audit_class_code=C03; context_audit_flag_codes=F01+F04; safety_binary=safe; safety_binary_code=B02; duplicate_text_status=same_text_different_context_review; duplicate_text_status_code=D02; preview_only=true

- 复核结论：待填写

### 重复组 53

- 状态：`D02` / `same_text_different_context_review` / 同文同标签但不同上下文，待复核
- 出现次数：2
- 重复文本：香薰蜡烛真的能提升睡眠氛围
- 风险分布：{"none": 2}
- 来源分布：{"meme_expansion": 2}
- 建议动作：看是否只是重复造句；如果上下文差异没有训练价值，建议删/重写/降权。

#### 本组怎么审

1. 先看文本本身是否足以判断。
2. 再比较标题、时间、话题等非回复链上下文是否真的不同。
3. 不要把合成的 `parent_comment/reply_chain` 当强证据。
4. 如果只是换标题/平台/泛泛场景，或靠假回复链撑风险，结论倾向 `删掉`、`退回重写` 或 `降权`。
5. 如果确实构成同文不同语境对照，结论可写 `保留对照`。

#### 涉及样本详情

#### `MEME_EXPAND_0096_NONE`

- 标签：risk_level=`none`；binary=`B02 / safe`；hard_negative=`true`
- 编码：primary=`none`；secondary=`无`
- 上下文审计：class=`C03 / safe_without_context`；flags=`F01+F04`；duplicate=`D02 / same_text_different_context_review`
- context_required：`true`
- 上下文：
  - title：商品/美食测评
  - description：无
  - parent_comment（旧字段，默认不作强证据）：只讨论购买和使用体验
  - reply_chain（旧字段，默认不作强证据）：没有隐含目标
  - time：2026-05-05
  - topic：食物/品牌/物品隐喻
- 关键 reasoning：
  - supporting_evidence：无
  - counter_evidence：上下文明确指向普通生活、学习、商品、娱乐或技术场景。；没有规避检测意图、隐含目标或异常互动共识。；相关词语可由字面含义充分解释。
  - final_rationale：反证充分，风险解释不成立，标为none。
- review_notes：source=meme_expansion; original_id=EXPAND_0096; generated_expansion; needs_human_review; original_primary=C4_典故/物品/符号借用; original_notes=generated_expansion; needs_human_review; meme_cluster=食物/品牌/物品隐喻; context_audit_class=safe_without_context; context_audit_class_code=C03; context_audit_flag_codes=F01+F04; safety_binary=safe; safety_binary_code=B02; duplicate_text_status=same_text_different_context_review; duplicate_text_status_code=D02; preview_only=true

#### `MEME_EXPAND_0110_NONE`

- 标签：risk_level=`none`；binary=`B02 / safe`；hard_negative=`true`
- 编码：primary=`none`；secondary=`无`
- 上下文审计：class=`C03 / safe_without_context`；flags=`F01+F04`；duplicate=`D02 / same_text_different_context_review`
- context_required：`true`
- 上下文：
  - title：课程/教程内容
  - description：无
  - parent_comment（旧字段，默认不作强证据）：讨论学习或技术问题
  - reply_chain（旧字段，默认不作强证据）：上下文支持普通解释
  - time：2026-03-06
  - topic：食物/品牌/物品隐喻
- 关键 reasoning：
  - supporting_evidence：无
  - counter_evidence：上下文明确指向普通生活、学习、商品、娱乐或技术场景。；没有规避检测意图、隐含目标或异常互动共识。；相关词语可由字面含义充分解释。
  - final_rationale：反证充分，风险解释不成立，标为none。
- review_notes：source=meme_expansion; original_id=EXPAND_0110; generated_expansion; needs_human_review; original_primary=C4_典故/物品/符号借用; original_notes=generated_expansion; needs_human_review; meme_cluster=食物/品牌/物品隐喻; context_audit_class=safe_without_context; context_audit_class_code=C03; context_audit_flag_codes=F01+F04; safety_binary=safe; safety_binary_code=B02; duplicate_text_status=same_text_different_context_review; duplicate_text_status_code=D02; preview_only=true

- 复核结论：待填写
