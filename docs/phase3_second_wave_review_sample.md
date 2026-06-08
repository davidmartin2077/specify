# 第三阶段第二波分层人工复核清单

本清单从第二波 185 条 raw 中确定性抽取 44 条，每个类别 4 条。候选原始标签未被修改。

复核回复格式建议：`ID：通过`，或 `ID：改为 medium，原因……`，或 `ID：退回，原因……`。


## 色情低俗 `sexual_content`

### 1. `PHASE3_W2_0016_SEXUAL_CONTENT_WEAK_SIGNAL`

- 模式：`weak_signal`
- 文本：深夜档是直播排班吧，这个标题别想太多
- 上下文：色情低俗二次回复里的普通解释；有人把原话往风险方向理解；也可能就是普通意思 / 先看前后文
- 当前标签：`low` / `E1_平台黑话` / hard_negative=`true`
- 初步风格标记：`none`
- 复核重点：普通解释是否更强，low 是否仍值得召回？
- 复核结论：待填写

### 2. `PHASE3_W2_0022_SEXUAL_CONTENT_SAFE_CONTEXT`

- 模式：`safe_context`
- 文本：性健康门诊面向成年人提供正规咨询和检测
- 上下文：色情低俗普通用户转述正常场景；前文在分享新闻、课程或正规流程；这个是在提醒大家 / 别只截半句话
- 当前标签：`none` / `none` / hard_negative=`true`
- 初步风格标记：`none`
- 复核重点：反证是否完整，none 是否会造成漏判？
- 复核结论：待填写

### 3. `PHASE3_W2_0003_SEXUAL_CONTENT_DIRECT`

- 模式：`direct`
- 文本：陪酒之后还能安排别的，费用另算
- 上下文：色情低俗评论区私聊暗示；有人继续追问具体条件；具体怎么走 / 公开区别留细节
- 当前标签：`high` / `E1_平台黑话` / hard_negative=`false`
- 初步风格标记：`none`
- 复核重点：风险意图是否足够明确，high 是否合理？
- 复核结论：待填写

### 4. `PHASE3_W2_0009_SEXUAL_CONTENT_OBFUSCATED`

- 模式：`obfuscated`
- 文本：联系方式藏在尺码表里，按最大码找
- 上下文：色情低俗群聊暗号接话；上级评论提醒最近别写太直；收到暗号 / 换个说法
- 当前标签：`medium` / `E1_平台黑话` / hard_negative=`false`
- 初步风格标记：`none`
- 复核重点：规避映射是否自然，medium 是否证据充分？
- 复核结论：待填写


## 广告/诈骗/导流 `spam_ads_fraud`

### 5. `PHASE3_W2_0042_SPAM_ADS_FRAUD_WEAK_SIGNAL`

- 模式：`weak_signal`
- 文本：内部名额听着像卖课话术，但还没让交钱
- 上下文：广告诈骗导流二次回复里的普通解释；有人把原话往风险方向理解；也可能就是普通意思 / 先看前后文
- 当前标签：`low` / `E1_平台黑话` / hard_negative=`true`
- 初步风格标记：`none`
- 复核重点：普通解释是否更强，low 是否仍值得召回？
- 复核结论：待填写

### 6. `PHASE3_W2_0048_SPAM_ADS_FRAUD_SAFE_CONTEXT`

- 模式：`safe_context`
- 文本：我妈差点把验证码报出去，还好银行客服拦住了
- 上下文：广告诈骗导流普通用户转述正常场景；前文在分享新闻、课程或正规流程；这个是在提醒大家 / 别只截半句话
- 当前标签：`none` / `none` / hard_negative=`true`
- 初步风格标记：`none`
- 复核重点：反证是否完整，none 是否会造成漏判？
- 复核结论：待填写

### 7. `PHASE3_W2_0034_SPAM_ADS_FRAUD_OBFUSCATED`

- 模式：`obfuscated`
- 文本：想进果汁群的别问钱，几杯自己报
- 上下文：广告诈骗导流群聊暗号接话；上级评论提醒最近别写太直；收到暗号 / 换个说法
- 当前标签：`medium` / `E1_平台黑话` / hard_negative=`false`
- 初步风格标记：`none`
- 复核重点：规避映射是否自然，medium 是否证据充分？
- 复核结论：待填写

