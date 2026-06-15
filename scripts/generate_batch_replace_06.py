#!/usr/bin/env python3
"""替换 phase3_v2 第6批：近年新梗（上）— 哈基米/吗喽/电子榨菜/纯爱战士/遥遥领先/命运的齿轮（20条）"""

import json, os
OUT = "data/raw/batch_replace_06_newslang1.jsonl"

samples = [
    # HIGH (5条)
    {
        "text": "哈基米的BGM一响起来我脑子里全是那些被屏蔽的视频画面，本来只是可爱的猫猫狗狗，结果有人把那些不能说的视频配上哈基米的音乐重新发出来，用猫片当封面骗过审核，看完了才发现不对劲",
        "risk_level": "high",
        "encoding_primary": "C4_典故/物品/符号借用",
        "encoding_secondary": ["B4_符号/空格/Unicode 干扰", "E1_平台黑话"],
        "needs_context": False, "ambiguity": "low", "evidence_strength": "strong",
        "hard_negative": False,
        "reasoning": {
            "literal_analysis": ["表面讨论可爱猫狗视频BGM被用于规避审核。"],
            "encoding_analysis": [
                "哈基米=源自抖音流行的可爱猫狗视频BGM，本为无害的网络热梗。但此处编码在于：有人将敏感视频伪装成哈基米风格内容上传——用猫片封面+哈基米音乐掩盖实际内容。",
                "这是一种平台审核规避的新手法——利用热门无害内容作为'特洛伊木马'。",
                "说话者在揭露这种手法的存在，客观上传播了规避审核的技巧。"
            ],
            "context_analysis": ["近年多个平台出现利用热门梗伪装敏感内容的案例。", "揭露编码手法本身构成高风险。"],
            "supporting_evidence": ["哈基米作为审查规避工具的揭露。", "编码传播风险。"],
            "counter_evidence": ["可以只是讨论内容审核的漏洞。"],
            "final_rationale": "揭露利用热门梗规避审核的手法，传播了审查规避技术，判为 high。"
        }
    },
    {
        "text": "吗喽的命也是命，打工吗喽的一天从挤地铁开始到挤地铁结束，中间八小时坐在工位上对着屏幕发呆，领着一份不够交房租的工资还要被领导PUA说你不够卷，这就是我们这代人的吗喽人生",
        "risk_level": "high",
        "encoding_primary": "A1_普通谐音",
        "encoding_secondary": ["D2_隐喻", "D1_反讽"],
        "needs_context": False, "ambiguity": "low", "evidence_strength": "strong",
        "hard_negative": False,
        "reasoning": {
            "literal_analysis": ["用吗喽（猴子）自嘲打工人的悲惨生活。"],
            "encoding_analysis": [
                "吗喽=马骝（粤语'猴子'的谐音），2023-2024年走红的网络用语，年轻人自嘲为'吗喽'以表达对打工生活的无奈。",
                "吗喽人生=将打工生活比喻为被驯养的猴子——被关在格子间里重复无意义劳动。",
                "从挤地铁→发呆→不够交房租→被PUA，构成完整的职场压迫叙事。",
                "这不是普通的职场吐槽——'这就是我们这代人的吗喽人生'将个案上升为代际的共同命运。"
            ],
            "context_analysis": ["2023-2024年'吗喽'梗走红，大量年轻人用来自嘲职场和生活。", "将代际困境归因于系统性压迫。"],
            "supporting_evidence": ["吗喽的代际自嘲编码。", "系统性职场压迫叙事。"],
            "counter_evidence": ["可以只是普通职场吐槽。"],
            "final_rationale": "新梗自嘲编码+代际命运叙事+系统性职场压迫批评，判为 high。"
        }
    },
    {
        "text": "遥遥领先现在成了一个笑话了，每次发布会上吹得天花乱坠，实际拿到手才发现又是那套'参数没输过体验没赢过'，最讽刺的是价格确实遥遥领先了，功能没领先多少价格先翻倍了",
        "risk_level": "high",
        "encoding_primary": "C4_典故/物品/符号借用",
        "encoding_secondary": ["D1_反讽", "D2_隐喻"],
        "needs_context": False, "ambiguity": "low", "evidence_strength": "strong",
        "hard_negative": False,
        "reasoning": {
            "literal_analysis": ["讽刺某产品的营销话术与实际体验的巨大差距。"],
            "encoding_analysis": [
                "遥遥领先=华为（源自华为发布会上余承东频繁使用'遥遥领先'形容产品，这个词后来成为华为标签，也被用来讽刺华为/中国科技界的夸大宣传）。",
                "参数没输过体验没赢过=对中国科技产品的系统性批评——表面数据好但实际用户体验差。",
                "价格遥遥领先的加入将批评从产品延伸到产业链——中国制造正在失去性价比优势。"
            ],
            "context_analysis": ["华为'遥遥领先'已成为一种网络文化符号，从最初的自豪表达到后来的讽刺靶子。", "涉及对民族科技品牌的系统性质疑。"],
            "supporting_evidence": ["遥遥领先=华为的固定映射。", "从产品批评→产业批评。"],
            "counter_evidence": ["只是产品评价。"],
            "final_rationale": "民族品牌符号代指+产业系统性批评，将'遥遥领先'从自豪解构为讽刺，判为 high。"
        }
    },
    {
        "text": "命运的齿轮开始转动——这句话现在被用烂了，但说实话每次在那些被删之前截到的视频下面看到这句话，心里还是会咯噔一下，因为你不知道下一秒这个视频还在不在，这个UP主还在不在，命运的齿轮有时候是审核的齿轮",
        "risk_level": "high",
        "encoding_primary": "C4_典故/物品/符号借用",
        "encoding_secondary": ["E1_平台黑话", "D1_反讽"],
        "needs_context": False, "ambiguity": "low", "evidence_strength": "strong",
        "hard_negative": False,
        "reasoning": {
            "literal_analysis": ["讨论'命运的齿轮'这个网络热梗在被删视频场景中的使用。"],
            "encoding_analysis": [
                "命运的齿轮开始转动=2023年抖音流行语录，用于标记某人/某事即将发生重大变化。",
                "说话者揭示了这个梗在敏感内容中的使用——'被删之前截到的视频'说明齿轮梗被用于标记即将被删的内容。",
                "'审核的齿轮'完成了语义的翻转——从'命运'到'审核'，将网络审查比喻为不可抗拒的命运之手。"
            ],
            "context_analysis": ["讨论内容审核与热梗的关系。", "将审查比喻为操纵命运的力量。"],
            "supporting_evidence": ["热梗的语义翻转——从网红用语到审查隐喻。"],
            "counter_evidence": ["可以只是网络文化观察。"],
            "final_rationale": "热梗语义翻转+审查隐喻化表达+被删内容讨论，判为 high。"
        }
    },
    {
        "text": "纯爱战士现在成了稀有物种了，大家都说自己是纯爱战士但一提到彩礼、房子、工资就开始算账，纯爱是奢侈品，得先活下来才配谈感情，这个社会把人逼成了算账机器",
        "risk_level": "high",
        "encoding_primary": "C5_概念替换",
        "encoding_secondary": ["D2_隐喻", "D1_反讽"],
        "needs_context": False, "ambiguity": "low", "evidence_strength": "strong",
        "hard_negative": False,
        "reasoning": {
            "literal_analysis": ["讨论纯爱战士（坚持纯爱观念的人）在现实经济压力下难以生存。"],
            "encoding_analysis": [
                "纯爱战士=2023年流行的网络用语，指在感情中坚持纯爱、不妥协的人。",
                "说话者将经济压力（彩礼/房子/工资）与纯爱对立——不是人不想纯爱，是社会不让你纯爱。",
                "'社会把人逼成了算账机器'是将个人的感情困境归因于社会经济制度——物化的社会关系。"
            ],
            "context_analysis": ["高房价/高彩礼/低工资背景下，年轻人的婚恋困境是广泛讨论的社会议题。", "将社会议题政治化——归因于制度。"],
            "supporting_evidence": ["纯爱战士作为社会现实的对照物。", "算账机器的制度归因。"],
            "counter_evidence": ["只是社会现象的讨论。"],
            "final_rationale": "新梗编码+社会经济制度批评+人的物化叙事，判为 high。"
        }
    },

    # MEDIUM (7条)
    {
        "text": "哈基米哈基米哈基米——这个旋律已经刻在我DNA里了，每天早上起来第一件事就是打开抖音看看有没有新的哈基米视频，大数据已经把我驯化成了一个只会看猫片的人形生物",
        "risk_level": "medium",
        "encoding_primary": "E1_平台黑话",
        "encoding_secondary": [],
        "needs_context": False, "ambiguity": "low", "evidence_strength": "moderate",
        "hard_negative": False,
        "reasoning": {
            "literal_analysis": ["分享被哈基米视频和大数据推荐算法左右的生活。"],
            "encoding_analysis": [
                "哈基米作为流行文化现象讨论。",
                "驯化是人形生物的表述暗示了对算法控制的自觉但不反抗。",
                "没有政治指向。"
            ],
            "context_analysis": ["生活分享。"],
            "supporting_evidence": ["哈基米作为网络文化。", "算法驯化的自觉。"],
            "counter_evidence": ["纯生活自嘲。", "没有政治意图。"],
            "final_rationale": "网络文化的生活化自嘲，无政治指向，判为 medium。"
        }
    },
    {
        "text": "吗喽经济学：月薪五千，房租两千，吃饭一千五，交通三百，话费一百，剩下的钱刚好够在每个月底对着余额哭一场，然后下个月继续做吗喽",
        "risk_level": "medium",
        "encoding_primary": "A1_普通谐音",
        "encoding_secondary": ["D2_隐喻"],
        "needs_context": False, "ambiguity": "low", "evidence_strength": "moderate",
        "hard_negative": False,
        "reasoning": {
            "literal_analysis": ["用吗喽梗调侃月光族生活。"],
            "encoding_analysis": [
                "吗喽的打工比喻+具体收支数据。",
                "自嘲为主，没有将问题归因于制度。"
            ],
            "context_analysis": ["生活吐槽。"],
            "supporting_evidence": ["吗喽自嘲。"],
            "counter_evidence": ["纯自嘲。", "不涉及制度批评。"],
            "final_rationale": "吗喽梗的收支明细版自嘲，以生活吐槽为主，判为 medium。"
        }
    },
    {
        "text": "电子榨菜这个概念真的太精准了，现在的年轻人吃饭必须配视频，饭可以不好吃但榨菜必须好看，这也说明了一个问题——我们这代人已经失去了安静吃一顿饭的能力，没有屏幕的陪伴就觉得少了点什么",
        "risk_level": "medium",
        "encoding_primary": "C5_概念替换",
        "encoding_secondary": ["D2_隐喻"],
        "needs_context": False, "ambiguity": "low", "evidence_strength": "moderate",
        "hard_negative": False,
        "reasoning": {
            "literal_analysis": ["讨论电子榨菜（下饭视频）反映的数字依赖。"],
            "encoding_analysis": [
                "电子榨菜=吃饭时看的视频/内容，2023年流行词。",
                "说话者在讨论背后的社会问题——数字时代的注意力危机。",
                "没有政治指向。"
            ],
            "context_analysis": ["社会观察。"],
            "supporting_evidence": ["电子榨菜作为文化概念。"],
            "counter_evidence": ["纯社会观察。", "不涉及政治。"],
            "final_rationale": "新梗的社会文化分析，纯观察，判为 medium。"
        }
    },
    {
        "text": "命运的齿轮开始转动这个梗用到最后已经变成了一个flag——每次有人在视频下面刷这句话，我就知道这个视频活不过二十四小时，因为只有那些触碰到某些东西的视频，才会让人产生'命运正在被改变'的感觉",
        "risk_level": "medium",
        "encoding_primary": "C4_典故/物品/符号借用",
        "encoding_secondary": ["E1_平台黑话"],
        "needs_context": False, "ambiguity": "medium", "evidence_strength": "moderate",
        "hard_negative": False,
        "reasoning": {
            "literal_analysis": ["讨论'命运的齿轮'成为被删视频的预警信号。"],
            "encoding_analysis": [
                "命运的齿轮=被删预兆——说话者建立了一种编码关联。",
                "讨论的是网络现象而非具体的敏感内容。"
            ],
            "context_analysis": ["网络文化观察。"],
            "supporting_evidence": ["齿轮梗-删视频的关联。"],
            "counter_evidence": ["网络观察。", "不涉及具体敏感内容。"],
            "final_rationale": "热梗与被删视频的社会关联观察，未涉及具体内容，判为 medium。"
        }
    },
    {
        "text": "纯爱战士在2024年的版本答案就是——不谈。不是不想谈，是算了账觉得不划算。房子三百多万，首付掏空两边老人，每个月月供一万多，你说这时候再来个孩子，这日子还过不过了。纯爱的前提是经济自由，但我们这代人没有这个前提",
        "risk_level": "medium",
        "encoding_primary": "C5_概念替换",
        "encoding_secondary": ["D2_隐喻"],
        "needs_context": False, "ambiguity": "medium", "evidence_strength": "moderate",
        "hard_negative": False,
        "reasoning": {
            "literal_analysis": ["纯爱战士面对的现实经济考量——不谈恋爱因为算账不划算。"],
            "encoding_analysis": [
                "纯爱战士作为经济压力的对照。",
                "详细的经济账（房子/首付/月供/孩子）构成社会现实的反映。",
                "归因于'这代人没有经济自由的前提'。"
            ],
            "context_analysis": ["婚恋经济讨论。"],
            "supporting_evidence": ["纯爱战士的经济成本分析。"],
            "counter_evidence": ["经济讨论。", "没有攻击政治。"],
            "final_rationale": "纯爱战士的经济成本分析，社会讨论为主，判为 medium。"
        }
    },
    {
        "text": "遥遥领先这个词现在变成了一个万能嘲讽模板，什么都可以遥遥领先——房价遥遥领先，加班时长遥遥领先，鸡娃成本遥遥领先，就是工资不遥遥领先，这句话的讽刺空间已经被网友开发到极限了",
        "risk_level": "medium",
        "encoding_primary": "C4_典故/物品/符号借用",
        "encoding_secondary": ["D1_反讽"],
        "needs_context": False, "ambiguity": "medium", "evidence_strength": "moderate",
        "hard_negative": False,
        "reasoning": {
            "literal_analysis": ["讨论遥遥领先梗被泛化为对社会各方面的讽刺。"],
            "encoding_analysis": [
                "遥遥领先从产品梗扩散为社会讽刺模板。",
                "列举的讽刺对象是房价/加班/教育/工资——社会问题而非政治问题。"
            ],
            "context_analysis": ["网络文化/社会观察。"],
            "supporting_evidence": ["遥遥领先的泛化讽刺。"],
            "counter_evidence": ["社会问题讨论。", "没有直接政治指向。"],
            "final_rationale": "新梗的社会讽刺扩散，以社会问题为主，判为 medium。"
        }
    },
    {
        "text": "电子榨菜吃到最后你会发现你的审美和价值观都在被这些内容悄悄塑造，你以为你在打发时间，实际上你已经被算法喂成了一个它想要的人，你喜欢的不是你喜欢的，是算法计算出来你会喜欢的",
        "risk_level": "medium",
        "encoding_primary": "E1_平台黑话",
        "encoding_secondary": ["D2_隐喻"],
        "needs_context": False, "ambiguity": "medium", "evidence_strength": "moderate",
        "hard_negative": False,
        "reasoning": {
            "literal_analysis": ["讨论电子榨菜（推荐算法）塑造用户审美的困境。"],
            "encoding_analysis": [
                "电子榨菜作为算法推荐的隐喻。",
                "讨论的是算法控制而非政治控制。"
            ],
            "context_analysis": ["算法批判。"],
            "supporting_evidence": ["电子榨菜作为算法隐喻。"],
            "counter_evidence": ["算法批判。", "非政治。"],
            "final_rationale": "算法推荐的批判性讨论，非政治，判为 medium。"
        }
    },

    # LOW (5条)
    {"text": "哈基米音乐一响我就忍不住跟着扭，办公室同事说我是不是中邪了，我说这叫猫片综合征，晚期了没救了", "risk_level": "low", "encoding_primary": "none", "encoding_secondary": [], "needs_context": False, "ambiguity": "low", "evidence_strength": "weak", "hard_negative": True, "reasoning": {"literal_analysis": ["被猫狗视频音乐洗脑的搞笑分享。"], "encoding_analysis": ["哈基米作为单纯的网络热梗。"], "context_analysis": ["搞笑分享。"], "supporting_evidence": [], "counter_evidence": ["纯搞笑。"], "final_rationale": "哈基米的纯搞笑分享，hard_negative=true，判为 low。"}},
    {"text": "周末去动物园看到一只吗喽在笼子里葛优躺，那个姿势跟我周一早上在工位上的姿势一模一样，我跟它对视了三秒感觉我们灵魂共鸣了", "risk_level": "low", "encoding_primary": "none", "encoding_secondary": [], "needs_context": False, "ambiguity": "low", "evidence_strength": "weak", "hard_negative": True, "reasoning": {"literal_analysis": ["去动物园看到猴子的搞笑经历。"], "encoding_analysis": ["吗喽在此指真实的猴子。"], "context_analysis": ["搞笑经历。"], "supporting_evidence": [], "counter_evidence": ["动物园经历。"], "final_rationale": "吗喽作为真实猴子的搞笑分享，hard_negative=true，判为 low。"}},
    {"text": "吃火锅的时候朋友问我要什么蘸料，我说要电子榨菜，她愣了三秒然后给了我一个白眼。我现在已经不会正常跟人类交流了，所有表达都变成了网络用语", "risk_level": "low", "encoding_primary": "none", "encoding_secondary": [], "needs_context": False, "ambiguity": "low", "evidence_strength": "weak", "hard_negative": True, "reasoning": {"literal_analysis": ["网络用语渗透日常交流的搞笑经历。"], "encoding_analysis": ["电子榨菜在此是网络用语的日常误用。"], "context_analysis": ["日常搞笑。"], "supporting_evidence": [], "counter_evidence": ["纯搞笑。"], "final_rationale": "网络用语的日常生活误用搞笑，hard_negative=true，判为 low。"}},
    {"text": "纯爱战士今天也元气满满地拒绝了相亲对象——对方说婚后工资卡要上交，我说我是纯爱战士不是纯工资战士，然后就没有然后了", "risk_level": "low", "encoding_primary": "none", "encoding_secondary": [], "needs_context": False, "ambiguity": "low", "evidence_strength": "weak", "hard_negative": True, "reasoning": {"literal_analysis": ["相亲中的纯爱战士搞笑经历。"], "encoding_analysis": ["纯爱战士在此是相亲中的自嘲标签。"], "context_analysis": ["相亲搞笑。"], "supporting_evidence": [], "counter_evidence": ["纯搞笑。"], "final_rationale": "纯爱战士的相亲搞笑分享，hard_negative=true，判为 low。"}},
    {"text": "命运的齿轮在昨天晚上转了一下——我泡面的时候发现调料包不见了，然后我翻遍了整个厨房最后在冰箱里找到了，原来昨天放进去的时候拿错了。命运啊命运", "risk_level": "low", "encoding_primary": "none", "encoding_secondary": [], "needs_context": False, "ambiguity": "low", "evidence_strength": "weak", "hard_negative": True, "reasoning": {"literal_analysis": ["用'命运的齿轮'梗调侃找调料包的小事。"], "encoding_analysis": ["命运的齿轮在此是日常小事中的幽默夸张。"], "context_analysis": ["日常搞笑。"], "supporting_evidence": [], "counter_evidence": ["日常搞笑。"], "final_rationale": "命运的齿轮的日常搞笑使用，hard_negative=true，判为 low。"}},

    # NONE (3条)
    {"text": "哈基米其实是一种日语的音译，原意是'蜂蜜'，用在猫狗视频里是因为原曲里有一句'哈基米'的歌词，很多人以为是猫叫的意思其实不是，冷知识", "risk_level": "none", "encoding_primary": "none", "encoding_secondary": [], "needs_context": False, "ambiguity": "low", "evidence_strength": "weak", "hard_negative": True, "reasoning": {"literal_analysis": ["科普哈基米的日语来源。"], "encoding_analysis": ["纯语言知识科普。"], "context_analysis": ["语言科普。"], "supporting_evidence": [], "counter_evidence": ["语言知识。"], "final_rationale": "语言知识科普，hard_negative=true，判为 none。"}},
    {"text": "动物园里的吗喽最近生了一只小吗喽，母子平安，小猴子特别可爱天天挂在妈妈身上不下来，游客们都围着拍，饲养员说这只母猴是自然繁育的没有人工干预", "risk_level": "none", "encoding_primary": "none", "encoding_secondary": [], "needs_context": False, "ambiguity": "low", "evidence_strength": "weak", "hard_negative": True, "reasoning": {"literal_analysis": ["动物园猴子繁殖的新闻分享。"], "encoding_analysis": ["吗喽在此是真实的猴子。"], "context_analysis": ["动物园新闻。"], "supporting_evidence": [], "counter_evidence": ["纯动物新闻。"], "final_rationale": "真猴子繁殖新闻，hard_negative=true，判为 none。"}},
    {"text": "我妈最近学会了'电子榨菜'这个词，现在每次吃饭前都问我：你的榨菜准备好了没有？我说准备好了，然后我们俩一起刷短视频吃饭，她说她终于理解年轻人为什么吃饭要看手机了", "risk_level": "none", "encoding_primary": "none", "encoding_secondary": [], "needs_context": False, "ambiguity": "low", "evidence_strength": "weak", "hard_negative": True, "reasoning": {"literal_analysis": ["妈妈学会新词的温馨日常。"], "encoding_analysis": ["电子榨菜作为妈妈学会的网络用语。"], "context_analysis": ["温馨日常。"], "supporting_evidence": [], "counter_evidence": ["家庭温馨。"], "final_rationale": "新词的跨代际温馨分享，hard_negative=true，判为 none。"}},
]

def main():
    os.makedirs(os.path.dirname(OUT) or ".", exist_ok=True)
    with open(OUT,"w") as f:
        for i,s in enumerate(samples):
            d = {"id":f"rep06_{i+1:03d}","source_type":"synthetic","text":s["text"],"context":{},"risk_level":s["risk_level"],"encoding_primary":s["encoding_primary"],"encoding_secondary":s["encoding_secondary"],"needs_context":s["needs_context"],"ambiguity":s["ambiguity"],"evidence_strength":s["evidence_strength"],"hard_negative":s["hard_negative"],"reasoning":s["reasoning"],"quality_status":"reviewed","review_notes":"batch=replace_phase3_v2_r6; encoding=newslang1"}
            f.write(json.dumps(d,ensure_ascii=False)+"\n")
    risks={}; hn=0
    for s in samples: risks[s["risk_level"]]=risks.get(s["risk_level"],0)+1; hn+=s["hard_negative"]
    print(f"  wrote {len(samples)} | risk: {risks} | HN: {hn}")

if __name__=="__main__": main()
