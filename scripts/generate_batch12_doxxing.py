#!/usr/bin/env python3
"""
Generate batch12: Doxxing / 开盒 / 人肉搜索 coverage.

Zero existing coverage for "开盒" in 1255 samples.
Doxxing is a real cybersecurity threat — posting personal info,
threatening to reveal identities, trading illegal data.

Scenarios covered:
1. 开盒威胁 — threatening to dox someone
2. 社工库/查档 — illegal personal data lookup services
3. 人肉搜索号召 — calling for mass doxxing
4. 个人信息已泄露 — actual disclosure patterns
5. 定位/IP泄露 — location/network exposure
6. 隐私交易 — buying/selling personal data

Risk: mostly high (doxxing is illegal under 个人信息保护法)
Tone: natural 贴吧/评论区/Telegram口吻, non-template, 有网感
"""

import json
from pathlib import Path
from collections import Counter

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "data/raw/batch12_doxxing.jsonl"

samples = []


def add(text, risk_level, encoding_primary, encoding_secondary,
        needs_context, hard_negative, literal_analysis, encoding_analysis,
        context_analysis, supporting_evidence, counter_evidence, final_rationale,
        context=None, ambiguity="low", evidence_strength="strong"):
    if context is None:
        context = {}
    if not isinstance(encoding_secondary, list):
        encoding_secondary = [encoding_secondary]
    samples.append({
        "id": f"BC_{len(samples)+1:04d}",
        "source_type": "synthetic",
        "text": text, "risk_level": risk_level,
        "encoding_primary": encoding_primary,
        "encoding_secondary": encoding_secondary,
        "needs_context": needs_context, "hard_negative": hard_negative,
        "ambiguity": ambiguity, "evidence_strength": evidence_strength,
        "reasoning": {
            "literal_analysis": literal_analysis,
            "encoding_analysis": encoding_analysis,
            "context_analysis": context_analysis,
            "supporting_evidence": supporting_evidence,
            "counter_evidence": counter_evidence,
            "final_rationale": final_rationale,
        },
        "context": context, "quality_status": "reviewed",
        "review_notes": "source=batch12_doxxing;",
    })


# ================================================================
# SECTION 1: 开盒威胁 — 直接威胁要曝光他人信息 (8 samples)
# 贴吧/评论区对线场景，吵架中说要开盒对方
# ================================================================

add(
    text="你再骂一句试试？信不信老子把你开了，你妈电话我都查得到",
    risk_level="high",
    encoding_primary="E1_平台黑话",
    encoding_secondary=["C3_数字/代码", "D1_威胁"],
    needs_context=False, hard_negative=False,
    literal_analysis=["文本表面是对线吵架中的威胁：声称能查到对方母亲的电话，是典型的'开盒'威胁——以公开个人隐私为武器进行恐吓。"],
    encoding_analysis=["'把你开了'='开盒'的口语化缩写，中文互联网黑话，指公开他人真实身份信息(姓名/电话/住址/工作单位等)。'你妈电话我都查得到'暗示已掌握或能获取对方家庭成员的隐私数据。此类威胁在贴吧/微博/游戏社区对线中极为常见，属于利用非法手段获取个人信息进行恐吓的典型模式。"],
    context_analysis=["无额外上下文。裸文本中'开了'+'电话查得到'的信号组合足以判为开盒威胁——这是中文互联网已高度固化的违规话语模式。"],
    supporting_evidence=["(1)'把你开了'=开盒威胁的直接口语表达；(2)'你妈电话'=扩大威胁范围至家庭成员；(3)声称'查得到'暗示已掌握非法查询渠道。三重信号明确指向开盒恐吓。"],
    counter_evidence=["可能是键盘侠口嗨——实际没有查询能力。但威胁本身的目的就是恐吓，无论是否真能查到，行为性质已构成违规。"],
    final_rationale="明确的开盒威胁+家庭成员隐私恐吓，属于个人信息保护法严厉打击的行为，判为 high。",
)

add(
    text="你IP不是杭州的嘛，西湖区的是吧，还要我继续说吗？",
    risk_level="high",
    encoding_primary="E1_平台黑话",
    encoding_secondary=["C1_地理位置暴露", "D1_威胁"],
    needs_context=False, hard_negative=False,
    literal_analysis=["文本表面是对对方地理位置的逐步精确揭露——先指出城市(杭州)，再缩到区(西湖区)，以'还要我继续说吗'作为威胁收尾。"],
    encoding_analysis=["'IP不是杭州的嘛'——利用网络IP地址反推地理位置是开盒常见手段。'西湖区'的精确化暗示掌握的信息远超IP粗定位，可能已通过社工库等渠道获取了更详细的个人信息。'还要我继续说吗'=威胁升级——再往下就是具体街道/小区/姓名。这是典型的渐进式开盒恐吓：先抛一部分信息证明'我真的查了'，再暗示还有更多。"],
    context_analysis=["无额外上下文。逐步精确化+威胁升级的修辞模式在裸文本中已经清晰。"],
    supporting_evidence=["(1)利用IP/网络信息定位对方地理位置；(2)从城市到区的逐步精确化证明信息获取能力；(3)'还要我继续说吗'=明确的隐晦威胁。三条都是开盒的标准模式。"],
    counter_evidence=["IP地理位置信息本身是公开可获取的。但配合威胁语式('还要我继续说吗')和逐步精确化的修辞，已超出正常地理讨论。"],
    final_rationale="IP定位+渐进式开盒威胁，地理位置精确化暗示已掌握更多隐私，判为 high。",
)

add(
    text="哈哈你继续叫，我这边已经查到你的实名了，要不要我念出来给大家听？",
    risk_level="high",
    encoding_primary="E1_平台黑话",
    encoding_secondary=["C3_数字/代码", "D1_威胁"],
    needs_context=False, hard_negative=False,
    literal_analysis=["文本是以嘲笑口吻宣布已掌握对方实名信息，并以公开念出为威胁手段。"],
    encoding_analysis=["'查到你的实名'——实名信息(姓名+身份证号)是最高敏感等级的个人信息。'念出来给大家听'=公开披露的威胁。文本巧妙利用了'念'这个动作——将公开个人信息包装成一种'表演'，降低了威胁的严肃感但实质不变。这是社交平台对线中常见的开盒炫耀模式。"],
    context_analysis=["无额外上下文。'实名'+'念出来'的组合是开盒行为的标准话语模式。"],
    supporting_evidence=["(1)声称已获取实名信息；(2)以公开发布为威胁；(3)'查到'暗示使用了非法查询渠道。明确的开盒威胁。"],
    counter_evidence=["可能是虚张声势。但威胁行为本身——声称掌握并要公开他人实名——即构成违规，无论是否真的掌握了。"],
    final_rationale="实名信息+公开威胁，开盒行为的核心模式，判为 high。",
)

add(
    text="别以为你匿名就没事，这年头想查一个人简简单单，你的号我已经存了",
    risk_level="high",
    encoding_primary="E1_平台黑话",
    encoding_secondary=["D1_威胁"],
    needs_context=False, hard_negative=False,
    literal_analysis=["文本告知对方：即使匿名也无法隐藏身份，并声称已保存对方账号信息以备后续查证。"],
    encoding_analysis=["'匿名就没事'指出了对方的心理预期——以为匿名可以保护自己。'想查一个人简简单单'暗示存在便捷的非法查询渠道(社工库/内部泄漏数据等)。'号已经存了'=已将对方账号标记为查询目标。这是非即时性威胁——不一定现在开，但保留了随时开的可能，对受害者造成持久心理压力。"],
    context_analysis=["无额外上下文。针对匿名用户的身份暴露威胁是开盒的典型场景。"],
    supporting_evidence=["(1)针对匿名用户的去匿名化威胁；(2)'查一个人简简单单'暗示非法渠道可得性；(3)保存账号=标记目标。三条指向持续性的开盒威胁。"],
    counter_evidence=["未明确说出'开盒'或具体个人信息。但'查一个人'+'存号'的组合已构成清晰的人身威胁。"],
    final_rationale="匿名破解+持续威胁+非法渠道暗示，构成开盒恐吓，判为 high。",
)

