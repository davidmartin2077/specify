# 第三阶段第二波 44 条人工复核反馈

本文件记录用户对 `docs/phase3_second_wave_review_sample.md` 中 44 条分层抽样样本的人工点评。当前只作为后续重写依据，不修改候选本体、不改标签、不入库。

## 总体原则反馈

1. 审核员语气并非完全不能出现，否则模型可能把审核员自己的说明误判为应封禁内容。
2. 但审核员语气更应该出现在 `reasoning` 逻辑链里，而不是直接作为 `text`。
3. `text` 应该是审核员判断所对应的真实评论、弹幕、回复、私聊话术或二次回复，而不是把审核标准、审核指导、风控提示直接搬到样本表面。
4. 很多陈述句不像正常评论区会出现；但在“对别人评论的二次回复”里，部分陈述句可能成立。后续构造时应明确上下文位置。
5. `safe_context` 不应大量写成官方 tips、平台提示、医院/银行/学校公告口吻；更适合写成普通用户转述、提醒、引用或讨论。
6. `weak_signal` 需要特别小心，不能写成“证据不足/需要核验/不能只看词”这种标注员结论。
7. 黑话样本需要像真实用法。过于“教人解读黑话”的句子应放进 reasoning 或特殊“黑话教学/解释”语境，不宜默认当普通评论区样本。
8. 明确直球风险句仍有训练价值，避免模型只会解读隐喻而不会识别直接表达；但要控制比例和自然度。

## 逐条反馈

