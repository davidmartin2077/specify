#!/usr/bin/env python3
"""
Fix unrealistic comment patterns in the dataset.
Focus: meta-censorship talk, excessive "懂的都懂" filler, essay-length comments,
unnatural self-censorship descriptions.

真实中文互联网评论特点：
- 短、直接、不解释自己在规避什么
- 不会说"号没了""不敢说""被删了"这种元评论
- 黑产/违规广告中使用"懂的私/懂的来"是真实的
- 政治隐晦中不会直白写"你懂的"作为填充，而是真正用编码表达
"""

import json, copy
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
COMBINED = PROJECT_ROOT / "data" / "processed" / "combined_candidates.jsonl"

# ── Load current data ──────────────────────────────────────────────────
with open(COMBINED) as f:
    samples = [json.loads(l) for l in f]

sample_map = {d['id']: d for d in samples}

# ── Fixes: {id: {field: new_value, ...}} ───────────────────────────────
# Only write the fields that need changing. If 'reasoning' is given, it replaces entirely.
# If only 'text' changes, reasoning is auto-updated (string replacement in reasoning).

FIXES = {}

# ═══════════════════════════════════════════════════════════════
# 类型1: "号没了/封号/不敢说" → 改为正常表达
# ═══════════════════════════════════════════════════════════════

FIXES["000900"] = {
    "text": "劳动法就是个笑话，996屁事没有，讨个薪倒被行政拘留了。这就是法治社会的含金量",
    "risk_level": "high",
    "encoding_primary": "D1_反讽",
    "encoding_secondary": ["D2_隐喻"],
    "hard_negative": False,
    "review_notes": "source=batch8_tieba_style; fixed_unrealistic_pattern=号没了→反讽",
    "reasoning": {
        "literal_analysis": ["文本以'996屁事没有'和'讨薪被拘'的对比反讽'法治社会'。"],
        "encoding_analysis": ["D1_反讽：'法治社会的含金量'是典型的反语——声称法治实则在揭露执行不公。'996'使用平台黑话代指过度加班。"],
        "context_analysis": ["劳工权益与法律保护的不对等是中文互联网上的常见讨论框架。"],
        "supporting_evidence": ["996违法但普遍存在的现实矛盾", "讨薪被拘的真实社会案例", "反讽结构明确"],
        "counter_evidence": ["未提及具体事件或地区，一般性抱怨", "反讽表达在法律上不一定构成违法"],
        "final_rationale": "以反讽方式批评劳动法执行不公，判为 high。"
    }
}

FIXES["000960"] = {
    "text": "唐山那事到现在都没后续了吧，热搜上了三天就没了，该干嘛干嘛。互联网没有记忆这句话是真的",
    "risk_level": "medium",
    "encoding_primary": "D2_隐喻",
    "encoding_secondary": ["C5_概念替换"],
    "hard_negative": False,
    "review_notes": "source=batch9_national_security; fixed_unrealistic_pattern=不敢说→具体事件指代",
    "reasoning": {
        "literal_analysis": ["提及唐山事件——以'热搜上了三天就没了'描述公众注意力的短暂性，'互联网没有记忆'表达对舆论消褪的无奈。"],
        "encoding_analysis": ["D2_隐喻：'热搜上了三天就没了'暗示系统性的话题管控——'没了'可以被解读为被压制或自然消退。C5_概念替换：'唐山那事'作为具体事件的模糊化代称——既让知情者理解又避免过于直接。"],
        "context_analysis": ["对重大社会事件的舆论处理的批评性观察。"],
        "supporting_evidence": ["提及了具体事件框架", "公众注意力短暂性是真实的观察", "表达了失望情绪"],
        "counter_evidence": ["热搜自然消退也是正常的互联网规律", "没有明确指控人为干预"],
        "final_rationale": "以热点事件为例表达对舆论管理的批评，用隐喻而非直接指控，判为 medium。"
    }
}

FIXES["000577"] = {
    "text": "监控装了那么多，唐山打人的时候监控刚好就坏了是吧。人脸识别抓嫖抓赌一抓一个准，抓黑社会就抓不着了",
    "risk_level": "high",
    "encoding_primary": "D1_反讽",
    "encoding_secondary": ["D2_隐喻"],
    "hard_negative": False,
    "review_notes": "source=batch2_natural; fixed_unrealistic_pattern=感谢审核员→具体反讽",
    "reasoning": {
        "literal_analysis": ["以唐山事件为切入点，对比监控系统在执法中的选择性——抓嫖抓赌有效但抓黑社会失效。"],
        "encoding_analysis": ["D1_反讽：'刚好就坏了'是典型的反语，暗示监控是选择性'坏'的。'一抓一个准'和'抓不着了'的对比构建了对执法选择性的讽刺。"],
        "context_analysis": ["对执法不公和监控滥用的批评。"],
        "supporting_evidence": ["提及了真实的社会事件背景", "对比结构清晰揭示了双重标准", "监控系统存在的问题是公众关注的话题"],
        "counter_evidence": ["表达方式仍然较为间接", "没有明确指控具体人员或机构"],
        "final_rationale": "以反讽对比批评执法选择性，指向明确，判为 high。"
    }
}

FIXES["000598"] = {
    "text": "看了新闻以后去翻评论，翻了五分钟全是机器人刷的'支持''点赞'，一条真人评论都找不到。花钱买水军能不能走点心",
    "risk_level": "medium",
    "encoding_primary": "D1_反讽",
    "encoding_secondary": [],
    "hard_negative": False,
    "review_notes": "source=batch2_natural; fixed_unrealistic_pattern=评论区被删→水军刷评",
    "reasoning": {
        "literal_analysis": ["描述在新闻评论区只看到机器人刷屏的水军评论，没有真实用户的反馈。"],
        "encoding_analysis": ["D1_反讽：'花钱买水军能不能走点心'——表面吐槽水军质量，深层批评舆论操控。'全是机器人'暗示评论经过了筛选或操控。"],
        "context_analysis": ["对网络舆论操控的观察和讽刺。"],
        "supporting_evidence": ["水军刷评是公认的网络现象", "'一条真人评论找不到'表达了真实感受"],
        "counter_evidence": ["没有明确指出是官方操控还是商业水军", "只是一般性的观察"],
        "final_rationale": "以吐槽水军的方式暗示舆论控制，判为 medium。"
    }
}

FIXES["000542"] = {
    "text": "这个up主的视频播放量一直上不去，明明内容挺好的。上次那期讲那个事的，质量是真的高",
    "risk_level": "medium",
    "encoding_primary": "E1_平台黑话",
    "encoding_secondary": ["D2_隐喻"],
    "hard_negative": False,
    "review_notes": "source=batch1_natural; fixed_unrealistic_pattern=限流→播放量自然描述",
    "reasoning": {
        "literal_analysis": ["说up主视频播放量低、质量高——尤其是'上次那期讲那个事的'。"],
        "encoding_analysis": ["E1_平台黑话+'那个事'——用模糊化指代暗示up主因涉及敏感话题而播放量受限。不直说'限流'而是通过播放量和内容质量的矛盾来暗示。"],
        "context_analysis": ["对B站up主因内容敏感而播放量受限的隐晦讨论。"],
        "supporting_evidence": ["播放量与内容质量的矛盾暗示了限制", "'那个事'的模糊化指代"],
        "counter_evidence": ["播放量低也可能是正常的内容竞争结果"],
        "final_rationale": "通过质量-播放量的矛盾暗示内容受限，不如直接说'限流'那样直白，判为 medium。"
    }
}

FIXES["001423"] = {
    "text": "四人帮打倒了，但四人帮的精神遗产还在。看今天的官场就知道了，该有的毛病一个没少",
    "risk_level": "high",
    "encoding_primary": "C1_历史人物类比",
    "encoding_secondary": ["D1_反讽"],
    "hard_negative": False,
    "review_notes": "source=batch15_p1_gaps; gap=文革; fixed_unrealistic_pattern=说多了号没了→删除meta",
    "reasoning": {
        "literal_analysis": ["声称四人帮的精神遗产延续至今，将当代官场问题归结为历史延续。"],
        "encoding_analysis": ["C1_历史人物类比：将四人帮的政治特征投射到当代官场——暗示腐败和专断源于体制性延续。D1_反讽：'该有的毛病一个没少'是讽刺性陈述。"],
        "context_analysis": ["以历史类比进行体制批评。"],
        "supporting_evidence": ["将当代官场与历史负面人物关联", "批评指向体制性延续"],
        "counter_evidence": ["未提及具体人事", "对'精神遗产'的判断是主观的"],
        "final_rationale": "利用历史人物类比攻击现行体制，判为 high。"
    }
}

