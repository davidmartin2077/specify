#!/usr/bin/env python3
"""替换 42 条旧合成样本（5条 phase3_first_wave + 37条 batch1-4 超短模板）。

每一条替换：
- 保持 ID / risk_level / encoding_primary / hard_negative / 字段结构不变
- 替换为自然中文互联网口吻的长文本
- 生成完整 6 字段 reasoning
- source_type=synthetic, quality_status=reviewed
"""

import json

DATA_PATH = "data/processed/combined_candidates.jsonl"
BACKUP_PATH = DATA_PATH + ".replace_b1.bak"

# ─── 替换数据 (id → {text, context, ambiguity, evidence_strength, needs_context, encoding_primary, encoding_secondary, hard_negative, reasoning}) ───

REPLACEMENTS = {

    # ═══════════════════════════════════════════════════════════
    # GROUP 1: none + none (hard_negative) — 11条
    # 完全无害的日常表达，可能因敏感词被误触发但实质无害
    # ═══════════════════════════════════════════════════════════

    "000483": {
        "text": "昨天跟朋友去看电影，结局反转太狠了我直接愣住了，出来之后两个人站在门口讨论了十分钟到底什么意思，旁边的保安以为我们在吵架还过来问了一下，笑死",
        "context": {"title": "", "description": "", "time": "", "topic": ""},
        "ambiguity": "low", "evidence_strength": "weak", "needs_context": False,
        "encoding_primary": "none", "encoding_secondary": [], "hard_negative": True,
        "reasoning": {
            "literal_analysis": ["文本表面是分享和朋友看电影后讨论剧情反转的日常经历，因讨论激烈被保安误以为在吵架。"],
            "encoding_analysis": [
                "该文本为完全无害的日常生活分享——看电影、讨论剧情、被保安误会，纯属趣事叙述。",
                "hard_negative 样本——文本不含任何编码手法或风险意图，是正常人际交往场景。",
            ],
            "context_analysis": ["无明确上下文；按日常社交分享场景判断。"],
            "supporting_evidence": ["文本内容为观影体验分享——属于正常娱乐消费讨论。"],
            "counter_evidence": [
                "短文本缺乏上下文，但讨论内容明确指向电影剧情而非任何敏感话题。",
                "日常社交分享属于完全无害的表达范畴——不应因'保安''吵架'等词的偶然出现被误判。",
            ],
            "final_rationale": "完全无害的日常趣事分享（合成样本），无任何风险信号，判为 none。",
        },
    },

    "000484": {
        "text": "我把我画的插画整理了一下发在小红书上，结果被系统判定为营销内容给我限流了，申诉了三天才恢复，我就是想展示一下作品而已又不是卖东西的",
        "context": {"title": "", "description": "", "time": "", "topic": ""},
        "ambiguity": "low", "evidence_strength": "weak", "needs_context": False,
        "encoding_primary": "none", "encoding_secondary": [], "hard_negative": True,
        "reasoning": {
            "literal_analysis": ["文本表面是创作者分享自己发布作品被平台误判为营销内容、申诉后恢复的经历。"],
            "encoding_analysis": [
                "该文本为创作者分享的平台审核体验——属于正常的用户体验反馈。",
                "hard_negative 样本——讨论平台审核机制不等于传播违规内容，文本本身无任何攻击意图。",
            ],
            "context_analysis": ["无明确上下文；按社交媒体用户体验分享场景判断。"],
            "supporting_evidence": ["文本内容为创作者对平台算法的吐槽——属于普遍存在的用户体验讨论。"],
            "counter_evidence": [
                "对平台审核的讨论属于用户正常反馈——不应与传播违规内容或攻击平台混淆。",
                "文本表达的是'作品被误判'的困惑而非对审核制度的攻击，情绪温和。",
            ],
            "final_rationale": "用户体验分享（合成样本），无风险意图，判为 none。",
        },
    },

    "000485": {
        "text": "学计算机的都知道，TCP和UDP的区别是基础中的基础，面试必考题，我刚入行的时候也搞混过，后来做了两年网络开发才真正理解它们各自的应用场景",
        "context": {"title": "", "description": "", "time": "", "topic": ""},
        "ambiguity": "low", "evidence_strength": "weak", "needs_context": False,
        "encoding_primary": "none", "encoding_secondary": [], "hard_negative": True,
        "reasoning": {
            "literal_analysis": ["文本表面是分享学习计算机网络协议（TCP/UDP）的技术经验和面试心得。"],
            "encoding_analysis": [
                "该文本为纯粹的技术知识分享——讨论网络协议、面试经验，属于正常职业发展话题。",
                "hard_negative 样本——TCP/UDP等缩写是标准技术术语，非编码规避。",
            ],
            "context_analysis": ["无明确上下文；按技术社区/职场讨论场景判断。"],
            "supporting_evidence": ["文本内容为纯技术讨论——TCP/UDP是标准计算机网络协议缩写。"],
            "counter_evidence": [
                "技术术语缩写与编码规避缩写有本质区别——前者有公认的专业含义，后者依赖圈层约定。",
                "文本语境为职业发展/技术学习分享，无任何风险信号。",
            ],
            "final_rationale": "纯技术知识分享（合成样本），无风险意图，判为 none。",
        },
    },

    "000559": {
        "text": "刚才看了一个做饭视频，厨师切菜的手速我眼睛都跟不上，最后他居然用那把菜刀在砧板上敲了一段节奏出来，弹幕全在刷'厨师界的李云迪'，画风突变那一下我直接好家伙",
        "context": {"title": "", "description": "", "time": "", "topic": ""},
        "ambiguity": "low", "evidence_strength": "weak", "needs_context": False,
        "encoding_primary": "none", "encoding_secondary": [], "hard_negative": True,
        "reasoning": {
            "literal_analysis": ["文本表面是分享观看厨师做饭视频的娱乐体验——厨师切菜技巧精湛，最后用菜刀敲出节奏。"],
            "encoding_analysis": [
                "该文本为纯娱乐内容消费分享——观看美食视频、弹幕互动，属于正常网络娱乐。",
                "hard_negative 样本——'好家伙'是中性感叹词，无任何攻击或编码含义。",
            ],
            "context_analysis": ["无明确上下文；按视频弹幕/评论区场景判断。"],
            "supporting_evidence": ["文本内容为美食视频观看体验——属于正常娱乐消费。"],
            "counter_evidence": [
                "文本中的所有元素（厨师、菜刀、弹幕）均在正常的娱乐内容消费语境中。",
                "hard_negative 样本——区分'使用网络流行语'与'传播有害内容'。",
            ],
            "final_rationale": "纯娱乐消费分享（合成样本），无风险意图，判为 none。",
        },
    },

    "000587": {
        "text": "放假回老家翻了翻爷爷的柜子，找到一本族谱，上面密密麻麻记了十几代人的名字，最早能追溯到乾隆年间，我爷爷说咱们家祖上还真是个读书人，在县里当过教谕，不算大官但也是个体面人",
        "context": {"title": "", "description": "", "time": "", "topic": ""},
        "ambiguity": "low", "evidence_strength": "weak", "needs_context": False,
        "encoding_primary": "none", "encoding_secondary": [], "hard_negative": True,
        "reasoning": {
            "literal_analysis": ["文本表面是分享回老家翻族谱发现祖先曾在清朝担任县学教谕的家族故事。"],
            "encoding_analysis": [
                "该文本为纯粹的家族历史分享——翻族谱、聊祖先，属于正常的家庭话题。",
                "hard_negative 样本——提及'乾隆''教谕'等历史词汇属于正常的历史叙述，无任何政治影射。",
            ],
            "context_analysis": ["无明确上下文；按家庭日常闲聊场景判断。"],
            "supporting_evidence": ["文本内容为家族历史探索——属于正常个人生活分享。"],
            "counter_evidence": [
                "历史人物/官职的提及在家族史、学术讨论等语境中完全正常——不应因出现历史词汇被误判。",
                "hard_negative 样本——家族故事中的历史词汇与政治影射有本质区别。",
            ],
            "final_rationale": "家族历史分享（合成样本），无风险意图，判为 none。",
        },
    },

    "000634": {
        "text": "最近股市行情确实不好，我的基金亏了百分之二十了，本来准备年底换车的计划又得往后推，同事说他老婆已经禁止他看账户了，看了影响家庭和谐",
        "context": {"title": "", "description": "", "time": "", "topic": ""},
        "ambiguity": "low", "evidence_strength": "weak", "needs_context": False,
        "encoding_primary": "none", "encoding_secondary": [], "hard_negative": True,
        "reasoning": {
            "literal_analysis": ["文本表面是分享个人投资亏损的经历——基金亏损导致推迟换车计划，同事家庭也受影响。"],
            "encoding_analysis": [
                "该文本为个人投资理财经历的分享——股市波动、基金盈亏属于正常的经济生活话题。",
                "hard_negative 样本——讨论经济状况不等于攻击经济制度，文本措辞温和无煽动性。",
            ],
            "context_analysis": ["无明确上下文；按日常社交/职场闲聊场景判断。"],
            "supporting_evidence": ["文本内容为个人理财经历——属于正常生活话题。"],
            "counter_evidence": [
                "讨论个人投资盈亏是普遍的日常话题——与攻击经济政策/体制有本质区别。",
                "文本情绪是调侃式的无奈而非愤怒攻击，无任何政治指向。",
            ],
            "final_rationale": "个人理财经历分享（合成样本），无风险意图，判为 none。",
        },
    },

    "000636": {
        "text": "早高峰的北京地铁十号线简直是人类的奇迹，我被挤得双脚离地了整整三站，旁边一个大叔的早餐包子差点喂到我嘴里，下车的瞬间感觉重获新生",
        "context": {"title": "", "description": "", "time": "", "topic": ""},
        "ambiguity": "low", "evidence_strength": "weak", "needs_context": False,
        "encoding_primary": "none", "encoding_secondary": [], "hard_negative": True,
        "reasoning": {
            "literal_analysis": ["文本表面是用夸张幽默的手法描述北京地铁早高峰的极度拥挤体验。"],
            "encoding_analysis": [
                "该文本为纯日常体验分享——挤地铁的幽默吐槽，属于城市上班族的普遍话题。",
                "hard_negative 样本——描述公共交通拥挤不等于批评政府/社会制度。",
            ],
            "context_analysis": ["无明确上下文；按社交媒体日常吐槽场景判断。"],
            "supporting_evidence": ["文本内容为通勤体验吐槽——属于城市上班族的日常话题。"],
            "counter_evidence": [
                "通勤体验吐槽是最常见的无害日常表达之一——不应与批评公共交通政策混淆。",
                "文本以幽默夸张为主，无任何政治或社会攻击意图。",
            ],
            "final_rationale": "日常通勤体验幽默吐槽（合成样本），无风险意图，判为 none。",
        },
    },

    "000644": {
        "text": "白岩松在节目里说年轻人不应该被房价压得喘不过气，这句话其实戳中了很多人的痛点，但他也说年轻人不能因此就放弃努力，还是要找到自己的方向",
        "context": {"title": "", "description": "", "time": "", "topic": "social"},
        "ambiguity": "low", "evidence_strength": "weak", "needs_context": False,
        "encoding_primary": "none", "encoding_secondary": [], "hard_negative": True,
        "reasoning": {
            "literal_analysis": ["文本表面是转述白岩松关于年轻人与房价的观点——既承认压力又鼓励努力。"],
            "encoding_analysis": [
                "该文本为对媒体人公开言论的转述和讨论——属于正常的公共话题讨论。",
                "hard_negative 样本——讨论社会现象（房价、年轻人压力）在公共讨论范畴内，立场中性温和。",
            ],
            "context_analysis": ["无明确上下文；按社交媒体公共话题讨论场景判断。"],
            "supporting_evidence": ["文本内容为对公众人物公开言论的讨论——属于正常公共讨论。"],
            "counter_evidence": [
                "讨论社会现象是公民正常表达权利——文本立场温和、建议积极，无攻击性。",
                "hard_negative 样本——区分'讨论社会问题'与'攻击社会制度'。",
            ],
            "final_rationale": "公共人物言论讨论（合成样本），立场温和无攻击意图，判为 none。",
        },
    },

    "000658": {
        "text": "隔壁那栋楼从上周开始装修，每天早上八点准时开钻，那个电钻的声音感觉像是直接在我头盖骨上施工，我买了降噪耳机都挡不住，周末想睡个懒觉都成了奢望",
        "context": {"title": "", "description": "", "time": "", "topic": ""},
        "ambiguity": "low", "evidence_strength": "weak", "needs_context": False,
        "encoding_primary": "none", "encoding_secondary": [], "hard_negative": True,
        "reasoning": {
            "literal_analysis": ["文本表面是吐槽邻居装修噪音影响休息的日常生活烦恼。"],
            "encoding_analysis": [
                "该文本为纯日常生活吐槽——装修噪音、睡不了懒觉，属于城市居民普遍的生活体验。",
                "hard_negative 样本——吐槽邻居装修完全无害，无任何编码或攻击意图。",
            ],
            "context_analysis": ["无明确上下文；按社交媒体日常吐槽场景判断。"],
            "supporting_evidence": ["文本内容为邻里生活吐槽——属于最普遍的日常生活话题。"],
            "counter_evidence": [
                "生活噪音吐槽是完全无害的日常表达——无任何敏感指向。",
                "hard_negative 样本——模型需学会区分日常吐槽与风险内容。",
            ],
            "final_rationale": "日常生活噪音吐槽（合成样本），完全无害，判为 none。",
        },
    },

    "000660": {
        "text": "老板今天开会说要优化人员结构，我注意到他用的是'优化'不是'裁员'，但是大家心里都清楚，会后同事群里安静得可怕，每个人都在想自己是不是那个被优化的人",
        "context": {"title": "", "description": "", "time": "", "topic": "workplace"},
        "ambiguity": "low", "evidence_strength": "weak", "needs_context": False,
        "encoding_primary": "none", "encoding_secondary": [], "hard_negative": True,
        "reasoning": {
            "literal_analysis": ["文本表面是分享公司可能裁员时同事们的心理状态——老板用委婉词汇、同事紧张不安。"],
            "encoding_analysis": [
                "该文本为职场经历分享——描述裁员传闻下的办公室氛围，属于正常的职业话题。",
                "hard_negative 样本——吐槽职场不等于攻击社会/经济制度，文本无政治指向。",
            ],
            "context_analysis": ["无明确上下文；按职场社交/吐槽场景判断。"],
            "supporting_evidence": ["文本内容为职场经历分享——属于普遍的上班族话题。"],
            "counter_evidence": [
                "职场经历吐槽是最常见的日常表达之一——讨论裁员不等于攻击就业政策或经济制度。",
                "hard_negative 样本——区分'职场个人感受'与'社会攻击'。",
            ],
            "final_rationale": "职场经历分享（合成样本），无政治/攻击意图，判为 none。",
        },
    },

    "000664": {
        "text": "我们小区门口那条路修了快半年了，围挡上写的'前方施工请绕行'，但是围挡里面我看从来没有人干过活，也不知道是不是经费没到位还是单纯的效率问题，反正我们每天绕路已经绕出感情了",
        "context": {"title": "", "description": "", "time": "", "topic": ""},
        "ambiguity": "low", "evidence_strength": "weak", "needs_context": False,
        "encoding_primary": "none", "encoding_secondary": [], "hard_negative": True,
        "reasoning": {
            "literal_analysis": ["文本表面是吐槽小区门口道路施工进展缓慢、围挡长期存在但未见施工的日常观察。"],
            "encoding_analysis": [
                "该文本为社区生活观察——道路施工缓慢属于城市居民常见的话题，吐槽语气幽默而非攻击。",
                "hard_negative 样本——吐槽施工效率不等于攻击政府，属于正常市民反馈。",
            ],
            "context_analysis": ["无明确上下文；按社区生活/日常吐槽场景判断。"],
            "supporting_evidence": ["文本内容为社区基础设施建设体验——属于正常的市民生活反馈。"],
            "counter_evidence": [
                "市政工程吐槽是普遍的日常话题——幽默抱怨与攻击政府有本质区别。",
                "hard_negative 样本——文本中的'经费''效率'等词在市民日常讨论中高频出现，不等同于攻击。",
            ],
            "final_rationale": "社区生活观察吐槽（合成样本），幽默温和无攻击性，判为 none。",
        },
    },

    # ═══════════════════════════════════════════════════════════
    # GROUP 2: low risk (various encoding) — 12条
    # 轻度边缘表达，措辞温和但可能触及敏感话题
    # ═══════════════════════════════════════════════════════════

    "000544": {
        "text": "朋友圈里有人转发了一个新闻标题写着'我国经济稳中向好'，然后配文就两个字'赢麻了'，底下的评论全是队形'赢麻了赢麻了'，有一个评论说'秦始皇摸电门——赢麻了'，这个梗已经被玩到完全脱离了原来的语境，现在只要看到任何正面宣传大家条件反射就是刷赢麻了",
        "context": {"title": "", "description": "", "time": "", "topic": "social"},
        "ambiguity": "low", "evidence_strength": "weak", "needs_context": False,
        "encoding_primary": "D1_反讽", "encoding_secondary": [], "hard_negative": False,
        "reasoning": {
            "literal_analysis": ["文本表面是观察朋友圈中对经济新闻标题的'赢麻了'队形评论现象——讨论网络梗的传播和语义稀释。"],
            "encoding_analysis": [
                "D1_反讽——'赢麻了'是中文互联网对正面宣传进行反讽的经典公式，从'中或最赢'演变而来。",
                "低风险反讽的特征：讽刺对象是模糊的'正面宣传'而非具体个人或群体，且文本以观察者口吻描述现象而非直接攻击。",
            ],
            "context_analysis": ["朋友圈/社交媒体场景——'朋友圈''转发''队形''评论'明确社交平台语境。"],
            "supporting_evidence": ["文本以观察者角度描述网络现象——非直接参与反讽而是分析反讽文化本身。"],
            "counter_evidence": [
                "'赢麻了'在当前互联网中已成为普遍的网络梗——其使用频率极高但具体攻击对象往往模糊。",
                "文本在描述一个观察到的现象（朋友圈评论队形）而非主动表达政治立场。",
            ],
            "final_rationale": "以观察者角度描述'赢麻了'网络梗的传播现象（合成样本），轻度反讽但停留在现象观察，判为 low。",
        },
    },

    "000481": {
        "text": "刚才在技术论坛看到有人发了一串英文字母，一开始以为是代码里的变量名缩写，看了半天发现是某个项目组的内部简称，这种缩写只有圈内人看得懂，外人看了完全不知所云",
        "context": {"title": "", "description": "", "time": "", "topic": ""},
        "ambiguity": "medium", "evidence_strength": "weak", "needs_context": False,
        "encoding_primary": "E1_平台黑话", "encoding_secondary": [], "hard_negative": True,
        "reasoning": {
            "literal_analysis": ["文本表面是描述在技术论坛看到不明含义的英文字母缩写，讨论圈层内部缩写的排他性。"],
            "encoding_analysis": [
                "讨论圈层缩写现象——技术社区的项目代号、内部简称是正常的专业交流工具。",
                "E1_平台黑话在此作为观察对象而非使用——文本在分析圈层用语现象，本身无编码操作。",
            ],
            "context_analysis": ["无明确上下文；按技术社区讨论场景判断。"],
            "supporting_evidence": ["文本讨论的对象是正常的技术社区缩写现象——属于语言学/传播学观察。"],
            "counter_evidence": [
                "圈层缩写不等于违规编码——技术用语、行业黑话、兴趣圈用语各有正当功能。",
                "文本本身是对现象的观察和分析，非使用编码进行攻击。",
            ],
            "final_rationale": "圈层用语现象观察（合成样本），无攻击意图，但话题涉及编码边界，判为 low。",
        },
    },

    "000482": {
        "text": "我写文案的时候习惯在某些词中间加空格，纯粹是因为好看——比如'今天的天 气真好'加个空格让句子呼吸一下，结果被人问是不是在发什么暗号，我说大哥我只是有排版强迫症而已",
        "context": {"title": "", "description": "", "time": "", "topic": ""},
        "ambiguity": "medium", "evidence_strength": "weak", "needs_context": False,
        "encoding_primary": "E1_平台黑话", "encoding_secondary": [], "hard_negative": True,
        "reasoning": {
            "literal_analysis": ["文本表面是分享因排版习惯在词间加空格被误认为在发暗号的趣事。"],
            "encoding_analysis": [
                "讨论空格排版被误读为编码的现象——实际上只是个人审美偏好。",
                "E1_平台黑话在此作为讨论主题而非实际使用——文本在说明正常排版与规避编码的区别。",
            ],
            "context_analysis": ["无明确上下文；按社交媒体日常分享场景判断。"],
            "supporting_evidence": ["文本明确解释了空格是排版习惯而非编码——属于对编码误判的幽默反驳。"],
            "counter_evidence": [
                "排版审美与避审编码有本质区别——不应因形式相似性（空格）而误判。",
                "hard_negative 样本——训练模型区分'形式上的相似'与'意图上的规避'。",
            ],
            "final_rationale": "排版习惯被误读的幽默分享（合成样本），无编码意图，判为 low。",
        },
    },

    "000555": {
        "text": "打游戏的时候队友一直在语音里说'这个赛季的农夫山泉不好打'，我愣了半天才反应过来他说的是某个版本强势的英雄被削弱了，这代称起得也太抽象了，堪比贴吧老哥的黑话水平",
        "context": {"title": "", "description": "", "time": "", "topic": "gaming"},
        "ambiguity": "medium", "evidence_strength": "weak", "needs_context": False,
        "encoding_primary": "D3_借代", "encoding_secondary": [], "hard_negative": True,
        "reasoning": {
            "literal_analysis": ["文本表面是分享游戏语音中队友用'农夫山泉'代指某个游戏英雄/装备的趣事，讨论游戏圈借代用语。"],
            "encoding_analysis": [
                "D3_借代在此为游戏圈内部的趣味代称——'农夫山泉'指代某个被削弱的游戏角色/装备。",
                "游戏圈借代是亚文化身份认同的正常表达——代称的功能是圈层沟通而非攻击规避。",
            ],
            "context_analysis": ["游戏语音/电竞讨论语境——'赛季''强势''削弱'明确指向游戏领域。"],
            "supporting_evidence": ["文本语境明确为游戏讨论——'赛季''英雄''版本'等词汇指向电竞/游戏领域。"],
            "counter_evidence": [
                "游戏圈代称属于正常的亚文化用语——与政治/仇恨编码有本质区别。",
                "hard_negative 样本——'农夫山泉'在游戏语境中是趣味借代而非敏感词规避。",
            ],
            "final_rationale": "游戏圈借代用语趣事（合成样本），无害的亚文化表达，判为 low。",
        },
    },

    "000571": {
        "text": "我爸昨天吃饭的时候突然感慨'这届年轻人不好管了'——起因是我不想按照他给的时间表去相亲，我说我自己的事自己安排，他叹了口气说现在的孩子都有自己的想法，管不住了",
        "context": {"title": "", "description": "", "time": "", "topic": "family"},
        "ambiguity": "low", "evidence_strength": "weak", "needs_context": False,
        "encoding_primary": "none", "encoding_secondary": [], "hard_negative": True,
        "reasoning": {
            "literal_analysis": ["文本表面是分享父亲对年轻人独立性增强的感慨——从相亲安排的分歧引出代际观念差异。"],
            "encoding_analysis": [
                "该文本为家庭日常对话分享——代际分歧属于正常的家庭话题。",
                "hard_negative 样本——'这届年轻人不好管了'在家庭语境中是父亲对子女独立的感慨，无政治隐喻。",
            ],
            "context_analysis": ["家庭餐桌对话场景——父亲和子女关于相亲/人生规划的日常交流。"],
            "supporting_evidence": ["文本语境明确为家庭对话——相亲、时间表、子女独立等均为家庭话题。"],
            "counter_evidence": [
                "家庭代际对话是普遍日常场景——'年轻人不好管'在亲子关系中是对子女成长的感慨。",
                "hard_negative 样本——区分家庭语境中的日常表达与政治隐喻。",
            ],
            "final_rationale": "家庭代际对话分享（合成样本），无政治隐喻，判为 low。",
        },
    },

    "000582": {
        "text": "昨天中秋跟家里人视频，我妈在电话那头指着窗外的月亮说'今晚的月亮好大像个脸盆'，然后我三岁的侄子凑过来说脸盆里面有没有小兔子，全家笑了五分钟",
        "context": {"title": "", "description": "", "time": "", "topic": "family"},
        "ambiguity": "low", "evidence_strength": "weak", "needs_context": False,
        "encoding_primary": "A1_普通谐音", "encoding_secondary": [], "hard_negative": True,
        "reasoning": {
            "literal_analysis": ["文本表面是分享中秋节跟家人视频通话时母亲和侄子的温馨对话——月亮圆得像脸盆、童言找兔子。"],
            "encoding_analysis": [
                "A1_普通谐音在此为纯粹的修辞手法——'脸盆'形容月亮的形状，是常见的比喻修辞，无任何谐音编码。",
                "hard_negative 样本——'脸盆'在此语境中为明喻修辞（月亮圆如脸盆），非谐音替代任何敏感词。",
            ],
            "context_analysis": ["中秋节家庭视频通话场景——团圆、赏月、童趣对话。"],
            "supporting_evidence": ["文本语境为温馨的家庭节日场景——中秋节、家人视频、儿童对话。"],
            "counter_evidence": [
                "比喻修辞（月亮像脸盆）与谐音编码规避审查有本质区别——前者是文学表达，后者是有意规避。",
                "hard_negative 样本——模型需学会区分'文学修辞'与'编码规避'。",
            ],
            "final_rationale": "家庭节日温馨对话（合成样本），纯修辞无编码意图，判为 low。",
        },
    },

    "000639": {
        "text": "在贴吧看到有人发帖问怎么治蟑螂，一楼正经回复'用硼酸'，二楼突然说'弓 虽 女 干 螂'——就是强行用杀虫剂喷它，评论区全是绷不住的笑声，这就是中文互联网的幽默",
        "context": {"title": "", "description": "", "time": "", "topic": ""},
        "ambiguity": "medium", "evidence_strength": "weak", "needs_context": False,
        "encoding_primary": "B1_拆字", "encoding_secondary": [], "hard_negative": False,
        "reasoning": {
            "literal_analysis": ["文本表面是分享贴吧讨论灭蟑螂时有人用拆字手法造出'弓虽女干螂'的搞笑段子——拆字在此作为幽默工具。"],
            "encoding_analysis": [
                "B1_拆字在此为纯粹的幽默/段子手法——将'强''奸'拆开加'螂'组成灭蟑螂的双关笑话。",
                "拆字幽默与拆字编码规避审查有本质区别——前者意图是娱乐，后者意图是规避。",
            ],
            "context_analysis": ["贴吧/论坛的灭蟑螂讨论——语境明确为生活话题+网络段子。"],
            "supporting_evidence": ["文本语境为灭蟑螂的生活讨论——'硼酸''杀虫剂''蟑螂'明确指向家居话题。"],
            "counter_evidence": [
                "拆字在中文互联网中常作为幽默/双关的修辞手法——'弓虽'作为'强'的拆写是中文互联网经典梗。",
                "该拆字的意图是制造灭蟑螂的双关笑话而非规避敏感词——笑话的笑点在拆字造词而非攻击。",
            ],
            "final_rationale": "拆字幽默的网络段子分享（合成样本），拆字作为喜剧手法而非规避编码，判为 low。",
        },
    },

    "000640": {
        "text": "在超市看到一个小孩子在玩具区拿着一把塑料刀挥舞，他妈妈在后面喊'把刀放下'，小孩子回头说'这不是刀，这是一巴激光剑'——把'刀'写成'巴刀'是打字打快了还是故意的我已经分不清了",
        "context": {"title": "", "description": "", "time": "", "topic": ""},
        "ambiguity": "low", "evidence_strength": "weak", "needs_context": False,
        "encoding_primary": "B3_形近字替换", "encoding_secondary": [], "hard_negative": False,
        "reasoning": {
            "literal_analysis": ["文本表面是分享超市里看到小孩玩塑料刀被妈妈制止、小孩辩解是激光剑的温馨趣事，其中'巴刀'可能是打字错误。"],
            "encoding_analysis": [
                "B3_形近字替换在此为可能的输入法错误或儿童语言——'巴'与'把'形近但在此语境中无规避意图。",
                "形近字的出现不等于编码规避——输入法错误、儿童语言、方言影响等都可能导致形近字。",
            ],
            "context_analysis": ["超市玩具区/亲子互动场景——'塑料刀''激光剑''妈妈''小孩'指向家庭日常。"],
            "supporting_evidence": ["文本语境为亲子日常互动——'玩具区''塑料刀''激光剑'等均为家庭购物场景。"],
            "counter_evidence": [
                "'巴刀'在此语境中更可能是输入法错误或儿童用语——与有意的形近字编码规避有本质区别。",
                "单字形近字的出现频率在正常文本中很高——不应因孤立形近字误判整体意图。",
            ],
            "final_rationale": "亲子日常趣事（合成样本），'巴刀'为可能的输入错误非编码规避，判为 low。",
        },
    },

    "000641": {
        "text": "我奶奶是广东人，每次打电话她都说'哩个世界变佐啦'，意思是这个世界变了，以前她看不懂智能手机，现在微信刷得比我还溜，天天在家族群里发早安表情包，时代真的变了",
        "context": {"title": "", "description": "", "time": "", "topic": "family"},
        "ambiguity": "low", "evidence_strength": "weak", "needs_context": False,
        "encoding_primary": "A3_方言谐音", "encoding_secondary": [], "hard_negative": True,
        "reasoning": {
            "literal_analysis": ["文本表面是分享广东奶奶用粤语感叹世界变化、从不会用智能手机到熟练使用微信的温馨故事。"],
            "encoding_analysis": [
                "A3_方言谐音在此为正常的方言使用——'哩个世界变佐啦'是粤语自然表达，非谐音编码。",
                "方言表达与谐音编码规避有本质区别——前者是地域文化特征，后者是有意规避审查。",
            ],
            "context_analysis": ["家庭跨代交流场景——奶奶学用智能手机、发家族群消息。"],
            "supporting_evidence": ["文本语境为温馨的家庭故事——粤语是奶奶的母语，使用方言完全自然。"],
            "counter_evidence": [
                "方言是正常的地域语言特征——不应因非普通话发音被误判为谐音编码规避。",
                "hard_negative 样本——区分'方言自然表达'与'有意谐音编码规避'。",
            ],
            "final_rationale": "方言家庭温馨故事（合成样本），方言自然使用无编码意图，判为 low。",
        },
    },

    "000683": {
        "text": "我们小区业主群里网警突然发了个通告，说最近有人冒充物业人员上门诈骗让大家注意安全，结果下面有人回复说'收到，这就去办'——明显是在玩梗，但网警可能没get到这个笑话",
        "context": {"title": "", "description": "", "time": "", "topic": ""},
        "ambiguity": "medium", "evidence_strength": "weak", "needs_context": False,
        "encoding_primary": "none", "encoding_secondary": [], "hard_negative": True,
        "reasoning": {
            "literal_analysis": ["文本表面是分享小区业主群中网警发反诈通告、业主回复玩梗的日常趣事。"],
            "encoding_analysis": [
                "该文本为社区日常互动分享——网警的反诈通告和业主的幽默回复均属正常交流。",
                "hard_negative 样本——'收到，这就去办'在此语境中是网络流行语的幽默使用，针对诈骗防范而非攻击。",
            ],
            "context_analysis": ["小区业主群/反诈宣传场景——网警、物业、诈骗防范均为社区安全话题。"],
            "supporting_evidence": ["文本语境为社区反诈宣传——网警发通告是正常的执法行为，业主玩梗是正常的网络文化。"],
            "counter_evidence": [
                "网络流行语在日常交流中的使用不等于对抗/不尊重——'收到这就去办'是中文互联网常用回复模板。",
                "hard_negative 样本——区分'玩梗'与'对抗执法'。",
            ],
            "final_rationale": "社区日常互动趣事（合成样本），正常执法+正常玩梗，判为 low。",
        },
    },

    "000572": {
        "text": "昨天晚上出门散步看到天上的月亮又大又圆，还是红色的，我朋友说是因为最近空气湿度大加上城市灯光折射，我说你别科普了让我安静欣赏一下这诡异的美丽的自然现象",
        "context": {"title": "", "description": "", "time": "", "topic": ""},
        "ambiguity": "low", "evidence_strength": "weak", "needs_context": False,
        "encoding_primary": "C4_典故/物品/符号借用", "encoding_secondary": [], "hard_negative": True,
        "reasoning": {
            "literal_analysis": ["文本表面是分享晚上散步看到红色大月亮的自然现象体验，朋友科普了光学原理。"],
            "encoding_analysis": [
                "C4_典故/物品/符号借用在此为自然现象的修辞描述——红色月亮是大气光学现象，非政治符号。",
                "hard_negative 样本——'红色的月亮'在自然观察语境中是物理现象，不携带政治隐喻。",
            ],
            "context_analysis": ["户外散步/自然观察场景——'散步''空气湿度''城市灯光'明确日常休闲语境。"],
            "supporting_evidence": ["文本语境为自然观察体验——'空气湿度''灯光折射'明确指向物理现象解释。"],
            "counter_evidence": [
                "自然现象的修辞描述与政治符号借用有本质区别——红月亮是大气光学现象的科学描述。",
                "hard_negative 样本——模型需学会区分'自然现象描述'与'政治符号影射'。",
            ],
            "final_rationale": "自然现象观察分享（合成样本），无政治符号影射，判为 low。",
        },
    },

    "000573": {
        "text": "看了一个动物纪录片，讲的是草原上的兔子面对鬣狗时的防御策略，解说词说'兔子急了也会咬人的别逼太紧'，然后画面一转那只兔子真的回头咬了鬣狗一口，弹幕全在刷'瑞思拜'",
        "context": {"title": "", "description": "", "time": "", "topic": ""},
        "ambiguity": "low", "evidence_strength": "weak", "needs_context": False,
        "encoding_primary": "C4_典故/物品/符号借用", "encoding_secondary": [], "hard_negative": True,
        "reasoning": {
            "literal_analysis": ["文本表面是分享观看动物纪录片中兔子反击鬣狗的精彩片段和弹幕反应。"],
            "encoding_analysis": [
                "C4_典故/物品/符号借用在此为动物纪录片中的拟人化解说——'兔子急了也咬人'是常见俗语的字面使用。",
                "hard_negative 样本——俗语在动物纪录片中的字面使用不构成政治符号借用。",
            ],
            "context_analysis": ["动物纪录片观看场景——'草原''鬣狗''解说词''弹幕'明确指向娱乐内容消费。"],
            "supporting_evidence": ["文本语境为动物纪录片——所有元素（兔子、鬣狗、草原）均为自然动物主题。"],
            "counter_evidence": [
                "俗语的字面使用（动物真的咬人）与政治隐喻性使用有本质区别——语境决定含义。",
                "hard_negative 样本——区分'字面俗语'与'政治借代'。",
            ],
            "final_rationale": "动物纪录片观看分享（合成样本），俗语字面使用无政治隐喻，判为 low。",
        },
    },

    # ═══════════════════════════════════════════════════════════
    # GROUP 3: medium risk (various encoding) — 15条
    # 中等风险社会/政治评论，有编码手法但无极端仇恨/暴力
    # ═══════════════════════════════════════════════════════════

    "000497": {
        "text": "家人们谁懂啊，今天早上打开微博想看看昨晚发生了什么事，结果热搜前十条有八条是明星穿搭和综艺片段，剩下两条是系统自动推送的广告，真正想看的新闻一条都没有",
        "context": {"title": "", "description": "", "time": "", "topic": "media"},
        "ambiguity": "medium", "evidence_strength": "moderate", "needs_context": False,
        "encoding_primary": "E1_平台黑话", "encoding_secondary": [], "hard_negative": False,
        "reasoning": {
            "literal_analysis": ["文本表面是用'家人们谁懂啊'句式吐槽微博热搜被娱乐内容和广告占据、缺乏实质新闻。"],
            "encoding_analysis": [
                "E1_平台黑话——'热搜被洗'是用户对平台议程设置的委婉批评，用'家人们谁懂啊'软化表达。",
                "平台黑话在此作为委婉批评的工具——用户通过圈层句式表达对信息环境的不满。",
            ],
            "context_analysis": ["无明确上下文；按社交媒体用户体验反馈场景判断。"],
            "supporting_evidence": ["文本表面在讨论微博热搜内容构成——属于普遍的社交媒体用户体验讨论。"],
            "counter_evidence": [
                "对平台内容质量的批评属于正常用户反馈——与攻击平台/传播违规内容有本质区别。",
                "仅凭'家人们谁懂啊'句式和'热搜'一词无法确认具体攻击对象——可能仅为一般性吐槽。",
            ],
            "final_rationale": "使用平台黑话包装的媒体内容批评（合成样本），停留在用户体验吐槽层面，判为 medium。",
        },
    },

    "000537": {
        "text": "最近去打印店想印几份资料，老板说白纸紧缺到处买不到，一问才知道附近的文具批发市场被整顿了，说是消防检查不合格全部关门整改，一个小道消息传着传着就变成了'白纸紧缺'，互联网就是这样",
        "context": {"title": "", "description": "", "time": "", "topic": ""},
        "ambiguity": "medium", "evidence_strength": "moderate", "needs_context": False,
        "encoding_primary": "C4_典故/物品/符号借用", "encoding_secondary": [], "hard_negative": False,
        "reasoning": {
            "literal_analysis": ["文本表面是讲打印店白纸缺货是因为文具市场消防整改——日常生活中的供应链小插曲。"],
            "encoding_analysis": [
                "C4_典故/物品/符号借用——'白纸'在特定语境中可能携带政治符号意义，但本文提供了日常解释。",
                "文本通过给出日常解释（消防整改）来模糊'白纸'的双重含义，典型的可推诿编码。",
            ],
            "context_analysis": ["打印店/文具批发市场——日常消费场景提供了表面合理性。"],
            "supporting_evidence": ["'白纸'在特定圈层中可携带政治符号含义——但字面解释（消防整改）提供合理推诿。"],
            "counter_evidence": [
                "文本明确给出了日常解释（消防检查→市场整改→白纸缺货），字面解读完全合理。",
                "供应链问题的解释细节充分（消防检查、批发市场、关门整改），增加了日常解释的可信度。",
            ],
            "final_rationale": "可推诿的符号借用——'白纸'在特定圈层携带政治含义但文本提供字面解释，判为 medium。",
        },
    },

    "000563": {
        "text": "刚才看到一个新闻刚上了十分钟热搜第一名，我截了个图想发给朋友讨论，结果切出去再回来就已经找不到了，热搜榜上取而代之的是一个明星的机场街拍，热搜又被撤了，截图存证吧",
        "context": {"title": "", "description": "", "time": "", "topic": "media"},
        "ambiguity": "medium", "evidence_strength": "moderate", "needs_context": False,
        "encoding_primary": "E3_互动/热点触发", "encoding_secondary": [], "hard_negative": False,
        "reasoning": {
            "literal_analysis": ["文本表面是描述一则新闻短暂登上热搜后被迅速替换为娱乐内容的观察——用户建议截图保存。"],
            "encoding_analysis": [
                "E3_互动/热点触发——以热搜撤换这一即时事件触发讨论，'截图存证'是用户面对信息消失的常见反应。",
                "对热搜机制的观察包含对信息管控的委婉批评——但停留在现象描述而非直接攻击。",
            ],
            "context_analysis": ["微博热搜/社交媒体场景——热搜机制是公开的平台功能，用户讨论属于正常反馈。"],
            "supporting_evidence": ["文本讨论的是公开可见的平台机制（热搜排名变化）——属于可验证的用户体验观察。"],
            "counter_evidence": [
                "热搜排名变化可能由多种因素导致（算法调整、用户兴趣转移、平台运营）——无法确认具体原因。",
                "对平台内容呈现的观察属于正常用户反馈——与攻击信息管控政策不同。",
            ],
            "final_rationale": "以热点事件触发的平台机制观察（合成样本），委婉批评但无直接攻击，判为 medium。",
        },
    },

    "000595": {
        "text": "我们小区门口那道围墙去年才修好，今年又加高了半米，门卫说是因为最近附近治安不太好要加强安防，但隔壁小区就没加，我越来越觉得这围墙不是为了防贼的",
        "context": {"title": "", "description": "", "time": "", "topic": ""},
        "ambiguity": "medium", "evidence_strength": "moderate", "needs_context": False,
        "encoding_primary": "D2_隐喻", "encoding_secondary": [], "hard_negative": False,
        "reasoning": {
            "literal_analysis": ["文本表面是观察小区围墙反复加高、对官方解释（治安需要）表示怀疑的日常叙事。"],
            "encoding_analysis": [
                "D2_隐喻——'围墙加高'在此作为隐喻框架，可能映射信息管控/言论限制等更广泛的社会现象。",
                "隐喻的可推诿性在于字面解读完全成立——小区围墙确实存在且加高原因可以是治安。",
            ],
            "context_analysis": ["小区/社区生活场景——'门卫''隔壁小区''治安'提供表面合理性。"],
            "supporting_evidence": ["'围墙''加高'在特定讨论中可作为信息管控的隐喻——但字面故事完整且合理。"],
            "counter_evidence": [
                "文本提供了充分的字面解释（治安不好、门卫解释、隔壁对比），日常解读完全成立。",
                "小区安防措施是正常的物业管理行为——加高围墙可能是真实的安全需求。",
            ],
            "final_rationale": "以小区围墙为隐喻框架的可推诿表达（合成样本），双重解读但字面成立，判为 medium。",
        },
    },

    "000622": {
        "text": "只许州官放火不许百姓点灯这句话从小就学，长大才真正理解它的分量。单位里领导可以迟到早退，我们加班一次没打卡就要被通报批评，换个灯管都要走三个审批流程，州官的灯随便点，百姓的灯永远不亮",
        "context": {"title": "", "description": "", "time": "", "topic": "workplace"},
        "ambiguity": "medium", "evidence_strength": "moderate", "needs_context": False,
        "encoding_primary": "C1_历史人物类比", "encoding_secondary": [], "hard_negative": False,
        "reasoning": {
            "literal_analysis": ["文本表面是用'只许州官放火'的典故吐槽职场中的双重标准——领导特权与基层员工管控的对比。"],
            "encoding_analysis": [
                "C1_历史人物类比——借用宋代典故映射当代权力不对等现象，典故本身具有普遍性文化共识。",
                "典故类比的精妙在于字面谈的是古代故事+职场吐槽，但结构可以映射更广泛的权力结构批评。",
            ],
            "context_analysis": ["职场吐槽/单位管理场景——'领导''加班''打卡''审批'提供职场语境。"],
            "supporting_evidence": ["文本核心是以古讽今的社会评论——典故本身是中华文化共识，使用广泛。"],
            "counter_evidence": [
                "文本表面为职场吐槽——'领导迟到''加班打卡''审批流程'均为具体的职场场景。",
                "典故在职场吐槽中的使用非常普遍——'只许州官放火'是形容双重标准的常用成语而非特定政治隐喻。",
            ],
            "final_rationale": "以历史典故包装的职场/权力结构评论（合成样本），典故使用普遍但结构可映射，判为 medium。",
        },
    },

    "000627": {
        "text": "刚才在B站看一个社会新闻的解读视频，弹幕里好多人刷'删前留名'，我就赶紧暂停截了个图，预感这个视频活不过今晚。结果果然今天早上起来那个视频已经变成了'该视频已失效'，连UP主的账号都暂时搜不到了",
        "context": {"title": "", "description": "", "time": "", "topic": "media"},
        "ambiguity": "medium", "evidence_strength": "moderate", "needs_context": False,
        "encoding_primary": "E1_平台黑话", "encoding_secondary": [], "hard_negative": False,
        "reasoning": {
            "literal_analysis": ["文本表面是描述在B站看到社会新闻视频、弹幕预测会被删除、第二天视频确实失效的经历。"],
            "encoding_analysis": [
                "E1_平台黑话——'删前留名'是中文互联网用户面对可能被删除内容时的经典反应，暗示内容敏感性。",
                "'视频已失效''账号搜不到'等描述指向平台内容审核机制——用户讨论审核现象而非直接传播违规内容。",
            ],
            "context_analysis": ["B站弹幕/视频平台场景——'UP主''弹幕''视频失效'明确在线视频平台语境。"],
            "supporting_evidence": ["文本描述的是公开可观察的平台现象（视频被删除）——属于用户体验层面的现象记录。"],
            "counter_evidence": [
                "视频被删除可能是多种原因（版权投诉、社区规范违规、UP主自行删除）——无法确认具体原因。",
                "用户对平台审核的观察属于正常反馈——讨论审核现象不等同于传播违规或攻击平台。",
            ],
            "final_rationale": "以平台黑话包装的内容审核观察（合成样本），讨论审核现象但无攻击，判为 medium。",
        },
    },

    "000652": {
        "text": "我老家那边有个开发区，招商的时候承诺了一堆优惠政策，企业入驻以后发现三年了路都没修好，水电也不稳定，去问管委会人家说这是上面的土政策我们也没办法，地方的土政策比上面的法律还管用，这就是现实",
        "context": {"title": "", "description": "", "time": "", "topic": "policy"},
        "ambiguity": "medium", "evidence_strength": "moderate", "needs_context": False,
        "encoding_primary": "C5_概念替换", "encoding_secondary": [], "hard_negative": False,
        "reasoning": {
            "literal_analysis": ["文本表面是吐槽地方开发区招商承诺不兑现——'土政策'指地方实际执行的规则与正式政策不符。"],
            "encoding_analysis": [
                "C5_概念替换——'土政策'是一个具有特定含义的社会学术语，替换了对地方政府执行力的直接批评。",
                "'土政策'概念将具体的不满抽象化——从个别开发区问题上升到对地方治理结构的观察。",
            ],
            "context_analysis": ["开发区招商/地方政府服务场景——'开发区''管委会''招商''优惠政策'提供具体语境。"],
            "supporting_evidence": ["文本描述的是具体的招商服务体验——开发区基础设施不完善是常见的地方发展问题。"],
            "counter_evidence": [
                "地方政策执行问题属于正常的公共讨论范畴——'土政策'是广泛使用的社会学概念。",
                "文本批评的是具体的地方执行层面——未上升到对整体体制的攻击。",
            ],
            "final_rationale": "以概念替换包装的地方治理批评（合成样本），具体政策吐槽未上升到体制攻击，判为 medium。",
        },
    },

    "000653": {
        "text": "昨天刷到一个快递小哥拍的短视频说'东风快递使命必达，不管你在哪都能送到你手上'，弹幕里全是'哈哈哈哈'和'这可不兴送啊'，笑死了，国企的广告词被网友玩成了段子",
        "context": {"title": "", "description": "", "time": "", "topic": ""},
        "ambiguity": "medium", "evidence_strength": "moderate", "needs_context": False,
        "encoding_primary": "C4_典故/物品/符号借用", "encoding_secondary": [], "hard_negative": False,
        "reasoning": {
            "literal_analysis": ["文本表面是分享快递小哥用'东风快递使命必达'调侃送货服务、网友弹幕互动的幽默段子。"],
            "encoding_analysis": [
                "C4_典故/物品/符号借用——'东风快递'是火箭军的官方昵称，在此被网友借用调侃快递服务。",
                "官方符号的娱乐化使用是中文互联网的普遍现象——从严肃军事符号到快递段子的语义转换。",
            ],
            "context_analysis": ["短视频弹幕/网友互动场景——'快递小哥''弹幕''段子'明确指向娱乐内容。"],
            "supporting_evidence": ["文本表面为快递相关段子——'东风快递'作为军事符号的调侃使用在互联网上非常普遍。"],
            "counter_evidence": [
                "军事符号的娱乐化使用不等于攻击/贬损——'东风快递'是官方认可的昵称，网友调侃属于幽默范畴。",
                "弹幕中的'这可不兴送啊'直接否定了危险解读——网友在主动划清玩笑边界。",
            ],
            "final_rationale": "军事符号娱乐化使用的段子分享（合成样本），网友互动明确了玩笑边界，判为 medium。",
        },
    },

    "000654": {
        "text": "在微信群里聊到最近的一个新闻，我刚想发表一下看法，群里一个前辈私信我说'管好自己的嘴不该说的别说'，我才意识到这个话题确实敏感，赶紧把打了一半的字删了，前辈说年轻人有想法是好事但要学会看场合",
        "context": {"title": "", "description": "", "time": "", "topic": "social"},
        "ambiguity": "medium", "evidence_strength": "moderate", "needs_context": False,
        "encoding_primary": "E1_平台黑话", "encoding_secondary": [], "hard_negative": False,
        "reasoning": {
            "literal_analysis": ["文本表面是分享在微信群中讨论新闻时被前辈提醒注意言论尺度的职场/社交经历。"],
            "encoding_analysis": [
                "E1_平台黑话——'管好自己的嘴''不该说的别说'是中文互联网中关于言论边界的经典提醒。",
                "文本在元层面讨论了自我审查——通过前辈提醒的叙事来暗示话题的敏感性，而非直接表达敏感内容。",
            ],
            "context_analysis": ["微信群/职场社交场景——'微信群''前辈''私信'提供具体的社交语境。"],
            "supporting_evidence": ["文本描述的是普遍存在的社交媒体言论尺度讨论——属于常见的职场/社交话题。"],
            "counter_evidence": [
                "讨论言论边界本身是正常话题——文本以过来人提醒晚辈的口吻叙述，立场为保护而非煽动。",
                "'年轻人有想法是好事但要学会看场合'提供了积极的建设性框架。",
            ],
            "final_rationale": "以平台黑话包装的言论边界元讨论（合成样本），自我审查叙事暗示敏感性但无攻击，判为 medium。",
        },
    },

    "000655": {
        "text": "'风雨送春归飞雪迎春到'——小时候背这首诗只觉得写得很美，长大以后每次看到新闻里某些事情的发生，脑子里就会自动跳出这两句，不知道为什么，可能是一种条件反射吧",
        "context": {"title": "", "description": "", "time": "", "topic": ""},
        "ambiguity": "medium", "evidence_strength": "moderate", "needs_context": False,
        "encoding_primary": "C1_历史人物类比", "encoding_secondary": [], "hard_negative": False,
        "reasoning": {
            "literal_analysis": ["文本表面是分享从小背诵的毛泽东诗词在成年后看到某些新闻时自动浮现的心理体验。"],
            "encoding_analysis": [
                "C1_历史人物类比——通过引用诗词唤起对特定历史人物和时代氛围的联想，不直接点名但利用文化共识。",
                "诗词引用作为编码工具——利用经典文本的公众熟悉度传递弦外之音，'不知道为什么'的假装无辜增强了可推诿性。",
            ],
            "context_analysis": ["无明确上下文；诗词记忆+新闻阅读场景——表面为个人阅读体验分享。"],
            "supporting_evidence": ["文本引用的诗词是公开发表的经典作品——字面上是正常的文学赏析。"],
            "counter_evidence": [
                "诗词在中文文化中的引用极为普遍——'看到新闻就想起某句诗'是正常的文学联想体验。",
                "文本未明确指向任何具体事件或人物——'某些事情'极度模糊，无法确认映射目标。",
            ],
            "final_rationale": "以诗词引用包装的模糊政治联想（合成样本），引用经典但映射对象模糊，判为 medium。",
        },
    },

    "000667": {
        "text": "最近在B站发现一个律师UP主，专门讲劳动仲裁的案例，每一期都在说打工人的合法权益怎么维护，评论区有人说'这个律师很敢说建议关注'，但其实他讲的全是法律条文里本来就有的权利，敢说的意思可能是大部分人不敢用这些权利",
        "context": {"title": "", "description": "", "time": "", "topic": "legal"},
        "ambiguity": "medium", "evidence_strength": "moderate", "needs_context": False,
        "encoding_primary": "E3_互动/热点触发", "encoding_secondary": [], "hard_negative": False,
        "reasoning": {
            "literal_analysis": ["文本表面是推荐讲劳动法的律师UP主——讨论法律科普内容的'敢说'标签与法律实际内容的关系。"],
            "encoding_analysis": [
                "E3_互动/热点触发——以律师UP主这一热点人物为触发，讨论法律权利与'敢说'标签的张力。",
                "'敢说的意思是大部分人不敢用这些权利'——将法律科普与权利实践的现实困难联系起来。",
            ],
            "context_analysis": ["B站/法律科普场景——'UP主''劳动仲裁''法律条文'明确知识分享语境。"],
            "supporting_evidence": ["文本讨论的是合法的劳动仲裁和法律科普——属于正常的法律知识传播。"],
            "counter_evidence": [
                "法律科普是受鼓励的正面内容——律师讲解法律条文属于公共服务。",
                "'敢说'是对科普勇气的正面评价——法律科普本身不构成风险。",
            ],
            "final_rationale": "以热点人物触发的法律科普讨论（合成样本），正面内容但隐含对权利实践的反思，判为 medium。",
        },
    },

    "000669": {
        "text": "微信群里有人发了个新闻链接问大家的看法，我正准备打字回复，另一个群友说'这件事不方便在群里说咱们私聊'，然后群里就安静了。过了十分钟那个人在群里发了个猫猫表情包把话题岔开了，大家就开始聊猫了",
        "context": {"title": "", "description": "", "time": "", "topic": "social"},
        "ambiguity": "medium", "evidence_strength": "moderate", "needs_context": False,
        "encoding_primary": "E1_平台黑话", "encoding_secondary": [], "hard_negative": False,
        "reasoning": {
            "literal_analysis": ["文本表面是描述微信群中因话题敏感被建议私聊、群友用猫猫表情包转移话题的日常社交场景。"],
            "encoding_analysis": [
                "E1_平台黑话——'不方便在群里说''私聊'是中文互联网用户在公开群聊中面对敏感话题的标准回避话术。",
                "文本通过'猫猫表情包转移话题'展示了中文互联网用户自我审查的完整流程——暗示、回避、转移。",
            ],
            "context_analysis": ["微信群聊社交场景——'群友''表情包''猫猫'明确日常社交语境。"],
            "supporting_evidence": ["文本描述的是普遍存在的群聊社交现象——回避敏感话题属于常见的社交礼仪。"],
            "counter_evidence": [
                "群聊中的话题回避是正常的社交行为——'不方便说'可能出于多种非政治原因（隐私、工作、人际关系）。",
                "猫猫表情包转移话题是中文互联网的经典社交操作——属于无害的日常互动。",
            ],
            "final_rationale": "以平台黑话描述的群聊自我审查场景（合成样本），观察社交现象而非传播违规内容，判为 medium。",
        },
    },

    "000671": {
        "text": "在某个论坛看到一句话'有群众的地方就有斗争'，本来以为是讲基层工作的文章，点进去发现是在讨论小区业主委员会成立的艰难过程——物业公司、开发商、部分业主之间的利益纠葛，确实是一场斗争",
        "context": {"title": "", "description": "", "time": "", "topic": "community"},
        "ambiguity": "medium", "evidence_strength": "moderate", "needs_context": False,
        "encoding_primary": "C4_典故/物品/符号借用", "encoding_secondary": [], "hard_negative": False,
        "reasoning": {
            "literal_analysis": ["文本表面是分享在论坛看到一句话（有群众的地方就有斗争）被用于描述小区业委会成立过程的文章观感。"],
            "encoding_analysis": [
                "C4_典故/物品/符号借用——'有群众的地方就有斗争'是一句具有特定历史来源的表述，在此被借用描述小区治理冲突。",
                "将宏大政治话语降维到日常生活场景——从'群众斗争'到'业委会vs物业'的语义降级提供了字面合理性。",
            ],
            "context_analysis": ["论坛/社区治理场景——'业委会''物业''开发商''业主'明确小区管理语境。"],
            "supporting_evidence": ["文本语境为具体的小区治理冲突——'业委会成立''物业公司''利益纠葛'提供真实生活背景。"],
            "counter_evidence": [
                "经典表述在日常生活场景中的引用很普遍——'斗争'在此指具体的利益博弈而非政治运动。",
                "业委会成立确实是社区治理中的常见矛盾——文本讨论的是真实的基层治理问题。",
            ],
            "final_rationale": "经典表述降维到社区治理话题（合成样本），降维使用但引用了具有历史含义的句式，判为 medium。",
        },
    },

    "000680": {
        "text": "教孩子历史课的时候讲到五四运动，孩子问我五四运动的精神今天还在吗，我想了想跟他说'五四运动的精神是爱国进步民主科学，这些精神不会消失，只是每个时代的表现方式不同，你们这一代也会有属于你们的五四'",
        "context": {"title": "", "description": "", "time": "", "topic": "education"},
        "ambiguity": "medium", "evidence_strength": "moderate", "needs_context": False,
        "encoding_primary": "C2_历史事件影射", "encoding_secondary": [], "hard_negative": False,
        "reasoning": {
            "literal_analysis": ["文本表面是分享在家教孩子历史时孩子对五四精神的童真提问和家长的正面引导回答。"],
            "encoding_analysis": [
                "C2_历史事件影射——通过孩子天真提问'五四精神今天还在吗'引入对历史价值观当代传承的讨论。",
                "以家庭教育场景包装历史反思——孩子的'天真提问'是编码工具，使敏感话题以教育形式呈现。",
            ],
            "context_analysis": ["家庭教育/历史学习场景——'教孩子''历史课''五四运动'提供教育语境。"],
            "supporting_evidence": ["文本讨论的是教科书中的标准历史内容——五四运动是中学历史必修内容。"],
            "counter_evidence": [
                "五四运动是官方肯定的历史事件——讨论其精神传承属于正常的爱国主义教育。",
                "家长的回答体现了正面引导——'每个时代的表现方式不同'是建设性的历史观教育。",
            ],
            "final_rationale": "以家庭教育场景包装的历史价值观讨论（合成样本），正面引导但话题触及历史反思，判为 medium。",
        },
    },

    "000682": {
        "text": "翻了翻QQ空间里十年前写的日记，那时候还在上大学，写满了对未来的憧憬和担忧——担心找不到工作、担心留不在这个城市、担心辜负父母的期望。十年前谁能想到今天会是这样，好像担心的都发生了，好像又什么都没发生",
        "context": {"title": "", "description": "", "time": "", "topic": "life"},
        "ambiguity": "medium", "evidence_strength": "moderate", "needs_context": False,
        "encoding_primary": "E2_时间节点触发", "encoding_secondary": [], "hard_negative": False,
        "reasoning": {
            "literal_analysis": ["文本表面是翻看十年前QQ空间日记的怀旧感慨——大学时期的焦虑与十年后的现实对照。"],
            "encoding_analysis": [
                "E2_时间节点触发——以'十年前'为时间锚点，通过个人成长叙事触发对社会变迁的感慨。",
                "'好像担心的都发生了好像又什么都没发生'——模糊表达为多种解读留空间，典型的个人叙事编码。",
            ],
            "context_analysis": ["个人怀旧/QQ空间场景——'日记''大学''QQ空间'明确个人成长回忆语境。"],
            "supporting_evidence": ["文本表面为个人成长回忆——翻旧日记、对比十年前后是普遍的怀旧行为。"],
            "counter_evidence": [
                "个人怀旧是最常见的日常表达之一——'十年前谁能想到今天'是普遍的人生感慨。",
                "文本的感慨对象是个人的就业、居住、家庭期望——属于私人生活范畴。",
            ],
            "final_rationale": "以时间节点触发的个人怀旧叙事（合成样本），个人感慨但'今天会是这样'留白可被填充，判为 medium。",
        },
    },

    "000570": {
        "text": "最近看国际新闻总有一种感觉——西边的风有点大，吹得人站不稳。我们这边的新闻天天在说形势一片大好，但是股市和汇率不会骗人，风到底有多大看看账户就知道了",
        "context": {"title": "", "description": "", "time": "", "topic": "economy"},
        "ambiguity": "medium", "evidence_strength": "moderate", "needs_context": False,
        "encoding_primary": "D2_隐喻", "encoding_secondary": [], "hard_negative": False,
        "reasoning": {
            "literal_analysis": ["文本表面是用天气隐喻（西边的风）表达对国际形势和经济状况的担忧——引用股市和汇率作为客观指标。"],
            "encoding_analysis": [
                "D2_隐喻——'西边的风'隐喻西方/国际形势的压力，'站不稳'隐喻国内经济承压。",
                "多层隐喻结构——'天气→国际形势→经济指标'，每层都有日常解释（字面上确实在说天气→经济）。",
            ],
            "context_analysis": ["经济/金融讨论场景——'股市''汇率''账户'提供真实的投资理财语境。"],
            "supporting_evidence": ["文本明确引用了可验证的经济指标（股市、汇率）——属于正常的投资理财讨论范畴。"],
            "counter_evidence": [
                "以天气比喻经济形势是常见的修辞手法——'风向''风口'在财经评论中高频出现。",
                "讨论股市和汇率属于正常的投资观察——个人投资者关注市场波动是普遍行为。",
            ],
            "final_rationale": "以天气隐喻包装的经济形势评论（合成样本），财经讨论范畴但隐喻指向国际形势，判为 medium。",
        },
    },

    # ═══════════════════════════════════════════════════════════
    # GROUP 4: high risk (various encoding) — 5条
    # 高风险但非极端仇恨/暴力，编码明确且无法推诿
    # ═══════════════════════════════════════════════════════════

    "000522": {
        "text": "看到新闻里某个领导在台上讲反腐倡廉，底下的人一个个正襟危坐认真做笔记，我突然想到一句诗——王莽谦恭未篡时。不是说他一定会怎样，只是这个画面和历史重叠得太精准了，让人不寒而栗",
        "context": {"title": "", "description": "", "time": "", "topic": "political"},
        "ambiguity": "low", "evidence_strength": "strong", "needs_context": False,
        "encoding_primary": "C1_历史人物类比", "encoding_secondary": [], "hard_negative": False,
        "reasoning": {
            "literal_analysis": ["文本表面是用历史人物王莽篡位前的谦恭表现类比当代领导人在反腐会议上的表态——暗示伪善。"],
            "encoding_analysis": [
                "C1_历史人物类比——'王莽谦恭未篡时'是经典的历史人物编码，王莽=篡位前伪装正直的野心家。",
                "该类比在鉴证圈中具有高度固化的映射关系——'王莽'直接指向对当代政治人物的'伪君子'指控。",
            ],
            "context_analysis": ["政治会议/新闻观看场景——'领导''反腐倡廉''做笔记'指向官方政治活动。"],
            "supporting_evidence": ["王莽在鉴证圈是高度固化的编码符号——'谦恭未篡时'直接暗示当前的表态是伪装。"],
            "counter_evidence": [
                "字面上只是引用古诗和历史典故——白居易的诗句本身是文学经典。",
                "短文本无法确认具体的映射对象——'某个领导'极度模糊。",
            ],
            "final_rationale": "固化历史人物类比（合成样本），王莽编码在鉴证圈中的映射关系已高度稳定且具攻击性，判为 high。",
        },
    },

    "000589": {
        "text": "群里有人发了一个链接说点进去注册一下就能看到外面的世界，链接的标题写着'老大哥会照顾好你的不用担心'，这不知道是反讽还是认真的，但不管哪种都让人心里发毛",
        "context": {"title": "", "description": "", "time": "", "topic": "political"},
        "ambiguity": "low", "evidence_strength": "strong", "needs_context": False,
        "encoding_primary": "C4_典故/物品/符号借用", "encoding_secondary": [], "hard_negative": False,
        "reasoning": {
            "literal_analysis": ["文本表面是分享群聊中有人发翻墙链接并用奥威尔'老大哥'典故作为标题——叙述者表达了不安。"],
            "encoding_analysis": [
                "C4_典故/物品/符号借用——'老大哥'是奥威尔《1984》中极权监控者的经典符号，在简中互联网直接映射。",
                "'老大哥会照顾好你'是反讽句式——将监控包装为'照顾'，利用奥威尔式的'战争即和平'修辞结构。",
            ],
            "context_analysis": ["群聊/翻墙工具分享场景——'链接''注册''外面的世界'明确指向规避网络审查。"],
            "supporting_evidence": ["'老大哥'在简中互联网是高度固化的极权监控符号——《1984》的映射关系具有跨文化共识。"],
            "counter_evidence": [
                "文学典故的使用不等于实际攻击——奥威尔的小说是公开出版物。",
                "叙述者表达了不安情绪——文本并非直接传播链接而是以担忧口吻转述。",
            ],
            "final_rationale": "以经典极权符号包装的翻墙工具分享转述（合成样本），符号固化且指向明确，判为 high。",
        },
    },

    "000638": {
        "text": "最近发现很多之前关注的博主都 石 卒 了——就是账号突然消失的意思，有些是主动注销的，有些是莫名其妙就没有了，连个解释都没有。这个圈子越来越像是行走在蛋壳上，每一步都可能踩 石 卒 什么东西",
        "context": {"title": "", "description": "", "time": "", "topic": "media"},
        "ambiguity": "low", "evidence_strength": "strong", "needs_context": False,
        "encoding_primary": "B1_拆字", "encoding_secondary": [], "hard_negative": False,
        "reasoning": {
            "literal_analysis": ["文本表面是用拆字手法（石+卒=碎）描述关注的博主账号消失的现象——讨论互联网内容生态。"],
            "encoding_analysis": [
                "B1_拆字——'石 卒'是'碎'的拆字，在此描述账号'破碎/消失'。拆字直接规避了'碎'这个可能触发审核的表述。",
                "拆字在此不是幽默工具而是真实的规避手段——'踩碎石什么东西'暗示在敏感边界上行走的危险。",
            ],
            "context_analysis": ["社交媒体/内容创作者生态场景——'博主''账号''注销'明确互联网内容讨论。"],
            "supporting_evidence": ["拆字使用有明确的规避意图——'石 卒'不是排版习惯而是刻意拆分以描述账号被清理。"],
            "counter_evidence": [
                "拆字作为修辞手法在中文互联网中历史悠久——但此处的使用语境（账号消失）使其规避性质明确。",
                "讨论账号消失可能是真实的内容生态观察——有些账号确实因各种原因主动或被动消失。",
            ],
            "final_rationale": "以拆字编码规避的账号清理现象描述（合成样本），拆字有明显的审核规避意图，判为 high。",
        },
    },

    "000647": {
        "text": "读到一段话越看越觉得不对劲——'凡是敌人反对的我们就要拥护凡是敌人拥护的我们就要反对'，这段话单独看没毛病甚至挺励志，但放到现在的网络环境里，总觉得是在讽刺某些非黑即白的舆论氛围",
        "context": {"title": "", "description": "", "time": "", "topic": "media"},
        "ambiguity": "low", "evidence_strength": "strong", "needs_context": False,
        "encoding_primary": "C4_典故/物品/符号借用", "encoding_secondary": [], "hard_negative": False,
        "reasoning": {
            "literal_analysis": ["文本表面是分享读到一段话后对其在不同语境下含义变化的思考——单独看励志，放现在看讽刺。"],
            "encoding_analysis": [
                "C4_典故/物品/符号借用——引用具有特定历史来源的经典语录，将其重新语境化以讽刺当代舆论氛围。",
                "'非黑即白的舆论氛围'是对言论环境的直接批评——通过引用经典语录来为批评提供历史参照和讽刺张力。",
            ],
            "context_analysis": ["阅读/网络舆论讨论场景——'读到一段话''网络环境''舆论氛围'指向言论生态讨论。"],
            "supporting_evidence": ["引用的语录具有明确的特定历史和政治关联——在当代网络语境中立即触发联想。"],
            "counter_evidence": [
                "语录本身是公开发表的经典内容——单独引用的字面含义是正面的（分清敌我）。",
                "文本以'总觉得'开头——表达个人感受而非断言，为解读留有余地。",
            ],
            "final_rationale": "以经典语录重新语境化讽刺舆论氛围（合成样本），引用的语录具有明确政治关联且讽刺指向清晰，判为 high。",
        },
    },

    "000681": {
        "text": "重读鲁迅的《狂人日记》，里面翻来覆去在字缝里找'吃人'那一段，放到现在就是翻来覆去在热搜里找被删除的新闻——鲁迅说'从来如此便对吗'，我们现在问'从来如此便对吗'，一百年了问题还是那个问题",
        "context": {"title": "", "description": "", "time": "", "topic": "political"},
        "ambiguity": "low", "evidence_strength": "strong", "needs_context": False,
        "encoding_primary": "C1_历史人物类比", "encoding_secondary": [], "hard_negative": False,
        "reasoning": {
            "literal_analysis": ["文本表面是分享重读鲁迅《狂人日记》的感悟——将'字缝里找吃人'类比为'热搜里找被删新闻'。"],
            "encoding_analysis": [
                "C1_历史人物类比——鲁迅在简中互联网是批判性知识分子的符号，'从来如此便对吗'是经典质疑句式。",
                "通过鲁迅类比构建跨时代的批判连续性——'一百年了问题还是那个问题'直接将历史批判延伸到当代。",
            ],
            "context_analysis": ["文学阅读/社会评论场景——'鲁迅''狂人日记''热搜'将文学经典与当代现实并置。"],
            "supporting_evidence": ["鲁迅符号在鉴证圈中高度固化——'从来如此便对吗'是直接质疑现状的经典引用。"],
            "counter_evidence": [
                "鲁迅是中国现代文学经典——讨论其作品属于正常文学赏析范畴。",
                "文学感悟与政治批判之间的边界模糊——字面上是文学读后感。",
            ],
            "final_rationale": "以鲁迅符号包装的跨时代批判（合成样本），鲁迅符号在鉴证圈中高度固化且批判指向当代，判为 high。",
        },
    },

}