add(
    text="你们群那个叫'清风'的管理，真名是不是姓王？安徽人吧",
    risk_level="high",
    encoding_primary="E1_平台黑话",
    encoding_secondary=["C1_地理位置暴露", "C1_人物代指"],
    needs_context=False, hard_negative=False,
    literal_analysis=["文本表面上是在询问确认一个人的真名和籍贯，但采用的是暗示已经知道答案的反问句式。"],
    encoding_analysis=["'真名是不是姓王'+'安徽人吧'——在公开群聊中透露他人真实姓名和籍贯信息，且采用的是反问句式暗示'我已经查过了'。即使以疑问句包装，在公开场合暴露他人线下身份信息的意图是明确的。这种'似问实曝'的模式是开盒者常用的规避手法——以'我只是在问'来掩饰实际的信息公开行为。"],
    context_analysis=["无额外上下文。在群聊中公开他人真实身份信息、尤其是使用反问句式暗示已掌握信息，是典型的信息公开骚扰。"],
    supporting_evidence=["(1)公开场合(群聊)暴露他人线下真实身份；(2)反问句式=已查证的暗示；(3)姓名+籍贯的组合信息足以定位到特定个人。构成个人信息非法公开。"],
    counter_evidence=["可能是认识的人之间开玩笑。但'你们群那个叫XX的管理'表明说话者与目标并非熟识关系——是通过网络信息查询获得的陌生人的线下信息。"],
    final_rationale="公开他人真实姓名+籍贯，'似问实曝'的规避模式，属于个人信息非法公开，判为 high。",
)

add(
    text="笑了，你跟我对线之前能不能先看看自己发过什么帖？家庭地址工作单位我都能给你翻出来",
    risk_level="high",
    encoding_primary="E1_平台黑话",
    encoding_secondary=["D1_威胁", "C2_历史事件影射"],
    needs_context=False, hard_negative=False,
    literal_analysis=["文本以嘲笑开始，威胁通过翻查对方历史发帖来挖掘家庭地址和工作单位等隐私信息。"],
    encoding_analysis=["'看看自己发过什么帖'暗示通过对方的社交网络历史记录进行信息拼图——这是人肉搜索的基础手段。'家庭地址工作单位我都能给你翻出来'直接将威胁明确化——不是可能查到，而是'都能'，表达了确定的获取能力。'翻出来'一词形象地描述了从海量网络数据中挖掘拼凑个人信息的'人肉'过程。"],
    context_analysis=["无额外上下文。通过社交网络信息拼图进行人肉是开盒的主要技术路径之一。"],
    supporting_evidence=["(1)威胁通过历史帖子挖掘个人信息；(2)明确声称能获取家庭地址和工作单位——两类最高敏感的隐私信息；(3)威胁已具体化而非抽象恐吓。构成信息拼图式人肉威胁。"],
    counter_evidence=["可能只是口头威胁，实际无能力。但声称要挖掘并公开他人家庭地址和工作单位的威胁本身已是违规行为。"],
    final_rationale="社交网络信息拼图+家庭地址/工作单位明确威胁，人肉搜索的标准模式，判为 high。",
)

add(
    text="哦你就是那个在隔壁贴骂人的？我帮你回忆一下啊，你去年是不是说过你在XX公司上班？要不要我帮你@你们HR",
    risk_level="high",
    encoding_primary="E1_平台黑话",
    encoding_secondary=["C1_人物代指", "D1_威胁"],
    needs_context=False, hard_negative=False,
    literal_analysis=["文本表面'友好'地帮对方回忆过往发言，实际是威胁将对方的历史言论发送给其雇主HR。"],
    encoding_analysis=["'帮你回忆'——经典的反讽包装，实际是威胁。'XX公司'——已掌握对方工作单位。'帮你@你们HR'=威胁破坏对方职业生涯——这是开盒的高级形式：不仅暴露身份，还利用暴露的信息对受害者进行线下骚扰(联系雇主/家人)。文本采用'帮你'的伪善口吻，是中文互联网'阴阳怪气'文化的典型表达。"],
    context_analysis=["无额外上下文。职场威胁是开盒行为的严重升级——将网络冲突延伸至受害者的线下生活和职业生涯。"],
    supporting_evidence=["(1)已掌握对方工作单位信息；(2)威胁联系HR=现实生活骚扰；(3)'帮你'的反讽口吻表明恶意意图。这是开盒+线下骚扰的复合威胁。"],
    counter_evidence=["可能需要更多上下文确认是否真实掌握工作单位信息。但文本声称已掌握+威胁联系HR的组合，裸文本即可判。"],
    final_rationale="工作单位暴露+线下职场骚扰威胁，开盒行为的严重升级形式，判为 high。",
)

add(
    text="别跟我装了，你微信号后面那几位是不是7410？头像是个女的吧，你女朋友？挺漂亮的",
    risk_level="high",
    encoding_primary="E1_平台黑话",
    encoding_secondary=["C3_数字/代码", "D1_威胁"],
    needs_context=False, hard_negative=False,
    literal_analysis=["文本声称知道对方微信号的部分数字，并暗示看过对方或其亲友的照片，以'挺漂亮的'作为暧昧的威胁。"],
    encoding_analysis=["'微信号后面那几位是不是7410'——微信号属于个人隐私，掌握部分号段暗示已获取对方社交账号信息。'头像是个女的吧，你女朋友？'——将威胁延伸至对方亲友，暗示已看过私人照片。'挺漂亮的'——性暗示威胁，对被提及的女性构成极大的不适感和安全隐患。这是开盒行为中最为恶劣的类型之一：将个人隐私曝光与性骚扰相结合。"],
    context_analysis=["无额外上下文。微信号+亲友照片+性暗示的组合信号足够判为高危。"],
    supporting_evidence=["(1)掌握对方微信号段；(2)将威胁延伸至亲友(女友)；(3)性暗示'挺漂亮的'构成性别骚扰。三重信号指向严重的复合型网络暴力。"],
    counter_evidence=["可能完全是瞎编的。但即使信息为假，以亲友照片和性暗示进行威胁的行为本身即构成严重的网络骚扰。"],
    final_rationale="微信号+亲友照片+性暗示威胁，开盒+性别骚扰的复合型严重违规，判为 high。",
)


# ================================================================
# SECTION 2: 社工库/查档 — 非法个人信息查询服务 (7 samples)
# Telegram/暗网/灰色社群的典型话术
# ================================================================

