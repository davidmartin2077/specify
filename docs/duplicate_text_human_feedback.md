# 重复文本人工复核反馈

本文件记录用户对 `docs/duplicate_text_review.md` 中 53 个重复文本组的人工复核结论。

本反馈只作为清洗依据，不直接修改正式 `data/processed/combined_candidates.*`。

## 总体倾向

- 复核组数：53
- 删除/排除倾向：21 组
- 重写倾向：3 组
- 保留但改标签倾向：13 组
- 保留或留一条倾向：16 组

## 主要复核原则

1. 合成回复链不再作为强证据，风险主要靠回复链成立的样本按模板污染处理。
2. `nb`、`64`、`卖车包子` 这类评论本身可读、有真实评论感的样本可以保留或重写。
3. 病句、审核员视角、说明书式陈述句、模板化上下文优先删除、重写或降权。
4. 重复文本不必全留，很多组只留一个代表样本即可。

## 决策分布

| decision | count |
|---|---:|
| `delete_group` / 整组删除/不进入高质量训练集 | 17 |
| `keep_one` / 留一条 | 7 |
| `keep_one_delete_duplicates` / 留一条，删除重复项 | 4 |
| `keep_one_relabel_none` / 留一条，改 none | 4 |
| `delete_or_rewrite` / 删除或重写 | 3 |
| `keep_one_relabel_high` / 留一条，改 high | 2 |
| `keep_group` / 保留 | 2 |
| `rewrite_keep_one` / 退回重写，最多保留一条 | 1 |
| `keep_relabel_medium_or_high` / 保留，标签可调 medium/high | 1 |
| `delete_or_relabel_none_low` / 删除，或仅作 none/low 边界 | 1 |
| `keep_relabel_high_no_context` / 保留，改 high，不需要上下文 | 1 |
| `keep_relabel_medium_no_context` / 保留，改 medium，不需要上下文 | 1 |
| `keep_relabel_high_style_issue` / 保留或重写风格，风险可 high | 1 |
| `keep_one_style_statement` / 留一条，但注意陈述句风格 | 1 |
| `keep_one_high` / 留一条，高风险 | 1 |
| `keep_one_relabel_high_no_reasoning_needed` / 留一条，直接 high | 1 |
| `keep_relabel_none` / 保留，改 none | 1 |
| `rewrite_group` / 整组重写 | 1 |
| `keep_one_relabel_medium_or_high_style_statement` / 留一条，可改 medium/high，但注意陈述句风格 | 1 |
| `keep_group_style_statement` / 保留，但注意陈述句风格 | 1 |
| `rewrite_style_statement` / 重写陈述句风格 | 1 |

## 逐组反馈

### 重复组 01

- 重复文本：NB 是 New Balance 的鞋款缩写，不是别的意思
- 样本 ID：`MEME_EXPAND_0091_NONE`, `MEME_EXPAND_0105_NONE`, `MEME_EXPAND_0119_NONE`
- 原审计：`D02` / `same_text_different_context_review`
- 风险分布：{"none": 3}
- 人工结论：`rewrite_keep_one` / 退回重写，最多保留一条
- 归一动作：`rewrite`
- 用户反馈：退回重写，且保留一条就够了。nb 是鞋款本身就是在对 nb 做解释，文本可以变成“这块 nb 真好看”，然后解读 nb 对意思，也就是这里出现的是审核视角的词，并非评论本身。其实这个例子很好，nb 可以理解成牛逼，可以理解成新百伦，但就是样例不太行。

### 重复组 02

- 重复文本：一到这个日期，连普通蜡烛视频都有人刷懂
- 样本 ID：`MEME_EXPAND_0026_MEDIUM`, `MEME_EXPAND_0040_MEDIUM`, `MEME_EXPAND_0054_MEDIUM`
- 原审计：`D03` / `template_pollution_candidate`
- 风险分布：{"medium": 3}
- 人工结论：`delete_group` / 整组删除/不进入高质量训练集
- 归一动作：`delete_or_exclude`
- 用户反馈：模板污染了，删。

### 重复组 03

