# 重复文本人工复核清单

本文件从正式 `data/processed/combined_candidates.jsonl` 的 860 条样本中抽取全部重复 text 组。

不要只看 `docs/context_requirement_audit.md` 里的样例；那里只是展示前 12 组。这里才是第一步重复文本判断要看的完整文件。

## 怎么判断

- `D01`：可能是有效同文不同标签对照。重点看上下文是否真的改变标签。
- `D02`：同文同标签但上下文不同。重点看是否有训练价值，还是普通重复。
- `D03`：疑似模板污染。优先考虑删、重写或降权。

建议反馈格式：

```text
重复组 01：保留 / 删掉 / 退回重写 / 降权，原因……
MEME_EXPAND_0026_MEDIUM：退回重写，原因……
```

## 全部重复组

### 重复组 01

- 状态：`D02` / `same_text_different_context_review` / 同文同标签但不同上下文，待复核
- 出现次数：3
- 文本：NB 是 New Balance 的鞋款缩写，不是别的意思
- 风险分布：{"none": 3}
- 来源分布：{"meme_expansion": 3}
- 建议动作：看是否只是重复造句；如果上下文差异没有训练价值，建议删/重写/降权。
- 样本 ID：
  - `MEME_EXPAND_0091_NONE`
  - `MEME_EXPAND_0105_NONE`
  - `MEME_EXPAND_0119_NONE`

- 复核结论：待填写

### 重复组 02

- 状态：`D03` / `template_pollution_candidate` / 疑似模板污染，优先删/重写/降权
- 出现次数：3
- 文本：一到这个日期，连普通蜡烛视频都有人刷懂
- 风险分布：{"medium": 3}
- 来源分布：{"meme_expansion": 3}
- 建议动作：优先判为模板污染候选；建议退回重写或后续从高质量训练集中剔除。
- 样本 ID：
  - `MEME_EXPAND_0026_MEDIUM`
  - `MEME_EXPAND_0040_MEDIUM`
  - `MEME_EXPAND_0054_MEDIUM`

- 复核结论：待填写

### 重复组 03

- 状态：`D03` / `template_pollution_candidate` / 疑似模板污染，优先删/重写/降权
- 出现次数：3
- 文本：今天买了白纸，做手账真的很好用
- 风险分布：{"low": 3}
- 来源分布：{"meme_expansion": 3}
- 建议动作：优先判为模板污染候选；建议退回重写或后续从高质量训练集中剔除。
- 样本 ID：
  - `MEME_EXPAND_0061_LOW`
  - `MEME_EXPAND_0075_LOW`
  - `MEME_EXPAND_0089_LOW`

- 复核结论：待填写

### 重复组 04

- 状态：`D03` / `template_pollution_candidate` / 疑似模板污染，优先删/重写/降权
- 出现次数：3
- 文本：他说‘35号见’，不像普通约饭，但也没更多上下文
- 风险分布：{"medium": 3}
- 来源分布：{"meme_expansion": 3}
- 建议动作：优先判为模板污染候选；建议退回重写或后续从高质量训练集中剔除。
- 样本 ID：
  - `MEME_EXPAND_0030_MEDIUM`
  - `MEME_EXPAND_0044_MEDIUM`
  - `MEME_EXPAND_0058_MEDIUM`

- 复核结论：待填写

### 重复组 05

- 状态：`D02` / `same_text_different_context_review` / 同文同标签但不同上下文，待复核
- 出现次数：3
- 文本：倒车镜调低一点更适合我身高
- 风险分布：{"none": 3}
- 来源分布：{"meme_expansion": 3}
- 建议动作：看是否只是重复造句；如果上下文差异没有训练价值，建议删/重写/降权。
- 样本 ID：
  - `MEME_EXPAND_0092_NONE`
  - `MEME_EXPAND_0106_NONE`
  - `MEME_EXPAND_0120_NONE`

- 复核结论：待填写

### 重复组 06