add(
    text="最新社工库更新了，三大运营商全量，飞机上找我，懂的来",
    risk_level="high",
    encoding_primary="E1_平台黑话",
    encoding_secondary=["C3_数字/代码", "E2_社会议题话语"],
    needs_context=False, hard_negative=False,
    literal_analysis=["文本宣布社工库数据已更新，涵盖三大运营商全部数据，引导用户到Telegram('飞机')上联系。"],
    encoding_analysis=["'社工库'=社会工程学数据库，包含通过数据泄漏、非法爬取等手段获取的海量个人隐私信息(姓名/手机/身份证/住址/开房记录等)。'三大运营商全量'暗示数据库覆盖面之广——中国移动/联通/电信所有用户。'飞机'=Telegram的中文黑话，因中国互联网审查较严，非法数据交易多转移至Telegram。'懂的来'=面向已有'经验'的用户，暗示交易有门槛。"],
    context_analysis=["无额外上下文。社工库广告本身就是违法信息——个人信息保护法明确禁止非法买卖个人信息。"],
    supporting_evidence=["(1)'社工库'=明确的非法个人信息聚合数据库；(2)'三大运营商全量'=海量个人信息覆盖；(3)引导至境外加密平台交易。三段信号均指向非法个人信息买卖。"],
    counter_evidence=["可能是虚假广告——以社工库为名诈骗。但无论数据真假，社工库广告的发布行为本身已是违法。"],
    final_rationale="社工库广告+运营商全量数据+境外平台交易，明确非法个人信息买卖，判为 high。",
)

add(
    text="查档dd，手机号查户籍查快递查开房，什么都能查，价格私聊",
    risk_level="high",
    encoding_primary="E1_平台黑话",
    encoding_secondary=["C3_数字/代码"],
    needs_context=False, hard_negative=False,
    literal_analysis=["文本以'查档'为代号宣传非法查询服务：包括户籍、快递记录、开房记录等隐私信息查询，引导私聊谈价。"],
    encoding_analysis=["'查档'=查询档案的黑话，指通过非法途径查询公民个人信息档案。'手机号查户籍查快递查开房'列举了三种典型的非法查询类型——户籍(最高敏感)、快递(实时行踪)、开房(隐私生活)。'什么都能查'宣扬非法查询能力无边界。'价格私聊'=明确的商业交易意图。这是黑产链条中的'查询中间商'——掌握社工库/内鬼渠道，向下游提供查询服务。"],
    context_analysis=["无额外上下文。列举式的非法服务广告在裸文本中已足够清晰。"],
    supporting_evidence=["(1)'查档'=明确的非法信息查询黑话；(2)列举三种非法查询类型(户籍/快递/开房)；(3)'价格私聊'=商业交易意图。典型的黑产服务广告。"],
    counter_evidence=["可能是恶搞或玩梗。但具体列举的查询类型+价格私聊的组合表明此条具有真实的交易引导意图。"],
    final_rationale="非法个人信息查询服务广告，明确交易意图，属于黑产链条中间环节，判为 high。",
)

add(
    text="有内鬼渠道，能调的不用说了吧，懂的都知道这个圈子里什么数据能拿",
    risk_level="high",
    encoding_primary="E1_平台黑话",
    encoding_secondary=["C1_人物代指", "E2_社会议题话语"],
    needs_context=False, hard_negative=False,
    literal_analysis=["文本暗示拥有内部人员渠道(内鬼)可调取数据，以隐晦话术指向某些高价值数据类型'不用说了吧'。"],
    encoding_analysis=["'内鬼渠道'——指在电信/银行/公安/快递等系统内有内部人员非法出售数据。这是黑产上游——比社工库更'新鲜'、更精准的实时数据。'能调的'指能调取的敏感数据类型(通话记录/短信/定位/银行流水等)。'不用说了吧'=面向圈内人的隐晦暗示。'这个圈子里什么数据能拿'=暗示这是成熟的黑产行业而非个别行为。"],
    context_analysis=["无额外上下文。内鬼渠道+圈内暗示在裸文本中即构成明显的非法信息交易。"],
    supporting_evidence=["(1)'内鬼渠道'=内部人员违法出售数据；(2)'能调的'暗示实时数据调取能力——比社工库更危险；(3)'圈子'暗示成熟的黑产产业链。三条信号指向有组织的数据黑产。"],
    counter_evidence=["可能吹牛。但声称拥有内鬼渠道进行实时数据调取的言论本身即对社会秩序构成威胁。"],
    final_rationale="内鬼数据渠道+实时调取能力+黑产产业链暗示，有组织的数据犯罪，判为 high。",
)

add(
    text="出个查信息的地址，全自动机器人查询，输入手机号秒出结果，自取不送",
    risk_level="high",
    encoding_primary="E1_平台黑话",
    encoding_secondary=["C3_数字/代码", "D2_隐喻"],
    needs_context=False, hard_negative=False,
    literal_analysis=["文本在分发一个所谓'全自动查询机器人'的访问地址，声称输入手机号即可秒出各种个人信息。"],
    encoding_analysis=["'查信息的地址'——Telegram bot或暗网站点的链接分发，这是黑产将查询服务产品化、自动化的表现。'全自动机器人查询'=将非法查询做成SaaS式的工具——降低使用门槛，扩大危害面。'输入手机号秒出结果'=查询效率极高，危害性远超人工查询。'自取不送'=不主动推广的伪装口吻。这种自动化查询工具的出现标志着个人信息黑产已高度产业化。"],
    context_analysis=["无额外上下文。分发非法查询工具地址在裸文本中即构成违法。"],
    supporting_evidence=["(1)分发非法查询工具/Bot地址；(2)自动化+秒出=降低违法犯罪门槛；(3)将个人信息查询工具化/商品化。产业化个人信息犯罪。"],
    counter_evidence=["可能是诈骗——收了钱不提供查询。但分发此类工具的广告行为本身已构成违法。"],
    final_rationale="自动化查询工具分发+个人信息黑产SaaS化，判为 high。",
)

add(
    text="最近手头紧，有需要查东西的兄弟私我，啥都能查你懂的，价格看你查啥",
    risk_level="high",
    encoding_primary="E1_平台黑话",
    encoding_secondary=["C3_数字/代码"],
    needs_context=False, hard_negative=False,
    literal_analysis=["文本以个人经济困难为借口，向'兄弟'群体兜售非法查询服务，价格视查询内容而定。"],
    encoding_analysis=["以'手头紧'的个人化理由降低警惕——将自己包装成临时缺钱才做这行的普通人而非专业黑产。'兄弟'称呼建立亲近感，降低潜在客户的心理防线。'啥都能查'强调查询能力无死角。'价格看你查啥'=已建立分级定价体系——不同敏感级别的数据价格不同。这是社交平台(QQ/微信/贴吧)上最常见的黑产兜售模式。"],
    context_analysis=["无额外上下文。以个人化借口包装的商业兜售在裸文本中即可识别。"],
    supporting_evidence=["(1)非法查询服务兜售；(2)'啥都能查'的无边界宣告；(3)分级定价=商业化运营。社交平台上典型的黑产兜售。"],
    counter_evidence=["可能真的只是缺钱乱说的。但兜售非法查询服务的行为本身即违法。"],
    final_rationale="以个人借口包装的非法查询兜售，面向社群的分级定价模式，判为 high。",
)

add(
    text="新库到了，包含最近六个月的新数据，之前查不到的现在可以再来试试",
    risk_level="high",
    encoding_primary="E1_平台黑话",
    encoding_secondary=["C3_数字/代码"],
    needs_context=False, hard_negative=False,
    literal_analysis=["文本宣布有新一批泄漏数据到库，时效性为最近六个月，鼓励之前未查到信息的客户重新尝试。"],
    encoding_analysis=["'新库'=新的数据泄漏源或购买数据到库。'最近六个月'强调数据新鲜度——这对于追踪目标是关键卖点。'之前查不到的现在可以再来试试'——暗示建立了持续更新的数据获取渠道，是长期运营的黑产数据库。这种'数据新鲜度'营销手法与合法SaaS产品如出一辙——黑产已高度商业化。"],
    context_analysis=["无额外上下文。新数据到库的营销话术在裸文本中即可识别。"],
    supporting_evidence=["(1)数据更新公告=长期运营的证明；(2)'最近六个月'强调数据新鲜度；(3)鼓励二次消费(之前查不到的再来)。持续运营的黑产数据库。"],
    counter_evidence=["可能数据是虚假的。但以虚假数据为由诱导交易仍属诈骗，且涉及个人信息的非法获取声称。"],
    final_rationale="数据更新营销+持续运营的黑产数据库+诱导消费，判为 high。",
)