- 重复文本：今天买了白纸，做手账真的很好用
- 样本 ID：`MEME_EXPAND_0061_LOW`, `MEME_EXPAND_0075_LOW`, `MEME_EXPAND_0089_LOW`
- 原审计：`D03` / `template_pollution_candidate`
- 风险分布：{"low": 3}
- 人工结论：`keep_one_delete_duplicates` / 留一条，删除重复项
- 归一动作：`keep_or_keep_one`
- 用户反馈：评论很好，但是上下文重复，删掉两个保留一个。

### 重复组 04

- 重复文本：他说‘35号见’，不像普通约饭，但也没更多上下文
- 样本 ID：`MEME_EXPAND_0030_MEDIUM`, `MEME_EXPAND_0044_MEDIUM`, `MEME_EXPAND_0058_MEDIUM`
- 原审计：`D03` / `template_pollution_candidate`
- 风险分布：{"medium": 3}
- 人工结论：`delete_group` / 整组删除/不进入高质量训练集
- 归一动作：`delete_or_exclude`
- 用户反馈：模板污染，没有营养的训练，删掉。

### 重复组 05

- 重复文本：倒车镜调低一点更适合我身高
- 样本 ID：`MEME_EXPAND_0092_NONE`, `MEME_EXPAND_0106_NONE`, `MEME_EXPAND_0120_NONE`
- 原审计：`D02` / `same_text_different_context_review`
- 风险分布：{"none": 3}
- 人工结论：`keep_one_delete_duplicates` / 留一条，删除重复项
- 归一动作：`keep_or_keep_one`
- 用户反馈：删 2 留 1。

### 重复组 06

- 重复文本：单条懂没信息，但接在删前留名后就变味了
- 样本 ID：`MEME_EXPAND_0028_MEDIUM`, `MEME_EXPAND_0042_MEDIUM`, `MEME_EXPAND_0056_MEDIUM`
- 原审计：`D03` / `template_pollution_candidate`
- 风险分布：{"medium": 3}
- 人工结论：`delete_group` / 整组删除/不进入高质量训练集
- 归一动作：`delete_or_exclude`
- 用户反馈：模板污染，都不要。

### 重复组 07

- 重复文本：大家都说历史重演，但没有说明映射到哪件事
- 样本 ID：`MEME_EXPAND_0032_MEDIUM`, `MEME_EXPAND_0046_MEDIUM`, `MEME_EXPAND_0060_MEDIUM`
- 原审计：`D03` / `template_pollution_candidate`
- 风险分布：{"medium": 3}
- 人工结论：`delete_group` / 整组删除/不进入高质量训练集
- 归一动作：`delete_or_exclude`
- 用户反馈：不要了，质量不高。

### 重复组 08

- 重复文本：这个末代角色被剪成现实感很强的混剪
- 样本 ID：`MEME_EXPAND_0031_MEDIUM`, `MEME_EXPAND_0045_MEDIUM`, `MEME_EXPAND_0059_MEDIUM`
- 原审计：`D03` / `template_pollution_candidate`
- 风险分布：{"medium": 3}
- 人工结论：`delete_group` / 整组删除/不进入高质量训练集
- 归一动作：`delete_or_exclude`
- 用户反馈：病句，不要。

### 重复组 09

- 重复文本：这句感谢安排配上翻车现场，像阴阳但对象不明
- 样本 ID：`MEME_EXPAND_0027_MEDIUM`, `MEME_EXPAND_0041_MEDIUM`, `MEME_EXPAND_0055_MEDIUM`
- 原审计：`D02` / `same_text_different_context_review`
- 风险分布：{"medium": 3}
- 人工结论：`delete_or_rewrite` / 删除或重写
- 归一动作：`delete_or_exclude`
- 用户反馈：审核员视角，且模板污染。

### 重复组 10

- 重复文本：这司机又说为了大家好，结果油门没松过
- 样本 ID：`MEME_EXPAND_0029_MEDIUM`, `MEME_EXPAND_0043_MEDIUM`, `MEME_EXPAND_0057_MEDIUM`
- 原审计：`D03` / `template_pollution_candidate`
- 风险分布：{"medium": 3}
- 人工结论：`keep_relabel_medium_or_high` / 保留，标签可调 medium/high
- 归一动作：`keep_with_label_change`
- 用户反馈：上下文没意义，评论本身很有意思，留着，判断为 medium 甚至 high 都没问题。