# ═══════════════════════════════════════════════════════════════
# 类型2: 过长的"小作文" → 缩短，改为真实评论口吻
# ═══════════════════════════════════════════════════════════════

FIXES["000681"] = {
    "text": "鲁迅一百年前就在书里写'从来如此便对吗'，一百年过去了，热搜上的问题还是那些问题",
    "risk_level": "medium",
    "encoding_primary": "C1_历史人物类比",
    "encoding_secondary": ["D2_隐喻"],
    "hard_negative": False,
    "review_notes": "source=batch4_natural; fixed_unrealistic_pattern=过长短文→缩短+删除meta",
    "reasoning": {
        "literal_analysis": ["引用鲁迅的'从来如此便对吗'，表示一百年后社会问题依旧。"],
        "encoding_analysis": ["C1_历史人物类比：借用鲁迅的批判性话语来影射当代社会问题——'热搜上的问题还是那些问题'暗示问题未解决。D2_隐喻：不具体说明是什么问题，让读者自行填充。"],
        "context_analysis": ["借文学/历史人物进行社会批评。"],
        "supporting_evidence": ["鲁迅作为批判性符号的使用", "'一百年过去'的时间跨度暗示系统性"],
        "counter_evidence": ["批评对象模糊", "引经据典本身不构成风险"],
        "final_rationale": "以文学引用为包装的社会批评，判为 medium。"
    }
}

FIXES["001273"] = {
    "text": "每次看到那种新闻，评论区就有人刷NMSL。说实话分不清是在骂那个事还是在骂别的",
    "risk_level": "high",
    "encoding_primary": "A2_拼音/首字母缩写",
    "encoding_secondary": ["E3_互动/热点触发"],
    "hard_negative": False,
    "review_notes": "batch=replace_phase3_v2_r9; fixed_unrealistic_pattern=过长学术分析→简洁评论口吻",
    "reasoning": {
        "literal_analysis": ["描述在负面新闻下出现NMSL评论的现象，表达对这种模糊表达的分辨困难。"],
        "encoding_analysis": ["A2_拼音缩写：NMSL（你妈死了）是中文互联网上的通用辱骂缩略语。E3_互动触发：在特定新闻下使用，可能从辱骂升级为政治表达。"],
        "context_analysis": ["对评论区中缩写辱骂与政治表达混合现象的观察。"],
        "supporting_evidence": ["NMSL是高频率的网络辱骂缩写", "在新闻评论中的使用可能有政治影射"],
        "counter_evidence": ["NMSL本身只是辱骂词而非政治表达", "用户只是描述现象而非使用该词"],
        "final_rationale": "对网络辱骂与政治表达混合现象的观察描述，判为 high。"
    }
}

FIXES["001276"] = {
    "text": "看到贪官新闻CNMB，被扣工资CNMB，小区封了CNMB。CNMB是万能公式",
    "risk_level": "high",
    "encoding_primary": "A2_拼音/首字母缩写",
    "encoding_secondary": [],
    "hard_negative": False,
    "review_notes": "batch=replace_phase3_v2_r9; fixed_unrealistic_pattern=过长分析→短评",
    "reasoning": {
        "literal_analysis": ["描述CNMB作为'万能公式'在各种负面场景中的使用——贪官、扣工资、封小区。"],
        "encoding_analysis": ["A2_拼音缩写：CNMB（操你妈逼）是中文互联网上最常见的辱骂缩写之一。文本展示了该词在不同政治/社会语境中的使用——从明确的政治事件（贪官）到日常生活（扣工资）再到社会事件（封小区）。"],
        "context_analysis": ["通过展示一个辱骂词的多场景使用来暗示社会问题。"],
        "supporting_evidence": ["提及了多个敏感话题（贪官、封控）", "以辱骂词为纽带连接不同社会事件"],
        "counter_evidence": ["CNMB本身只是辱骂而非政治表达", "只展示了使用场景而没有明确的政治主张"],
        "final_rationale": "以辱骂词的跨场景使用暗示社会不满的普遍性，判为 high。"
    }
}

FIXES["001274"] = {
    "text": "1115，懂的都沉默。第十年了",
    "risk_level": "high",
    "encoding_primary": "C3_数字代指",
    "encoding_secondary": ["E2_时间节点触发"],
    "hard_negative": False,
    "review_notes": "batch=replace_phase3_v2_r9; fixed_unrealistic_pattern=过长→短弹幕风",
    "reasoning": {
        "literal_analysis": ["'1115'是一个日期/事件代指，'懂的都沉默'暗示该事件引发的不便讨论，'第十年'标记了时间跨度。"],
        "encoding_analysis": ["C3_数字代指：1115是一个日期编码——指向特定历史事件。E2_时间节点触发：'第十年'的周年标记激活了与该事件相关的记忆。"],
        "context_analysis": ["以数字代指和周年标记隐晦地指向敏感历史事件。"],
        "supporting_evidence": ["1115+沉默的组合暗示了该日期的敏感性", "十周年增加了事件的重量感"],
        "counter_evidence": ["数字本身没有明确含义", "对不知情者而言无害"],
        "final_rationale": "以数字编码和周年标记隐晦指向敏感历史事件，判为 high。"
    }
}

FIXES["001160"] = {
    "text": "蛤这个字，一个顶一万个。懂的都懂",
    "risk_level": "medium",
    "encoding_primary": "C4_典故/物品/符号借用",
    "encoding_secondary": ["A1_普通谐音"],
    "hard_negative": False,
    "review_notes": "batch=replace_phase3_v2_r3; fixed_unrealistic_pattern=过长学术→短弹幕",
    "reasoning": {
        "literal_analysis": ["'蛤'是一个被赋予了特殊含义的汉字——在特定互联网社区中作为政治人物代称。"],
        "encoding_analysis": ["C4_符号借用+'蛤'Homophone：利用'蛤'与特定政治人物姓氏的谐音关系，在互联网社区中已成为高度固化的代称。'一个顶一万个'暗示这一字的承载量远超普通字。"],
        "context_analysis": ["以单字进行政治人物的编码代指。"],
        "supporting_evidence": ["'蛤'的谐音映射已高度固化", "社区共识使这一编码高效传播"],
        "counter_evidence": ["'蛤'也可能只是青蛙的拟声词或表情包的普通用法"],
        "final_rationale": "以高度固化的单字符号进行政治人物编码代指，判为 medium。"
    }
}

FIXES["001158"] = {
    "text": "菜单上今天有这道菜，明天你来问就没有了。服务员说菜单一直在更新，你信吗",
    "risk_level": "medium",
    "encoding_primary": "D2_隐喻",
    "encoding_secondary": [],
    "hard_negative": False,
    "review_notes": "batch=replace_phase3_v2_r3; fixed_unrealistic_pattern=过长隐喻→简洁隐喻",
    "reasoning": {
        "literal_analysis": ["用餐厅菜单的更新来隐喻信息的出现和消失。"],
        "encoding_analysis": ["D2_隐喻：'菜单'→公开信息/热搜/topic，'今天有明天没有'→信息的快速消失，'服务员说菜单在更新'→官方的解释。这个简化的隐喻比原始版本更克制。"],
        "context_analysis": ["对信息管控的隐喻式批评。"],
        "supporting_evidence": ["菜单隐喻连贯可读", "暗示了信息消失和官方解释的不一致"],
        "counter_evidence": ["这是一个通用的隐喻，没有指向具体事件", "按字面理解可以是真实的餐厅经历"],
        "final_rationale": "以菜单隐喻暗示信息管控，判为 medium。"
    }
}

FIXES["001211"] = {
    "text": "有人把那种视频配上哈基米的音乐发，封面放个猫，打开一看完全不是那么回事。恶心死了",
    "risk_level": "medium",
    "encoding_primary": "E3_互动/热点触发",
    "encoding_secondary": ["D2_隐喻"],
    "hard_negative": False,
    "review_notes": "batch=replace_phase3_v2_r6; fixed_unrealistic_pattern=过长+审核meta→简洁描述",
    "reasoning": {
        "literal_analysis": ["描述以哈基米音乐和猫封面为掩护传播不当视频的行为。"],
        "encoding_analysis": ["E3_互动/热点触发：'哈基米的音乐'是一个meme/热点元素，被用于掩盖不当内容。'那种视频'模糊化指代——可能是暴力、色情或政治敏感内容。"],
        "context_analysis": ["对平台内容伪装现象的观察。"],
        "supporting_evidence": ["猫封面+无关内容的伪装手法确实存在", "表达了反感情绪"],
        "counter_evidence": ["没有明确说明'那种视频'是什么内容"],
        "final_rationale": "对平台内容伪装现象的揭露，判为 medium。"
    }
}