add(
    text="不要再问能不能查了，直接发号码，查不到不收你钱好吧",
    risk_level="high",
    encoding_primary="E1_平台黑话",
    encoding_secondary=["C3_数字/代码", "D3_反讽"],
    needs_context=False, hard_negative=False,
    literal_analysis=["文本以不耐烦的口吻回应潜在客户，要求直接发送手机号码，以'查不到不收钱'来建立可信度。"],
    encoding_analysis=["'不要再问能不能查了'=暗示已经有很多人来问，说明有大量需求。'直接发号码'=降低客户犹豫——不需要先确认，直接给号码就行。'查不到不收你钱'=典型的'按结果付费'黑产交易模式——降低客户风险感知。这种不耐烦+自信的口吻是为了在灰色市场中建立'专业'形象。"],
    context_analysis=["无额外上下文。引导发送手机号码进行非法查询在裸文本中即违法。"],
    supporting_evidence=["(1)引导用户发送他人手机号进行查询；(2)'按结果付费'的商业承诺；(3)不耐烦口吻暗示客户众多=市场需求大。明确的黑产交易引导。"],
    counter_evidence=["可能是执法陷阱或恶搞。但引导发送手机号码进行非法查询的表述自身即违规。"],
    final_rationale="引导发送手机号+商业承诺+市场需求暗示，典型黑产交易话术，判为 high。",
)


# ================================================================
# SECTION 3: 人肉搜索号召 — 发动群众力量挖掘个人信息 (5 samples)
# 贴吧/微博常见：发帖号召'万能网友'帮忙人肉
# ================================================================

add(
    text="万能吧友，帮我查查这个人，骗了我三千块跑了，有他微信号和照片，求大佬出手",
    risk_level="high",
    encoding_primary="E1_平台黑话",
    encoding_secondary=["C1_人物代指", "D2_隐喻"],
    needs_context=False, hard_negative=False,
    literal_analysis=["文本请求网友帮助人肉搜索一个声称骗了自己钱的人，提供了微信号和照片作为搜索线索。"],
    encoding_analysis=["'万能吧友'=贴吧经典求助语式，将人肉搜索包装成正义维权。即使声称的'被骗三千块'属实，通过公开平台征集人肉搜索本身就是违法的——个人信息保护法规定即使出于维权目的，也不能通过非法手段获取他人信息。'求大佬出手'=寻找具有社工库/人肉技术的人。这种'正义维权'的包装是人肉搜索最常见的遮掩形式。"],
    context_analysis=["无额外上下文。即使有合理维权理由，公开发动人肉搜索的行为本身即违法——应通过法律途径而非网络暴力。"],
    supporting_evidence=["(1)公开发动人肉搜索；(2)提供搜索线索(微信号/照片)；(3)'求大佬出手'=寻找有技术能力者。典型的网络人肉搜索号召。"],
    counter_evidence=["可能有真实被骗经历。但维权应通过法律途径——网络人肉搜索是对他人隐私的侵犯，即使对方是'骗子'。"],
    final_rationale="以维权为包装的人肉搜索号召，提供照片/微信号等搜索线索，判为 high。",
)

add(
    text="这个女的谁认识？在XX商场偷了我朋友的包，监控拍到脸了，知道的私我，重谢",
    risk_level="high",
    encoding_primary="E1_平台黑话",
    encoding_secondary=["C1_人物代指", "C2_历史事件影射"],
    needs_context=False, hard_negative=False,
    literal_analysis=["文本附带(或声称有)监控截图，请求网友指认一名女性，以'偷包'为理由，以'重谢'为激励。"],
    encoding_analysis=["'这个女的谁认识'=直接的人肉请求。'监控拍到脸了'=已掌握人脸图像——这是最精准的人肉搜索素材，结合人脸识别技术或社会关系网络极易定位。'知道的私我'=规避公开平台监管——将信息交换转入私信。'重谢'=金钱激励，将人肉搜索商业化。即使有监控证据证明偷窃，应报警处理而非网络公审——这不仅是隐私侵犯，更可能导致无辜者被网暴(监控可能认错人)。"],
    context_analysis=["无额外上下文。人脸图像+金钱激励的人肉号召在裸文本中即构成严重违规。"],
    supporting_evidence=["(1)人肉搜索请求+人脸图像；(2)'知道的私我'=规避监管；(3)'重谢'的金钱激励。公开人肉悬赏——将他人隐私和安全置于公众审判之下。"],
    counter_evidence=["可能确实是偷窃受害者在寻求帮助。但'重谢'+人脸照片+私信联系的方式已构成人肉悬赏——应引导其报警而非网络曝光。"],
    final_rationale="人脸图像+金钱激励+私信规避，人肉搜索的悬赏模式，判为 high。",
)

add(
    text="转发扩散！看看谁认识这个男的，在地铁上偷拍女生裙底被发现了就跑，照片在这，求转发！",
    risk_level="high",
    encoding_primary="E1_平台黑话",
    encoding_secondary=["C1_人物代指", "D1_威胁"],
    needs_context=False, hard_negative=False,
    literal_analysis=["文本以'正义执行'为名义，号召转发扩散一名被指控偷拍男性的照片，附有照片并要求人肉识别。"],
    encoding_analysis=["'转发扩散'——利用社交网络病毒式传播进行人肉搜索。'照片在这'=公开发布被指控者的肖像。'求转发'=主动扩大传播范围。即使被指控行为属实(偷拍)，公开其肖像并发起人肉的'网络执法'行为本身就是对他人隐私和人身安全的侵犯——更何况指控可能不实，一旦误伤无法挽回。"],
    context_analysis=["无额外上下文。附带照片的转发人肉号召在裸文本中即构成对他人肖像权和隐私的侵犯。"],
    supporting_evidence=["(1)公开被指控者照片；(2)号召转发扩散=病毒式人肉；(3)以'正义'包装私刑。网络时代的'游街示众'——利用公众审判替代法律程序。"],
    counter_evidence=["制止偷拍是正当行为。但转发照片+号召人肉超出了正当举报的边界——应提交警方而非网络曝光。"],
    final_rationale="照片+转发扩散+网络公审，以正义为名的私刑式人肉，判为 high。",
)

add(
    text="我知道这样不太好但是有没有大哥能帮我查个人，前任的新对象，就想知道他是干嘛的，没别的意思",
    risk_level="medium",
    encoding_primary="E1_平台黑话",
    encoding_secondary=["C1_人物代指"],
    needs_context=False, hard_negative=False,
    literal_analysis=["文本先自我否定('这样不太好')再提出人肉请求——想通过网友查询前任新恋人的背景信息，附加'没别的意思'为自己开脱。"],
    encoding_analysis=["先承认'这样不太好'但还是要做——自我矛盾暴露了行为的不正当性。'前任的新对象'=出于情感纠葛的动机，非正当维权。'就想知道他是干嘛的'=看似无辜的好奇心包装。'没别的意思'=经典'此地无银'式辩解。虽然查询动机和手段不如职业黑产严重，但仍属于利用灰色渠道侵犯他人隐私。"],
    context_analysis=["无额外上下文。出于个人情感动机的隐私侵犯虽然危害程度低于商业黑产，但仍属违规行为。"],
    supporting_evidence=["(1)请求通过非正常渠道查询他人信息；(2)出于个人情感动机而非正当维权；(3)自我矛盾的表述暴露了自知违规。"],
    counter_evidence=["只是好奇，没有恶意。且未声称有付费意愿或具体查询能力。整体危害程度较低。"],
    final_rationale="个人情感驱动的人肉请求，自知不当但仍实施，但无商业化和技术化特征，判为 medium。",
)