- 状态：`D03` / `template_pollution_candidate` / 疑似模板污染，优先删/重写/降权
- 出现次数：3
- 文本：单条懂没信息，但接在删前留名后就变味了
- 风险分布：{"medium": 3}
- 来源分布：{"meme_expansion": 3}
- 建议动作：优先判为模板污染候选；建议退回重写或后续从高质量训练集中剔除。
- 样本 ID：
  - `MEME_EXPAND_0028_MEDIUM`
  - `MEME_EXPAND_0042_MEDIUM`
  - `MEME_EXPAND_0056_MEDIUM`

- 复核结论：待填写

### 重复组 07

- 状态：`D03` / `template_pollution_candidate` / 疑似模板污染，优先删/重写/降权
- 出现次数：3
- 文本：大家都说历史重演，但没有说明映射到哪件事
- 风险分布：{"medium": 3}
- 来源分布：{"meme_expansion": 3}
- 建议动作：优先判为模板污染候选；建议退回重写或后续从高质量训练集中剔除。
- 样本 ID：
  - `MEME_EXPAND_0032_MEDIUM`
  - `MEME_EXPAND_0046_MEDIUM`
  - `MEME_EXPAND_0060_MEDIUM`

- 复核结论：待填写

### 重复组 08

- 状态：`D03` / `template_pollution_candidate` / 疑似模板污染，优先删/重写/降权
- 出现次数：3
- 文本：这个末代角色被剪成现实感很强的混剪
- 风险分布：{"medium": 3}
- 来源分布：{"meme_expansion": 3}
- 建议动作：优先判为模板污染候选；建议退回重写或后续从高质量训练集中剔除。
- 样本 ID：
  - `MEME_EXPAND_0031_MEDIUM`
  - `MEME_EXPAND_0045_MEDIUM`
  - `MEME_EXPAND_0059_MEDIUM`

- 复核结论：待填写

### 重复组 09

- 状态：`D02` / `same_text_different_context_review` / 同文同标签但不同上下文，待复核
- 出现次数：3
- 文本：这句感谢安排配上翻车现场，像阴阳但对象不明
- 风险分布：{"medium": 3}
- 来源分布：{"meme_expansion": 3}
- 建议动作：看是否只是重复造句；如果上下文差异没有训练价值，建议删/重写/降权。
- 样本 ID：
  - `MEME_EXPAND_0027_MEDIUM`
  - `MEME_EXPAND_0041_MEDIUM`
  - `MEME_EXPAND_0055_MEDIUM`

- 复核结论：待填写

### 重复组 10

- 状态：`D03` / `template_pollution_candidate` / 疑似模板污染，优先删/重写/降权
- 出现次数：3
- 文本：这司机又说为了大家好，结果油门没松过
- 风险分布：{"medium": 3}
- 来源分布：{"meme_expansion": 3}
- 建议动作：优先判为模板污染候选；建议退回重写或后续从高质量训练集中剔除。
- 样本 ID：
  - `MEME_EXPAND_0029_MEDIUM`
  - `MEME_EXPAND_0043_MEDIUM`
  - `MEME_EXPAND_0057_MEDIUM`

- 复核结论：待填写

### 重复组 11

- 状态：`D03` / `template_pollution_candidate` / 疑似模板污染，优先删/重写/降权
- 出现次数：3
- 文本：这游戏优化真棒，卡成PPT
- 风险分布：{"low": 3}
- 来源分布：{"meme_expansion": 3}
- 建议动作：优先判为模板污染候选；建议退回重写或后续从高质量训练集中剔除。
- 样本 ID：
  - `MEME_EXPAND_0062_LOW`
  - `MEME_EXPAND_0076_LOW`
  - `MEME_EXPAND_0090_LOW`

- 复核结论：待填写

### 重复组 12