### 重复组 11

- 重复文本：这游戏优化真棒，卡成PPT
- 样本 ID：`MEME_EXPAND_0062_LOW`, `MEME_EXPAND_0076_LOW`, `MEME_EXPAND_0090_LOW`
- 原审计：`D03` / `template_pollution_candidate`
- 风险分布：{"low": 3}
- 人工结论：`delete_or_relabel_none_low` / 删除，或仅作 none/low 边界
- 归一动作：`delete_or_exclude`
- 用户反馈：模板污染，判 none 或者 low 都没问题。

### 重复组 12

- 重复文本：64号选手这把打得不错
- 样本 ID：`MEME_EXPAND_0072_LOW`, `MEME_EXPAND_0086_LOW`
- 原审计：`D02` / `same_text_different_context_review`
- 风险分布：{"low": 2}
- 人工结论：`keep_one_delete_duplicates` / 留一条，删除重复项
- 归一动作：`keep_or_keep_one`
- 用户反馈：没什么问题，删除重复的，留一组。

### 重复组 13

- 重复文本：nb 这个缩写我只想说牛，别过度解读
- 样本 ID：`MEME_EXPAND_0063_LOW`, `MEME_EXPAND_0077_LOW`
- 原审计：`D02` / `same_text_different_context_review`
- 风险分布：{"low": 2}
- 人工结论：`delete_group` / 整组删除/不进入高质量训练集
- 归一动作：`delete_or_exclude`
- 用户反馈：质量不高，删了吧。

### 重复组 14

- 重复文本：五月多出来的那几天，大家都学会闭麦了
- 样本 ID：`MEME_EXPAND_0037_MEDIUM`, `MEME_EXPAND_0051_MEDIUM`
- 原审计：`D02` / `same_text_different_context_review`
- 风险分布：{"medium": 2}
- 人工结论：`keep_relabel_high_no_context` / 保留，改 high，不需要上下文
- 归一动作：`keep_with_label_change`
- 用户反馈：评论很有意思，但是上下文之类的可以不带，这个可以判 high 了，一眼都知道 64。

### 重复组 15

- 重复文本：今晚只发旧日历，不写具体日期
- 样本 ID：`MEME_EXPAND_0009_HIGH`, `MEME_EXPAND_0023_HIGH`
- 原审计：`D02` / `same_text_different_context_review`
- 风险分布：{"high": 2}
- 人工结论：`delete_group` / 整组删除/不进入高质量训练集
- 归一动作：`delete_or_exclude`
- 用户反馈：不要了，质量不高。

### 重复组 16

- 重复文本：他用某朝改革失败来类比今天，但证据只有一句话
- 样本 ID：`MEME_EXPAND_0038_MEDIUM`, `MEME_EXPAND_0052_MEDIUM`
- 原审计：`D02` / `same_text_different_context_review`
- 风险分布：{"medium": 2}
- 人工结论：`delete_group` / 整组删除/不进入高质量训练集
- 归一动作：`delete_or_exclude`
- 用户反馈：病句，不要。

### 重复组 17

- 重复文本：他这波真是英明神武，删评删到只剩彩虹屁
- 样本 ID：`MEME_EXPAND_0006_HIGH`, `MEME_EXPAND_0020_HIGH`
- 原审计：`D02` / `same_text_different_context_review`
- 风险分布：{"high": 2}
- 人工结论：`keep_one_relabel_high` / 留一条，改 high
- 归一动作：`keep_with_label_change`
- 用户反馈：直接辱党，直接判 high，留一个。

### 重复组 18

- 重复文本：倒车入库练了一下午，教练说我终于会看镜子了
- 样本 ID：`MEME_EXPAND_0064_LOW`, `MEME_EXPAND_0078_LOW`
- 原审计：`D02` / `same_text_different_context_review`
- 风险分布：{"low": 2}
- 人工结论：`keep_one_relabel_none` / 留一条，改 none
- 归一动作：`keep_with_label_change`
- 用户反馈：可以，但是判 none 就行，很日常的话。

### 重复组 19

