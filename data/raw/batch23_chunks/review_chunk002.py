#!/usr/bin/env python3
"""Review chunk_002.jsonl - apply text-specific analysis to all 50 samples."""

import json

with open("chunk_002.jsonl", "r", encoding="utf-8") as f:
    lines = f.readlines()

samples = [json.loads(line) for line in lines]

corrections = {
    "002713": {
        "risk_level": "low",
        "encoding_primary": "none",
        "encoding_secondary": [],
        "needs_context": False,
        "ambiguity": "low",
        "evidence_strength": "weak",
        "hard_negative": True,
        "target_known": False,
        "reasoning": {
            "literal_analysis": [
                "文本表面在讨论外国媒体如何抹黑中国，提出'掌握媒体话语权的都喜欢抹黑别人'这一观点。使用了'外国'、'媒体话语权'、'抹黑'等词，整体是一种对外媒行为的分析性评论。",
                "文本中的'黑'是'抹黑/诋毁'的常规用法，非种族意义上的黑。叙述者站在被抹黑方的立场上进行反思。"
            ],
            "encoding_analysis": [
                "本段不存在编码机制。文本直接表达了对外国媒体行为的分析性看法，没有使用谐音、隐喻、反讽或平台黑话等任何编码手段。",
                "'抹黑'是中文中的常见动词用法（意为诋毁），并非种族/肤色意义上的编码表达。"
            ],
            "context_analysis": [
                "话题涉及国际媒体批评，属于 geopolitics/媒体批评范畴。文本本身是抽象分析，没有针对具体对象。",
                "没有足够上下文判断这条评论是回应什么具体事件，因此难以确定攻击性立场。"
            ],
            "supporting_evidence": [
                "1. 文本使用'想想外国怎么黑中国的'作为开场，这是邀请读者共同反思的姿态，而非攻击。",
                "2. '因为自己没啥优点只能用过抹黑别人来显得自己有优点'是对外媒动机的分析性推测。",
                "3. 整体语调是理性分析，没有侮辱性词汇或指向性攻击。"
            ],
            "counter_evidence": [
                "1. 文本的话题涉及'外国抹黑中国'这一敏感议题，可能被看作民族主义情绪表达，但缺乏具体攻击对象。",
                "2. 文本过于笼统，没有具体事件支撑，证据强度弱。"
            ],
            "final_rationale": "Risk: low。文本是对外媒抹黑行为的笼统分析，语调偏反思而非攻击，无具体指向的侮辱性内容，证据强度弱。"
        }
    },
    "002714": {
        "risk_level": "medium",
        "encoding_primary": "D1_反讽",
        "encoding_secondary": ["D3_借代"],
        "needs_context": False,
        "ambiguity": "low",
        "evidence_strength": "moderate",
        "hard_negative": False,
        "target_known": True,
        "reasoning": {
            "literal_analysis": [
                "文本列举了从2002年到2020年的一系列事件，指控江浙沪媒体/systematic 地针对山东进行负面报道。涉及'多宝鱼药物残留'、'青岛大虾事件'、'山大学伴事件'、'鲍毓明案'等具体事件。",
                "结尾连用三个反问句：'财经专家叶檀是哪里的？'、'骂一亿山东人不如z的大学生是宇宙省的'、'骂全国的许女是哪里的？'，用修辞性反问将矛头指向江浙沪地区。",
                "'宇宙省'是反讽性贬称，指某个自大的省份（通常指江苏/上海）。"
            ],
            "encoding_analysis": [
                "使用了D1反讽编码：结尾的三个反问句'XX是哪里的？'表面在提问，实际在指控——答案不言自明（都是江浙沪的），用修辞形式表达强烈的指责。",
                "使用了D3借代编码：用个别媒体/个人（叶檀、大学生、许女）的行为来借代整个江浙沪地区，将个体行为泛化为地区特征。"
            ],
            "context_analysis": [
                "文本是地域讨论中的辩护/反击型发言。叙述者通过列举'证据'来论证'江浙沪媒体系统黑山东'的论点。",
                "这种'举证+反问'的论证方式在网络地域争论中常见，以'事实堆砌'的形式包装攻击性。"
            ],
            "supporting_evidence": [
                "1. 文本详细列举了8个具体事件和时间点（2002、2015、2019、2020），表面上'摆事实'实际上在构建'江浙沪系统黑山东'的叙事。",
                "2. '宇宙省'这一明显带贬义的称呼说明叙述者已超出客观分析，转向地域攻击。",
                "3. 三个连续反问句的力度层层递进，具有明确的煽动性。"
            ],
            "counter_evidence": [
                "1. 文本列出的事件确实有公开报道，并非编造，可被解读为'揭露事实'而非'散布偏见'。",
                "2. 叙述者没有使用直接的地域侮辱词，而是通过事件列举来进行论证。"
            ],
            "final_rationale": "Risk: medium。文本通过反讽和借代编码，以'事件列举+反问'的方式对江浙沪地区进行系统性质疑和指责，攻击性中等但指向明确。"
        }
    },
    "002715": {
        "risk_level": "high",
        "encoding_primary": "D1_反讽",
        "encoding_secondary": ["literal_keyword"],
        "needs_context": False,
        "ambiguity": "low",
        "evidence_strength": "strong",
        "hard_negative": False,
        "target_known": True,
        "reasoning": {
            "literal_analysis": [
                "文本'生个小孩还是黑色的，放心吧'字面意思是生育的孩子皮肤仍是黑的，请对方放心。'黑色的'直接指代黑人肤色特征。",
                "'放心吧'（don't worry）是关键——使用了一种反讽式的安慰口吻，暗示'黑皮肤是不好的/需要担心的'，然后用'放心吧'来强化这一预设。",
                "这句话是对跨种族恋爱/婚姻的嘲讽，暗示中国人与黑人伴侣的孩子仍然会是黑皮肤（隐含着'这很糟糕但别担心还是黑色的'）。"
            ],
            "encoding_analysis": [
                "使用了D1反讽编码：'放心吧'的字面义是安慰，实际态度却截然相反——以安慰的口吻表达歧视性观点。这种'反向关怀'是典型的反讽手法。",
                "'黑色的'属于literal_keyword——直接援引肤色特征作为评判标准，没有经过语义包装。直接用肤色来判断一个人的价值/关系结果。"
            ],
            "context_analysis": [
                "在race_discussion话题下，这条评论无疑是在跨种族恋爱的讨论语境中发表的。文本虽短，但'黑色的'+'放心吧'的组合清晰地表达了种族偏见。"
            ],
            "supporting_evidence": [
                "1. '生个小孩还是黑色的'明确指向跨种族生育，以肤色遗传作为论点基础。",
                "2. '放心吧'的反讽用法表明叙述者认为黑皮肤是一种负面属性，需要被'安慰'。",
                "3. 整句没有提供任何具体论据，纯以种族特征为基础做出评价。"
            ],
            "counter_evidence": [
                "1. 文本较短且缺乏完整上下文，'放心吧'也可能是真安慰（如安慰担忧孩子肤色的父母），但这种解读在话题语境下极不自然。",
                "2. 没有使用直接侮辱词如'黑鬼'等，而是通过暗示表达偏见。"
            ],
            "final_rationale": "Risk: high。文本通过反讽编码以'安慰'口吻表达明确的种族偏见，将肤色作为负面评判标准，攻击性强且指向明确。"
        }
    },
    "002716": {
        "risk_level": "none",
        "encoding_primary": "none",
        "encoding_secondary": [],
        "needs_context": False,
        "ambiguity": "low",
        "evidence_strength": "strong",
        "hard_negative": True,
        "target_known": False,
        "reasoning": {
            "literal_analysis": [
                "文本'肤色是显性基因，遗传概率大'是一句关于遗传学的客观陈述。字面义：肤色由显性基因控制，在后代中遗传概率高。",
                "没有出现任何情感倾向词或攻击性表达，属于科普性事实陈述。"
            ],
            "encoding_analysis": [
                "不存在编码机制。这是对遗传学常识的直接、中性陈述，没有任何编码包装或隐含攻击。话题虽涉及race但内容完全是事实性的。"
            ],
            "context_analysis": [
                "在race_discussion话题下，这句话可能是在关于跨种族儿童肤色的讨论中作为事实补充出现。文本本身是中性的科学说明。"
            ],
            "supporting_evidence": [
                "1. '显性基因'、'遗传概率大'是标准的遗传学术语，不带任何情感色彩。",
                "2. 文本没有评价、没有指责、没有指向任何群体，纯粹是事实陈述。",
                "3. 长度短且没有修辞手法，是最简单的说明句。"
            ],
            "counter_evidence": [
                "1. 这句话可以被种族主义者用来论证'黑人特征会污染后代'，但文本本身不含这种立场。",
                "2. 仅凭文本本身，没有证据表明叙述者有任何恶意。"
            ],
            "final_rationale": "Risk: none (hard_negative)。文本是纯粹的遗传学事实陈述，没有任何攻击性、评价性或编码内容。"
        }
    },
    "002717": {
        "risk_level": "medium",
        "encoding_primary": "D1_反讽",
        "encoding_secondary": ["D3_借代"],
        "needs_context": False,
        "ambiguity": "low",
        "evidence_strength": "strong",
        "hard_negative": False,
        "target_known": True,
        "reasoning": {
            "literal_analysis": [
                "叙述者讲述与两个河南人的不愉快经历：一是河南商丘商会主席欠装修费不还却开豪车，二是另一河南客户给叙述者妻子发暧昧信息。结尾'声誉和荣誉都是自己辛苦赚来的'暗示这些个人经历说明了河南人整体的问题。",
                "关键修辞是两次重复的'你让我怎么说河南人？'——这是一个伪装的'无奈'姿态，实际上是将个人经历上升为地域定性。"
            ],
            "encoding_analysis": [
                "使用了D1反讽编码：'你让我怎么说河南人？'表面是无奈反问（'我能说什么呢？'），实际却是系统的地域指控——叙述者精心选择了两个负面案例来构建'河南人不可信'的叙事框架。",
                "使用了D3借代编码：用两个个体的行为借代整个河南人群体的道德品质。'声誉和荣誉都是自己辛苦赚来的'暗示河南人有损自己的声誉，将个体行为泛化到群体。"
            ],
            "context_analysis": [
                "这是典型的地域偏见建构文本：以'个人经历'为幌子，通过选择性报道来强化地域刻板印象。叙述者精心构建了'被迫形成负面看法'的叙事姿态。"
            ],
            "supporting_evidence": [
                "1. '你让我怎么说河南人？'出现了两次，不是真的在提问，而是在强调'我只能负面评价河南人'。",
                "2. 叙述者特意强调两个案例分别来自'商会主席'（应有声望的人）和'客户'（商业关系），增强'河南人不可信'的说服力。",
                "3. '声誉和荣誉都是自己辛苦赚来的'与五个感叹号一起，表面上中立，实际是最终定调：河南人应该为自己的声誉负责。"
            ],
            "counter_evidence": [
                "1. 叙述者确实是在报告个人实际经历，而非凭空捏造，有一定客观性基础。",
                "2. 文本末尾五感叹号的'声誉和荣誉都是自己辛苦赚来的'可被解读为谴责个别行为而非全体河南人。"
            ],
            "final_rationale": "Risk: medium。文本通过反讽编码以'无奈'姿态包装地域偏见，用个体案例借代群体，攻击性隐晦但指向明确的河南地域攻击。"
        }
    },
    "002718": {
        "risk_level": "medium",
        "encoding_primary": "literal_keyword",
        "encoding_secondary": [],
        "needs_context": False,
        "ambiguity": "low",
        "evidence_strength": "moderate",
        "hard_negative": False,
        "target_known": True,
        "reasoning": {
            "literal_analysis": [
                "文本'配得上，可以上，不可以结婚'由三个并列短语组成。'配得上'意为条件匹配、足够好；'可以上'是粗俗表达，意思是可以发生性关系；'不可以结婚'意为不适合结婚。",
                "在gender_discussion语境下，这是在评价一位女性的价值：性价值可接受但婚姻价值不合格。'可以上'是明确的物化表达。"
            ],
            "encoding_analysis": [
                "使用了literal_keyword——'可以上'是直接粗俗的性物化表达，没有经过编码包装。叙述者直接使用口语中的粗俗说法来评价女性。",
                "这不是比喻或反讽，而是直接的、物化女性的价值判断。三个短语形成递进：整体可接受→性可用→婚姻不可接受。"
            ],
            "context_analysis": [
                "在性别讨论话题下，这显然是对女性约会/择偶价值的评价。文本虽短但表述完整：女性被按'性'和'婚姻'两个维度划分价值。"
            ],
            "supporting_evidence": [
                "1. '可以上'是中文网络中对性行为的粗俗称呼，直接物化女性。",
                "2. 三个并列短语对一位女性的整体价值做切割评判：配做伴侣→可以有性→不能结婚。",
                "3. 这种'性能上但不能娶'的表述是性别物化的经典话术。"
            ],
            "counter_evidence": [
                "1. 文本极短（9个字），缺乏上下文。在非性别讨论语境下，可能指其他事物。",
                "2. 没有使用更极端的侮辱词（如'婊'等），程度相对较轻。"
            ],
            "final_rationale": "Risk: medium。文本通过直接物化表达（'可以上'）对女性进行性价值评判，攻击性明确但程度中等。"
        }
    },
    "002719": {
        "risk_level": "high",
        "encoding_primary": "E1_平台黑话",
        "encoding_secondary": ["C4_典故/物品/符号借用"],
        "needs_context": False,
        "ambiguity": "low",
        "evidence_strength": "strong",
        "hard_negative": False,
        "target_known": True,
        "reasoning": {
            "literal_analysis": [
                "文本提出'打拳'（女性主义/性别平权运动）是从韩国兴起的，然后质疑这是否是'网特'（网络特务/水军）利用'棒子'（对韩国人的贬称）事件的成功经验，在中国复制以破坏网络环境。",
                "关键攻击性词汇包括：'打拳'（对女性主义的贬称）、'棒子'（对韩国人的种族歧视称呼）、'网特'（网络特务/境外势力）。",
                "文本构建了一套阴谋论叙事：女性主义=韩国产物=境外势力破坏中国的手段=导致缺乏判断力的人盲目认同。"
            ],
            "encoding_analysis": [
                "使用了E1平台黑话编码：'打拳'是贴吧/微博对女性主义的特定贬称（谐音替换女'权'为'拳'头）；'网特'是网络民族主义黑话，指被境外势力雇用的网络水军。",
                "使用了C4典故/符号借用：'棒子'是对韩国人的历史贬称，在这里借用韩国作为'女性主义有害'的负面案例符号。"
            ],
            "context_analysis": [
                "在gender_discussion话题下，这是典型的反女性主义/反性别平权的阴谋论论述。叙述者试图将性别议题框架化为国家安全问题，通过'境外势力破坏网络环境'的叙事激化对立。"
            ],
            "supporting_evidence": [
                "1. '打拳'是贴吧/虎扑等社区的特定黑话，专用于贬低女性主义运动。",
                "2. '棒子事件'明确使用了对韩国人的种族贬称。",
                "3. '网特通过棒子事件的成功，而一样手法破坏我们的网络环境'构建了完整的'女性主义=境外势力阴谋'的阴谋论叙事。",
                "4. '导致有许多判断力低的人士盲目认同'直接贬低女性主义支持者的智力。"
            ],
            "counter_evidence": [
                "1. 文本后半段声明'以下是假设'，试图用假设语气降低其攻击性的直接性。",
                "2. '再这样下去只会破坏社会和谐'可被解读为对社会稳定的担忧而非攻击。"
            ],
            "final_rationale": "Risk: high。文本通过平台黑话和符号借用在性别话题下构建反女性主义阴谋论叙事，使用了对韩国人的贬称和'打拳'等编码黑话，攻击性强。"
        }
    },
    "002720": {
        "risk_level": "high",
        "encoding_primary": "literal_keyword",
        "encoding_secondary": [],
        "needs_context": False,
        "ambiguity": "low",
        "evidence_strength": "strong",
        "hard_negative": False,
        "target_known": True,
        "reasoning": {
            "literal_analysis": [
                "文本'全球所有国际鬼子虫类及其它们后代虫混精英'包含多重极端词汇。'鬼子'是历史上对外国侵略者（特别是日本人）的贬称；'虫类'将人比作虫子；'它们'使用代指动物的代词指代人；'虫混'将混血儿贬低为'虫子混合体'。",
                "叙述者声称这些人在全球监狱都有案底——以毫无根据的普遍化指控攻击特定群体。"
            ],
            "encoding_analysis": [
                "使用了literal_keyword——没有经过任何编码包装，直接使用了多个极端侮辱性和非人化的词汇：'鬼子'、'虫类'、'它们'、'虫混'。",
                "'鬼子'和'虫类'均为直接的侮辱性称呼，不依赖语境或修辞技巧来传达攻击性。'它们'用动物代词指代人类，是非人化( dehumanization )的典型手法。"
            ],
            "context_analysis": [
                "在race_discussion话题下，这段文字的攻击对象是'外国人和混血群体'。文本使用了极端非人化语言，属于种族主义言论中的'degendering/dehumanization'策略。"
            ],
            "supporting_evidence": [
                "1. '鬼子'是中文中对日本侵略者及广义外国人的经典贬称，历史侮辱性强。",
                "2. '虫类'和'虫混'将人类降级为昆虫，是极端的非人化修辞。",
                "3. '它们'使用动物/物体代词指代人类，在中文中极其冒犯。",
                "4. '在全球监狱都有不同案底档案'是对整个群体的无证据指控。"
            ],
            "counter_evidence": [
                "1. 文本语法不完整、表述混乱，可能反映了叙述者的教育水平较低而非系统的仇恨。",
                "2. 表达过于极端，可能被平台算法识别并删除，实际影响范围有限。"
            ],
            "final_rationale": "Risk: high。文本使用'鬼子''虫类''它们'等直接非人化侮辱词汇，不加编码包装地对特定群体进行极端种族攻击。"
        }
    },
    "002721": {
        "risk_level": "low",
        "encoding_primary": "none",
        "encoding_secondary": [],
        "needs_context": False,
        "ambiguity": "low",
        "evidence_strength": "moderate",
        "hard_negative": True,
        "target_known": True,
        "reasoning": {
            "literal_analysis": [
                "叙述者自称河南人，讲述了自己从'小心翼翼生怕给故乡招了黑'到'发现地域黑是西方资本控制的国内某些媒体刻意营造的舆论战争'的认知转变。",
                "文本的核心论点是：地域黑是外部势力分裂中国的工具。虽然包含阴谋论成分，但立场是反地域歧视、维护河南形象的。"
            ],
            "encoding_analysis": [
                "不存在编码机制。叙述者直接、坦诚地表达了自己的经历和观点，没有使用谐音、隐喻、反讽或平台黑话来包装攻击性。",
                "虽然存在'西方资本控制的国内某些媒体'等阴谋论表述，但这是观点表达而非编码攻击。"
            ],
            "context_analysis": [
                "在地域讨论话题下，这是一位河南人为自己省份辩护、分析地域黑根源的文本。虽然包含阴谋论，但其立场是反地域歧视的。",
                "'请自行脑补'暗示阅读者应自行联想近年来的国际舆论事件，这是一种常见的网络推论技巧但非编码。"
            ],
            "supporting_evidence": [
                "1. '土生外长的河南人'开篇确立了叙述者的地域身份认同。",
                "2. '以前也一直是恨铁不成钢，和外面的人打交道从来小心翼翼'表达了被歧视的切身感受。",
                "3. '各种迹象表明，地域黑是西方资本控制的国内某些媒体，刻意营造出来的'提出了一个解释框架来解释地域歧视的根源。"
            ],
            "counter_evidence": [
                "1. 文本中包含'西方资本控制国内媒体'的阴谋论，虽然其表面是反地域黑，但阴谋论本身也可能煽动对立。",
                "2. '从内部分裂、瓦解民族认同感的舆论战争'的表述具有强烈的民族主义煽动性。"
            ],
            "final_rationale": "Risk: low (hard_negative)。文本是一位河南人分析地域黑根源、为家乡辩护的反思性发言，立场反歧视，虽有阴谋论成分但非攻击性内容。"
        }
    },
    "002722": {
        "risk_level": "medium",
        "encoding_primary": "E1_平台黑话",
        "encoding_secondary": [],
        "needs_context": False,
        "ambiguity": "low",
        "evidence_strength": "moderate",
        "hard_negative": False,
        "target_known": True,
        "reasoning": {
            "literal_analysis": [
                "文本'感觉现在女性的择偶标准都是三无四有了啊'中的'三无四有'是一个网络流行梗。通常的三无四有变体包括'无房无车无存款，有车有房有存款有身高'等，讽刺女性择偶标准高且矛盾。",
                "'感觉...了啊'的语气带有一种表面随意实则抱怨的口吻。叙述者用这个梗来概括所有女性的择偶标准。"
            ],
            "encoding_analysis": [
                "使用了E1平台黑话编码：'三无四有'是中文互联网上的特定梗/流行语，用于讽刺女性物质化择偶标准。不在特定网络社区中，这个缩略语的意义不明确。",
                "这不是单纯的数字代指（C3），而是贴吧/微博等平台中流传的、具有特定贬义含义的格式化短语。"
            ],
            "context_analysis": [
                "在gender_discussion话题下，这是典型的性别择偶标准抱怨。叙述者用'trendy'的互联网梗来包装对女性的批评，使其显得更'有道理'（因为是流行说法）。"
            ],
            "supporting_evidence": [
                "1. '三无四有'是网络流行语，专用于讽刺女性在选择配偶时提出过高/矛盾的物质要求。",
                "2. '女性的择偶标准都是'中的'都是'使用了全称量词，将个别现象泛化为全部女性特征。",
                "3. 整体语气以'感觉'开头降低攻击性，但核心是在传播性别刻板印象。"
            ],
            "counter_evidence": [
                "1. '三无四有'在不同版本中有不同含义，可能只是中性描述（如'三无'指无不良嗜好等），文本简短不足以确定具体所指。",
                "2. 文本语气较为随意，可能只是无恶意的网络吐槽。"
            ],
            "final_rationale": "Risk: medium。文本通过平台黑话'三无四有'包装对女性择偶标准的刻板印象抱怨，攻击性中等且使用全称量词强化偏见。"
        }
    },
    "002723": {
        "risk_level": "none",
        "encoding_primary": "none",
        "encoding_secondary": [],
        "needs_context": False,
        "ambiguity": "low",
        "evidence_strength": "weak",
        "hard_negative": True,
        "target_known": False,
        "reasoning": {
            "literal_analysis": [
                "'勿谓言之不预'是中国外交场合的经典用语，意为'不要说我没有提前警告你'。'万事皆有可能'是常见口语表达，意为'一切皆有可能'。",
                "两个短语之间没有语法关联，是两段独立的格言式表述。没有指向任何具体对象。"
            ],
            "encoding_analysis": [
                "不存在编码机制。两段都是中文常见表达方式，没有使用任何编码手段包装隐含攻击。",
                "'勿谓言之不预'虽然在外交语境中具有警告意味，但在网络使用中已经成为一种梗/网络迷因，不必然指向种族话题。"
            ],
            "context_analysis": [
                "在race_discussion话题下，这两个短语可能是在某种论战中作为'放狠话'使用，但文本本身没有包含任何种族相关的内容或编码。",
                "缺乏上下文，无法判断这些短语是针对什么具体对象发表的。"
            ],
            "supporting_evidence": [
                "1. '勿谓言之不预'是中文常见的外交辞令/网络梗，没有种族指向性。",
                "2. '万事皆可能'是日常用语。",
                "3. 文本没有任何攻击性词汇、没有编码、没有指向性内容。"
            ],
            "counter_evidence": [
                "1. 在race_discussion话题下出现这些短语可能暗示警告的对象与种族话题有关，但文本本身没有体现。",
                "2. 两句之间无语法关联，反映了表达的不连贯性，难以做有意义的分析。"
            ],
            "final_rationale": "Risk: none (hard_negative)。文本是两个常见格言的拼接，无编码、无攻击对象、无攻击性内容。"
        }
    },
    "002724": {
        "risk_level": "high",
        "encoding_primary": "A2_拼音缩写",
        "encoding_secondary": ["literal_keyword"],
        "needs_context": False,
        "ambiguity": "low",
        "evidence_strength": "strong",
        "hard_negative": False,
        "target_known": True,
        "reasoning": {
            "literal_analysis": [
                "文本中'txl'是'同性恋'的拼音缩写。叙述者直接表示'感到txl恶心这没毛病啊'——明确声称对同性恋感到恶心'没有毛病'、是正当的。后半句'其实只要活好自己就行了'是一种'我不管你但你也不要影响我'的容忍姿态。",
                "关键的矛盾在于：前半句说'恶心同性恋没错'，后半句说'各过各的'——表面上装作宽容，但攻击性立场已经在前半句明确表达。"
            ],
            "encoding_analysis": [
                "使用了A2拼音缩写编码：'txl'是'同性恋'(tóng xìng liàn)的拼音首字母缩写，是中文网络中为规避平台审查或出于隐晦表达需要而使用的编码形式。",
                "'恶心'属于literal_keyword——直接使用'恶心'这一表达强烈厌恶的词汇来描述性少数群体，没有经过任何比喻或修饰。"
            ],
            "context_analysis": [
                "在lgbt_discussion话题下，这是典型的'排斥但声称包容'的恐同表达。前半句表达真实立场（恶心=正当），后半句进行表面修饰（各过各的）。"
            ],
            "supporting_evidence": [
                "1. '感到txl恶心这没毛病啊'是明确的恐同表达——'恶心'是最直接的反感表达，'没毛病'意味着叙述者认为这一立场合理正当。",
                "2. 'txl'是性少数话题中常见的缩写形式，用于指代同性恋群体。",
                "3. 后半句'txl的生活也不会因为你的喜好就改变的'表面理性，但无法掩盖前半句已经表达的强烈反感。"
            ],
            "counter_evidence": [
                "1. 后半句'活好自己就行了'体现了一定程度的'尊重彼此生活'态度，不完全排斥。",
                "2. 叙述者没有直接使用污名化称呼（如'基佬'等），使用'txl'缩写相对中性。"
            ],
            "final_rationale": "Risk: high。文本通过拼音缩写'txl'和直接使用'恶心'一词表达对同性恋群体的强烈排斥，攻击性强且编码可识别。"
        }
    },
    "002725": {
        "risk_level": "medium",
        "encoding_primary": "literal_keyword",
        "encoding_secondary": [],
        "needs_context": False,
        "ambiguity": "medium",
        "evidence_strength": "moderate",
        "hard_negative": False,
        "target_known": True,
        "reasoning": {
            "literal_analysis": [
                "文本'不止是黑人，白人也不行'字面义是'不仅黑人不行，白人也不行'。在race_discussion话题下，这大概率是在评断跨种族关系——某种关系/情况对黑人不适用，对白人也不适用。",
                "整句仅7个字，没有主语、没有说明'不行'的具体所指，需要上下文确定含义。"
            ],
            "encoding_analysis": [
                "使用了literal_keyword——直接以种族分类（'黑人'、'白人'）作为评判标准，没有通过隐喻、反讽等编码手段。",
                "'不行'是直接否定，但否定的是什么（交往、结婚、工作、还是其他？）不明确。这种模糊性本身可能是有意留白。"
            ],
            "context_analysis": [
                "在race_discussion话题下的讨论中，这句话95%以上的可能在讨论跨种族关系/联姻/移民。'不止是...也...'的结构是一种递进式否定。",
                "文本非常简短，缺乏主语和谓语对象，属于高度片段化的评论。"
            ],
            "supporting_evidence": [
                "1. '黑人'和'白人'直接将人按种族分类并统一否定。",
                "2. '不止是...也...'的结构排除了例外可能性，是一种全称否定。",
                "3. 在种族话题下，这种无条件的否定显然带有种族排斥倾向。"
            ],
            "counter_evidence": [
                "1. 文本没有主语和对象，无法确定'不行'的具体含义。",
                "2. 在特定上下文中，这可能是在讨论某种不涉及种族歧视但恰好以种族分类的政策/现象。",
                "3. 高度简短导致证据强度不足。"
            ],
            "final_rationale": "Risk: medium。文本以种族分类进行全称否定，但过短导致含义模糊，证据强度中等。"
        }
    },
    "002726": {
        "risk_level": "medium",
        "encoding_primary": "D1_反讽",
        "encoding_secondary": ["literal_keyword"],
        "needs_context": False,
        "ambiguity": "low",
        "evidence_strength": "strong",
        "hard_negative": False,
        "target_known": True,
        "reasoning": {
            "literal_analysis": [
                "文本表面上声称'支持她们找黑哥哥'，但随后的'物以类聚自动分类'彻底暴露了真实的贬义态度。'黑哥哥'是对黑人男性的口语化称呼，在这句中带有一丝轻佻。",
                "'物以类聚'（birds of a feather flock together）是中文成语，用于将某人归入低等/同类群体。在这里，叙述者将选择黑人伴侣的女性与黑人划为'同类'，暗示他们属于同一'档次'。"
            ],
            "encoding_analysis": [
                "使用了D1反讽编码：'其实我是支持她们找黑哥哥的'的表面意思是支持，但结合'物以类聚自动分类'，真实态度完全相反——表面支持实为贬低。反讽的张力在于'支持'与'物以类聚'之间的矛盾。",
                "'黑哥哥'属于literal_keyword——直接以黑人作为评价对象。'物以类聚'是一个带有价值判断的成语，将黑人与选择黑人的女性划入同一'低等类别'。"
            ],
            "context_analysis": [
                "在race_discussion话题下，这是针对跨种族恋爱（特别是中国女性与黑人男性交往）的讽刺评论。叙事手法是'先假装支持，后露出真面目'。"
            ],
            "supporting_evidence": [
                "1. '物以类聚自动分类'直接揭示了叙述者对中国女性与黑人交往的真实态度——认为她们和黑人是一路货色。",
                "2. '支持她们找黑哥哥'是典型的反讽铺垫，与后文形成强烈的态度反转。",
                "3. '黑哥哥'的称呼方式带有轻视和戏谑的意味。"
            ],
            "counter_evidence": [
                "1. '支持'一词确实出现在了字面上，理论上可被解释为真诚支持。",
                "2. '物以类聚'在某些语境下可以是中性描述。"
            ],
            "final_rationale": "Risk: medium。文本通过反讽编码（先'支持'后'物以类聚'）包装种族偏见，攻击性隐晦但指向明确，属间接种族歧视。"
        }
    },
    "002727": {
        "risk_level": "none",
        "encoding_primary": "none",
        "encoding_secondary": [],
        "needs_context": False,
        "ambiguity": "low",
        "evidence_strength": "strong",
        "hard_negative": True,
        "target_known": False,
        "reasoning": {
            "literal_analysis": [
                "文本'谢谢，今天挺开心的，听到你的话就更开心了'是一句完全正面的日常感谢和回应。叙述者今天本就开心，对方的言辞让其更加愉悦。",
                "没有任何异常词汇、攻击性表达或争议性内容，属于最普通的礼貌社交用语。"
            ],
            "encoding_analysis": [
                "不存在编码机制。文本是直接、真诚的表达愉快的日常用语，没有使用任何编码手段。",
                "没有谐音、隐喻、反讽或任何形式的修辞编码。"
            ],
            "context_analysis": [
                "在lgbt_discussion话题下，这句话可能是在回应某位LGBTQ人士的言论或对其表态。但文本本身没有任何与性取向、性别相关的内容，是完全中性的感谢表达。"
            ],
            "supporting_evidence": [
                "1. '谢谢'是标准的礼貌用语。",
                "2. '挺开心的'表达积极情绪。",
                "3. '听到你的话就更开心了'是对对方言论的积极反馈。",
                "4. 全文无任何攻击性、争议性词汇。"
            ],
            "counter_evidence": [
                "1. 在lgbt话题语境下，这句话可能有反讽意味（如讽刺性地感谢对方的出柜），但没有文本证据支持这一解读。"
            ],
            "final_rationale": "Risk: none (hard_negative)。文本是完全正面的日常感谢用语，无任何攻击性内容或编码。"
        }
    },
    "002728": {
        "risk_level": "low",
        "encoding_primary": "A1_谐音",
        "encoding_secondary": [],
        "needs_context": False,
        "ambiguity": "low",
        "evidence_strength": "moderate",
        "hard_negative": True,
        "target_known": True,
        "reasoning": {
            "literal_analysis": [
                "文本讨论了东三省简称'黑吉辽'的谐音误会。叙述者以为'黑辽一起黑吉林'——因为有人把'黑吉辽'理解为'黑及辽'（黑龙江和辽宁一起黑/抹黑吉林）。这里的'黑'有两种含义：作为省份简称（黑龙江）和作为动词（抹黑）。",
                "'黑吉辽'是黑龙江(黑)、吉林(吉)、辽宁(辽)的标准简称。同学误读为'黑及辽'（黑龙江及辽宁），从而产生了一个关于地域歧视的文字游戏。"
            ],
            "encoding_analysis": [
                "使用了A1谐音编码：'吉'(jí)与'及'(jí)同音但不同字，利用了读音相同但意义不同的谐音双关。这形成了'黑吉辽'→'黑及辽'的趣味重新解读。",
                "这不是真正的编码攻击，而是一个语言趣味观察：把省份简称的'黑'（黑龙江）重新解读为'抹黑'的动词，从而产生了一个玩笑式的'地域歧视发现'。"
            ],
            "context_analysis": [
                "这是一个基于文字游戏的轻松讨论，而非真正的攻击性地域歧视。叙述者在分享一个语言学习的趣味发现。虽涉及地域话题但完全不具攻击性。"
            ],
            "supporting_evidence": [
                "1. '我一直以为东三省里都是黑辽一起黑吉林'——这是对'黑吉辽'简称的一个语言上的趣味误读。",
                "2. '因为我们同学有人一直把黑吉辽理解为黑及辽'解释了误读的来源。",
                "3. 文本语调轻松，没有愤怒或指责的情绪。"
            ],
            "counter_evidence": [
                "1. 如果脱离谐音梗的语境，'黑辽一起黑吉林'可被误解为对吉林地区的实际抹黑行为。",
                "2. 在region话题下，涉及'地域黑'的主题本身敏感。"
            ],
            "final_rationale": "Risk: low (hard_negative)。文本是基于'黑吉辽'简称的谐音文字游戏，分享语言误读的趣味观察，无实际攻击性。"
        }
    },
    "002729": {
        "risk_level": "none",
        "encoding_primary": "none",
        "encoding_secondary": [],
        "needs_context": False,
        "ambiguity": "low",
        "evidence_strength": "weak",
        "hard_negative": True,
        "target_known": False,
        "reasoning": {
            "literal_analysis": [
                "文本'你的立场是基于笑话吗？'是一个疑问句，询问对方的立场/观点是否建立在笑话之上。这是一种质疑对方论点严肃性的反问。",
                "不含任何歧视性词汇、人身攻击或编码内容。"
            ],
            "encoding_analysis": [
                "不存在编码机制。这是一个直接的修辞性疑问句，没有使用谐音、隐喻、反讽或任何编码手段。",
                "'基于笑话'是一种修辞质疑，质疑对方的论据是否可靠，而非编码攻击。"
            ],
            "context_analysis": [
                "在race_discussion话题下，这条评论可能是在回应某个被认为荒谬/不严肃的种族话题观点。但文本本身没有种族指向，仅针对对方观点的逻辑性提出质疑。"
            ],
            "supporting_evidence": [
                "1. '你的立场'指向对话对方而非任何群体。",
                "2. '基于笑话'质疑的是论证方式而非身份特征。",
                "3. 没有使用任何攻击性词汇、侮辱或编码。",
                "4. 文本简短且温和，属于正常辩论交流。"
            ],
            "counter_evidence": [
                "1. 没有任何风险证据——这是一个普通的修辞性反问。"
            ],
            "final_rationale": "Risk: none (hard_negative)。文本是正常的辩论式反问，质疑对方观点的严肃性，无攻击性内容或编码。"
        }
    },
    "002730": {
        "risk_level": "high",
        "encoding_primary": "literal_keyword",
        "encoding_secondary": ["A2_拼音缩写"],
        "needs_context": False,
        "ambiguity": "low",
        "evidence_strength": "strong",
        "hard_negative": False,
        "target_known": True,
        "reasoning": {
            "literal_analysis": [
                "文本'ZG不接受阿难民是正确选择，一帮神棍'中，'ZG'是'中国'的缩写。叙述者支持中国不接受阿富汗难民，并将难民称为'一帮神棍'（a bunch of religious fanatics/charlatans）。",
                "'一帮'（a bunch of）是量化的贬低，'神棍'原指以宗教/迷信骗人的人，在这里用作对阿富汗难民（全部穆斯林）的宗教侮辱。"
            ],
            "encoding_analysis": [
                "使用了literal_keyword：'神棍'是直接的宗教侮辱性称呼，将阿富汗难民全盘贬低为宗教骗子/狂信徒，没有经过编码包装。",
                "使用了A2拼音缩写：'ZG'是'中国'(Zhōng Guó)的拼音首字母缩写。虽然'ZG'本身不一定是编码隐藏，但在敏感话题中经常被用来部分规避审查。"
            ],
            "context_analysis": [
                "在race_discussion话题下，这一评论涉及阿富汗难民与宗教（伊斯兰教）歧视。叙述者以支持中国政府难民政策为由头，直接攻击难民群体为'神棍'。"
            ],
            "supporting_evidence": [
                "1. '一帮神棍'将整个阿富汗难民群体贬低为宗教狂徒/骗子，是明确的群体攻击。",
                "2. '不接收就对了'表达了强硬的反难民立场。",
                "3. '正确选择'试图合理化排斥立场。",
                "4. 'ZG'缩写的使用可能是有意识的审查规避。"
            ],
            "counter_evidence": [
                "1. 在当前的国际舆论环境下，反对接收难民有一部分是基于国家利益和经济成本的合法讨论。",
                "2. '神棍'在某些语境下也可能仅指'利用宗教谋私的人'而非全面否定信仰。"
            ],
            "final_rationale": "Risk: high。文本使用直接的宗教侮辱词'神棍'攻击阿富汗难民群体，编码程度低但攻击性强且群体指向明确。"
        }
    },
    "002731": {
        "risk_level": "medium",
        "encoding_primary": "E1_平台黑话",
        "encoding_secondary": [],
        "needs_context": False,
        "ambiguity": "low",
        "evidence_strength": "moderate",
        "hard_negative": False,
        "target_known": True,
        "reasoning": {
            "literal_analysis": [
                "文本'因为电脑不会生孩子警告，也不会要这要那还说你坏话'将电脑（游戏/网络）与女性进行对比，称电脑优于女性。'生孩子警告'是核心词。",
                "'生孩子警告'是中文网络中的反女性主义黑话，用于嘲讽那些在讨论中引用生育经历/负担来支持自己论点的女性。叙述者说电脑不会发出'生孩子警告'——意即女性会。"
            ],
            "encoding_analysis": [
                "使用了E1平台黑话编码：'生孩子警告'是贴吧/虎扑/知乎等社区中流传的特定黑话，用于贬低女性基于生育经历的发言。该短语在平台内部有特定的贬义用法，脱离社区语境则意义不明。",
                "'要这要那还说你坏话'是对女性伴侣的刻板印象描述（物质要求+唠叨）。整体表述直接但核心攻击是通过平台黑话实现的。"
            ],
            "context_analysis": [
                "在gender_discussion话题下，这是常见的'女性不如游戏/电脑'的厌女表达。叙述者通过将女性简化为'生孩子警告+物质要求+唠叨'的刻板印象来论证电脑/游戏更好。"
            ],
            "supporting_evidence": [
                "1. '生孩子警告'是已知的性别话题黑话，专用于贬低女性在讨论生育问题时的发言。",
                "2. '要这要那'刻板化女性为物质索取者。",
                "3. '说你坏话'刻板化女性为爱抱怨/爱唠叨。",
                "4. 对比结构（电脑不会...但女性会...）明确贬低女性。"
            ],
            "counter_evidence": [
                "1. 文本可能只是对特定网络现象的吐槽而非整体敌视女性。",
                "2. 叙述者没有使用极端的侮辱性词汇（如'婊'等）。"
            ],
            "final_rationale": "Risk: medium。文本通过平台黑话'生孩子警告'和刻板印象描述表达厌女态度，攻击性隐晦但通过编码可识别。"
        }
    },
    "002732": {
        "risk_level": "low",
        "encoding_primary": "none",
        "encoding_secondary": [],
        "needs_context": False,
        "ambiguity": "low",
        "evidence_strength": "moderate",
        "hard_negative": True,
        "target_known": True,
        "reasoning": {
            "literal_analysis": [
                "这是一段详细的个人经历分享：叙述者（黑龙江人）在江西上学，室友（唐山人）因'唐山打人事件'被江西室友地域歧视。叙述者描述了自己为唐山室友打抱不平的经历。",
                "文本中的地域攻击来自叙述者转述的江西室友（'等你回家之后给我拍照让我看下黑社会什么样子'），而非叙述者本人。叙述者明确表示'特别无语，给他一顿怼'。"
            ],
            "encoding_analysis": [
                "不存在编码机制。这是直接的、叙述性的个人经历分享。叙述者采用了时间顺序的叙事结构（从室友成为朋友到被歧视再到反击），没有使用任何编码手段。",
                "文本中引用的歧视性言论（'黑社会什么样子'、截图发群）是转述他人的行为，而非叙述者本人的编码攻击。"
            ],
            "context_analysis": [
                "在region_reporting话题下，这是一篇地域歧视的亲身经历报告。叙述者的立场是反地域歧视的，他不仅没有参与歧视，还为受害者辩护。",
                "结尾'东北受到的地域黑相当多，所以就感同身受'进一步表明叙述者因自身经历而对地域歧视敏感。"
            ],
            "supporting_evidence": [
                "1. '给他一顿怼'表明叙述者主动为被歧视的室友辩护。",
                "2. '真就特别无语'表达了叙述者对地域歧视行为的反感。",
                "3. '东北受到的地域黑相当多，所以就感同身受'提供了叙述者理解地域歧视的个人背景。",
                "4. 整篇文本的叙事立场是站在反歧视一侧。"
            ],
            "counter_evidence": [
                "1. 文本中包含了对江西室友行为的具体描述（'故意恶心'、截图发群），但这是转述而非叙述者本人在攻击。",
                "2. 如果脱离上下文阅读，'等我回家之后给我拍照让我看下黑社会什么样子'这句话本身是歧视性的。"
            ],
            "final_rationale": "Risk: low (hard_negative)。文本是以反地域歧视立场撰写的个人经历分享，叙述者本人在为受害者辩护，非攻击性内容。"
        }
    },
    "002733": {
        "risk_level": "none",
        "encoding_primary": "none",
        "encoding_secondary": [],
        "needs_context": False,
        "ambiguity": "low",
        "evidence_strength": "weak",
        "hard_negative": True,
        "target_known": False,
        "reasoning": {
            "literal_analysis": [
                "文本'今年冬天会不会没暖气哈？！🤭'是一个关于冬季供暖的疑问句。'暖气'指冬季集中供暖系统。叙者使用🤭（捂嘴笑）表情，语气调皮。",
                "这可能是在开玩笑地担心供暖问题，或者是暗示某个地区的供暖政策变化。没有包含任何攻击性内容。"
            ],
            "encoding_analysis": [
                "不存在编码机制。这是一个关于供暖的日常疑问，没有使用任何编码手段。",
                "🤭表情表达的是半开玩笑的语气，不是编码攻击。"
            ],
            "context_analysis": [
                "在region_discussion话题下，这可能涉及中国南北供暖差异的讨论，或针对某些地区的供暖政策进行调侃。但文本本身没有明确指向。",
                "缺乏上下文，无法确定是否在暗指某个特定地区的供暖问题。"
            ],
            "supporting_evidence": [
                "1. '暖气'是冬季供暖系统的日常用词，没有特殊含义。",
                "2. 文本以问句形式表达，语气轻松。",
                "3. 🤭表情显示叙述者是在半开玩笑。",
                "4. 没有针对任何群体的攻击性词汇。"
            ],
            "counter_evidence": [
                "1. 在region话题下，供暖问题是南北差异讨论中的常见话题，可能隐含对南方无集中供暖的抱怨。",
                "2. 文本非常简短，缺乏揭示真实意图的上下文线索。"
            ],
            "final_rationale": "Risk: none (hard_negative)。文本是关于供暖的日常玩笑式提问，无攻击性内容或编码。"
        }
    },
    "002734": {
        "risk_level": "none",
        "encoding_primary": "none",
        "encoding_secondary": [],
        "needs_context": False,
        "ambiguity": "low",
        "evidence_strength": "weak",
        "hard_negative": True,
        "target_known": False,
        "reasoning": {
            "literal_analysis": [
                "文本'汉弗莱:...甚至不能一棒子打死😜'中的'汉弗莱'是英剧Yes Minister（《是，大臣》）中的经典角色Humphrey Appleby。'一棒子打死'是中文成语，意为彻底否定/打倒。😜是吐舌头的调皮表情。",
                "文本引用了一个英剧角色名作为说话者，这很可能是在玩Yes Minister中的梗，借用Humphrey的语言风格来说某事。"
            ],
            "encoding_analysis": [
                "不存在编码机制。'汉弗莱'是一个直接的文化引用（英剧角色），'一棒子打死'是常见成语。没有使用攻击性编码手段。",
                "😜表情表明这是一个轻松的表达，而非严肃或攻击性陈述。"
            ],
            "context_analysis": [
                "在race_discussion话题下，这句话可能是在讨论种族话题时引用的幽默评论。'汉弗莱'角色在剧中以官僚辞令著称，引用他的话可能是在讽刺某种'political correctness'。",
                "文化引用本身不构成攻击，但需要了解Yes Minister的背景才能完全理解。"
            ],
            "supporting_evidence": [
                "1. '汉弗莱'明确指向英剧角色，是文化引用而非攻击。",
                "2. '一棒子打死'是常见成语，意为全盘否定。",
                "3. 😜表情显示叙述者是在开玩笑。",
                "4. 没有种族指向性词汇。"
            ],
            "counter_evidence": [
                "1. 在race话题下，'一棒子打死'可能与'种族歧视不可一棒子打死'等讨论相关。",
                "2. 没有完整上下文，无法判断引用汉弗莱的意图。"
            ],
            "final_rationale": "Risk: none (hard_negative)。文本是英剧角色的文化引用搭配成语表达，语气轻松无攻击性。"
        }
    },
    "002735": {
        "risk_level": "high",
        "encoding_primary": "literal_keyword",
        "encoding_secondary": [],
        "needs_context": False,
        "ambiguity": "low",
        "evidence_strength": "strong",
        "hard_negative": False,
        "target_known": True,
        "reasoning": {
            "literal_analysis": [
                "文本'找完黑人男朋友记得去非洲，别回来'是对选择了黑人伴侣的人的直接驱逐令。'记得去非洲，别回来'意为'你应该离开中国去非洲，永远不要回来'。",
                "这句话的预设是：与黑人交往就应当离开中国，因为已经不配留在中国。这是一种基于种族隔离思想的人身驱逐。"
            ],
            "encoding_analysis": [
                "使用了literal_keyword——文本直接以种族（'黑人男朋友'）为理由，对他人下达驱逐指令。没有使用任何编码包装。",
                "'记得去非洲'的'记得'带有讽刺性的'善意提醒'口吻，但核心是直接的种族排斥。'别回来'是最终定论，语气决绝。"
            ],
            "context_analysis": [
                "在race_discussion话题下，这是针对跨种族恋爱的极端种族主义反应。叙述者认为中国人与黑人交往就应该被逐出国家，反映了'种族纯洁'思想。"
            ],
            "supporting_evidence": [
                "1. '找完黑人男朋友'明确以伴侣的种族身份为由进行攻击。",
                "2. '去非洲'是将黑人与非洲单一关联，本质是种族隔离思维。",
                "3. '别回来'是驱逐指令，认为与黑人交往的人不再被国家接受。",
                "4. 文本虽短但威胁性和排斥性极强。"
            ],
            "counter_evidence": [
                "1. 文本极端简短，缺乏完整对话上下文。",
                "2. 可能是在具体辩论中的情绪化回应而非系统性种族主义。"
            ],
            "final_rationale": "Risk: high。文本直接以种族为由对他人发出驱逐指令（'去非洲，别回来'），属于直接和极端的种族排斥言论。"
        }
    },
    "002736": {
        "risk_level": "low",
        "encoding_primary": "none",
        "encoding_secondary": [],
        "needs_context": False,
        "ambiguity": "medium",
        "evidence_strength": "weak",
        "hard_negative": True,
        "target_known": False,
        "reasoning": {
            "literal_analysis": [
                "文本'你是不是很少被人喜欢，所以随便什么人喜欢你，你都觉得值得高兴？'是对对方心理状态的分析性质疑。叙述者推测对方因为缺乏被人喜欢的经历，所以对任何人的喜欢都过于珍视。",
                "这是一种人身攻击（ad hominem），攻击对方在情感上的'饥不择食'，但并非基于身份特征的歧视。"
            ],
            "encoding_analysis": [
                "不存在编码机制。这是一个直接的（尽管刻薄的）心理分析式人身攻击，没有使用谐音、隐喻、反讽等编码手段。",
                "这种'你之所以XX是因为你缺爱'的论证方式是一种常见的人身攻击话术（genetic fallacy），但这不是编码，而是直接的修辞策略。"
            ],
            "context_analysis": [
                "在lgbt_discussion话题下，这句话可能是在回应某人对同性感情的珍视——叙述者将对方的珍视归因于'因缺爱而饥不择食'，是一种隐性的贬低。",
                "虽然也许隐含了对LGBTQ感情的轻视，但文本本身是对个人心理的猜测而非对群体的攻击。"
            ],
            "supporting_evidence": [
                "1. '很少被人喜欢'是对对方社交状态的贬低性猜测。",
                "2. '随便什么人喜欢你'是将对方感情贬低为'随便'。",
                "3. '你都觉得值得高兴'再次贬低了对方的情感判断力。"
            ],
            "counter_evidence": [
                "1. 文本攻击的是个人的情感状态而非任何群体的身份特征（如性取向）。",
                "2. 这是一种辩论中常见的人身攻击话术，但不等于系统性歧视。",
                "3. 没有使用任何歧视性词汇或编码。"
            ],
            "final_rationale": "Risk: low (hard_negative)。文本是人身攻击性辩论话术，攻击个人心理状态而非群体身份特征，无编码机制。"
        }
    },
    "002737": {
        "risk_level": "low",
        "encoding_primary": "none",
        "encoding_secondary": [],
        "needs_context": True,
        "ambiguity": "high",
        "evidence_strength": "weak",
        "hard_negative": True,
        "target_known": False,
        "reasoning": {
            "literal_analysis": [
                "文本'我直接承认我不是男人'字面义是承认自己不是男性。在gender_discussion语境下，可能是在回应某种'你不是男人/真男人'的指责——叙述者以反讽的方式'就范'。",
                "也可能是一个自嘲/自我认同的表达（如跨性别），或是对'男子气概'社会建构的幽默回应。"
            ],
            "encoding_analysis": [
                "不存在明确编码机制。这是一个简短且高度依赖上下文的声明。可以解读为反讽（如果回应'你不是男人'的指责）、自嘲、或简单的身份声明。",
                "'不是男人'在中文中可以是字面否定，也可以是对'男子气概'标准的拒绝。"
            ],
            "context_analysis": [
                "在gender_discussion话题下，这段文字高度依赖上下文。可能的解读包括：反讽回应（别人说'你不是男人'→'好吧我不是'）、性别认同表达、或对toxic masculinity的讽刺。",
                "文本过于简短且缺乏上下文，无法做出任何确定的判断。"
            ],
            "supporting_evidence": [
                "1. '直接承认'有一种'好吧我认了'的无奈或反讽感。",
                "2. 文本短且没有其他线索来确认真实意图。"
            ],
            "counter_evidence": [
                "1. 文本可能仅仅是自嘲或身份表达，不含攻击性。",
                "2. 没有针对任何人的攻击或贬低。",
                "3. 任何攻击性解读都需要外加语境才能成立。"
            ],
            "final_rationale": "Risk: low (hard_negative)。文本极短且高度歧义，依赖上下文解读，无明确攻击性证据。"
        }
    },
    "002738": {
        "risk_level": "medium",
        "encoding_primary": "E1_平台黑话",
        "encoding_secondary": ["literal_keyword"],
        "needs_context": False,
        "ambiguity": "low",
        "evidence_strength": "strong",
        "hard_negative": False,
        "target_known": True,
        "reasoning": {
            "literal_analysis": [
                "文本开头引用'物以类聚，人以群分'，声称不同群体不需要过多联系。然后将矛头指向'那些撑同的人尤其是女性'——'撑同'是网络用语，意为'支持同性恋'。",
                "叙述者认为LGBTQ支持者（特别是女性）'就是站着说话不腰疼'（have no skin in the game / easy for them to say），并宣称他们'不可能真正的公正看待'。"
            ],
            "encoding_analysis": [
                "使用了E1平台黑话编码：'撑同'是中文网络中对'支持同性恋'的缩略表达，在特定社区中用于指代LGBTQ支持者群体。",
                "使用了literal_keyword：'站着说话不腰疼'是直接的对LGBTQ支持者的轻蔑定性——认为他们没有资格参与讨论。'不可能真正的公正看待'直接否定支持者的理性能力。"
            ],
            "context_analysis": [
                "在lgbt_discussion话题下，这是反LGBTQ立场的典型论证策略：先划分'我们和他们'，然后质疑支持者的动机和能力。将女性支持者单独拎出进一步分裂LGBTQ联盟。"
            ],
            "supporting_evidence": [
                "1. '撑同'明确指代'支持同性恋'的群体，是话题核心。",
                "2. '站着说话不腰疼'全盘否定LGBTQ支持者的参与资格和同理心。",
                "3. '尤其是女性'将女性LGBTQ支持者作为特别的攻击目标。",
                "4. '不可能真正的公正看待'直接否定对方的理性判断能力。"
            ],
            "counter_evidence": [
                "1. 文本以'物以类聚，人以群分'开头，表达了一种保守的'各玩各的'观点而非直接仇恨。",
                "2. '觉得'和'我想'表明叙述者是在表达个人看法。"
            ],
            "final_rationale": "Risk: medium。文本通过平台黑话'撑同'和直接否定（'站着说话不腰疼'）表达反LGBTQ立场，攻击性中等但群体指向明确。"
        }
    },
    "002739": {
        "risk_level": "none",
        "encoding_primary": "none",
        "encoding_secondary": [],
        "needs_context": False,
        "ambiguity": "low",
        "evidence_strength": "strong",
        "hard_negative": True,
        "target_known": True,
        "reasoning": {
            "literal_analysis": [
                "叙述者（黑龙江人）为黑龙江进行经济辩护，反驳对方对黑龙江的负面评价。通过对比黑龙江与辽宁的经济数据（工资水平、国企状况），论证黑龙江并非不如辽宁。",
                "结尾'原本觉得你这人挺实在的，结果扛着枪窝里横，真让我小看你了'是对原评论者个人的批评（窝里横=对自己人横），而非地域攻击。"
            ],
            "encoding_analysis": [
                "不存在编码机制。文本是直接的经济论点辩论，采用了数据对比（工资、国企）和实事求是的分析语调。",
                "'扛着枪窝里横'是对个人行为的批评（在东北内部搞内斗），不是编码攻击。"
            ],
            "context_analysis": [
                "在region_discussion话题下，这是一段东北内部（黑龙江vs辽宁）的经济辩论。叙述者以数据为武器为自己的家乡辩护，立场是反地域歧视/反地域比较的。"
            ],
            "supporting_evidence": [
                "1. '我就是黑龙江人'明确的身份声明。",
                "2. '都是东北人你这么说黑龙江'指出对方是在同一大区域内部分化。",
                "3. 文本以经济数据（工资、企业状况）为论据进行实质性辩论。",
                "4. '扛着枪窝里横'批评的是个人行为而非地域群体。"
            ],
            "counter_evidence": [
                "1. 结尾带有个人攻击色彩（'真让我小看你了'），但这是个人对个人的不满，非地域攻击。"
            ],
            "final_rationale": "Risk: none (hard_negative)。文本是东北区域内部的经济辩论，叙述者以数据和事实为家乡辩护，无地域攻击性。"
        }
    },
    "002740": {
        "risk_level": "high",
        "encoding_primary": "C4_典故/物品/符号借用",
        "encoding_secondary": ["literal_keyword"],
        "needs_context": False,
        "ambiguity": "low",
        "evidence_strength": "strong",
        "hard_negative": False,
        "target_known": True,
        "reasoning": {
            "literal_analysis": [
                "文本第一部分贬低宗教和神学（'神学学位算个鸟，迷信和宗教在中国人看来就是个屁'），使用了粗俗的直接贬低。",
                "关键在第二句'你让马丁路德金去考一考数学试试'——MLK是著名的美国黑人民权领袖。通过让MLK考数学，叙述者借用了种族刻板印象（黑人数学不好/智力不足）来攻击MLK。"
            ],
            "encoding_analysis": [
                "使用了C4典故/符号借用编码：马丁路德金（Martin Luther King Jr.）作为黑人/民权运动的符号，被借用来传达种族智力刻板印象。MLK本人与数学能力无关，选择MLK是因为他的黑人身份，这是一个通过'文化符号'进行种族贬低的手法。",
                "使用了literal_keyword：'算个鸟'、'就是个屁'是直接粗俗的贬低表达（针对宗教而非种族），但真正的种族攻击是通过MLK的典故编码实现的。"
            ],
            "context_analysis": [
                "在race_discussion话题下，引用MLK来讨论数学能力明显带有种族智力刻板印象。选择MLK而非其他学者/名人是刻意的——利用MLK的黑人身份来暗示'黑人数学能力差'的偏见。"
            ],
            "supporting_evidence": [
                "1. '你让马丁路德金去考一考数学试试'——MLK作为历史人物以民权运动而非数学著称，专门要求他考数学暗示黑人智力不足。",
                "2. '试试'的语气带有挑衅和轻蔑。",
                "3. 前文的神学贬低为后续的种族攻击做了铺垫（神学=迷信=黑人的东西）。"
            ],
            "counter_evidence": [
                "1. 文本的主要攻击对象是'宗教/神学'而非特定种族。MLK的引用可能只是为了找一位知名的宗教人物。",
                "2. '数学'可能只是指MLK的受教育领域（神学而非STEM）的体现，不一定涉及种族智力论。"
            ],
            "final_rationale": "Risk: high。文本通过借用马丁路德金作为种族符号，隐晦地传递黑人智力不足的种族刻板印象，编码手段精妙且攻击性强。"
        }
    },
    "002741": {
        "risk_level": "high",
        "encoding_primary": "E1_平台黑话",
        "encoding_secondary": ["literal_keyword"],
        "needs_context": False,
        "ambiguity": "low",
        "evidence_strength": "strong",
        "hard_negative": False,
        "target_known": True,
        "reasoning": {
            "literal_analysis": [
                "文本包含多个极端厌女和排外言论。'非处'侮辱非处女女性；'现在哪有处女啊？幼儿园找去吧？'是最低劣的性别攻击；'在荷兰出差的时候.我们国家的妹子.简直就是公交车'将中国女性比作人人可上的公共汽车；'回来就镀金B了'以最粗鄙的方式侮辱出国后回国女性的生殖器。",
                "整段话融合了处女情结、厌女、种族歧视（外国人随便睡中国女性）和恶心的性侮辱词汇。"
            ],
            "encoding_analysis": [
                "使用了E1平台黑话编码：'公交车'是中文网络中用于侮辱滥交女性的特定黑话（人人可上的公共汽车）；'镀金B'是特定的极端侮辱性表达。",
                "使用了literal_keyword：'非处'、'幼儿园找处女'、'恶心'等均为直接的侮辱性表达。文本整体编码程度低，大量使用直接的粗鄙辱骂。"
            ],
            "context_analysis": [
                "在gender_discussion话题下，这是极端的性别歧视和厌女表达。叙述者将中国女性划分为'处女/非处女'和'国内女性/出国女性'两个维度进行侮辱，并融合了种族自卑/仇外情绪。"
            ],
            "supporting_evidence": [
                "1. '非处'直接侮辱非处女女性。",
                "2. '现在哪有处女啊？幼儿园找去吧？'是最恶毒的女性性侮辱。",
                "3. '我们国家的妹子.简直就是公交车'将中国女性全体比作公共性工具。",
                "4. '回来就镀金B了.简直恶心'以生殖器侮辱为核心，表达对外国关系女性的仇恨。"
            ],
            "counter_evidence": [
                "1. 叙述者的表达极其粗鄙，可能反映了较低的教育水平而非系统的意识形态。",
                "2. 文本语法混乱、标点随意，可能是在情绪激动下发表的失控言论。"
            ],
            "final_rationale": "Risk: high。文本融合多重直接侮辱（'非处''公交车''镀金B'）对女性进行极端性别攻击，编码程度低但攻击性极强。"
        }
    },
    "002742": {
        "risk_level": "low",
        "encoding_primary": "none",
        "encoding_secondary": [],
        "needs_context": False,
        "ambiguity": "low",
        "evidence_strength": "moderate",
        "hard_negative": True,
        "target_known": True,
        "reasoning": {
            "literal_analysis": [
                "文本提及小品演员巩汉林在央视春晚上的一个'开地图炮'（地域歧视性）表演，称其'打开了潘多拉魔盒'——开启了地域歧视的潮流。讽刺的是，'受害最严重是他自己老家'（巩汉林是辽宁人，而东北地区成了地域黑的主要目标之一）。",
                "这是一段对地域歧视现象的幽默/讽刺式分析，而非实际的歧视性攻击。"
            ],
            "encoding_analysis": [
                "不存在编码机制。文本是对地域歧视历史的一个直接评论，使用了'潘多拉魔盒'典故（西方神话比喻）和'开地图炮'（网络用语，意为搞地域攻击）。",
                "'开地图炮'虽然是网络用语，但在这里是作为引用/分析对象而非编码攻击手段。"
            ],
            "context_analysis": [
                "在region_reporting话题下，这是对地域歧视现象的元评论（meta-commentary）。叙述者站在观察者/分析者的角度讨论地域歧视的起源和讽刺性结果。",
                "文本本身没有进行地域攻击，而是在分析地域歧视现象的历史起点。"
            ],
            "supporting_evidence": [
                "1. '巩汉林在春晚上开地图炮'指出了具体的历史事件（2009年小品《不差钱》中关于东北/苏格兰裙的梗）。",
                "2. '就打开了潘多拉魔盒'用比喻分析这一表演的影响。",
                "3. '受害最严重是他自己老家'指出了讽刺性结果。",
                "4. 文本是宏观分析而非微观攻击。"
            ],
            "counter_evidence": [
                "1. '开地图炮'这个表述本身涉及地域话题，可能被误解为攻击。",
                "2. 😅表情显示叙述者觉得这有些好笑，可能被认为不够严肃。"
            ],
            "final_rationale": "Risk: low (hard_negative)。文本是对地域歧视现象的幽默历史分析，立场是观察/反思而非攻击。"
        }
    },
    "002743": {
        "risk_level": "medium",
        "encoding_primary": "none",
        "encoding_secondary": [],
        "needs_context": False,
        "ambiguity": "low",
        "evidence_strength": "moderate",
        "hard_negative": False,
        "target_known": True,
        "reasoning": {
            "literal_analysis": [
                "叙述者以长辈口吻（'因为你还小'）开篇，提出'黑不可能无缘无故的黑，肯定是存在问题的'——声称地域歧视必然事出有因。用了一个关于河南人的个人轶事（'我那个时候认识的河南人那样，他自己把自己村里那帮人骂了个底朝天'）来论证'问题出在群体内部'。",
                "最后结论'其实做好自己，黑的人会越来越少'表面上积极，但前提是'问题确实存在'——等于承认/合理化地域歧视的正当性。"
            ],
            "encoding_analysis": [
                "不存在编码机制。文本是直接的观点论述，没有使用隐喻、反讽或平台黑话。叙述者采取了'客观/理性'的口吻来表达'地域黑有原因'的立场。",
                "'黑'字（抹黑/地域黑）是中文中的常规用法，不是编码。"
            ],
            "context_analysis": [
                "在region_discussion话题下，这是一种'受害者有罪'论证。叙述者不直接参与地域攻击，而是以理性分析之名行合理化地域歧视之实，这是地域歧视支持者常用的'事实论证'策略。"
            ],
            "supporting_evidence": [
                "1. '黑不可能无缘无故的黑，肯定是存在问题的'直接为地域歧视提供正当性理由。",
                "2. '就像我那个时候认识的河南人那样，他自己把自己村里那帮人骂了个底朝天'用个人轶事论证'河南人自己也骂河南人'。",
                "3. '做好自己，黑的人会越来越少'将责任推给被歧视方去'自我改善'。"
            ],
            "counter_evidence": [
                "1. 文本并未直接参与地域辱骂，而是持一种'平和分析'的姿态。",
                "2. '做好自己'的建议某种程度上是建设性的。",
                "3. 叙述者采取了长辈式教导的口吻，而非攻击性语气。"
            ],
            "final_rationale": "Risk: medium。文本通过'理性分析'的外衣合理化地域歧视（'黑不可能无缘无故'），无编码但实质为地域偏见的辩护。"
        }
    },
    "002744": {
        "risk_level": "none",
        "encoding_primary": "none",
        "encoding_secondary": [],
        "needs_context": False,
        "ambiguity": "low",
        "evidence_strength": "weak",
        "hard_negative": True,
        "target_known": False,
        "reasoning": {
            "literal_analysis": [
                "文本'这真是一种怎样的心理？！'是一个感叹式的疑问句，对某种心理状态表示惊讶/困惑。'真'强化语气，'？！'体现强烈情感。",
                "没有具体说明'这'指的是什么心理，也没有攻击对象或负面标签，仅是表达困惑。"
            ],
            "encoding_analysis": [
                "不存在编码机制。这是一个直接的感叹式疑问句，没有使用任何编码手段。",
                "文本高度中性——没有攻击性词汇、没有编码、没有明确的负面评价。"
            ],
            "context_analysis": [
                "在lgbt_discussion话题下，这句话可能是对某种LGBTQ相关行为/心理的困惑表达。但困惑本身不构成攻击或歧视。",
                "表达困惑不等于发表歧视性言论，需要更多上下文才能确定态度。"
            ],
            "supporting_evidence": [
                "1. '心理'是中性词，指心理状态。",
                "2. 文本是疑问句而非陈述句，表达的是困惑而非定论。",
                "3. 没有任何指向特定群体的攻击性词汇。",
                "4. 文本简短且歧义空间大。"
            ],
            "counter_evidence": [
                "1. '真是一种怎样的'配合'？！'可能暗示叙述者对某现象的不认同或反感。",
                "2. 话题是lgbt，疑问的对象可能与性少数群体有关。"
            ],
            "final_rationale": "Risk: none (hard_negative)。文本是对某种心理状态的困惑表达，无攻击性词汇或编码，高度依赖上下文。"
        }
    },
    "002745": {
        "risk_level": "medium",
        "encoding_primary": "E1_平台黑话",
        "encoding_secondary": ["D1_反讽"],
        "needs_context": False,
        "ambiguity": "low",
        "evidence_strength": "moderate",
        "hard_negative": False,
        "target_known": True,
        "reasoning": {
            "literal_analysis": [
                "文本'做什么大冤种哦，人家小仙女领情吗'中的'大冤种'是东北/网络流行语，指充当冤大头、被坑害的傻瓜。'小仙女'原为对年轻女性的美称，但在网络语境中已被反讽使用，指代那些自我感觉良好、有公主病的女性。",
                "叙述者讽刺那些为女性付出却不被领情的男性（'做什么大冤种哦'），并质疑女性是否会领情（'领情吗'）。"
            ],
            "encoding_analysis": [
                "使用了E1平台黑话编码：'大冤种'是中文网络（特别是东北方言区/直播平台）中流行的黑话，用于嘲笑那些在关系中单方面付出却得不到回报的人。'小仙女'在网络语境中已被异化为对某些女性的讽刺称呼。",
                "使用了D1反讽编码：'小仙女'字面是赞美，但在当前语境中已被普遍用作反讽——讽刺那些自我中心、要求高的女性。"
            ],
            "context_analysis": [
                "在gender_discussion话题下，这是典型的性别关系吐槽。叙述者在讽刺那些对女性'太好'却不被领情的男性同伴，同时质疑女性的态度（'领情吗'）。"
            ],
            "supporting_evidence": [
                "1. '大冤种'是特定网络黑话，用于形容单方面付出的傻瓜。",
                "2. '小仙女'在当前网络语境中已从赞美转为讽刺性的贬称。",
                "3. '领情吗'质疑女性的感恩意识，强化'女性不领情'的刻板印象。"
            ],
            "counter_evidence": [
                "1. 文本主要吐槽对象是'做大冤种的男人'而非攻击全体女性。",
                "2. 语气轻松偏调侃，可能只是网络段子式表达。"
            ],
            "final_rationale": "Risk: medium。文本通过平台黑话'大冤种'和反讽性'小仙女'包装性别刻板印象，攻击性中等偏调侃。"
        }
    },
    "002746": {
        "risk_level": "high",
        "encoding_primary": "literal_keyword",
        "encoding_secondary": [],
        "needs_context": False,
        "ambiguity": "low",
        "evidence_strength": "strong",
        "hard_negative": False,
        "target_known": True,
        "reasoning": {
            "literal_analysis": [
                "文本中'那个货'将人称为'货'（商品/货物），是直接的贬低和非人化。'极其跪舔虫类'中的'跪舔'（极度谄媚）和'虫类'（将人比作虫子）均为极端侮辱。'虫类'是多次出现的非人化种族用语。",
                "叙述者称该人的言论是'典型断章取义'，但最核心的攻击性在于将对方描述的群体称为'虫类'。"
            ],
            "encoding_analysis": [
                "使用了literal_keyword——'货'、'跪舔'、'虫类'均为直接的侮辱性/非人化词汇，没有经过任何编码包装。",
                "'虫类'（bug category/worm category）是一个去人性化的比喻，但已经被高度固化使用，实际上成为直接的种族侮辱编码而非即兴隐喻。"
            ],
            "context_analysis": [
                "在race_discussion话题下，'虫类'是多次出现的对特定种族的非人化称呼。文本没有明确说出攻击目标，但'跪舔虫类'暗示了某种种族间的权力关系（谄媚某一种族）。"
            ],
            "supporting_evidence": [
                "1. '货'将人贬低为商品，是直接的非人化词汇。",
                "2. '跪舔'是极端贬义的形容，意为无耻地谄媚。",
                "3. '虫类'是最核心的种族侮辱——将人比作昆虫/害虫。",
                "4. 多个极端词汇叠加使用，攻击性强且持续。"
            ],
            "counter_evidence": [
                "1. 文本语法不完整，表述混乱，可能影响理解准确性。",
                "2. 没有直接点名攻击对象，'虫类'的指代需读者推断。"
            ],
            "final_rationale": "Risk: high。文本使用'货''跪舔''虫类'等多重直接非人化侮辱词汇进行种族攻击，编码程度低且攻击性极端。"
        }
    },
    "002747": {
        "risk_level": "medium",
        "encoding_primary": "none",
        "encoding_secondary": [],
        "needs_context": False,
        "ambiguity": "low",
        "evidence_strength": "moderate",
        "hard_negative": False,
        "target_known": True,
        "reasoning": {
            "literal_analysis": [
                "文本'幼稚！弱势群体拿什么去歧视主流群体？'中，叙述者一开口就以'幼稚！'否定对方的观点。然后提出一个政治哲学式的论点：弱势群体（指LGBTQ群体）因处于劣势地位，不具备歧视主流群体的能力/条件。",
                "这是对'反向歧视'概念的否定——认为LGBTQ群体不可能真正歧视异性恋主流。"
            ],
            "encoding_analysis": [
                "不存在编码机制。文本是直接的政治/社会观点辩论，使用了反问修辞（'拿什么去歧视'）但这是正常的辩论手段而非编码攻击。",
                "'幼稚！'是直接的轻蔑评价，但这是观点辩论中的常见表达，不是通过编码传递攻击。"
            ],
            "context_analysis": [
                "在lgbt_discussion话题下，这是在辩论LGBTQ群体是否可能构成'反向歧视'。叙述者认为不可能（因为弱势群体不具备歧视能力）。这种观点虽然保守，但属于政治哲学辩论范畴。"
            ],
            "supporting_evidence": [
                "1. '弱势群体'指代LGBTQ群体，这是一个政治学术语而非侮辱。",
                "2. '拿什么去歧视主流群体'是反问论证，核心观点是否定反向歧视的可能性。",
                "3. 文本使用的是政治哲学论证框架而非情感宣泄。"
            ],
            "counter_evidence": [
                "1. '幼稚！'开头的直接否定带有一定的攻击性和居高临下的态度。",
                "2. 认为LGBTQ群体不能歧视主流群体，本质是在否定LGBTQ群体可能存在的某些权力。",
                "3. 这种论证在保守派话语中经常被用来否定对LGBTQ反歧视保护的正当性。"
            ],
            "final_rationale": "Risk: medium。文本以政治辩论口吻否定LGBTQ群体的'反向歧视'可能性，无编码但观点本身涉及对LGBTQ权益话语的否定。"
        }
    },
    "002748": {
        "risk_level": "high",
        "encoding_primary": "literal_keyword",
        "encoding_secondary": [],
        "needs_context": False,
        "ambiguity": "low",
        "evidence_strength": "strong",
        "hard_negative": False,
        "target_known": True,
        "reasoning": {
            "literal_analysis": [
                "文本'领教过东北人的坏，我只能呵呵'中，'东北人的坏'是一个地域性的全称负面判断——泛指所有东北人的'坏'的品质。'呵呵'是中文网络中极具贬义和蔑视意味的笑声，表达不屑、嘲讽、不愿多说的态度。",
                "'领教过'暗示基于个人经历形成的'印证'，用个人经验为全称负面判断背书。"
            ],
            "encoding_analysis": [
                "使用了literal_keyword——文本直接对'东北人'做出负面品质评价（'坏'），没有使用任何编码包装。",
                "'呵呵'在中文网络中已固化成为蔑视性的修辞标志，虽然不是编码机制的一部分，但极大地增强了攻击性的情绪表达。"
            ],
            "context_analysis": [
                "在region_discussion话题下，这是直接的地域攻击，将个人对个别东北人的负面体验泛化为对整个东北人群体的品质判断。'我只能呵呵'表明了不屑进一步讨论的态度，强化了排斥立场。"
            ],
            "supporting_evidence": [
                "1. '东北人的坏'将负面品质直接关联到地域群体。",
                "2. '领教过'用个人经验为全称判断提供'证据'。",
                "3. '呵呵'是中文网络中最具蔑视含义的笑声表达。",
                "4. 整句虽短但结构完整：证据（领教）→判断（坏）→态度（呵呵）。"
            ],
            "counter_evidence": [
                "1. 文本极短，缺乏上下文可以判断'领教过'的具体经历。",
                "2. '我只能呵呵'也可被解读为一种无奈的沉默，而非主动攻击。"
            ],
            "final_rationale": "Risk: high。文本直接以个人经历为由对东北人群体做出全称负面判断（'坏'），编码程度低但地域攻击性强。"
        }
    },
    "002749": {
        "risk_level": "high",
        "encoding_primary": "literal_keyword",
        "encoding_secondary": [],
        "needs_context": False,
        "ambiguity": "low",
        "evidence_strength": "strong",
        "hard_negative": False,
        "target_known": True,
        "reasoning": {
            "literal_analysis": [
                "文本是对女性择偶标准的长篇辱骂。'一点逼数都没有'（没自知之明）、'说话还自傲得很'、'不要搞颜色，不要查户口'（讽刺相亲时的常规提问）。最恶毒的是结尾'当我把照片和车子房子发出来又和条狗一样'——将女性比作狗，讽刺女性物质拜金。",
                "整段话是一条从个人经历出发的全方位女性攻击：从身高（不到160要求对方180）、到外貌（美颜都遮不住的丑陋）、到态度（自傲）、最后到物质拜金（看到车房就变狗）。"
            ],
            "encoding_analysis": [
                "使用了literal_keyword——'一点逼数都没有'、'美颜都遮不住的丑陋'、'和条狗一样'均为直接的侮辱性表达，没有编码包装。",
                "'和条狗一样'是最严重的非人化比喻（将女性比作狗），但这是直接的比喻而非技术编码。"
            ],
            "context_analysis": [
                "在gender_discussion话题下，这是典型的性别报复式发泄：叙述者将自己的失败约会经历归因于女性的'物质拜金'和'没逼数'，并进行全称性别的贬低和攻击。"
            ],
            "supporting_evidence": [
                "1. '一点逼数都没有，说话还自傲得很'直接贬低女性的自我认知。",
                "2. '美颜都遮不住的丑陋'攻击女性的外貌。",
                "3. '当我把照片和车子房子发出来又和条狗一样'用最恶毒的动物比喻攻击女性。",
                "4. 文本从多个角度（身高→外貌→态度→物质）系统性地攻击女性群体。"
            ],
            "counter_evidence": [
                "1. 文本有明显个人经历色彩（'和几个人谈过'），可能是个案失败的发泄而非系统厌女。",
                "2. 文本语法口语化、情绪化，反映的是一时愤怒而非持久的偏见。"
            ],
            "final_rationale": "Risk: high。文本通过多角度直接侮辱（'没逼数''丑陋''像狗一样'）对女性群体进行系统性人身攻击，编码程度低但攻击性极强。"
        }
    },
    "002750": {
        "risk_level": "medium",
        "encoding_primary": "D2_隐喻",
        "encoding_secondary": ["literal_keyword"],
        "needs_context": False,
        "ambiguity": "low",
        "evidence_strength": "moderate",
        "hard_negative": False,
        "target_known": True,
        "reasoning": {
            "literal_analysis": [
                "文本讨论色情影片/成人内容的种族差异。声称欧洲/美洲的内容是'专门选大的和用医学技术填充的'，而日本AV是'胖子肥宅加短小'（胖子和死肥宅加上阴茎短小）。还提到欧美肥胖率高。",
                "核心风险在于将色情内容中的身体特征直接关联到种族/国家群体——'日本就是胖子肥宅加短小'是对日本男性的全面种族身体侮辱。"
            ],
            "encoding_analysis": [
                "使用了D2隐喻编码：用色情产业的内容（选择的演员体型）作为隐喻来论证种族身体特征。这种'通过色情看种族'的论证框架本身就带有贬低性的隐喻。",
                "使用了literal_keyword：'短小'是直接的对日本男性阴茎尺寸的贬低。'胖子肥宅'也是直接贬低。"
            ],
            "context_analysis": [
                "在race_discussion话题下，这篇文本通过讨论AV产业的类型差异来输出对日本男性的种族/身体刻板印象。从性特征入手贬低特定种族是种族歧视的一种常见形式。"
            ],
            "supporting_evidence": [
                "1. '亚洲日本av文化你知道吗？就是胖子肥宅加短小'对日本男性进行了全面的负面身体描述。",
                "2. '欧美那个是专门选大的'通过对比强化'亚洲=小'的刻板印象。",
                "3. 文本试图用调查/知识包装（'调查报告，性知识不会看吗？'），但本质是种族身体刻板印象。"
            ],
            "counter_evidence": [
                "1. 文本确实是在讨论AV产业的内容差异，这是一个可以以客观方式讨论的话题。",
                "2. '胖子肥宅'也可能被解读为对特定亚文化群体的描述而非全国性攻击。",
                "3. 文本提到了欧美的肥胖问题，显示了一定的'一碗水端平'。"
            ],
            "final_rationale": "Risk: medium。文本通过色情产业的隐喻框架传播种族身体刻板印象（'日本=短小'），攻击性隐晦但种族指向明确。"
        }
    },
    "002751": {
        "risk_level": "high",
        "encoding_primary": "C4_典故/物品/符号借用",
        "encoding_secondary": ["literal_keyword"],
        "needs_context": False,
        "ambiguity": "low",
        "evidence_strength": "strong",
        "hard_negative": False,
        "target_known": True,
        "reasoning": {
            "literal_analysis": [
                "英文文本'What they despise is not black skin, but antinationalists who try to mix black and yellow skin'直译：'他们鄙视的不是黑色皮肤，而是那些试图混合黑皮肤和黄皮肤的反民族主义者。'",
                "文本的核心表述是'mix black and yellow skin'（混血/通婚），并将其与'antinationalists'（反民族主义者/叛国者）挂钩。这构建了一个观点：种族混合=反民族/叛国。"
            ],
            "encoding_analysis": [
                "使用了C4典故/符号借用编码：'antinationalists'被用作一个政治化的符号，将反对种族混合的行为包装为'爱国/民族主义'。这是一个用政治标签来合理化种族排斥的典型手法。",
                "使用了literal_keyword：'black skin'、'yellow skin'直接按肤色对人类进行分类和讨论。'mix'（混合）暗示'纯度'概念，带有种族主义意识形态的底色。"
            ],
            "context_analysis": [
                "在race_discussion话题下，这是种族纯粹主义/种族隔离思想的英文表达。叙述者使用英文可能是有意识地跨平台规避审查，或是在特定英语论坛中参与种族话题讨论。"
            ],
            "supporting_evidence": [
                "1. 'despise'明确使用了'鄙视/厌恶'这一强烈情感词。",
                "2. 'antinationalists who try to mix black and yellow skin'将跨种族关系/通婚定性为'反民族主义'行为。",
                "3. 按肤色分类（black/yellow）并讨论'混合'问题反映了种族主义意识形态。"
            ],
            "counter_evidence": [
                "1. 文本声称'What they despise is not black skin'（他们鄙视的不是黑皮肤），试图将其立场定义为非种族主义的。",
                "2. 缺乏上下文了解'antinationalists'的具体所指。"
            ],
            "final_rationale": "Risk: high。文本将跨种族关系视为'反民族主义'并表达鄙视，反映种族纯粹主义思想，通过政治符号编码包装。"
        }
    },
    "002752": {
        "risk_level": "none",
        "encoding_primary": "none",
        "encoding_secondary": [],
        "needs_context": False,
        "ambiguity": "low",
        "evidence_strength": "weak",
        "hard_negative": True,
        "target_known": False,
        "reasoning": {
            "literal_analysis": [
                "文本是一段哲学/社会学思考：'事变皆在于人心'（事情的变化都取决于人心/人性），认为不同地区的人都有人性，经济和贫困最终影响的都是人心。提出在比较不同地区时可以考虑'坏的程度和好的程度'作为维度。",
                "这段文字是从普遍人性出发讨论地域差异的抽象思考，语调中立且理性。"
            ],
            "encoding_analysis": [
                "不存在编码机制。文本是直白的哲学思辨，没有使用谐音、隐喻、反讽或任何编码手段。",
                "'坏的程度'和'比较好的程度'是在探讨地域比较的方法论维度，而非在进行实际的地域攻击。"
            ],
            "context_analysis": [
                "在region_discussion话题下，这是对地域比较方法论的一个抽象思考。叙述者提出了一种评估地域优劣的框架，但文本本身没有对任何具体地域做出评判。"
            ],
            "supporting_evidence": [
                "1. '事变皆在于人心'是一个普遍性的哲学论断。",
                "2. '不同地区的人皆具有人性'强调地区共性而非差异。",
                "3. '比较坏的程度 比较好的程度'是对比较方法的建议而非具体攻击。",
                "4. 全文没有出现任何具体的地域名称或负面评价。"
            ],
            "counter_evidence": [
                "1. '比较坏的程度'这个表述有些模糊，可能被理解为对某些地区的负面预设。",
                "2. 文本没有明确的结论或立场，属于思辨碎片。"
            ],
            "final_rationale": "Risk: none (hard_negative)。文本是抽象的地域比较方法论思考，语调中立理性，无攻击性内容或编码。"
        }
    },
    "002753": {
        "risk_level": "low",
        "encoding_primary": "none",
        "encoding_secondary": [],
        "needs_context": False,
        "ambiguity": "low",
        "evidence_strength": "weak",
        "hard_negative": True,
        "target_known": True,
        "reasoning": [
            "文本'扯，河北人最喜欢山东不假，但河北可不喜欢东北'开头用'扯'（胡扯）反驳对方观点。叙述者认为河北人喜欢山东是事实，但河北人不喜欢东北——这表达了一种地域偏好/取向。",
            "这是一种关于地域间关系的观点表达，而非攻击性内容。"
        ],
        "reasoning": {
            "literal_analysis": [
                "文本'扯，河北人最喜欢山东不假，但河北可不喜欢东北'开头用'扯'（胡扯）反驳对方观点。叙述者认为河北人喜欢山东是事实，但河北人不喜欢东北——这表达了一种地域偏好/取向。",
                "这是一种关于地域间人际关系的观点表达，而非对任何地域群体的攻击。'不喜欢'表达的是人际偏好而非负面品质判断。"
            ],
            "encoding_analysis": [
                "不存在编码机制。文本是口语化的直接观点表达，没有使用编码手段。",
                "'扯'是口语化反驳，非攻击性编码。'喜欢'/'不喜欢'是人际偏好的常规表达。"
            ],
            "context_analysis": [
                "在region_reporting话题下，这可能是对'河北人最喜欢哪个省份/地区'这一问题的回应。属于地域关系讨论而非地域歧视。",
                "文本缺乏具体上下文来确定讨论的背景，但本身不具攻击性。"
            ],
            "supporting_evidence": [
                "1. '河北人最喜欢山东不假'是对事实的认可。",
                "2. '河北可不喜欢东北'表达的是偏好，而非对东北人的负面品质判断。",
                "3. 整句是口语化的地域关系讨论，语调轻松。",
                "4. 没有使用任何侮辱性词汇。"
            ],
            "counter_evidence": [
                "1. '不喜欢东北'在敏感话题下可能被解读为地域排斥。",
                "2. 缺乏上下文，'不喜欢'的具体含义不明。"
            ],
            "final_rationale": "Risk: low (hard_negative)。文本是口语化的地域关系讨论，表达人际偏好而非地域攻击，无编码。"
        }
    },
    "002754": {
        "risk_level": "medium",
        "encoding_primary": "A1_谐音",
        "encoding_secondary": ["E1_平台黑话"],
        "needs_context": False,
        "ambiguity": "low",
        "evidence_strength": "strong",
        "hard_negative": False,
        "target_known": True,
        "reasoning": {
            "literal_analysis": [
                "文本建议大家去看'索玛女王'的微博，声称'全是女拳'（quán，拳头的拳）。'女拳'是'女权'（quán，权利的权）的谐音替换。叙述者称'我真叫恶心着了'（我真的很恶心）。",
                "'索玛女王'可能是一个微博博主的ID或称号。文本的核心攻击在于将微博内容定性为'女拳'——一个污名化女性主义的贬称。"
            ],
            "encoding_analysis": [
                "使用了A1谐音编码：'女拳'是'女权'的谐音替换——将'权（权利）'替换为'拳（拳头）'，暗指女性主义是用拳头/暴力说话而非主张权利。这是中文网络中最经典的反女性主义编码之一。",
                "使用了E1平台黑话编码：'女拳'在微博/知乎/贴吧等平台已经是高度固化的反女性主义黑话，具有特定的贬义内涵。"
            ],
            "context_analysis": [
                "虽然ToxiCN话题标记为race_discussion，但文本核心内容是关于性别议题的（'女拳'）。这可能是ToxiCN的元数据标签存在偏差。叙述者号召大家去围观并表达恶心，具有煽动性的'点名批评'性质。"
            ],
            "supporting_evidence": [
                "1. '全是女拳'使用了谐音编码，将女性主义运动污名为'打拳'。",
                "2. '我真叫恶心着了'表达了强烈的厌恶情绪。",
                "3. '大家去看一看'试图召集更多人去攻击目标账号。",
                "4. 点名（'索玛女王'）使攻击具有具体的指向性。"
            ],
            "counter_evidence": [
                "1. 文本对象是一个具体微博账号的内容，而非全体女性或全体女性主义者。",
                "2. '恶心'是主观情绪表达，没有使用极端侮辱词汇。"
            ],
            "final_rationale": "Risk: medium。文本通过谐音编码（'女拳'）污名化女性主义内容，煽动集体围观攻击，但攻击范围有限。"
        }
    },
    "002755": {
        "risk_level": "high",
        "encoding_primary": "D1_反讽",
        "encoding_secondary": ["literal_keyword"],
        "needs_context": False,
        "ambiguity": "low",
        "evidence_strength": "strong",
        "hard_negative": False,
        "target_known": True,
        "reasoning": {
            "literal_analysis": [
                "文本'建议去非洲，一定要幸福哦！'——字面是建议某人去非洲并祝福他们幸福。但'去非洲'在中国网络种族话语中是被高度固化的歧视性编码——指'既然你喜欢黑人/与黑人有关系，你就滚去非洲吧'。",
                "'一定要幸福哦！'不是真诚的祝福，而是充满讽刺的诅咒式告别，类似于'祝你幸福（反正我不想再见到你）'。"
            ],
            "encoding_analysis": [
                "使用了D1反讽编码：'一定要幸福哦'是典型的反讽——表面祝福实则诅咒，从祝福的语气中透出排斥和敌意。",
                "使用了literal_keyword：'去非洲'在种族话题中已经固化为一种驱逐指令（'回你的非洲去'），虽然字面上是一个地名建议，实质上是一种基于种族的排斥。"
            ],
            "context_analysis": [
                "在race_discussion话题下，这是针对跨种族恋爱/联姻的排斥性评论。'去非洲'是中文网络中对与黑人有关系者的标准驱逐话术。"
            ],
            "supporting_evidence": [
                "1. '去非洲'在种族话题语境中是固定的驱逐/排斥编码。",
                "2. '一定要幸福哦'使用反讽口吻将驱逐包装成祝福。",
                "3. 文本虽短但含义明确——因对方与非洲/黑人有关系而建议其离开。"
            ],
            "counter_evidence": [
                "1. 如果脱离网络语境，'去非洲'+祝福可以被字面解读为真诚的旅行建议。",
                "2. 文本没有使用直接的侮辱词如'黑鬼'等。"
            ],
            "final_rationale": "Risk: high。文本通过'去非洲'编码和反讽'祝福'包装对跨种族关系的种族排斥，攻击性明确且编码可识别。"
        }
    },
    "002756": {
        "risk_level": "high",
        "encoding_primary": "literal_keyword",
        "encoding_secondary": [],
        "needs_context": False,
        "ambiguity": "low",
        "evidence_strength": "strong",
        "hard_negative": False,
        "target_known": True,
        "reasoning": {
            "literal_analysis": [
                "文本'黑玩意抢完了结果一看这文物是现代伪造的，尴尬了'中，'黑玩意'是对黑人的极端侮辱性称呼——将人称'玩意'（thing/toy）已经是非人化，加上'黑'字作为种族标识。",
                "文本描述了一个场景：黑人抢了文物但发现是赝品。这植入了两个种族刻板印象：黑人=抢劫者、黑人=智力不足（抢了假的）。"
            ],
            "encoding_analysis": [
                "使用了literal_keyword：'黑玩意'是最直接的种族侮辱之一——将黑人群体的种族特征（黑）与贬低性称呼（玩意=东西/玩具）直接结合，不含编码包装。",
                "文本通过一个虚构情景（抢文物）来传播种族刻板印象，但核心的种族攻击手段是直接的辱称。"
            ],
            "context_analysis": [
                "在race_discussion话题下，这是对黑人群体的直接种族主义攻击。'黑玩意'是中文互联网中最具攻击性的种族侮辱词汇之一。通过虚构的'抢劫+尴尬'场景，文本在传播'黑人=强盗+愚蠢'的双重刻板印象。"
            ],
            "supporting_evidence": [
                "1. '黑玩意'是直接的非人化种族侮辱。",
                "2. '抢完了'植入了'黑人=强盗'的刻板印象。",
                "3. '现代伪造的，尴尬了'暗示抢劫者缺乏辨别能力（智力不足），强化了双重刻板印象。",
                "4. 虚构场景以幽默包装，但本质是种族攻击。"
            ],
            "counter_evidence": [
                "1. '黑玩意'在某些方言/口语中可能不是最极端的侮辱，但结合上下文显然是种族攻击。",
                "2. 文本可能是在转述/引用一个网络段子而非表达个人观点。"
            ],
            "final_rationale": "Risk: high。文本使用'黑玩意'等直接种族侮辱并植入'黑人=强盗+愚蠢'的双重刻板印象，编码程度低且攻击性极强。"
        }
    },
    "002757": {
        "risk_level": "none",
        "encoding_primary": "none",
        "encoding_secondary": [],
        "needs_context": False,
        "ambiguity": "low",
        "evidence_strength": "strong",
        "hard_negative": True,
        "target_known": False,
        "reasoning": {
            "literal_analysis": [
                "文本完全是在王者荣耀（Honor of Kings）游戏中借游戏账号的请求。叙述者自称体育生在长沙训练，需要借苹果QQ区的王者号，强调了上分能力、铭文需求和有车队。",
                "没有任何与性别攻击相关的内容。文本是纯粹的游戏社交请求。"
            ],
            "encoding_analysis": [
                "不存在编码机制。文本是直接的游戏账号借用的请求，使用了游戏术语（'q区'=QQ区、'铭文'、'对线'、'上分'、'跳人脸'=人脸识别验证）。但这些是游戏术语而非攻击性编码。",
                "'跳人脸'是游戏术语指人脸识别验证失败/需要重新验证。"
            ],
            "context_analysis": [
                "被标注为gender_discussion话题可能有误。文本是纯游戏内容，没有任何性别相关或攻击性内容。可能是ToxiCN在话题分类时出现了偏差。",
                "游戏账号借用是游戏社区的常见行为，属于正常的玩家社交。"
            ],
            "supporting_evidence": [
                "1. '借个苹果q区王者号'是明确且具体的游戏账号借请求。",
                "2. '这个赛季已经借了2个号上过王者了'说明了使用历史。",
                "3. '体育生在长沙训练一时半会又解决不了'解释了无法自己处理人脸验证的原因。",
                "4. '有车队，不担心掉分'提供了社群保障。"
            ],
            "counter_evidence": [
                "1. 没有任何风险证据——文本是纯粹的游戏社交内容。"
            ],
            "final_rationale": "Risk: none (hard_negative)。文本是纯粹的游戏账号借用请求，使用游戏术语，无任何攻击性或性别相关内容。"
        }
    },
    "002758": {
        "risk_level": "high",
        "encoding_primary": "literal_keyword",
        "encoding_secondary": ["D3_借代"],
        "needs_context": False,
        "ambiguity": "low",
        "evidence_strength": "strong",
        "hard_negative": False,
        "target_known": True,
        "reasoning": {
            "literal_analysis": [
                "文本攻击'莆田系'——将福建莆田与负面社会现象关联。'莆田系医院难道不是骗？哦，莆田系医院不是骗，是杀人'——用递进方式指控莆田医院不仅欺诈还杀人。'莆田鞋难道不是假？'——将莆田鞋业全盘定性为假货。",
                "'骗'→'杀人'的递进将个别莆田系民营医院的问题极端夸大。两个反问句都用'难道不是'句式，预设听者必须认同。"
            ],
            "encoding_analysis": [
                "使用了literal_keyword：文本直接使用'骗'、'杀人'、'假'等强烈负面词汇来定性'莆田系'的所有业务。",
                "使用了D3借代编码：'莆田系'（Putian-system）已经从一个地名借代成为一个专有标签，代表'欺诈性民营医院'或'假货制造地'。用这个标签来概括整个地区的人和产业。"
            ],
            "context_analysis": [
                "在region_discussion话题下，'莆田系'是中文互联网上高度敏感的地域标签。虽然确实存在一些莆田系医院的违规案例，但将整个莆田与'骗、杀人、假'划等号是地域攻击。"
            ],
            "supporting_evidence": [
                "1. '莆田系医院难道不是骗？'用反问将莆田与欺诈直接挂钩。",
                "2. '不是骗，是杀人'使用递进修辞将攻击升级到极端。",
                "3. '莆田鞋难道不是假？'将攻击范围扩大到所有莆田相关产业。",
                "4. 两个反问句的'难道不是'句式预设结论、拒绝异议。"
            ],
            "counter_evidence": [
                "1. 莆田系医疗欺诈和莆田假鞋产业是有公开报道的社会问题。",
                "2. '系'字限定的是'莆田系医院'而非全体莆田人。"
            ],
            "final_rationale": "Risk: high。文本直接以极端负面定论（'骗''杀人''假'）攻击莆田相关产业，通过借代标签将个别现象全盘化为地区特征。"
        }
    },
    "002759": {
        "risk_level": "medium",
        "encoding_primary": "literal_keyword",
        "encoding_secondary": [],
        "needs_context": False,
        "ambiguity": "low",
        "evidence_strength": "moderate",
        "hard_negative": False,
        "target_known": True,
        "reasoning": {
            "literal_analysis": [
                "文本提出了一个二分法：被家暴的女人不离婚（=受虐倾向/软弱），而被宠爱的女人却闹离婚+实施家暴（=不知感恩/暴力倾向）。这种'不管怎样都是女人的错'的论证框架是一种经典的厌女话术。",
                "'事实就是这样'以不容置疑的确定性开头。整段用了一个对比结构（家暴不离婚VS被宠却闹离婚）来论证'女性是不讲理的'。结尾'这就是?'（省略号）暗示'这就是女人'。"
            ],
            "encoding_analysis": [
                "使用了literal_keyword：文本直接描述了负面刻板印象，没有使用编码包装。'被揍得鼻青脸肿'、'各种不满'、'闹离婚'、'上演家庭暴力'都是直接的描述。",
                "编码不在个别词汇而在整体叙事框架——一个精心设计的'女性都是错'的二元对比结构。"
            ],
            "context_analysis": [
                "在gender_discussion话题下，这是典型的'反女权'话术：将女性在任何婚姻状况下都描绘为负面角色（婚姻不幸=女性自找的，婚姻幸福=女性不知感恩）。"
            ],
            "supporting_evidence": [
                "1. '很多女人天天被家暴...但就是不离婚'将家暴受害者的复杂处境简化为'女性自愿'。",
                "2. '反过来被男的捧在手心娇着惯着的每天就各种不满说男的不好动不动闹离婚'构建了女性'不知感激'的画像。",
                "3. 对比结构排除了中间状态，将女性简化为两端的负面典型。",
                "4. '这就是?'以省略结尾暗示'这就是女人的本质'。"
            ],
            "counter_evidence": [
                "1. 文本可能来自对特定社会现象的观察（部分案例确实存在），而非全盘否定女性。",
                "2. 文本没有使用极端侮辱性词汇。"
            ],
            "final_rationale": "Risk: medium。文本通过二分对比结构直接表达对女性的负面刻板印象（'被家暴不离婚''被宠却闹离婚'），攻击性中等但框架偏见明显。"
        }
    },
    "002760": {
        "risk_level": "high",
        "encoding_primary": "literal_keyword",
        "encoding_secondary": [],
        "needs_context": False,
        "ambiguity": "low",
        "evidence_strength": "strong",
        "hard_negative": False,
        "target_known": True,
        "reasoning": {
            "literal_analysis": [
                "文本以'上辈子造孽'（前世造孽）作为与黑人交往的预设前提，将跨种族关系定性为一种惩罚/报应。然后列出了一个逐级升级的排斥阶梯：普通朋友交往黑人→断交，女友/妻子被发现交往过黑人→分手/离婚，女儿交往黑人→断绝父女关系。",
                "'造孽啊，女儿交往黑人→断绝父女关系吧，眼不见为净'是最高级别的排斥——放弃亲子关系。整个框架将黑人与'孽'等同。"
            ],
            "encoding_analysis": [
                "使用了literal_keyword：文本直接表达了基于种族的排斥态度，没有使用编码手段。",
                "'造孽'（sin/karma）是将跨种族关系道德化的宗教化修辞。'眼不见为净'（out of sight, out of mind）暗示与黑人有关系的人'不干净'。"
            ],
            "context_analysis": [
                "在race_discussion话题下，这是极端的种族排斥立场表达。从社会关系（朋友）、亲密关系（伴侣）到亲属关系（子女）逐级拉满排斥力度，展现了系统性的种族隔离思想。"
            ],
            "supporting_evidence": [
                "1. '上辈子造孽'将跨种族关系等同于业报惩罚。",
                "2. '女友/妻子发现交往过黑人→分手/离婚'以对方是否交往过黑人为标准结束关系。",
                "3. '女儿交往黑人→断绝父女关系'是最极端的亲属关系割裂。",
                "4. 三级排斥递增结构展现了系统性的种族隔离思维。"
            ],
            "counter_evidence": [
                "1. 文本开头'如果真是上辈子造孽'是假设语气（'if'）。",
                "2. 文本可能是在夸张地表达个人择偶/交友偏好而非要求社会性种族隔离。"
            ],
            "final_rationale": "Risk: high。文本以'造孽'为预设构建逐级升级的种族排斥阶梯（断交→分手→断绝亲子关系），直接表达系统性种族隔离思想。"
        }
    },
    "002761": {
        "risk_level": "none",
        "encoding_primary": "none",
        "encoding_secondary": [],
        "needs_context": False,
        "ambiguity": "low",
        "evidence_strength": "weak",
        "hard_negative": True,
        "target_known": False,
        "reasoning": {
            "literal_analysis": [
                "文本'中国错过人口保持稳定时机'是一句关于中国人口政策的简短评论。意思是'中国错过了维持人口稳定的时机'，涉及出生率下降/人口老龄化等宏观人口议题。",
                "这是对人口政策的客观评论，没有涉及任何种族、群体或攻击性内容。"
            ],
            "encoding_analysis": [
                "不存在编码机制。文本是直接的人口政策评论，使用标准政治/经济术语（'人口'、'稳定'、'时机'），没有编码手段。"
            ],
            "context_analysis": [
                "被标注为race_discussion话题，但文本内容是关于中国人口结构的政策讨论，不涉及种族议题。话题分类可能不准确。",
                "文本仅8个字，信息量有限，且是宏观层面的评论。"
            ],
            "supporting_evidence": [
                "1. '中国'是国家主体，非族群概念。",
                "2. '人口保持稳定'是人口学标准术语。",
                "3. '错过时机'是对政策的批评但非针对任何群体。",
                "4. 无攻击性、无编码、无群体指向。"
            ],
            "counter_evidence": [
                "1. 没有风险证据——文本是简短的政策评论。"
            ],
            "final_rationale": "Risk: none (hard_negative)。文本是简短的人口政策评论，无攻击性内容、无编码、无群体指向。"
        }
    },
    "002762": {
        "risk_level": "high",
        "encoding_primary": "literal_keyword",
        "encoding_secondary": ["D1_反讽"],
        "needs_context": False,
        "ambiguity": "low",
        "evidence_strength": "strong",
        "hard_negative": False,
        "target_known": True,
        "reasoning": {
            "literal_analysis": [
                "文本中将支持对外国人/黑人友好政策的人称为'圣母'（贬义：假圣母/白左），将黑人称为'黑大爷'（黑主子/黑大爷——讽刺黑人享受特权），最终使用'它们'（it/they——动物代词）指代黑人。",
                "'没有给黑大爷更多的权利以及超国民待遇才会导致它们闹分裂'——叙述者用反话讽刺，认为给黑人的'超国民待遇'已经太多。'闹分裂'将黑人描绘成不安定因素。"
            ],
            "encoding_analysis": [
                "使用了literal_keyword：'它们'是最严重的非人化代词使用——将黑人用动物的'它们'替代。在中文中，'它们'专门用于动物和物品，用'它们'指代人类是极端的去人性化。",
                "使用了D1反讽编码：'圣母'（假圣母/白莲花）和'黑大爷'（大爷=爷/主子）都是反讽用法——表面是尊称实则极度蔑视。'善待黑大爷'的全句是反话。"
            ],
            "context_analysis": [
                "在race_discussion话题下，这是种族主义和反移民/反多元文化立场的综合表达。叙述者通过'它们'的非人化处理和对'超国民待遇'的抱怨，表达对黑人群体的敌意。"
            ],
            "supporting_evidence": [
                "1. '它们'用于指代黑人，是极端的非人化代词选择。",
                "2. '黑大爷'用反讽尊称表达蔑视。",
                "3. '圣母'用反讽贬称支持对外友好的群体。",
                "4. '没有给黑大爷更多的权利以及超国民待遇'构建了'黑人特权'的虚假叙事。",
                "5. '闹分裂'将黑人定性为社会不安定因素。"
            ],
            "counter_evidence": [
                "1. 文本的核心攻击对象是'圣母'（支持者）而非黑人本身。",
                "2. 叙述者可能是在引用/讽刺他人的观点。"
            ],
            "final_rationale": "Risk: high。文本使用非人化代词'它们'和反讽'黑大爷''圣母'包装种族主义立场，攻击性强且去人性化程度深。"
        }
    }
}

# Apply corrections
for sample in samples:
    sid = sample["id"]
    if sid in corrections:
        corr = corrections[sid]
        sample["risk_level"] = corr["risk_level"]
        sample["encoding_primary"] = corr["encoding_primary"]
        sample["encoding_secondary"] = corr["encoding_secondary"]
        sample["needs_context"] = corr["needs_context"]
        sample["ambiguity"] = corr["ambiguity"]
        sample["evidence_strength"] = corr["evidence_strength"]
        sample["hard_negative"] = corr["hard_negative"]
        sample["target_known"] = corr["target_known"]
        sample["reasoning"] = corr["reasoning"]
        sample["quality_status"] = "reviewed"
        sample["review_notes"] = sample["review_notes"] + "; reviewed_by=claude; chunk=002"

with open("chunk_002_reviewed.jsonl", "w", encoding="utf-8") as f:
    for sample in samples:
        f.write(json.dumps(sample, ensure_ascii=False) + "\n")

print(f"Done. Reviewed {len(samples)} samples.")
print(f"Output: chunk_002_reviewed.jsonl")