- 状态：`D02` / `same_text_different_context_review` / 同文同标签但不同上下文，待复核
- 出现次数：2
- 文本：64号选手这把打得不错
- 风险分布：{"low": 2}
- 来源分布：{"meme_expansion": 2}
- 建议动作：看是否只是重复造句；如果上下文差异没有训练价值，建议删/重写/降权。
- 样本 ID：
  - `MEME_EXPAND_0072_LOW`
  - `MEME_EXPAND_0086_LOW`

- 复核结论：待填写

### 重复组 13

- 状态：`D02` / `same_text_different_context_review` / 同文同标签但不同上下文，待复核
- 出现次数：2
- 文本：nb 这个缩写我只想说牛，别过度解读
- 风险分布：{"low": 2}
- 来源分布：{"meme_expansion": 2}
- 建议动作：看是否只是重复造句；如果上下文差异没有训练价值，建议删/重写/降权。
- 样本 ID：
  - `MEME_EXPAND_0063_LOW`
  - `MEME_EXPAND_0077_LOW`

- 复核结论：待填写

### 重复组 14

- 状态：`D02` / `same_text_different_context_review` / 同文同标签但不同上下文，待复核
- 出现次数：2
- 文本：五月多出来的那几天，大家都学会闭麦了
- 风险分布：{"medium": 2}
- 来源分布：{"meme_expansion": 2}
- 建议动作：看是否只是重复造句；如果上下文差异没有训练价值，建议删/重写/降权。
- 样本 ID：
  - `MEME_EXPAND_0037_MEDIUM`
  - `MEME_EXPAND_0051_MEDIUM`

- 复核结论：待填写

### 重复组 15

- 状态：`D02` / `same_text_different_context_review` / 同文同标签但不同上下文，待复核
- 出现次数：2
- 文本：今晚只发旧日历，不写具体日期
- 风险分布：{"high": 2}
- 来源分布：{"meme_expansion": 2}
- 建议动作：看是否只是重复造句；如果上下文差异没有训练价值，建议删/重写/降权。
- 样本 ID：
  - `MEME_EXPAND_0009_HIGH`
  - `MEME_EXPAND_0023_HIGH`

- 复核结论：待填写

### 重复组 16

- 状态：`D02` / `same_text_different_context_review` / 同文同标签但不同上下文，待复核
- 出现次数：2
- 文本：他用某朝改革失败来类比今天，但证据只有一句话
- 风险分布：{"medium": 2}
- 来源分布：{"meme_expansion": 2}
- 建议动作：看是否只是重复造句；如果上下文差异没有训练价值，建议删/重写/降权。
- 样本 ID：
  - `MEME_EXPAND_0038_MEDIUM`
  - `MEME_EXPAND_0052_MEDIUM`

- 复核结论：待填写

### 重复组 17

- 状态：`D02` / `same_text_different_context_review` / 同文同标签但不同上下文，待复核
- 出现次数：2
- 文本：他这波真是英明神武，删评删到只剩彩虹屁
- 风险分布：{"high": 2}
- 来源分布：{"meme_expansion": 2}
- 建议动作：看是否只是重复造句；如果上下文差异没有训练价值，建议删/重写/降权。
- 样本 ID：
  - `MEME_EXPAND_0006_HIGH`
  - `MEME_EXPAND_0020_HIGH`

- 复核结论：待填写

### 重复组 18

- 状态：`D02` / `same_text_different_context_review` / 同文同标签但不同上下文，待复核
- 出现次数：2
- 文本：倒车入库练了一下午，教练说我终于会看镜子了
- 风险分布：{"low": 2}
- 来源分布：{"meme_expansion": 2}
- 建议动作：看是否只是重复造句；如果上下文差异没有训练价值，建议删/重写/降权。
- 样本 ID：
  - `MEME_EXPAND_0064_LOW`
  - `MEME_EXPAND_0078_LOW`

- 复核结论：待填写

### 重复组 19

