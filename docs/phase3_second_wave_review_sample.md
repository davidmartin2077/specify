# 第三阶段第二波分层人工复核清单

本清单从第二波 185 条 raw 中确定性抽取 44 条，每个类别 4 条。候选原始标签未被修改。

复核回复格式建议：`ID：通过`，或 `ID：改为 medium，原因……`，或 `ID：退回，原因……`。


## 色情低俗 `sexual_content`

### 1. `PHASE3_W2_0020_SEXUAL_CONTENT_WEAK_SIGNAL`

- 模式：`weak_signal`
- 文本：陪玩可以是正规游戏服务，不能只看这个词
- 上下文：色情低俗高召回边界复核区；当前只有弱信号和不完整语境；普通解释也成立 / 先保留复核
- 当前标签：`low` / `E1_平台黑话` / hard_negative=`true`
- 初步风格标记：`reviewer_voice`
- 复核重点：普通解释是否更强，low 是否仍值得召回？
- 复核结论：待填写

### 2. `PHASE3_W2_0022_SEXUAL_CONTENT_SAFE_CONTEXT`

- 模式：`safe_context`
- 文本：性健康门诊面向成年人提供正规咨询和检测
- 上下文：色情低俗新闻教育与正常语境区；上下文提供完整反证；属于正常讨论 / 不要只看关键词
- 当前标签：`none` / `none` / hard_negative=`true`
- 初步风格标记：`none`
- 复核重点：反证是否完整，none 是否会造成漏判？
- 复核结论：待填写

### 3. `PHASE3_W2_0003_SEXUAL_CONTENT_DIRECT`

- 模式：`direct`
- 文本：陪酒之后还能安排别的，费用另算
- 上下文：色情低俗疑似明确风险互动区；有人继续追问具体条件；具体怎么走 / 公开区别留细节
- 当前标签：`high` / `E1_平台黑话` / hard_negative=`false`
- 初步风格标记：`none`
- 复核重点：风险意图是否足够明确，high 是否合理？
- 复核结论：待填写

### 4. `PHASE3_W2_0009_SEXUAL_CONTENT_OBFUSCATED`

- 模式：`obfuscated`
- 文本：联系方式藏在尺码表里，按最大码找
- 上下文：色情低俗规避表达与黑话讨论区；上级评论提示不要使用原词；暗号收到 / 换个写法
- 当前标签：`medium` / `E1_平台黑话` / hard_negative=`false`
- 初步风格标记：`none`
- 复核重点：规避映射是否自然，medium 是否证据充分？
- 复核结论：待填写


## 广告/诈骗/导流 `spam_ads_fraud`

### 5. `PHASE3_W2_0044_SPAM_ADS_FRAUD_WEAK_SIGNAL`

- 模式：`weak_signal`
- 文本：兼职要求实名认证，需要进一步核验公司主体
- 上下文：广告诈骗导流高召回边界复核区；当前只有弱信号和不完整语境；普通解释也成立 / 先保留复核
- 当前标签：`low` / `E1_平台黑话` / hard_negative=`true`
- 初步风格标记：`reviewer_voice`
- 复核重点：普通解释是否更强，low 是否仍值得召回？
- 复核结论：待填写

### 6. `PHASE3_W2_0048_SPAM_ADS_FRAUD_SAFE_CONTEXT`

- 模式：`safe_context`
- 文本：银行客服不会索要验证码，遇到催促应立即挂断
- 上下文：广告诈骗导流新闻教育与正常语境区；上下文提供完整反证；属于正常讨论 / 不要只看关键词
- 当前标签：`none` / `none` / hard_negative=`true`
- 初步风格标记：`none`
- 复核重点：反证是否完整，none 是否会造成漏判？
- 复核结论：待填写

### 7. `PHASE3_W2_0034_SPAM_ADS_FRAUD_OBFUSCATED`

- 模式：`obfuscated`
- 文本：费用写成奶茶杯数，懂价格的直接报杯
- 上下文：广告诈骗导流规避表达与黑话讨论区；上级评论提示不要使用原词；暗号收到 / 换个写法
- 当前标签：`medium` / `E1_平台黑话` / hard_negative=`false`
- 初步风格标记：`none`
- 复核重点：规避映射是否自然，medium 是否证据充分？
- 复核结论：待填写