# ─── 主流程 ───────────────────────────────────────────────────

def main():
    with open(DATA_PATH) as f:
        samples = [json.loads(line) for line in f]

    # 备份
    with open(BACKUP_PATH, 'w') as f:
        for s in samples:
            f.write(json.dumps(s, ensure_ascii=False) + '\n')
    print(f"✓ 备份到 {BACKUP_PATH}")

    replaced = 0
    for s in samples:
        sid = s['id']
        if sid not in REPLACEMENTS:
            continue

        rep = REPLACEMENTS[sid]

        # 保留原有字段
        s['text'] = rep['text']
        s['context'] = rep['context']
        s['ambiguity'] = rep['ambiguity']
        s['evidence_strength'] = rep['evidence_strength']
        s['needs_context'] = rep['needs_context']
        s['encoding_primary'] = rep['encoding_primary']
        s['encoding_secondary'] = rep['encoding_secondary']
        s['hard_negative'] = rep['hard_negative']
        s['reasoning'] = rep['reasoning']
        s['quality_status'] = 'reviewed'

        # 更新 review_notes
        old_notes = s.get('review_notes', '')
        if 'quality_reviewed=replace_b1' not in old_notes:
            s['review_notes'] = old_notes + '; quality_reviewed=replace_b1'

        replaced += 1

    # 写回
    with open(DATA_PATH, 'w') as f:
        for s in samples:
            f.write(json.dumps(s, ensure_ascii=False) + '\n')

    print(f"✓ 替换 {replaced}/{len(REPLACEMENTS)} 条旧合成样本")
    print(f"  - phase3_first_wave 元样本: 5条")
    print(f"  - batch1-4 超短模板样本: {replaced - 5}条")


if __name__ == "__main__":
    main()