- 重复文本：六月四号我生日，求祝福
- 样本 ID：`MEME_EXPAND_0065_LOW`, `MEME_EXPAND_0079_LOW`
- 原审计：`D02` / `same_text_different_context_review`
- 风险分布：{"low": 2}
- 人工结论：`keep_relabel_medium_no_context` / 保留，改 medium，不需要上下文
- 归一动作：`keep_with_label_change`
- 用户反馈：例子可以，但是这句话也不用看上下文。但是在评论区说弹幕莫名其妙说自己生日也挺抽象的，判个中吧。

### 重复组 20

- 重复文本：删前留名是抽奖梗，不是内容风险
- 样本 ID：`MEME_EXPAND_0070_LOW`, `MEME_EXPAND_0084_LOW`
- 原审计：`D02` / `same_text_different_context_review`
- 风险分布：{"low": 2}
- 人工结论：`delete_group` / 整组删除/不进入高质量训练集
- 归一动作：`delete_or_exclude`
- 用户反馈：质量不高，都不要了。

### 重复组 21

- 重复文本：别再刷 j c 了，今天这条时间线已经够明显
- 样本 ID：`MEME_EXPAND_0007_HIGH`, `MEME_EXPAND_0021_HIGH`
- 原审计：`D02` / `same_text_different_context_review`
- 风险分布：{"high": 2}
- 人工结论：`delete_group` / 整组删除/不进入高质量训练集
- 归一动作：`delete_or_exclude`
- 用户反馈：质量不高。

### 重复组 22

- 重复文本：别发全称，写成 g·c·q 就行，这句本身有规避味
- 样本 ID：`MEME_EXPAND_0035_MEDIUM`, `MEME_EXPAND_0049_MEDIUM`
- 原审计：`D02` / `same_text_different_context_review`
- 风险分布：{"medium": 2}
- 人工结论：`delete_or_rewrite` / 删除或重写
- 归一动作：`delete_or_exclude`
- 用户反馈：审核视角，建议不要或者重写。

### 重复组 23

- 重复文本：前面说那年夏天的别回了，楼已经被清过一轮
- 样本 ID：`MEME_EXPAND_0011_HIGH`, `MEME_EXPAND_0025_HIGH`
- 原审计：`D02` / `same_text_different_context_review`
- 风险分布：{"high": 2}
- 人工结论：`keep_one_delete_duplicates` / 留一条，删除重复项
- 归一动作：`keep_or_keep_one`
- 用户反馈：没什么问题，删 2 留 1。

### 重复组 24

- 重复文本：包子、茶杯和旧照片一起发，单看都正常
- 样本 ID：`MEME_EXPAND_0033_MEDIUM`, `MEME_EXPAND_0047_MEDIUM`
- 原审计：`D02` / `same_text_different_context_review`
- 风险分布：{"medium": 2}
- 人工结论：`delete_group` / 整组删除/不进入高质量训练集
- 归一动作：`delete_or_exclude`
- 用户反馈：质量不高。

### 重复组 25

- 重复文本：包子铺突然限评，大家却都在问馅儿是不是换了
- 样本 ID：`MEME_EXPAND_0005_HIGH`, `MEME_EXPAND_0019_HIGH`
- 原审计：`D02` / `same_text_different_context_review`
- 风险分布：{"high": 2}
- 人工结论：`keep_one` / 留一条
- 归一动作：`keep_or_keep_one`
- 用户反馈：很有意思一个评论，留 1 个。

### 重复组 26

- 重复文本：历史书翻到这一页，弹幕都在说熟悉的配方
- 样本 ID：`MEME_EXPAND_0004_HIGH`, `MEME_EXPAND_0018_HIGH`
- 原审计：`D02` / `same_text_different_context_review`
- 风险分布：{"high": 2}
- 人工结论：`keep_relabel_high_style_issue` / 保留或重写风格，风险可 high
- 归一动作：`keep_with_label_change`
- 用户反馈：像个陈述句，不像是出现在弹幕和评论里的话，但是本身判 high 没毛病。

### 重复组 27