### 8. `PHASE3_W2_0040_SPAM_ADS_FRAUD_CONTEXTUAL`

- 模式：`contextual`
- 文本：对方一直催我先垫钱，说错过就不能恢复
- 上下文：广告诈骗导流上下文触发风险讨论区；单句含义依赖前后互动；结合前文看 / 需要进一步核验
- 当前标签：`medium` / `E1_平台黑话` / hard_negative=`false`
- 初步风格标记：`none`
- 复核重点：上下文是否真的提升风险解释，medium 是否过度？
- 复核结论：待填写


## 辱骂/群体攻击 `insulting_abuse`

### 9. `PHASE3_W2_0062_INSULTING_ABUSE_WEAK_SIGNAL`

- 模式：`weak_signal`
- 文本：灰头像可能只是界面样式，借代证据不足
- 上下文：辱骂群体攻击高召回边界复核区；当前只有弱信号和不完整语境；普通解释也成立 / 先保留复核
- 当前标签：`low` / `D3_借代` / hard_negative=`true`
- 初步风格标记：`reviewer_voice`
- 复核重点：普通解释是否更强，low 是否仍值得召回？
- 复核结论：待填写

### 10. `PHASE3_W2_0063_INSULTING_ABUSE_SAFE_CONTEXT`

- 模式：`safe_context`
- 文本：反歧视公益片引用偏见话术，是为了批评群体攻击
- 上下文：辱骂群体攻击新闻教育与正常语境区；上下文提供完整反证；属于正常讨论 / 不要只看关键词
- 当前标签：`none` / `none` / hard_negative=`true`
- 初步风格标记：`none`
- 复核重点：反证是否完整，none 是否会造成漏判？
- 复核结论：待填写

### 11. `PHASE3_W2_0058_INSULTING_ABUSE_CONTEXTUAL`

- 模式：`contextual`
- 文本：一听他说做什么工作的，我就知道评论没法看
- 上下文：辱骂群体攻击上下文触发风险讨论区；单句含义依赖前后互动；结合前文看 / 需要进一步核验
- 当前标签：`medium` / `D3_借代` / hard_negative=`false`
- 初步风格标记：`none`
- 复核重点：上下文是否真的提升风险解释，medium 是否过度？
- 复核结论：待填写

### 12. `PHASE3_W2_0053_INSULTING_ABUSE_DIRECT`

- 模式：`direct`
- 文本：这类病人活该被排斥，别让他们进社区
- 上下文：辱骂群体攻击疑似明确风险互动区；有人继续追问具体条件；具体怎么走 / 公开区别留细节
- 当前标签：`high` / `D3_借代` / hard_negative=`false`
- 初步风格标记：`none`
- 复核重点：风险意图是否足够明确，high 是否合理？
- 复核结论：待填写


## 枪爆武器 `weapons_explosives`

### 13. `PHASE3_W2_0075_WEAPONS_EXPLOSIVES_WEAK_SIGNAL`

- 模式：`weak_signal`
- 文本：管子和弹簧可能是普通机械件，缺少用途证据
- 上下文：枪爆武器高召回边界复核区；当前只有弱信号和不完整语境；普通解释也成立 / 先保留复核
- 当前标签：`low` / `C4_典故/物品/符号借用` / hard_negative=`true`
- 初步风格标记：`none`
- 复核重点：普通解释是否更强，low 是否仍值得召回？
- 复核结论：待填写

### 14. `PHASE3_W2_0079_WEAPONS_EXPLOSIVES_SAFE_CONTEXT`

- 模式：`safe_context`
- 文本：消防培训讲解起爆风险，是为了规范危险品处置
- 上下文：枪爆武器新闻教育与正常语境区；上下文提供完整反证；属于正常讨论 / 不要只看关键词
- 当前标签：`none` / `none` / hard_negative=`true`
- 初步风格标记：`none`
- 复核重点：反证是否完整，none 是否会造成漏判？
- 复核结论：待填写

### 15. `PHASE3_W2_0068_WEAPONS_EXPLOSIVES_DIRECT`