### 8. `PHASE3_W2_0040_SPAM_ADS_FRAUD_CONTEXTUAL`

- 模式：`contextual`
- 文本：他一直催我先垫钱，说错过就不能恢复
- 上下文：广告诈骗导流回复链里的追问；前文正在讨论类似情况；这话接着前面看 / 感觉不太对劲
- 当前标签：`medium` / `E1_平台黑话` / hard_negative=`false`
- 初步风格标记：`none`
- 复核重点：上下文是否真的提升风险解释，medium 是否过度？
- 复核结论：待填写


## 辱骂/群体攻击 `insulting_abuse`

### 9. `PHASE3_W2_0062_INSULTING_ABUSE_WEAK_SIGNAL`

- 模式：`weak_signal`
- 文本：灰头像不就是默认头像吗，别见一个就扣帽子
- 上下文：辱骂群体攻击二次回复里的普通解释；有人把原话往风险方向理解；也可能就是普通意思 / 先看前后文
- 当前标签：`low` / `D3_借代` / hard_negative=`true`
- 初步风格标记：`none`
- 复核重点：普通解释是否更强，low 是否仍值得召回？
- 复核结论：待填写

### 10. `PHASE3_W2_0063_INSULTING_ABUSE_SAFE_CONTEXT`

- 模式：`safe_context`
- 文本：这个公益片明明是在反歧视，别只截那句脏话
- 上下文：辱骂群体攻击普通用户转述正常场景；前文在分享新闻、课程或正规流程；这个是在提醒大家 / 别只截半句话
- 当前标签：`none` / `none` / hard_negative=`true`
- 初步风格标记：`none`
- 复核重点：反证是否完整，none 是否会造成漏判？
- 复核结论：待填写

### 11. `PHASE3_W2_0058_INSULTING_ABUSE_CONTEXTUAL`

- 模式：`contextual`
- 文本：一听他说做什么工作的，我就知道评论没法看
- 上下文：辱骂群体攻击回复链里的追问；前文正在讨论类似情况；这话接着前面看 / 感觉不太对劲
- 当前标签：`medium` / `D3_借代` / hard_negative=`false`
- 初步风格标记：`none`
- 复核重点：上下文是否真的提升风险解释，medium 是否过度？
- 复核结论：待填写

### 12. `PHASE3_W2_0053_INSULTING_ABUSE_DIRECT`

- 模式：`direct`
- 文本：这类病人活该被排斥，别让他们进社区
- 上下文：辱骂群体攻击评论区私聊暗示；有人继续追问具体条件；具体怎么走 / 公开区别留细节
- 当前标签：`high` / `D3_借代` / hard_negative=`false`
- 初步风格标记：`none`
- 复核重点：风险意图是否足够明确，high 是否合理？
- 复核结论：待填写


## 枪爆武器 `weapons_explosives`

### 13. `PHASE3_W2_0075_WEAPONS_EXPLOSIVES_WEAK_SIGNAL`

- 模式：`weak_signal`
- 文本：这不就是修车用的管子和弹簧吗，别吓人
- 上下文：枪爆武器二次回复里的普通解释；有人把原话往风险方向理解；也可能就是普通意思 / 先看前后文
- 当前标签：`low` / `C4_典故/物品/符号借用` / hard_negative=`true`
- 初步风格标记：`none`
- 复核重点：普通解释是否更强，low 是否仍值得召回？
- 复核结论：待填写

### 14. `PHASE3_W2_0079_WEAPONS_EXPLOSIVES_SAFE_CONTEXT`

- 模式：`safe_context`
- 文本：消防课讲这个，是提醒别乱碰危险品
- 上下文：枪爆武器普通用户转述正常场景；前文在分享新闻、课程或正规流程；这个是在提醒大家 / 别只截半句话
- 当前标签：`none` / `none` / hard_negative=`true`
- 初步风格标记：`none`
- 复核重点：反证是否完整，none 是否会造成漏判？
- 复核结论：待填写

### 15. `PHASE3_W2_0068_WEAPONS_EXPLOSIVES_DIRECT`

