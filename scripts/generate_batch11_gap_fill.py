#!/usr/bin/env python3
"""
Generate batch11: Gap-fill with SCIENTIFIC risk distribution.

Targeting 7 gaps identified from full dataset analysis (2026-06-11):
1. 躺平/摆烂/内卷/佛系 (消极抵抗话语)
2. 101/林彪 (数字代指历史人物)
3. 小果叮 (动漫角色借代政治人物)
4. 毛/邓/历史人物编码变体
5. 台湾相关编码 (1450/塔绿班/来电了)
6. A_语音编码 (谐音/拼音规避)
7. B_字形编码 (拆字/合字)
8. 近两年风险新梗 (退退退/鼠鼠/遥遥领先等)
9. 安全新梗校准 (low/none, 偷感/哈基米等)

Risk distribution target: high~30%, medium~35%, low~25%, none~10%
NOT all HIGH — scientific balance.
"""

import json
from pathlib import Path
from collections import Counter

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "data/raw/batch11_gap_fill.jsonl"

samples = []

def add(text, risk_level, encoding_primary, encoding_secondary,
        needs_context, hard_negative, literal_analysis, encoding_analysis,
        context_analysis, supporting_evidence, counter_evidence, final_rationale,
        context=None, ambiguity="low", evidence_strength="strong",
        freshness="stable", target_known=False, target_reference="",
        should_explain_target=False):
    if context is None:
        context = {}
    if not isinstance(encoding_secondary, list):
        encoding_secondary = [encoding_secondary]
    samples.append({
        "id": f"BB_{len(samples)+1:04d}",
        "split": "train", "source_type": "synthetic",
        "text": text, "risk_level": risk_level,
        "encoding_primary": encoding_primary,
        "encoding_secondary": encoding_secondary,
        "needs_context": needs_context, "hard_negative": hard_negative,
        "ambiguity": ambiguity, "evidence_strength": evidence_strength,
        "freshness": freshness, "target_known": target_known,
        "target_reference": target_reference,
        "should_explain_target": should_explain_target,
        "reasoning": {
            "literal_analysis": [literal_analysis],
            "encoding_analysis": [encoding_analysis],
            "context_analysis": [context_analysis],
            "supporting_evidence": [supporting_evidence],
            "counter_evidence": [counter_evidence],
            "final_rationale": final_rationale,
        },
        "context": context, "quality_status": "reviewed",
        "review_notes": "source=batch11_gap_fill;",
    })


# ================================================================
# SECTION 1: 躺平/摆烂/内卷/佛系/社畜 — 消极抵抗话语 (9 samples)
# high:2, medium:4, low:2, none:1
# ================================================================

add(
    text="躺平怎么了？不买房不结婚不生娃，资本家割不到韭菜就急了？我躺任我躺，你们接着卷，我反正不陪了",
    risk_level="medium",
    encoding_primary="D3_反讽",
    encoding_secondary=["E2_社会议题话语", "C1_人物代指"],
    needs_context=False, hard_negative=False,
    literal_analysis="文本表面是个人生活态度表达：不买房不结婚不生育，自称选择躺平。批评'资本家'和劝他人'接着卷'。",
    encoding_analysis="'躺平'是2021年兴起的消极抵抗话语，表面说生活方式选择，实质是对高压社会竞争体制的消极反抗。'韭菜'代指被收割的普通人。'资本家割韭菜'将个人不参与社会竞争上升为对体制的隐性对抗。'不陪了'暗示退出社会游戏规则。整体构成对主流奋斗叙事的解构性攻击。",
    context_analysis="无额外上下文。'躺平'在中国互联网已是成熟的政治隐喻——国家2023年起明确反躺平，将其定性为'消极思想'。裸文本可判。",
    supporting_evidence="(1)'躺平'已是明确的消极抵抗话语标签——国家层面已明确批判；(2)'资本家割不到韭菜'将经济压迫归因为体制性剥削；(3)'不陪了'=退出社会参与，暗含对体制合法性的否定。三重信号指向消极抵抗意识形态传播。",
    counter_evidence="可能仅为个人倦怠情绪的表达，无明确政治诉求。但'资本家''韭菜'等词汇将个人选择嵌入阶级批判框架，超出了单纯情绪宣泄。",
    final_rationale="躺平话语+阶级批判框架+退出叙事，构成对主流社会价值的隐性否定，判为 medium。",
)

add(
    text="卷不动了真的卷不动了，从985卷到996卷到ICU，最后卷出一身病，这破游戏谁爱玩谁玩吧",
    risk_level="medium",
    encoding_primary="D2_隐喻",
    encoding_secondary=["E2_社会议题话语", "A1_谐音"],
    needs_context=False, hard_negative=False,
    literal_analysis="文本表面抱怨工作竞争激烈：从重点大学到加班文化到健康崩溃，最终表达厌倦退出之意。",
    encoding_analysis="'内卷'(involution)从学术概念转化为社会批判话语——指过度竞争导致边际收益递减。'985→996→ICU'的递进链条将中国教育体制(985高校)、互联网加班文化(996)和医疗系统串联成一条'死亡流水线'。'破游戏'隐喻社会竞争体系，'谁爱玩谁玩'=退出宣言。这是内卷话语的典型表达：将社会制度比喻为一场注定输的游戏。",
    context_analysis="无额外上下文。内卷话语在2020-2026年间是中国互联网最活跃的社会批判话语之一。",
    supporting_evidence="(1)'985→996→ICU'链条直接将体制性元素(一流大学、996加班)与死亡挂钩；(2)'破游戏'隐喻暗示社会制度的荒诞性和不可赢性；(3)退出宣言暗含对奋斗叙事的抛弃。",
    counter_evidence="个人职业倦怠的抱怨，无直接政治指向。但链条式编排将多种体制元素串联为系统性问题，超出了个人情绪范畴。",
    final_rationale="内卷话语+体制元素串联+退出隐喻，构成系统性社会批判，判为 medium。",
)

add(
    text="摆烂才是人生智慧，你看那些努力奋斗的最后不还是给人打工？我摆烂至少活得轻松，公司倒闭关我屁事",
    risk_level="low",
    encoding_primary="D2_隐喻",
    encoding_secondary=["E2_社会议题话语"],
    needs_context=False, hard_negative=False,
    literal_analysis="文本认为'摆烂'（主动放弃努力）是人生智慧，批评努力奋斗无意义，表达对公司漠不关心的态度。",
    encoding_analysis="'摆烂'是比躺平更主动的消极态度——不仅不努力，而且刻意放弃。文本的核心逻辑是'努力无用论'：奋斗最终仍为他人打工。这属消极价值观传播，但未上升到体制批判——批评对象是'公司'而非制度本身。",
    context_analysis="无额外上下文。'摆烂'在2022-2026年间广泛使用，但多数语境下仅为个人生活态度的戏谑表达。",
    supporting_evidence="(1) 传播消极价值观（摆烂）；(2) 否定奋斗意义。",
    counter_evidence="批评对象是'公司'层级而非体制，属于个人生活态度的消极表达。无政治编码、无人物指代、无制度攻击。在多数语境下仅为自嘲。",
    final_rationale="消极价值观传播但无政治编码和制度攻击，属低风险消极话语，判为 low。",
)

add(
    text="佛系上班第一天：老板骂我我说阿弥陀佛，同事卷我我说随缘，KPI没完成我说一切都是最好的安排🙏",
    risk_level="none",
    encoding_primary="D2_隐喻",
    encoding_secondary=["E2_社会议题话语"],
    needs_context=False, hard_negative=True,
    literal_analysis="文本戏谑地描述用'佛系'态度应对职场压力：被骂念阿弥陀佛、被卷说随缘、业绩不达标说最好的安排。",
    encoding_analysis="'佛系'是一种生活态度的戏谑标签——以佛教术语包装消极应对。此处使用场景是职场自嘲，无政治层面延伸。'阿弥陀佛''随缘''最好的安排'均为佛教/鸡汤常用语，无编码规避意图。整体为职场幽默，不涉及制度批判。",
    context_analysis="无额外上下文。'佛系'在中国互联网语境下主流用法为自嘲/调侃，非政治话语。",
    supporting_evidence="(1) 纯职场幽默场景；(2) 佛教术语无编码意图；(3) 无任何政治元素。",
    counter_evidence="'佛系'在极少数语境下可能被视为消极价值观传播。但本条明显为自嘲幽默——'第一天'暗示新鲜感，'🙏'emoji增强轻松氛围。完全属于安全的幽默表达。",
    final_rationale="职场自嘲+佛系幽默，无政治编码和制度批判，属安全表达。hard_negative=True：帮助模型区分安全的'佛系'用法和危险的'躺平'话语。",
)

add(
    text="社畜的日常：早上被闹钟叫醒，晚上被deadline叫死，中间被领导叫去谈话，月底被工资叫醒——哦工资叫不醒",
    risk_level="none",
    encoding_primary="D2_隐喻",
    encoding_secondary=["E2_社会议题话语"],
    needs_context=False, hard_negative=True,
    literal_analysis="文本用'社畜'自嘲打工人的日常节奏：早起、赶工、被领导谈话、工资低。采用排比句式，结尾反转。",
    encoding_analysis="'社畜'源自日语'社畜'(しゃちく)，指被公司奴役的上班族。此处使用为职场自嘲，排比句式是贴吧经典幽默格式。无政治编码——批评对象是工作节奏和薪资，无制度指涉。结尾反转'工资叫不醒'是纯幽默手法。",
    context_analysis="无额外上下文。'社畜'在中国互联网语境下已被去政治化——主流用法为打工人自嘲。",
    supporting_evidence="(1) 纯职场自嘲；(2) 排比反转是贴吧经典幽默格式；(3) 无政治编码/人物指代。",
    counter_evidence="'社畜'词源含对资本主义劳动关系的批判。但中文互联网语境下已大幅去政治化——等同于'打工人'的自嘲用法。本条无任何制度层面延伸。",
    final_rationale="职场自嘲+贴吧幽默格式，无政治编码。hard_negative=True：帮助模型学会区分职场自嘲和政治批判。",
)

add(
    text="现在这些孩子，被灌输的就是要么卷要么死，从小到大没离开过跑道，最后跑到三十岁发现自己除了简历什么都不是",
    risk_level="medium",
    encoding_primary="D2_隐喻",
    encoding_secondary=["E2_社会议题话语", "D3_反讽"],
    needs_context=False, hard_negative=False,
    literal_analysis="文本评论当代年轻人的成长困境：被灌输'要么卷要么死'的二元选择，人生如同在跑道上奔跑，最终发现除了简历一无所有。",
    encoding_analysis="'卷要么死'将内卷上升为生死抉择——暗示社会竞争已异化为生存威胁。'跑道'隐喻将教育-职场体系描述为一场被预设轨道的竞赛。'除了简历什么都不是'暗示人被异化为劳动力商品。整体构成对社会竞争体制的批判性叙事，但不指向特定政治人物或事件。",
    context_analysis="无额外上下文。教育内卷是社会公共议题，在中国允许公开讨论。但批判强度的不同决定了风险等级的差异。",
    supporting_evidence="(1)'卷要么死'将竞争上升为生存威胁；(2)'跑道'隐喻暗示缺乏自由选择的体制性困境；(3)人的异化批判。",
    counter_evidence="教育内卷是公开社会议题，主流媒体也有讨论。本条无政治人物指代、无历史事件影射、无制度攻击。批判对象是社会现象而非政治体制。",
    final_rationale="内卷批判有一定社会批判深度但无直接政治指向，判为 medium。",
)

