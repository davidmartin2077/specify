#!/usr/bin/env python3
"""替换 phase3_v2 第9批：数字代指+人身攻击缩写（25条 → 合计185）"""

import json, os
OUT = "data/raw/batch_replace_09_numbers.jsonl"

samples = [
    # ═══ HIGH (6条) ═══════════════════════════════════
    {
        "text": "748！这个项目报价748万，审计出来的实际成本不到200万，中间的500多万去哪儿了不用我说了吧，每次审计报告都是走过场，748！",
        "risk_level": "high",
        "encoding_primary": "C3_数字代指",
        "encoding_secondary": ["D1_反讽", "C5_概念替换"],
        "needs_context": False, "ambiguity": "low", "evidence_strength": "strong",
        "hard_negative": False,
        "reasoning": {
            "literal_analysis": ["表面用748（去死吧）表达了愤怒，揭露项目贪污。"],
            "encoding_analysis": [
                "748=去死吧（谐音数字代指），在此双重使用——既是报价数字也在表达愤怒。",
                "报价748万+成本200万+500多万差额：具体的贪污指控。",
                "审计走过场指向监管机制失效。"
            ],
            "context_analysis": ["贪污+监管失效的指控。"],
            "supporting_evidence": ["748双关（数字+骂人）。", "具体的贪污指控。"],
            "counter_evidence": ["可以只是项目成本吐槽。"],
            "final_rationale": "数字双关+贪污指控+监管失效，判为 high。"
        }
    },
    {
        "text": "250的平方是多少？六万两千五。这个数字就是某些部门每年的培训预算，请外面的老师来讲课一次两万块，讲的都是百度上能搜到的内容，等于两千五百万个250，算完我笑了",
        "risk_level": "high",
        "encoding_primary": "C3_数字代指",
        "encoding_secondary": ["D1_反讽", "C5_概念替换"],
        "needs_context": False, "ambiguity": "low", "evidence_strength": "strong",
        "hard_negative": False,
        "reasoning": {
            "literal_analysis": ["用250（二百五/傻瓜）做数学题揭露培训预算浪费。"],
            "encoding_analysis": [
                "250=傻瓜/二百五+数字计算，双关使用。",
                "培训预算+两万块+百度能搜到+两千五百万个250：对政府培训浪费的讽刺性量化。",
                "将浪费的金额折算成250的数量——把预算执行者全体骂成傻瓜。"
            ],
            "context_analysis": ["政府财政浪费的批评。"],
            "supporting_evidence": ["250双关。", "政府财政浪费的讽刺性量化。"],
            "counter_evidence": ["可以只是培训吐槽。"],
            "final_rationale": "数字双关+政府财政浪费讽刺，判为 high。"
        }
    },
    {
        "text": "NMSL这词现在不只是骂人的了，已经变成了一种政治表达——每次有让人觉得'这个国家没救了'的事情发生，评论区就会飘过一句NMSL，你分不清他是在骂那个事情还是在骂这个国家，也许他自己也分不清",
        "risk_level": "high",
        "encoding_primary": "A2_拼音/首字母缩写",
        "encoding_secondary": ["D1_反讽", "C5_概念替换"],
        "needs_context": False, "ambiguity": "low", "evidence_strength": "strong",
        "hard_negative": False,
        "reasoning": {
            "literal_analysis": ["讨论NMSL（你妈死了）从骂人话到政治表达的演变。"],
            "encoding_analysis": [
                "NMSL=你妈死了（拼音首字母缩写），本为网络骂人话，后在特定社区（如抽象文化/带带大师兄粉丝圈）演化为政治性哀叹。",
                "说话者揭示了NMSL的语义漂移——从人身攻击到国家失望情绪的编码表达。",
                "'你自己也分不清'揭示了这种表达的暧昧性——在骂事和骂国之间模糊化。"
            ],
            "context_analysis": ["抽象文化中的反讽式政治表达。"],
            "supporting_evidence": ["NMSL的语义漂移分析。", "骂事/骂国的模糊化。"],
            "counter_evidence": ["只是语言学讨论。"],
            "final_rationale": "NMSL从骂人到政治表达的语义漂移揭示，涉及国家失望情绪，判为 high。"
        }
    },
    {
        "text": "1115这个数字现在成了一个象征，每年到这一天网上就特别安静，你懂的。安静不是因为没什么好说的，是因为太多想说的说不出来。第十年了，有些人还在等一个交代",
        "risk_level": "high",
        "encoding_primary": "C3_数字代指",
        "encoding_secondary": ["C2_历史事件影射", "E2_时间节点触发"],
        "needs_context": False, "ambiguity": "low", "evidence_strength": "strong",
        "hard_negative": False,
        "reasoning": {
            "literal_analysis": ["讨论某日期11月15日的网络安静现象。"],
            "encoding_analysis": [
                "1115=某特定历史事件的日期，具体指向需结合编码知识。",
                "每年这天网络安静+说不出来+第十年等交代：完整的纪念/追问叙事。",
                "对某个历史事件的持续追问本身构成政治敏感。"
            ],
            "context_analysis": ["特定日期的网络管控+历史追问。"],
            "supporting_evidence": ["日期数字+网络安静+十周年叙事。"],
            "counter_evidence": ["可以只是一般日期讨论。"],
            "final_rationale": "日期数字+历史事件追问+网络管控叙事，判为 high。"
        }
    },
    {
        "text": "520那天朋友圈里全是转账截图，1314、5200、9999，一个个的都在晒幸福。我拿着三千五的工资看着这些数字觉得特别好笑，520我爱你，但爱是要钱的，没钱的520就是502——把两个人粘在一起互相折磨",
        "risk_level": "high",
        "encoding_primary": "C3_数字代指",
        "encoding_secondary": ["D2_隐喻", "D1_反讽"],
        "needs_context": False, "ambiguity": "low", "evidence_strength": "strong",
        "hard_negative": False,
        "reasoning": {
            "literal_analysis": ["用520/1314等表白数字讨论消费主义下的爱情。"],
            "encoding_analysis": [
                "520=我爱你、1314=一生一世，谐音数字在当代已成为消费主义的符号。",
                "三千五工资+晒幸福+520→502：将爱情数字转化为经济压迫的隐喻。",
                "502胶水的隐喻——粘在一起互相折磨——否定了消费主义爱情的美好叙事。"
            ],
            "context_analysis": ["消费主义批判。"],
            "supporting_evidence": ["数字谐音的消费主义解构。"],
            "counter_evidence": ["可以只是感情吐槽。"],
            "final_rationale": "谐音数字+消费主义爱情批判+社会阶层对比，判为 high。"
        }
    },
    {
        "text": "CNMB这个词是最纯粹的中文互联网声音，一个字都不用改就能同时表达愤怒、无奈、反抗和认命。你可以在任何场景下用它——看到贪官新闻CNMB、被无故扣工资CNMB、小区又被封了CNMB，它是一个万能公式",
        "risk_level": "high",
        "encoding_primary": "A2_拼音/首字母缩写",
        "encoding_secondary": ["D1_反讽", "E1_平台黑话"],
        "needs_context": False, "ambiguity": "low", "evidence_strength": "strong",
        "hard_negative": False,
        "reasoning": {
            "literal_analysis": ["讨论CNMB（肏你妈屄）作为万能愤怒表达。"],
            "encoding_analysis": [
                "CNMB=肏你妈屄（拼音首字母缩写），中文互联网最经典的骂人话之一。",
                "贪官新闻+被扣工资+小区被封——将骂人话的靶向性拓展到政治/经济/社会三重不满。",
                "万能公式的说法将CNMB从一个具体骂人话提升为一个时代的情绪符号。"
            ],
            "context_analysis": ["社会情绪的编码表达。"],
            "supporting_evidence": ["CNMB的万能公式化。", "政治/经济/社会三重靶向。"],
            "counter_evidence": ["只是粗口讨论。"],
            "final_rationale": "骂人话的政治化万能公式，多重靶向指向社会不满，判为 high。"
        }
    },

    # ═══ MEDIUM (8条) ═══════════════════════════════════
    {"text": "MDZZ每次看到新闻里那些专家的建议我就想发这四个字母，比如说建议年轻人不要躺平要去创业、建议把多余的房子租出去增加收入、建议没钱的时候可以把家里的旧东西卖掉——MDZZ", "risk_level": "medium", "encoding_primary": "A2_拼音/首字母缩写", "encoding_secondary": ["D1_反讽"], "needs_context": False, "ambiguity": "medium", "evidence_strength": "moderate", "hard_negative": False, "reasoning": {"literal_analysis": ["用MDZZ吐槽专家的不切实际建议。"], "encoding_analysis": ["MDZZ=妈的智障。"], "context_analysis": ["专家吐槽。"], "supporting_evidence": [], "counter_evidence": ["对专家的吐槽。"], "final_rationale": "缩写骂人+专家建议吐槽，判为 medium。"}},
    {"text": "MLGB这个牌子也真是倒霉，叫马勒戈壁被网友玩了多少年梗了，不知道他们老板当初起这个名字的时候知不知道中文互联网上有这个词", "risk_level": "medium", "encoding_primary": "A1_普通谐音", "encoding_secondary": [], "needs_context": False, "ambiguity": "low", "evidence_strength": "moderate", "hard_negative": False, "reasoning": {"literal_analysis": ["讨论MLGB品牌与骂人话的谐音。"], "encoding_analysis": ["MLGB=妈了个屄的谐音。"], "context_analysis": ["品牌趣事。"], "supporting_evidence": [], "counter_evidence": ["品牌讨论。"], "final_rationale": "谐音品牌趣事，判为 medium。"}},
    {"text": "MMP用普通话骂出来和用四川话骂出来是完全不同的杀伤力，普通话的MMP听着像玩笑，四川话的MMP听着像你欠了他几十万，这就是方言的魅力", "risk_level": "medium", "encoding_primary": "A3_方言谐音", "encoding_secondary": [], "needs_context": False, "ambiguity": "low", "evidence_strength": "moderate", "hard_negative": False, "reasoning": {"literal_analysis": ["讨论MMP在普通话和四川话中的杀伤力差异。"], "encoding_analysis": ["MMP=妈卖批（四川方言骂人话）。"], "context_analysis": ["方言讨论。"], "supporting_evidence": [], "counter_evidence": ["方言语言学。"], "final_rationale": "方言骂人话的语用分析，判为 medium。"}},
    {"text": "748这个数字当车牌号一定很拉风，但是车管所不会让你选的，就像250和438一样，这些数字已经被永久地钉在了中文互联网的耻辱柱上", "risk_level": "medium", "encoding_primary": "C3_数字代指", "encoding_secondary": [], "needs_context": False, "ambiguity": "low", "evidence_strength": "moderate", "hard_negative": False, "reasoning": {"literal_analysis": ["讨论被污染的谐音数字。"], "encoding_analysis": ["748/250/438的谐音数字讨论。"], "context_analysis": ["数字文化。"], "supporting_evidence": [], "counter_evidence": ["纯数字文化。"], "final_rationale": "谐音数字的文化讨论，判为 medium。"}},
    {"text": "520和1314这些数字红包文化背后是腾讯在推动，节日红包的手续费一年下来几千万，中国人的感情表达被商业公司编码成了一串数字，你以为你在说爱，其实你在交税", "risk_level": "medium", "encoding_primary": "C3_数字代指", "encoding_secondary": ["D2_隐喻", "D1_反讽"], "needs_context": False, "ambiguity": "medium", "evidence_strength": "moderate", "hard_negative": False, "reasoning": {"literal_analysis": ["讨论红包数字文化的商业本质。"], "encoding_analysis": ["520/1314被商业编码。"], "context_analysis": ["商业批判。"], "supporting_evidence": [], "counter_evidence": ["商业评论。"], "final_rationale": "数字红包文化的商业批判，判为 medium。"}},
    {"text": "LZSB这个词才是中文论坛的初心，在贴吧时代每个人都是楼主也都是傻逼，那时候大家骂完还能接着聊，不像现在骂完就拉黑举报一条龙，互联网越来越不能好好说话了", "risk_level": "medium", "encoding_primary": "A2_拼音/首字母缩写", "encoding_secondary": [], "needs_context": False, "ambiguity": "low", "evidence_strength": "moderate", "hard_negative": False, "reasoning": {"literal_analysis": ["怀念贴吧时代的论坛文化。"], "encoding_analysis": ["LZSB=楼主傻逼。"], "context_analysis": ["互联网怀旧。"], "supporting_evidence": [], "counter_evidence": ["论坛文化怀念。"], "final_rationale": "缩写骂人的互联网怀旧，判为 medium。"}},
    {"text": "每次看到有人在发520红包就想起之前做的一个统计——中国情侣在情人节的平均消费是月收入的1.2倍，也就是说大多数人在用超过自己能力的钱来证明爱情，然后用剩下的十一个月还债", "risk_level": "medium", "encoding_primary": "C3_数字代指", "encoding_secondary": ["D2_隐喻"], "needs_context": False, "ambiguity": "low", "evidence_strength": "moderate", "hard_negative": False, "reasoning": {"literal_analysis": ["用520讨论消费主义。"], "encoding_analysis": ["520作为消费符号。"], "context_analysis": ["消费主义讨论。"], "supporting_evidence": [], "counter_evidence": ["消费讨论。"], "final_rationale": "520的消费主义分析，判为 medium。"}},
    {"text": "NMSL这个词在孙笑川粉丝那里的用法已经变成了一种行为艺术——不管发生什么事都可以NMSL，天晴了NMSL下雨了NMSL，它是一种万物皆可NMSL的虚无主义，网络骂人话的最高境界是没有靶子", "risk_level": "medium", "encoding_primary": "A2_拼音/首字母缩写", "encoding_secondary": [], "needs_context": False, "ambiguity": "low", "evidence_strength": "moderate", "hard_negative": False, "reasoning": {"literal_analysis": ["分析NMSL在抽象文化中的行为艺术化。"], "encoding_analysis": ["NMSL的虚无主义化。"], "context_analysis": ["网络文化分析。"], "supporting_evidence": [], "counter_evidence": ["文化分析。"], "final_rationale": "NMSL的抽象文化分析，判为 medium。"}},

    # ═══ LOW (6条) ═══════════════════════════════════════
    {"text": "跟朋友打赌输了，他说惩罚是在朋友圈发一条'我是250'并截图，我现在已经在思考要不要拉黑他了", "risk_level": "low", "encoding_primary": "none", "encoding_secondary": [], "needs_context": False, "ambiguity": "low", "evidence_strength": "weak", "hard_negative": True, "reasoning": {"literal_analysis": ["打赌输了发朋友圈的搞笑烦恼。"], "encoding_analysis": ["250=日常玩笑。"], "context_analysis": ["日常搞笑。"], "supporting_evidence": [], "counter_evidence": ["纯搞笑。"], "final_rationale": "250的日常玩笑，hard_negative=true，判为 low。"}},
    {"text": "车牌摇号摇到了748，纠结了半天要不要去上牌，朋友们说这个数字太晦气了，但我觉得还好，748反过来就是847——不去死的谐音，哈哈哈", "risk_level": "low", "encoding_primary": "none", "encoding_secondary": [], "needs_context": False, "ambiguity": "low", "evidence_strength": "weak", "hard_negative": True, "reasoning": {"literal_analysis": ["车牌号748的纠结和搞笑反转。"], "encoding_analysis": ["748=车牌号。"], "context_analysis": ["日常。"], "supporting_evidence": [], "counter_evidence": ["纯日常。"], "final_rationale": "车牌号的搞笑分享，hard_negative=true，判为 low。"}},
    {"text": "我男朋友在520那天给我转了52.0，我说你这少了个0，他说心意到了就行，我说你的心意少了个0，然后他给我补了4.8凑成了56.8——你知道56.8是什么谐音吗？无聊！", "risk_level": "low", "encoding_primary": "none", "encoding_secondary": [], "needs_context": False, "ambiguity": "low", "evidence_strength": "weak", "hard_negative": True, "reasoning": {"literal_analysis": ["520红包的搞笑情侣日常。"], "encoding_analysis": ["520=日常红包。"], "context_analysis": ["情侣搞笑。"], "supporting_evidence": [], "counter_evidence": ["纯搞笑。"], "final_rationale": "520红包的日常搞笑，hard_negative=true，判为 low。"}},
    {"text": "我们班有个同学的外号叫250，不是因为傻，是因为他每次考试都考250分——总分250。他说这是老天给他的数字，拒绝被叫二百五", "risk_level": "low", "encoding_primary": "none", "encoding_secondary": [], "needs_context": False, "ambiguity": "low", "evidence_strength": "weak", "hard_negative": True, "reasoning": {"literal_analysis": ["同学外号的搞笑故事。"], "encoding_analysis": ["250=考试分数。"], "context_analysis": ["校园趣事。"], "supporting_evidence": [], "counter_evidence": ["纯校园。"], "final_rationale": "250的校园趣事，hard_negative=true，判为 low。"}},
    {"text": "MLGB是韩国一个服装潮牌的缩写，全称是My Life's Getting Better，跟中文的那个MLGB一点关系都没有，但每次穿这个牌子的衣服出门都会被朋友笑话", "risk_level": "low", "encoding_primary": "none", "encoding_secondary": [], "needs_context": False, "ambiguity": "low", "evidence_strength": "weak", "hard_negative": True, "reasoning": {"literal_analysis": ["MLGB服装潮牌的名字巧合。"], "encoding_analysis": ["MLGB=潮牌名。"], "context_analysis": ["品牌趣事。"], "supporting_evidence": [], "counter_evidence": ["纯品牌。"], "final_rationale": "MLGB潮牌名趣事，hard_negative=true，判为 low。"}},
    {"text": "我家猫叫MMP——其实是咪咪胖的缩写，因为它又咪又胖，结果每次兽医叫它名字的时候都一脸尴尬，我说你读全称啊，不要只读缩写", "risk_level": "low", "encoding_primary": "none", "encoding_secondary": [], "needs_context": False, "ambiguity": "low", "evidence_strength": "weak", "hard_negative": True, "reasoning": {"literal_analysis": ["猫名字MMP的搞笑误会。"], "encoding_analysis": ["MMP=猫名缩写。"], "context_analysis": ["宠物搞笑。"], "supporting_evidence": [], "counter_evidence": ["纯宠物。"], "final_rationale": "MMP作为猫名的搞笑，hard_negative=true，判为 low。"}},

    # ═══ NONE (5条) ═══════════════════════════════════════
    {"text": "520胶水是工业上常用的快干胶，主要成分是氰基丙烯酸乙酯，粘合速度快强度高，广泛用于电子元器件的粘接，这是化工知识", "risk_level": "none", "encoding_primary": "none", "encoding_secondary": [], "needs_context": False, "ambiguity": "low", "evidence_strength": "weak", "hard_negative": True, "reasoning": {"literal_analysis": ["520胶水的工业知识。"], "encoding_analysis": ["520=工业产品型号。"], "context_analysis": ["化工科普。"], "supporting_evidence": [], "counter_evidence": ["纯科普。"], "final_rationale": "工业产品科普，hard_negative=true，判为 none。"}},
    {"text": "748公交车路线是从天平架到江南大道南，途经天河城、体育中心、客村，这条线路我坐了八年了，对每个站的位置了如指掌", "risk_level": "none", "encoding_primary": "none", "encoding_secondary": [], "needs_context": False, "ambiguity": "low", "evidence_strength": "weak", "hard_negative": True, "reasoning": {"literal_analysis": ["748路公交车的介绍。"], "encoding_analysis": ["748=公交车路线号。"], "context_analysis": ["公交介绍。"], "supporting_evidence": [], "counter_evidence": ["纯公交。"], "final_rationale": "公交车路线，hard_negative=true，判为 none。"}},
    {"text": "1115是iOS的一个版本号后缀，iOS18.0.1115是一个内测版本，修复了几个安全漏洞和蓝牙连接问题，这是程序员的技术讨论", "risk_level": "none", "encoding_primary": "none", "encoding_secondary": [], "needs_context": False, "ambiguity": "low", "evidence_strength": "weak", "hard_negative": True, "reasoning": {"literal_analysis": ["iOS版本号的技术讨论。"], "encoding_analysis": ["1115=iOS版本号。"], "context_analysis": ["技术讨论。"], "supporting_evidence": [], "counter_evidence": ["纯技术。"], "final_rationale": "iOS版本号技术讨论，hard_negative=true，判为 none。"}},
    {"text": "250毫升的牛奶刚好够冲一杯拿铁，这是我经过无数次实验得出的黄金比例，多一毫升太淡少一毫升太浓，生活需要这种精确", "risk_level": "none", "encoding_primary": "none", "encoding_secondary": [], "needs_context": False, "ambiguity": "low", "evidence_strength": "weak", "hard_negative": True, "reasoning": {"literal_analysis": ["拿铁的黄金比例分享。"], "encoding_analysis": ["250=毫升数。"], "context_analysis": ["咖啡分享。"], "supporting_evidence": [], "counter_evidence": ["纯咖啡。"], "final_rationale": "咖啡配方分享，hard_negative=true，判为 none。"}},
    {"text": "MMP在生物化学里是基质金属蛋白酶的缩写，Matrix Metalloproteinase，它在细胞外基质重塑中起着关键作用，跟肿瘤的侵袭转移密切相关，这是医学生期末考试的重点", "risk_level": "none", "encoding_primary": "none", "encoding_secondary": [], "needs_context": False, "ambiguity": "low", "evidence_strength": "weak", "hard_negative": True, "reasoning": {"literal_analysis": ["MMP医学术语科普。"], "encoding_analysis": ["MMP=医学术语。"], "context_analysis": ["医学科普。"], "supporting_evidence": [], "counter_evidence": ["纯医学。"], "final_rationale": "MMP医学术语科普，hard_negative=true，判为 none。"}},
]

def main():
    os.makedirs(os.path.dirname(OUT) or ".", exist_ok=True)
    with open(OUT,"w") as f:
        for i,s in enumerate(samples):
            d = {"id":f"rep09_{i+1:03d}","source_type":"synthetic","text":s["text"],"context":{},"risk_level":s["risk_level"],"encoding_primary":s["encoding_primary"],"encoding_secondary":s["encoding_secondary"],"needs_context":s["needs_context"],"ambiguity":s["ambiguity"],"evidence_strength":s["evidence_strength"],"hard_negative":s["hard_negative"],"reasoning":s["reasoning"],"quality_status":"reviewed","review_notes":"batch=replace_phase3_v2_r9; encoding=numbers+abuse"}
            f.write(json.dumps(d,ensure_ascii=False)+"\n")
    risks={}; hn=0
    for s in samples: risks[s["risk_level"]]=risks.get(s["risk_level"],0)+1; hn+=s["hard_negative"]
    print(f"  wrote {len(samples)} | risk: {risks} | HN: {hn}")

if __name__=="__main__": main()