- 模式：`direct`
- 文本：这批管制刀具不开票，同城可以当面拿
- 上下文：枪爆武器评论区私聊暗示；有人继续追问具体条件；具体怎么走 / 公开区别留细节
- 当前标签：`high` / `C4_典故/物品/符号借用` / hard_negative=`false`
- 初步风格标记：`none`
- 复核重点：风险意图是否足够明确，high 是否合理？
- 复核结论：待填写

### 16. `PHASE3_W2_0069_WEAPONS_EXPLOSIVES_OBFUSCATED`

- 模式：`obfuscated`
- 文本：老钟表还有吗，走得响不响你应该懂
- 上下文：枪爆武器群聊暗号接话；上级评论提醒最近别写太直；收到暗号 / 换个说法
- 当前标签：`medium` / `C4_典故/物品/符号借用` / hard_negative=`false`
- 初步风格标记：`none`
- 复核重点：规避映射是否自然，medium 是否证据充分？
- 复核结论：待填写


## 公共事务 `public_affairs`

### 17. `PHASE3_W2_0091_PUBLIC_AFFAIRS_WEAK_SIGNAL`

- 模式：`weak_signal`
- 文本：他说多叫几个人去门口，也可能只是想有人作证
- 上下文：公共事务二次回复里的普通解释；有人把原话往风险方向理解；也可能就是普通意思 / 先看前后文
- 当前标签：`low` / `E3_话题/热点触发` / hard_negative=`true`
- 初步风格标记：`none`
- 复核重点：普通解释是否更强，low 是否仍值得召回？
- 复核结论：待填写

### 18. `PHASE3_W2_0095_PUBLIC_AFFAIRS_SAFE_CONTEXT`

- 模式：`safe_context`
- 文本：新闻把当事人电话打码了，这点还挺必要
- 上下文：公共事务普通用户转述正常场景；前文在分享新闻、课程或正规流程；这个是在提醒大家 / 别只截半句话
- 当前标签：`none` / `none` / hard_negative=`true`
- 初步风格标记：`none`
- 复核重点：反证是否完整，none 是否会造成漏判？
- 复核结论：待填写

### 19. `PHASE3_W2_0084_PUBLIC_AFFAIRS_OBFUSCATED`

- 模式：`obfuscated`
- 文本：今晚看房的还是老地方，别在群名里写集合
- 上下文：公共事务群聊暗号接话；上级评论提醒最近别写太直；收到暗号 / 换个说法
- 当前标签：`medium` / `E3_话题/热点触发` / hard_negative=`false`
- 初步风格标记：`none`
- 复核重点：规避映射是否自然，medium 是否证据充分？
- 复核结论：待填写

### 20. `PHASE3_W2_0088_PUBLIC_AFFAIRS_CONTEXTUAL`

- 模式：`contextual`
- 文本：这次别只转发，得让他们真正看到人数
- 上下文：公共事务回复链里的追问；前文正在讨论类似情况；这话接着前面看 / 感觉不太对劲
- 当前标签：`medium` / `E3_话题/热点触发` / hard_negative=`false`
- 初步风格标记：`none`
- 复核重点：上下文是否真的提升风险解释，medium 是否过度？
- 复核结论：待填写


## 政治历史/鉴证梗 `political_history`

### 21. `PHASE3_W2_0107_POLITICAL_HISTORY_WEAK_SIGNAL`

- 模式：`weak_signal`
- 文本：我发这个日期是家里纪念日，别往大事上带
- 上下文：政治历史鉴证梗二次回复里的普通解释；有人把原话往风险方向理解；也可能就是普通意思 / 先看前后文
- 当前标签：`low` / `C2_历史事件影射` / hard_negative=`true`
- 初步风格标记：`none`
- 复核重点：普通解释是否更强，low 是否仍值得召回？
- 复核结论：待填写

### 22. `PHASE3_W2_0108_POLITICAL_HISTORY_SAFE_CONTEXT`

- 模式：`safe_context`
- 文本：这节课就是讲制度变迁，老师没提现实人物
- 上下文：政治历史鉴证梗普通用户转述正常场景；前文在分享新闻、课程或正规流程；这个是在提醒大家 / 别只截半句话
- 当前标签：`none` / `none` / hard_negative=`true`
- 初步风格标记：`none`
- 复核重点：反证是否完整，none 是否会造成漏判？
- 复核结论：待填写