- 模式：`direct`
- 文本：这批管制刀具不开票，同城可以当面拿
- 上下文：枪爆武器疑似明确风险互动区；有人继续追问具体条件；具体怎么走 / 公开区别留细节
- 当前标签：`high` / `C4_典故/物品/符号借用` / hard_negative=`false`
- 初步风格标记：`none`
- 复核重点：风险意图是否足够明确，high 是否合理？
- 复核结论：待填写

### 16. `PHASE3_W2_0069_WEAPONS_EXPLOSIVES_OBFUSCATED`

- 模式：`obfuscated`
- 文本：击发那套叫钟表，问走时就是问成色
- 上下文：枪爆武器规避表达与黑话讨论区；上级评论提示不要使用原词；暗号收到 / 换个写法
- 当前标签：`medium` / `C4_典故/物品/符号借用` / hard_negative=`false`
- 初步风格标记：`none`
- 复核重点：规避映射是否自然，medium 是否证据充分？
- 复核结论：待填写


## 公共事务 `public_affairs`

### 17. `PHASE3_W2_0091_PUBLIC_AFFAIRS_WEAK_SIGNAL`

- 模式：`weak_signal`
- 文本：强调人数有施压意味，但具体行为尚不明确
- 上下文：公共事务高召回边界复核区；当前只有弱信号和不完整语境；普通解释也成立 / 先保留复核
- 当前标签：`low` / `E3_话题/热点触发` / hard_negative=`true`
- 初步风格标记：`none`
- 复核重点：普通解释是否更强，low 是否仍值得召回？
- 复核结论：待填写

### 18. `PHASE3_W2_0095_PUBLIC_AFFAIRS_SAFE_CONTEXT`

- 模式：`safe_context`
- 文本：新闻报道群众诉求时应保护个人信息并核实事实
- 上下文：公共事务新闻教育与正常语境区；上下文提供完整反证；属于正常讨论 / 不要只看关键词
- 当前标签：`none` / `none` / hard_negative=`true`
- 初步风格标记：`none`
- 复核重点：反证是否完整，none 是否会造成漏判？
- 复核结论：待填写

### 19. `PHASE3_W2_0084_PUBLIC_AFFAIRS_OBFUSCATED`

- 模式：`obfuscated`
- 文本：集合两个字换成看房，时间还是老地方
- 上下文：公共事务规避表达与黑话讨论区；上级评论提示不要使用原词；暗号收到 / 换个写法
- 当前标签：`medium` / `E3_话题/热点触发` / hard_negative=`false`
- 初步风格标记：`none`
- 复核重点：规避映射是否自然，medium 是否证据充分？
- 复核结论：待填写

### 20. `PHASE3_W2_0088_PUBLIC_AFFAIRS_CONTEXTUAL`

- 模式：`contextual`
- 文本：这次别只转发，得让他们真正看到人数
- 上下文：公共事务上下文触发风险讨论区；单句含义依赖前后互动；结合前文看 / 需要进一步核验
- 当前标签：`medium` / `E3_话题/热点触发` / hard_negative=`false`
- 初步风格标记：`none`
- 复核重点：上下文是否真的提升风险解释，medium 是否过度？
- 复核结论：待填写


## 政治历史/鉴证梗 `political_history`

### 21. `PHASE3_W2_0107_POLITICAL_HISTORY_WEAK_SIGNAL`

- 模式：`weak_signal`
- 文本：某个日期具有私人纪念意义，不能自动关联公共事件
- 上下文：政治历史鉴证梗高召回边界复核区；当前只有弱信号和不完整语境；普通解释也成立 / 先保留复核
- 当前标签：`low` / `C2_历史事件影射` / hard_negative=`true`
- 初步风格标记：`reviewer_voice`
- 复核重点：普通解释是否更强，low 是否仍值得召回？
- 复核结论：待填写

### 22. `PHASE3_W2_0108_POLITICAL_HISTORY_SAFE_CONTEXT`

- 模式：`safe_context`
- 文本：历史课程比较制度变迁，属于正常学术讨论
- 上下文：政治历史鉴证梗新闻教育与正常语境区；上下文提供完整反证；属于正常讨论 / 不要只看关键词
- 当前标签：`none` / `none` / hard_negative=`true`
- 初步风格标记：`none`
- 复核重点：反证是否完整，none 是否会造成漏判？
- 复核结论：待填写