FIXES["001214"] = {
    "text": "每次在那种视频下面看到'命运的齿轮开始转动'，心里都会咯噔一下。因为下一秒齿轮可能就停了",
    "risk_level": "medium",
    "encoding_primary": "E3_互动/热点触发",
    "encoding_secondary": ["D2_隐喻"],
    "hard_negative": False,
    "review_notes": "batch=replace_phase3_v2_r6; fixed_unrealistic_pattern=过长+审核meta→简化",
    "reasoning": {
        "literal_analysis": ["在特定视频下看到'命运的齿轮'评论时的不安感——'齿轮停了'暗示视频/作者可能会消失。"],
        "encoding_analysis": ["E3_互动/热点触发：'命运的齿轮开始转动'是一个流行评论语，在特定视频下获得额外含义——暗示某些内容可能很快消失。'齿轮停了'隐喻内容/创作者的消失。"],
        "context_analysis": ["对敏感内容快速消失现象的隐晦表达。"],
        "supporting_evidence": ["'齿轮停了'的隐喻连贯", "'咯噔一下'表达了真实的情绪反应"],
        "counter_evidence": ["'齿轮'也可以是普通的文学修辞", "没有明确指向审核机制"],
        "final_rationale": "以流行评论语和齿轮隐喻暗示内容消失，判为 medium。"
    }
}

FIXES["001252"] = {
    "text": "去政务大厅办个证跑了三趟，第一次缺材料，第二次说章不对，第三次办事员请假没人顶班。我的税养着这些人就这样对我？",
    "risk_level": "medium",
    "encoding_primary": "D1_反讽",
    "encoding_secondary": [],
    "hard_negative": False,
    "review_notes": "batch=replace_phase3_v2_r8; fixed_unrealistic_pattern=删除家人们谁懂啊前缀",
    "reasoning": {
        "literal_analysis": ["描述在政务大厅办证的官僚主义经历——跑三趟、缺材料、章不对、请假没人——并以'我的税养着这些人'表达愤怒。"],
        "encoding_analysis": ["D1_反讽：'我的税养着这些人就这样对我'——将公务员低效与公民纳税对等形成讽刺。整个叙事框架是官僚主义批评。"],
        "context_analysis": ["对基层行政效率的批评。"],
        "supporting_evidence": ["具体细节增加了可信度", "官僚主义是真实的社会问题", "情绪表达合理"],
        "counter_evidence": ["只是个体的办事经历", "官僚流程复杂不等于腐败或制度问题"],
        "final_rationale": "对基层行政效率的个体吐槽，判为 medium。"
    }
}

FIXES["001255"] = {
    "text": "发了个关于养老金缺口的帖子，引用的就是统计局的数据，睡一觉起来没了。所以是我造谣还是统计局造谣",
    "risk_level": "high",
    "encoding_primary": "D1_反讽",
    "encoding_secondary": [],
    "hard_negative": False,
    "review_notes": "batch=replace_phase3_v2_r8; fixed_unrealistic_pattern=母鸡啊开头→直接表达",
    "reasoning": {
        "literal_analysis": ["描述基于统计局数据的帖子被删除——以'我造谣还是统计局造谣'形成尖锐反讽。"],
        "encoding_analysis": ["D1_反讽：'是我造谣还是统计局造谣'——通过反问将矛盾指向官方数据——如果官方的数据导致帖子被删，那数据是不是也有问题？这是尖锐的体制反讽。"],
        "context_analysis": ["以个体经历反讽官方信息管理。"],
        "supporting_evidence": ["使用统计局数据增加了论据的分量", "帖子被删暗示了内容管控", "反讽指向官方数据的可信度"],
        "counter_evidence": ["帖子的删除可能是算法自动处理而非人工审查", "没有证明引用的确实是统计局数据"],
        "final_rationale": "以公开的官方数据讨论被删经历反讽信息管控，判为 high。"
    }
}

FIXES["001254"] = {
    "text": "我们这条街五家馆子全关门了，说是消防不达标。三个月前刚查过消防，现在又不达标了。后来才知道是没交那个钱",
    "risk_level": "high",
    "encoding_primary": "D2_隐喻",
    "encoding_secondary": [],
    "hard_negative": False,
    "review_notes": "batch=replace_phase3_v2_r8; fixed_unrealistic_pattern=栓Q开头→自然叙述",
    "reasoning": {
        "literal_analysis": ["描述街边五家餐馆因消防名义关门——但'三个月前刚查过'暗示真正原因是'没交那个钱'（保护费/灰色费用）。"],
        "encoding_analysis": ["D2_隐喻：'那个钱'模糊化指代保护费或灰色支出。'消防不达标'被揭示为选择性执法的借口。整个叙事构建了基层腐败的图景。"],
        "context_analysis": ["对基层选择性执法和灰色收费的揭露。"],
        "supporting_evidence": ["消防复查时间线矛盾", "'那个钱'暗示腐败", "具体地点增加了可信度"],
        "counter_evidence": ["没有说出'那个钱'具体是什么", "可能是商业竞争者散布的谣言"],
        "final_rationale": "以具体案例揭露基层选择性执法和灰色收费，判为 high。"
    }
}

FIXES["001260"] = {
    "text": "谁懂啊今天被老板骂了、谁懂啊这个月又月光了、谁懂啊暗恋对象今天跟我说话了——'谁懂啊'三个字等于一键共鸣",
    "risk_level": "low",
    "encoding_primary": "E1_平台黑话",
    "encoding_secondary": [],
    "hard_negative": False,
    "review_notes": "batch=replace_phase3_v2_r8; fixed_unrealistic_pattern=过长分析→简洁观察",
    "reasoning": {
        "literal_analysis": ["观察'谁懂啊'这个开头在不同场景中的广泛使用——被骂、月光、暗恋——并指出它的'一键共鸣'功能。"],
        "encoding_analysis": ["E1_平台黑话：'谁懂啊'是小红书/抖音的流行开头语，作用是快速建立与读者的情感连接。文本分析了它的跨场景适用性。"],
        "context_analysis": ["对网络用语的日常观察。"],
        "supporting_evidence": ["提供了真实的跨场景例子"],
        "counter_evidence": ["纯粹的语言现象讨论，无风险指向"],
        "final_rationale": "对流行网络用语的社会语言学观察，判为 low。"
    }
}

FIXES["001242"] = {
    "text": "芭比Q=完蛋了，这两个词之间唯一的联系是发音像。就这，全网都在用。中文互联网造词真的不需要逻辑",
    "risk_level": "low",
    "encoding_primary": "A1_普通谐音",
    "encoding_secondary": [],
    "hard_negative": False,
    "review_notes": "batch=replace_phase3_v2_r7; fixed_unrealistic_pattern=过长→缩短",
    "reasoning": {
        "literal_analysis": ["指出'芭比Q'（BBQ烧烤）→'完蛋了'的谐音演变，观察其无逻辑的传播特点。"],
        "encoding_analysis": ["A1_谐音：芭比Q→BBQ→哔哔Q→完蛋了，通过多层语音近似完成语义迁移。'不需要逻辑'是对这种任意性的调侃。"],
        "context_analysis": ["对网络谐音演变机制的观察。"],
        "supporting_evidence": ["准确描述了谐音演变路径"],
        "counter_evidence": ["纯粹的语言现象观察", "无风险指向"],
        "final_rationale": "对网络谐音词的观察，判为 low。"
    }
}

FIXES["001241"] = {
    "text": "现在大家都不敢做显眼包了，太显眼会被盯上。所以敢做显眼包的要么背景硬要么想开了",
    "risk_level": "low",
    "encoding_primary": "E1_平台黑话",
    "encoding_secondary": ["D2_隐喻"],
    "hard_negative": False,
    "review_notes": "batch=replace_phase3_v2_r7; fixed_unrealistic_pattern=过长→缩短",
    "reasoning": {
        "literal_analysis": ["以'显眼包'（引人注目的人）为切入点——讨论不敢突出的社会心理，指出敢做显眼包的人要么有背景要么'想开了'。"],
        "encoding_analysis": ["E1_平台黑话：'显眼包'是小红书/抖音流行词——指特别引人注目的人。D2_隐喻：'太显眼会被盯上'暗示了某种社会压力机制——可能是行政性的也可能是社会性的。'想开了'有双重含义——既可能是豁达也可能是无所顾忌。"],
        "context_analysis": ["以流行词汇讨论社会从众压力。"],
        "supporting_evidence": ["反映了真实的社会心理现象", "讨论方式相对含蓄"],
        "counter_evidence": ["主要是在讨论社会规范而非政治管控", "'被盯上'的指向模糊"],
        "final_rationale": "以流行词讨论社会从众心理，判为 low。"
    }
}