- 状态：`D02` / `same_text_different_context_review` / 同文同标签但不同上下文，待复核
- 出现次数：2
- 文本：六月四号我生日，求祝福
- 风险分布：{"low": 2}
- 来源分布：{"meme_expansion": 2}
- 建议动作：看是否只是重复造句；如果上下文差异没有训练价值，建议删/重写/降权。
- 样本 ID：
  - `MEME_EXPAND_0065_LOW`
  - `MEME_EXPAND_0079_LOW`

- 复核结论：待填写

### 重复组 20

- 状态：`D02` / `same_text_different_context_review` / 同文同标签但不同上下文，待复核
- 出现次数：2
- 文本：删前留名是抽奖梗，不是内容风险
- 风险分布：{"low": 2}
- 来源分布：{"meme_expansion": 2}
- 建议动作：看是否只是重复造句；如果上下文差异没有训练价值，建议删/重写/降权。
- 样本 ID：
  - `MEME_EXPAND_0070_LOW`
  - `MEME_EXPAND_0084_LOW`

- 复核结论：待填写

### 重复组 21

- 状态：`D02` / `same_text_different_context_review` / 同文同标签但不同上下文，待复核
- 出现次数：2
- 文本：别再刷 j c 了，今天这条时间线已经够明显
- 风险分布：{"high": 2}
- 来源分布：{"meme_expansion": 2}
- 建议动作：看是否只是重复造句；如果上下文差异没有训练价值，建议删/重写/降权。
- 样本 ID：
  - `MEME_EXPAND_0007_HIGH`
  - `MEME_EXPAND_0021_HIGH`

- 复核结论：待填写

### 重复组 22

- 状态：`D02` / `same_text_different_context_review` / 同文同标签但不同上下文，待复核
- 出现次数：2
- 文本：别发全称，写成 g·c·q 就行，这句本身有规避味
- 风险分布：{"medium": 2}
- 来源分布：{"meme_expansion": 2}
- 建议动作：看是否只是重复造句；如果上下文差异没有训练价值，建议删/重写/降权。
- 样本 ID：
  - `MEME_EXPAND_0035_MEDIUM`
  - `MEME_EXPAND_0049_MEDIUM`

- 复核结论：待填写

### 重复组 23

- 状态：`D02` / `same_text_different_context_review` / 同文同标签但不同上下文，待复核
- 出现次数：2
- 文本：前面说那年夏天的别回了，楼已经被清过一轮
- 风险分布：{"high": 2}
- 来源分布：{"meme_expansion": 2}
- 建议动作：看是否只是重复造句；如果上下文差异没有训练价值，建议删/重写/降权。
- 样本 ID：
  - `MEME_EXPAND_0011_HIGH`
  - `MEME_EXPAND_0025_HIGH`

- 复核结论：待填写

### 重复组 24

- 状态：`D02` / `same_text_different_context_review` / 同文同标签但不同上下文，待复核
- 出现次数：2
- 文本：包子、茶杯和旧照片一起发，单看都正常
- 风险分布：{"medium": 2}
- 来源分布：{"meme_expansion": 2}
- 建议动作：看是否只是重复造句；如果上下文差异没有训练价值，建议删/重写/降权。
- 样本 ID：
  - `MEME_EXPAND_0033_MEDIUM`
  - `MEME_EXPAND_0047_MEDIUM`

- 复核结论：待填写

### 重复组 25

- 状态：`D02` / `same_text_different_context_review` / 同文同标签但不同上下文，待复核
- 出现次数：2
- 文本：包子铺突然限评，大家却都在问馅儿是不是换了
- 风险分布：{"high": 2}
- 来源分布：{"meme_expansion": 2}
- 建议动作：看是否只是重复造句；如果上下文差异没有训练价值，建议删/重写/降权。
- 样本 ID：
  - `MEME_EXPAND_0005_HIGH`
  - `MEME_EXPAND_0019_HIGH`

- 复核结论：待填写

### 重复组 26