### 23. `PHASE3_W2_0103_POLITICAL_HISTORY_CONTEXTUAL`

- 模式：`contextual`
- 文本：这集人物关系怎么看着像现实里的旧剧本
- 上下文：政治历史鉴证梗回复链里的追问；前文正在讨论类似情况；这话接着前面看 / 感觉不太对劲
- 当前标签：`medium` / `C2_历史事件影射` / hard_negative=`false`
- 初步风格标记：`none`
- 复核重点：上下文是否真的提升风险解释，medium 是否过度？
- 复核结论：待填写

### 24. `PHASE3_W2_0098_POLITICAL_HISTORY_DIRECT`

- 模式：`direct`
- 文本：这个日期一到，评论区都知道在纪念什么
- 上下文：政治历史鉴证梗评论区私聊暗示；有人继续追问具体条件；具体怎么走 / 公开区别留细节
- 当前标签：`high` / `C2_历史事件影射` / hard_negative=`false`
- 初步风格标记：`none`
- 复核重点：风险意图是否足够明确，high 是否合理？
- 复核结论：待填写


## 平台规避/审查黑话 `platform_censorship_evasion`

### 25. `PHASE3_W2_0120_PLATFORM_CENSORSHIP_EVASION_WEAK_SIGNAL`

- 模式：`weak_signal`
- 文本：截图发出来好看一点吧，不一定是怕被删
- 上下文：平台规避审查黑话二次回复里的普通解释；有人把原话往风险方向理解；也可能就是普通意思 / 先看前后文
- 当前标签：`low` / `B4_符号/空格/Unicode 干扰` / hard_negative=`true`
- 初步风格标记：`none`
- 复核重点：普通解释是否更强，low 是否仍值得召回？
- 复核结论：待填写

### 26. `PHASE3_W2_0124_PLATFORM_CENSORSHIP_EVASION_SAFE_CONTEXT`

- 模式：`safe_context`
- 文本：论文使用首字母缩写并在首次出现时给出定义
- 上下文：平台规避审查黑话普通用户转述正常场景；前文在分享新闻、课程或正规流程；这个是在提醒大家 / 别只截半句话
- 当前标签：`none` / `none` / hard_negative=`true`
- 初步风格标记：`none`
- 复核重点：反证是否完整，none 是否会造成漏判？
- 复核结论：待填写

### 27. `PHASE3_W2_0113_PLATFORM_CENSORSHIP_EVASION_DIRECT`

- 模式：`direct`
- 文本：全称别写了，三个首字母评论区自己懂
- 上下文：平台规避审查黑话评论区私聊暗示；有人继续追问具体条件；具体怎么走 / 公开区别留细节
- 当前标签：`high` / `B4_符号/空格/Unicode 干扰` / hard_negative=`false`
- 初步风格标记：`none`
- 复核重点：风险意图是否足够明确，high 是否合理？
- 复核结论：待填写

### 28. `PHASE3_W2_0114_PLATFORM_CENSORSHIP_EVASION_OBFUSCATED`

- 模式：`obfuscated`
- 文本：左右各垫一点空白，看起来还是原来那几个字
- 上下文：平台规避审查黑话群聊暗号接话；上级评论提醒最近别写太直；收到暗号 / 换个说法
- 当前标签：`medium` / `B4_符号/空格/Unicode 干扰` / hard_negative=`false`
- 初步风格标记：`none`
- 复核重点：规避映射是否自然，medium 是否证据充分？
- 复核结论：待填写


## 网络黑产/安全风险 `cyber_abuse`

### 29. `PHASE3_W2_0136_CYBER_ABUSE_WEAK_SIGNAL`

- 模式：`weak_signal`
- 文本：查实名是查我自己的账号，别乱开别人信息
- 上下文：网络黑产安全风险二次回复里的普通解释；有人把原话往风险方向理解；也可能就是普通意思 / 先看前后文
- 当前标签：`low` / `E1_平台黑话` / hard_negative=`true`
- 初步风格标记：`none`
- 复核重点：普通解释是否更强，low 是否仍值得召回？
- 复核结论：待填写