- 重复文本：历史总是相似，这句是影评里的主题概括
- 样本 ID：`MEME_EXPAND_0074_LOW`, `MEME_EXPAND_0088_LOW`
- 原审计：`D02` / `same_text_different_context_review`
- 风险分布：{"low": 2}
- 人工结论：`keep_one` / 留一条
- 归一动作：`keep_or_keep_one`
- 用户反馈：没什么问题，留一个。

### 重复组 28

- 重复文本：历史重演是小说主题，不是在指现实事件
- 样本 ID：`MEME_EXPAND_0095_NONE`, `MEME_EXPAND_0109_NONE`
- 原审计：`D02` / `same_text_different_context_review`
- 风险分布：{"none": 2}
- 人工结论：`keep_one_style_statement` / 留一条，但注意陈述句风格
- 归一动作：`keep_or_keep_one`
- 用户反馈：陈述句，留一个。

### 重复组 29

- 重复文本：又到那个 5·35 的晚上，评论区自动静音
- 样本 ID：`MEME_EXPAND_0002_HIGH`, `MEME_EXPAND_0016_HIGH`
- 原审计：`D02` / `same_text_different_context_review`
- 风险分布：{"high": 2}
- 人工结论：`keep_one_high` / 留一条，高风险
- 归一动作：`keep_or_keep_one`
- 用户反馈：直接高风险，留一个。

### 重复组 30

- 重复文本：崇祯时期财政问题很复杂，不能只怪一个人
- 样本 ID：`MEME_EXPAND_0073_LOW`, `MEME_EXPAND_0087_LOW`
- 原审计：`D02` / `same_text_different_context_review`
- 风险分布：{"low": 2}
- 人工结论：`keep_one` / 留一条
- 归一动作：`keep_or_keep_one`
- 用户反馈：没什么问题，留一个。

### 重复组 31

- 重复文本：庆丰包子的素馅我觉得一般
- 样本 ID：`MEME_EXPAND_0103_NONE`, `MEME_EXPAND_0117_NONE`
- 原审计：`D02` / `same_text_different_context_review`
- 风险分布：{"none": 2}
- 人工结论：`keep_one_relabel_high_no_reasoning_needed` / 留一条，直接 high
- 归一动作：`keep_with_label_change`
- 用户反馈：看到卖车包子直接 high，不需要任何逻辑。

### 重复组 32

- 重复文本：感谢安排是婚礼流程顺利后的真诚感谢
- 样本 ID：`MEME_EXPAND_0097_NONE`, `MEME_EXPAND_0111_NONE`
- 原审计：`D02` / `same_text_different_context_review`
- 风险分布：{"none": 2}
- 人工结论：`delete_group` / 整组删除/不进入高质量训练集
- 归一动作：`delete_or_exclude`
- 用户反馈：病句，删了不要。

### 重复组 33

- 重复文本：我买了64色马克笔，做手账刚好够用
- 样本 ID：`MEME_EXPAND_0100_NONE`, `MEME_EXPAND_0114_NONE`
- 原审计：`D02` / `same_text_different_context_review`
- 风险分布：{"none": 2}
- 人工结论：`keep_one_relabel_none` / 留一条，改 none
- 归一动作：`keep_with_label_change`
- 用户反馈：判 none 没问题，留一个即可。

### 重复组 34

- 重复文本：末代皇帝的性格分析应放在当时制度背景里看
- 样本 ID：`MEME_EXPAND_0101_NONE`, `MEME_EXPAND_0115_NONE`
- 原审计：`D02` / `same_text_different_context_review`
- 风险分布：{"none": 2}
- 人工结论：`keep_group` / 保留
- 归一动作：`keep_or_keep_one`
- 用户反馈：没毛病。

### 重复组 35

- 重复文本：楼上说倒车，楼下接后视镜早拆了
- 样本 ID：`MEME_EXPAND_0036_MEDIUM`, `MEME_EXPAND_0050_MEDIUM`
- 原审计：`D02` / `same_text_different_context_review`
- 风险分布：{"medium": 2}
- 人工结论：`delete_group` / 整组删除/不进入高质量训练集
- 归一动作：`delete_or_exclude`
- 用户反馈：病句不要。

### 重复组 36