- 状态：`D02` / `same_text_different_context_review` / 同文同标签但不同上下文，待复核
- 出现次数：2
- 文本：历史书翻到这一页，弹幕都在说熟悉的配方
- 风险分布：{"high": 2}
- 来源分布：{"meme_expansion": 2}
- 建议动作：看是否只是重复造句；如果上下文差异没有训练价值，建议删/重写/降权。
- 样本 ID：
  - `MEME_EXPAND_0004_HIGH`
  - `MEME_EXPAND_0018_HIGH`

- 复核结论：待填写

### 重复组 27

- 状态：`D02` / `same_text_different_context_review` / 同文同标签但不同上下文，待复核
- 出现次数：2
- 文本：历史总是相似，这句是影评里的主题概括
- 风险分布：{"low": 2}
- 来源分布：{"meme_expansion": 2}
- 建议动作：看是否只是重复造句；如果上下文差异没有训练价值，建议删/重写/降权。
- 样本 ID：
  - `MEME_EXPAND_0074_LOW`
  - `MEME_EXPAND_0088_LOW`

- 复核结论：待填写

### 重复组 28

- 状态：`D02` / `same_text_different_context_review` / 同文同标签但不同上下文，待复核
- 出现次数：2
- 文本：历史重演是小说主题，不是在指现实事件
- 风险分布：{"none": 2}
- 来源分布：{"meme_expansion": 2}
- 建议动作：看是否只是重复造句；如果上下文差异没有训练价值，建议删/重写/降权。
- 样本 ID：
  - `MEME_EXPAND_0095_NONE`
  - `MEME_EXPAND_0109_NONE`

- 复核结论：待填写

### 重复组 29

- 状态：`D02` / `same_text_different_context_review` / 同文同标签但不同上下文，待复核
- 出现次数：2
- 文本：又到那个 5·35 的晚上，评论区自动静音
- 风险分布：{"high": 2}
- 来源分布：{"meme_expansion": 2}
- 建议动作：看是否只是重复造句；如果上下文差异没有训练价值，建议删/重写/降权。
- 样本 ID：
  - `MEME_EXPAND_0002_HIGH`
  - `MEME_EXPAND_0016_HIGH`

- 复核结论：待填写

### 重复组 30

- 状态：`D02` / `same_text_different_context_review` / 同文同标签但不同上下文，待复核
- 出现次数：2
- 文本：崇祯时期财政问题很复杂，不能只怪一个人
- 风险分布：{"low": 2}
- 来源分布：{"meme_expansion": 2}
- 建议动作：看是否只是重复造句；如果上下文差异没有训练价值，建议删/重写/降权。
- 样本 ID：
  - `MEME_EXPAND_0073_LOW`
  - `MEME_EXPAND_0087_LOW`

- 复核结论：待填写

### 重复组 31

- 状态：`D02` / `same_text_different_context_review` / 同文同标签但不同上下文，待复核
- 出现次数：2
- 文本：庆丰包子的素馅我觉得一般
- 风险分布：{"none": 2}
- 来源分布：{"meme_expansion": 2}
- 建议动作：看是否只是重复造句；如果上下文差异没有训练价值，建议删/重写/降权。
- 样本 ID：
  - `MEME_EXPAND_0103_NONE`
  - `MEME_EXPAND_0117_NONE`

- 复核结论：待填写

### 重复组 32

- 状态：`D02` / `same_text_different_context_review` / 同文同标签但不同上下文，待复核
- 出现次数：2
- 文本：感谢安排是婚礼流程顺利后的真诚感谢
- 风险分布：{"none": 2}
- 来源分布：{"meme_expansion": 2}
- 建议动作：看是否只是重复造句；如果上下文差异没有训练价值，建议删/重写/降权。
- 样本 ID：
  - `MEME_EXPAND_0097_NONE`
  - `MEME_EXPAND_0111_NONE`

- 复核结论：待填写

### 重复组 33