add(
    text="家人们谁有那个曝光渣男的账号，就是那个专门发劈腿男信息的，我想投个稿",
    risk_level="medium",
    encoding_primary="E1_平台黑话",
    encoding_secondary=["C1_人物代指", "E2_社会议题话语"],
    needs_context=False, hard_negative=False,
    literal_analysis=["文本寻找专门曝光他人私人信息的账号，表示想投稿曝光某人。"],
    encoding_analysis=["'曝光渣男的账号'=以'情感维权'为包装的个人信息曝光账号——这些账号实质上是人肉搜索的'分发渠道'，收集并公开他人的私人信息(照片/姓名/工作单位/聊天记录等)。'想投个稿'=主动参与这种个人信息公开行为。虽然'曝光渣男/渣女'有大量受众，但此类账号和投稿行为已构成对他人隐私和名誉的系统性侵犯——且往往信息单方面、无法核实真伪。"],
    context_analysis=["无额外上下文。寻找曝光渠道+主动投稿的意图在裸文本中可判。"],
    supporting_evidence=["(1)寻找人肉信息分发渠道；(2)主动参与曝光他人隐私；(3)'曝光渣男'以情感争议包装隐私侵犯。"],
    counter_evidence=["曝光账号在社交媒体有一定正当性争议——部分人认为其在'保护'潜在受害者。但未经核实的单方面曝光仍然侵犯他人合法权益。"],
    final_rationale="寻找人肉分发渠道+主动参与曝光他人隐私，以情感维权包装，判为 medium。",
)


# ================================================================
# SECTION 4: 个人信息已泄露 — 披露/暗示已掌握的他人信息 (6 samples)
# 在某处公开贴出他人的真实信息片段
# ================================================================

add(
    text="大家注意避雷这个买家，地址是广东省深圳市南山区XX花园，姓陈，手机尾号8862，收到货就说坏了要退款",
    risk_level="high",
    encoding_primary="E1_平台黑话",
    encoding_secondary=["C1_地理位置暴露", "C3_数字/代码"],
    needs_context=False, hard_negative=False,
    literal_analysis=["文本以'避雷'为名公开了一名买家的姓名片段、大致住址和手机尾号，指控其恶意退款。"],
    encoding_analysis=["以'避雷/挂人'为名义公开他人身份信息是中文互联网最常见的个人信息泄露形式。'广东省深圳市南山区XX花园'=将住址精确到小区级别。'姓陈'+'手机尾号8862'=结合已足以在小区范围内定位到具体个人。即使指控属实，这种'用隐私曝光来维权'的方式已违反个人信息保护法——应通过平台纠纷解决机制而非泄露他人信息。"],
    context_analysis=["无额外上下文。地址+姓氏+手机尾号的组合信息在裸文本中已构成明确的个人信息泄露。"],
    supporting_evidence=["(1)公开他人精确住址(小区级别)；(2)公开姓氏+手机尾号——可交叉定位；(3)以'避雷'为包装。典型的'挂人'式个人信息泄露。"],
    counter_evidence=["商家维权确有必要。但应通过合法途径(平台仲裁/法律)而非公开他人个人信息。"],
    final_rationale="精确地址+姓氏+手机尾号的'挂人'式信息泄露，可定位到具体个人，判为 high。",
)

add(
    text="挂个人，QQ号146xxxx832，在群里发广告拉人头搞传销的，大家看到直接踢",
    risk_level="high",
    encoding_primary="E1_平台黑话",
    encoding_secondary=["C3_数字/代码", "C1_人物代指"],
    needs_context=False, hard_negative=False,
    literal_analysis=["文本公开某人的QQ号段并指控其从事传销活动，号召群管理将其移除。"],
    encoding_analysis=["公开他人QQ号+指控(传销)的'挂人'模式。即使指控可能属实，QQ号属于个人通信信息——在公开平台发布他人联系方式和违法指控构成双重侵害：通信隐私+名誉。且'搞传销'的指控未经司法认定，属于私刑式审判。在群聊/论坛中公开他人联系方式的'挂人'行为是中国互联网的灰色地带。"],
    context_analysis=["无额外上下文。QQ号+违法指控的公开'挂人'在裸文本中构成侵权。"],
    supporting_evidence=["(1)公开他人QQ号(通信隐私)；(2)未经司法认定的违法指控；(3)号召群体行动的'挂人'模式。"],
    counter_evidence=["群管理确实需要信息来识别和移除违规者。但应通过私信或内部举报渠道，而非公开发帖曝光。"],
    final_rationale="公开通信账号+违法指控的'挂人'，未经司法认定的私刑式审判，判为 high。",
)

add(
    text="这哥们住北京朝阳区双井那边，在一家互联网公司做运营，95年的，有人认识吗？",
    risk_level="high",
    encoding_primary="E1_平台黑话",
    encoding_secondary=["C1_地理位置暴露", "C1_人物代指"],
    needs_context=False, hard_negative=False,
    literal_analysis=["文本看似在'寻人'，实际是在公开某人的详细个人信息：住址区域、行业、年龄段。"],
    encoding_analysis=["'住北京朝阳区双井'=精确到商圈级别的住址。'在一家互联网公司做运营'=职业信息。'95年的'=年龄。三项信息组合=足以在'双井互联网运营95年'这个交集内定位到极少数人。'有人认识吗'=以'寻人'为伪装的信息公开——但寻人不需要公开如此精确的个人信息组合。"],
    context_analysis=["无额外上下文。精确地址+职业+年龄的组合已构成事实上的个人信息公开。"],
    supporting_evidence=["(1)精确到商圈的住址；(2)行业+岗位的职业信息；(3)年龄段。三项组合信息足以定位个人。"],
    counter_evidence=["可能是本人同意后的征友或寻人启事。但裸文本中没有任何征得同意的线索，按最坏意图假设。"],
    final_rationale="精确住址+职业+年龄的组合信息泄露，以'寻人'包装，判为 high。",
)

add(
    text="避雷一个外卖骑手，工号SH02187，姓刘，送餐时偷吃客户餐品还往里面吐口水，大家注意",
    risk_level="medium",
    encoding_primary="E1_平台黑话",
    encoding_secondary=["C3_数字/代码", "C1_人物代指"],
    needs_context=False, hard_negative=False,
    literal_analysis=["文本公开一名外卖骑手的工号和姓氏，指控其有偷吃餐品和吐口水等恶劣行为。"],
    encoding_analysis=["工号+姓氏=可定位到具体个人（外卖平台内部）。指控行为(偷吃+吐口水)有明确的公共安全风险——涉及食品安全，可能影响其他消费者。这类曝光比纯个人纠纷有更强的公共利益属性。但工号是内部信息——公开后该骑手可能遭遇网暴甚至线下报复。且指控未经核实。"],
    context_analysis=["无额外上下文。食品安全关切的曝光相比私人纠纷有较高的公共利益正当性，但个人信息公开仍需边界。"],
    supporting_evidence=["(1)公开工号(可定位到个人)；(2)涉及食品安全的指控有公共关切但未经核实；(3)可能导致网暴或线下报复。"],
    counter_evidence=["食品安全是重大公共利益——消费者有权知道。工号非一般意义的'隐私'信息，骑手在服务过程中本就应公开。整体在公共安全和隐私保护的边界上。"],
    final_rationale="涉及食品安全的曝光有一定公共利益基础，但工号+姓氏的组合仍可定位个人且有网暴风险，判为 medium。",
)

