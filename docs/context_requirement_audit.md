# 上下文依赖与二元安全标签审计

本报告只审计并生成预览，不修改正式 `data/processed/combined_candidates.jsonl`，也不把外部 340 条入库。

## 输入范围

- 正式 processed：860 条
- 外部 raw 预览：340 条
- 合计：1200 条

## 二元标签预览

| binary | count |
|---|---:|
| B01 / unsafe | 899 |
| B02 / safe | 301 |

规则：`high/medium/low -> unsafe`，`none -> safe`。二元标签用于封杀率/召回评测，多级 `risk_level` 继续用于解释、分层治理和人工复核。

## 上下文依赖分层

| class | count |
|---|---:|
| C02 / contextual_required | 846 |
| C03 / safe_without_context | 301 |
| C01 / direct_no_context | 53 |

- `direct_no_context`：单条文本本身已有足够风险信号，后续不应硬编标题、上级评论或回复链。
- `contextual_required`：需要标题、上级评论、时间、话题或回复链才能支撑当前风险解释。
- `safe_without_context`：单条文本正常或外部标签安全，不应为凑 schema 强行制造风险语境。

## 主要审计标记

| flag | count |
|---|---:|
| F01 / generic_or_template_context | 429 |
| F02 / external_placeholder_context | 340 |
| F03 / do_not_invent_context_review_needed | 246 |
| F04 / safe_sample_context_may_be_optional | 166 |
| F05 / likely_direct_no_context | 10 |
| F06 / context_required_but_empty | 1 |

这些标记是启发式，不是自动判错。优先人工复核 `F02 external_placeholder_context`、`F05 likely_direct_no_context` 和 `F08 reasoning_claims_context_but_context_thin`。

完整代码表见 `docs/context_audit_codebook.md`。这些数字码只服务人工复核和数据命名，不应进入模型训练文本。

## 重复文本判断

- 正式 860 条重复 text 组：53
- 疑似有效同文不同语境对照：0 组
- 同文不同语境待复核：45 组
- 疑似模板污染：8 组

样例：

- `NB 是 New Balance 的鞋款缩写，不是别的意思`
  count=3；status=`D02 / same_text_different_context_review`；ids=MEME_EXPAND_0091_NONE, MEME_EXPAND_0105_NONE, MEME_EXPAND_0119_NONE
- `一到这个日期，连普通蜡烛视频都有人刷懂`
  count=3；status=`D03 / template_pollution_candidate`；ids=MEME_EXPAND_0026_MEDIUM, MEME_EXPAND_0040_MEDIUM, MEME_EXPAND_0054_MEDIUM
- `今天买了白纸，做手账真的很好用`
  count=3；status=`D03 / template_pollution_candidate`；ids=MEME_EXPAND_0061_LOW, MEME_EXPAND_0075_LOW, MEME_EXPAND_0089_LOW
- `他说‘35号见’，不像普通约饭，但也没更多上下文`
  count=3；status=`D03 / template_pollution_candidate`；ids=MEME_EXPAND_0030_MEDIUM, MEME_EXPAND_0044_MEDIUM, MEME_EXPAND_0058_MEDIUM
- `倒车镜调低一点更适合我身高`
  count=3；status=`D02 / same_text_different_context_review`；ids=MEME_EXPAND_0092_NONE, MEME_EXPAND_0106_NONE, MEME_EXPAND_0120_NONE
- `单条懂没信息，但接在删前留名后就变味了`
  count=3；status=`D03 / template_pollution_candidate`；ids=MEME_EXPAND_0028_MEDIUM, MEME_EXPAND_0042_MEDIUM, MEME_EXPAND_0056_MEDIUM
- `大家都说历史重演，但没有说明映射到哪件事`
  count=3；status=`D03 / template_pollution_candidate`；ids=MEME_EXPAND_0032_MEDIUM, MEME_EXPAND_0046_MEDIUM, MEME_EXPAND_0060_MEDIUM
- `这个末代角色被剪成现实感很强的混剪`
  count=3；status=`D03 / template_pollution_candidate`；ids=MEME_EXPAND_0031_MEDIUM, MEME_EXPAND_0045_MEDIUM, MEME_EXPAND_0059_MEDIUM
- `这句感谢安排配上翻车现场，像阴阳但对象不明`
  count=3；status=`D02 / same_text_different_context_review`；ids=MEME_EXPAND_0027_MEDIUM, MEME_EXPAND_0041_MEDIUM, MEME_EXPAND_0055_MEDIUM
- `这司机又说为了大家好，结果油门没松过`
  count=3；status=`D03 / template_pollution_candidate`；ids=MEME_EXPAND_0029_MEDIUM, MEME_EXPAND_0043_MEDIUM, MEME_EXPAND_0057_MEDIUM
- `这游戏优化真棒，卡成PPT`
  count=3；status=`D03 / template_pollution_candidate`；ids=MEME_EXPAND_0062_LOW, MEME_EXPAND_0076_LOW, MEME_EXPAND_0090_LOW
- `64号选手这把打得不错`
  count=2；status=`D02 / same_text_different_context_review`；ids=MEME_EXPAND_0072_LOW, MEME_EXPAND_0086_LOW

## 评测集草案

- `data/eval/risk_test_preview.jsonl`：全 unsafe 预览样本，用于衡量 unsafe recall/封杀率。
- `data/eval/normal_test_preview.jsonl`：safe 或 hard negative 预览样本，用于衡量 false positive/误封率。

第一阶段建议阈值：risk_test unsafe recall 目标 80%-90%+；normal_test 误封率暂可容忍约 30%，后续靠 hard negative 和真实安全评论继续压低。

## 生成文件

- `data/raw/context_requirement_audit.json`
- `data/raw/combined_candidates_binary_preview.jsonl`
- `data/raw/external_safety_binary_preview.jsonl`
- `data/eval/risk_test_preview.jsonl`
- `data/eval/normal_test_preview.jsonl`