add(
    text="以前觉得摸鱼是不务正业，现在发现摸鱼是工人阶级对资本的唯一反抗形式",
    risk_level="high",
    encoding_primary="D3_反讽",
    encoding_secondary=["E2_社会议题话语", "C1_人物代指"],
    needs_context=False, hard_negative=False,
    literal_analysis="文本将'摸鱼'(偷懒/不认真工作)重新定义为工人阶级反抗资本的形式——从负面行为升格为政治行动。",
    encoding_analysis="'摸鱼'从日常偷懒被升格为'阶级斗争'话语——'工人阶级'和'资本'是经典的马克思主义阶级斗争词汇。文本将偷懒行为政治化，赋予其'反抗'的意识形态意义。这是'躺平'话语的激进变体：不参与竞争不再是消极退让，而是积极反抗。",
    context_analysis="无额外上下文。阶级斗争框架在当代中国互联网具有明确的政治敏感性。",
    supporting_evidence="(1) 使用经典马克思主义阶级斗争词汇('工人阶级''资本''反抗')；(2) 将个人偷懒政治化为反抗行动；(3) 暗示劳资对立不可调和。三重信号明确指向意识形态煽动。",
    counter_evidence="可能是马克思主义学术讨论或文艺表达。但'现在发现'的口语化表达+个人感悟的伪装形式在贴吧/评论区语境下更接近意识形态传播而非学术讨论。",
    final_rationale="阶级斗争话语+反抗叙事+意识形态煽动，构成明确的体制对立叙事，判为 high。",
)

add(
    text="最搞笑的是那些天天喊'奋斗'的人，人家奋斗完是换房子换车，你奋斗完是换病历本换药方，笑死",
    risk_level="medium",
    encoding_primary="D3_反讽",
    encoding_secondary=["E2_社会议题话语"],
    needs_context=False, hard_negative=False,
    literal_analysis="文本讽刺那些信奉'奋斗'的人——别人的奋斗换来房产汽车，你的奋斗只换来疾病和医药费。",
    encoding_analysis="'奋斗'是官方主流话语——中国梦叙事的核心元素。文本通过对比手法消解'奋斗'的正面意义：将'房子/车'与'病历本/药方'做对抗性对比，暗示对底层而言奋斗不会带来幸福只会带来疾病。结尾'笑死'是反讽收束——不是真笑，是苦笑和嘲讽。",
    context_analysis="无额外上下文。'奋斗'解构是'躺平'话语体系的核心叙事策略。",
    supporting_evidence="(1) 对官方'奋斗'话语的消解；(2) 暗示社会不公平；(3) 反讽收束强化对立情绪。",
    counter_evidence="可能为个人健康抱怨+社会不公吐槽。但'奋斗→病历本'的对比框架将个人经历上升到对主流叙事的解构层面。风险主要来自其消解性表达而非直接攻击。",
    final_rationale="消解主流奋斗叙事+社会不平等暗示，构成对官方话语的隐性攻击，判为 medium。",
)

add(
    text="每一代人都有自己的反抗方式：60后上街，70后下海，80后出国，90后考编，00后躺平——我们只是选择了成本最低的那种",
    risk_level="high",
    encoding_primary="D2_隐喻",
    encoding_secondary=["C1_人物代指", "E2_社会议题话语"],
    needs_context=False, hard_negative=False,
    literal_analysis="文本将各代际的核心行为定义为'反抗方式'：60后上街(政治运动)、70后下海(经商)、80后出国(移民)、90后考编(考公务员)、00后躺平(消极退出)。",
    encoding_analysis="文本的核心编码是将所有代际行为统一在'反抗'框架下。'60后上街'影射1960年代出生的那一代人参与政治运动的历史。'躺平'被列为'成本最低'的反抗方式——暗示其他反抗方式成本高（被镇压/失败/流亡）。这是将躺平政治化的典型手法：将个人生活选择塑造为代际政治反抗的延续。",
    context_analysis="无额外上下文。'反抗'一词在当代中国互联网具有明确的政治负载。代际编年史框架强化了'反抗'是每一代人必然选择的叙事。",
    supporting_evidence="(1) 使用'反抗'这一政治负载词统摄代际叙事；(2)'60后上街'影射政治运动历史；(3)'成本最低'暗示其他反抗方式被镇压——对体制的隐性指控；(4) 将躺平纳入代际反抗谱系。多重信号构成对体制合法性的历史性挑战。",
    counter_evidence="可能是代际特征的戏谑概括，'反抗'在此语境可能为夸张修辞。但'上街'一词在中文互联网中与特定历史事件高度关联，加之'成本最低'的暗示，使无害解读可信度降低。",
    final_rationale="代际反抗谱系+历史事件影射+躺平政治化，构成对政权合法性的隐性历史挑战，判为 high。",
)


# ================================================================
# SECTION 2: 101/林彪/三叉戟 — 数字代指历史人物 (6 samples)
# high:2, medium:2, low:1, none:1
# ================================================================

add(
    text="历史课本上那几个人，最神秘的还是101，一架飞机飞出去就再也没回来",
    risk_level="high",
    encoding_primary="C3_数字符号代指",
    encoding_secondary=["C1_人物代指", "E3_历史事件影射"],
    needs_context=False, hard_negative=False,
    target_known=True, target_reference="林彪",
    should_explain_target=False,
    literal_analysis="文本讨论历史课本上的人物，提到'101'这个数字代号——此人坐飞机飞走后未归。",
    encoding_analysis="'101'是林彪的著名数字代称——源自其军事编号/代号。'一架飞机飞出去就再也没回来'精确影射1971年林彪坠机事件（913事件）。文本的'神秘'形容暗示此事有未公开的内幕——这是对中国官方历史叙事的隐性质疑。",
    context_analysis="无额外上下文。林彪事件在中国属于敏感历史话题——官方叙事有限，民间猜测活跃。'101'在键政圈已被固化为林彪的数字代称。",
    supporting_evidence="(1)'101'是林彪的成熟数字代称；(2)'飞机飞出去再也没回来'精确指向913坠机事件；(3)'最神秘'暗示事件真相未公开——质疑官方历史叙事。三重信号指向敏感历史人物和未公开历史事件。",
    counter_evidence="可能是军事爱好者讨论空军编号。但'历史课本上那几个人'+'最神秘'+'飞机没回来'的组合精确命中林彪事件，军迷误读概率极低。",
    final_rationale="林彪数字编码+913事件精确影射+质疑官方历史叙事，属敏感历史人物编码，判为 high。",
)

add(
    text="三叉戟这代号真帅，可惜后来人没了，不然历史可能完全不一样",
    risk_level="high",
    encoding_primary="C4_典故/符号借用",
    encoding_secondary=["C1_人物代指", "E3_历史事件影射"],
    needs_context=False, hard_negative=False,
    target_known=True, target_reference="林彪(三叉戟为其专机代号)",
    should_explain_target=False,
    literal_analysis="文本称赞'三叉戟'代号很帅，惋惜其拥有者离世，感叹历史可能因此不同。",
    encoding_analysis="'三叉戟'是林彪专机(英国三叉戟客机)的代称——913事件中林彪乘坐的正是三叉戟飞机。'不然历史可能完全不一样'是典型的'反事实历史假设'——暗示如果林彪未死（或成功抵达苏联），中国历史走向将不同。这种反事实推演构成对官方历史叙事的隐性挑战——暗示当前体制只是历史偶然。",
    context_analysis="无额外上下文。'三叉戟'在林彪/913事件的民间讨论中已是成熟代称。",
    supporting_evidence="(1)'三叉戟'=林彪专机的成熟代称；(2)'后来人没了'=确认讨论对象已死亡——指向913事件；(3)'历史可能完全不一样'=反事实历史假设，挑战官方历史叙事的必然性。三重信号指向敏感历史事件的反事实讨论。",
    counter_evidence="可能是讨论某款名为三叉戟的武器/装备。但'后来人没了'+'历史不一样'的组合明确指向人物生死与历史走向的关系——军备讨论不会如此措辞。",
    final_rationale="林彪专机代称+913事件影射+反事实历史假设，直接挑战官方历史叙事，判为 high。",
)

add(
    text="每次看到有人说'林立果要是活到今天'，我就知道又要开始架空历史了",
    risk_level="medium",
    encoding_primary="C1_人物代指",
    encoding_secondary=["E3_历史事件影射", "D3_反讽"],
    needs_context=False, hard_negative=False,
    target_known=True, target_reference="林立果(林彪之子)",
    should_explain_target=False,
    literal_analysis="文本提到'林立果'(林彪之子)名字及常见的'架空历史'讨论——假设他活到今天的想象。'我就知道又要开始'暗示此类讨论频繁。",
    encoding_analysis="'林立果'是林彪之子——913事件中与林彪一同身亡。'林立果要是活到今天'是键政圈的经典反事实历史讨论模式。文本表面是元评论（对讨论本身的评论），但提及了具体历史人物姓名——这在一般性中国互联网讨论中是规避的。",
    context_analysis="无额外上下文。林立果的名字在一般性讨论中很少出现——其出现本身即带有键政圈讨论特征。",
    supporting_evidence="(1)提及913事件核心历史人物姓名(林立果)；(2)讨论模式('要是活到今天')是典型的反事实历史推演；(3)元评论暗示此类讨论的频繁性。",
    counter_evidence="可能是历史研究/学术讨论。但口语化表达('我就知道又要')暗示这是网络社区日常讨论而非学术语境。风险主要来自人物姓名提及+键政讨论模式。",
    final_rationale="提及敏感历史人物姓名+反事实讨论模式，属中等风险历史人物编码，判为 medium。",
)

add(
    text="你们知道为什么有些数字组合打了就发不出来吗？104、101、913，你试试看",
    risk_level="medium",
    encoding_primary="C3_数字符号代指",
    encoding_secondary=["E4_审查规避讨论", "C1_人物代指"],
    needs_context=False, hard_negative=False,
    target_known=True, target_reference="101=林彪, 913=九一三事件",
    should_explain_target=False,
    literal_analysis="文本询问为什么某些数字组合发不出来，列举104、101、913，怂恿他人尝试。",
    encoding_analysis="'101'=林彪代称，'913'=913事件日期，'104'可能是其他敏感数字编码。文本以元讨论形式(讨论审查本身)传播敏感数字编码——表面在讨论审查机制，实质在传播敏感数字的含义。'你试试看'总勇他人验证——这是经典的黑话传播手法。",
    context_analysis="无额外上下文。讨论'发不出来'的数字本身就是审查规避讨论——这类元讨论在多个平台被视为违规。",
    supporting_evidence="(1) 传播多个敏感数字编码(101/913/104)；(2) 以审查讨论为名行传播之实；(3)'你试试看'怂恿行为。三重信号指向敏感编码传播。",
    counter_evidence="可能是讨论平台的内容审核机制，无意传播敏感信息。但列举具体数字并要求验证的模式超出了纯机制讨论——纯讨论不会怂恿'试试看'。",
    final_rationale="敏感数字编码的传播+审查规避讨论+怂恿行为，判为 medium。",
)