- 重复文本：楼上问司机是谁，楼下只回‘油门到底’
- 样本 ID：`MEME_EXPAND_0008_HIGH`, `MEME_EXPAND_0022_HIGH`
- 原审计：`D02` / `same_text_different_context_review`
- 风险分布：{"high": 2}
- 人工结论：`delete_group` / 整组删除/不进入高质量训练集
- 归一动作：`delete_or_exclude`
- 用户反馈：病句不要。

### 重复组 37

- 重复文本：河蟹真的好吃，清蒸就很鲜
- 样本 ID：`MEME_EXPAND_0068_LOW`, `MEME_EXPAND_0082_LOW`
- 原审计：`D02` / `same_text_different_context_review`
- 风险分布：{"low": 2}
- 人工结论：`keep_one_relabel_none` / 留一条，改 none
- 归一动作：`keep_with_label_change`
- 用户反馈：None 留一个。

### 重复组 38

- 重复文本：油门踩重了才熄火，驾考真的紧张
- 样本 ID：`MEME_EXPAND_0099_NONE`, `MEME_EXPAND_0113_NONE`
- 原审计：`D02` / `same_text_different_context_review`
- 风险分布：{"none": 2}
- 人工结论：`keep_one_relabel_none` / 留一条，改 none
- 归一动作：`keep_with_label_change`
- 用户反馈：None 留一个。

### 重复组 39

- 重复文本：符号分隔歌词是为了卡点，不是规避关键词
- 样本 ID：`MEME_EXPAND_0098_NONE`, `MEME_EXPAND_0112_NONE`
- 原审计：`D02` / `same_text_different_context_review`
- 风险分布：{"none": 2}
- 人工结论：`delete_or_rewrite` / 删除或重写
- 归一动作：`delete_or_exclude`
- 用户反馈：审核员语气，模板污染。

### 重复组 40

- 重复文本：第35页的公式推导有个笔误
- 样本 ID：`MEME_EXPAND_0093_NONE`, `MEME_EXPAND_0107_NONE`
- 原审计：`D02` / `same_text_different_context_review`
- 风险分布：{"none": 2}
- 人工结论：`keep_relabel_none` / 保留，改 none
- 归一动作：`keep_with_label_change`
- 用户反馈：直接判 none 没问题。

### 重复组 41

- 重复文本：老师英明是弹幕在夸讲题清楚
- 样本 ID：`MEME_EXPAND_0104_NONE`, `MEME_EXPAND_0118_NONE`
- 原审计：`D02` / `same_text_different_context_review`
- 风险分布：{"none": 2}
- 人工结论：`delete_group` / 整组删除/不进入高质量训练集
- 归一动作：`delete_or_exclude`
- 用户反馈：病句不要。

### 重复组 42

- 重复文本：英明两个字刷得太整齐，像反话又像真粉
- 样本 ID：`MEME_EXPAND_0034_MEDIUM`, `MEME_EXPAND_0048_MEDIUM`
- 原审计：`D02` / `same_text_different_context_review`
- 风险分布：{"medium": 2}
- 人工结论：`rewrite_group` / 整组重写
- 归一动作：`rewrite`
- 用户反馈：病句，重写，不像正常评论。

### 重复组 43

- 重复文本：视频讲的是历史课，弹幕却都在问现在呢
- 样本 ID：`MEME_EXPAND_0039_MEDIUM`, `MEME_EXPAND_0053_MEDIUM`
- 原审计：`D02` / `same_text_different_context_review`
- 风险分布：{"medium": 2}
- 人工结论：`keep_one_relabel_medium_or_high_style_statement` / 留一条，可改 medium/high，但注意陈述句风格
- 归一动作：`keep_with_label_change`
- 用户反馈：陈述句，但是评论本身可以当作中或者高，留一个。

### 重复组 44

- 重复文本：车开太快了，真的要检查刹车片
- 样本 ID：`MEME_EXPAND_0071_LOW`, `MEME_EXPAND_0085_LOW`
- 原审计：`D02` / `same_text_different_context_review`
- 风险分布：{"low": 2}
- 人工结论：`keep_group` / 保留
- 归一动作：`keep_or_keep_one`
- 用户反馈：没问题，留。

### 重复组 45