add(
    text="这个电话185xxxx1234的，天天打骚扰电话问要不要贷款，有没有人知道是哪家公司的，我想投诉",
    risk_level="medium",
    encoding_primary="E1_平台黑话",
    encoding_secondary=["C3_数字/代码"],
    needs_context=False, hard_negative=False,
    literal_analysis=["文本公开一个电话号码段，投诉该号码频繁骚扰，希望找到所属公司以便投诉。"],
    encoding_analysis=["公开骚扰电话号码——在中国互联网语境下较为常见，很多人认为'骚扰电话没有隐私权'。但手机号码是个人信息——即使对方在骚扰你，公开其号码也可能给号码持有者(可能号码被冒用或只是销售人员的办公号)带来网暴风险。这种'以暴制暴'的维权方式在互联网上极为普遍但法律上处于灰色地带。"],
    context_analysis=["无额外上下文。被骚扰后的求助有一定正当性——但公开号码仍属个人信息泄露。"],
    supporting_evidence=["(1)公开他人手机号码段；(2)以'投诉'为包装——目的正当但手段仍有侵权。"],
    counter_evidence=["反骚扰有正当性——在中国互联网语境下公开骚扰电话是常见的'互助'行为。号码本身可能为商用号而非私人号。整体危害较低。"],
    final_rationale="被骚扰后的反制性信息公开，有一定正当性但手段仍涉及隐私侵犯，判为 medium。",
)

add(
    text="出个名单，以下微信号都是卖假货的代理，大家自己小心：wxid_xxx001, wxid_xxx002, xiaoli8989, wanggege666",
    risk_level="medium",
    encoding_primary="E1_平台黑话",
    encoding_secondary=["C3_数字/代码"],
    needs_context=False, hard_negative=False,
    literal_analysis=["文本公开了多个微信号，指控其为假货代理，提醒他人警惕。"],
    encoding_analysis=["公开'假货代理'微信号的'避雷'名单——微信号属于个人信息但很多商业微信号本就是公开的。指控卖假货有消费者保护的正向社会功能。但批量发布他人联系方式的'名单'形式有组织化特征——可能被滥用为商业竞争对手的抹黑工具。介于正当消费者警示和组织化信息泄露之间。"],
    context_analysis=["无额外上下文。批量微信号公开+指控在裸文本中可判。"],
    supporting_evidence=["(1)批量公开微信号；(2)指控(假货代理)未经核实；(3)名单形式有组织化特征。"],
    counter_evidence=["商业微信通常是公开信息；消费者警示有一定正当性。整体危害程度低于私人信息泄露。"],
    final_rationale="批量公开商业微信号+消费者警示，介于正当信息共享和个人信息泄露边界，判为 medium。",
)


# ================================================================
# SECTION 5: 定位/行踪暴露 — 通过技术手段暴露他人实时位置 (5 samples)
# IP定位、基站定位、GPS追踪等
# ================================================================

add(
    text="你这会在XX网吧二楼吧，左边那个显示器是27寸的，别回头，我就在你后面",
    risk_level="high",
    encoding_primary="E1_平台黑话",
    encoding_secondary=["C1_地理位置暴露", "D1_威胁"],
    needs_context=False, hard_negative=False,
    literal_analysis=["文本对目标进行实时位置暴露——精确到某网吧二楼、显示器尺寸，最后以'别回头'制造恐怖氛围。"],
    encoding_analysis=["'XX网吧二楼'+'27寸显示器'=极度精确的空间定位，说明已通过某种手段(可能是IP定位+摄像头/内鬼/熟人)获取了目标的实时位置。'别回头，我就在你后面'=从线上威胁升级为线下跟踪——这是网络暴力向物理暴力过渡的危险信号。文本营造的恐怖氛围是网络跟踪(cyberstalking)的典型特征。"],
    context_analysis=["无额外上下文。实时精确位置+线下追踪威胁已超出网络言论范畴，构成人身安全威胁。"],
    supporting_evidence=["(1)实时精确位置暴露(网吧+楼层+设备)；(2)'我就在你后面'=线下跟踪/威胁；(3)营造恐怖氛围。从网络暴力向物理暴力过渡。"],
    counter_evidence=["可能在开玩笑——但即使是玩笑，发布他人实时精确位置+跟踪暗示已构成严重的网络跟踪行为。"],
    final_rationale="实时精确位置暴露+线下跟踪威胁，网络暴力向物理暴力的危险过渡，判为 high。",
)

add(
    text="你的IP我一查就知道了，都说了别在网上乱发东西，这下好了吧，你家是不是住在XX路附近？",
    risk_level="high",
    encoding_primary="E1_平台黑话",
    encoding_secondary=["C1_地理位置暴露", "D1_威胁", "D3_反讽"],
    needs_context=False, hard_negative=False,
    literal_analysis=["文本以长辈教训的口吻('都说了别在网上乱发东西')结合IP定位威胁，暗示已知道对方住址。"],
    encoding_analysis=["'IP我一查就知道了'=利用网络技术手段获取地理位置。'让你别在网上乱发东西'=将责任转嫁给受害者——'是你自己暴露的'。'你家是不是住在XX路附近'=从IP粗定位缩小到具体路段——暗示使用了更精确的定位手段(可能结合了对方发布的其他信息进行交叉比对)。这种'教训口吻'让威胁显得更'合理'但实质危险程度不变。"],
    context_analysis=["无额外上下文。IP定位+住址暗示的威胁语式在裸文本中可判。"],
    supporting_evidence=["(1)承认使用IP定位技术；(2)精确到路段级别的住址暗示；(3)转嫁责任的'教训'口吻。技术性网络跟踪。"],
    counter_evidence=["XX路可能只是IP粗定位的城市区域——不一定真实知道具体住址。但威胁使用IP定位+住址暗示的行为本身即构成跟踪恐吓。"],
    final_rationale="IP定位+住址暗示+受害者归责，技术性网络跟踪威胁，判为 high。",
)

add(
    text="有能查实时定位的吗？不需要太精确，哪个城市就行，我要确认一个人是不是骗我说出差",
    risk_level="medium",
    encoding_primary="E1_平台黑话",
    encoding_secondary=["C1_地理位置暴露", "D2_隐喻"],
    needs_context=False, hard_negative=False,
    literal_analysis=["文本以个人情感/信任顾虑为由，寻求能获取他人实时定位的服务，声称'不需要太精确'。"],
    encoding_analysis=["寻求实时定位服务——无论出于什么理由，未经他人同意追踪其位置是严重侵犯隐私的行为。'确认是不是骗我说出差'=情感关系中的控制欲驱动——这类需求在人肉/定位服务中非常常见。'不需要太精确'=试图降低自己的道德负罪感，但城市级别的定位已经是隐私侵犯。相比商业黑产，个人动机的定位请求危害面较小但性质相同。"],
    context_analysis=["无额外上下文。出于个人情感动机寻求定位服务在裸文本中可判。"],
    supporting_evidence=["(1)寻求实时定位服务；(2)未经他人同意的追踪意图；(3)个人情感动机驱动。"],
    counter_evidence=["仅要求城市级别——定位精度低，危害有限。个人关系中确实存在信任问题，但应通过沟通而非定位追踪解决。整体介于隐私侵犯和个人关系纠纷之间。"],
    final_rationale="个人动机的定位服务寻求，精度要求低但性质仍为隐私侵犯，判为 medium。",
)