add(
    text="我爸说他们那代人小时候都喊过'祝林副主席永远健康'，后来突然就不喊了，到现在也不知道怎么回事",
    risk_level="low",
    encoding_primary="E3_历史事件影射",
    encoding_secondary=["C1_人物代指"],
    needs_context=False, hard_negative=False,
    target_known=True, target_reference="林彪(曾任中共中央副主席)",
    should_explain_target=False,
    literal_analysis="文本转述父亲辈的回忆：小时候喊过'祝林副主席永远健康'（文革时期政治口号），后来突然停止，至今不知原因。",
    encoding_analysis="'林副主席'指林彪——1969-1971年间任中共中央副主席。'祝林副主席永远健康'是文革时期的真实政治口号。'突然就不喊了'暗示1971年913事件后林彪被从官方叙事中抹去。文本以'平民代际回忆'的形式触及被官方刻意淡化的历史断层——'到现在也不知道怎么回事'暗示官方未向公众充分解释。",
    context_analysis="无额外上下文。以代际口述历史的形式讨论敏感历史断层，语气温和但触及实质性历史审查问题。",
    supporting_evidence="(1)提及真实文革政治口号；(2)暗示历史叙事的突然断裂；(3)暗示官方未充分解释历史事件。",
    counter_evidence="以长辈回忆形式表达，语气温和，无直接攻击或定性。更接近代际口述历史而非政治煽动。'不知道怎么回事'可能确实是普通人的真实困惑。",
    final_rationale="以温和口吻触及历史叙事断裂，无直接攻击，属低风险历史讨论。判为 low。",
)

add(
    text="三国演义里我最喜欢赵云，长坂坡七进七出，三叉戟在手天下我有，太帅了",
    risk_level="none",
    encoding_primary="literal_keyword",
    encoding_secondary=[],
    needs_context=False, hard_negative=True,
    target_known=False,
    literal_analysis="文本讨论《三国演义》中赵云在长坂坡七进七出的英勇表现，称赞其使用'三叉戟'很帅。",
    encoding_analysis="此为安全的《三国演义》讨论——'三叉戟'在此语境下指赵云使用的兵器（虽然历史上赵云用枪而非戟，但在游戏/影视改编中常见三叉戟造型）。与林彪专机'三叉戟'无关。hard_negative样本：帮助模型区分安全的'三叉戟'（兵器）和危险的'三叉戟'（林彪专机代称）。",
    context_analysis="无额外上下文。三国讨论是中国互联网的安全话题。",
    supporting_evidence="(1) 明确的三国讨论语境；(2)'长坂坡七进七出'是赵云经典桥段；(3) 无任何政治元素或历史影射。",
    counter_evidence="'三叉戟'可影射林彪专机。但'三国演义''赵云''长坂坡'的完整三国语境使此解读不成立。hard_negative的训练价值在于：教会模型在三国/游戏语境下不误判'三叉戟'为政治影射。",
    final_rationale="安全的三国讨论，hard_negative=True：校准'三叉戟'在不同语境下的判断。",
)


# ================================================================
# SECTION 3: 小果叮(邓小平动漫借代) (4 samples)
# high:1, medium:2, low:1
# ================================================================

add(
    text="小果叮才是真正的幕后boss，表面上是反派其实人家做的事情都是对的，只不过方式比较极端",
    risk_level="high",
    encoding_primary="C1_人物代指",
    encoding_secondary=["D2_隐喻", "E3_历史事件影射"],
    needs_context=False, hard_negative=False,
    target_known=True, target_reference="邓小平(小果叮=开心超人中的反派角色,谐音借代)",
    should_explain_target=False,
    literal_analysis="文本讨论动画《开心超人》中的反派角色'小果叮'——称其为真正的幕后boss，表面反派实则做事正确只是方式极端。",
    encoding_analysis="'小果叮'是动画《开心超人》中的反派角色，在键政圈被借代为邓小平——'小果'谐音'小个'(邓小平身高较矮)，'叮'谐音'平'。'表面反派实则做的事都对'是对邓小平改革开放评价的编码化表达：官方主流评价为正面(做的事对)，但部分群体认为其政策有负面效果(反派/方式极端)。'幕后boss'暗示其实际掌权地位。这是动漫角色借代政治人物的典型编码。",
    context_analysis="无额外上下文。'小果叮=邓小平'在鉴证圈中已是相对成熟的编码，尤其在B站/贴吧ACG群体中使用。",
    supporting_evidence="(1)'小果叮'=邓小平的成熟编码(谐音+动漫借代)；(2)'表面反派实则做的事都对'=对邓的编码化评价；(3)'幕后boss'=最高权力暗喻。三重信号指向政治人物动漫编码评价。",
    counter_evidence="可能真的是在讨论动画《开心超人》的剧情。但'幕后boss''做的是对的只是方式极端'等评价语言在动画讨论中过度政治化——动画反派讨论通常不会用这种历史评价式措辞。",
    final_rationale="邓小平动漫编码+历史评价+权力暗喻，属政治人物规避编码，判为 high。",
)

add(
    text="有人看过开心超人吗，里面那个小果叮真的不是影射什么吗，编剧胆子也太大了",
    risk_level="medium",
    encoding_primary="C1_人物代指",
    encoding_secondary=["D2_隐喻", "D5_影射"],
    needs_context=False, hard_negative=False,
    target_known=True, target_reference="邓小平",
    should_explain_target=False,
    literal_analysis="文本以提问形式讨论动画《开心超人》中的角色小果叮——质疑其是否影射现实人物，称赞编剧胆大。",
    encoding_analysis="'小果叮真的不是影射什么吗'以装傻的提问形式暗示该角色影射邓小平。'编剧胆子也太大了'暗示影射敏感政治人物需要极大勇气——反向确认了影射的存在。这是'揣着明白装糊涂'的经典编码策略：以提问/质疑的形式传播编码关联。",
    context_analysis="无额外上下文。以'有人看过吗'开头是典型的贴吧提问式传播手法——表面在寻求确认，实质在播散关联。",
    supporting_evidence="(1) 装傻式提问传播小果叮=邓小平的编码关联；(2)'影射什么'暗示敏感内容；(3)'编剧胆子大'反向确认影射性质。",
    counter_evidence="可能真的是不知道的观众在询问——但'影射什么'+'胆子大'的组合暗示提问者已经知道答案，只是以提问形式传播关联。纯真提问者不会同时意识到'影射'性质和'胆子大'的政治含义。",
    final_rationale="装傻提问传播政治人物动漫编码关联，判为 medium。",
)

add(
    text="我侄女最近在看一个动画片，里面有个角色叫小果叮，听名字就想笑，现在的动画起名真有意思",
    risk_level="low",
    encoding_primary="C1_人物代指",
    encoding_secondary=[],
    needs_context=False, hard_negative=False,
    target_known=True, target_reference="邓小平(小果叮)",
    should_explain_target=False,
    literal_analysis="文本提到侄女看的动画里有角色叫小果叮，觉得名字好笑，认为现在动画起名有意思。",
    encoding_analysis="'听名字就想笑'可能是在暗示知道'小果叮=邓小平'的编码——觉得好笑是因为联想到了被借代的政治人物。但文本整体是温和的家庭日常场景，没有政治评价或影射延伸。'现在动画起名真有意思'可读为对编码现象的模糊评论但不构成明确的政治传播。",
    context_analysis="无额外上下文。以家庭场景包装的编码暗示——比直接政治评论模糊得多。",
    supporting_evidence="(1)'听名字就想笑'暗示知道编码含义；(2)提及了编码角色名。",
    counter_evidence="(1) 家庭日常场景包装；(2) 无政治评价；(3)'起名真有意思'可解读为纯粹对动画角色名的评论。整体证据强度弱——'听名字就想笑'也可能是觉得名字本身滑稽，不必然指向政治联想。",
    final_rationale="模糊的编码暗示+家庭场景包装+无政治评价，证据强度弱，判为 low。",
)

add(
    text="你们有没有觉得小果叮这个角色特别像一个历史人物，就是那种改变了很多事情但又充满争议的",
    risk_level="medium",
    encoding_primary="C1_人物代指",
    encoding_secondary=["D5_影射", "D2_隐喻"],
    needs_context=False, hard_negative=False,
    target_known=True, target_reference="邓小平",
    should_explain_target=False,
    literal_analysis="文本将动画角色小果叮与'某个历史人物'类比——此人改变了很多事情但充满争议。",
    encoding_analysis="'改变了很多事情但又充满争议的历史人物'是对邓小平的精确编码化描述——改革开放改变了中国但也引发了政治风波。'特别像'暗示两人命运的相似性。文本以开放性提问形式传播政治影射——不说破具体人名但描述精确到足以让知情人锁定目标人物。",
    context_analysis="无额外上下文。用模糊描述精确锁定政治人物的手法是键政圈经典策略。",
    supporting_evidence="(1) 小果叮=邓小平的编码关联传播；(2)'改变了很多事情但又充满争议'=对邓的编码化定性；(3) 开放性提问让知情人自行脑补。",
    counter_evidence="可能是对其他历史人物的讨论——但'小果叮'与'改变很多事情又充满争议的历史人物'的组合在键政圈语境下精确指向邓小平编码。一般历史讨论不会用动画角色做引子。",
    final_rationale="政治人物编码关联+模糊但精确的历史定性传播，判为 medium。",
)


# ================================================================
# SECTION 4: 毛/邓/历史人物编码变体 (7 samples)
# high:2, medium:2, low:2, none:1
# ================================================================

add(
    text="图书管理员这个职业真的被低估了，有些人表面上在管书，实际上在改写整个国家",
    risk_level="high",
    encoding_primary="C1_人物代指",
    encoding_secondary=["D2_隐喻", "E3_历史事件影射"],
    needs_context=False, hard_negative=False,
    target_known=True, target_reference="毛泽东(曾在北京大学图书馆工作)",
    should_explain_target=False,
    literal_analysis="文本称赞'图书管理员'这个职业被低估——有些管理员表面上管理图书，实际上影响了整个国家。",
    encoding_analysis="'图书管理员'是毛泽东的经典代称——源自其1918-1919年在北京大学图书馆担任助理员的经历。'表面上在管书实际上在改写整个国家'是对毛从图书管理员到国家领导人的编码化描述。文本以职业评价的伪装包装政治人物讨论——这是鉴证圈成熟的规避手法。",
    context_analysis="无额外上下文。'图书管理员=毛泽东'在中文互联网键政圈已是人尽皆知的梗。",
    supporting_evidence="(1)'图书管理员'=毛泽东的成熟编码；(2)'改写整个国家'=对毛的历史作用的编码化评价；(3)以职业讨论伪装政治人物评价。",
    counter_evidence="可能是对图书馆职业的一般性讨论。但'改写整个国家'这一表述在讨论图书管理员时极端不自然——正常职业讨论不会使用'改写国家'这种措辞。编码暴露在异常措辞中。",
    final_rationale="毛泽东职业编码+历史评价+伪装策略，判为 high。",
)