- 状态：`D02` / `same_text_different_context_review` / 同文同标签但不同上下文，待复核
- 出现次数：2
- 文本：我买了64色马克笔，做手账刚好够用
- 风险分布：{"none": 2}
- 来源分布：{"meme_expansion": 2}
- 建议动作：看是否只是重复造句；如果上下文差异没有训练价值，建议删/重写/降权。
- 样本 ID：
  - `MEME_EXPAND_0100_NONE`
  - `MEME_EXPAND_0114_NONE`

- 复核结论：待填写

### 重复组 34

- 状态：`D02` / `same_text_different_context_review` / 同文同标签但不同上下文，待复核
- 出现次数：2
- 文本：末代皇帝的性格分析应放在当时制度背景里看
- 风险分布：{"none": 2}
- 来源分布：{"meme_expansion": 2}
- 建议动作：看是否只是重复造句；如果上下文差异没有训练价值，建议删/重写/降权。
- 样本 ID：
  - `MEME_EXPAND_0101_NONE`
  - `MEME_EXPAND_0115_NONE`

- 复核结论：待填写

### 重复组 35

- 状态：`D02` / `same_text_different_context_review` / 同文同标签但不同上下文，待复核
- 出现次数：2
- 文本：楼上说倒车，楼下接后视镜早拆了
- 风险分布：{"medium": 2}
- 来源分布：{"meme_expansion": 2}
- 建议动作：看是否只是重复造句；如果上下文差异没有训练价值，建议删/重写/降权。
- 样本 ID：
  - `MEME_EXPAND_0036_MEDIUM`
  - `MEME_EXPAND_0050_MEDIUM`

- 复核结论：待填写

### 重复组 36

- 状态：`D02` / `same_text_different_context_review` / 同文同标签但不同上下文，待复核
- 出现次数：2
- 文本：楼上问司机是谁，楼下只回‘油门到底’
- 风险分布：{"high": 2}
- 来源分布：{"meme_expansion": 2}
- 建议动作：看是否只是重复造句；如果上下文差异没有训练价值，建议删/重写/降权。
- 样本 ID：
  - `MEME_EXPAND_0008_HIGH`
  - `MEME_EXPAND_0022_HIGH`

- 复核结论：待填写

### 重复组 37

- 状态：`D02` / `same_text_different_context_review` / 同文同标签但不同上下文，待复核
- 出现次数：2
- 文本：河蟹真的好吃，清蒸就很鲜
- 风险分布：{"low": 2}
- 来源分布：{"meme_expansion": 2}
- 建议动作：看是否只是重复造句；如果上下文差异没有训练价值，建议删/重写/降权。
- 样本 ID：
  - `MEME_EXPAND_0068_LOW`
  - `MEME_EXPAND_0082_LOW`

- 复核结论：待填写

### 重复组 38

- 状态：`D02` / `same_text_different_context_review` / 同文同标签但不同上下文，待复核
- 出现次数：2
- 文本：油门踩重了才熄火，驾考真的紧张
- 风险分布：{"none": 2}
- 来源分布：{"meme_expansion": 2}
- 建议动作：看是否只是重复造句；如果上下文差异没有训练价值，建议删/重写/降权。
- 样本 ID：
  - `MEME_EXPAND_0099_NONE`
  - `MEME_EXPAND_0113_NONE`

- 复核结论：待填写

### 重复组 39

- 状态：`D02` / `same_text_different_context_review` / 同文同标签但不同上下文，待复核
- 出现次数：2
- 文本：符号分隔歌词是为了卡点，不是规避关键词
- 风险分布：{"none": 2}
- 来源分布：{"meme_expansion": 2}
- 建议动作：看是否只是重复造句；如果上下文差异没有训练价值，建议删/重写/降权。
- 样本 ID：
  - `MEME_EXPAND_0098_NONE`
  - `MEME_EXPAND_0112_NONE`

- 复核结论：待填写

### 重复组 40