- 重复文本：车门焊死、油门踩满、倒车镜拆了，三件套齐活
- 样本 ID：`MEME_EXPAND_0001_HIGH`, `MEME_EXPAND_0015_HIGH`
- 原审计：`D02` / `same_text_different_context_review`
- 风险分布：{"high": 2}
- 人工结论：`keep_one` / 留一条
- 归一动作：`keep_or_keep_one`
- 用户反馈：留一个。

### 重复组 46

- 重复文本：这个历史人物复出那段，评论区都在说别展开
- 样本 ID：`MEME_EXPAND_0010_HIGH`, `MEME_EXPAND_0024_HIGH`
- 原审计：`D02` / `same_text_different_context_review`
- 风险分布：{"high": 2}
- 人工结论：`delete_group` / 整组删除/不进入高质量训练集
- 归一动作：`delete_or_exclude`
- 用户反馈：病句，模板污染，不要了。

### 重复组 47

- 重复文本：这个朝代的改革失败，主要是财政和军制问题
- 样本 ID：`MEME_EXPAND_0067_LOW`, `MEME_EXPAND_0081_LOW`
- 原审计：`D02` / `same_text_different_context_review`
- 风险分布：{"low": 2}
- 人工结论：`keep_one` / 留一条
- 归一动作：`keep_or_keep_one`
- 用户反馈：没问题，留一个。

### 重复组 48

- 重复文本：这剧里的末代掌舵人，怎么越看越像今天的某些人
- 样本 ID：`MEME_EXPAND_0003_HIGH`, `MEME_EXPAND_0017_HIGH`
- 原审计：`D02` / `same_text_different_context_review`
- 风险分布：{"high": 2}
- 人工结论：`keep_one_relabel_high` / 留一条，改 high
- 归一动作：`keep_with_label_change`
- 用户反馈：这个可以，可以判 high，并且留一个。

### 重复组 49

- 重复文本：这是正常明史课程，不涉及现实类比
- 样本 ID：`MEME_EXPAND_0094_NONE`, `MEME_EXPAND_0108_NONE`
- 原审计：`D02` / `same_text_different_context_review`
- 风险分布：{"none": 2}
- 人工结论：`keep_group_style_statement` / 保留，但注意陈述句风格
- 归一动作：`keep_or_keep_one`
- 用户反馈：陈述句，本身没问题。

### 重复组 50

- 重复文本：这波操作太英明了，真是在夸修图教程
- 样本 ID：`MEME_EXPAND_0069_LOW`, `MEME_EXPAND_0083_LOW`
- 原审计：`D02` / `same_text_different_context_review`
- 风险分布：{"low": 2}
- 人工结论：`delete_group` / 整组删除/不进入高质量训练集
- 归一动作：`delete_or_exclude`
- 用户反馈：低质量，不要。

### 重复组 51

- 重复文本：这部历史剧的末代皇帝演得不错
- 样本 ID：`MEME_EXPAND_0066_LOW`, `MEME_EXPAND_0080_LOW`
- 原审计：`D02` / `same_text_different_context_review`
- 风险分布：{"low": 2}
- 人工结论：`keep_one` / 留一条
- 归一动作：`keep_or_keep_one`
- 用户反馈：留一个。

### 重复组 52

- 重复文本：这部历史纪录片讲的是史料争议，不涉及现实类比
- 样本 ID：`MEME_EXPAND_0102_NONE`, `MEME_EXPAND_0116_NONE`
- 原审计：`D02` / `same_text_different_context_review`
- 风险分布：{"none": 2}
- 人工结论：`rewrite_style_statement` / 重写陈述句风格
- 归一动作：`rewrite`
- 用户反馈：陈述句，以后少点这种陈述句行不行，跟说明书一样。

### 重复组 53

- 重复文本：香薰蜡烛真的能提升睡眠氛围
- 样本 ID：`MEME_EXPAND_0096_NONE`, `MEME_EXPAND_0110_NONE`
- 原审计：`D02` / `same_text_different_context_review`
- 风险分布：{"none": 2}
- 人工结论：`keep_one` / 留一条
- 归一动作：`keep_or_keep_one`
- 用户反馈：留一个。