add(
    text="这个博主的定位我找到了，就在杭州滨江区那个商场里上班，每天下午两点左右发微博，估计是趁老板不在摸鱼",
    risk_level="medium",
    encoding_primary="E1_平台黑话",
    encoding_secondary=["C1_地理位置暴露", "C1_人物代指"],
    needs_context=False, hard_negative=False,
    literal_analysis=["文本声称通过某博主发博规律推断出其工作地点和发博时间规律，但更多是炫耀'追踪'能力。"],
    encoding_analysis=["'定位我找到了'=对匿名博主进行去匿名化是部分网民的不良爱好——通过照片背景/发博时间/内容细节拼图定位。'在杭州滨江区那个商场里上班'=从公开信息拼图出的位置推测。此类'粉丝追踪'在饭圈/互联网八卦中常见——虽然信息多来自博主自身公开内容，但整理和公开他人位置信息仍有安全隐患。"],
    context_analysis=["无额外上下文。对博主的去匿名化追踪在裸文本中可判。"],
    supporting_evidence=["(1)主动追踪并公开博主位置信息；(2)'找到了'的炫耀口吻；(3)对他人行踪规律的公开分析。"],
    counter_evidence=["信息可能全部来自博主自愿公开的内容——位置是推测而非查询所得。博主是公众人物/内容创作者，对隐私的预期与普通人不同。整体危害较低。"],
    final_rationale="通过公开信息拼图追踪博主位置，手段较温和但仍有安全隐患，判为 medium。",
)

add(
    text="有人能帮我定位一个手机号吗，怀疑我老公出轨，只要告诉我他晚上在哪就行，价格好说",
    risk_level="medium",
    encoding_primary="E1_平台黑话",
    encoding_secondary=["C1_地理位置暴露", "C3_数字/代码"],
    needs_context=False, hard_negative=False,
    literal_analysis=["文本以婚姻中的不信任为由，寻求手机号定位服务，有限定的查询时间和金钱交易意愿。"],
    encoding_analysis=["'定位一个手机号'=寻求非法定位服务——基站定位/GPS追踪等均需特殊渠道。'怀疑老公出轨'=情感动机驱动。'只要告诉我晚上在哪'=限定范围试图降低非法感。'价格好说'=明确的金钱交易意愿。虽然动机'情有可原'，但通过黑产手段监视配偶位置是明确的违法行为——隐私保护不因婚姻关系而失效。"],
    context_analysis=["无额外上下文。寻求手机定位服务+金钱交易意愿在裸文本中可判。"],
    supporting_evidence=["(1)寻求非法手机定位服务；(2)金钱交易意愿；(3)对他人的位置监控意图。"],
    counter_evidence=["情感关系中的不信任是一个普遍但非政治化的问题。定位配偶在道德上有争议但部分人认为'情有可原'。危害局限于个人关系而非公共安全。"],
    final_rationale="情感动机的定位服务寻求+金钱交易，隐私侵犯但局限于个人关系，判为 medium。",
)


# ================================================================
# SECTION 6: 数据交易/买卖 — 个人信息作为商品流通 (5 samples)
# Telegram/暗网交易群的典型话术
# ================================================================

add(
    text="出一手快递数据，日更，带姓名电话地址，量大的来，散户别问",
    risk_level="high",
    encoding_primary="E1_平台黑话",
    encoding_secondary=["C3_数字/代码", "D2_隐喻"],
    needs_context=False, hard_negative=False,
    literal_analysis=["文本在出售快递数据——包含收件人姓名、电话、地址，每日更新，只面向批量采购的客户。"],
    encoding_analysis=["'一手快递数据'=直接来自快递公司内部泄漏或系统漏洞的原始数据——比社工库的二手数据更新、更准确。'日更'=每日更新，说明数据源是持续的、实时的——这是大宗数据交易而非零散查询。'带姓名电话地址'=明确数据字段——姓名+电话+地址的三件套是最高价值的数据组合。'散户别问'=面向下游黑产的B2B模式。这是个人信息黑产的上游——大规模、持续化的数据批发。"],
    context_analysis=["无额外上下文。快递数据批发出售在裸文本中即构成重大违法。"],
    supporting_evidence=["(1)快递数据批发出售(姓名+电话+地址三件套)；(2)'日更'=持续性数据泄漏；(3)B2B模式面向下游黑产。大规模个人信息非法交易。"],
    counter_evidence=["可能是骗局——不存在真实数据。但以快递数据为名的交易引导行为本身即构成违法。"],
    final_rationale="大规模快递数据批发出售+持续日更+三件套信息，黑产上游供应链，判为 high。",
)

add(
    text="收各种平台用户数据，只要带手机号的就行，注册数据也收，有的带价来",
    risk_level="high",
    encoding_primary="E1_平台黑话",
    encoding_secondary=["C3_数字/代码"],
    needs_context=False, hard_negative=False,
    literal_analysis=["文本在收购各类平台的用户数据，最低要求是包含手机号，也接受注册数据，要求卖家报价。"],
    encoding_analysis=["'收各种平台用户数据'=数据黑市的买方——有买方才有卖方，收购需求驱动着个人信息黑产。'带手机号就行'=手机号是关联其他信息(实名/社交/金融)的关键标识。'注册数据也收'=降低门槛——连注册信息(可能仅含手机号+用户名)都要，说明需求量大。'带价来'=建立了成熟的交易机制。数据买方是黑产链条的核心驱动力之一。"],
    context_analysis=["无额外上下文。收购用户数据的要约在裸文本中即构成违法。"],
    supporting_evidence=["(1)收购各类平台用户数据；(2)手机号为最低门槛——说明以手机号关联更多信息为目的；(3)成熟交易机制(带价来)。数据黑市的需求方。"],
    counter_evidence=["可能是合规的数据采购用于市场调研。但'只要带手机号'+'注册数据也收'的低门槛暗示非合规用途——合规数据采购不会这样表述。"],
    final_rationale="收购个人数据+手机号关联+成熟交易机制，黑产需求方，判为 high。",
)

add(
    text="有银行流水的渠道吗？能拉半年的那种，不要问用来干嘛，能做的聊",
    risk_level="high",
    encoding_primary="E1_平台黑话",
    encoding_secondary=["C3_数字/代码", "D2_隐喻"],
    needs_context=False, hard_negative=False,
    literal_analysis=["文本在寻找能提供银行流水查询的渠道——要求半年记录，对用途保密。"],
    encoding_analysis=["'银行流水'=金融隐私的最高敏感级别——包含所有收入和支出记录，可还原一个人的全部经济活动轨迹。'能拉半年的'=查询能力极强——说明渠道在银行系统内部或具有高级权限。'不要问用来干嘛'=拒绝说明用途——暗示用途非法(催收/诈骗/敲诈/商业间谍)。银行流水泄露是个人信息安全最严重的事故之一。"],
    context_analysis=["无额外上下文。银行流水查询渠道的寻求在裸文本中即构成最严重的隐私安全威胁。"],
    supporting_evidence=["(1)寻求银行流水查询渠道——最高敏感金融隐私；(2)半年的长周期查询能力；(3)'不要问干嘛'=用途非法化。金融隐私+内鬼渠道+用途隐匿。"],
    counter_evidence=["可能用于合法尽调或司法调查。但'不要问用来干嘛'的表述与合法用途完全不符——合法渠道不需要隐匿用途。"],
    final_rationale="银行流水查询渠道+金融隐私+用途隐匿，最高级别的个人信息安全威胁，判为 high。",
)