### 23. `PHASE3_W2_0103_POLITICAL_HISTORY_CONTEXTUAL`

- 模式：`contextual`
- 文本：这集人物关系怎么看着像现实里的旧剧本
- 上下文：政治历史鉴证梗上下文触发风险讨论区；单句含义依赖前后互动；结合前文看 / 需要进一步核验
- 当前标签：`medium` / `C2_历史事件影射` / hard_negative=`false`
- 初步风格标记：`none`
- 复核重点：上下文是否真的提升风险解释，medium 是否过度？
- 复核结论：待填写

### 24. `PHASE3_W2_0098_POLITICAL_HISTORY_DIRECT`

- 模式：`direct`
- 文本：这个日期一到，评论区都知道在纪念什么
- 上下文：政治历史鉴证梗疑似明确风险互动区；有人继续追问具体条件；具体怎么走 / 公开区别留细节
- 当前标签：`high` / `C2_历史事件影射` / hard_negative=`false`
- 初步风格标记：`none`
- 复核重点：风险意图是否足够明确，high 是否合理？
- 复核结论：待填写


## 平台规避/审查黑话 `platform_censorship_evasion`

### 25. `PHASE3_W2_0120_PLATFORM_CENSORSHIP_EVASION_WEAK_SIGNAL`

- 模式：`weak_signal`
- 文本：用截图可能只是方便排版，不一定为了规避
- 上下文：平台规避审查黑话高召回边界复核区；当前只有弱信号和不完整语境；普通解释也成立 / 先保留复核
- 当前标签：`low` / `B4_符号/空格/Unicode 干扰` / hard_negative=`true`
- 初步风格标记：`reviewer_voice`
- 复核重点：普通解释是否更强，low 是否仍值得召回？
- 复核结论：待填写

### 26. `PHASE3_W2_0124_PLATFORM_CENSORSHIP_EVASION_SAFE_CONTEXT`

- 模式：`safe_context`
- 文本：论文使用首字母缩写并在首次出现时给出定义
- 上下文：平台规避审查黑话新闻教育与正常语境区；上下文提供完整反证；属于正常讨论 / 不要只看关键词
- 当前标签：`none` / `none` / hard_negative=`true`
- 初步风格标记：`none`
- 复核重点：反证是否完整，none 是否会造成漏判？
- 复核结论：待填写

### 27. `PHASE3_W2_0113_PLATFORM_CENSORSHIP_EVASION_DIRECT`

- 模式：`direct`
- 文本：全称换成拼音首字母，审核就不容易发现
- 上下文：平台规避审查黑话疑似明确风险互动区；有人继续追问具体条件；具体怎么走 / 公开区别留细节
- 当前标签：`high` / `B4_符号/空格/Unicode 干扰` / hard_negative=`false`
- 初步风格标记：`none`
- 复核重点：风险意图是否足够明确，high 是否合理？
- 复核结论：待填写

### 28. `PHASE3_W2_0114_PLATFORM_CENSORSHIP_EVASION_OBFUSCATED`

- 模式：`obfuscated`
- 文本：原字左右各加一个看不见的符号就能过
- 上下文：平台规避审查黑话规避表达与黑话讨论区；上级评论提示不要使用原词；暗号收到 / 换个写法
- 当前标签：`medium` / `B4_符号/空格/Unicode 干扰` / hard_negative=`false`
- 初步风格标记：`none`
- 复核重点：规避映射是否自然，medium 是否证据充分？
- 复核结论：待填写


## 网络黑产/安全风险 `cyber_abuse`

### 29. `PHASE3_W2_0136_CYBER_ABUSE_WEAK_SIGNAL`

- 模式：`weak_signal`
- 文本：查询实名可能是本人业务核验，需确认授权
- 上下文：网络黑产安全风险高召回边界复核区；当前只有弱信号和不完整语境；普通解释也成立 / 先保留复核
- 当前标签：`low` / `E1_平台黑话` / hard_negative=`true`
- 初步风格标记：`reviewer_voice`
- 复核重点：普通解释是否更强，low 是否仍值得召回？
- 复核结论：待填写