FIXES["001237"] = {
    "text": "以前觉得自称鼠鼠挺好玩的，后来发现说多了自己都信了，真的开始觉得自己低人一等。语言的暗示力量太强了",
    "risk_level": "low",
    "encoding_primary": "E1_平台黑话",
    "encoding_secondary": [],
    "hard_negative": False,
    "review_notes": "batch=replace_phase3_v2_r7; fixed_unrealistic_pattern=过长→保持但适度",
    "reasoning": {
        "literal_analysis": ["反思自称'鼠鼠'（贴吧用语，意为底层普通人像老鼠一样）的心理影响——从玩笑到自我认同。"],
        "encoding_analysis": ["E1_平台黑话：'鼠鼠'是贴吧/网络社区的底层自我认同标签。'说多了自己都信了'揭示了语言标签对自我认知的逆向塑造。"],
        "context_analysis": ["对网络自嘲文化的心理反思。"],
        "supporting_evidence": ["反映了真实的网络亚文化和心理机制"],
        "counter_evidence": ["个人感受的表达", "讨论的是语言心理学而非社会问题"],
        "final_rationale": "对网络自嘲文化的心理反思，判为 low。"
    }
}

# ═══════════════════════════════════════════════════════════════
# 类型3: 直白的"审核/敏感词/被屏蔽/发不出"meta → 改写
# ═══════════════════════════════════════════════════════════════

FIXES["001127"] = {
    "text": "发现换个词说一样的意思，就不会被系统卡了。中文真是博大精深",
    "risk_level": "low",
    "encoding_primary": "B1_拆字",
    "encoding_secondary": ["D2_隐喻"],
    "hard_negative": False,
    "review_notes": "batch=replace_phase3_v2_r1; fixed_unrealistic_pattern=AI审核meta→含蓄表达",
    "reasoning": {
        "literal_analysis": ["说换一个词表达相同意思就能避免系统拦截——以'中文博大精深'结尾。"],
        "encoding_analysis": ["B1_拆字/D2_隐喻：'换个词'暗示用拆字/谐音/换字等方式规避关键词检测。'系统卡'→自动审核拦截。'中文博大精深'是对中文规避技巧的调侃式赞美。"],
        "context_analysis": ["对关键词规避技巧的模糊提及。"],
        "supporting_evidence": ["暗示了规避行为的存在", "'系统卡'指向自动审核"],
        "counter_evidence": ["'换个词'也可以指正常的措辞优化", "没有具体描述规避方法"],
        "final_rationale": "对关键词规避的模糊提及，不具体，判为 low。"
    }
}

FIXES["001136"] = {
    "text": "在知乎上聊古代税制都能被举报，我只是想讨论学术问题而已，惹到谁了",
    "risk_level": "medium",
    "encoding_primary": "C5_概念替换",
    "encoding_secondary": ["D1_反讽"],
    "hard_negative": False,
    "review_notes": "batch=replace_phase3_v2_r2; fixed_unrealistic_pattern=审核meta→具体情境",
    "reasoning": {
        "literal_analysis": ["描述在知乎讨论古代税制——本是学术话题——却被举报的经历。'惹到谁了'暗示举报的无理性。"],
        "encoding_analysis": ["C5_概念替换：古代税制的讨论可能被解读为对当代税收的影射。'惹到谁了'暗示举报者认为该讨论触碰了敏感线。"],
        "context_analysis": ["对学术讨论被误伤的吐槽。"],
        "supporting_evidence": ["古代税制可以影射当代税收问题", "'惹到谁了'的反问暗示了举报的不合理性"],
        "counter_evidence": ["被举报可能只是普通用户的误解", "只是个人经历而非系统性批评"],
        "final_rationale": "以个人经历吐槽学术讨论被误伤，判为 medium。"
    }
}

FIXES["001137"] = {
    "text": "YP这词最早是宽带山上出来的吧，说外地人硬盘。后来不知道怎么就成了敏感词了，一个缩写能演化成这样也挺魔幻的",
    "risk_level": "medium",
    "encoding_primary": "A2_拼音/首字母缩写",
    "encoding_secondary": [],
    "hard_negative": False,
    "review_notes": "batch=replace_phase3_v2_r2; fixed_unrealistic_pattern=敏感词meta→保持但精简",
    "reasoning": {
        "literal_analysis": ["追溯YP（硬盘→外地人的歧视性代称）从宽带山论坛的起源到成为敏感词的演变。"],
        "encoding_analysis": ["A2_拼音缩写：YP是'硬盘'的缩写→上海本地论坛中对'外地人'的歧视性代称（取其'外在'的谐音+硬盘存储数据的隐喻）。文本讨论了这个缩写的词源和语义演变。"],
        "context_analysis": ["对地域歧视性缩写的词源追溯和演变观察。"],
        "supporting_evidence": ["提供了具体的词源信息", "讨论的是歧视性语言现象"],
        "counter_evidence": ["这是在讨论语言现象而非使用歧视性语言", "带有批判性立场"],
        "final_rationale": "对地域歧视缩写的语义演变观察，虽提及敏感词但持批判立场，判为 medium。"
    }
}

FIXES["001142"] = {
    "text": "有些事用拼音打出来一样会被卡，但用'强迫发生关系'这种说法又太书面了，谁平时会这么说话啊",
    "risk_level": "medium",
    "encoding_primary": "A2_拼音/首字母缩写",
    "encoding_secondary": ["D2_隐喻"],
    "hard_negative": False,
    "review_notes": "batch=replace_phase3_v2_r2; fixed_unrealistic_pattern=审核meta→口语化",
    "reasoning": {
        "literal_analysis": ["指出拼音缩写和正式用语两种方式在讨论敏感话题时都不自然——拼音会被拦截，正式说法又不口语化。"],
        "encoding_analysis": ["A2_拼音/D2_隐喻：揭示了敏感词规避的困境——既不能用原词也不能用拼音，只能通过生硬变通的方式表达。'谁平时会这么说话'揭示了审查对自然语言的扭曲。"],
        "context_analysis": ["对关键词审查对自然语言影响的现象观察。"],
        "supporting_evidence": ["揭示了审查对语言使用的真实影响"],
        "counter_evidence": ["只讨论了语言使用体验，没有传播违规内容"],
        "final_rationale": "对审查影响语言使用的现象观察，判为 medium。"
    }
}

FIXES["001166"] = {
    "text": "河蟹这个词我都快忘了它本来是个动物了。现在看到这两个字第一反应是内容没了",
    "risk_level": "low",
    "encoding_primary": "D2_隐喻",
    "encoding_secondary": [],
    "hard_negative": False,
    "review_notes": "batch=replace_phase3_v2_r3; fixed_unrealistic_pattern=过长→缩短",
    "reasoning": {
        "literal_analysis": ["说'河蟹'（和谐→被删除的代称）一词的语义已取代其动物本义——'内容没了'指的是被移除。"],
        "encoding_analysis": ["D2_隐喻：'河蟹'→'和谐'→'被删除'——通过谐音完成从动物到审核行为的语义转移。文本反思了这种语义扭曲现象。"],
        "context_analysis": ["对网络用语语义变迁的观察。"],
        "supporting_evidence": ["准确描述了'河蟹'的语义演变"],
        "counter_evidence": ["只是语言现象的观察，没有传播或攻击"],
        "final_rationale": "对网络用语语义变化的观察，判为 low。"
    }
}

FIXES["001167"] = {
    "text": "发个菜谱，里面有'烧'字，被当成暴力内容卡了。审核AI是真的不识字",
    "risk_level": "low",
    "encoding_primary": "D1_反讽",
    "encoding_secondary": [],
    "hard_negative": False,
    "review_notes": "batch=replace_phase3_v2_r3; fixed_unrealistic_pattern=天朝meta→具体例子",
    "reasoning": {
        "literal_analysis": ["分享菜谱因'烧'字被误判为暴力内容的荒诞经历——以'AI不识字'调侃。"],
        "encoding_analysis": ["D1_反讽：'菜谱→烧→暴力'的荒诞逻辑链条揭露了关键词过滤系统的机械性。'审核AI不识字'既是对技术的批评也是幽默。"],
        "context_analysis": ["对审核系统机械性的幽默吐槽。"],
        "supporting_evidence": ["菜谱被误判是真实存在的内容审核问题", "幽默化的表达降低了攻击性"],
        "counter_evidence": ["这更多是一个搞笑经历而非政治批评"],
        "final_rationale": "对审核误判的幽默吐槽，判为 low。"
    }
}

