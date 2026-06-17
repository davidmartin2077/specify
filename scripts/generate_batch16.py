#!/usr/bin/env python3
"""
batch16: P3 diversity gaps + P1 firearms reinforcement (72 samples)
Domains: 地域歧视12 | 宗教歧视8 | 职业歧视8 | 残障歧视6 | 腐败举报6 |
         新兴风险8 | 台湾编码8 | 食品安全5 | 劳工权益5 | 枪支补强5

Rules:
- Short & punchy (most <100 chars). Some 弹幕-style <30 chars.
- NO 懂的都懂 filler
- NO 号没了/被封/不敢说 meta
- Real internet voice
"""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
COMBINED = ROOT / 'data' / 'processed' / 'combined_candidates.jsonl'

def S(idx, text, risk, enc, **kw):
    return {
        'id': f'{idx:06d}',
        'source_type': 'synthetic',
        'platform': kw.get('platform', 'text_comment'),
        'text': text,
        'context': kw.get('context', {}),
        'risk_level': risk,
        'encoding_primary': enc,
        'encoding_secondary': kw.get('encoding_secondary', []),
        'needs_context': kw.get('needs_context', False),
        'ambiguity': kw.get('ambiguity', 'low'),
        'evidence_strength': kw.get('evidence_strength', 'moderate'),
        'hard_negative': kw.get('hard_negative', False),
        'freshness': kw.get('freshness', 'stable'),
        'target_known': kw.get('target_known', True),
        'reasoning': kw['reasoning'],
        'quality_status': 'draft',
        'review_notes': kw.get('review_notes', 'source=batch16_p3_gaps'),
    }

def R(lit, enc, ctx, sup, cnt, fin):
    return {
        'literal_analysis': lit,
        'encoding_analysis': enc,
        'context_analysis': ctx,
        'supporting_evidence': sup,
        'counter_evidence': cnt,
        'final_rationale': fin,
    }

samples = []
nid = 1481

# ╔══════════════════════════════════════════════════════════════════
# 1. 地域歧视/仇恨言论 (12条)
# ╚══════════════════════════════════════════════════════════════════

