#!/usr/bin/env python3
"""替换 phase3_v2 第5批：历史人物代指（20条）"""

import json, os
OUT = "data/raw/batch_replace_05_history.jsonl"

samples = [
    # ═══ HIGH (5条) ═══════════════════════════════════
    {
        "text": "腊肉挂在城楼上这么多年了，每年还有人去排队看，你说他们是真怀念还是被学校组织去的，我小学的时候就被拉去排过队，老师提前交代了不许笑不许说话，后来才知道为什么",
        "risk_level": "high",
        "encoding_primary": "C4_典故/物品/符号借用",
        "encoding_secondary": ["C2_历史事件影射", "D1_反讽"],
        "needs_context": False, "ambiguity": "low", "evidence_strength": "strong",
        "hard_negative": False,
        "reasoning": {
            "literal_analysis": ["表面说腊肉挂在城楼上供人参观，讲述小时候被组织排队参观的经历。"],
            "encoding_analysis": [
                "腊肉=毛泽东（源自特定历史时期的说法，将毛的遗体比喻为腊肉。这个比喻最早来自某位外国领导人的私下评论，后流传至网络成为毛的贬义代指）。",
                "'挂在城楼上'指的是天安门城楼上的毛泽东像和毛主席纪念堂中的遗体。",
                "'被学校组织去排队'揭示了对毛的崇拜是自上而下组织的。",
                "'后来才知道为什么'是编码完成句——暗示长大了才明白当年不让笑不让说话的原因：不是尊重，是管控。"
            ],
            "context_analysis": [
                "毛的历史评价是高度敏感话题。腊肉作为贬义代指出现在对官方崇拜仪式的反思中。",
                "评论将'排队看腊肉'与'被组织''不许笑''后来才懂'等细节串联，形成对官方历史叙事的消解。"
            ],
            "supporting_evidence": [
                "腊肉在网络上已固化为毛的贬义代指。",
                "被组织排队→不许笑→后来才懂：完整的认知觉醒叙事。",
                "对官方崇拜仪式的消解。"
            ],
            "counter_evidence": [
                "如果腊肉真的就是指腊肉，那'挂在城楼上'是小概率的说法。",
                "但结合'学校组织''不许笑''后来知道为什么'，指向性明确。"
            ],
            "final_rationale": "领导人贬义代指+官方崇拜仪式消解+认知觉醒叙事，判为 high。"
        }
    },
    {
        "text": "常凯申当年在日记里写的那些东西现在被翻出来看真是一言难尽，一边骂苏联一边求美国，一边说共匪该死一边自己也在屠村，历史这东西经不起细看",
        "risk_level": "high",
        "encoding_primary": "C1_历史人物类比",
        "encoding_secondary": ["C2_历史事件影射", "A1_普通谐音"],
        "needs_context": False, "ambiguity": "low", "evidence_strength": "strong",
        "hard_negative": False,
        "reasoning": {
            "literal_analysis": ["讨论某历史人物日记中的矛盾行为——骂苏联、求美国、屠村。"],
            "encoding_analysis": [
                "常凯申=蒋介石（Chiang Kai-shek的错误音译→常凯申，源自清华某学者将Chiang Kai-shek误译为'常凯申'的学术事件，此后'常凯申'成为蒋的网络代指兼调侃符号）。",
                "讨论蒋的历史行为——骂苏联+求美国+屠村，描绘了蒋在历史中的两面性。",
                "'历史经不起细看'是关键的编码收尾——暗示任何政治人物的历史都有不堪的一面。"
            ],
            "context_analysis": [
                "常凯申本身已成为一种网络文化符号——用学术错误来调侃历史的严肃性。",
                "但讨论延伸到对历史人物的道德审判，涉及两岸共同的历史记忆。"
            ],
            "supporting_evidence": [
                "常凯申是蒋介石的高频网络代指。",
                "对历史人物两面性的揭露。",
                "历史经不起细看的泛化暗示。"
            ],
            "counter_evidence": [
                "讨论已故历史人物本身的敏感度低于讨论现任领导人。",
                "但'历史经不起细看'的泛化暗示有解构官方历史叙事的意图。"
            ],
            "final_rationale": "历史人物代指+两面性揭露+官方历史叙事解构，判为 high。"
        }
    },
    {
        "text": "总设计师当年说让一部分人先富起来，确实做到了，富起来的那部分人现在都在国外买岛买酒庄，剩下的那部分人还在等着先富带后富，等了四十年了还在等，不知道还要等几个四十年",
        "risk_level": "high",
        "encoding_primary": "C1_历史人物类比",
        "encoding_secondary": ["D1_反讽", "C2_历史事件影射"],
        "needs_context": False, "ambiguity": "low", "evidence_strength": "strong",
        "hard_negative": False,
        "reasoning": {
            "literal_analysis": ["讨论某经济改革话语——'先富带后富'四十年未兑现。"],
            "encoding_analysis": [
                "总设计师=邓小平（邓被称为'改革开放的总设计师'，这个官方尊称在网络上被反讽性使用——用来指代邓的同时，'设计'一词暗示一切是有意安排的）。",
                "'让一部分人先富起来'是邓的著名语录，在此被用来揭露改革开放承诺的未兑现。",
                "'富起来的在国外买岛，剩下的还在等'将贫富差距的扩大归咎于改革开放的制度设计。",
                "'等了四十年了还在等'是对邓小平路线的根本性质疑。"
            ],
            "context_analysis": [
                "改革开放的成果分配不均是近年中国社会的主要矛盾之一。",
                "将贫富差距归咎于邓的'设计'，是对改革开放叙事的根本性挑战。"
            ],
            "supporting_evidence": [
                "总设计师是邓小平的固定代指。",
                "先富带后富→国外买岛→等了四十年：完整的改革开放批判叙事。",
                "对改革开放路线根本性的质疑。"
            ],
            "counter_evidence": [
                "先富带后富的讨论是公共政策讨论。",
                "但将问题归咎于'设计'而非执行偏差，有制度否定倾向。"
            ],
            "final_rationale": "历史人物代指+改革开放成果批判+制度设计质疑，判为 high。"
        }
    },
    {
        "text": "图书管理员这个职业真是卧虎藏龙，北京那个就不说了大家都知道，历史上好几个改变世界的都是从图书馆里走出来的，所以说不要小看任何一个在图书馆里翻旧报纸的人",
        "risk_level": "high",
        "encoding_primary": "C4_典故/物品/符号借用",
        "encoding_secondary": ["C1_历史人物类比", "D2_隐喻"],
        "needs_context": False, "ambiguity": "low", "evidence_strength": "strong",
        "hard_negative": False,
        "reasoning": {
            "literal_analysis": ["表面讨论图书管理员这个职业人才辈出，举了北京的例子和历史上的例子。"],
            "encoding_analysis": [
                "图书管理员=毛泽东（毛年轻时在北大图书馆做过管理员，这个身份在网络上被用来代指毛本人——既是一种致敬也是一种反讽，取决于上下文）。",
                "'北京那个就不说了大家都知道'是经典编码提示——用'不说了'来强调'你应该知道我说的是谁'。",
                "'历史上好几个改变世界的都是从图书馆里走出来的'将毛的政治轨迹浪漫化为'改变世界'——表面敬仰，但在特定语境中也可解读为反讽。"
            ],
            "context_analysis": [
                "图书管理员作为毛的代指本身评价中性，但结合'改变世界'的宏观叙事——可以是对毛的正面评价也可以是对其'改变'的反思。"
            ],
            "supporting_evidence": [
                "图书管理员在网络上已固化为毛的代指。",
                "北京那个+大家都知道=双重编码确认。",
                "改变世界的说法在反讽语境中含义翻转。"
            ],
            "counter_evidence": [
                "可以是对毛的正面致敬。",
                "没有直接批评或贬低。"
            ],
            "final_rationale": "领导人符号代指+编码确认信号+宏观历史评价（可在反讽与歌颂间切换），敏感性高，判为 high。"
        }
    },
    {
        "text": "委员长当年要是赢了现在会怎么样，这种架空历史的问题每次提出来都有人吵翻天，但说实话，不管谁赢，老百姓的日子都不会有太大区别，该交的税一样交，该服的管一样服",
        "risk_level": "high",
        "encoding_primary": "C1_历史人物类比",
        "encoding_secondary": ["C2_历史事件影射", "D1_反讽"],
        "needs_context": False, "ambiguity": "low", "evidence_strength": "strong",
        "hard_negative": False,
        "reasoning": {
            "literal_analysis": ["架空历史讨论：如果蒋介石赢了内战现在会怎样。"],
            "encoding_analysis": [
                "委员长=蒋介石（蒋曾任国民政府军事委员会委员长，在大陆时期'委员长'为其正式称谓，在网络上被沿用为代指）。",
                "架空历史的讨论将国共内战的结果视为偶然——暗示历史本可以不同。",
                "最关键的是最后一句——'不管谁赢老百姓的日子都不会有太大区别'，将国共两党等同为压迫机器，对两者的治理本质进行了等值否定。"
            ],
            "context_analysis": [
                "架空历史的讨论本身不违法，但最后一句将国共做等值比较——两者都是'交税''服管'——直接否定了共产党执政的正当性。"
            ],
            "supporting_evidence": [
                "委员长是蒋介石的固定代指。",
                "国共内战架空历史+两党等值否定。",
                "结尾句直接否定了共产党相对于国民党的优越性。"
            ],
            "counter_evidence": [
                "形式上只是历史假设。",
                "但结尾句的等值判断超出了假设的范畴。"
            ],
            "final_rationale": "历史人物代指+国共内战架空讨论+两党等值否定，否定了执政正当性，判为 high。"
        }
    },

    # ═══ MEDIUM (8条) ═══════════════════════════════════
    {
        "text": "大救星这个说法现在基本听不到了，小时候课本里到处都是，后来慢慢就没了，换成了一些更现代的词汇，但意思差不多，语言在进化但内核没变",
        "risk_level": "medium",
        "encoding_primary": "C4_典故/物品/符号借用",
        "encoding_secondary": ["D1_反讽"],
        "needs_context": False, "ambiguity": "medium", "evidence_strength": "moderate",
        "hard_negative": False,
        "reasoning": {
            "literal_analysis": ["讨论'大救星'这个词汇从课本中消失，被现代词汇替代但内核不变。"],
            "encoding_analysis": [
                "大救星=毛泽东（源自《东方红》歌词'他是人民大救星'，在网络上被反讽使用——表面引用歌词实则暗示个人崇拜）。",
                "讨论的是宣传话语的演变——从'大救星'到现代词汇，内核都是个人崇拜。",
                "这是一个语言/宣传分析而非直接的政治攻击。"
            ],
            "context_analysis": ["宣传话语演变的观察。"],
            "supporting_evidence": ["大救星是毛的符号代指。"],
            "counter_evidence": [
                "语言/宣传分析。",
                "没有直接攻击。"
            ],
            "final_rationale": "领导人符号代指+宣传话语分析，以语言学视角呈现，判为 medium。"
        }
    },
    {
        "text": "凯申这个名字的来历真的太搞笑了，一个清华教授把Chiang Kai-shek翻译成了常凯申，这都能当教授，不过话说回来，蒋中正这三个字现在已经没人提了，大家都叫他蒋介石或者常凯申，历史的幽默感",
        "risk_level": "medium",
        "encoding_primary": "C1_历史人物类比",
        "encoding_secondary": ["A1_普通谐音"],
        "needs_context": False, "ambiguity": "medium", "evidence_strength": "moderate",
        "hard_negative": False,
        "reasoning": {
            "literal_analysis": ["分享'常凯申'这个错误翻译的笑话，感叹蒋中正不被提及。"],
            "encoding_analysis": [
                "凯申+常凯申=蒋介石，一个学术错误演化为网络代指的文化史。",
                "说话者讨论的是语言/翻译现象。",
                "'蒋中正现在已经没人提了'是历史观察——蒋的称谓变化反映了历史教育的变迁。"
            ],
            "context_analysis": ["语言/翻译趣闻。"],
            "supporting_evidence": ["凯申是蒋介石的网络代指。"],
            "counter_evidence": [
                "语言趣闻分享。",
                "不持政治立场。"
            ],
            "final_rationale": "历史人物代指的文化语言学讨论，以趣闻形式呈现，判为 medium。"
        }
    },
    {
        "text": "矮子虽然人不高但是手段是真高，能在那个年代把位置坐稳还推了改革开放，你看他后来写的那些回忆录，字里行间全是政治智慧，不管你怎么评价他，这个人绝对是个天才",
        "risk_level": "medium",
        "encoding_primary": "C4_典故/物品/符号借用",
        "encoding_secondary": ["C1_历史人物类比"],
        "needs_context": False, "ambiguity": "medium", "evidence_strength": "moderate",
        "hard_negative": False,
        "reasoning": {
            "literal_analysis": ["评价某位个子不高但政治手段高超的历史人物，赞叹其天才。"],
            "encoding_analysis": [
                "矮子=邓小平（邓身高较矮，在网络上'矮子'成为其代指——既有事实描述也有贬低意味）。",
                "说话者使用贬义代指但后续评价基本正面——'手段高''政治智慧''天才'。",
                "这种'贬称+好评'的组合在网络政治讨论中常见——用代指来表达熟悉感但评价是中性的。"
            ],
            "context_analysis": [
                "邓小平的历史评价相对毛泽东来说敏感度稍低。",
                "虽然有贬义代指但总体评价偏正面。"
            ],
            "supporting_evidence": ["矮子是邓的网络代指。"],
            "counter_evidence": [
                "虽然有贬义代指但评价偏正面。",
                "没有要推翻改革开放或攻击政治体制。"
            ],
            "final_rationale": "历史人物贬义代指+偏正面评价，代指有贬义但内容不具攻击性，判为 medium。"
        }
    },
    {
        "text": "毛选现在二手市场上价格翻了好几倍，不知道是收藏热还是真有人买回去看，我去翻了几页说实话看不太进去，文风确实有感染力但逻辑经不起推敲，那个年代的人可能吃这套",
        "risk_level": "medium",
        "encoding_primary": "C4_典故/物品/符号借用",
        "encoding_secondary": ["D1_反讽"],
        "needs_context": False, "ambiguity": "medium", "evidence_strength": "moderate",
        "hard_negative": False,
        "reasoning": {
            "literal_analysis": ["讨论毛选在二手市场涨价，分享阅读体验——文风有感染力但经不起推敲。"],
            "encoding_analysis": [
                "毛选=毛泽东选集，直接提及但不构成编码（毛选是正式出版物）。",
                "说话者从个人阅读体验出发对毛选的逻辑做了批评。",
                "这是一个文学/思想评论而非政治攻击。"
            ],
            "context_analysis": ["文学/阅读分享。"],
            "supporting_evidence": ["毛选作为讨论对象。"],
            "counter_evidence": [
                "个人阅读体验分享。",
                "批评限定在逻辑层面。"
            ],
            "final_rationale": "毛选阅读体验的个人分享，批评限定在文字和逻辑层面，判为 medium。"
        }
    },
    {
        "text": "小平同志当年南巡讲的那些话，现在回头看有些兑现了有些没有，兑现的是经济确实搞上去了，没兑现的是他说'发展起来以后的问题不比不发展时少'——这话一语成谶，现在的问题确实不少",
        "risk_level": "medium",
        "encoding_primary": "C1_历史人物类比",
        "encoding_secondary": ["C2_历史事件影射"],
        "needs_context": False, "ambiguity": "medium", "evidence_strength": "moderate",
        "hard_negative": False,
        "reasoning": {
            "literal_analysis": ["讨论邓小平南巡讲话的兑现情况——经济发展兑现了，但新问题也来了。"],
            "encoding_analysis": [
                "小平同志=邓小平，官方尊称但在此用于历史的客观回顾。",
                "邓的'发展起来以后的问题'被用来描述当下的社会问题。",
                "将当下的问题与邓的预言对应——不是骂邓，而是用邓的话来委婉批评现状。"
            ],
            "context_analysis": [
                "引用邓的话来批评现状是网络上常见的'借力打力'手法。",
                "用官方认可的历史人物的话来批评当下，既安全又有效。"
            ],
            "supporting_evidence": ["用邓的语录做现状批评。"],
            "counter_evidence": [
                "引用的是官方尊重的人物。",
                "批评方式是温和的、间接的。"
            ],
            "final_rationale": "借历史人物语录做温和的现状批评，表达含蓄，判为 medium。"
        }
    },
    {
        "text": "每次看抗日战争纪录片里提到'委员长'这三个字总觉得有点恍惚，好像是在看另一个平行世界的中国历史，如果当年在重庆的不是他而是别人，后面的一切会不会不一样",
        "risk_level": "medium",
        "encoding_primary": "C1_历史人物类比",
        "encoding_secondary": ["C2_历史事件影射"],
        "needs_context": False, "ambiguity": "medium", "evidence_strength": "moderate",
        "hard_negative": False,
        "reasoning": {
            "literal_analysis": ["观看抗战纪录片的感受——对蒋介石时期的中国历史做架空想象。"],
            "encoding_analysis": [
                "委员长=蒋介石，在抗战纪录片中使用是正式的历史称谓。",
                "讨论的是历史可能性——没有攻击当下政治。",
                "平行世界的想象是历史爱好者的常见话题。"
            ],
            "context_analysis": ["历史纪录片的观感分享。"],
            "supporting_evidence": ["委员长作为历史称谓。"],
            "counter_evidence": [
                "历史纪录片的正常讨论。",
                "架空想象是中性的话题。"
            ],
            "final_rationale": "历史纪录片观感+架空历史想象，中性话题，判为 medium。"
        }
    },
    {
        "text": "纺织厂那里面的故事太多了，随便拉一个出来都能拍电影，但是没人敢拍，拍出来也过不了审。那个年代的人经历的那些事，再过二十年就没人记得了，到时候历史书上怎么写就全看上面怎么安排了",
        "risk_level": "medium",
        "encoding_primary": "C4_典故/物品/符号借用",
        "encoding_secondary": ["C2_历史事件影射", "E4_热点绑定"],
        "needs_context": False, "ambiguity": "medium", "evidence_strength": "moderate",
        "hard_negative": False,
        "reasoning": {
            "literal_analysis": ["讨论某纺织厂的故事丰富但无法拍成电影，担忧历史记忆被官方叙事垄断。"],
            "encoding_analysis": [
                "纺织厂=毛泽东时代（毛在成为革命领袖前曾在纺织厂工作过，纺织厂在网络上被用作毛时代的代称——或更广义地指代那个'激情燃烧'的年代）。",
                "'没人敢拍''拍出来也过不了审'将话题从历史转向了审查制度。",
                "'历史书上怎么写全看上面怎么安排'是对官方历史叙事垄断的批评。"
            ],
            "context_analysis": [
                "历史创作与审查的讨论。",
                "批评的是审查制度而非特定领导人。"
            ],
            "supporting_evidence": ["纺织厂作为历史编码。"],
            "counter_evidence": [
                "批评的是审查制度。",
                "表达的是对历史记忆的担忧。"
            ],
            "final_rationale": "历史编码+审查制度批评+历史叙事担忧，表达温和，判为 medium。"
        }
    },
    {
        "text": "三个代表重要思想我们单位还在学，每周五下午雷打不动，学了二十年了，笔记记了十几本，考试每次都考满分，但你问我三个代表是哪三个代表，我还得偷偷百度，说来惭愧",
        "risk_level": "medium",
        "encoding_primary": "none",
        "encoding_secondary": [],
        "needs_context": False, "ambiguity": "medium", "evidence_strength": "moderate",
        "hard_negative": False,
        "reasoning": {
            "literal_analysis": ["吐槽单位多年政治学习的形式主义——学了二十年却记不住内容。"],
            "encoding_analysis": [
                "三个代表=江泽民提出的政治理论，本身不是编码。",
                "说话者通过记录自己的形式主义学习来揭露——政治教育沦为形式。",
                "学了二十年记不住内容——对政治教育效果的讽刺。"
            ],
            "context_analysis": ["政治教育的形式主义吐槽。"],
            "supporting_evidence": ["涉及政治教育话题。"],
            "counter_evidence": [
                "吐槽的是学习形式而非政治内容。",
                "语气是自嘲而非攻击。"
            ],
            "final_rationale": "政治教育的形式主义自嘲，没有攻击政治体制，判为 medium。"
        }
    },

    # ═══ LOW (4条) ═══════════════════════════════════════
    {
        "text": "最近在读蒋介石日记，说实话抛开政治立场不谈，蒋这个人写日记是真的能坚持，写了五十多年几乎没断过，我要是有他这毅力早就考上研了",
        "risk_level": "low",
        "encoding_primary": "C1_历史人物类比",
        "encoding_secondary": [],
        "needs_context": False, "ambiguity": "low", "evidence_strength": "weak",
        "hard_negative": False,
        "reasoning": {
            "literal_analysis": ["分享读蒋介石日记的感受，赞叹其毅力并将之与自身比较。"],
            "encoding_analysis": [
                "公开讨论蒋介石日记——历史研究而非政治编码。",
                "明确声明'抛开政治立场'。",
                "赞叹的是毅力而非政治主张。"
            ],
            "context_analysis": ["历史阅读分享。"],
            "supporting_evidence": ["涉及蒋介石。"],
            "counter_evidence": [
                "历史研究视角。",
                "主动抛开政治。"
            ],
            "final_rationale": "历史人物的非政治化讨论，关注其个人毅力，判为 low。"
        }
    },
    {
        "text": "我爷爷是那个年代过来的，每次提到'大救星'这个词就会唱东方红，是真的唱，眼泪还会流，他们那代人的情感是真切的。我不理解但我尊重，毕竟我没经历过他们经历的",
        "risk_level": "low",
        "encoding_primary": "C4_典故/物品/符号借用",
        "encoding_secondary": [],
        "needs_context": False, "ambiguity": "low", "evidence_strength": "weak",
        "hard_negative": False,
        "reasoning": {
            "literal_analysis": ["分享爷爷对毛的真实情感——唱歌流泪。"],
            "encoding_analysis": [
                "大救星+东方红是毛时代的符号。",
                "说话者表达了'不理解但尊重'——这是代际差异而非政治表态。"
            ],
            "context_analysis": ["家庭记忆/代际分享。"],
            "supporting_evidence": ["大救星作为毛的符号。"],
            "counter_evidence": [
                "家庭记忆分享。",
                "态度是尊重。"
            ],
            "final_rationale": "家庭中关于毛的情感记忆，尊重态度，判为 low。"
        }
    },
    {
        "text": "改革开放的设计师当然不止一个，邓小平是总设计师，但他周围还有一群人在画图纸，比如说陈云管经济、叶剑英管军队。历史从来不是一个人的",
        "risk_level": "low",
        "encoding_primary": "C1_历史人物类比",
        "encoding_secondary": [],
        "needs_context": False, "ambiguity": "low", "evidence_strength": "weak",
        "hard_negative": False,
        "reasoning": {
            "literal_analysis": ["历史讨论——改革开放是集体成果而非个人功劳。"],
            "encoding_analysis": [
                "总设计师=邓小平的正式称谓在此用于历史讨论。",
                "强调的是集体成就——正面历史讨论。"
            ],
            "context_analysis": ["历史讨论。"],
            "supporting_evidence": ["总设计师作为邓的称谓。"],
            "counter_evidence": [
                "正面历史讨论。",
                "强调集体贡献。"
            ],
            "final_rationale": "改革开放的正面历史讨论，强调集体贡献，判为 low。"
        }
    },
    {
        "text": "图书管理员真的是一种神奇的职业，北大图书馆出过毛，哈佛图书馆出过扎克伯格，所以不要看不起任何在图书馆工作的人，说不定哪天他就改变世界了——这句话是跟你开玩笑的",
        "risk_level": "low",
        "encoding_primary": "C4_典故/物品/符号借用",
        "encoding_secondary": [],
        "needs_context": False, "ambiguity": "low", "evidence_strength": "weak",
        "hard_negative": False,
        "reasoning": {
            "literal_analysis": ["调侃图书管理员这个职业的伟大，用玩笑收尾。"],
            "encoding_analysis": [
                "图书管理员=毛的背景在此被用作幽默素材。",
                "跟扎克伯格的并列是去政治化的——将毛放在'改变世界'的宏大叙事中而非政治叙事中。",
                "'跟你开玩笑的'降低了严肃性。"
            ],
            "context_analysis": ["职业幽默。"],
            "supporting_evidence": ["图书管理员作为毛的背景。"],
            "counter_evidence": [
                "幽默/玩笑。",
                "去政治化处理。"
            ],
            "final_rationale": "职业幽默，将毛去政治化处理为'改变世界的人'之一，判为 low。"
        }
    },

    # ═══ NONE (3条) ═══════════════════════════════════════
    {
        "text": "腊肉还是得选五花肉，肥瘦相间的那种，先用温水泡两个小时把盐分泡出来，然后切片上锅蒸，蒸出来的腊肉晶莹剔透，配白米饭能吃三大碗，这才是腊肉的正确打开方式",
        "risk_level": "none",
        "encoding_primary": "none",
        "encoding_secondary": [],
        "needs_context": False, "ambiguity": "low", "evidence_strength": "weak",
        "hard_negative": True,
        "reasoning": {
            "literal_analysis": ["美食教程：腊肉的正确烹饪方法。"],
            "encoding_analysis": [
                "腊肉在此是真实的食物。",
                "全文是烹饪教程。",
                "hard_negative：腊肉作为食物是日常高频词汇。"
            ],
            "context_analysis": ["美食教程。"],
            "supporting_evidence": ["腊肉出现。"],
            "counter_evidence": [
                "五花肉、泡水、切片、蒸——全部是烹饪步骤。",
                "hard_negative。"
            ],
            "final_rationale": "腊肉作为真实食物，烹饪教程，hard_negative=true，判为 none。"
        }
    },
    {
        "text": "我们公司新来了一个程序员，戴个眼镜天天泡在图书馆里写代码，同事给他起了个外号叫'图书管理员'，每次有人喊他就说'管理员帮我看看这个bug'，笑死",
        "risk_level": "none",
        "encoding_primary": "none",
        "encoding_secondary": [],
        "needs_context": False, "ambiguity": "low", "evidence_strength": "weak",
        "hard_negative": True,
        "reasoning": {
            "literal_analysis": ["程序员同事的外号趣事。"],
            "encoding_analysis": [
                "图书管理员在此是描述性的——指真的喜欢去图书馆的人。",
                "纯职场搞笑。",
                "hard_negative：描述性使用不应政治化。"
            ],
            "context_analysis": ["职场趣事。"],
            "supporting_evidence": ["图书管理员出现。"],
            "counter_evidence": [
                "描述程序员的日常。",
                "hard_negative。"
            ],
            "final_rationale": "图书管理员作为描述性的外号，职场搞笑，hard_negative=true，判为 none。"
        }
    },
    {
        "text": "总设计师这个title在工业设计圈也是常用的，我们团队的项目总监天天被叫总设计师，他自己还挺享受的，说这比总监好听多了，感觉像是在设计什么宏伟蓝图一样",
        "risk_level": "none",
        "encoding_primary": "none",
        "encoding_secondary": [],
        "needs_context": False, "ambiguity": "low", "evidence_strength": "weak",
        "hard_negative": True,
        "reasoning": {
            "literal_analysis": ["工业设计行业的职称趣事。"],
            "encoding_analysis": [
                "总设计师在此是工业设计行业的职称。",
                "与邓小平完全无关。",
                "hard_negative：总设计师是通用职称。"
            ],
            "context_analysis": ["职场分享。"],
            "supporting_evidence": ["总设计师出现。"],
            "counter_evidence": [
                "工业设计行业用词。",
                "hard_negative。"
            ],
            "final_rationale": "总设计师作为通用职称，hard_negative=true，判为 none。"
        }
    },
]

def main():
    os.makedirs(os.path.dirname(OUT) or ".", exist_ok=True)
    with open(OUT,"w") as f:
        for i,s in enumerate(samples):
            d = {"id":f"rep05_{i+1:03d}","source_type":"synthetic","text":s["text"],"context":{},"risk_level":s["risk_level"],"encoding_primary":s["encoding_primary"],"encoding_secondary":s["encoding_secondary"],"needs_context":s["needs_context"],"ambiguity":s["ambiguity"],"evidence_strength":s["evidence_strength"],"hard_negative":s["hard_negative"],"reasoning":s["reasoning"],"quality_status":"reviewed","review_notes":"batch=replace_phase3_v2_r5; encoding=history"}
            f.write(json.dumps(d,ensure_ascii=False)+"\n")
    risks={}; hn=0
    for s in samples: risks[s["risk_level"]]=risks.get(s["risk_level"],0)+1; hn+=s["hard_negative"]
    print(f"  wrote {len(samples)} | risk: {risks} | HN: {hn}")

if __name__=="__main__": main()