### 30. `PHASE3_W2_0140_CYBER_ABUSE_SAFE_CONTEXT`

- 模式：`safe_context`
- 文本：企业下线离职账号属于正常权限治理流程
- 上下文：网络黑产安全风险新闻教育与正常语境区；上下文提供完整反证；属于正常讨论 / 不要只看关键词
- 当前标签：`none` / `none` / hard_negative=`true`
- 初步风格标记：`none`
- 复核重点：反证是否完整，none 是否会造成漏判？
- 复核结论：待填写

### 31. `PHASE3_W2_0129_CYBER_ABUSE_OBFUSCATED`

- 模式：`obfuscated`
- 文本：验证码叫门票，问几秒出票就是问速度
- 上下文：网络黑产安全风险规避表达与黑话讨论区；上级评论提示不要使用原词；暗号收到 / 换个写法
- 当前标签：`medium` / `E1_平台黑话` / hard_negative=`false`
- 初步风格标记：`none`
- 复核重点：规避映射是否自然，medium 是否证据充分？
- 复核结论：待填写

### 32. `PHASE3_W2_0133_CYBER_ABUSE_CONTEXTUAL`

- 模式：`contextual`
- 文本：只知道号码也能查到住址吗，有现成渠道没
- 上下文：网络黑产安全风险上下文触发风险讨论区；单句含义依赖前后互动；结合前文看 / 需要进一步核验
- 当前标签：`medium` / `E1_平台黑话` / hard_negative=`false`
- 初步风格标记：`none`
- 复核重点：上下文是否真的提升风险解释，medium 是否过度？
- 复核结论：待填写


## 暴力极端 `violence_extremism`

### 33. `PHASE3_W2_0152_VIOLENCE_EXTREMISM_WEAK_SIGNAL`

- 模式：`weak_signal`
- 文本：敢过去带有挑衅意味，但尚无明确暴力内容
- 上下文：暴力极端高召回边界复核区；当前只有弱信号和不完整语境；普通解释也成立 / 先保留复核
- 当前标签：`low` / `E3_话题/热点触发` / hard_negative=`true`
- 初步风格标记：`reviewer_voice`
- 复核重点：普通解释是否更强，low 是否仍值得召回？
- 复核结论：待填写

### 34. `PHASE3_W2_0153_VIOLENCE_EXTREMISM_SAFE_CONTEXT`

- 模式：`safe_context`
- 文本：社区劝架员提醒发生冲突先报警并远离现场
- 上下文：暴力极端新闻教育与正常语境区；上下文提供完整反证；属于正常讨论 / 不要只看关键词
- 当前标签：`none` / `none` / hard_negative=`true`
- 初步风格标记：`none`
- 复核重点：反证是否完整，none 是否会造成漏判？
- 复核结论：待填写

### 35. `PHASE3_W2_0148_VIOLENCE_EXTREMISM_CONTEXTUAL`

- 模式：`contextual`
- 文本：大家到了听统一口令，不要自己先行动
- 上下文：暴力极端上下文触发风险讨论区；单句含义依赖前后互动；结合前文看 / 需要进一步核验
- 当前标签：`medium` / `E3_话题/热点触发` / hard_negative=`false`
- 初步风格标记：`none`
- 复核重点：上下文是否真的提升风险解释，medium 是否过度？
- 复核结论：待填写

### 36. `PHASE3_W2_0143_VIOLENCE_EXTREMISM_DIRECT`

- 模式：`direct`
- 文本：名单上的人一个都别放过，按地址分组找
- 上下文：暴力极端疑似明确风险互动区；有人继续追问具体条件；具体怎么走 / 公开区别留细节
- 当前标签：`high` / `E3_话题/热点触发` / hard_negative=`false`
- 初步风格标记：`none`
- 复核重点：风险意图是否足够明确，high 是否合理？
- 复核结论：待填写


## 违禁交易 `illegal_goods`

### 37. `PHASE3_W2_0165_ILLEGAL_GOODS_WEAK_SIGNAL`