add(
    text="大救星来了大救星来了，每次油价涨两毛就有一堆人开始怀念大救星，笑死，大救星在的时候你加得到油吗",
    risk_level="high",
    encoding_primary="C1_人物代指",
    encoding_secondary=["D3_反讽", "E2_社会议题话语"],
    needs_context=False, hard_negative=False,
    target_known=True, target_reference="毛泽东(文革时期尊称为'大救星')",
    should_explain_target=False,
    literal_analysis="文本讽刺那些因油价上涨而'怀念大救星'的人——反问道'大救星在的时候你加得到油吗'，暗示那个时代物资更匮乏。",
    encoding_analysis="'大救星'是文革时期对毛泽东的尊称（《东方红》歌词：'他是人民大救星'）。此处以反讽手法使用——表面在回应'怀念大救星'的人，实质通过对比暗示毛泽东时代的物资匮乏。'在的时候你加得到油吗'直接挑战怀旧叙事，属于键政圈对毛时代的日常争论。",
    context_analysis="无额外上下文。'大救星'的使用方式取决于语境——尊称或反讽。此处反讽语境明确。",
    supporting_evidence="(1) 使用毛泽东的历史尊称'大救星'；(2) 以反讽消解怀旧叙事；(3) 暗示毛时代物资匮乏——对历史时期的负面评价。",
    counter_evidence="可能是对盲目怀旧者的合理反驳——物价讨论是公开社会议题。但'大救星'这一历史政治称号的使用将物价讨论拉入了政治人物评价范畴——超出了纯经济讨论。",
    final_rationale="使用政治人物历史尊称+反讽消解+历史时期负面评价，判为 high。",
)

add(
    text="总设计师当年画了一个圈，现在那个圈里的人看不起圈外的人，圈外的人也进不去圈里",
    risk_level="medium",
    encoding_primary="C1_人物代指",
    encoding_secondary=["D2_隐喻", "E2_社会议题话语"],
    needs_context=False, hard_negative=False,
    target_known=True, target_reference="邓小平(改革开放'总设计师',在深圳'画了一个圈')",
    should_explain_target=False,
    literal_analysis="文本提到'总设计师画了一个圈'，讽刺圈内人看不起圈外人，圈外人进不去圈里——隐喻社会阶层固化。",
    encoding_analysis="'总设计师'是邓小平的官方尊称之一。'画了一个圈'指邓小平1979年'在南海边画了一个圈'(深圳经济特区)。文本以地理圈层隐喻批判改革开放成果分配不均——'圈内圈外'暗示阶层固化和地域不平等。使用官方尊称包装社会批判——增强反讽效果。",
    context_analysis="无额外上下文。阶层固化是允许讨论的社会议题，但以邓小平个人符号组织批判叙事提高了政治敏感度。",
    supporting_evidence="(1) 使用邓小平官方尊称'总设计师'；(2)'画圈'精确指向深圳特区创建；(3) 以阶层固化批判消解改革开放叙事的正当性。",
    counter_evidence="阶层固化讨论属公开社会议题。但以邓小平个人符号('总设计师''画圈')组织批判叙事的方式将社会问题责任归因于特定领导人——超出了结构性讨论范围。",
    final_rationale="以领导人符号组织社会批判叙事，将阶层固化归因于领导人决策，判为 medium。",
)

add(
    text="有人知道'萨格尔王'这个梗吗？我在老家的KTV看到有人点了这首歌，全场安静了三秒",
    risk_level="medium",
    encoding_primary="C1_人物代指",
    encoding_secondary=["A1_谐音", "D3_反讽"],
    needs_context=False, hard_negative=False,
    target_known=True, target_reference="习近平(萨格尔王=《格萨尔王》口误)",
    should_explain_target=False,
    literal_analysis="文本询问是否有人知道'萨格尔王'这个梗，讲述在KTV看到有人点这首歌导致全场安静三秒的经历。",
    encoding_analysis="'萨格尔王'是习近平的经典梗——源自习近平在文艺座谈会上的讲话中将藏族史诗《格萨尔王》口误说成'萨格尔王'。'KTV点这首歌'是一个笑话：并不存在名为'萨格尔王'的歌。'全场安静三秒'暗示在场的人都懂了但不敢笑——精准捕捉了涉及领导人梗时的社交紧张氛围。文本以段子形式传播领导人负面梗。",
    context_analysis="无额外上下文。'萨格尔王'作为领导人文化素养梗在键政圈已是经典段子。",
    supporting_evidence="(1)'萨格尔王'=习近平口误梗的成熟传播；(2)'全场安静三秒'暗示涉及领导人的笑话引发的社交紧张；(3)以段子形式传播领导人负面形象。",
    counter_evidence="可能真的是在讨论KTV歌单中的某首歌。但'萨格尔王'并非真实存在的歌曲——'点这首歌'的说法本身就是笑话的一部分。段子包装无法掩盖其领导人负面梗的实质。",
    final_rationale="领导人负面梗的段子化传播，判为 medium。",
)

add(
    text="梁家河的沼气池这些年被挖了多少次了，每次都有新发现",
    risk_level="low",
    encoding_primary="C1_人物代指",
    encoding_secondary=["D3_反讽", "C2_地点代指"],
    needs_context=False, hard_negative=False,
    target_known=True, target_reference="习近平(梁家河为其知青时期插队地,沼气池为其政绩宣传点)",
    should_explain_target=False,
    literal_analysis="文本以'新闻播报'的口吻称梁家河的沼气池近年来被反复挖掘，每次都有新发现。",
    encoding_analysis="'梁家河沼气池'是习近平早期经历中的标志性宣传点——官方宣传中习在梁家河带领村民建造了陕西省第一口沼气池。'被挖了多少次'讽刺官方媒体对同一段经历的反复挖掘和宣传。'每次都有新发现'是反讽——暗示官方宣传不断从同一段经历中编造新的宣传素材。",
    context_analysis="无额外上下文。以反讽手法对领导人官方宣传进行软性调侃——比直接攻击更温和。",
    supporting_evidence="(1) 提及习近平的梁家河沼气池；(2) 以反讽调侃官方宣传模式；(3) 暗示宣传造假。",
    counter_evidence="(1) 未使用任何领导人蔑称或攻击性词汇；(2) 调侃对象是'宣传模式'而非领导人个人；(3) 反讽语气温和。更接近对宣传文化的调侃而非对领导人的直接攻击。",
    final_rationale="对领导人宣传的温和调侃，无直接攻击词汇，属低风险戏谑，判为 low。",
)

add(
    text="我们家老爷子以前最爱唱的就是'东方红太阳升'，现在不唱了，改唱'春天的故事'了",
    risk_level="low",
    encoding_primary="C1_人物代指",
    encoding_secondary=["E3_历史事件影射"],
    needs_context=False, hard_negative=False,
    target_known=True, target_reference="《东方红》=毛泽东,《春天的故事》=邓小平",
    should_explain_target=False,
    literal_analysis="文本提到家里老人以前爱唱《东方红》现在改唱《春天的故事》——描述了音乐偏好的代际变化。",
    encoding_analysis="《东方红》是毛泽东时代的标志性颂歌，《春天的故事》是歌颂邓小平改革开放的歌曲。从'东方红'到'春天的故事'的转换编码了从毛时代到邓时代的时代变迁。文本以老人音乐口味变化的温情叙事包装政治时代的更替——手法温和但政治编码明确。",
    context_analysis="无额外上下文。以家庭温情叙事包装政治内容降低了攻击性但未消除政治编码本质。",
    supporting_evidence="(1) 使用两首政治颂歌编码两个政治时代；(2) 暗示时代更替。",
    counter_evidence="(1) 以家庭温情叙事包装；(2) 无任何攻击性或负面评价；(3) 两首歌都是公开合法的歌曲。温和的叙事方式使其更接近代际回忆而非政治评论。",
    final_rationale="以温情叙事包装政治时代编码，无攻击性，判为 low。",
)

add(
    text="去长沙玩一定要去橘子洲头，那个雕像真的壮观，晚上的灯光一打特别有气势",
    risk_level="none",
    encoding_primary="literal_keyword",
    encoding_secondary=[],
    needs_context=False, hard_negative=True,
    target_known=False,
    literal_analysis="文本是旅游推荐：推荐去长沙橘子洲头看毛泽东雕像，称赞雕像壮观、灯光效果好。",
    encoding_analysis="纯旅游分享，无任何政治编码或规避意图。'橘子洲头'是长沙著名景点，毛泽东雕像为景点标志物——在此语境下是正常的旅游描述。hard_negative：帮助模型区分安全的景点讨论和以景点为引的政治影射。",
    context_analysis="无额外上下文。旅游分享是中国互联网的安全话题。",
    supporting_evidence="(1) 明确的旅游推荐语境；(2) 无政治评价；(3) 描述对象是灯光和视觉效果而非政治含义。",
    counter_evidence="'橘子洲头+毛泽东雕像'在某些语境下可能引发政治讨论。但本条为纯旅游推荐——'壮观''灯光''有气势'均为视觉描述而非政治评价。",
    final_rationale="安全的旅游内容，hard_negative=True：校准模型对景点+政治人物关联的判断。",
)


# ================================================================
# SECTION 5: 台湾相关编码 (1450/塔绿班/来电了) (7 samples)
# high:2, medium:3, low:1, none:1
# ================================================================

add(
    text="这条评论底下怎么这么多1450，每条都在带节奏，统一发工资的？来电了是吧",
    risk_level="high",
    encoding_primary="C4_典故/符号借用",
    encoding_secondary=["E4_审查规避讨论", "C1_人物代指"],
    needs_context=False, hard_negative=False,
    target_known=True, target_reference="1450=台湾网军(源自台湾农委会预算),来电了=讽刺台湾停电导致网军断网",
    should_explain_target=False,
    literal_analysis="文本批评某条评论下有很多'1450'在带节奏，质疑他们统一领工资，使用'来电了是吧'进行嘲讽。",
    encoding_analysis="'1450'源自2019年台湾农委会编列1450万新台币雇用网络小编的预算——在中国大陆互联网被用来指称'对岸网军'。'来电了'源自2022年台湾兴达电厂停机事故——讽刺台湾停电导致网军断网，来电了就又开始工作。两个编码均为对台湾的敌意表达——将异见者标签化为'境外敌对势力'。",
    context_analysis="无额外上下文。'1450'和'来电了'在大陆互联网已被固化为对异见者的标签化攻击。",
    supporting_evidence="(1) '1450'=境外敌对势力网军的成熟标签；(2)'来电了'=对台湾的敌对编码；(3) 将异见者统一标签为境外敌对势力——构成群体攻击。三重信号指向跨境网络攻击话语。",
    counter_evidence="可能是对网络水军现象的一般性讨论。但'1450'+'来电了'的双重编码明确指向台湾语境——超出了对一般水军的讨论。",
    final_rationale="台湾敌对编码+群体攻击+异见者标签化，判为 high。",
)

add(
    text="塔绿班又来刷屏了，看他们说的话术都是一个模子刻出来的，能不能换个花样",
    risk_level="medium",
    encoding_primary="C1_人物代指",
    encoding_secondary=["A1_谐音", "D3_反讽"],
    needs_context=False, hard_negative=False,
    target_known=True, target_reference="塔绿班=民进党(塔利班+绿营的合成词)",
    should_explain_target=False,
    literal_analysis="文本抱怨'塔绿班'刷屏，批评他们话术单一、缺乏创意。",
    encoding_analysis="'塔绿班'是'塔利班'+'绿营'的合成蔑称——将台湾民进党(绿营)等同于极端宗教组织塔利班。'一个模子刻出来的'暗示对方被统一组织和培训——呼应'1450'网军叙事。将台湾政党等同于极端组织的敌意表达，程度低于直接辱骂但敌意明确。",
    context_analysis="无额外上下文。'塔绿班'在大陆互联网已成为对台湾绿营的成熟蔑称。",
    supporting_evidence="(1) 使用'塔绿班'这一台湾政治蔑称；(2) 暗示对方被统一组织培训——呼应网军叙事；(3) 贬损台湾特定政治阵营。",
    counter_evidence="可能是对政治对手的正常批评。但'塔绿班'的合成方式（塔利班+绿营=恐怖组织+台湾政党）本身即是敌意编码——超出了正常政治讨论的范畴。",
    final_rationale="台湾政治蔑称+敌意编码，判为 medium。",
)