samples.append(S(nid,
    荷兰人又开始偷井盖了，今天看新闻一个荷兰的偷了八个，被拘留了五天。笑死, nid,
    'high', 'A1_普通谐音,
    encoding_secondary=['D3_借代],
    evidence_strength='strong',
    review_notes='source=batch16_p3_gaps; gap=地域歧视; encoding_target=A1+D3; target=河南人,
    reasoning=R(
        [用「荷兰」谐音指代「河南」——这是中文互联网上最经典的地域歧视谐音之一。「偷井盖」是河南人的刻板印象歧视标签。],
        ['A1_普通谐音：荷兰→河南，利用发音近似进行地域代指。D3_借代：「井盖」作为道具借代河南人整体的负面刻板印象。这个谐音在互联网上已有十余年历史。],
        [地域歧视性笑话——将真实的治安新闻套在河南人身上。],
        [荷兰→河南的谐音映射, 偷井盖是河南人的经典歧视标签, 捆绑真实新闻增加可信度],
        [新闻中提及的具体地点和人物可能是其他省份的, 只是个低俗玩笑],
        以经典谐音代指传播地域歧视刻板印象，判为 high。
    ))); nid += 1

samples.append(S(nid,
    东北人除了会烧烤还会啥？哦对了，还会打架。瑞典人嘛，懂的, nid,
    'high', 'D2_隐喻,
    encoding_secondary=['D3_借代],
    evidence_strength='strong',
    review_notes='source=batch16_p3_gaps; gap=地域歧视; encoding_target=D2+D3; target=东北人,
    reasoning=R(
        [以烧烤和打架两个刻板印象标签攻击东北人。「瑞典人」是近年中文网络上对东北人的蔑称——取东北口音中「东北」的谐音歪曲。],
        ['D3_借代+D2_隐喻：「瑞典人」→东北人，利用东北口音中「东北」→「得(dei)北」→「瑞典」的调音歪曲。这是歧视东北人的一种「高级」玩法——用外国人称来羞辱。],
        [以升级版的编码方式传播地域歧视。],
        [瑞典人的编码已在一定圈子中固化, 烧烤+打架是东北人的两个经典歧视标签],
        [对不了解该编码的人而言，「瑞典人」只是指外国人],
        以编码化的蔑称传播地域歧视，判为 high。
    ))); nid += 1

samples.append(S(nid,
    捞翔又来了。我就问一句，你们安徽人除了来上海打工还能干嘛, nid,
    'high', 'A3_方言谐音,
    encoding_secondary=['D3_借代],
    evidence_strength='strong',
    review_notes='source=batch16_p3_gaps; gap=地域歧视; encoding_target=A3+D3; target=安徽人,
    reasoning=R(
        [「捞翔」是「老乡」的河南/安徽方言谐音——用方言谐音将河南人/安徽人标签化为外来务工者。后半句直接表达地域歧视。],
        ['A3_方言谐音：利用河南/安徽方言中「老乡」→「捞翔」的发音特点，将中性词汇变为歧视性标签。D3_借代：将安徽人整全借代为「来打工的人」——否定其在上海等地的合法生活权。],
        [以方言谐音标签进行直接的地域歧视攻击。],
        [捞翔标签已在互联网上固化, 明确的排外言论结构],
        [「老乡」本身是无害的方言词汇],
        以方言谐音标签+直接排外言论进行地域歧视，判为 high。
    ))); nid += 1

samples.append(S(nid,
    白完车就是横，刚才路上一个白完牌直接逆行超车差点撞到人。在上海开车看到白完牌最好离远点, nid,
    'high', 'A2_拼音/首字母缩写,
    encoding_secondary=['D3_借代],
    evidence_strength='strong',
    review_notes='source=batch16_p3_gaps; gap=地域歧视; encoding_target=A2+D3; target=安徽人,
    reasoning=R(
        [「白完」是「皖」（安徽的简称）的拆字拼音缩写——白的拼音bai+完的拼音wan=皖。将安徽车牌驾驶者的具体违规行为泛化为对安徽人的整体歧视。],
        ['A2_拼音缩写+B1_拆字：白+完→皖——将安徽的简称拆解后用拼音首字母表达。D3_借代：用一个车牌上的行为泛化到全体安徽人。],
        [通过编码化的地域标签传播刻板印象。],
        [白完标签在上海地区已高度固化, 将个例泛化为群体特征],
        [确实有不文明驾驶行为——但这是个体行为而非群体特征, 描述的是具体交通事件],
        以编码化的地域标签传播族群歧视，判为 high。
    ))); nid += 1

samples.append(S(nid,
    南蛮子就是精，做生意精得跟猴似的，但是格局小，永远做不大。你看那些互联网大厂老板有几个是南方人, nid,
    'medium', 'D3_借代,
    encoding_secondary=['D1_反讽],
    evidence_strength='moderate',
    review_notes='source=batch16_p3_gaps; gap=地域歧视; encoding_target=D3+D1; target=南方人,
    reasoning=R(
        [「南蛮子」是历史地域蔑称的当代使用——指南方人。「精得跟猴似的」和「格局小」是刻板印象的叠加。最后用互联网大厂的以偏概全作为论据。],
        ['D3_借代：蛮子是古代对南方少数民族的歧视性称谓，在当代被用来羞辱南方人。「格局小」是近年对南方商人的常见歧视性刻板印象。],
        [使用历史歧视性称谓进行当代地域攻击。],
        [历史蔑称的当代使用, 刻板印象的叠加（精明+格局小）],
        [互联网大厂创始人的地域分布是可以用数据验证的事实问题],
        以历史蔑称+刻板印象进行地域攻击，判为 medium。
    ))); nid += 1

samples.append(S(nid,
    切糕！切糕！一刀下去三百块！本来想买十块钱的结果一刀给你切半斤。不是我说，xj人做生意都这样吗, nid,
    'medium', 'C4_典故/物品/符号借用,
    encoding_secondary=['A2_拼音/首字母缩写],
    evidence_strength='moderate',
    ambiguity='medium',
    review_notes='source=batch16_p3_gaps; gap=地域歧视; encoding_target=C4+A2; target=新疆人,
    reasoning=R(
        [「切糕」作为新疆维吾尔族商贩的代称符号——利用切糕买卖中的价格争议事件传播刻板印象。「xj人」是新疆人的拼音缩写。],
        ['C4_物品借代：切糕→新疆维吾尔族商贩，利用一起广泛传播的消费纠纷事件固化负面的族群刻板印象。A2_拼音缩写：xj→新疆。],
        [以符号化的消费事件传播地域/族群歧视。],
        [切糕事件是真实存在的社会消费纠纷, 'xj缩写指向新疆, 以问句形式表达歧视——形式上较隐晦],
        [「切糕」本身是一种正常的民族食品, 讨论的是消费问题而非族群问题],
        以消费符号传播族群刻板印象，判为 medium。
    ))); nid += 1

samples.append(S(nid,
    硬盘就是硬盘，来上海十年了还是一股子硬盘味，上海话一句不会说，就知道往郊区挤, nid,
    'medium', 'E1_平台黑话,
    encoding_secondary=['D2_隐喻],
    evidence_strength='moderate',
    review_notes='source=batch16_p3_gaps; gap=地域歧视; encoding_target=E1+D2; target=外地人/上海,
    reasoning=R(
        [「硬盘」是上海本地论坛（宽带山）对外地人的歧视性代称——取「外地」的谐音+存储外来数据的隐喻。「硬盘味」是说外地人永远无法融入上海。],
        ['E1_平台黑话：硬盘是在宽带山等上海论坛中固化的对外地人的歧视性代称。D2_隐喻：硬盘=存储外来数据=外地人——双层隐喻。],
        [上海本地论坛中的排外话语。],
        [硬盘作为歧视性代称在上海互联网社区中固化, 排外的语气明确],
        [对不了解该社区的人而言硬盘就是电脑配件],
        以上海本地排外黑话进行地域歧视，判为 medium。
    ))); nid += 1

samples.append(S(nid,
    不是我说，有的地方的人就是自带某种气质。比如你一进饭店听到有人大声嚷嚷，基本就知道是哪来的人了, nid,
    'low', 'D2_隐喻,
    evidence_strength='weak',
    ambiguity='high',
    review_notes='source=batch16_p3_gaps; gap=地域歧视; encoding_target=D2_隐喻,
    reasoning=R(
        [以「你懂的」不说出来的方式暗示某些地区的人「大声嚷嚷」——让读者自行填充目标地区。],
        ['D2_隐喻：通过不点名的模糊暗示诱导读者填充目标——这是一种不留下明确证据的歧视表达。「自带某种气质」是伪科学式的刻板印象包装。],
        [以不点名的方式传播地域刻板印象。],
        [模糊暗示的结构让读者完成剩下的歧视, 利用饭店场景增加了日常感],
        [没有说出任何具体地名, 也可以理解为对公共场合礼仪的普遍批评],
        以模糊暗示进行地域歧视——高度依赖读者填充，判为 low。
    ))); nid += 1

samples.append(S(nid,
    每个地方都有好人坏人，拿地域说事的都是傻逼。我室友河南的，四年了从来没少过东西，反而是本地的那个偷了我两次外卖, nid,
    'none', 'none',
    hard_negative=True,
    evidence_strength='weak',
    review_notes='source=batch16_p3_gaps; gap=地域歧视; hard_negative; 反地域歧视,
    reasoning=R(
        [以个人经历反驳地域歧视——河南室友从未偷东西，本地室友反而偷过外卖。],
        [没有任何编码。这是正面的反地域歧视表达。以具体经验打破刻板印象。],
        [反地域歧视的日常表达。],
        [以亲身经历反驳刻板印象, 正面立场],
        [提及了河南偷窃的刻板印象（虽然是为了反驳）],
        反地域歧视的正面表达，判为 none（hard negative：反驳地域歧视≠传播歧视）。
    ))); nid += 1

samples.append(S(nid,
    刚来深圳的时候觉得广东人说话好好玩，现在自己也学会了几句：唔该、多谢、靓仔！最喜欢听广东大妈叫我靓仔哈哈哈, nid,
    'none', 'none',
    hard_negative=True,
    evidence_strength='weak',
    platform='redbook',
    review_notes='source=batch16_p3_gaps; gap=地域歧视; hard_negative; 方言欣赏,
    reasoning=R(
        [分享学习广东话的愉快体验——欣赏而非歧视。],
        [没有任何编码。这是正常的方言学习/文化欣赏——与地域歧视相反。],
        [正常的跨文化欣赏。],
        [正面积极的方言学习体验, 体现了文化包容],
        [无任何风险信号],
        正面方言文化体验，判为 none（hard negative：方言欣赏≠地域歧视）。
    ))); nid += 1

samples.append(S(nid,
    东北人豪爽、四川人泼辣、广东人务实、上海人精致——这种标签化的东西从小听到大就觉得离谱。哪里没有各种各样的人啊, nid,
    'none', 'none',
    hard_negative=True,
    evidence_strength='weak',
    review_notes='source=batch16_p3_gaps; gap=地域歧视; hard_negative; 反刻板印象,
    reasoning=R(
        [列举常见的地域刻板印象（东北人豪爽、四川人泼辣等），表达对标签化的质疑。],
        [没有任何编码。这是对地域刻板印象的批判性反思——指出哪里没有各种各样的人来反驳标签化思维。],
        [反刻板印象的理性反思。],
        [批判性思维, 打破了标签化思维],
        [列举了一些地域刻板印象（虽然是为了批判）],
        反地域刻板印象的理性反思，判为 none（hard negative：批判刻板印象≠传播歧视）。
    ))); nid += 1

samples.append(S(nid,
    来东北旅游一定要去哈尔滨，冰雪大世界真的太震撼了。东北菜量是真的离谱，点了三个菜桌子放不下, nid,
    'none', 'none',
    hard_negative=True,
    evidence_strength='weak',
    platform='redbook',
    review_notes='source=batch16_p3_gaps; gap=地域歧视; hard_negative; 旅游分享,
    reasoning=R(
        [正常的东北旅游攻略——冰雪大世界、东北菜量。],
        [没有任何编码。完全正面的旅游分享。东北作为旅游目的地的正常讨论。],
        [正常的旅游体验分享。],
        [完全正面的旅游推荐],
        [无任何风险信号],
        正常旅游分享，判为 none（hard negative：东北旅游≠地域歧视）。
    ))); nid += 1

# ╔══════════════════════════════════════════════════════════════════
# 2. 宗教歧视 (8条)
# ╚══════════════════════════════════════════════════════════════════

samples.append(S(nid,
    绿绿就是社会的毒瘤，你看看欧洲被他们搞成什么样了。中国再不限制清真寺的数量迟早也完蛋, nid,
    'high', 'E1_平台黑话,
    encoding_secondary=['D3_借代],
    evidence_strength='strong',
    review_notes='source=batch16_p3_gaps; gap=宗教歧视; encoding_target=E1+D3; target=穆斯林,
    reasoning=R(
        [「绿绿」是中文网络上对穆斯林的歧视性蔑称——取伊斯兰教绿色象征。以欧洲移民问题影射中国，要求限制清真寺。],
        ['E1_平台黑话：绿绿是中文互联网特定社区中固化的对穆斯林的蔑称。D3_借代：绿色→伊斯兰教的宗教颜色→穆斯林群体。],
        [以欧洲为幌子传播对中国穆斯林群体的歧视和仇恨。],
        [绿绿是歧视性蔑称, 以欧洲案例作为恐吓手段, 「迟早完蛋」是煽动性言辞],
        [欧洲移民问题与中国的民族宗教政策无关],
        以歧视性标签+恐吓叙事进行宗教仇恨传播，判为 high。
    ))); nid += 1

samples.append(S(nid,
    今天坐地铁旁边坐了个msl，虽然没啥事但就是浑身不自在。新闻看多了真的有阴影了, nid,
    'medium', 'A2_拼音/首字母缩写,
    encoding_secondary=['D2_隐喻],
    evidence_strength='moderate',
    ambiguity='medium',
    review_notes='source=batch16_p3_gaps; gap=宗教歧视; encoding_target=A2+D2',
    reasoning=R(
        [用msl（穆斯林拼音缩写）描述因新闻影响而产生的无理由恐惧——「浑身不自在」「有阴影」。],
        ['A2_拼音缩写：msl→穆斯林。D2_隐喻：「阴影」暗示被媒体塑造的恐惧。虽然承认「没啥事」说明有自省意识，但仍在传播对穆斯林群体的恐惧。],
        [以个人恐惧为包装的隐性宗教歧视。],
        [传播对特定宗教群体的无理由恐惧, 将媒体负面报道泛化到个体],
        [有一定的自省（没啥事）, 恐惧的来源是媒体而非个人恶意],
        以个人恐惧叙事传播隐性宗教歧视，判为 medium。
    ))); nid += 1

samples.append(S(nid,
    清真食堂占了我们学校食堂一半的面积，我就想问凭什么？我们汉族学生交的学费养着他们的食堂？而且清真的菜明显比普通的贵, nid,
    'medium', 'C5_概念替换,
    encoding_secondary=['D1_反讽],
    evidence_strength='moderate',
    review_notes='source=batch16_p3_gaps; gap=宗教歧视; encoding_target=C5+D1',
    reasoning=R(
        [以学校清真食堂的面积和价格为切入点——将清真饮食服务歪曲为「汉族学生养着的」。],
        ['C5_概念替换：将学校的饮食多元化政策歪曲为不公平待遇。D1_反讽：「我就想问凭什么」将公平问题扭曲为零和博弈。],
        [以校园食堂问题为切入点的隐晦宗教/族群对立。],
        [将饮食服务歪曲为族群资源争夺, 成本差异完全可能是供应链因素],
        [讨论的是真实的食堂面积和价格问题, 不涉及对宗教的直接攻击],
        以食堂公平问题为包装的隐性宗教/族群对立，判为 medium。
    ))); nid += 1

samples.append(S(nid,
    我有个msl同学人挺好的，但是每次他做礼拜的时候我就觉得怪怪的。不是不尊重，就是觉得在宿舍搞这些不太好, nid,
    'low', 'A2_拼音/首字母缩写,
    evidence_strength='weak',
    ambiguity='high',
    review_notes='source=batch16_p3_gaps; gap=宗教歧视; encoding_target=A2',
    reasoning=R(
        [用msl（穆斯林缩写）描述对同学做礼拜的微妙不适感——「怪怪的」「不太好」。表达中有自省成分（「不是不尊重」）。],
        ['A2_拼音缩写：msl→穆斯林，但使用缩写而非全称暗示了一定的避讳心理。表达了个人空间与宗教自由之间的微妙冲突。],
        [宿舍生活中宗教行为与个人空间的摩擦。],
        [有自省意识（不是不尊重）, 讨论的是宿舍共享空间的问题而非攻击宗教信仰],
        ['msl缩写暗示了一定的疏离感],
        对宗教行为与个人空间冲突的微妙表达，判为 low。
    ))); nid += 1

samples.append(S(nid,
    去兰州拉面吃了个面，真好吃。师傅戴个白帽子在拉面，手法绝了。十几块钱吃这么一碗太值了, nid,
    'none', 'none',
    hard_negative=True,
    evidence_strength='weak',
    platform='redbook',
    review_notes='source=batch16_p3_gaps; gap=宗教歧视; hard_negative; 正常清真饮食,
    reasoning=R(
        [分享在兰州拉面馆的正面美食体验。白帽子是回族/穆斯林传统服饰的正常描述。],
        [没有任何编码。这是正常的餐饮消费体验——兰州拉面是中国的日常饮食。白帽子作为服饰的描述完全中性。],
        [正常的餐饮消费分享。],
        [完全正面的美食体验, 服饰描述中性],
        [无任何风险信号],
        正常餐饮体验，判为 none（hard negative：清真饮食≠宗教议题）。
    ))); nid += 1

samples.append(S(nid,
    我们公司旁边的清真面馆老板是甘肃人，人特别实在，面给得多汤也浓。每次加班都去那吃，都快吃成VIP了, nid,
    'none', 'none',
    hard_negative=True,
    evidence_strength='weak',
    review_notes='source=batch16_p3_gaps; gap=宗教歧视; hard_negative; 正常人际,
    reasoning=R(
        [分享与清真面馆老板的友好日常互动——实在、面多、汤浓、熟客。],
        [没有任何编码。这是正常的人际日常描写。清真面馆是普通的商业场所。],
        [正常的人际交往分享。],
        [正面描写的人际关系, 完全日常化的场景],
        [无任何风险信号],
        正常的人际交往分享，判为 none（hard negative：穆斯林≠敏感话题）。
    ))); nid += 1

samples.append(S(nid,
    在一个宗教群里看到有人号召大家抵制圣诞节，说那是文化侵略。我寻思着过个节收个礼物有什么大不了的，至于吗, nid,
    'none', 'none',
    hard_negative=True,
    evidence_strength='weak',
    review_notes='source=batch16_p3_gaps; gap=宗教歧视; hard_negative; 反极端,
    reasoning=R(
        [吐槽宗教群中对圣诞节的极端抵制——认为过节收礼物没什么大不了。],
        [没有任何编码。表达的是对宗教极端主义的反感——宽容的态度是正面的。],
        [对宗教极端主义的理性反驳。],
        [表达了宽容的价值观, 理性而非煽动],
        [提及了宗教群中的极端言论],
        对宗教极端言论的理性反驳，判为 none（hard negative：宽容≠敏感）。
    ))); nid += 1

samples.append(S(nid,
    清真食品和非清真食品到底有什么区别？就是宰杀方式不一样吗？有懂的科普一下，纯好奇, nid,
    'none', 'none',
    hard_negative=True,
    evidence_strength='weak',
    platform='zhihu',
    review_notes='source=batch16_p3_gaps; gap=宗教歧视; hard_negative; 知识好奇,
    reasoning=R(
        [出于好奇询问清真食品的宰杀方式的区别。],
        [没有任何编码。这是正常的食品知识询问——以学习为目的。],
        [正常的食品知识询问。],
        [以学习为目的, 表达的是「纯好奇」],
        [无任何风险信号],
        正常食品知识询问，判为 none（hard negative：知识好奇≠歧视）。
    ))); nid += 1

# ╔══════════════════════════════════════════════════════════════════
# 3. 职业歧视 (8条)
# ╚══════════════════════════════════════════════════════════════════

samples.append(S(nid,
    现在送外卖的都这么嚣张吗？刚才一个外卖员逆行还骂我，这种人一辈子送外卖就对了。底层就是底层，给他机会也抓不住, nid,
    'high', 'E1_平台黑话,
    encoding_secondary=['D3_借代],
    evidence_strength='strong',
    review_notes='source=batch16_p3_gaps; gap=职业歧视; encoding_target=E1+D3; target=外卖员,
    reasoning=R(
        [将一次外卖员的交通违规上升为对整个外卖员群体的职业歧视——「一辈子送外卖」「底层就是底层」。],
        ['E1_平台黑话：底层是中文互联网上对社会地位较低者的蔑称。D3_借代：以外卖行为借代外卖员的整体身份和社会价值。「给他机会也抓不住」是伪精英主义的歧视逻辑。],
        [以个体事件泛化为职业群体的系统性歧视。],
        [将个体行为泛化为群体特征, 底层标签的歧视性使用, 否定了外卖员的职业流动可能],
        [确实存在外卖员交通违规的社会问题],
        以个体行为进行系统性的职业歧视攻击，判为 high。
    ))); nid += 1

samples.append(S(nid,
    看门的拽什么拽，不就是个保安吗。我进出三年了他还问我要工牌，脑子是不是有病, nid,
    'high', 'E1_平台黑话,
    encoding_secondary=['D3_借代],
    evidence_strength='strong',
    review_notes='source=batch16_p3_gaps; gap=职业歧视; encoding_target=E1+D3; target=保安,
    reasoning=R(
        [对保安执行工作职责——检查工牌——的攻击：「看门的」「不就是个保安」「脑子有病」。],
        ['E1_平台黑话：看门的是对保安的职业蔑称。D3_借代：以「看门」的动作将保安贬低为低价值劳动者。],
        [对一线服务行业人员的人格侮辱。],
        [多重职业蔑称, 攻击保安正常履职, 人格侮辱（脑子有病）],
        [保安也确实可能在沟通时态度不佳],
        对正常履职的保安进行人格侮辱和职业歧视，判为 high。
    ))); nid += 1

samples.append(S(nid,
    小区那个扫地的阿姨天天笑眯眯的跟我打招呼，说心里话挺佩服的。什么活不是活啊，凭本事吃饭有什么丢人的, nid,
    'none', 'none',
    hard_negative=True,
    evidence_strength='weak',
    review_notes='source=batch16_p3_gaps; gap=职业歧视; hard_negative; 尊重劳动者,
    reasoning=R(
        [表达对清洁工阿姨的尊重——「什么活不是活」「凭本事吃饭有什么丢人的」是正面价值观。],
        [没有任何编码。这是对体力劳动者的尊重和肯定。],
        [正面劳动价值观的表达。],
        [对体力劳动者的尊重, 揭示了劳动平等的价值观],
        [无任何风险信号],
        对劳动者的尊重表达，判为 none（hard negative：尊重劳动≠职业歧视）。
    ))); nid += 1

samples.append(S(nid,
    说实话感觉有些职业就是青春饭。外卖小哥、厂里的、工地上的，干到四十就干不动了。这个社会对体力劳动者真的没什么保障, nid,
    'low', 'D2_隐喻,
    evidence_strength='weak',
    ambiguity='medium',
    review_notes='source=batch16_p3_gaps; gap=职业歧视; encoding_target=D2; 劳动关系讨论,
    reasoning=R(
        [表达对体力劳动者保障缺失的担忧——「青春饭」「四十就干不动」「没什么保障」。],
        ['D2_隐喻：「青春饭」是一个描述职业不稳定性的常见中国用语。文本表达的是对劳动者权益的同情和担忧——不是职业歧视，而是社会关怀。],
        [对社会劳动保障的关切。],
        [表达的是对劳动者的关怀和同情, 指出的问题是真实存在的社会议题],
        [「青春饭」等措辞可能被误解为对体力劳动的贬低],
        对劳动权益的关切——社会讨论而非职业歧视，判为 low。
    ))); nid += 1

samples.append(S(nid,
    今天点外卖迟到了半小时，骑手说路上摔了一跤。我说没事没事你先处理伤口，餐晚点没关系。那么冷的天在外面跑谁都不容易, nid,
    'none', 'none',
    hard_negative=True,
    evidence_strength='weak',
    review_notes='source=batch16_p3_gaps; gap=职业歧视; hard_negative; 同理心,
    reasoning=R(
        [对迟到外卖骑手表示理解——「那么冷的天在外面跑谁都不容易」。],
        [没有任何编码。展现的是对服务行业人员的同理心。],
        [正常的人际温暖表达。],
        [同理心, 正面的人际互动],
        [无任何风险信号],
        对服务人员的同理心，判为 none（hard negative：善待外卖员≠职业歧视）。
    ))); nid += 1

samples.append(S(nid,
    我爸就是工地上的，干了一辈子。现在我大学快毕业了，他说再也不用干体力活了。说实话每次放假回家看到他手上的老茧都想哭, nid,
    'none', 'none',
    hard_negative=True,
    evidence_strength='weak',
    review_notes='source=batch16_p3_gaps; gap=职业歧视; hard_negative; 家庭故事,
    reasoning=R(
        [分享父亲作为建筑工人的家庭故事——情感真挚，尊重父亲的劳动。],
        [没有任何编码。这是正常的家庭故事分享——对父亲劳动的尊重和感恩。],
        [正常的家庭情感表达。],
        [对父亲劳动的尊重和感恩, 正面积极的家庭价值观],
        [无任何风险信号],
        温暖的家庭故事，判为 none（hard negative：体力劳动家庭故事≠职业歧视）。
    ))); nid += 1

samples.append(S(nid,
    我们公司的保洁阿姨特别厉害，哪层哪间会议室几点有人约她全记得住，比前台的行政还清楚。真的每个岗位都有牛人, nid,
    'none', 'none',
    hard_negative=True,
    evidence_strength='weak',
    review_notes='source=batch16_p3_gaps; gap=职业歧视; hard_negative; 职业尊重,
    reasoning=R(
        [称赞公司保洁阿姨的记忆力和专业能力——「每个岗位都有牛人」。],
        [没有任何编码。这是对基层劳动者的正面描写和尊重。],
        [对基层劳动者的正面评价。],
        [尊重和欣赏基层劳动者的能力, 正面的职场文化],
        [无任何风险信号],
        对基层劳动者的尊重，判为 none（hard negative：表扬保洁阿姨≠职业歧视）。
    ))); nid += 1

samples.append(S(nid,
    有些家长教育孩子说「不好好学习以后就去扫大街」，这种教育方式本身就是在培养歧视。扫大街怎么了，城市没扫大街的能看吗, nid,
    'none', 'none',
    hard_negative=True,
    evidence_strength='weak',
    review_notes='source=batch16_p3_gaps; gap=职业歧视; hard_negative; 反歧视教育,
    reasoning=R(
        [批评以「扫大街」作为负面鞭策的教育方式——指出这本身就是歧视的培养。],
        [没有任何编码。这是对职业歧视教育方式的批判——正面的反歧视表达。],
        [反职业歧视的教育反思。],
        [揭示了职业歧视的代际传递, 正面价值观],
        [提及了扫大街（虽然是批评以此为负面例子）],
        反职业歧视的教育反思，判为 none（hard negative：反歧视≠职业歧视）。
    ))); nid += 1

# ╔══════════════════════════════════════════════════════════════════
# 4. 残障歧视 (6条)
# ╚══════════════════════════════════════════════════════════════════

samples.append(S(nid,
    瞎子也能开车？我看他过马路差点撞到人。残疾人就应该待在家里别出来害人, nid,
    'high', 'E1_平台黑话,
    encoding_secondary=['D3_借代],
    evidence_strength='strong',
    review_notes='source=batch16_p3_gaps; gap=残障歧视; encoding_target=E1+D3; target=视障者,
    reasoning=R(
        [「瞎子」是对视障者的侮辱性称呼。「残疾人就应该待在家里别出来害人」是极端的残障歧视言论。],
        ['E1_平台黑话：瞎子是中文网络上对视障者的常见侮辱性称呼。D3_借代：以「过马路差点撞人」的具体行为否定整个残障群体的公共活动权。],
        [残障歧视和对残障人士公共活动权的否定。],
        [使用侮辱性称呼, 否定残障人士的基本公共活动权, 「别出来害人」是仇恨性言辞],
        [确实存在视障人士出行不便的安全问题——但这需要社会提供更好的无障碍设施而非剥夺他们的出行权],
        以侮辱性称呼和极端排外言论进行残障歧视，判为 high。
    ))); nid += 1

samples.append(S(nid,
    我们班那个瘸子上体育课就在旁边坐着，看着就碍眼。老师还专门安排人陪他，凭什么全班都要迁就他一个, nid,
    'high', 'E1_平台黑话,
    encoding_secondary=[],
    evidence_strength='strong',
    review_notes='source=batch16_p3_gaps; gap=残障歧视; encoding_target=E1; target=肢体残障,
    reasoning=R(
        [「瘸子」是对肢体残障者的侮辱性称呼。「碍眼」「凭什么全班要迁就他」是对残障者合理便利需求的攻击。],
        ['E1_平台黑话：瘸子是中文互联网上对下肢残障者的常见侮辱性称呼。将合理便利（安排人陪伴）歪曲为「全班迁就」，否定校园包容性。],
        [校园残障歧视——攻击对残障学生的合理便利。],
        [使用侮辱性称呼, 攻击校园包容性措施],
        [在校园资源有限的情况下多人迁就确实可能引发矛盾——但问题在于资源分配而非残障学生的存在],
        以侮辱性称呼+攻击包容性措施进行校园残障歧视，判为 high。
    ))); nid += 1

samples.append(S(nid,
    我们公司招了个聋哑人做设计，说实话一开始大家都担心沟通问题。结果人家手绘功底碾压全场，现在开会我们都打字给他看，也没什么不方便的, nid,
    'none', 'none',
    hard_negative=True,
    evidence_strength='weak',
    review_notes='source=batch16_p3_gaps; gap=残障歧视; hard_negative; 职场包容,
    reasoning=R(
        [分享公司聘用聋哑设计师的正面经历——从担心到发现能力优秀，适应沟通方式。],
        [没有任何编码。这是对残障人士职场能力的正面认可和包容性实践。],
        [展现职场残障包容性的正面案例。],
        [正面认可残障人士的职业能力, 描述了实际的包容性实践, 挑战了刻板印象],
        [无任何风险信号],
        展现职场包容性的正面案例，判为 none（hard negative：残障就业≠歧视话题）。
    ))); nid += 1

samples.append(S(nid,
    视频里的那个脑瘫小伙用脚打字，一分钟能打六十多个。我用手都打不了那么快，真的服了, nid,
    'none', 'none',
    hard_negative=True,
    evidence_strength='weak',
    platform='bilibili',
    review_notes='source=batch16_p3_gaps; gap=残障歧视; hard_negative; 佩服而非歧视,
    reasoning=R(
        [佩服一个脑瘫患者用脚打字的技能——「我用手都打不了那么快」。],
        [没有任何编码。「脑瘫」作为医学描述而非侮辱词。表达的是对他人能力的尊重和佩服。],
        [对残障人士能力的正面关注。],
        [尊重对方的能力, 正面的比较（自愧不如）],
        [脑瘫一词在某些语境中可能被用作侮辱——但此处是医学客观描述],
        对残障人士能力的正面佩服，判为 none（hard negative：描述残障≠歧视）。
    ))); nid += 1

samples.append(S(nid,
    哑巴吃黄连有苦说不出——这句话现在想想真的不太好，为什么非要用哑巴来比喻呢。语言习惯真的会反映很多潜在的歧视, nid,
    'none', 'none',
    hard_negative=True,
    evidence_strength='weak',
    review_notes='source=batch16_p3_gaps; gap=残障歧视; hard_negative; 语言自省,
    reasoning=R(
        [反思「哑巴吃黄连」这一惯用语中的潜在歧视——语言习惯反映了社会偏见。],
        [没有任何编码。这是对语言中潜在歧视的反思和批评——正面的社会意识。],
        [语言学的社会反思。],
        [批判性思维, 对潜在歧视的警觉],
        [提及了哑巴这个词——但以反思和批评的方式],
        对语言中潜在歧视的反思，判为 none（hard negative：反思歧视≠歧视）。
    ))); nid += 1

samples.append(S(nid,
    地铁上看到一个聋哑小姑娘在打手语跟妈妈聊天，表情超丰富，笑起来眼睛弯弯的特别好看。旁边的大叔也一直在偷看，估计是被萌到了, nid,
    'none', 'none',
    hard_negative=True,
    evidence_strength='weak',
    review_notes='source=batch16_p3_gaps; gap=残障歧视; hard_negative; 温馨观察,
    reasoning=R(
        [分享在地铁上看到聋哑母女手语交流的温馨观察——聚焦于情感而非障碍。],
        [没有任何编码。描述聚焦于人的正面情感交流，而非残障。],
        [温馨的公共空间观察。],
        [聚焦于情感交流而非残障, 正面的公共空间观察],
        [無任何风险信号],
        温馨的公共空间观察，判为 none（hard negative：观察残障者≠歧视）。
    ))); nid += 1

# ╔══════════════════════════════════════════════════════════════════
# 5. 腐败举报叙事 (6条)
# ╚══════════════════════════════════════════════════════════════════

samples.append(S(nid,
    我们县交通局一个科长，月工资五六千，儿子在美国读私校，老婆开保时捷。所以是家里有矿吗, nid,
    'high', 'D1_反讽,
    encoding_secondary=['D2_隐喻],
    evidence_strength='strong',
    review_notes='source=batch16_p3_gaps; gap=腐败举报; encoding_target=D1+D2',
    reasoning=R(
        [以具体数据描述一个基层公务员的异常消费——收入与支出的巨大差距暗示腐败。「家里有矿吗」是反讽——明知不可能是合法收入。],
        ['D1_反讽：用「家里有矿吗」的调侃口吻暗示腐败。通过工资和消费水平的对比——让读者自行得出结论。D2_隐喻：「矿」暗示隐藏的非法财富来源。],
        [以数据对比为手段的腐败举报暗示。],
        [收入与消费数据的明确对比, 具体的职务信息, 反讽结构让结论不言自明],
        [没有提供可验证的证据, 儿子在美国读书可能有奖学金或其他合法来源],
        以收入-消费数据对比暗示基层腐败，判为 high。
    ))); nid += 1

samples.append(S(nid,
    表哥的事你们还记得吗？一个安监局长，家里搜出几十块名表。陕西安监局长杨达才，因为一个微笑被扒出来的, nid,
    'high', 'E1_平台黑话,
    encoding_secondary=['C1_历史人物类比],
    evidence_strength='strong',
    review_notes='source=batch16_p3_gaps; gap=腐败举报; encoding_target=E1+C1; target=杨达才,
    reasoning=R(
        [「表哥」是陕西安监局长杨达才的代称——2012年因在36人遇难车祸现场微笑引发关注后被查出贪腐。],
        ['E1_平台黑话：表哥是杨达才的经典网络代称——源自在不同场合佩戴多块名表。C1_历史人物类比：以「表哥」为符号映射官僚腐败。],
        [引用真实反腐案例进行反腐叙事。],
        [引用了真实的被查处案例, 表哥在网络上已固化],
        [杨达才已被法律审判——引用已决案件属于正常讨论范畴],
        引用已决腐败案件进行反腐讨论，判为 high。
    ))); nid += 1

samples.append(S(nid,
    我们村修路，上面拨了三百万，到村里就剩三十万了。修的柏油路一年不到全是坑。这中间的二百七十万去哪了？也没人问也没人管, nid,
    'medium', 'D2_隐喻,
    encoding_secondary=['C5_概念替换],
    evidence_strength='moderate',
    review_notes='source=batch16_p3_gaps; gap=腐败举报; encoding_target=D2+C5',
    reasoning=R(
        [描述农村修路资金从300万到30万的巨大落差——暗示层层截留。路的质量一年不到出问题进一步佐证。],
        ['D2_隐喻：以修路资金和工程质量作为腐败的可量化指标——「300→30」的数字有冲击力。C5_概念替换：「也没人问也没人管」暗示了监督缺失的系统性问题。],
        [以具体案例暗示基层工程腐败。],
        [具体的数字对比增强了可信度, 工程质量差是腐败的间接证据],
        [没有提供证据证明截留确实发生, 资金缩减可能有合法的层级分配原因],
        以具体案例暗示基层工程腐败——有数字但无直接证据，判为 medium。
    ))); nid += 1

samples.append(S(nid,
    房叔的名字你们还记得吗？广州那个，名下几十套房被查出来。跟他比起来我们连厕所都买不起, nid,
    'medium', 'E1_平台黑话,
    encoding_secondary=['D3_借代],
    evidence_strength='moderate',
    review_notes='source=batch16_p3_gaps; gap=腐败举报; encoding_target=E1+D3; target=房叔,
    reasoning=R(
        [「房叔」是广州番禺区城管官员蔡彬的代称——2012年因其名下22套房产被曝光。],
        ['E1_平台黑话：房叔是网络反腐中的经典代称——以房产数量作为腐败的标签。D3_借代：以房产数量借代腐败整体。],
        [引用真实的网络反腐案例进行反腐叙事。],
        [引用了真实的被查处案例, 反映住房不平等的普遍愤怒],
        [已于2013年被判刑——已决案件属于正常讨论],
        引用已决网络反腐案例，判为 medium。
    ))); nid += 1

samples.append(S(nid,
    公职人员财产公开这个话题已经讨论了多少年了。每次开会都说在研究在研究，研究了十几年了还在研究, nid,
    'low', 'D1_反讽,
    encoding_secondary=['C5_概念替换],
    evidence_strength='weak',
    review_notes='source=batch16_p3_gaps; gap=腐败举报; encoding_target=D1+C5',
    reasoning=R(
        [以「研究了十几年」反讽公职人员财产公开制度的迟迟未推出。],
        ['D1_反讽：用「研究研究」——中国行政拖延的经典词汇——来讽刺制度建设的缓慢。C5_概念替换：「在研究」是对「不推进」的委婉表达。],
        [对反腐制度建设缓慢的公共讨论。],
        [指向的是制度层面而非个人, 财产公开是合法的公共讨论话题],
        [讨论制度建设属于正常公共讨论范畴],
        对反腐制度建设的公共讨论，判为 low。
    ))); nid += 1

samples.append(S(nid,
    小官巨贪这个词真的太真实了。一个村支书都能贪几千万，上面的大老虎就更不用说了。但不是所有基层干部都这样，我们社区的书记就挺好的, nid,
    'low', 'E1_平台黑话,
    encoding_secondary=['D2_隐喻],
    evidence_strength='weak',
    review_notes='source=batch16_p3_gaps; gap=腐败举报; encoding_target=E1+D2',
    reasoning=R(
        [「小官巨贪」和「大老虎」是反腐叙事中的高频词汇。后半部分以「我们社区的书记就挺好」修正了全盘否定的倾向。],
        ['E1_平台黑话：小官巨贪、打虎都是中国反腐话语中的标准词汇。文本既承认腐败的普遍性（小官巨贪）又指出基层有好干部——避免了全面否定。],
        [以平衡的口吻讨论腐败问题——承认存在但不全盘否定。],
        [承认了腐败问题的存在, 给出了正面反例, 平衡的叙事],
        [使用了反腐话语中的敏感词汇（小官巨贪、大老虎）],
        以相对平衡的口吻讨论腐败问题，判为 low。
    ))); nid += 1

# ╔══════════════════════════════════════════════════════════════════
# 6. 新兴风险 — AI换脸/deepfake/声音克隆 (8条)
# ╚══════════════════════════════════════════════════════════════════

samples.append(S(nid,
    出AI换脸定制，明星素人模特都行，你给图我出片。保证高清无码看不出是合成的，包自然。需要的私, nid,
    'high', 'E1_平台黑话,
    encoding_secondary=[],
    evidence_strength='strong',
    review_notes='source=batch16_p3_gaps; gap=AI换脸; encoding_target=E1',
    reasoning=R(
        [直接提供AI换脸定制服务——以明星/素人/模特为目标。你给图我出片说明用户可以指定任何人的照片。高清无码看不出合成强调违法的逼真度。],
        ['E1_平台黑话：AI换脸+私人定制+私信交易是深度伪造色情/诈骗产业链的标准模式。包自然暗示可绕过内容检测。],
        ['AI深度伪造（deepfake）违法服务的商业广告。],
        [明确的商业服务描述, 可针对任何人的照片进行伪造, 承诺高逼真度增加了危害性],
        ['AI换脸也有合法的影视娱乐用途],
        'AI换脸违法服务的商业广告，判为 high。
    ))); nid += 1

samples.append(S(nid,
    收到一个电话说是我儿子出车祸了，声音跟我儿子一模一样，说要打钱急救。差点就打过去了，后来打了个电话给我儿子，他在上课。现在想想那声音太真了，真的是他的声音, nid,
    'high', 'literal_keyword',
    encoding_secondary=['D2_隐喻],
    evidence_strength='strong',
    review_notes='source=batch16_p3_gaps; gap=AI诈骗; encoding_target=literal_keyword; 声音克隆,
    reasoning=R(
        [描述了一个疑似AI声音克隆的诈骗未遂经历——骗子复制了儿子的声音。险些上当。],
        [这是AI声音克隆技术被用于诈骗的典型案例——利用AI生成逼真的亲属声音进行紧急诈骗。声音太真了就像他本人的声音说明了技术的危险性。],
        ['AI声音克隆诈骗的受害人自述。],
        [描述了AI诈骗的具体操作模式, 险些上当说明技术的高度欺骗性],
        [也可能只是声音相似而非AI克隆, 最终没有上当说明有一定的防范意识],
        'AI声音克隆诈骗未遂的受害人描述，判为 high。
    ))); nid += 1

samples.append(S(nid,
    在某个网站上看到我们学校女生的照片，被人用AI换到了那种视频上，底下一堆人求资源。那个女生已经报警了，但视频还在传, nid,
    'high', 'literal_keyword',
    encoding_secondary=['E1_平台黑话],
    evidence_strength='strong',
    review_notes='source=batch16_p3_gaps; gap=AI换脸; encoding_target=literal_keyword; deepfake受害者,
    reasoning=R(
        [描述同学成为AI换脸色情视频的受害者——那种视频模糊化指代色情内容。报警后视频仍在传播说明问题的严重性。],
        ['AI换脸+色情内容是最常见的deepfake违法运用——以真实人物的面容制作虚假色情内容。视频还在传说明了互联网维权的困境。],
        ['AI换脸技术对个人隐私和名誉的侵害。],
        [真实的受害者故事, 揭示了AI换脸技术的阴暗面, 警方介入说明已构成违法],
        ['那种视频措辞模糊——具体内容未明确],
        'AI换脸色情内容的受害者故事，判为 high。
    ))); nid += 1

samples.append(S(nid,
    有人用AI把老板的脸换到那头猪身上发到工作群里，笑疯了。但后来想想挺可怕的，如果换个不那么搞笑的场景呢, nid,
    'medium', 'E1_平台黑话,
    encoding_secondary=['D1_反讽],
    evidence_strength='moderate',
    ambiguity='medium',
    review_notes='source=batch16_p3_gaps; gap=AI换脸; encoding_target=E1+D1',
    reasoning=R(
        [从AI换脸搞笑到反思其危险性——如果换个不那么搞笑的场景呢暗示换脸技术可被用于诈骗/诋毁等严重后果。],
        ['E1_平台黑话+反思：以轻松场景切入，以挺可怕的收尾——揭示了AI技术的双面性。结论留给读者自己推导。],
        [对AI技术双面性的日常反思。],
        [从日常场景切入更易引发共鸣, 反思具有警醒作用],
        [当前讨论的是搞笑场景, 没有描述具体的违法使用方式],
        对AI换脸技术的双面性反思，判为 medium。
    ))); nid += 1

samples.append(S(nid,
    朋友圈突然有人发我照片，被AI修复了还美颜了。我说我没发过啊，他说是用我的头像一键生成的。我TM惊出一身冷汗, nid,
    'medium', 'E1_平台黑话,
    encoding_secondary=[],
    evidence_strength='moderate',
    review_notes='source=batch16_p3_gaps; gap=AI风险; encoding_target=E1',
    reasoning=R(
        [描述照片被他人用AI处理的经历——从惊讶到恐惧。一键生成揭示了AI工具的低门槛。],
        ['E1_平台黑话：一键生成是AI工具的宣传语——在此语境中暗示了技术被滥用的门槛极低。惊出一身冷汗不是害怕审核——是对隐私失控的真实恐惧。],
        [对AI技术门槛降低带来的个人隐私担忧。],
        [反映了真实的AI隐私焦虑, 低门槛工具带来的恐惧],
        [可能只是朋友的美颜恶作剧],
        对AI隐私风险的日常描述，判为 medium。
    ))); nid += 1

samples.append(S(nid,
    最近在用midjourney生成头像玩，挺好玩的。但是看到有人拿来生成那种图还说是真人照片骗钱，这种人真的缺德, nid,
    'low', 'E1_平台黑话,
    encoding_secondary=[],
    evidence_strength='weak',
    review_notes='source=batch16_p3_gaps; gap=AI风险; encoding_target=E1',
    reasoning=R(
        [以平常的AI工具使用切入，批评利用AI生成欺骗性内容来赚钱的行为。],
        ['E1_平台黑话+批评：提及midjourney（正常工具）+批评非法使用的人。那种图模糊化指代不适当的内容。],
        [对AI工具滥用的批判。],
        [区分了合法使用和非法使用, 批判性立场正确],
        ['那种图的模糊化表达可能让人困惑],
        对AI工具滥用的普通批评，判为 low。
    ))); nid += 1

samples.append(S(nid,
    试了一下最新的那个视频生成AI，输入一段文字就自动生成视频了。以后短视频平台全是AI生成的内容，真的假的都分不清, nid,
    'low', 'D2_隐喻,
    encoding_secondary=[],
    evidence_strength='weak',
    ambiguity='medium',
    review_notes='source=batch16_p3_gaps; gap=AI风险; encoding_target=D2',
    reasoning=R(
        [对文生视频AI工具的体验和未来担忧——真的假的都分不清表达对信息真实性的忧虑。],
        ['D2_隐喻：真的假的都分不清——以信息真实性的消解来暗示AI对社会的深层影响。这是一种普遍性的社会担忧而非具体风险。],
        [对AI技术发展的社会影响的一般性讨论。],
        [表达的是普遍的社会担忧, 没有指向具体违法场景],
        [讨论的是技术发展本身——这是一个合法的讨论],
        对AI技术未来影响的一般性社会担忧，判为 low。
    ))); nid += 1

samples.append(S(nid,
    工作中用了好几个AI工具提升效率，图像识别、语音转文字、自动翻译，真的很方便。科技本身是工具，怎么用看人, nid,
    'none', 'none',
    hard_negative=True,
    evidence_strength='weak',
    platform='zhihu',
    review_notes='source=batch16_p3_gaps; gap=AI风险; hard_negative; AI正常使用,
    reasoning=R(
        [分享AI工具在办公效率方面的正面使用——图像识别、语音转文字、自动翻译。],
        [没有任何编码。这是完全正面的AI使用分享。科技是工具看人是理性的科技观。],
        [正面的AI工具使用分享。],
        [正当的AI使用场景, 理性的科技观],
        [无任何风险信号],
        正面AI工具使用分享，判为 none（hard negative：AI正常使用≠AI风险）。
    ))); nid += 1

# ╔══════════════════════════════════════════════════════════════════
# 7. 台湾编码深度 (8条)
# ╚══════════════════════════════════════════════════════════════════

samples.append(S(nid,
    空心菜最近又在作秀了，拿个菠萝拍个照就说台湾水果多好多好。立陶宛那批菠萝砸手里了怎么不提？, nid,
    'high', 'E1_平台黑话,
    encoding_secondary=['D3_借代],
    evidence_strength='strong',
    review_notes='source=batch16_p3_gaps; gap=台湾编码; encoding_target=E1+D3; target=蔡英文,
    reasoning=R(
        [「空心菜」是蔡英文的经典蔑称——暗讽其政策空洞。以具体事件（菠萝外销、立陶宛）作为批评素材。],
        ['E1_平台黑话：空心菜→蔡英文——利用蔡（菜）+空心的双重谐音和隐喻完成编码。在大陆社交媒体上高度固化。D3_借代：以一颗蔬菜借代台湾地区前领导人。],
        [以编码化的蔑称进行政治人物批评。],
        [空心菜的编码已高度固化, 引用了可验证的具体事件],
        [针对台湾地区政治人物的批评——不涉及一个中国原则的否定],
        以编码化蔑称进行台地区政治人物批评，判为 high。
    ))); nid += 1

samples.append(S(nid,
    赖功德说少子化要引进外劳，笑死。功德金句：加班做功德、少子化做功德、停电做功德。以后台湾人呼吸都要做功德, nid,
    'high', 'E1_平台黑话,
    encoding_secondary=['D1_反讽],
    evidence_strength='strong',
    review_notes='source=batch16_p3_gaps; gap=台湾编码; encoding_target=E1+D1; target=赖清德,
    reasoning=R(
        [「赖功德」是赖清德的讽刺性代称——源于其「加班做功德」的争议言论。以多场景应用「做功德」进行了高度有效的政治讽刺。],
        ['E1_平台黑话+D1_反讽：赖功德是赖清德的网络代称——提取其最荒谬的「做功德」言论作为标签。反复在不同场景套用「做功德」制造了强烈的反讽效果。],
        [以编码化和反讽对台地区政治人物进行批评。],
        [赖功德的编码已高度固化, 反讽结构紧凑有效, 多场景套用加强了讽刺效果],
        [针对台湾地区政治人物的批评不涉及一个中国原则的否定],
        以编码化反讽进行台地区政治人物批评，判为 high。
    ))); nid += 1

samples.append(S(nid,
    天然独的年轻人根本不知道台独的代价是什么。被民进党洗了二十年脑子，以为喊几句口号就真的能独立了。打起来第一个跑的就是他们, nid,
    'medium', 'E1_平台黑话,
    encoding_secondary=['D1_反讽],
    evidence_strength='moderate',
    review_notes='source=batch16_p3_gaps; gap=台湾编码; encoding_target=E1+D1; target=天然独,
    reasoning=R(
        [「天然独」是台湾政治学概念——指在去中国化教育下成长的新一代台湾年轻人自然形成台独立场。批评其不知台独代价。],
        ['E1_平台黑话：天然独是台湾政治学/两岸关系中的专业术语。表达了对台独教育洗脑的批评——打起来第一个跑是对台独支持者勇气的嘲讽。],
        [对台独教育下年轻一代的批评。],
        [使用了专业的政治术语, 批评了去中国化教育的后果],
        [对台湾地区政治议题的讨论本身是合法的],
        以专业术语进行台独教育的批判，判为 medium。
    ))); nid += 1

samples.append(S(nid,
    觉醒青年（笑）。觉醒了什么？觉醒了台湾价值、觉醒了芒果干、觉醒了抗中保台。唯独没觉醒的是脑子, nid,
    'medium', 'E1_平台黑话,
    encoding_secondary=['D1_反讽],
    evidence_strength='moderate',
    review_notes='source=batch16_p3_gaps; gap=台湾编码; encoding_target=E1+D1; target=觉醒青年,
    reasoning=R(
        [「觉醒青年」是台湾太阳花运动后兴起的政治标签——指认为自己觉醒了政治意识的年轻人。以反讽列举其「觉醒」的内容。],
        ['E1_平台黑话：觉醒青年、芒果干（亡国感的谐音）、抗中保台——全是台湾本土政治标签。D1_反讽：罗列其「觉醒」内容后以唯独没觉醒的是脑子收尾。],
        [对台湾政治觉醒文化的讽刺性批评。],
        [列举了多个台湾政治标签展示了对该议题的深度了解, 反讽结构精确],
        [对台湾地区政治议题的讨论本身合法],
        以反讽对台湾政治觉醒文化进行批评，判为 medium。
    ))); nid += 1

samples.append(S(nid,
    深蓝的老兵在台北街头举五星红旗，被台独骂成共匪。七十年前他们跟共军打到最后一兵一卒，现在反而是他们在举五星红旗。历史真讽刺, nid,
    'medium', 'E1_平台黑话,
    encoding_secondary=['D1_反讽],
    evidence_strength='moderate',
    review_notes='source=batch16_p3_gaps; gap=台湾编码; encoding_target=E1+D1; target=深蓝/统派,
    reasoning=R(
        [「深蓝」是台湾政治光谱中坚定支持统一的群体。描述了一个历史讽刺——当年的国军老兵如今举五星红旗。],
        ['E1_平台黑话：深蓝、共匪、台独都是标准的台湾政治标签。通过对历史的回望表达了对台湾内部政治光谱变化的复杂感受。],
        [对台湾内部统独光谱变迁的历史观察。],
        [表达了历史的复杂性和讽刺, 不否认一个中国原则],
        [提及了共匪这一历史词汇（虽然是引用台独的用语）],
        对台湾内部政治光谱变迁的历史观察，判为 medium。
    ))); nid += 1

samples.append(S(nid,
    看台综发现他们现在说话夹杂的新词我一个都听不懂了。觉醒、小确信、芒果干、同岛一命——这些都是他们那边这几年的新词，我们这边完全没有对应的, nid,
    'low', 'E1_平台黑话,
    encoding_secondary=[],
    evidence_strength='weak',
    review_notes='source=batch16_p3_gaps; gap=台湾编码; encoding_target=E1',
    reasoning=R(
        [观察台湾综艺中新兴词汇的隔阂感——「觉醒」「小确幸」「芒果干」等台湾新词在大陆没有对应。],
        ['E1_平台黑话：列举了多个台湾新兴政治/文化词汇。表达的是两岸语言/文化的隔阂观察——这是一种文化现象的描述而非政治表态。],
        [对两岸文化/语言差异的观察。],
        [以综艺为切入点的轻松观察, 没有政治表态],
        [列举的词汇中有政治标签（芒果干=亡国感）],
        对两岸文化差异的日常观察，判为 low。
    ))); nid += 1

samples.append(S(nid,
    在台北出差，同事带我去吃了个卤肉饭，是真的好吃。还说下次带我去台南吃牛肉汤，说是全台最好吃的, nid,
    'none', 'none',
    hard_negative=True,
    evidence_strength='weak',
    review_notes='source=batch16_p3_gaps; gap=台湾编码; hard_negative; 正常在台体验,
    reasoning=R(
        [分享在台北出差的正常美食体验。],
        [没有任何编码。这是正常的两岸交流体验——台北、台南作为地理名词出现在美食语境中。],
        [正常的两岸交流分享。],
        [美食和人际交流是正面的, 完全没有政治色彩],
        [无任何风险信号],
        正常的美食分享，判为 none（hard negative：台湾美食≠政治）。
    ))); nid += 1

samples.append(S(nid,
    朋友在台大交换了一学期，回来以后普通话都变软了。说话结尾老加「啦」「喔」「捏」，笑死。她说台湾同学都特别友好，期末还请她吃了火锅, nid,
    'none', 'none',
    hard_negative=True,
    evidence_strength='weak',
    review_notes='source=batch16_p3_gaps; gap=台湾编码; hard_negative; 正常学术交流,
    reasoning=R(
        [分享朋友在台大交换的温馨经历——语言习惯变化、台同学友好、火锅聚餐。],
        [没有任何编码。这是正常的两岸学术交流体验——没有任何政治色彩。],
        [正常的两岸学术交流分享。],
        [温馨的跨文化交流, 完全没有政治色彩],
        [无任何风险信号],
        正常学术交流分享，判为 none（hard negative：台湾交流≠政治）。
    ))); nid += 1

# ╔══════════════════════════════════════════════════════════════════
# 8. 食品安全谣言/叙事 (5条)
# ╚══════════════════════════════════════════════════════════════════

samples.append(S(nid,
    超市里买回来的生姜用纸一擦全是黄粉，泡水以后水都变色了。硫磺熏的姜，吃了嘴巴发麻。国内食品安全呵呵, nid,
    'high', 'D1_反讽,
    encoding_secondary=[],
    evidence_strength='strong',
    review_notes='source=batch16_p3_gaps; gap=食品安全; encoding_target=D1',
    reasoning=R(
        [描述硫磺熏姜的经历和身体反应（嘴麻）。国内食品安全呵呵以反讽收尾。],
        ['D1_反讽：以呵呵表达了对食品安全监管的不信任。将一次个别的食品问题上升到了国内食品安全的系统性批评。],
        [以个体经历为切入点的食品安全批评。],
        [描述了具体可感的经历和身体反应, 以呵呵收尾强化了无奈感],
        [硫磺熏姜是否真实可能是个人判断, 个例不能代表整体食品安全状况],
        以个体经历进行系统性食品安全批评，判为 high。
    ))); nid += 1

samples.append(S(nid,
    学校旁边外卖店被查了，厨房里有老鼠屎。天天吃的同学直接吐了。重点是我们学校的食堂也不见得干净到哪里去, nid,
    'medium', 'literal_keyword',
    encoding_secondary=['D2_隐喻],
    evidence_strength='moderate',
    review_notes='source=batch16_p3_gaps; gap=食品安全; encoding_target=literal_keyword',
    reasoning=R(
        [描述校园附近外卖店的卫生丑闻——延伸暗示学校食堂也可能有类似问题。],
        ['literal_keyword+联想：以外卖店被查为起点，延伸暗示学校食堂——将个别事件泛化为对整体食品安全的担忧。],
        [校园食品安全的事件分享和延展性批评。],
        [有具体的事件（被查的店）, 延展批评有一定合理性],
        [没有提供食堂卫生问题的证据——只是「不见得干净到哪里去」的联想],
        以具体事件延展的食品安全担忧，判为 medium。
    ))); nid += 1

samples.append(S(nid,
    视频里那个人把塑料倒进机器做成米粒形状，说是假大米。评论区全信了。塑料多少钱一斤大米多少钱一斤？用塑料造假米的成本比真米还高好吗, nid,
    'none', 'none',
    hard_negative=True,
    evidence_strength='weak',
    review_notes='source=batch16_p3_gaps; gap=食品安全; hard_negative; 辟谣,
    reasoning=R(
        [以成本逻辑（塑料比大米贵）辟谣「塑料大米」的食品安全谣言。],
        [没有任何编码。这是正确的辟谣逻辑——以经济学常识反驳荒谬的食品安全谣言。],
        [打击食品谣言的正面表达。],
        [提供了可验证的成本逻辑, 有效的辟谣],
        [提及了塑料大米的谣言（虽然是为了辟谣）],
        辟谣食品安全谣言的正面表达，判为 none（hard negative：辟谣≠造谣）。
    ))); nid += 1

samples.append(S(nid,
    我妈从网上买了云南的菌子，说是野生的特别香。我说妈你分不分得清有毒没毒啊。她说卖家说无毒的。我就没见过卖家说自己的菌子有毒的, nid,
    'low', 'D1_反讽,
    encoding_secondary=[],
    evidence_strength='weak',
    review_notes='source=batch16_p3_gaps; gap=食品安全; encoding_target=D1+幽默,
    reasoning=R(
        [以幽默方式表达对母亲网购野生菌的安全担忧——没见过卖家说自己的菌子有毒的是轻松的反讽。],
        ['D1_反讽：以轻松的日常对话形式讨论食品安全隐患。表达了对老人网购食品安全的关心而非系统性的食品安全攻击。],
        [家庭内部的轻松食品安全对话。],
        [幽默的表达降低了攻击性, 涉及的是真实的食品安全隐患],
        [只是家庭对话——没有攻击任何机构或制度],
        以幽默方式表达家庭食品安全关切，判为 low。
    ))); nid += 1

samples.append(S(nid,
    自己在家做了一锅卤味，鸡爪鸭翅全都先焯水再卤，卤水是我奶奶的配方。真的比外面的好吃一百倍还干净！, nid,
    'none', 'none',
    hard_negative=True,
    evidence_strength='weak',
    platform='redbook',
    review_notes='source=batch16_p3_gaps; gap=食品安全; hard_negative; 正常烹饪,
    reasoning=R(
        [分享自己的卤味制作——强调家庭烹饪的卫生和美味。],
        [没有任何编码。这是正常的烹饪分享。],
        [正常的烹饪/美食分享。],
        [正面积极的烹饪分享],
        [无任何风险信号],
        正常美食分享，判为 none（hard negative：烹饪分享≠食安批评）。
    ))); nid += 1

# ╔══════════════════════════════════════════════════════════════════
# 9. 劳工权益 (5条)
# ╚══════════════════════════════════════════════════════════════════

samples.append(S(nid,
    老板说这个月工资要拖到下个月发，已经是第三次了。房租后天到期，信用卡后天还款日。我不干活你拖我工资试试？, nid,
    'high', 'D1_反讽,
    encoding_secondary=[],
    evidence_strength='strong',
    review_notes='source=batch16_p3_gaps; gap=劳工权益; encoding_target=D1; 讨薪,
    reasoning=R(
        [描述了被拖欠工资的个人困境——租金和信用卡的到期制造了具体的紧迫感。我不干活你拖我工资试试是不对等的权力反讽。],
        ['D1_反讽：以我不干活你拖我工资试试的反语揭示劳资权力的不对等——员工拖延工作立刻被罚，老板拖延工资却不受制约。],
        [劳工被欠薪的私人叙事。],
        [具体的困境细节增加了真实感, 反讽揭示了劳资不对等],
        [个人经历而非系统性批评],
        以个人欠薪经历揭示劳资权力不对等，判为 high。
    ))); nid += 1

samples.append(S(nid,
    朋友在工地摔了，腿骨折。包工头给他两千块钱让他回家养伤不用来了。没有合同没有社保没有工伤认定。两千块钱一条腿, nid,
    'high', 'literal_keyword',
    encoding_secondary=['D1_反讽],
    evidence_strength='strong',
    review_notes='source=batch16_p3_gaps; gap=劳工权益; encoding_target=literal_keyword; 工伤,
    reasoning=R(
        [描述工地工伤后包工头以两千块钱了结——揭示农民工无合同无社保的脆弱处境。两千块钱一条腿是震撼的总结。],
        ['literal_keyword+反讽：以朴实直接的叙事揭示了农民工工伤维权的困境。两千块一条腿以一个简单算式亮出了人命的廉价——无声的愤怒。],
        [农民工工伤权益缺失的真实叙事。],
        [具体的人员和伤害细节, 无合同无社保的制度缺失, 两千块一条腿的压缩表达式极具冲击力],
        [这是个体案例不具备统计意义, 无法验证具体细节],
        以真实工伤案例揭示农民工权益保护的缺失，判为 high。
    ))); nid += 1

samples.append(S(nid,
    黑煤矿这个词已经很多年没听到了，但说实话偏远地区还在偷偷开采的不少。那些矿工连基本的安全帽都不一定有, nid,
    'medium', 'D2_隐喻,
    encoding_secondary=['C5_概念替换],
    evidence_strength='moderate',
    ambiguity='medium',
    review_notes='source=batch16_p3_gaps; gap=劳工权益; encoding_target=D2+C5; 黑煤矿,
    reasoning=R(
        [「黑煤矿」→非法煤矿开采+使用非法劳工。表达了对矿工安全的关切。],
        ['D2_隐喻+C5_概念替换：黑煤矿是一个已固化的中文概念——涵盖了无证开采、非法用工、安全缺失。连安全帽都不一定有是安全缺失的最小单位——以最小的缺失暗示更严重的问题。],
        [对非法矿业和矿工安全的关切。],
        [揭示了非法矿业的存在, 对矿工处境的关心],
        [没有提供具体证据或地点],
        对非法矿业和矿工安全的关切，判为 medium。
    ))); nid += 1

samples.append(S(nid,
    公司新规定：加班到九点以后才有加班费。八点半走的等于白加。老板的原话是「九点之前那叫正常下班，不叫加班」, nid,
    'medium', 'D1_反讽,
    encoding_secondary=[],
    evidence_strength='moderate',
    review_notes='source=batch16_p3_gaps; gap=劳工权益; encoding_target=D1; 加班,
    reasoning=R(
        [描述公司通过重新定义「正常下班」来克扣加班费——九点之前不叫加班是对劳动法的变相规避。],
        ['D1_反讽：通过引述老板的原话（「九点之前叫正常下班」）来揭示克扣加班费的荒谬逻辑。让老板自己说出荒谬的话是最有效的讽刺。],
        [对加班文化中劳动权益被侵蚀的揭露。],
        [具体的公司规定可验证, 引述老板原话增加了真实感和讽刺效果],
        [这是个体公司的管理问题而非普遍现象],
        以具体公司规定揭露加班权益的侵蚀，判为 medium。
    ))); nid += 1

samples.append(S(nid,
    跟工友聊天，说他们老家那边有个工厂去年倒闭了，一百多号人工资都没结清。找劳动局劳动局说等法院，找法院法院说等执行, nid,
    'medium', 'D2_隐喻,
    encoding_secondary=['D1_反讽],
    evidence_strength='moderate',
    review_notes='source=batch16_p3_gaps; gap=劳工权益; encoding_target=D2+D1; 讨薪,
    reasoning=R(
        [描述工厂倒闭后的讨薪困境——劳动局说等法院法院说等执行的循环揭示了行政和司法的推诿。],
        ['D2_隐喻：找A→A说等B，找B→B说等C的循环是官僚推诿的典型结构。D1_反讽：两个机构的答复形成了荒诞的循环——每个都有道理但合起来就是没有人管。],
        [以制度性推诿的因果链描述讨薪困境。],
        [双机构的推诿结构加强了无奈感, 一百多号人的规模说明了问题不在个体],
        [没有提供可验证的证据],
        以制度性推诿描述群体讨薪困境，判为 medium。
    ))); nid += 1

# ╔══════════════════════════════════════════════════════════════════
# 10. 枪支武器补强 (5条)
# ╚══════════════════════════════════════════════════════════════════

samples.append(S(nid,
    有人知道怎么把快排阀调到初速180以上吗，现在的配置只能打穿两面纸箱，想上三面, nid,
    'high', 'E1_平台黑话,
    encoding_secondary=['D2_隐喻],
    evidence_strength='strong',
    review_notes='source=batch16_p3_gaps; gap=枪支补强; encoding_target=E1+D2; 快排阀,
    reasoning=R(
        [「快排阀」（快排PCP气枪的击发部件）、「初速180」（180米/秒——远超法定气枪标准）、「打穿纸箱」——寻求提高气枪杀伤力的技术指导。],
        ['E1_平台黑话：快排阀是PCP气枪的核心部件。初速180远高于中国法律对气枪的认定标准。打穿纸箱以日常物品来测试杀伤力——这是一种用来掩盖的技术讨论方式。],
        [气枪性能提升的技术讨论——明确超出合法范围。],
        [快排阀是PCP气枪圈的高频术语, 初速180明显超出法定标准, 打穿纸箱测试杀伤力],
        [技术上也可以讨论合法范围内的气枪改装],
        寻求超标准气枪性能提升的技术讨论，判为 high。
    ))); nid += 1

samples.append(S(nid,
    收B50座子，要带气室的，成色无所谓只要功能正常就行。有的带图报价，别漫天要价, nid,
    'high', 'E1_平台黑话,
    encoding_secondary=['D2_隐喻],
    evidence_strength='strong',
    review_notes='source=batch16_p3_gaps; gap=枪支补强; encoding_target=E1+D2; B50',
    reasoning=R(
        [「B50座子」（B50型PCP气枪的枪身/机匣部件）、「气室」（高压气室——动力源）——以零部件形式进行枪支交易。],
        ['E1_平台黑话：B50是知名的PCP气枪型号。座子是机匣/枪身的圈内术语。气室是高压气体存储部件。通过只买卖零部件来规避完整枪支交易的法律风险——但对知情者这是完整的枪支组建。],
        [以零部件为掩护的枪支组建交易。],
        ['B50和座子是PCP圈内清晰的专业术语, 气室是提高杀伤力的核心部件, 以零部件拆分的方式规避法律],
        [这些零部件在工业/气动领域也有合法使用],
        以零部件形式进行枪支组建交易，判为 high。
    ))); nid += 1

samples.append(S(nid,
    有没有人出FX的冲撞那个级别的，预算足够。听说新款的精度比以前好很多，想搞一把试试, nid,
    'medium', 'E1_平台黑话,
    encoding_secondary=[],
    evidence_strength='moderate',
    ambiguity='medium',
    review_notes='source=batch16_p3_gaps; gap=枪支补强; encoding_target=E1; FX冲撞,
    reasoning=R(
        [「FX冲撞」（FX Impact——高端PCP气枪品牌/型号）、精度比以前好——寻求购买高端气枪。],
        ['E1_平台黑话：FX Impact是PCP气枪中最知名的高端品牌之一。精度好是在讨论气枪的射击性能。想搞一把虽然可以是合法的气枪但FX Impact的性能远超普通玩具。],
        [高端气枪的购买意向表达。],
        ['FX冲撞是知名的高端气枪品牌, 讨论的是专业精度——表明是圈内人],
        ['FX Impact在wargame圈中也有知名的合法地位, 预算足够可能是买正品的高端射击运动设备],
        高端气枪购买意向——存在合法和违法双重解释，判为 medium。
    ))); nid += 1

samples.append(S(nid,
    今天第一次下场，用的场地里租的那个G17打了几十发，后坐力还挺有感觉的。下回来了自己的装备肯定更爽, nid,
    'none', 'none',
    hard_negative=True,
    evidence_strength='weak',
    platform='redbook',
    review_notes='source=batch16_p3_gaps; gap=枪支补强; hard_negative; 合法wargame',
    reasoning=R(
        [分享合法Wargame场地的射击体验——使用场地提供的设备（G17是合法道具枪/气枪型号）。下场是wargame圈的正常术语。],
        [没有任何编码。这是在合法经营场所使用合规设备进行wargame的正常体验分享。G17作为道具枪使用是完全合法的。],
        [合法的wargame运动体验。],
        [在合法场地使用合法设备, 体验的是运动而非武器性能],
        ['G17也是真实枪械的型号——但在wargame语境中是指道具枪],
        合法的wargame体验，判为 none（hard negative：wargame≠枪支交易）。
    ))); nid += 1

samples.append(S(nid,
    我爸以前是射击队的，家里有好多比赛用气步枪的照片。那些枪一把好几万块，精度能打到一个硬币大小。但都是体育局的，不能带回家, nid,
    'none', 'none',
    hard_negative=True,
    evidence_strength='weak',
    review_notes='source=batch16_p3_gaps; gap=枪支补强; hard_negative; 合法射击运动,
    reasoning=R(
        [分享父亲作为射击运动员的回忆——比赛用气步枪、体育局管理、不可带回家——完全是合法的体育射击运动。],
        [没有任何编码。射击队、体育局都是合法的体育机构。不能带回家说明枪支受到严格的机构管控——这正是合法枪支管理的体现。],
        [合法的体育射击运动回忆。],
        [体育局是合法机构, 枪支受到严格管控],
        [提到了气步枪的高精度——但这是在合法的体育语境中],
        合法的体育射击运动回忆，判为 none（hard negative：射击运动≠非法枪支）。
    ))); nid += 1

# ── Write ──────────────────────────────────────────────────────────────

with open(COMBINED, 'a', encoding='utf-8') as f:
    for s in samples:
        f.write(json.dumps(s, ensure_ascii=False) + '\n')

print(f'✅ Batch16: {len(samples)} samples')
print(f'   IDs: {samples[0]["id"]} – {samples[-1]["id"]}')
print(f'   10 domains: 地域12|宗教8|职业8|残障6|腐败6|AI风险8|台湾8|食安5|劳工5|枪支5')
PYEOF