- 状态：`D02` / `same_text_different_context_review` / 同文同标签但不同上下文，待复核
- 出现次数：2
- 文本：第35页的公式推导有个笔误
- 风险分布：{"none": 2}
- 来源分布：{"meme_expansion": 2}
- 建议动作：看是否只是重复造句；如果上下文差异没有训练价值，建议删/重写/降权。
- 样本 ID：
  - `MEME_EXPAND_0093_NONE`
  - `MEME_EXPAND_0107_NONE`

- 复核结论：待填写

### 重复组 41

- 状态：`D02` / `same_text_different_context_review` / 同文同标签但不同上下文，待复核
- 出现次数：2
- 文本：老师英明是弹幕在夸讲题清楚
- 风险分布：{"none": 2}
- 来源分布：{"meme_expansion": 2}
- 建议动作：看是否只是重复造句；如果上下文差异没有训练价值，建议删/重写/降权。
- 样本 ID：
  - `MEME_EXPAND_0104_NONE`
  - `MEME_EXPAND_0118_NONE`

- 复核结论：待填写

### 重复组 42

- 状态：`D02` / `same_text_different_context_review` / 同文同标签但不同上下文，待复核
- 出现次数：2
- 文本：英明两个字刷得太整齐，像反话又像真粉
- 风险分布：{"medium": 2}
- 来源分布：{"meme_expansion": 2}
- 建议动作：看是否只是重复造句；如果上下文差异没有训练价值，建议删/重写/降权。
- 样本 ID：
  - `MEME_EXPAND_0034_MEDIUM`
  - `MEME_EXPAND_0048_MEDIUM`

- 复核结论：待填写

### 重复组 43

- 状态：`D02` / `same_text_different_context_review` / 同文同标签但不同上下文，待复核
- 出现次数：2
- 文本：视频讲的是历史课，弹幕却都在问现在呢
- 风险分布：{"medium": 2}
- 来源分布：{"meme_expansion": 2}
- 建议动作：看是否只是重复造句；如果上下文差异没有训练价值，建议删/重写/降权。
- 样本 ID：
  - `MEME_EXPAND_0039_MEDIUM`
  - `MEME_EXPAND_0053_MEDIUM`

- 复核结论：待填写

### 重复组 44

- 状态：`D02` / `same_text_different_context_review` / 同文同标签但不同上下文，待复核
- 出现次数：2
- 文本：车开太快了，真的要检查刹车片
- 风险分布：{"low": 2}
- 来源分布：{"meme_expansion": 2}
- 建议动作：看是否只是重复造句；如果上下文差异没有训练价值，建议删/重写/降权。
- 样本 ID：
  - `MEME_EXPAND_0071_LOW`
  - `MEME_EXPAND_0085_LOW`

- 复核结论：待填写

### 重复组 45

- 状态：`D02` / `same_text_different_context_review` / 同文同标签但不同上下文，待复核
- 出现次数：2
- 文本：车门焊死、油门踩满、倒车镜拆了，三件套齐活
- 风险分布：{"high": 2}
- 来源分布：{"meme_expansion": 2}
- 建议动作：看是否只是重复造句；如果上下文差异没有训练价值，建议删/重写/降权。
- 样本 ID：
  - `MEME_EXPAND_0001_HIGH`
  - `MEME_EXPAND_0015_HIGH`

- 复核结论：待填写

### 重复组 46

- 状态：`D02` / `same_text_different_context_review` / 同文同标签但不同上下文，待复核
- 出现次数：2
- 文本：这个历史人物复出那段，评论区都在说别展开
- 风险分布：{"high": 2}
- 来源分布：{"meme_expansion": 2}
- 建议动作：看是否只是重复造句；如果上下文差异没有训练价值，建议删/重写/降权。
- 样本 ID：
  - `MEME_EXPAND_0010_HIGH`
  - `MEME_EXPAND_0024_HIGH`

- 复核结论：待填写

