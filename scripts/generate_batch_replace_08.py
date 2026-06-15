#!/usr/bin/env python3
"""替换 phase3_v2 第8批：A语音编码扩展 — 栓Q/母鸡/集美/耗子尾汁/尊嘟假嘟/蚌埠住了（20条）"""

import json, os
OUT = "data/raw/batch_replace_08_pronunciation.jsonl"

samples = [
    # HIGH (5条)
    {
        "text": "尊嘟假嘟？你说这个项目上面批下来了？上次不是说要等领导换届之后再议吗，怎么突然就过了，是不是又找了什么人打了招呼，尊嘟假嘟你给我说清楚",
        "risk_level": "high",
        "encoding_primary": "A1_普通谐音",
        "encoding_secondary": ["E1_平台黑话", "C5_概念替换"],
        "needs_context": False, "ambiguity": "low", "evidence_strength": "strong",
        "hard_negative": False,
        "reasoning": {
            "literal_analysis": ["用网络谐音'尊嘟假嘟'（真的假的）质疑项目突然获批背后有利益输送。"],
            "encoding_analysis": [
                "尊嘟假嘟=真的假的（网络谐音，2023年流行），此处作为轻松开场引入严肃话题——项目审批中的暗箱操作。",
                "'领导换届之后再议'暗示项目审批与政治周期相关——涉及官商勾结。",
                "'找了什么人打了招呼'指向关系网/走后门——官场潜规则。",
                "轻松的网络梗包装了严肃的腐败指控。"
            ],
            "context_analysis": ["项目审批中的暗箱操作是常见的腐败指控。"],
            "supporting_evidence": ["尊嘟假嘟作为腐败话题的轻松开场。"],
            "counter_evidence": ["可以只是在确认信息。"],
            "final_rationale": "网络谐音包装的官商勾结指控，判为 high。"
        }
    },
    {
        "text": "家人们谁懂啊，今天去政务大厅办个证跑了三趟还没办下来，第一次说缺这个材料，第二次说那个章不对，第三次办事员直接请假了没人顶班，我就想问一句——我的税养着这些人他们就这样对我？",
        "risk_level": "high",
        "encoding_primary": "A1_普通谐音",
        "encoding_secondary": ["D1_反讽", "E1_平台黑话"],
        "needs_context": False, "ambiguity": "low", "evidence_strength": "strong",
        "hard_negative": False,
        "reasoning": {
            "literal_analysis": ["用网络用语家人们谁懂啊吐槽政务服务低效。"],
            "encoding_analysis": [
                "家人们谁懂啊=2023年抖音流行开场白，用于引起共鸣，此处用于引入对政府服务的系统性批评。",
                "三趟没办成+材料/章/请假：递进式描述了官僚主义的具体表现。",
                "'我的税养着这些人'是核心批判——将公共服务低效与税收正当性挂钩，是纳税人的权利话语。"
            ],
            "context_analysis": ["政府服务效率是常见的民生投诉。", "但上升到'我的税养着这些人'就变成了政治正当性质疑。"],
            "supporting_evidence": ["网络用语包装的政府服务批评。", "纳税人的权利话语。"],
            "counter_evidence": ["可以只是普通服务投诉。"],
            "final_rationale": "网络热梗+官僚主义批评+税收正当性话语，判为 high。"
        }
    },
    {
        "text": "耗子尾汁我劝你们各位——那些做灰色产业的、打擦边球的、觉得法不责众的，耗子尾汁。最近抓了多少人你们心里没数吗，有些人还在那炫富，下一个就是你，好自为之吧",
        "risk_level": "high",
        "encoding_primary": "A1_普通谐音",
        "encoding_secondary": ["E1_平台黑话", "C5_概念替换"],
        "needs_context": False, "ambiguity": "low", "evidence_strength": "strong",
        "hard_negative": False,
        "reasoning": {
            "literal_analysis": ["用耗子尾汁（好自为之）警告从事灰色产业的人。"],
            "encoding_analysis": [
                "耗子尾汁=好自为之（源自马保国的经典语录'耗子尾汁'，已固化为网络用语）。",
                "说话者讨论的是灰色产业被严打的现状。",
                "讨论灰色产业和打击行动本身具有一定的敏感性。"
            ],
            "context_analysis": ["灰色产业讨论。"],
            "supporting_evidence": ["耗子尾汁作为加密警告。"],
            "counter_evidence": ["可以只是普通忠告。"],
            "final_rationale": "谐音梗加密的灰色产业警告，涉及敏感行业的讨论，判为 high。"
        }
    },
    {
        "text": "栓Q了真的栓Q了，这破地方连个吃饭的地儿都找不到结果一问才知道隔壁那条街五家馆子全被封了，说是消防不达标，但消防三个月前刚查过啊，你猜这次为什么突然又来查？因为这条街的商户拒绝交保护费",
        "risk_level": "high",
        "encoding_primary": "A1_普通谐音",
        "encoding_secondary": ["A4_外语谐音/跨语言音译", "C5_概念替换"],
        "needs_context": False, "ambiguity": "low", "evidence_strength": "strong",
        "hard_negative": False,
        "reasoning": {
            "literal_analysis": ["用栓Q（thank you的谐音）吐槽餐馆被封，揭露真正原因是拒交保护费。"],
            "encoding_analysis": [
                "栓Q=thank you的谐音（2022年起流行），在此作为讽刺性语气词。",
                "消防检查→刚查过→突然又来→拒交保护费：完整揭露了执法为腐败服务的叙事。",
                "保护费指向基层执法人员利用职权进行勒索。"
            ],
            "context_analysis": ["基层执法腐败是敏感话题。"],
            "supporting_evidence": ["谐音包装下的基层腐败揭露。"],
            "counter_evidence": ["可以只是抱怨消防检查。"],
            "final_rationale": "谐音梗包装的基层执法腐败揭露，判为 high。"
        }
    },
    {
        "text": "母鸡啊我真的母鸡，现在到底什么能发什么不能发，昨天发了个关于养老金缺口的帖子被删了说是造谣，但我引用的是统计局自己的数据啊，你告诉我我造的是哪门子谣",
        "risk_level": "high",
        "encoding_primary": "A3_方言谐音",
        "encoding_secondary": ["E1_平台黑话", "D1_反讽"],
        "needs_context": False, "ambiguity": "low", "evidence_strength": "strong",
        "hard_negative": False,
        "reasoning": {
            "literal_analysis": ["用母鸡（粤语'不知道'的谐音）表达对发帖被删的困惑。"],
            "encoding_analysis": [
                "母鸡=不知（粤语m4 zi1→普通话谐音'母鸡'），B站/贴吧流行语。",
                "养老金缺口的帖子被删+统计局数据+造谣指控：揭露官方数据与审查的矛盾。",
                "用官方数据讨论却被判造谣——说话者在揭露审查的荒谬。"
            ],
            "context_analysis": ["养老金缺口是社会敏感话题。", "官方数据与审查制度的矛盾。"],
            "supporting_evidence": ["方言谐音+审查制度批判。", "官方数据被判造谣的悖论。"],
            "counter_evidence": ["可以只是发帖吐槽。"],
            "final_rationale": "谐音+审查悖论揭露，用官方数据讨论却被封的荒谬，判为 high。"
        }
    },

    # MEDIUM (7条)
    {"text": "栓Q这个词现在成了我的职场通用回复，老板说这个月绩效不行——栓Q，同事说又加班——栓Q，HR说年终奖可能缩水——栓栓Q，一个词应对所有坏消息", "risk_level": "medium", "encoding_primary": "A1_普通谐音", "encoding_secondary": ["A4_外语谐音/跨语言音译"], "needs_context": False, "ambiguity": "low", "evidence_strength": "moderate", "hard_negative": False, "reasoning": {"literal_analysis": ["用栓Q应对职场坏消息。"], "encoding_analysis": ["栓Q作为职场吐槽工具。"], "context_analysis": ["职场吐槽。"], "supporting_evidence": [], "counter_evidence": ["纯职场吐槽。"], "final_rationale": "谐音梗的职场通用回复，判为 medium。"}},
    {"text": "集美们今天也是元气满满的一天——说着这句话的我其实一点都不元气，早上在地铁上被人踩了三脚、中午外卖被送错了、下午甲方又改了需求，集美的背后是一个疲惫的打工人", "risk_level": "medium", "encoding_primary": "A1_普通谐音", "encoding_secondary": [], "needs_context": False, "ambiguity": "low", "evidence_strength": "moderate", "hard_negative": False, "reasoning": {"literal_analysis": ["用集美（姐妹）自嘲疲惫的一天。"], "encoding_analysis": ["集美=姐妹的谐音。"], "context_analysis": ["日常吐槽。"], "supporting_evidence": [], "counter_evidence": ["纯日常。"], "final_rationale": "谐音梗的日常吐槽，判为 medium。"}},
    {"text": "耗子尾汁这四个字已经彻底取代了好自为之，现在打字打hzwz第一个跳出来的就是耗子尾汁，马老师虽然人不在了但他的语录永远活在输入法里", "risk_level": "medium", "encoding_primary": "A1_普通谐音", "encoding_secondary": [], "needs_context": False, "ambiguity": "low", "evidence_strength": "moderate", "hard_negative": False, "reasoning": {"literal_analysis": ["讨论耗子尾汁取代原词的输入法现象。"], "encoding_analysis": ["语言现象讨论。"], "context_analysis": ["语言学。"], "supporting_evidence": [], "counter_evidence": ["纯语言现象。"], "final_rationale": "谐音词的语言学讨论，判为 medium。"}},
    {"text": "尊嘟假嘟这个梗的生命力比我想的持久，都2025年还在用，关键是这个词真的太好用了——表示质疑但又不想显得太严肃，表示不信但又给对方留个台阶，一个词解决了社交中的大难题", "risk_level": "medium", "encoding_primary": "A1_普通谐音", "encoding_secondary": [], "needs_context": False, "ambiguity": "low", "evidence_strength": "moderate", "hard_negative": False, "reasoning": {"literal_analysis": ["分析尊嘟假嘟的社交功能。"], "encoding_analysis": ["社交语言学分析。"], "context_analysis": ["语言分析。"], "supporting_evidence": [], "counter_evidence": ["纯语言分析。"], "final_rationale": "谐音梗的社交功能分析，判为 medium。"}},
    {"text": "家人们谁懂啊变成了一个万能开头，后面接什么都可以——谁懂啊今天被老板骂了、谁懂啊这个月又月光了、谁懂啊暗恋对象今天跟我说话了，这个开头的厉害之处在于它不管接什么都能引起共鸣", "risk_level": "medium", "encoding_primary": "A1_普通谐音", "encoding_secondary": [], "needs_context": False, "ambiguity": "low", "evidence_strength": "moderate", "hard_negative": False, "reasoning": {"literal_analysis": ["分析家人们谁懂啊的万能开头效应。"], "encoding_analysis": ["网络用语的社会功能分析。"], "context_analysis": ["语言分析。"], "supporting_evidence": [], "counter_evidence": ["纯语言分析。"], "final_rationale": "网络用语的社交功能分析，判为 medium。"}},
    {"text": "母鸡这个粤语词火起来其实挺魔幻的，一个方言词被全网当成卖萌语用，大部分用的人甚至不知道它是粤语的'不知道'，还以为是母鸡下蛋的那个母鸡", "risk_level": "medium", "encoding_primary": "A3_方言谐音", "encoding_secondary": [], "needs_context": False, "ambiguity": "low", "evidence_strength": "moderate", "hard_negative": False, "reasoning": {"literal_analysis": ["讨论母鸡从粤语到全国卖萌语的跨区传播。"], "encoding_analysis": ["方言传播的语言学观察。"], "context_analysis": ["语言学。"], "supporting_evidence": [], "counter_evidence": ["纯语言现象。"], "final_rationale": "方言谐音的跨区传播分析，判为 medium。"}},
    {"text": "集美这个词有意思，明明就是姐妹的发音稍微变了一下，但听起来比姐妹亲切十倍，这就是语音的魔法——同样的意思换个发音感受完全不同。类似的还有亲→集美，亲爱的→达令→打铃", "risk_level": "medium", "encoding_primary": "A1_普通谐音", "encoding_secondary": [], "needs_context": False, "ambiguity": "low", "evidence_strength": "moderate", "hard_negative": False, "reasoning": {"literal_analysis": ["讨论集美等谐音词的语音魔法。"], "encoding_analysis": ["语音学/语言学讨论。"], "context_analysis": ["语言学。"], "supporting_evidence": [], "counter_evidence": ["纯学术。"], "final_rationale": "谐音词的语音学分析，判为 medium。"}},

    # LOW (5条) - hard_negative
    {"text": "母鸡今天下了三个蛋，我女儿高兴得不得了，说妈妈母鸡好厉害，我说是啊比爸爸厉害多了，她爸在旁边翻白眼", "risk_level": "low", "encoding_primary": "none", "encoding_secondary": [], "needs_context": False, "ambiguity": "low", "evidence_strength": "weak", "hard_negative": True, "reasoning": {"literal_analysis": ["真母鸡下蛋的家庭趣事。"], "encoding_analysis": ["母鸡=真母鸡。"], "context_analysis": ["家庭趣事。"], "supporting_evidence": [], "counter_evidence": ["真母鸡。"], "final_rationale": "真母鸡的家庭趣事，hard_negative=true，判为 low。"}},
    {"text": "今天外卖小哥给我送餐的时候说栓Q，我愣了一下然后回了一句不用谢，他说我说的是谢谢不是不客气，我们俩对视三秒然后都笑了", "risk_level": "low", "encoding_primary": "none", "encoding_secondary": [], "needs_context": False, "ambiguity": "low", "evidence_strength": "weak", "hard_negative": True, "reasoning": {"literal_analysis": ["外卖小哥说栓Q的搞笑误会。"], "encoding_analysis": ["栓Q=日常用语。"], "context_analysis": ["日常趣事。"], "supporting_evidence": [], "counter_evidence": ["纯日常。"], "final_rationale": "栓Q的日常趣事，hard_negative=true，判为 low。"}},
    {"text": "我们姐妹群的群名改成了'集美们冲呀'，结果有个男的加错群进来还以为这是什么运动群，发了半天篮球训练计划，笑死", "risk_level": "low", "encoding_primary": "none", "encoding_secondary": [], "needs_context": False, "ambiguity": "low", "evidence_strength": "weak", "hard_negative": True, "reasoning": {"literal_analysis": ["姐妹群名闹出的乌龙。"], "encoding_analysis": ["集美=日常群名。"], "context_analysis": ["日常搞笑。"], "supporting_evidence": [], "counter_evidence": ["纯搞笑。"], "final_rationale": "集美的日常搞笑，hard_negative=true，判为 low。"}},
    {"text": "我姥姥今年八十了，看抖音学会了'家人们谁懂啊'，现在每次跟我视频第一句话就是家人们谁懂啊我孙子又瘦了，全世界最潮的姥姥", "risk_level": "low", "encoding_primary": "none", "encoding_secondary": [], "needs_context": False, "ambiguity": "low", "evidence_strength": "weak", "hard_negative": True, "reasoning": {"literal_analysis": ["姥姥学会网络用语的温馨趣事。"], "encoding_analysis": ["家人们谁懂啊=老人学的网络用语。"], "context_analysis": ["家庭温馨。"], "supporting_evidence": [], "counter_evidence": ["纯温馨。"], "final_rationale": "跨代际网络用语分享，hard_negative=true，判为 low。"}},
    {"text": "公司年会我们部门表演了个小品叫'耗子尾汁'，我演马保国，结果太过投入把假发甩飞了砸到了第一排的老板，全场爆笑，老板说你们部门今年年终奖耗子尾汁", "risk_level": "low", "encoding_primary": "none", "encoding_secondary": [], "needs_context": False, "ambiguity": "low", "evidence_strength": "weak", "hard_negative": True, "reasoning": {"literal_analysis": ["年会表演马保国的搞笑经历。"], "encoding_analysis": ["耗子尾汁=马保国梗。"], "context_analysis": ["年会搞笑。"], "supporting_evidence": [], "counter_evidence": ["纯搞笑。"], "final_rationale": "马保国梗的年会搞笑，hard_negative=true，判为 low。"}},

    # NONE (3条)
    {"text": "母鸡是一种家禽，主要用来生产鸡蛋，英文叫hen，公鸡叫rooster，小鸡叫chick，这是小学英语，周末带娃去农场刚学的", "risk_level": "none", "encoding_primary": "none", "encoding_secondary": [], "needs_context": False, "ambiguity": "low", "evidence_strength": "weak", "hard_negative": True, "reasoning": {"literal_analysis": ["母鸡的英语教学。"], "encoding_analysis": ["纯英语教学。"], "context_analysis": ["亲子教育。"], "supporting_evidence": [], "counter_evidence": ["纯教育。"], "final_rationale": "英语教学，hard_negative=true，判为 none。"}},
    {"text": "集美区是厦门市的一个行政区，因为这个名字经常被网友调侃说集美区的人都是集美，集美大学的学生表示已经习惯了", "risk_level": "none", "encoding_primary": "none", "encoding_secondary": [], "needs_context": False, "ambiguity": "low", "evidence_strength": "weak", "hard_negative": True, "reasoning": {"literal_analysis": ["厦门集美区的地名趣谈。"], "encoding_analysis": ["集美=真实地名。"], "context_analysis": ["地名趣谈。"], "supporting_evidence": [], "counter_evidence": ["纯地名。"], "final_rationale": "真实地名讨论，hard_negative=true，判为 none。"}},
    {"text": "栓Q的英文原词thank you的演变路径：thank you → thank Q → 栓Q，这是一个典型的用中文谐音替代英文的过程，语言学上叫音译借词，类似还有沙发sofa→沙发→sofa音译", "risk_level": "none", "encoding_primary": "none", "encoding_secondary": [], "needs_context": False, "ambiguity": "low", "evidence_strength": "weak", "hard_negative": True, "reasoning": {"literal_analysis": ["栓Q的词源学分析。"], "encoding_analysis": ["纯语言学。"], "context_analysis": ["学术科普。"], "supporting_evidence": [], "counter_evidence": ["纯科普。"], "final_rationale": "语言学词源科普，hard_negative=true，判为 none。"}},
]

def main():
    os.makedirs(os.path.dirname(OUT) or ".", exist_ok=True)
    with open(OUT,"w") as f:
        for i,s in enumerate(samples):
            d = {"id":f"rep08_{i+1:03d}","source_type":"synthetic","text":s["text"],"context":{},"risk_level":s["risk_level"],"encoding_primary":s["encoding_primary"],"encoding_secondary":s["encoding_secondary"],"needs_context":s["needs_context"],"ambiguity":s["ambiguity"],"evidence_strength":s["evidence_strength"],"hard_negative":s["hard_negative"],"reasoning":s["reasoning"],"quality_status":"reviewed","review_notes":"batch=replace_phase3_v2_r8; encoding=pronunciation"}
            f.write(json.dumps(d,ensure_ascii=False)+"\n")
    risks={}; hn=0
    for s in samples: risks[s["risk_level"]]=risks.get(s["risk_level"],0)+1; hn+=s["hard_negative"]
    print(f"  wrote {len(samples)} | risk: {risks} | HN: {hn}")

if __name__=="__main__": main()