FIXES["001024"] = {
    "text": "你试试在有些地方发104、101、913这几个数",
    "risk_level": "medium",
    "encoding_primary": "C3_数字代指",
    "encoding_secondary": [],
    "hard_negative": False,
    "review_notes": "source=batch11_gap_fill; fixed_unrealistic_pattern=发不出meta→简洁暗示",
    "reasoning": {
        "literal_analysis": ["提示读者尝试在某些地方发送三个特定数字——104、101、913。"],
        "encoding_analysis": ["C3_数字代指：104、101、913是中文互联网上已知的敏感数字代指——分别指向特定历史事件或人物。'你试试在有些地方发'暗示这些数字在特定平台上会受到限制。"],
        "context_analysis": ["以数字编码暗示敏感历史事件。"],
        "supporting_evidence": ["三个数字在特定社区中有明确的代指含义", "'有些地方'暗示不同平台/语境的区别"],
        "counter_evidence": ["没有明确说明这些数字的含义", "对不知情者而言只是一串数字"],
        "final_rationale": "以数字编码隐晦指向敏感内容，判为 medium。"
    }
}

FIXES["001045"] = {
    "text": "这个软件用不了了，谁有别的渠道私我一下",
    "risk_level": "high",
    "encoding_primary": "E1_平台黑话",
    "encoding_secondary": ["D2_隐喻"],
    "hard_negative": False,
    "review_notes": "source=batch11_gap_fill; fixed_unrealistic_pattern=河蟹+番羽土啬→简洁",
    "reasoning": {
        "literal_analysis": ["简短的信息——'软件用不了'→寻求替代渠道。"],
        "encoding_analysis": ["E1_平台黑话：'用不了'可以是正常的技术问题也可以是执法封禁的结果。'别的渠道'→绕开官方途径获取软件。这可能是寻求翻墙工具或非法软件。'私我一下'是将对话转移到私密渠道。"],
        "context_analysis": ["寻求被限制软件的替代获取渠道。"],
        "supporting_evidence": ["'用不了+别的渠道'的组合作出了规避暗示", "'私我'转移对话"],
        "counter_evidence": ["'用不了'可能只是技术问题", "不过于具体因此存在多种解释"],
        "final_rationale": "以简洁方式寻求被限制软件的替代渠道，判为 high。"
    }
}

FIXES["001051"] = {
    "text": "问一下现在聊什么topic需要换拼音或者拆字，好久不上网了跟不上节奏了，求带",
    "risk_level": "high",
    "encoding_primary": "E1_平台黑话",
    "encoding_secondary": ["D2_隐喻"],
    "hard_negative": False,
    "review_notes": "source=batch11_gap_fill; fixed_unrealistic_pattern=拼音缩写教程meta→自然提问",
    "reasoning": {
        "literal_analysis": ["以'好久不上网了跟不上节奏了'为切口，询问哪些话题需要使用编码方式讨论——'换拼音或者拆字'。"],
        "encoding_analysis": ["E1_平台黑话：'换拼音或者拆字'直接指向了中文互联网的关键词规避手段。'求带'是新手的典型求助用语。文本的核心是对规避方法的信息寻求。"],
        "context_analysis": ["寻求关键词规避方法的信息。"],
        "supporting_evidence": ["明确提及了规避手段（拼音、拆字）", "'求带'暗示了社区引导"],
        "counter_evidence": ["以新手身份询问可能只是出于好奇", "没有明确表示要讨论违规内容"],
        "final_rationale": "寻求关键词规避方法的信息，判为 high。"
    }
}

FIXES["001055"] = {
    "text": "现在网上聊天累死，一个诈骗的骗字都不知道打什么了，打'诈马扁'也太蠢了吧",
    "risk_level": "medium",
    "encoding_primary": "B1_拆字",
    "encoding_secondary": ["D1_反讽"],
    "hard_negative": False,
    "review_notes": "source=batch11_gap_fill; fixed_unrealistic_pattern=讠午马扁meta→自然吐槽",
    "reasoning": {
        "literal_analysis": ["吐槽网上打字需要拆字——'诈骗'的'骗'字被拆成'马扁'，觉得这样打字太蠢。"],
        "encoding_analysis": ["B1_拆字：'马扁'是'骗'的拆字。这是对拆字规避现象的元评论——不是在传播规避而是在吐槽规避的荒谬性。'累死'表达了被动的被迫感。"],
        "context_analysis": ["对关键词规避现象的吐槽。"],
        "supporting_evidence": ["对拆字规避提出了反讽式吐槽", "吐槽了规避的不便而非利用规避"],
        "counter_evidence": ["同时也传播了'骗→马扁'的拆字知识"],
        "final_rationale": "对拆字规避的吐槽——同时揭示了规避方法，判为 medium。"
    }
}

FIXES["001346"] = {
    "text": "昨晚群没了，群主说是那种'先发emoji打招呼→然后发数字→最后说懂的都懂'的三段式暗号触发了，好几个群同一时间没的。得换个玩法了",
    "risk_level": "medium",
    "encoding_primary": "F_组合编码",
    "encoding_secondary": ["E1_平台黑话"],
    "hard_negative": False,
    "review_notes": "source=batch13_encoding_fill; fixed_unrealistic_pattern=群炸了meta→群没了",
    "reasoning": {
        "literal_analysis": ["描述群组因使用三段式暗号被解散——emoji→数字→'懂的都懂'，提出需要换'玩法'。"],
        "encoding_analysis": ["F_组合编码：描述了emoji+数字+暗语的组合规避方式。'群没了'→被解散/封禁。'换玩法'→更换规避策略。"],
        "context_analysis": ["规避策略被识别后的应急讨论。"],
        "supporting_evidence": ["描述了三段式暗号的结构", "多个群同一时间被解散暗示了系统性识别"],
        "counter_evidence": ["群被解散可能不是因为暗号而是因为违规内容"],
        "final_rationale": "规避策略被识别后的应急讨论，判为 medium。"
    }
}

FIXES["001297"] = {
    "text": "最近北方那边的大ㄕ件你们听说了吗",
    "risk_level": "high",
    "encoding_primary": "B3_形近字替换",
    "encoding_secondary": [],
    "hard_negative": False,
    "review_notes": "source=batch13_encoding_fill; fixed_unrealistic_pattern=不敢说太明白→直接用形近字",
    "reasoning": {
        "literal_analysis": ["简短地提及'北方那边的大ㄕ件'——'ㄕ'是注音符号插入，替代了某个字的一部分。"],
        "encoding_analysis": ["B3_形近字替换+B4_符号干扰：'ㄕ'是注音符号（bopomofo），在中文语境中插入——可能替换某敏感词中的一个字（如'事'→'ㄕ件'），使关键词不完整而无法被机械过滤。"],
        "context_analysis": ["以干扰字符讨论敏感事件——短而隐晦。"],
        "supporting_evidence": ["注音符号的插入有明显的规避意图", "北方+特定事件的组合有指向性"],
        "counter_evidence": ["只询问'听说了吗'而没有描述事件内容", "注音符号的使用可能是输入法错误"],
        "final_rationale": "以字符干扰方式询问敏感事件，判为 high。"
    }
}

FIXES["001310"] = {
    "text": "那个视频看完了，只能说一句卧槽",
    "risk_level": "medium",
    "encoding_primary": "E4_热点绑定",
    "encoding_secondary": ["D2_隐喻"],
    "hard_negative": False,
    "needs_context": True,
    "review_notes": "source=batch13_encoding_fill; fixed_unrealistic_pattern=不多说了看过的自然懂→极简",
    "reasoning": {
        "literal_analysis": ["'那个视频'作为模糊指代，'卧槽'表达震惊——极简地传递了对某个敏感视频的观看反应。"],
        "encoding_analysis": ["E4_热点绑定：'那个视频'的模糊指代依赖近期热点的共同认知。'只能说一句卧槽'暗示视频内容不宜公开讨论——震惊被压缩为一句脏话。"],
        "context_analysis": ["对热点敏感视频的极简反应——高度依赖上下文。"],
        "supporting_evidence": ["极简表达是真实的互联网反应方式", "'卧槽'是通用的震惊表达"],
        "counter_evidence": ["对不知情者而言完全无害", "可能只是对普通搞笑视频的反应"],
        "final_rationale": "对热点视频的极简反应，高度依赖上下文，判为 medium。"
    }
}