| # | ID | 用户反馈 | 后续处理倾向 |
|---:|---|---|---|
| 1 | `PHASE3_W2_0020_SEXUAL_CONTENT_WEAK_SIGNAL` | 像审核员语气，这个文本应该放在逻辑链里，而不是当作评论本身。 | 重写 text，保留类似判断到 reasoning。 |
| 2 | `PHASE3_W2_0022_SEXUAL_CONTENT_SAFE_CONTEXT` | 没什么问题，正常说明。 | 可保留。 |
| 3 | `PHASE3_W2_0003_SEXUAL_CONTENT_DIRECT` | 确实高风险。 | 可保留。 |
| 4 | `PHASE3_W2_0009_SEXUAL_CONTENT_OBFUSCATED` | 高风险。 | 可能从 medium 提升，或保留但加强高风险 rationale。 |
| 5 | `PHASE3_W2_0044_SPAM_ADS_FRAUD_WEAK_SIGNAL` | 审核视角语气。 | 重写 text。 |
| 6 | `PHASE3_W2_0048_SPAM_ADS_FRAUD_SAFE_CONTEXT` | 像是反诈宣传。 | 可作为反诈语境，但需减少 tips/宣传口吻，改成评论/转述更自然。 |
| 7 | `PHASE3_W2_0034_SPAM_ADS_FRAUD_OBFUSCATED` | 确实是黑话，但是有点人机抽象；评论区怎么会突然联系到奶茶？不过这样写也确实能躲避常规审核，比如有的“控会员”会说成“果汁群/汇源果汁”。 | 保留“食品/饮料代称”机制，但重写为更真实的圈内话术。 |
| 8 | `PHASE3_W2_0040_SPAM_ADS_FRAUD_CONTEXTUAL` | 没什么问题，就是有点人机；不像在评论区或弹幕，更多是私聊环境。 | 可保留语义，调整 platform/context 为私聊或投诉转述。 |
| 9 | `PHASE3_W2_0062_INSULTING_ABUSE_WEAK_SIGNAL` | 人机。 | 重写 text。 |
| 10 | `PHASE3_W2_0063_INSULTING_ABUSE_SAFE_CONTEXT` | 像是审核员语气。 | 重写为普通用户反歧视评论/转述。 |
| 11 | `PHASE3_W2_0058_INSULTING_ABUSE_CONTEXTUAL` | 没什么问题。 | 可保留。 |
| 12 | `PHASE3_W2_0053_INSULTING_ABUSE_DIRECT` | 没什么问题。 | 可保留。 |
| 13 | `PHASE3_W2_0075_WEAPONS_EXPLOSIVES_WEAK_SIGNAL` | 审核员语气。 | 重写 text。 |
| 14 | `PHASE3_W2_0079_WEAPONS_EXPLOSIVES_SAFE_CONTEXT` | 安全宣传语气。 | 改成普通讨论/评论转述，避免宣传文案。 |
| 15 | `PHASE3_W2_0068_WEAPONS_EXPLOSIVES_DIRECT` | 逆天了，这么直白的吗？不过模型训练也可能需要这种大白话，否则可能只会解读隐喻、不会解读直球。 | 保留直球样本价值，控制比例并确保上下文合理。 |
| 16 | `PHASE3_W2_0069_WEAPONS_EXPLOSIVES_OBFUSCATED` | 这种称谓/话术有“敌人解读”的成分在里面。 | 重写黑话，使其更像真实圈内代称，避免过度解释化。 |
| 17 | `PHASE3_W2_0091_PUBLIC_AFFAIRS_WEAK_SIGNAL` | 审核员语气。 | 重写 text。 |
| 18 | `PHASE3_W2_0095_PUBLIC_AFFAIRS_SAFE_CONTEXT` | 陈述句。 | 改成更像评论/转述/二次回复。 |
| 19 | `PHASE3_W2_0084_PUBLIC_AFFAIRS_OBFUSCATED` | 教人解读黑话。 | 放到 reasoning 或改成真实暗号使用场景。 |
| 20 | `PHASE3_W2_0088_PUBLIC_AFFAIRS_CONTEXTUAL` | 没什么问题。 | 可保留。 |
| 21 | `PHASE3_W2_0107_POLITICAL_HISTORY_WEAK_SIGNAL` | 审核员语气。 | 重写 text。 |
| 22 | `PHASE3_W2_0108_POLITICAL_HISTORY_SAFE_CONTEXT` | 正常陈述，审核员语气。 | 改成用户评论或课堂/读书会转述。 |
| 23 | `PHASE3_W2_0103_POLITICAL_HISTORY_CONTEXTUAL` | 没什么问题。 | 可保留。 |
| 24 | `PHASE3_W2_0098_POLITICAL_HISTORY_DIRECT` | 没什么问题。 | 可保留。 |
| 25 | `PHASE3_W2_0120_PLATFORM_CENSORSHIP_EVASION_WEAK_SIGNAL` | 审核员语气。 | 重写 text。 |
| 26 | `PHASE3_W2_0124_PLATFORM_CENSORSHIP_EVASION_SAFE_CONTEXT` | 没什么问题。 | 可保留。 |
| 27 | `PHASE3_W2_0113_PLATFORM_CENSORSHIP_EVASION_DIRECT` | 直球、当面挑衅，或者是审核员指导；此地无银三百两。 | 不宜作为普通评论；改成真实规避尝试或移入 reasoning。 |
| 28 | `PHASE3_W2_0114_PLATFORM_CENSORSHIP_EVASION_OBFUSCATED` | 此地无银三百两，也更适合当逻辑链而不是直接评论。 | 重写 text，保留机制到 reasoning。 |
| 29 | `PHASE3_W2_0136_CYBER_ABUSE_WEAK_SIGNAL` | 平台提示常见语录。 | 改成普通用户咨询/私聊语境。 |
| 30 | `PHASE3_W2_0140_CYBER_ABUSE_SAFE_CONTEXT` | 平台提示常见语录。 | 改成普通用户或管理员转述，不写成平台公告。 |
| 31 | `PHASE3_W2_0129_CYBER_ABUSE_OBFUSCATED` | 同 16，有种黑话教学味道，不像评论区正常评论。 | 重写为真实黑产沟通或私聊环境。 |
| 32 | `PHASE3_W2_0133_CYBER_ABUSE_CONTEXTUAL` | 像是黑产私聊，但评论区/弹幕出现这种肯定直接 ban 掉。 | 保留风险方向，明确私聊/群聊场景或提高风险。 |
| 33 | `PHASE3_W2_0152_VIOLENCE_EXTREMISM_WEAK_SIGNAL` | 审核员语气。 | 重写 text。 |
| 34 | `PHASE3_W2_0153_VIOLENCE_EXTREMISM_SAFE_CONTEXT` | 审核员语气。 | 重写为普通用户劝阻/转述。 |
| 35 | `PHASE3_W2_0148_VIOLENCE_EXTREMISM_CONTEXTUAL` | 没什么问题。 | 可保留。 |
| 36 | `PHASE3_W2_0143_VIOLENCE_EXTREMISM_DIRECT` | 没什么问题。 | 可保留。 |
| 37 | `PHASE3_W2_0165_ILLEGAL_GOODS_WEAK_SIGNAL` | 审核员语气。 | 重写 text。 |
| 38 | `PHASE3_W2_0169_ILLEGAL_GOODS_SAFE_CONTEXT` | 陈述句。 | 改成普通评论/转述，减少说明文口吻。 |
| 39 | `PHASE3_W2_0158_ILLEGAL_GOODS_DIRECT` | 没什么问题，确实直球的风险句子。 | 可保留直球样本。 |
| 40 | `PHASE3_W2_0159_ILLEGAL_GOODS_OBFUSCATED` | 同 16 和 31。 | 重写黑话，避免教学/敌人解读感。 |
| 41 | `PHASE3_W2_0181_GAMBLING_WEAK_SIGNAL` | 审核员语气。 | 重写 text。 |
| 42 | `PHASE3_W2_0185_GAMBLING_SAFE_CONTEXT` | 不像是评论，风险度没问题，像是正常陈述。 | 可保留标签方向，但重写为评论/转述。 |
| 43 | `PHASE3_W2_0174_GAMBLING_OBFUSCATED` | 同 16、31、40。 | 重写黑话，避免教学口吻。 |
| 44 | `PHASE3_W2_0178_GAMBLING_CONTEXTUAL` | 高风险。 | 可能从 medium 提升，或加强高风险 rationale。 |

## 初步归纳

按用户反馈，第二波 44 条抽样中可初步分为：

- 可保留或基本通过：2、3、11、12、20、23、24、26、35、36、39。
- 直球风险但需控制比例或可能调高：4、15、32、44。
- 需要重写 text 的审核员语气/审核说明：1、5、9、10、13、17、21、22、25、33、34、37、41。
- 需要降低 tips/宣传/陈述句口吻：6、14、18、29、30、38、42。
- 需要重写黑话，使其更像真实话术而不是黑话教学：7、16、19、27、28、31、40、43。
- 语境可保留但应改成私聊/二次回复/转述等更合理场景：8、32。