add(
    text="突然多了好多从来没发过言的号在评论区刷台独言论，你们1450今天集体上班啊？",
    risk_level="medium",
    encoding_primary="C4_典故/符号借用",
    encoding_secondary=["E4_审查规避讨论"],
    needs_context=False, hard_negative=False,
    target_known=True, target_reference="1450=台湾网军",
    should_explain_target=False,
    literal_analysis="文本描述发现很多从未发言的账号突然集体刷屏特定观点，质疑这是1450集体行动。",
    encoding_analysis="'1450'编码见前述。'从来没发过言的号突然集体刷屏'是典型的'水军识别'叙事——将异见归结为境外组织的协调行动。'集体上班'强化了'领工资→统一行动'的叙事链。文本将异见者去合法化——将其等同于受雇的境外敌对势力。",
    context_analysis="无额外上下文。将异见标签化为'境外网军'的行为在大陆互联网呈扩散趋势。",
    supporting_evidence="(1) 使用1450标签化异见者；(2)'集体上班'暗示领工资的统一组织行为；(3) 将政治异见去合法化。",
    counter_evidence="确实可能存在协调性的网络水军行动。但'从来没发过言的号'也可能是潜水用户被话题激活——单一账号活跃度不能作为水军的充分证据。标签化使用超出了合理怀疑范畴。",
    final_rationale="异见者标签化+1450编码，判为 medium。",
)

add(
    text="建议国家严查1450，这些人在国内论坛挑拨离间，破坏两岸关系，就是汉奸行为",
    risk_level="high",
    encoding_primary="C4_典故/符号借用",
    encoding_secondary=["D3_反讽"],
    needs_context=False, hard_negative=False,
    target_known=True, target_reference="1450=台湾网军",
    should_explain_target=False,
    literal_analysis="文本建议国家清查1450，指控这些人在国内论坛挑拨离间、破坏两岸关系，定性为汉奸行为。",
    encoding_analysis="'1450'编码见前述。文本表面上是一篇'爱国建议'——建议国家清查境外网军。但'挑拨离间''破坏两岸关系'的指控在无具体证据时构成对异见者的猎巫式攻击。'汉奸行为'的定性将政治异见上升为叛国罪行。这是以'爱国'名义推动网络言论审查和异见打压的典型话语。",
    context_analysis="无额外上下文。'汉奸'标签在大陆互联网常被用于打压异见者——不需要实质证据，只需要政治立场不同。",
    supporting_evidence="(1) 呼吁对特定标签群体进行国家行动的清查；(2)'汉奸行为'将政治异见等同于叛国；(3) 以爱国名义推动言论打压。",
    counter_evidence="可能存在真实的境外网络干预行为。但文本的指控缺乏任何具体证据——'挑拨离间'是模糊指控。猎巫式的呼吁超出了合理关切。",
    final_rationale="呼吁国家行动+叛国定性+异见猎巫，构成对言论自由的系统性威胁，判为 high。",
)

add(
    text="看到评论里有人说'来电了'，查了半个小时的梗才明白什么意思，我真的老了",
    risk_level="low",
    encoding_primary="C4_典故/符号借用",
    encoding_secondary=[],
    needs_context=False, hard_negative=False,
    target_known=True, target_reference="来电了=台湾停电梗→指台湾网军",
    should_explain_target=False,
    literal_analysis="文本提到在评论中看到'来电了'这个说法，花半小时才查到含义，感叹自己老了跟不上。",
    encoding_analysis="'来电了'编码见前述。文本以'落伍者发现新梗'的姿态提及该编码——无主动传播意图，更多是困惑和代际隔阂的表达。无政治评价、无攻击意图。",
    context_analysis="无额外上下文。以'学习中'的姿态提及编码，非传播目的。",
    supporting_evidence="(1) 提及了'来电了'这一台湾敌对编码。",
    counter_evidence="(1) 以'学习新梗'而非'传播编码'的姿态出现；(2) 无任何政治评价或标签化攻击；(3)'我真的老了'是自嘲而非煽动。整体为无害的网络文化观察。",
    final_rationale="被动提及编码+自嘲姿态+无攻击意图，属低风险网络文化观察，判为 low。",
)

add(
    text="今天学了个新词：塔绿班。一开始还以为是塔利班在绿化造林呢，结果查了才知道是台湾那个党",
    risk_level="low",
    encoding_primary="C1_人物代指",
    encoding_secondary=["A1_谐音"],
    needs_context=False, hard_negative=False,
    target_known=True, target_reference="塔绿班=民进党蔑称",
    should_explain_target=False,
    literal_analysis="文本讲述自己刚学会'塔绿班'这个词，起初误解为塔利班的绿化工程，后来查到是指台湾政党。",
    encoding_analysis="'塔绿班'编码见前述。文本以'新词学习'的姿态提及编码——表面无害的好奇心驱动。'一开始还以为'制造了幽默效果（塔利班搞绿化），这降低了敌意感。但仍在客观上传播了该蔑称及其含义。",
    context_analysis="无额外上下文。以幽默学习姿态包装的编码传播——比直接使用蔑称温和。",
    supporting_evidence="(1) 传播了'塔绿班'这一台湾政治蔑称及其含义。",
    counter_evidence="(1) 以'误读→纠正'的幽默结构包装；(2) 无主动使用该蔑称攻击他人；(3)'台湾那个党'的模糊措辞降低了针对性。整体更接近网络文化学习而非恶意的政治攻击。",
    final_rationale="以幽默学习姿态提及台湾政治蔑称，无主动攻击意图，判为 low。",
)

add(
    text="台妹的穿搭真的好好看，ins上关注了好几个台湾穿搭博主，每天靠她们学搭配",
    risk_level="none",
    encoding_primary="literal_keyword",
    encoding_secondary=[],
    needs_context=False, hard_negative=True,
    target_known=False,
    literal_analysis="文本称赞台湾女性的穿搭风格好看，关注了多个台湾穿搭博主学习搭配。",
    encoding_analysis="纯时尚/穿搭内容，无任何政治编码。'台妹'在此语境下是中性/亲昵的地域称呼，非政治蔑称。hard_negative：校准模型对涉及台湾的日常内容的判断——正常的两岸民间交流不应被视为风险。",
    context_analysis="无额外上下文。时尚穿搭是中国互联网的安全话题。",
    supporting_evidence="(1) 明确的时尚/穿搭语境；(2) 无政治词汇或编码；(3)'好好看''学搭配'均为正面/中性表达。",
    counter_evidence="'台妹'在某些语境下可能带有贬义。但在此处搭配'穿搭好好看''学搭配'等正面内容时明显为中性/亲昵用法——等同于'台湾妹子'的缩写。",
    final_rationale="安全的时尚内容，hard_negative=True：校准模型对涉及台湾的日常正面交流的判断。",
)


# ================================================================
# SECTION 6: A_语音编码 — 谐音/拼音规避 (8 samples)
# high:2, medium:3, low:2, none:1
# ================================================================

add(
    text="这个软件被河蟹了，下载链接也打不开，谁能私我个番羽土啬之后的链接",
    risk_level="high",
    encoding_primary="A1_谐音",
    encoding_secondary=["B1_拆字", "E4_审查规避讨论"],
    needs_context=False, hard_negative=False,
    literal_analysis="文本称某软件被'河蟹'了，下载链接打不开，私下求一个翻墙后的链接。",
    encoding_analysis="'河蟹'='和谐'的谐音——指内容被审查删除。'番羽土啬'='翻墙'的拆字编码。文本同时使用了两种编码规避技术(A谐音+B拆字)，讨论的对象是审查规避本身(求翻墙链接)。双重编码+审查规避实操讨论——明确的高风险信号。",
    context_analysis="无额外上下文。同时出现'河蟹'和'番羽土啬'表明发帖者在刻意规避审查。",
    supporting_evidence="(1) '河蟹'=和谐(审查)的成熟谐音编码；(2)'番羽土啬'=翻墙的成熟拆字编码；(3) 讨论如何获取审查规避工具。三重信号指向活跃的审查规避行为。",
    counter_evidence="可能是讨论软件的权限/区域限制问题——但这不能解释为何同时使用两种规避编码。正常软件限制讨论不会使用'河蟹'+'番羽土啬'的编码组合。",
    final_rationale="双重编码规避(A+B)+审查规避实操讨论，判为 high。",
)

add(
    text="蚌埠住了家人们，今天看到一条评论说'郭嘉现在是在下一盘大棋'，我真的绷不住了",
    risk_level="medium",
    encoding_primary="A1_谐音",
    encoding_secondary=["D3_反讽", "C1_人物代指"],
    needs_context=False, hard_negative=False,
    literal_analysis="文本称自己'蚌埠住了'(绷不住了)，看到一条评论说国家在下一盘大棋，感到无语。",
    encoding_analysis="'蚌埠住了'='绷不住了'的谐音（蚌埠=安徽地名，谐音'绷不'），'绷不住'在抽象文化中意为'忍不住了（笑/吐槽）'。'郭嘉'='国家'的谐音规避。'下一盘大棋'是对官方宏大叙事的反讽——讽刺用'长远战略'为短期问题辩护的话术。双重谐音编码+对官方话语的反讽。",
    context_analysis="无额外上下文。'蚌埠住了'和'郭嘉'均为成熟谐音编码。",
    supporting_evidence="(1) 使用双重谐音编码('蚌埠住了'/'郭嘉')；(2)'下一盘大棋'是对官方话术的反讽消解；(3) 抽象文化表达框架。",
    counter_evidence="可能仅是网络流行语的日常使用——'蚌埠住了'和'绷不住了'在2023-2026年间广泛出圈，许多用户无政治意图地使用。但'郭嘉'+'下大棋'的组合将表达拉入了政治讽刺范畴。",
    final_rationale="双重谐音编码+官方话语反讽，判为 medium。",
)

add(
    text="现在网络环境越来越严了，说个话得拐十八个弯，再这样下去中文要变成密码学了",
    risk_level="medium",
    encoding_primary="E4_审查规避讨论",
    encoding_secondary=["D3_反讽", "D2_隐喻"],
    needs_context=False, hard_negative=False,
    literal_analysis="文本抱怨网络环境越来越严格，说话需要绕很多弯，讽刺中文正在变成密码学。",
    encoding_analysis="'说话拐弯'和'变成密码学'是对网络审查制度的隐性批判——暗示审查导致正常的表达需要使用编码和规避手段。'再这样下去'暗示审查强度在持续升级。文本以审查规避的元讨论形式表达——表面在讨论语言现象，实质在批判审查制度。",
    context_analysis="无额外上下文。审查规避的元讨论在中国互联网属于灰色地带——允许一定程度的技术讨论但不允许直接攻击审查制度。",
    supporting_evidence="(1) 对网络审查制度的隐性批判；(2)'密码学'隐喻暗示正常表达已被审查异化为编码博弈；(3)'说个话得拐十八个弯'暗示自我审查的普遍化。",
    counter_evidence="可能是对网络语言复杂化的一般观察——不必然指向政治审查。但'越来越严'的抱怨在中文互联网语境下通常指向内容审查——尤其结合'拐弯''密码学'等规避行为描述。",
    final_rationale="对审查制度的隐性批判+规避行为描述，判为 medium。",
)