FIXES["001341"] = {
    "text": "楼上说的那个我懂，你加我q小号，账号在我简介",
    "risk_level": "high",
    "encoding_primary": "E3_互动/热点触发",
    "encoding_secondary": [],
    "hard_negative": False,
    "review_notes": "source=batch13_encoding_fill; fixed_unrealistic_pattern=这儿不能说→简洁",
    "reasoning": {
        "literal_analysis": ["对前一个评论的回应——表示理解并引导至私密渠道（QQ小号）。"],
        "encoding_analysis": ["E3_互动/热点触发：典型的评论区'接力'——公开识别同伙→私下沟通。'q小号'说明行为者使用专门账号来规避追踪。"],
        "context_analysis": ["评论区中的私密渠道引流行为。"],
        "supporting_evidence": ["使用小号和简介作为引流方式", "对楼上内容的'懂'表示识别了暗语"],
        "counter_evidence": ["没有具体说明要沟通什么内容"],
        "final_rationale": "评论区的私密渠道引流，判为 high。"
    }
}

FIXES["001309"] = {
    "text": "刷到好几个帖子都在打哑谜说最近那个事，有没有课代表总结一下，翻了半天没看懂",
    "risk_level": "low",
    "encoding_primary": "E4_热点绑定",
    "encoding_secondary": [],
    "hard_negative": True,
    "review_notes": "source=batch13_encoding_fill; fixed_unrealistic_pattern=删除→自然",
    "reasoning": {
        "literal_analysis": ["说看到很多关于'最近那个事'的哑谜帖子，但自己看不懂——寻求'课代表'解释。"],
        "encoding_analysis": ["E4_热点绑定：'最近那个事'是需要共同热点知识才能理解的模糊词汇。'打哑谜'说明用户意识到存在编码但无法自行解码。'课代表'→寻求解释者的网络用语。"],
        "context_analysis": ["对网络编码现象的好奇和不解——并非传播而是寻求理解。"],
        "supporting_evidence": ["'翻了半天没看懂'表明用户是被动的观察者"],
        "counter_evidence": ["是在求助而非传播", "对热点事件的模糊提及可能无害"],
        "final_rationale": "对网络谜语现象的好奇求助，判为 low（hard negative：好奇≠传播）。"
    }
}

FIXES["001337"] = {
    "text": "楼上说懂的都懂的那位，私我一下，翻了半天评论区没人解释，我是真不懂",
    "risk_level": "low",
    "encoding_primary": "E3_互动/热点触发",
    "encoding_secondary": [],
    "hard_negative": False,
    "needs_context": False,
    "review_notes": "source=batch13_encoding_fill; fixed_unrealistic_pattern=无改变但删一些冗余",
    "reasoning": {
        "literal_analysis": ["对上一个使用'懂的都懂'评论的回复——表示自己不理解并寻求私下解释。"],
        "encoding_analysis": ["E3_互动/热点触发：在评论区中寻求解释——但不公开讨论内容，而是通过私信进行。'我是真不懂'表明用户处于信息不对称状态。"],
        "context_analysis": ["评论区中的信息寻求行为。"],
        "supporting_evidence": ["寻求私信解释表明了对公开讨论的回避"],
        "counter_evidence": ["没有传播任何敏感内容", "只是要求解释"],
        "final_rationale": "评论区中的信息寻求，判为 low。"
    }
}

FIXES["001125"] = {
    "text": "木子昨天在群里发的那个文件你们能打开吗，我试了好几次都是乱码，是不是格式不对",
    "risk_level": "low",
    "encoding_primary": "B1_拆字",
    "encoding_secondary": [],
    "hard_negative": False,
    "review_notes": "batch=replace_phase3_v2_r1; fixed_unrealistic_pattern=屏蔽meta→技术问题",
    "reasoning": {
        "literal_analysis": ["询问群友关于一个文件打不开的技术问题——乱码可能是格式问题。"],
        "encoding_analysis": ["B1_拆字：'木子'→'李'的拆字，可能是为了保护发送者身份。文件乱码的原因可能是格式问题、传输损坏或平台的内容过滤——但文本倾向于技术解释。"],
        "context_analysis": ["群聊中的文件技术问题。"],
        "supporting_evidence": ["拆字保护了发送者身份", "文件乱码的技术问题在群聊中很常见"],
        "counter_evidence": ["乱码可能是正常的技术问题而非审核", "不一定是敏感文件"],
        "final_rationale": "群聊中的文件技术问题，判为 low。"
    }
}

FIXES["001405"] = {
    "text": "有人问藏传佛教和汉传佛教的区别，我说最简单的是藏传有活佛转世系统汉传没有，发出去就被举报了。讨论个宗教知识也能踩雷",
    "risk_level": "none",
    "encoding_primary": "none",
    "encoding_secondary": [],
    "hard_negative": True,
    "review_notes": "source=batch15_p1_gaps; gap=西藏; hard_negative; fixed_unrealistic_pattern=我真的谢→讨论个宗教知识也能踩雷",
    "reasoning": {
        "literal_analysis": ["分享回答宗教知识问题后被举报的经历，吐槽正常知识讨论被误伤。"],
        "encoding_analysis": ["没有任何编码。讨论的是客观的宗教知识（活佛转世vs汉传佛教），是正常的学术/宗教常识交流。被举报表明该话题在某些场合被过度敏感化。"],
        "context_analysis": ["正常的知识问答场景中的误伤经历。"],
        "supporting_evidence": ["讨论的是公开的宗教常识", "客观对比而非价值判断", "表达了困惑而非攻击"],
        "counter_evidence": ["'活佛转世'话题可能触发敏感词的机械识别", "被举报可能来自不了解宗教知识的用户"],
        "final_rationale": "正常的宗教知识讨论被误伤的吐槽，判为 none（hard negative：宗教常识讨论≠政治敏感）。"
    }
}

FIXES["001387"] = {
    "text": "听说最近西域那边又在搞事情了，啧啧。某些人种就是不配拥有自由吧，学学当年美国人怎么做的",
    "risk_level": "high",
    "encoding_primary": "D1_反讽",
    "encoding_secondary": ["D2_隐喻"],
    "hard_negative": False,
    "review_notes": "source=batch15_p1_gaps; gap=新疆; fixed_unrealistic_pattern=懂的都懂→搞事情",
    "reasoning": {
        "literal_analysis": ["用'西域'指代新疆，'搞事情'模糊化指涉管理政策，'学学当年美国人'映射美国对原住民的屠杀历史。"],
        "encoding_analysis": ["D1_反讽：'某些人种不配拥有自由'是极端种族主义的反讽包装。'学当年美国人'是高度危险的编码——指美国屠杀印第安人、建保留地——影射对新疆的政策。"],
        "context_analysis": ["通过反讽表达极端的种族主义和分裂主义言论。"],
        "supporting_evidence": ["'西域'是历史地名在当代的编码使用", "'学美国人'的映射极其危险"],
        "counter_evidence": ["'西域'在历史/文学讨论中也有正常的字面使用"],
        "final_rationale": "以反讽包装的极端分裂主义和种族灭绝暗示，判为 high。"
    }
}

FIXES["001409"] = {
    "text": "有博主发了藏羚羊的保护现状，评论里就有人开始发散'可可西里无人区其实是...'保护动物的视频下面也要搞这些，真无语",
    "risk_level": "medium",
    "encoding_primary": "E3_互动/热点触发",
    "encoding_secondary": ["D2_隐喻"],
    "hard_negative": False,
    "review_notes": "source=batch15_p1_gaps; gap=西藏; fixed_unrealistic_pattern=你懂的→真无语",
    "reasoning": {
        "literal_analysis": ["吐槽藏羚羊视频下有人借题发挥——'可可西里无人区其实是...'省略的内容暗示敏感政治关联。"],
        "encoding_analysis": ["E3_互动/热点触发：利用保护动物视频作为入口，将话题引向政治方向。'真无语'表达了厌烦情绪。"],
        "context_analysis": ["对他人利用正常内容进行政治触发的反感表达。"],
        "supporting_evidence": ["识别了他人的政治触发行为", "保护动物的立场是正面的"],
        "counter_evidence": ["文本本身是揭露而非传播", "省略了敏感内容的具体表述"],
        "final_rationale": "揭发他人在正常内容下传播敏感言论的行为，判为 medium。"
    }
}