- 模式：`weak_signal`
- 文本：问购药渠道可能是正常就医困难，也可能寻求违规来源
- 上下文：违禁交易高召回边界复核区；当前只有弱信号和不完整语境；普通解释也成立 / 先保留复核
- 当前标签：`low` / `C4_典故/物品/符号借用` / hard_negative=`true`
- 初步风格标记：`none`
- 复核重点：普通解释是否更强，low 是否仍值得召回？
- 复核结论：待填写

### 38. `PHASE3_W2_0169_ILLEGAL_GOODS_SAFE_CONTEXT`

- 模式：`safe_context`
- 文本：禁毒教育展示毒品伪装方式，是为了提高警惕
- 上下文：违禁交易新闻教育与正常语境区；上下文提供完整反证；属于正常讨论 / 不要只看关键词
- 当前标签：`none` / `none` / hard_negative=`true`
- 初步风格标记：`none`
- 复核重点：反证是否完整，none 是否会造成漏判？
- 复核结论：待填写

### 39. `PHASE3_W2_0158_ILLEGAL_GOODS_DIRECT`

- 模式：`direct`
- 文本：需要伪造证件的发照片和用途，最快当天出
- 上下文：违禁交易疑似明确风险互动区；有人继续追问具体条件；具体怎么走 / 公开区别留细节
- 当前标签：`high` / `C4_典故/物品/符号借用` / hard_negative=`false`
- 初步风格标记：`none`
- 复核重点：风险意图是否足够明确，high 是否合理？
- 复核结论：待填写

### 40. `PHASE3_W2_0159_ILLEGAL_GOODS_OBFUSCATED`

- 模式：`obfuscated`
- 文本：管制药叫蓝糖，问几盒就是问数量
- 上下文：违禁交易规避表达与黑话讨论区；上级评论提示不要使用原词；暗号收到 / 换个写法
- 当前标签：`medium` / `C4_典故/物品/符号借用` / hard_negative=`false`
- 初步风格标记：`none`
- 复核重点：规避映射是否自然，medium 是否证据充分？
- 复核结论：待填写


## 赌博 `gambling`

### 41. `PHASE3_W2_0181_GAMBLING_WEAK_SIGNAL`

- 模式：`weak_signal`
- 文本：老地方开桌可能只是朋友聚会，暂无线索证明下注
- 上下文：赌博高召回边界复核区；当前只有弱信号和不完整语境；普通解释也成立 / 先保留复核
- 当前标签：`low` / `E1_平台黑话` / hard_negative=`true`
- 初步风格标记：`reviewer_voice`
- 复核重点：普通解释是否更强，low 是否仍值得召回？
- 复核结论：待填写

### 42. `PHASE3_W2_0185_GAMBLING_SAFE_CONTEXT`

- 模式：`safe_context`
- 文本：体育节目分析赔率变化时同时提示理性观赛
- 上下文：赌博新闻教育与正常语境区；上下文提供完整反证；属于正常讨论 / 不要只看关键词
- 当前标签：`none` / `none` / hard_negative=`true`
- 初步风格标记：`none`
- 复核重点：反证是否完整，none 是否会造成漏判？
- 复核结论：待填写

### 43. `PHASE3_W2_0174_GAMBLING_OBFUSCATED`

- 模式：`obfuscated`
- 文本：下注改叫点菜，金额就按菜品数量发
- 上下文：赌博规避表达与黑话讨论区；上级评论提示不要使用原词；暗号收到 / 换个写法
- 当前标签：`medium` / `E1_平台黑话` / hard_negative=`false`
- 初步风格标记：`none`
- 复核重点：规避映射是否自然，medium 是否证据充分？
- 复核结论：待填写

### 44. `PHASE3_W2_0178_GAMBLING_CONTEXTUAL`

- 模式：`contextual`
- 文本：老地方桌子开了，还是按以前的底
- 上下文：赌博上下文触发风险讨论区；单句含义依赖前后互动；结合前文看 / 需要进一步核验
- 当前标签：`medium` / `E1_平台黑话` / hard_negative=`false`
- 初步风格标记：`none`
- 复核重点：上下文是否真的提升风险解释，medium 是否过度？
- 复核结论：待填写