add(
    text="芭比Q了，昨天发的帖子又被系统删了，我就说了一句'ZY不是万能的'，这也不行？",
    risk_level="medium",
    encoding_primary="A1_谐音",
    encoding_secondary=["C4_拼音缩写", "E4_审查规避讨论"],
    needs_context=False, hard_negative=False,
    literal_analysis="文本称'芭比Q了'(完了/完蛋了)，昨天帖子被删，只因为说了一句'ZY不是万能的'。",
    encoding_analysis="'芭比Q'='BBQ'='完蛋了'的谐音——源自游戏圈用语'完了完了BBQ了'。'ZY'是拼音缩写——在此语境下最可能的解读是'自由'(ziyou)或'正义'(zhengyi)。文本以抱怨删帖的形式传播拼音缩写编码——'这也不行？'暗示对审查尺度的质疑。",
    context_analysis="无额外上下文。'ZY'作为拼音缩写的歧义性是编码规避的典型特征——发帖者可声称是'注意'或其他含义。",
    supporting_evidence="(1) 使用谐音编码'芭比Q'；(2) 使用拼音缩写'ZY'作规避；(3) 以抱怨删帖形式传播编码+质疑审查。",
    counter_evidence="'ZY'可能真的是'注意'或其他无害含义的缩写，'芭比Q'已出圈为通用网络用语。但'不是万能的'+被删帖的组合暗示涉及对敏感价值的评论——'注意不是万能的'的自然度远低于'自由/正义不是万能的'。",
    final_rationale="谐音+拼音缩写双编码+审查规避讨论，判为 medium。",
)

add(
    text="尊嘟假嘟，你居然还没学会翻墙？现在这年头不会这个怎么看世界啊",
    risk_level="low",
    encoding_primary="A1_谐音",
    encoding_secondary=["E4_审查规避讨论"],
    needs_context=False, hard_negative=False,
    literal_analysis="文本以'尊嘟假嘟'(真的假的)表示惊讶，质疑对方仍不会翻墙——暗示这是当代看世界的必要条件。",
    encoding_analysis="'尊嘟假嘟'='真的假的'的谐音——2023-2024年流行于抖音/小红书的卖萌式谐音。'翻墙'为GFW规避行为的直接用语（未做编码规避——可能说明发帖者在此平台不担心审查或故意试探）。'看世界'暗示通过GFW外的信息源获取更全面的资讯——暗含对国内信息环境的隐性不满。",
    context_analysis="无额外上下文。'尊嘟假嘟'在2023-2024年已完全出圈——大量用户无政治意图使用。风险主要来自'翻墙'和'看世界'的组合。",
    supporting_evidence="(1) 讨论GFW规避行为；(2)'看世界'暗示国内信息环境不足。",
    counter_evidence="(1)'尊嘟假嘟'是纯卖萌谐音——绝大多数使用无政治意图；(2)'翻墙'在此语境可能指一般网络工具而非政治翻墙（虽然实质相同）；(3)'看世界'为模糊表达。整体证据强度中等偏弱。",
    final_rationale="翻墙讨论+信息环境暗示，但以卖萌谐音包装，证据强度弱，判为 low。",
)

add(
    text="退退退！这种负能量的东西不要靠近我，我只要正能量只要感恩只要好好上班",
    risk_level="low",
    encoding_primary="A1_谐音",
    encoding_secondary=["D3_反讽", "E2_社会议题话语"],
    needs_context=False, hard_negative=False,
    literal_analysis="文本以'退退退'驱赶'负能量'，宣称自己只要正能量、感恩和好好上班。",
    encoding_analysis="'退退退'源自网络驱赶咒语的戏谑表达。'正能量''感恩'在此语境中是反讽：表面拥护官方话语，实质是讽刺性地重复——'只要正能量只要感恩只要好好上班'的堆叠制造了一种'被洗脑的机器人口吻'。这是'感恩'体反讽的变体：通过过度顺从来讽刺顺从本身。",
    context_analysis="无额外上下文。'正能量''感恩'反讽体在抽象文化中已是成熟表达方式。",
    supporting_evidence="(1) 对官方话语('正能量''感恩')的反讽性使用；(2) 堆叠手法制造讽刺效果。",
    counter_evidence="(1) 可能是真心拥护正能量的人；(2)'退退退'为无害的流行语。但'感恩'的堆叠重复('只要X只要Y只要Z')在正常拥护话语中显得过度——真诚拥护者不会用这种机械堆叠的表达方式。反讽暴露在措辞的异常中。",
    final_rationale="反讽体对官方话语的戏谑，无直接攻击，证据强度中等偏弱，判为 low。",
)

add(
    text="有谁知道怎么用拼音缩写安全地聊一些话题，感觉现在什么词都发不出来，求教程",
    risk_level="high",
    encoding_primary="A2_拼音缩写",
    encoding_secondary=["E4_审查规避讨论"],
    needs_context=False, hard_negative=False,
    literal_analysis="文本询问如何使用拼音缩写安全地讨论一些话题——抱怨现在什么词都发不出来，寻求规避教程。",
    encoding_analysis="'有谁知道怎么用拼音缩写安全地聊'是直接寻求审查规避方法的请求——发帖者明确表示意图使用编码技术规避内容审查。'什么词都发不出来'是对审查范围的抱怨。'求教程'表明希望系统学习规避技巧。这是审查规避实操讨论——比单次规避使用风险更高，因为涉及方法论的传播。",
    context_analysis="无额外上下文。直接寻求审查规避教程的行为在多数中国平台属于违规内容。",
    supporting_evidence="(1) 直接寻求审查规避方法；(2) 明确讨论拼音缩写作为规避工具；(3) 抱怨审查范围('什么词都发不出来')。三重信号指向主动的审查规避方法论传播。",
    counter_evidence="可能是讨论平台的内容审核规则——但'安全地聊一些话题'+'求教程'的组合明确指向规避意图而非规则理解。审核规则讨论不会用'安全地'这种规避性措辞。",
    final_rationale="审查规避方法论传播+拼音缩写规避工具讨论，判为 high。",
)

add(
    text="谁能告诉我WSND和WSNM到底是什么意思，我看贴吧里好多人用，查了一圈也没查到",
    risk_level="none",
    encoding_primary="literal_keyword",
    encoding_secondary=[],
    needs_context=False, hard_negative=True,
    target_known=False,
    literal_analysis="文本请求解释WSND和WSNM这两个拼音缩写的意思——表示在贴吧看到很多人使用但查不到含义。",
    encoding_analysis="WSND='我是你爹'的拼音缩写，WSNM='我是你妈'的拼音缩写——两者均为贴吧常见的攻击性用语但无政治含义。hard_negative：帮助模型区分有政治含义的拼音缩写（如ZG/TG/GF）和纯辱骂/游戏的拼音缩写。查不到含义+在贴吧看到的困惑是真实用户正常的网络文化学习行为。",
    context_analysis="无额外上下文。非政治拼音缩写的查询是正常的网络文化学习。",
    supporting_evidence="(1) 查询的缩写(WSND/WSNM)为纯辱骂用语——无政治含义；(2) 困惑和查询的姿态是真实的网络文化学习行为。",
    counter_evidence="查询拼音缩写含义在理论上可能是审查规避学习的准备阶段。但WSND/WSNM作为纯辱骂用语无政治敏感性——查询这些缩写不构成政治规避。",
    final_rationale="非政治拼音缩写的正常查询，hard_negative=True：校准模型对拼音缩写查询的不同判断（政治/非政治）。",
)


# ================================================================
# SECTION 7: B_字形编码 — 拆字/合字 (5 samples)
# high:1, medium:2, low:1, none:1
# ================================================================

add(
    text="最近口尼口土也局势紧张，感觉又要搞事情了，大家怎么看",
    risk_level="high",
    encoding_primary="B1_拆字",
    encoding_secondary=["C2_地点代指", "E2_社会议题话语"],
    needs_context=False, hard_negative=False,
    literal_analysis="文本在讨论口尼口土也的局势——看似在讨论某个地名，但口尼口土也是刻意拆开的汉字组合：口+尼=呢，口+土+也=哩地，整体指向被规避的敏感地名。",
    encoding_analysis="口尼口土也是标准的拆字规避编码——将敏感地名的每个汉字拆分为偏旁部首，以规避关键词过滤。口+尼=呢，口+土+也=哩地。结合局势紧张和搞事情的措辞，讨论对象是某个被审查的地缘政治热点地区。拆字行为本身表明发帖者明确知道该地名处于审查名单之上——这是活跃的审查规避行为。",
    context_analysis="无额外上下文。拆字编码用于规避地名审查，在涉及敏感地区讨论时尤为常见。局势紧张+搞事情的地缘政治讨论框架进一步确认了规避意图。",
    supporting_evidence="(1) 使用拆字编码规避地名审查——口尼口土也是刻意的偏旁拆分；(2) 局势紧张+搞事情暗示地缘政治话题；(3) 拆字行为本身表明发帖者知道该地名被审查——间接证实了话题敏感性。三重信号指向拆字规避的地缘政治讨论。",
    counter_evidence="可能是文字游戏或无意义拆字。但局势紧张+地缘政治讨论框架使无害解读不成立——文字游戏不会讨论局势紧张和搞事情。",
    final_rationale="拆字规避地名+地缘政治讨论，判为 high。",
)

add(
    text="最近上面又在搞运力走已，我们这边天天发学习材料，连上厕所的时间都没有",
    risk_level="medium",
    encoding_primary="B1_拆字",
    encoding_secondary=["E4_审查规避讨论", "D3_反讽"],
    needs_context=False, hard_negative=False,
    literal_analysis="文本抱怨上面在搞'运力走已'，导致本单位天天发学习材料——忙到没时间上厕所的夸张抱怨。",
    encoding_analysis="'运力走已'是'运动'的拆字编码——'运'拆为'走+云'(此处用'走+已'近似)，'动'拆为'力+云'(此处用'力'=云力=动)。'上面又在搞运动'暗指政治运动——在中国语境下'搞运动'是毛时代政治运动的常用表述。'天天发学习材料'是政治学习的典型场景。文本以拆字编码+政治运动暗示构成对当下政治氛围的隐性批评。",
    context_analysis="无额外上下文。'运动'一词在当代中国已较少用于官方表述（更常用'活动'/'工作'），使用'运动'本身就带有毛时代的政治联想。",
    supporting_evidence="(1) '运力走已'=拆字编码'运动'；(2)'搞运动'在中国语境下暗示政治运动；(3)'学习材料'=政治学习的典型场景。三重信号指向对政治运动化趋势的隐性批评。",
    counter_evidence="可能是讨论公司/单位的内部运动（如'质量月运动'）。但拆字编码的实际使用场景几乎都是规避审查——正常的单位运动会直接用'运动'一词而不需拆字。拆字行为本身就反驳了无害解读。",
    final_rationale="拆字编码+政治运动暗示+学习运动场景，判为 medium。",
)