### 30. `PHASE3_W2_0140_CYBER_ABUSE_SAFE_CONTEXT`

- 模式：`safe_context`
- 文本：离职同事的账号今天统一下线，权限别留着
- 上下文：网络黑产安全风险普通用户转述正常场景；前文在分享新闻、课程或正规流程；这个是在提醒大家 / 别只截半句话
- 当前标签：`none` / `none` / hard_negative=`true`
- 初步风格标记：`none`
- 复核重点：反证是否完整，none 是否会造成漏判？
- 复核结论：待填写

### 31. `PHASE3_W2_0129_CYBER_ABUSE_OBFUSCATED`

- 模式：`obfuscated`
- 文本：门票几秒能出来？我这边要批量验一波
- 上下文：网络黑产安全风险群聊暗号接话；上级评论提醒最近别写太直；收到暗号 / 换个说法
- 当前标签：`medium` / `E1_平台黑话` / hard_negative=`false`
- 初步风格标记：`none`
- 复核重点：规避映射是否自然，medium 是否证据充分？
- 复核结论：待填写

### 32. `PHASE3_W2_0133_CYBER_ABUSE_CONTEXTUAL`

- 模式：`contextual`
- 文本：只知道号码也能查到住址吗，有现成渠道没
- 上下文：网络黑产安全风险回复链里的追问；前文正在讨论类似情况；这话接着前面看 / 感觉不太对劲
- 当前标签：`medium` / `E1_平台黑话` / hard_negative=`false`
- 初步风格标记：`none`
- 复核重点：上下文是否真的提升风险解释，medium 是否过度？
- 复核结论：待填写


## 暴力极端 `violence_extremism`

### 33. `PHASE3_W2_0152_VIOLENCE_EXTREMISM_WEAK_SIGNAL`

- 模式：`weak_signal`
- 文本：他说敢不敢过去，听着冲，但也可能只是吵架嘴硬
- 上下文：暴力极端二次回复里的普通解释；有人把原话往风险方向理解；也可能就是普通意思 / 先看前后文
- 当前标签：`low` / `E3_话题/热点触发` / hard_negative=`true`
- 初步风格标记：`none`
- 复核重点：普通解释是否更强，low 是否仍值得召回？
- 复核结论：待填写

### 34. `PHASE3_W2_0153_VIOLENCE_EXTREMISM_SAFE_CONTEXT`

- 模式：`safe_context`
- 文本：邻居群都在劝先报警，别再往现场凑了
- 上下文：暴力极端普通用户转述正常场景；前文在分享新闻、课程或正规流程；这个是在提醒大家 / 别只截半句话
- 当前标签：`none` / `none` / hard_negative=`true`
- 初步风格标记：`none`
- 复核重点：反证是否完整，none 是否会造成漏判？
- 复核结论：待填写

### 35. `PHASE3_W2_0148_VIOLENCE_EXTREMISM_CONTEXTUAL`

- 模式：`contextual`
- 文本：大家到了听统一口令，不要自己先行动
- 上下文：暴力极端回复链里的追问；前文正在讨论类似情况；这话接着前面看 / 感觉不太对劲
- 当前标签：`medium` / `E3_话题/热点触发` / hard_negative=`false`
- 初步风格标记：`none`
- 复核重点：上下文是否真的提升风险解释，medium 是否过度？
- 复核结论：待填写

### 36. `PHASE3_W2_0143_VIOLENCE_EXTREMISM_DIRECT`

- 模式：`direct`
- 文本：名单上的人一个都别放过，按地址分组找
- 上下文：暴力极端评论区私聊暗示；有人继续追问具体条件；具体怎么走 / 公开区别留细节
- 当前标签：`high` / `E3_话题/热点触发` / hard_negative=`false`
- 初步风格标记：`none`
- 复核重点：风险意图是否足够明确，high 是否合理？
- 复核结论：待填写


## 违禁交易 `illegal_goods`

### 37. `PHASE3_W2_0165_ILLEGAL_GOODS_WEAK_SIGNAL`