add(
    text="出征信报告，一手渠道不是那种社工库爬的老数据，需要的滴滴",
    risk_level="high",
    encoding_primary="E1_平台黑话",
    encoding_secondary=["C3_数字/代码"],
    needs_context=False, hard_negative=False,
    literal_analysis=["文本在出售个人征信报告查询服务，强调是实时查询的新数据而非社工库的陈旧数据。"],
    encoding_analysis=["'征信报告'=中国人民银行征信中心的个人信用记录——包含身份信息/住址/工作单位/信贷记录/担保记录/查询记录等极其敏感的全部金融信息。'一手渠道不是社工库爬的'=暗示拥有征信系统的实时查询权限(可能是内部人员/系统漏洞/API滥用)——比社工库数据更权威、更全面。'需要的滴滴'=私信联系。征信报告是法定最高级别的个人敏感信息。"],
    context_analysis=["无额外上下文。征信报告查询服务的出售在裸文本中即构成最严重的违法。"],
    supporting_evidence=["(1)出售征信报告查询——最高级别个人敏感信息；(2)'一手渠道'暗示可实时查询征信系统；(3)比社工库更精确的数据质量承诺。非法获取国家征信系统数据。"],
    counter_evidence=["不存在合法出售征信报告查询服务的情形——此条在任何语境下均为违法。"],
    final_rationale="征信报告+实时查询+一手渠道，非法获取国家征信系统数据，判为 high。",
)

add(
    text="出个爬虫脚本，能爬XX平台的所有公开帖子和发帖人信息，批量导出，需要的私",
    risk_level="high",
    encoding_primary="E1_平台黑话",
    encoding_secondary=["C3_数字/代码", "D2_隐喻"],
    needs_context=False, hard_negative=False,
    literal_analysis=["文本在出售一个爬虫工具，声称能批量抓取某平台的所有公开帖子和发帖人信息并导出。"],
    encoding_analysis=["'爬虫脚本'+'发帖人信息'=利用自动化工具批量获取用户信息——即使发帖人信息是公开的，批量抓取和导出就构成了对个人信息的大规模收集，违反个人信息保护法的'目的限制'和'最小必要'原则。'批量导出'=将数据结构化存储，方便二次利用(诈骗/推广/人肉)。工具化、自动化的个人信息收集比手工查询危害大得多。"],
    context_analysis=["无额外上下文。批量抓取工具+导出功能的出售在裸文本中可判。"],
    supporting_evidence=["(1)出售批量个人信息抓取工具；(2)降低信息收集门槛(自动化)；(3)'批量导出'=便于二次犯罪。工具化个人信息犯罪。"],
    counter_evidence=["爬虫本身是技术工具——有合法用途(学术研究/舆情分析)。但加上'发帖人信息'和出售意图，用于非法目的的概率极高。"],
    final_rationale="批量个人信息抓取工具出售+降低犯罪门槛，工具化个人信息侵害，判为 high。",
)


# ================================================================
# SECTION 7: 安全意识样本 — low/none (4 samples)
# 帮助模型区分真正的开盒威胁和正常的隐私安全意识
# ================================================================

add(
    text="大家在社交媒体上不要随便发自己的车票机票，上面的二维码和条形码都能扫出个人信息来",
    risk_level="none",
    encoding_primary="none",
    encoding_secondary=[],
    needs_context=False, hard_negative=True,
    literal_analysis=["文本是善意的网络安全提醒——告诫网友不要在社交媒体发布含二维码/条形码的票据照片，以免个人信息被扫出。"],
    encoding_analysis=["此条为正常的网络安全意识提醒。'车票机票''二维码条形码''个人信息'都是安全科普中的正常词汇。不存在违反信息保护的行为——相反是在帮助他人保护信息。hard_negative=True：帮助模型区分'谈论信息安全'和'实施信息侵犯'。"],
    context_analysis=["无额外上下文。善意提醒+安全教育，纯正向内容。"],
    supporting_evidence=["(1)完全善意的安全教育内容；(2)无任何威胁、交易、曝光行为。"],
    counter_evidence=["无。纯安全内容。"],
    final_rationale="善意的网络安全提醒，帮助他人保护隐私，pure safe。hard_negative=True。",
)

add(
    text="建议大家定期检查自己的账号有没有被异地登录，上次我发现我号在深圳被人登了赶紧改密码",
    risk_level="none",
    encoding_primary="none",
    encoding_secondary=[],
    needs_context=False, hard_negative=True,
    literal_analysis=["文本分享个人账号安全经验——发现异地登录后及时改密码，并建议他人定期检查。"],
    encoding_analysis=["此条为个人安全经验分享。'异地登录''改密码'是正常的安全操作。无任何违规——在分享保护自己的经验而非侵犯他人。hard_negative=True：帮助模型学会区分'账号安全讨论'和'账号信息泄露'。"],
    context_analysis=["无额外上下文。个人安全经验分享，纯正向。"],
    supporting_evidence=["(1)分享个人安全经验；(2)完全正向，无任何侵犯。"],
    counter_evidence=["无。"],
    final_rationale="个人账号安全经验分享，纯正向。hard_negative=True。",
)

add(
    text="问一下，如果有人在网上乱发我的照片和个人信息，我应该怎么维权？报警有用吗？",
    risk_level="none",
    encoding_primary="none",
    encoding_secondary=[],
    needs_context=False, hard_negative=True,
    literal_analysis=["文本是受害者在求助如何维权——询问照片和个人信息被他人泄露后的法律救济途径。"],
    encoding_analysis=["此条为信息泄露受害者的维权求助。虽然包含'照片''个人信息'等关键词，但语境完全相反——是在寻求保护自己而非侵犯他人。'报警有用吗'是受害者的正常困惑。hard_negative=True：帮助模型区分'受害者求助'和'施害者行为'。"],
    context_analysis=["无额外上下文。受害者维权求助，纯正向。"],
    supporting_evidence=["(1)受害者身份——信息被他人泄露；(2)寻求合法维权途径；(3)无任何侵犯他人的意图。"],
    counter_evidence=["无。受害者求助，应予以支持。"],
    final_rationale="个人信息泄露受害者维权求助，纯正向。hard_negative=True。",
)

add(
    text="现在诈骗电话太猖獗了，知道你的身份证、家庭住址、工作单位，说的跟真的一样，大家一定要小心",
    risk_level="none",
    encoding_primary="none",
    encoding_secondary=[],
    needs_context=False, hard_negative=True,
    literal_analysis=["文本是对诈骗电话的警示——提醒他人即使对方掌握了详细的个人信息也可能是骗子。"],
    encoding_analysis=["此条为反诈骗安全警示。列举诈骗电话可能掌握的信息类型(身份证/住址/工作单位)是为了说明骗子的手段——旨在帮助他人识别骗局而非传播这些信息。hard_negative=True：帮助模型区分'反诈警示'和'信息泄露'。"],
    context_analysis=["无额外上下文。反诈警示，纯正向。"],
    supporting_evidence=["(1)反诈安全警示；(2)列举信息类型是为了说明诈骗手段；(3)纯善意。"],
    counter_evidence=["无。"],
    final_rationale="反诈骗安全警示，纯正向。hard_negative=True。",
)


# ================================================================
# Write output
# ================================================================
print(f"\nGenerated {len(samples)} samples")

# Risk distribution
risks = Counter(s["risk_level"] for s in samples)
print(f"Risk distribution: {dict(risks)}")

# Encoding distribution
encodings = Counter(s["encoding_primary"] for s in samples)
print(f"Encoding distribution: {dict(encodings)}")

with open(OUTPUT, "w", encoding="utf-8") as f:
    for s in samples:
        f.write(json.dumps(s, ensure_ascii=False, separators=(",", ":")) + "\n")

print(f"Wrote to {OUTPUT}")