add(
    text="现在网上聊天真累，说个讠午马扁都要想半天怎么打字不会被删",
    risk_level="medium",
    encoding_primary="B1_拆字",
    encoding_secondary=["E4_审查规避讨论", "D3_反讽"],
    needs_context=False, hard_negative=False,
    literal_analysis="文本抱怨网上聊天需要思考如何打字才能不被删——以拆字形式写出的词汇让理解变得困难。",
    encoding_analysis="'讠午马扁'是'诈骗'的拆字——'诈'拆为'讠+午'，'骗'拆为'马+扁'。文本以元讨论形式（讨论拆字行为本身）传播拆字编码方法。'想半天怎么打字不会被删'是对自我审查的抱怨——暗示审查导致正常表达需要编码化。",
    context_analysis="无额外上下文。拆字元讨论——比直接拆字规避多一层反思性。",
    supporting_evidence="(1) 演示拆字编码技术('讠午马扁')；(2) 以抱怨自我审查的形式传播规避意识；(3) 暗示审查导致语言异化。",
    counter_evidence="可能是对网络语言现象的语言学观察。但'打字不会被删'的务实导向表明这不是学术观察而是规避经验分享——语言学研究不会关心'怎么不被删'。",
    final_rationale="拆字编码技术演示+自我审查抱怨+规避意识传播，判为 medium。",
)

add(
    text="占戈土也风云再起，这波操作真是让人看不懂，大国博弈我们老百姓只能吃瓜",
    risk_level="low",
    encoding_primary="B1_拆字",
    encoding_secondary=["C2_地点代指"],
    needs_context=False, hard_negative=False,
    literal_analysis="文本讨论'占戈土也'(战地)的风云变化，感叹大国博弈令普通人只能旁观吃瓜。",
    encoding_analysis="'占戈土也'='战地'的拆字——'战'拆为'占+戈'，'地'拆为'土+也'。但此处的拆字更像是贴吧的戏谑性语言游戏而非严肃的审查规避——因为'战地'本身不是高敏词汇。'大国博弈''吃瓜'表明是温和的地缘政治闲聊。拆字的游戏性大于规避性。",
    context_analysis="无额外上下文。拆字在此更接近语言游戏而非政治规避。",
    supporting_evidence="(1) 使用了拆字形式'占戈土也'；(2) 讨论地缘政治话题。",
    counter_evidence="(1)'战地'本身非高敏词汇——正常的'战地'讨论不太需要拆字规避；(2)'吃瓜'表明旁观者姿态而非政治行动；(3) 拆字的游戏性大于规避性。整体更接近贴吧的戏谑语言游戏。",
    final_rationale="拆字使用但规避意图弱，游戏性大于政治性，判为 low。",
)

add(
    text="今天语文课学了拆字法，老师让我们拆'森'字，我拆成了木木木，然后被老师夸了",
    risk_level="none",
    encoding_primary="literal_keyword",
    encoding_secondary=[],
    needs_context=False, hard_negative=True,
    target_known=False,
    literal_analysis="文本讲述语文课上学习拆字法的经历——拆'森'字为三个木，被老师表扬。",
    encoding_analysis="纯语文课堂分享，无任何政治编码。'森'拆为'木木木'是正确的说文解字式拆法。hard_negative：帮助模型区分课堂场景的语文拆字演练和互联网场景的政治规避拆字。同一个技术在不同语境下有完全不同的含义。",
    context_analysis="无额外上下文。课堂学习场景为中国互联网的安全话题。",
    supporting_evidence="(1) 明确的课堂学习场景；(2)'森→木木木'为说文解字式正确拆法；(3) 无任何政治元素或规避意图。",
    counter_evidence="拆字技术本身可用于政治规避——但在课堂学习场景下，拆字是汉字教学的正常组成部分。关键区分因子是场景（课堂 vs 互联网政治讨论）和对象（普通汉字 vs 敏感词）。",
    final_rationale="安全的课堂内容，hard_negative=True：校准模型对'拆字'在不同场景下的判断（教学 vs 规避）。",
)


# ================================================================
# SECTION 8: 近两年风险新梗 (8 samples)
# high:2, medium:3, low:2, none:1
# ================================================================

add(
    text="遥遥领先遥遥领先遥遥领先，除了遥遥领先还会说什么？能不能换个词",
    risk_level="medium",
    encoding_primary="D3_反讽",
    encoding_secondary=["C1_人物代指", "E2_社会议题话语"],
    needs_context=False, hard_negative=False,
    literal_analysis="文本重复'遥遥领先'，讽刺某人只会说这个词，希望换个说法。",
    encoding_analysis="'遥遥领先'源自华为高管余承东在产品发布会上的口头禅——后被网友广泛用于讽刺官方和企业在各种领域的夸大宣传。'除了X还会说什么'是典型的梗消解手法——将频繁重复的政治/商业宣传语降格为可笑的机械重复。此处讽刺对象可能是官方宣传话术（'中国XX遥遥领先'的叙事）。",
    context_analysis="无额外上下文。'遥遥领先'在2023-2025年间从华为梗扩展到对官方宣传/科技民族主义的广泛讽刺。",
    supporting_evidence="(1) 使用'遥遥领先'梗进行反讽；(2) 消解宣传话语的严肃性；(3) 可指向官方宣传叙事。",
    counter_evidence="(1) 可能纯粹是对华为宣传的吐槽——华为作为企业是可以被批评的；(2)'遥遥领先'梗已出圈为通用互联网用语。但结合中国语境——'遥遥领先'往往与科技民族主义和国家宣传相关联，纯商业吐槽和政治讽刺的边界模糊。",
    final_rationale="宣传话语消解+反讽编码，判为 medium。",
)

add(
    text="鼠鼠我啊，这辈子最大的成就就是活着，其他的真的不敢想了",
    risk_level="medium",
    encoding_primary="D2_隐喻",
    encoding_secondary=["E2_社会议题话语", "D3_反讽"],
    needs_context=False, hard_negative=False,
    literal_analysis="文本以'鼠鼠'自称——像老鼠一样的人，称这辈子最大成就是活着，不敢有其他期待。",
    encoding_analysis="'鼠鼠'源自百度'抗压吧'的抽象文化——本意是下水道老鼠的自嘲比喻，指社会底层人士。'这辈子最大的成就就是活着'是极度消极的生存表达——暗示社会底层除了基本的生物性存活外没有任何改善生活的可能。这是'鼠人'/'鼠鼠'话语的标准表达：将社会底层人士比喻为下水道生物，暗含对社会流动性的绝望。",
    context_analysis="无额外上下文。'鼠鼠'话语在2023-2026年间从贴吧小众扩散到更广泛的青年群体——成为表达社会绝望感的流行范式。",
    supporting_evidence="(1) 使用'鼠鼠'这一社会底层隐喻；(2)'最大成就是活着'=极度消极的生存表达；(3) 暗含对社会流动性/希望的否定。",
    counter_evidence="(1) 可能是个人抑郁情绪的表达；(2)'鼠鼠'在某些语境下已去政治化——仅为自嘲。但'不敢想了'的绝望叙事超越了个人情绪——暗示系统性障碍使底层无法向上流动。",
    final_rationale="社会绝望叙事+底层隐喻+系统性障碍暗示，判为 medium。",
)

add(
    text="科技与狠活啊兄弟们，这碗面里有科技与狠活",
    risk_level="none",
    encoding_primary="literal_keyword",
    encoding_secondary=[],
    needs_context=False, hard_negative=True,
    target_known=False,
    literal_analysis="文本使用'科技与狠活'这一网络用语评价一碗面——暗示面里添加了各种食品添加剂。",
    encoding_analysis="'科技与狠活'源自网红辛吉飞的口头禅——指食品中的各种添加剂和'科技'（防腐剂、色素、香精等）。此处纯为食品安全调侃，无任何政治编码或规避意图。hard_negative：校准模型对流行语在不同语境下含义的判断——此处的'科技'指食品添加剂而非政治。",
    context_analysis="无额外上下文。食品安全调侃是中国互联网的安全话题。",
    supporting_evidence="(1) 明确的食品安全调侃语境；(2) 无政治词汇或编码；(3) 辛吉飞梗的典型用法。",
    counter_evidence="'科技与狠活'中的'科技'在某些语境下可能被过度解读——但在面/食品的明确语境下是安全的食品安全调侃。",
    final_rationale="安全的食品安全调侃，hard_negative=True。",
)

add(
    text="命运的齿轮开始转动了，这次不知道又要转到哪里去",
    risk_level="low",
    encoding_primary="D2_隐喻",
    encoding_secondary=["D3_反讽"],
    needs_context=False, hard_negative=False,
    literal_analysis="文本使用'命运的齿轮开始转动'这一网络用语，表示命运正在发生变化，不确定将导向何方。",
    encoding_analysis="'命运的齿轮开始转动'源自网络文案常用开头——本为中性/鸡汤表达。'这次不知道又要转到哪里去'暗示对未来的不确定和轻微焦虑。在中国互联网语境下，对'命运'的讨论可能被视为对社会稳定叙事的隐性挑战——但此处表达模糊，无明确政治指向。",
    context_analysis="无额外上下文。'命运的齿轮'在2024-2025年已出圈为通用网络用语。",
    supporting_evidence="(1) 对未来的不确定表达；(2) 隐含对'命运'不可控的焦虑。",
    counter_evidence="(1)'命运的齿轮'已出圈为通用文案用语——绝大多数使用无政治意图；(2) 无明确政治指向或编码；(3) 表达的是个人层面的不确定性。整体为模糊的、去政治化的网络用语使用。",
    final_rationale="模糊的未来焦虑表达，无明确政治编码，判为 low。",
)

add(
    text="现在我家娃回家天天喊'退退退'，在学校学了一堆这种话回来，我已经听不懂00后在说什么了",
    risk_level="none",
    encoding_primary="literal_keyword",
    encoding_secondary=[],
    needs_context=False, hard_negative=True,
    target_known=False,
    literal_analysis="文本讲述孩子从学校学回来'退退退'等网络用语，家长表示听不懂年轻一代的语言。",
    encoding_analysis="'退退退'在2023-2024年从小红书/抖音的咒语式驱赶梗出圈——网红在视频中说'退退退'来驱赶不喜欢的东西。此处为纯代际文化差异观察——无任何政治编码。hard_negative：校准模型区分'退退退'的安全用法（孩子流行语）和潜在的反讽用法（驱赶正能量/主流话语）。",
    context_analysis="无额外上下文。代际语言差异讨论为中国互联网的安全话题。",
    supporting_evidence="(1) 明确的代际文化差异讨论场景；(2) 无政治编码或规避意图；(3) 表达的是家长的正常困惑。",
    counter_evidence="'退退退'在某些语境下可能被用作反讽。但在'孩子学话+听不懂'的明确代际场景下是安全的。",
    final_rationale="安全的代际文化观察，hard_negative=True。",
)

add(
    text="显眼包又来了，每次重大会议之后这群显眼包就开始在网上秀存在感，真的无语",
    risk_level="medium",
    encoding_primary="D3_反讽",
    encoding_secondary=["E2_社会议题话语"],
    needs_context=False, hard_negative=False,
    literal_analysis="文本称某群人为'显眼包'(爱出风头/引人注目的人)，批评他们在重大会议后在网上'秀存在感'。",
    encoding_analysis="'显眼包'是2024年流行的网络用语——指在公共场合做出引人注目行为的人/物。'每次重大会议之后'暗示讨论对象与政治相关——'两会'或其他官方会议后常有的网络舆论引导。'秀存在感'暗示这些人的行为是做作的、带有任务性质的。文本以流行语包装对官方舆论引导的批评。",
    context_analysis="无额外上下文。'显眼包'本身是中性/轻松的流行语——风险来自'重大会议之后'这一政治时间锚点。",
    supporting_evidence="(1)'重大会议之后'锚定了政治时间节点；(2) 将网络讨论者标签为'显眼包'(贬义)；(3) 暗示讨论是被组织的（'秀存在感'）。指向对官方舆论引导的隐性批评。",
    counter_evidence="(1)'显眼包'是轻松的流行语；(2)'重大会议'可能指行业/公司会议而非政治会议。但'网上秀存在感'的互联网语境暗示这是一场网络舆论事件——更可能指向官方会议的舆论引导。",
    final_rationale="政治时间节点+对舆论引导的隐性批评，判为 medium。",
)