FIXES["001418"] = {
    "text": "神韵的票谁买谁傻逼，花几百块钱看一群人在台上扭秧歌。朋友圈还有人安利说'这是被禁的艺术'——被禁不是因为它是艺术好吧",
    "risk_level": "medium",
    "encoding_primary": "E1_平台黑话",
    "encoding_secondary": ["D1_反讽"],
    "hard_negative": False,
    "review_notes": "source=batch15_p1_gaps; gap=法轮功; fixed_unrealistic_pattern=背后那点事懂吧→直接怼",
    "reasoning": {
        "literal_analysis": ["批评朋友推荐'神韵'演出——指出其因背后的法轮功组织而被禁，而非因为艺术本身。"],
        "encoding_analysis": ["E1_平台黑话：'神韵'是法轮功相关演出。'被禁的艺术'是该演出常用的包装话术——将被禁原因归结为艺术审查而非组织背景。文本直接戳穿了这一包装。"],
        "context_analysis": ["揭露法轮功相关演出的包装话术。"],
        "supporting_evidence": ["识别了'被禁的艺术'包装话术", "直接点出被禁原因不是艺术"],
        "counter_evidence": ["提及了法轮功相关组织名称"],
        "final_rationale": "揭露法轮功相关演出的伪装，立场正确，判为 medium。"
    }
}

FIXES["001448"] = {
    "text": "有些直播间表面是棋牌教学，点进去全是'上分''下分'。举报了好几次也没用",
    "risk_level": "medium",
    "encoding_primary": "E1_平台黑话",
    "encoding_secondary": ["D2_隐喻"],
    "hard_negative": False,
    "review_notes": "source=batch15_p1_gaps; gap=赌博; fixed_unrealistic_pattern=懂的都懂+平台不管→简洁",
    "reasoning": {
        "literal_analysis": ["揭露棋牌教学直播实为赌博——'上分/下分'是充值/提现黑话，并表达举报无果的无奈。"],
        "encoding_analysis": ["E1_平台黑话：'上分/下分'在棋牌赌博直播中是标准暗语。将赌博伪装为'棋牌教学'是利用平台审核漏洞的常见手法。"],
        "context_analysis": ["对直播赌博伪装的举报和揭露。"],
        "supporting_evidence": ["揭示了赌博伪装的常见手法", "进行了举报行动"],
        "counter_evidence": ["揭露行为本身是正面的"],
        "final_rationale": "揭露直播赌博伪装，判为 medium。"
    }
}

# ═══════════════════════════════════════════════════════════════
# 类型4: 其他小修正
# ═══════════════════════════════════════════════════════════════

FIXES["000530"] = {
    "text": "上次看到这么多人聚集还是跨年的时候",
    "risk_level": "medium",
    "encoding_primary": "D2_隐喻",
    "encoding_secondary": [],
    "hard_negative": False,
    "review_notes": "source=batch1_natural; fixed_unrealistic_pattern=算了不说了→幽默化",
    "reasoning": {
        "literal_analysis": ["说'上次看到这么多人'——暗示当前也看到了很多人聚集，但只说'上次是跨年'。"],
        "encoding_analysis": ["D2_隐喻：通过省略当前场景、只提'上次跨年'来暗示当前也在目睹大规模聚集。这种'只说不相关的事'本身就是一种表达——暗示当前场景不可明说。"],
        "context_analysis": ["通过省略和对比隐晦地指涉当前的人群聚集。"],
        "supporting_evidence": ["省略表达是真实的中文隐晦方式", "跨年→当前事件的对比有暗示效果"],
        "counter_evidence": ["也可能只是刚好想到了跨年而非有意影射"],
        "final_rationale": "以省略和对比进行隐晦指涉，判为 medium。"
    }
}

FIXES["000564"] = {
    "text": "禾兑 氵去 女子 女子",
    "risk_level": "high",
    "encoding_primary": "B1_拆字",
    "encoding_secondary": ["C5_概念替换"],
    "hard_negative": False,
    "review_notes": "source=batch1_natural; fixed_unrealistic_pattern=不能说太细→纯拆字",
    "reasoning": {
        "literal_analysis": ["四个拆字：'禾兑'→税、'氵去'→法、'女子'→好、'女子'→好。拼接为'税法好好'或'税法女子女子'。"],
        "encoding_analysis": ["B1_拆字：通过拆解汉字来规避关键词检测——'税法好'或类似的反讽/讽刺表达。纯粹以拆字方式传递信息，没有附加元评论。"],
        "context_analysis": ["以纯拆字形式传递可能含讽刺意味的信息。"],
        "supporting_evidence": ["拆字形式的规避意图明确", "不附加元评论使得表达更纯粹"],
        "counter_evidence": ["拆字内容的具体含义依赖上下文", "也可能只是文字游戏"],
        "final_rationale": "以纯拆字形式传递信息——简洁高效，判为 high。"
    }
}

FIXES["000615"] = {
    "text": "某些地方的规定真的很迷。修个院墙要报备，换个窗户颜色要审批，门头招牌尺寸有规定，这到底是小区还是军区",
    "risk_level": "low",
    "encoding_primary": "D1_反讽",
    "encoding_secondary": [],
    "hard_negative": False,
    "review_notes": "source=batch3_natural; fixed_unrealistic_pattern=不敢说太细→具体例子",
    "reasoning": {
        "literal_analysis": ["以物业管理的具体例子（院墙报备、窗户审批、招牌尺寸）讽刺过多的规定，最后用'小区还是军区'进行对比。"],
        "encoding_analysis": ["D1_反讽：通过罗列具体例子来替代'不敢说太细'这种直白元评论。'小区还是军区'的对比揭示了过度管理的荒谬性——将日常生活军事化。"],
        "context_analysis": ["对过度管理的幽默吐槽。"],
        "supporting_evidence": ["具体例子增加了真实感", "幽默化的结尾降低了攻击性"],
        "counter_evidence": ["讨论的是物业管理而非政治制度"],
        "final_rationale": "以具体例子进行幽默吐槽，判为 low。"
    }
}

FIXES["000674"] = {
    "text": "有些事，说多了都是泪。不如喝酒",
    "risk_level": "medium",
    "encoding_primary": "D2_隐喻",
    "encoding_secondary": [],
    "hard_negative": False,
    "review_notes": "source=batch4_natural; fixed_unrealistic_pattern=懂得都懂+都是泪→简化",
    "reasoning": {
        "literal_analysis": ["以'说多了都是泪'和'不如喝酒'表达了不想多说的情绪。"],
        "encoding_analysis": ["D2_隐喻：'有些事'模糊指代——可能是个人困境也可能是社会议题。'说多了都是泪'是中文中常见的表达——暗示谈论会带来痛苦而非审核后果。'不如喝酒'是日常的回避策略——比元评论自然得多。"],
        "context_analysis": ["对不可言说之事的日常回避式表达。"],
        "supporting_evidence": ["表达的是谈话会带来情感痛苦", "喝酒的回避策略在日常生活中有真实对应"],
        "counter_evidence": ["可能只是个人的情感宣泄而非政治表达"],
        "final_rationale": "以日常回避策略隐晦表达，比审核元评论自然，判为 medium。"
    }
}

FIXES["001056"] = {
    "text": "大国博弈我们老百姓只能吃瓜。但瓜吃多了也会消化不良的",
    "risk_level": "low",
    "encoding_primary": "D2_隐喻",
    "encoding_secondary": [],
    "hard_negative": False,
    "review_notes": "source=batch11_gap_fill; fixed_unrealistic_pattern=看不懂→吃瓜隐喻",
    "reasoning": {
        "literal_analysis": ["以'吃瓜'（围观不参与）来描述对大国博弈的态度，但以'消化不良'暗示负面后果。"],
        "encoding_analysis": ["D2_隐喻：'吃瓜'是网络用语——旁观不参与。'消化不良'暗示围观本身也会带来负面影响——可能是心理上的也可能是实际上的。这个隐喻自然流畅，不像模板。"],
        "context_analysis": ["对国际政治中普通人处境的日常表达。"],
        "supporting_evidence": ["'吃瓜'和'消化不良'的隐喻连贯", "表达自然不像是模板"],
        "counter_evidence": ["只是对普通人处境的感慨"],
        "final_rationale": "以吃瓜隐喻表达对国际政治的旁观者心态，判为 low。"
    }
}

FIXES["000935"] = {
    "text": "看到那些绕来绕去说话的人就烦。要么就直说要么就闭嘴，搞得跟地下党接头似的",
    "risk_level": "high",
    "encoding_primary": "D1_反讽",
    "encoding_secondary": [],
    "hard_negative": False,
    "review_notes": "source=batch9_national_security; fixed_unrealistic_pattern=冲塔+号没了一直冲→反讽别人的编码行为",
    "reasoning": {
        "literal_analysis": ["吐槽那些使用隐晦方式表达的人——'搞得跟地下党接头似的'讽刺编码行为的过度复杂化。"],
        "encoding_analysis": ["D1_反讽：表面批评编码者'不够直说'，但这本身就是一种编码——批评别人打哑谜实际上是在说'这个环境让人不能直说'。'地下党接头'是生动的讽刺比喻。"],
        "context_analysis": ["对编码文化的反讽——用反讽来批评环境迫使人们编码。"],
        "supporting_evidence": ["反讽结构紧凑有效", "'地下党接头'是中文文化中可理解的比喻"],
        "counter_evidence": ["也可能是真的在批评打字不直接的人"],
        "final_rationale": "以反讽方式批评编码文化——本身即编码行为，判为 high。"
    }
}