- 模式：`weak_signal`
- 文本：医院没号我才问哪里能买药，不是要走歪门路
- 上下文：违禁交易二次回复里的普通解释；有人把原话往风险方向理解；也可能就是普通意思 / 先看前后文
- 当前标签：`low` / `C4_典故/物品/符号借用` / hard_negative=`true`
- 初步风格标记：`none`
- 复核重点：普通解释是否更强，low 是否仍值得召回？
- 复核结论：待填写

### 38. `PHASE3_W2_0169_ILLEGAL_GOODS_SAFE_CONTEXT`

- 模式：`safe_context`
- 文本：禁毒课放那些伪装图，是提醒大家别上当
- 上下文：违禁交易普通用户转述正常场景；前文在分享新闻、课程或正规流程；这个是在提醒大家 / 别只截半句话
- 当前标签：`none` / `none` / hard_negative=`true`
- 初步风格标记：`none`
- 复核重点：反证是否完整，none 是否会造成漏判？
- 复核结论：待填写

### 39. `PHASE3_W2_0158_ILLEGAL_GOODS_DIRECT`

- 模式：`direct`
- 文本：需要伪造证件的发照片和用途，最快当天出
- 上下文：违禁交易评论区私聊暗示；有人继续追问具体条件；具体怎么走 / 公开区别留细节
- 当前标签：`high` / `C4_典故/物品/符号借用` / hard_negative=`false`
- 初步风格标记：`none`
- 复核重点：风险意图是否足够明确，high 是否合理？
- 复核结论：待填写

### 40. `PHASE3_W2_0159_ILLEGAL_GOODS_OBFUSCATED`

- 模式：`obfuscated`
- 文本：管制药叫蓝糖，问几盒就是问数量
- 上下文：违禁交易群聊暗号接话；上级评论提醒最近别写太直；收到暗号 / 换个说法
- 当前标签：`medium` / `C4_典故/物品/符号借用` / hard_negative=`false`
- 初步风格标记：`none`
- 复核重点：规避映射是否自然，medium 是否证据充分？
- 复核结论：待填写


## 赌博 `gambling`

### 41. `PHASE3_W2_0181_GAMBLING_WEAK_SIGNAL`

- 模式：`weak_signal`
- 文本：老地方开桌也可能就是朋友打牌，不一定下钱
- 上下文：赌博二次回复里的普通解释；有人把原话往风险方向理解；也可能就是普通意思 / 先看前后文
- 当前标签：`low` / `E1_平台黑话` / hard_negative=`true`
- 初步风格标记：`none`
- 复核重点：普通解释是否更强，low 是否仍值得召回？
- 复核结论：待填写

### 42. `PHASE3_W2_0185_GAMBLING_SAFE_CONTEXT`

- 模式：`safe_context`
- 文本：体育节目聊赔率，也一直提醒别拿它下注
- 上下文：赌博普通用户转述正常场景；前文在分享新闻、课程或正规流程；这个是在提醒大家 / 别只截半句话
- 当前标签：`none` / `none` / hard_negative=`true`
- 初步风格标记：`none`
- 复核重点：反证是否完整，none 是否会造成漏判？
- 复核结论：待填写

### 43. `PHASE3_W2_0174_GAMBLING_OBFUSCATED`

- 模式：`obfuscated`
- 文本：今晚点菜按老规矩，几盘就是几手
- 上下文：赌博群聊暗号接话；上级评论提醒最近别写太直；收到暗号 / 换个说法
- 当前标签：`medium` / `E1_平台黑话` / hard_negative=`false`
- 初步风格标记：`none`
- 复核重点：规避映射是否自然，medium 是否证据充分？
- 复核结论：待填写

### 44. `PHASE3_W2_0178_GAMBLING_CONTEXTUAL`

- 模式：`contextual`
- 文本：老地方桌子开了，还是按以前的底
- 上下文：赌博回复链里的追问；前文正在讨论类似情况；这话接着前面看 / 感觉不太对劲
- 当前标签：`medium` / `E1_平台黑话` / hard_negative=`false`
- 初步风格标记：`none`
- 复核重点：上下文是否真的提升风险解释，medium 是否过度？
- 复核结论：待填写