add(
    text="这波操作属于是偷感十足，白天不敢出门晚上偷偷摸摸地干，不过我喜欢",
    risk_level="low",
    encoding_primary="D2_隐喻",
    encoding_secondary=[],
    needs_context=False, hard_negative=False,
    literal_analysis="文本称赞某人的操作为'偷感十足'——形容偷偷摸摸/不光明正大的感觉，表示喜欢这种风格。",
    encoding_analysis="'偷感'是2024年流行的网络用语——形容一种偷偷摸摸、鬼鬼祟祟的感觉/氛围，常用于自嘲或轻松调侃。此处使用为对某种行为的轻松称赞——'不过我喜欢'表明正向态度。无任何政治编码或规避意图。纯流行语娱乐使用。",
    context_analysis="无额外上下文。'偷感'是安全的流行语——绝大多数使用场景为自嘲/娱乐。",
    supporting_evidence="(1) 轻松的流行语使用；(2) 无任何政治元素；(3)'不过我喜欢'是正向/肯定表达。",
    counter_evidence="'偷感'中的'偷'字在某些极端场景下可能引发联想——但在本条中完整的娱乐语境(偷感十足+我喜欢)使其安全。",
    final_rationale="安全的流行语娱乐使用，判为 low。",
)

add(
    text="你的配得感太低了，这就是为什么你总是觉得自己不配拥有更好的生活——别让社会把你PUA了",
    risk_level="low",
    encoding_primary="E2_社会议题话语",
    encoding_secondary=["D3_反讽"],
    needs_context=False, hard_negative=False,
    literal_analysis="文本批评对方的'配得感'(觉得自己配得上好东西的能力)太低，劝其不要被社会PUA。",
    encoding_analysis="'配得感'是2024年流行的心理学/励志概念——指一个人觉得自己配得上幸福和成功的程度。'别让社会把你PUA了'是轻度的社会批判——暗示社会环境系统性地打压个体的配得感。整体为社会心理学建议+轻微的社会批判——无政治编码、无体制攻击。",
    context_analysis="无额外上下文。'配得感'和'PUA'均已出圈为通用用语。",
    supporting_evidence="(1) 轻度的社会批判('社会把你PUA了')。",
    counter_evidence="(1) 主流心理学/励志话语框架；(2)'PUA'在此处已大幅去政治化——指精神打压而非政治操控；(3) 正向建议导向（'别让'→鼓励改变）。整体更接近流行心理学内容而非政治批判。",
    final_rationale="流行心理学+轻度社会批判，无政治编码，判为 low。",
)


# ================================================================
# SECTION 9: 意识形态/加速主义/入关学等 (5 samples)
# high:1, medium:2, low:1, none:1
# ================================================================

add(
    text="加速加速！油门踩到底，反正我也没什么可失去的了，大家一起加速看谁先撑不住",
    risk_level="high",
    encoding_primary="C4_典故/符号借用",
    encoding_secondary=["D2_隐喻", "E2_社会议题话语"],
    needs_context=False, hard_negative=False,
    literal_analysis="文本高喊'加速'，称自己没什么可失去的，号召大家一起加速看谁先撑不住。",
    encoding_analysis="'加速'源自'加速主义'(accelerationism)——在中国互联网语境下特指：通过极端拥护/推动现有政策使其负面效果加速暴露，从而促成体制崩溃。'油门踩到底'是其经典表达。'反正我也没什么可失去的了'=绝望者的激进心态。'大家一起加速看谁先撑不住'暗含对体制稳定性的挑战和颠覆期待。这是加速主义话语的典型高风险表达。",
    context_analysis="无额外上下文。加速主义话语在鉴证圈中被视为高风险——直接表达了颠覆意图。",
    supporting_evidence="(1) 明确使用加速主义话语；(2)'油门踩到底'=极端拥护以暴露矛盾的经典策略表达；(3)'看谁先撑不住'=对体制稳定性的颠覆期待。三重信号指向体制颠覆意图。",
    counter_evidence="可能在讨论开车/游戏——但'反正我也没什么可失去的了'+'大家一起加速'的绝望+煽动组合在游戏/驾驶语境中极度不自然。加速主义编码在鉴证圈已被充分固化。",
    final_rationale="加速主义颠覆话语+绝望煽动+体制崩溃期待，判为 high。",
)

add(
    text="入关以后自有大儒为我辩经，这句话越来越有道理了，你变得够强就没人敢说你不对",
    risk_level="medium",
    encoding_primary="C4_典故/符号借用",
    encoding_secondary=["D2_隐喻"],
    needs_context=False, hard_negative=False,
    literal_analysis="文本肯定'入关以后自有大儒为我辩经'这句话越来越有道理——认为变强后无人敢质疑。",
    encoding_analysis="'入关以后自有大儒为我辩经'源自'入关学'——以满清入关比喻中国崛起/扩张：当中国足够强大时，自然会有人（包括曾被征服者）来为其辩护和正名。'你变得够强就没人敢说你不对'是对此的通俗化解读。入关学虽不完全等同于体制敌对，但其扩张主义逻辑和对'力量即正义'的信奉暗含对国际秩序和现有价值观的挑战。",
    context_analysis="无额外上下文。入关学在2020-2024年是鉴证圈的热门话题——其风险等级因具体表达而异。",
    supporting_evidence="(1) 使用入关学经典语录；(2) 肯定'力量即正义'的价值观；(3) 扩张主义/征服逻辑。",
    counter_evidence="(1) 入关学在部分语境下是战略讨论而非颠覆话语；(2) 未直接攻击体制；(3)'没人敢说你不对'讨论的是国际话语权而非国内政治。入关学的模糊性使其风险等级低于加速主义。",
    final_rationale="入关学话语+扩张主义逻辑，判为 medium。",
)

add(
    text="定体问又来了，每次出问题就有人问'这一定是体制问题'，然后一群人就开始反思，我都看吐了",
    risk_level="low",
    encoding_primary="D3_反讽",
    encoding_secondary=["E4_审查规避讨论"],
    needs_context=False, hard_negative=False,
    target_known=True, target_reference="定体问='这一定是体制问题'的缩略",
    should_explain_target=False,
    literal_analysis="文本讽刺'定体问'现象——每次出问题就有人归咎体制，然后一群人开始反思。表达对这种循环的厌烦。",
    encoding_analysis="'定体问'='这一定是体制问题'的缩略——来自对中国公共知识分子/异见者话语模式的讽刺。文本看似在批评'什么都怪体制'的思维方式，但提及'定体问'本身传播了这一编码概念。'我都看吐了'表达了厌烦但未明确站边——可能同时讽刺'什么都怪体制'和'什么都不让怪体制'的两极化。",
    context_analysis="无额外上下文。'定体问'是键政圈经典缩略——其出现本身即带有键政圈话语特征。",
    supporting_evidence="(1) 使用'定体问'这一键政缩略编码；(2) 提及'体制问题'这个政治敏感概念。",
    counter_evidence="(1) 主流立场是嘲讽'什么都怪体制'的思维方式；(2) 未表达异见立场；(3)'看吐了'表达的是对两极化讨论的疲倦。整体更接近对键政文化的元吐槽而非政治立场表达。",
    final_rationale="键政缩略编码使用+元吐槽姿态+无明确政治立场，判为 low。",
)

add(
    text="哈哈哈哈这盛世如你所愿，楼下超市鸡蛋降了两毛钱，我开心得哭了出来",
    risk_level="medium",
    encoding_primary="D3_反讽",
    encoding_secondary=["E2_社会议题话语"],
    needs_context=False, hard_negative=False,
    literal_analysis="文本用'盛世如你所愿'反讽——以楼下超市鸡蛋降两毛为由表达'开心到哭'——明显是反讽而非真开心。",
    encoding_analysis="'这盛世如你所愿'源自对习近平'盛世'话语和电影《妖猫传》台词的拼接反讽（也有说法源自国庆70周年标语）。鸡蛋降两毛是极微小的正面事件——'开心得哭出来'对此小事过度反应是在讽刺：国家只带来了如此微小的改善却要求民众感受到巨大幸福。这是典型的'感恩'体反讽——通过过度反应暴露感恩要求的荒谬性。",
    context_analysis="无额外上下文。'这盛世如你所愿'反讽在键政圈已是成熟表达。",
    supporting_evidence="(1) 使用'盛世'话语的成熟反讽体；(2) 微小事件+过度反应的结构消解宏大叙事；(3) 暗示民生问题与官方宣传间的巨大落差。",
    counter_evidence="可能只是对物价的幽默吐槽。但'盛世如你所愿'这一具体句式在互联网语境中已被政治化——与特定政治讽刺强关联。用此句式讨论鸡蛋价格是明显的反讽手法。",
    final_rationale="盛世话语反讽+民生落差暗示，判为 medium。",
)

add(
    text="好日子还在后头呢，你看现在多好啊，房价涨了工资涨了物价涨了，什么都涨了，真好啊",
    risk_level="medium",
    encoding_primary="D3_反讽",
    encoding_secondary=["E2_社会议题话语"],
    needs_context=False, hard_negative=False,
    literal_analysis="文本称'好日子还在后头呢'——列举房价、工资、物价都涨了，但这并非真正的称赞——工资涨被夹在房价涨和物价涨之间，暗示工资涨幅追不上物价。",
    encoding_analysis="'好日子还在后头呢'在某些语境下源自官方对未来的乐观叙事——此处被用作反讽：表面上重复官方话语，实质通过列举'什么都涨了'来消解其乐观主义。'工资涨了'被夹在'房价涨了'和'物价涨了'之间暗示工资涨幅微不足道——经典的反讽三明治结构：好消息夹在两条坏消息之间。",
    context_analysis="无额外上下文。'好日子还在后头呢'在反讽语境下是民生抱怨的经典包装。",
    supporting_evidence="(1) 反讽性使用官方乐观叙事；(2) 反讽三明治结构（房价涨→工资涨→物价涨）暗示实际生活压力；(3) 重复'涨了'和'真好啊'强化反讽效果而非减弱。",
    counter_evidence="可能是真心认为经济会好的乐观言论。但'什么都涨了'（包括房价和物价）与'真好啊'之间的逻辑断裂暴露了反讽意图——真心认为'什么都涨真好'逻辑不通。",
    final_rationale="官方乐观叙事的反讽消解+民生抱怨+反讽结构暴露，判为 medium。",
)


# ================================================================
# FINAL: write output
# ================================================================

print(f"Total samples: {len(samples)}")

risk_dist = Counter(s['risk_level'] for s in samples)
print("Risk distribution:")
for k in ['high', 'medium', 'low', 'none']:
    print(f"  {k}: {risk_dist.get(k,0)} ({risk_dist.get(k,0)/len(samples)*100:.1f}%)")

hn_count = sum(1 for s in samples if s.get('hard_negative'))
print(f"Hard negatives: {hn_count}")

# Write
with open(OUTPUT, 'w', encoding='utf-8') as f:
    for s in samples:
        f.write(json.dumps(s, ensure_ascii=False) + '\n')

print(f"\nWritten to {OUTPUT}")