### 重复组 47

- 状态：`D02` / `same_text_different_context_review` / 同文同标签但不同上下文，待复核
- 出现次数：2
- 文本：这个朝代的改革失败，主要是财政和军制问题
- 风险分布：{"low": 2}
- 来源分布：{"meme_expansion": 2}
- 建议动作：看是否只是重复造句；如果上下文差异没有训练价值，建议删/重写/降权。
- 样本 ID：
  - `MEME_EXPAND_0067_LOW`
  - `MEME_EXPAND_0081_LOW`

- 复核结论：待填写

### 重复组 48

- 状态：`D02` / `same_text_different_context_review` / 同文同标签但不同上下文，待复核
- 出现次数：2
- 文本：这剧里的末代掌舵人，怎么越看越像今天的某些人
- 风险分布：{"high": 2}
- 来源分布：{"meme_expansion": 2}
- 建议动作：看是否只是重复造句；如果上下文差异没有训练价值，建议删/重写/降权。
- 样本 ID：
  - `MEME_EXPAND_0003_HIGH`
  - `MEME_EXPAND_0017_HIGH`

- 复核结论：待填写

### 重复组 49

- 状态：`D02` / `same_text_different_context_review` / 同文同标签但不同上下文，待复核
- 出现次数：2
- 文本：这是正常明史课程，不涉及现实类比
- 风险分布：{"none": 2}
- 来源分布：{"meme_expansion": 2}
- 建议动作：看是否只是重复造句；如果上下文差异没有训练价值，建议删/重写/降权。
- 样本 ID：
  - `MEME_EXPAND_0094_NONE`
  - `MEME_EXPAND_0108_NONE`

- 复核结论：待填写

### 重复组 50

- 状态：`D02` / `same_text_different_context_review` / 同文同标签但不同上下文，待复核
- 出现次数：2
- 文本：这波操作太英明了，真是在夸修图教程
- 风险分布：{"low": 2}
- 来源分布：{"meme_expansion": 2}
- 建议动作：看是否只是重复造句；如果上下文差异没有训练价值，建议删/重写/降权。
- 样本 ID：
  - `MEME_EXPAND_0069_LOW`
  - `MEME_EXPAND_0083_LOW`

- 复核结论：待填写

### 重复组 51

- 状态：`D02` / `same_text_different_context_review` / 同文同标签但不同上下文，待复核
- 出现次数：2
- 文本：这部历史剧的末代皇帝演得不错
- 风险分布：{"low": 2}
- 来源分布：{"meme_expansion": 2}
- 建议动作：看是否只是重复造句；如果上下文差异没有训练价值，建议删/重写/降权。
- 样本 ID：
  - `MEME_EXPAND_0066_LOW`
  - `MEME_EXPAND_0080_LOW`

- 复核结论：待填写

### 重复组 52

- 状态：`D02` / `same_text_different_context_review` / 同文同标签但不同上下文，待复核
- 出现次数：2
- 文本：这部历史纪录片讲的是史料争议，不涉及现实类比
- 风险分布：{"none": 2}
- 来源分布：{"meme_expansion": 2}
- 建议动作：看是否只是重复造句；如果上下文差异没有训练价值，建议删/重写/降权。
- 样本 ID：
  - `MEME_EXPAND_0102_NONE`
  - `MEME_EXPAND_0116_NONE`

- 复核结论：待填写

### 重复组 53

- 状态：`D02` / `same_text_different_context_review` / 同文同标签但不同上下文，待复核
- 出现次数：2
- 文本：香薰蜡烛真的能提升睡眠氛围
- 风险分布：{"none": 2}
- 来源分布：{"meme_expansion": 2}
- 建议动作：看是否只是重复造句；如果上下文差异没有训练价值，建议删/重写/降权。
- 样本 ID：
  - `MEME_EXPAND_0096_NONE`
  - `MEME_EXPAND_0110_NONE`

- 复核结论：待填写