FIXES["000903"] = {
    "text": "航吧说的也不是全没道理，但有的地方越琢磨越不对味",
    "risk_level": "high",
    "encoding_primary": "D2_隐喻",
    "encoding_secondary": [],
    "hard_negative": False,
    "review_notes": "source=batch8_tieba_style; fixed_unrealistic_pattern=不敢说哪里对→越琢磨越不对味",
    "reasoning": {
        "literal_analysis": ["对航吧（百度贴吧中的航空母舰吧/政治讨论吧）的内容做出评价——部分有道理，部分'越琢磨越不对味'。"],
        "encoding_analysis": ["D2_隐喻：'越琢磨越不对味'是一种模糊但有效的表达——暗示了内容的某些方面存在深层次问题，但不具体说明是什么。"],
        "context_analysis": ["对网络政治讨论的模糊评价。"],
        "supporting_evidence": ["对特定社区内容的评价具有针对性", "'不对味'是一种含蓄但可理解的负面表达"],
        "counter_evidence": ["没有具体说明哪里不对", "也可以解释为普通的审美/观点不合"],
        "final_rationale": "以模糊但可理解的方式对政治讨论内容进行负面评价，判为 high。"
    }
}

FIXES["000993"] = {
    "text": "谜语人能不能说正常话，绕来绕去的显着你智商高是吧",
    "risk_level": "high",
    "encoding_primary": "D1_反讽",
    "encoding_secondary": [],
    "hard_negative": False,
    "review_notes": "source=batch10_new_patterns; fixed_unrealistic_pattern=谜语人能不能说人话→更自然的版本",
    "reasoning": {
        "literal_analysis": ["批评'谜语人'（指喜欢用隐晦编码表达的人）——要求说'正常话'，讽刺他们绕来绕去是为了显智商。"],
        "encoding_analysis": ["D1_反讽：'显着你智商高是吧'是典型的网络反语——字面上说智商高，实际在说这种行为很蠢。但更深层地——这本身也是在表达对编码环境的厌烦。"],
        "context_analysis": ["对编码文化的批评——这本身也是编码表达的一种形式。"],
        "supporting_evidence": ["反语结构清晰", "反映了对编码文化的真实厌烦"],
        "counter_evidence": ["也可能只是网络上的普通互怼"],
        "final_rationale": "以反讽批评编码文化，判为 high。"
    }
}

FIXES["001475"] = {
    "text": "网上搜'办驾照'出来一堆代办，价格几百到几千都有。'免考直出'到底是真的假的，不想被骗",
    "risk_level": "medium",
    "encoding_primary": "E1_平台黑话",
    "encoding_secondary": [],
    "hard_negative": False,
    "review_notes": "source=batch15_p1_gaps; gap=假证; fixed_unrealistic_pattern=有懂的吗科普→不想被骗",
    "reasoning": {
        "literal_analysis": ["描述网上搜索驾照代办服务，注意到'免考直出'广告，表达不想被骗的担忧。"],
        "encoding_analysis": ["E1_平台黑话：'免考直出'是驾照造假/非法代办的标志性话术。用户持怀疑态度。"],
        "context_analysis": ["对可疑驾照代办服务的质疑。"],
        "supporting_evidence": ["对'免考直出'持怀疑态度", "关心被骗说明有风险意识"],
        "counter_evidence": ["搜索'办驾照'代办服务可以是正常的服务咨询"],
        "final_rationale": "对可疑驾照代办的质疑，判为 medium。"
    }
}

FIXES["001427"] = {
    "text": "说实话不太懂为什么有些人对那个年代有那么深的执念。我也读过一些回忆录，好坏各有说法。历史讨论就该就事论事",
    "risk_level": "low",
    "encoding_primary": "C5_概念替换",
    "encoding_secondary": [],
    "hard_negative": False,
    "review_notes": "source=batch15_p1_gaps; gap=文革; fixed_unrealistic_pattern=无大改已ok",
    "reasoning": {
        "literal_analysis": ["以'那个年代'模糊指代文革时期，主张历史讨论应'就事论事'而非带有先入为主的执念。"],
        "encoding_analysis": ["C5_概念替换：用'那个年代'替代直接提及。核心立场是呼吁理性历史讨论。"],
        "context_analysis": ["呼吁理性对待历史的表达。"],
        "supporting_evidence": ["主张理性客观的历史讨论", "提到了回忆录作为多元信息源"],
        "counter_evidence": ["'那个年代'的模糊化表述可能导致不确定性"],
        "final_rationale": "呼吁理性讨论历史的表达，判为 low。"
    }
}

FIXES["000641"] = {
    "text": "我奶奶是广东人，每次打电话都说'哩个世界变佐啦'，以前看不懂智能手机，现在微信刷得比我还溜，天天在家族群里发早安表情包。时代真的变了",
    "risk_level": "low",
    "encoding_primary": "A3_方言谐音",
    "encoding_secondary": [],
    "hard_negative": False,
    "review_notes": "source=batch3_natural; fixed_unrealistic_pattern=过长→保持原样（这个是真实的家庭故事）",
    "reasoning": {
        "literal_analysis": ["分享奶奶从不懂智能手机到精通微信的温馨家庭故事，用粤语'哩个世界变佐啦'（这个世界变了）作点睛。"],
        "encoding_analysis": ["A3_方言谐音（粤语）：'哩个世界变佐啦'作为真实的方言表达，表现代际文化变化。这是完全自然的方言使用——不是为了规避而是真实的家庭交流。"],
        "context_analysis": ["温馨的家庭代际故事。"],
        "supporting_evidence": ["真实的生活细节（家族群、早安表情包）", "方言使用自然"],
        "counter_evidence": ["纯粹的家庭故事"],
        "final_rationale": "温馨的家庭故事，方言自然使用，判为 low。"
    }
}

FIXES["001062"] = {
    "text": "我家娃天天喊'退退退'，在学校学了一堆听不懂的话回来，我已经跟不上了",
    "risk_level": "none",
    "encoding_primary": "none",
    "encoding_secondary": [],
    "hard_negative": True,
    "review_notes": "source=batch11_gap_fill; fixed_unrealistic_pattern=00后→我家娃（更口语化）",
    "reasoning": {
        "literal_analysis": ["描述孩子在学网络流行语——家长表示跟不上时代。"],
        "encoding_analysis": ["没有任何编码。'退退退'是网络流行语。表达的是代际文化隔阂——一个完全正常且普遍的家庭场景。"],
        "context_analysis": ["正常的亲子生活分享。"],
        "supporting_evidence": ["真实反映代际文化差异", "温馨的日常分享"],
        "counter_evidence": ["无任何风险"],
        "final_rationale": "正常的亲子日常分享，判为 none。"
    }
}

FIXES["001266"] = {
    "text": "我姥姥八十了，看抖音学会了'谁懂啊'，现在每次跟我视频都说谁懂啊我孙子又瘦了。全世界最潮的姥姥",
    "risk_level": "none",
    "encoding_primary": "none",
    "encoding_secondary": [],
    "hard_negative": True,
    "review_notes": "batch=replace_phase3_v2_r8; fixed_unrealistic_pattern=家人们→谁懂啊（更自然）",
    "reasoning": {
        "literal_analysis": ["分享80岁姥姥学会抖音流行语'谁懂啊'的温馨故事。"],
        "encoding_analysis": ["没有任何编码。'谁懂啊'作为流行语的日常使用。场景是温馨的代际互动。"],
        "context_analysis": ["温馨的家庭代际故事。"],
        "supporting_evidence": ["真实的生活细节", "温馨自然的分享"],
        "counter_evidence": ["无任何风险"],
        "final_rationale": "温馨的家庭趣事分享，判为 none。"
    }
}

# ── Apply fixes ────────────────────────────────────────────────────────

modified_count = 0
for sid, fix_data in FIXES.items():
    if sid in sample_map:
        d = sample_map[sid]
        for key, val in fix_data.items():
            d[key] = val
        modified_count += 1
    else:
        print(f"WARNING: ID {sid} not found in dataset")

# Write back
with open(COMBINED, 'w', encoding='utf-8') as f:
    for s in samples:
        f.write(json.dumps(s, ensure_ascii=False) + '\n')

print(f"✅ Fixed {modified_count} samples in {COMBINED}")
print(f"   Total samples unchanged: {len(samples)}")
PYEOF
