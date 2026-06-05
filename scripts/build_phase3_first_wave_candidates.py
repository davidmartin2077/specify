#!/usr/bin/env python3
"""Build the first phase-3 targeted expansion batch.

The batch follows data/processed/phase3_sampling_plan.json. It writes raw
needs_revision candidates only and never merges into processed data.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
OUTPUT_PATH = ROOT / "data/raw/phase3_first_wave_candidates.jsonl"
BATCH = "phase3_v1_coverage_gaps"


MODE_META = {
    "direct": {
        "risk": "high",
        "hard_negative": False,
        "ambiguity": "medium",
        "evidence": "strong",
        "context_note": "文本与互动语境共同显示明确风险意图或招揽信号。",
        "support": ["文本含较明确的风险意图。", "上下文回复进一步强化风险解释。"],
        "counter": ["未提供完整行为链或具体对象，仍需人工复核。"],
    },
    "obfuscated": {
        "risk": "medium",
        "hard_negative": False,
        "ambiguity": "medium",
        "evidence": "moderate",
        "context_note": "文本使用替代词、缩写、符号或平台规避表达，语境支持风险解读。",
        "support": ["存在规避直接表达的编码信号。", "上下文出现共同理解或私下沟通暗示。"],
        "counter": ["具体目标或行为仍未完全展开，不宜直接判最高风险。"],
    },
    "contextual": {
        "risk": "medium",
        "hard_negative": False,
        "ambiguity": "high",
        "evidence": "moderate",
        "context_note": "单看文本存在普通解释，但标题、上级评论或回复链使风险解释值得召回复核。",
        "support": ["文本与当前话题组合后出现风险联想。", "上下文提供了独立支持。"],
        "counter": ["脱离当前语境时可能只是普通表达。"],
    },
    "weak_signal": {
        "risk": "low",
        "hard_negative": True,
        "ambiguity": "high",
        "evidence": "weak",
        "context_note": "文本存在弱风险联想，但普通解释仍然更完整。",
        "support": ["存在值得高召回关注的弱信号。"],
        "counter": ["缺少明确目标、规避意图或行为链。", "普通解释目前更强。"],
    },
    "safe_context": {
        "risk": "none",
        "hard_negative": True,
        "ambiguity": "low",
        "evidence": "weak",
        "context_note": "上下文明确属于新闻、教育、举报、科普或正常生活语境。",
        "support": [],
        "counter": ["文本没有招揽、交易、攻击、规避或现实动员意图。", "普通语境和反证完整。"],
    },
}


PROFILES: list[dict[str, Any]] = [
    {
        "category": "sexual_content",
        "name": "色情低俗",
        "quota": 25,
        "primary": "E1_平台黑话",
        "secondary": ["C4_典故/物品/符号借用"],
        "platforms": ["抖音", "小红书", "贴吧", "微信群", "微博"],
        "texts": {
            "direct": [
                "同城想找人陪夜的直接来，价钱好商量",
                "今晚还有空档，要求不多，先说预算",
                "想约的别磨叽，时间地点都能谈",
                "只接本地，先把条件和时长说清楚",
                "有偿陪伴，今晚能到的优先",
            ],
            "obfuscated": [
                "那个字别打，按老说法问茶就行",
                "同城的看门牌号，完整版别在这里问",
                "价格不写，主页第一条有暗号",
                "写直了会没，想懂的按两个表情找",
                "别问项目，按以前的颜色说就懂了",
            ],
            "contextual": [
                "夜里有空，想认识新朋友的留个话",
                "同城还没睡的举个手，聊天别太拘谨",
                "今晚一个人有点无聊，有没有附近的",
                "主页刚更新，成年人自己判断要不要看",
                "有些内容这里放不了，知道怎么找就行",
            ],
            "weak_signal": [
                "这个交友帖说得有点含糊，先看看再说",
                "同城聊天本身没问题，就是这个账号有点怪",
                "主页内容看着暧昧，但也可能只是擦边玩梗",
                "成年人话题可以讨论，别默认都是交易",
                "这句陪伴可能只是情绪聊天，证据还不够",
            ],
            "safe_context": [
                "青春期教育需要正规讲解，不该一提性教育就删",
                "电影分级是保护未成年人，不等于传播低俗内容",
                "新闻报道案件时提到相关词，不代表评论在招揽",
                "举报擦边账号时别复述链接，直接走平台流程",
                "医学科普讨论生殖健康，应结合专业语境判断",
            ],
        },
    },
    {
        "category": "spam_ads_fraud",
        "name": "广告诈骗导流",
        "quota": 25,
        "primary": "E1_平台黑话",
        "secondary": ["C4_典故/物品/符号借用"],
        "platforms": ["微信群", "小红书", "微博", "QQ群", "抖音"],
        "texts": {
            "direct": [
                "垫一单返两单，今天名额只剩最后几个",
                "资料费先交，岗位当天就能安排",
                "订单异常点我发的入口，补偿马上到账",
                "急用钱的私我，不看征信，先付手续费",
                "跟着老师买明天的票，收益稳稳的",
            ],
            "obfuscated": [
                "别写刷那个字，按一单两回的说法来",
                "平台不让留号，去头像角落找联系方式",
                "退款入口不能公开发，私下给你小窗",
                "想进内圈看字母缩写，别在评论问价",
                "招聘两个字容易限流，群里都叫上车",
            ],
            "contextual": [
                "想空闲赚点的来问，流程很简单",
                "这个岗位不用经验，先准备一点材料费",
                "订单有问题可以走快速补偿通道",
                "进群以后有人带，跟着做就不会错",
                "机会不等人，想参加的今晚之前决定",
            ],
            "weak_signal": [
                "说是兼职但没写公司名称，先谨慎看看",
                "这个补偿消息像客服，也可能只是通知",
                "群里一直说稳赚，但还没看到收费",
                "让加私人号有点怪，不过可能是正常招聘",
                "限时名额不一定是诈骗，但值得核验",
            ],
            "safe_context": [
                "刷单返利都是骗局，先赚小钱只是让你放松警惕",
                "正规招聘不会让求职者先交资料费",
                "退款请走平台客服，陌生链接不要点",
                "投资没有稳赚，老师带单的话术要警惕",
                "公益捐款只走官方公示渠道，私人二维码别扫",
            ],
        },
    },
    {
        "category": "insulting_abuse",
        "name": "辱骂群体攻击",
        "quota": 25,
        "primary": "D1_反讽",
        "secondary": ["D3_借代", "E1_平台黑话"],
        "platforms": ["微博", "贴吧", "知乎", "B站", "微信群"],
        "texts": {
            "direct": [
                "这群人就是没救了，走到哪都只会添乱",
                "一看那个地方来的就知道什么素质",
                "他们这种人根本不配在这里说话",
                "别装了，你们整个群体都一个德行",
                "这种人就该被赶出去，省得污染环境",
            ],
            "obfuscated": [
                "老外号不打了，两个首字母大家都懂",
                "那个群体名会被删，换成动物叫法就行",
                "别写地域名，用口音那个梗代一下",
                "骂人的字拆开打，不然评论发不出",
                "那帮人的简称就三个符号，别写全",
            ],
            "contextual": [
                "又是他们，熟悉的操作一点没变",
                "这个口音一出来，评论区气氛就变了",
                "每次出事都能看到同一拨人",
                "别问是哪群，懂的人已经开始躲了",
                "看头像就知道会说出什么话",
            ],
            "weak_signal": [
                "这句他们可能只是指帖子里的几个人",
                "吐槽口音不一定是在攻击整个地域",
                "说没素质有点冲，但目标还不明确",
                "这个外号可能是朋友间玩笑，先别升级",
                "反讽味道很重，不过也可能只针对行为",
            ],
            "safe_context": [
                "社区规则引用辱骂词只是举例，不是在攻击用户",
                "网暴截图里的脏话已经打码，别再复读造成二次伤害",
                "讨论地域歧视是为了反对偏见，不该误判为地图炮",
                "语言学课程分析方言和口音，不等于嘲笑某地人",
                "举报群体攻击时保留证据即可，不要继续扩散辱称",
            ],
        },
    },
    {
        "category": "weapons_explosives",
        "name": "枪爆武器",
        "quota": 25,
        "primary": "C4_典故/物品/符号借用",
        "secondary": ["E1_平台黑话", "B4_符号/空格/Unicode 干扰"],
        "platforms": ["论坛", "贴吧", "微信群", "B站", "微博"],
        "texts": {
            "direct": [
                "要成套零件的来问，能装起来的优先",
                "这批弹药还有，数量不多，先到先得",
                "想找真家伙的别在评论问，直接联系",
                "材料和成品都有，只接懂行的人",
                "需要特殊装备的报数量和地点",
            ],
            "obfuscated": [
                "木仓两个字别连着打，按编号问",
                "零件名字不写全，图里圈出来的就是",
                "那个响的东西用烟花表情代一下",
                "按弓单的写法问，别说原字",
                "成套的叫玩具，懂装的人自然懂",
            ],
            "contextual": [
                "这套零件成色不错，装起来应该挺顺",
                "声音够不够大，远一点还能听见吗",
                "老型号的配件还有没有，想补一套",
                "图里那几个金属件能单独出吗",
                "懂结构的看看，这个尺寸是不是刚好",
            ],
            "weak_signal": [
                "说成套零件有点可疑，也可能是机械维修",
                "提到声音大不一定是在说危险物品",
                "这个玩具可能真的是模型收藏",
                "编号交流看着隐晦，但物品类型还不明",
                "金属配件本身有正常工业用途",
            ],
            "safe_context": [
                "博物馆里的武器都是历史展品，不代表可以求购买渠道",
                "实验室安全课讨论爆炸危险，是为了避免事故",
                "警方通报提到涉枪案件属于新闻事实描述",
                "影视道具制作要遵守规定，不能当成真实装备交易",
                "军事历史课程讲弹药演变，不涉及现实获取方式",
            ],
        },
    },
    {
        "category": "cyber_abuse",
        "name": "网络黑产安全风险",
        "quota": 25,
        "primary": "C4_典故/物品/符号借用",
        "secondary": ["E1_平台黑话"],
        "platforms": ["论坛", "B站", "知乎", "微信群", "贴吧"],
        "texts": {
            "direct": [
                "这批号库刚拖出来，想要的报量",
                "能直接跑的版本还有，别问原理",
                "账号找回团队接单，成功后再算钱",
                "后台权限已经拿到，谁要数据自己说",
                "这套工具专门绕验证，想试的来",
            ],
            "obfuscated": [
                "库那个字别写，用表格代一下",
                "能跑的东西不发论坛，去老地方拿",
                "找回两个字太显眼，群里都叫捞",
                "权限截图别带域名，懂的人看路径",
                "工具名字拆成首字母，别让搜索搜到",
            ],
            "contextual": [
                "这个后台也太纸糊了，随便试试就进去了",
                "别讲修复，我只想知道怎么复现",
                "这个账号还能不能捞回来，有熟手吗",
                "截图里的数据看着不像演示环境",
                "验证那一步有没有更省事的办法",
            ],
            "weak_signal": [
                "问复现可能是安全研究，也可能越界",
                "说捞账号不一定是黑产，可能只是官方申诉",
                "后台截图可疑，但还不能确认是真实数据",
                "工具绕验证听着危险，具体用途未知",
                "讨论号库可能是在举报泄露事件",
            ],
            "safe_context": [
                "漏洞复盘重点是修复，不是教人攻击别人的站",
                "账号被盗应走官方申诉，不要找所谓找回团队",
                "安全新闻报道数据泄露时不要继续转发样本",
                "课程中的攻击演示必须在授权环境里完成",
                "反诈宣传解释钓鱼网站，是为了提醒用户识别",
            ],
        },
    },
    {
        "category": "violence_extremism",
        "name": "暴力极端",
        "quota": 25,
        "primary": "E3_话题/热点触发",
        "secondary": ["D2_夸张/反话", "E1_平台黑话"],
        "platforms": ["微信群", "微博", "贴吧", "抖音", "论坛"],
        "texts": {
            "direct": [
                "别只在网上说，今晚都到现场来",
                "真有胆子的带上家伙一起去",
                "这次必须让对面付出代价，一个都别放过",
                "人已经叫齐了，到了以后统一行动",
                "别劝了，今天就要把事情闹大",
            ],
            "obfuscated": [
                "那个动作别写，用火焰表情表示",
                "现场两个字容易删，群里改叫看电影",
                "家伙别说全，按工具箱来问",
                "统一行动用三个字母代替，别留痕",
                "名单不发文字，只发颜色和编号",
            ],
            "contextual": [
                "今晚谁敢来就知道到底怎么回事了",
                "光说没用，总得有人先站出来",
                "到时候别问为什么，跟着人群走",
                "这口气忍不了，必须给个说法",
                "大家都准备好了，就差一个时间",
            ],
            "weak_signal": [
                "说到现场可能只是围观，也可能是动员",
                "必须给说法是情绪表达，未必指向暴力",
                "准备好了的具体内容不明，先保留召回",
                "跟着人群走有风险联想，但证据不足",
                "火焰表情可能只是激动，不一定是行动暗号",
            ],
            "safe_context": [
                "安全演练里的危险动作都是反面教材，现实中不要模仿",
                "新闻报道极端事件是为了说明危害，不是宣传行为",
                "家长提醒孩子远离暴力内容属于安全教育",
                "历史课程讨论战争不能被当成现实动员",
                "社区用户劝大家冷静并报警，应视为反风险表达",
            ],
        },
    },
    {
        "category": "illegal_goods",
        "name": "违禁交易",
        "quota": 25,
        "primary": "C4_典故/物品/符号借用",
        "secondary": ["E1_平台黑话"],
        "platforms": ["贴吧", "微信群", "论坛", "小红书", "微博"],
        "texts": {
            "direct": [
                "这批货纯度不错，要多少直接报",
                "同城能送，想拿的先说数量",
                "还有几份，熟人价格可以谈",
                "需要特殊药的来问，别走公开平台",
                "货已经到手，老客户优先",
            ],
            "obfuscated": [
                "名字别打，按小白片问就行",
                "那种粉用字母代，群里别写全",
                "颜色和批次对上就是，懂货的私下说",
                "药那个字会限流，改成糖就好",
                "数量用表情发，别留文字记录",
            ],
            "contextual": [
                "这批成色比上次好，价格也差不多",
                "同城有需要的吗，东西不方便公开说",
                "剩的不多了，想要的早点决定",
                "老规矩先看货，别在楼里问细节",
                "那个白色的还有没有，上次挺好用",
            ],
            "weak_signal": [
                "说成色和批次像交易，也可能是普通商品",
                "特殊药可能是正规处方药，证据还不够",
                "白色的指向不明，先保留低风险召回",
                "同城送货本身正常，关键看具体物品",
                "不方便公开说有规避感，但行为链不完整",
            ],
            "safe_context": [
                "法院案例提到违禁品只是案件事实，不代表可以求渠道",
                "处方药必须遵医嘱，病友群不要互相推荐购买",
                "警方禁毒宣传讲危害，是明确反对相关行为",
                "医学课程讨论麻醉药物属于专业教育语境",
                "举报可疑交易时不要复述联系方式，直接提交平台",
            ],
        },
    },
    {
        "category": "gambling",
        "name": "赌博",
        "quota": 25,
        "primary": "E1_平台黑话",
        "secondary": ["C3_数字代指", "C4_典故/物品/符号借用"],
        "platforms": ["贴吧", "微信群", "微博", "虎扑", "抖音"],
        "texts": {
            "direct": [
                "今晚那场还能下，想跟的赶紧",
                "桌子差两个人，底分按老规矩",
                "号码已经出了，想买的报份数",
                "这边赔率更好，第一次还能送",
                "想翻本的来，今晚有人带着走",
            ],
            "obfuscated": [
                "下注两个字别打，按上车说",
                "号码用水果代，别在群名片写",
                "水位只在老地方发，楼里别问",
                "桌子和底分别连着说，容易被封",
                "今晚那场用队服颜色代，懂的跟",
            ],
            "contextual": [
                "今晚水位变化挺有意思，老地方见",
                "这桌还缺人，规矩进来再说",
                "号码看着有戏，想跟的自己判断",
                "市场太看好主队了，临场再看看",
                "上次没跟上的，这次别又错过",
            ],
            "weak_signal": [
                "水位可能只是赛事数据，也可能是盘口黑话",
                "牌桌缺人可能是娱乐，未必涉及金钱",
                "说跟一手有赌博联想，但还没看到下注",
                "号码有戏可能是在聊彩票，也可能是普通预测",
                "翻本是风险词，但也可能是泛化玩笑",
            ],
            "safe_context": [
                "珍爱生活远离赌博，别把家庭日子都压上去",
                "警方通报赌球案件是为了提醒公众远离风险",
                "概率课拿彩票举例，是为了说明期望值并不划算",
                "家庭打牌不带钱只是节日娱乐，不应直接误判",
                "体育数据复盘明确说只看比赛不参与下注",
            ],
        },
    },
    {
        "category": "public_affairs",
        "name": "公共事务",
        "quota": 15,
        "primary": "D1_反讽",
        "secondary": ["E3_话题/热点触发"],
        "platforms": ["微博", "知乎", "B站"],
        "texts": {
            "direct": [
                "流程都是摆设，今晚直接去门口堵着",
                "别再等通知了，大家一起到现场讨说法",
                "名单已经整理好，明天统一去反映",
            ],
            "obfuscated": [
                "那个部门别写全，用两个字母代",
                "现场集合改叫散步，群里别说原词",
                "名单不发文字，按楼栋编号统计",
            ],
            "contextual": [
                "先说都是为你好，后面就不让问为什么",
                "熟悉的流程又来了，解释永远在最后",
                "这次大家都沉默，反而说明问题不小",
            ],
            "weak_signal": [
                "这句像公共议题反讽，也可能只是普通抱怨",
                "说流程熟悉有影射感，但目标不明确",
                "大家沉默不一定有特殊含义，需要更多上下文",
            ],
            "safe_context": [
                "政策解读先看原文，不要只截一句话带节奏",
                "业主维权应收集证据并走街道和物业流程",
                "公共事务课程讨论治理案例属于正常教学",
            ],
        },
    },
    {
        "category": "political_history",
        "name": "政治历史鉴证梗",
        "quota": 15,
        "primary": "C1_历史人物类比",
        "secondary": ["C2_历史事件影射", "E2_时间节点触发"],
        "platforms": ["B站", "微博", "知乎"],
        "texts": {
            "direct": [
                "这段讲古人是假，照着今天那位写才是真",
                "五月三十五一到，评论区又自动安静",
                "他隐忍多年再回来收拾局面，这映射太明显了",
            ],
            "obfuscated": [
                "名字别打，用那位历史角色代一下",
                "日期不写全，往后多一天大家就懂",
                "现实人物用剧中称号说，别直接点名",
            ],
            "contextual": [
                "又是熟悉的剧本，历史总喜欢换衣服重演",
                "这句古诗今天看，意思突然不一样了",
                "旧照片一发出来，评论区都不说话了",
            ],
            "weak_signal": [
                "历史类比有可能成立，但也可能只是读史感想",
                "异常日期值得召回，不过缺少事件上下文",
                "角色经历像现实人物，具体映射仍不明确",
            ],
            "safe_context": [
                "历史课强调史料互证，不是所有类比都能套现实",
                "影视角色讨论围绕剧情本身，没有现实人物映射",
                "周年纪念是私人生活事件，不应因为日期就过度联想",
            ],
        },
    },
    {
        "category": "platform_censorship_evasion",
        "name": "平台规避审查黑话",
        "quota": 15,
        "primary": "E1_平台黑话",
        "secondary": ["A2_拼音/首字母缩写", "B4_符号/空格/Unicode 干扰"],
        "platforms": ["B站", "微博", "贴吧"],
        "texts": {
            "direct": [
                "原词发不出来，中间加空格就能过",
                "全名别打，三个首字母评论区都懂",
                "那个词用表情替掉，不然马上没",
            ],
            "obfuscated": [
                "别连着打，拆成偏旁再发",
                "用同音字写，搜索就搜不到了",
                "两个字母加一个符号，老用户看得懂",
            ],
            "contextual": [
                "这里不方便展开，知道的人自然知道",
                "主页第一条自己看，别在评论问细节",
                "那个名字不能说，说了号就没了",
            ],
            "weak_signal": [
                "说不能展开可能只是话题太长，不一定是规避",
                "首字母可能是普通缩写，目标还不明确",
                "加空格也可能只是排版，需要结合语境",
            ],
            "safe_context": [
                "结局不能说是为了避免剧透，不是规避审核",
                "作品集放主页属于正常内容展示，没有风险导流",
                "技术文档里的首字母缩写含义明确，不应乱猜",
            ],
        },
    },
]


def context_for(profile: dict[str, Any], mode: str, index: int) -> dict[str, Any]:
    name = profile["name"]
    mode_context = {
        "direct": {
            "title": f"{name}相关可疑互动区",
            "parent": "有人询问具体方式或条件",
            "replies": ["怎么联系", "别在公开区说"],
        },
        "obfuscated": {
            "title": f"{name}相关边缘话题",
            "parent": "原评论疑似因写得太直接被删除",
            "replies": ["懂了", "别写全"],
        },
        "contextual": {
            "title": f"{name}相关讨论区",
            "parent": "上级评论语义含糊",
            "replies": ["这话什么意思", "有点可疑"],
        },
        "weak_signal": {
            "title": f"{name}语境边界讨论",
            "parent": "目前缺少完整上下文",
            "replies": ["先别下结论", "需要更多信息"],
        },
        "safe_context": {
            "title": f"{name}新闻/教育/正常语境",
            "parent": "内容用于提醒、科普、举报或正常讨论",
            "replies": ["别误判", "结合语境看"],
        },
    }[mode]
    return {
        "title": mode_context["title"],
        "description": "",
        "parent_comment": mode_context["parent"],
        "reply_chain": mode_context["replies"],
        "time": "",
        "topic": name,
    }


def reasoning(profile: dict[str, Any], mode: str, text: str) -> dict[str, Any]:
    meta = MODE_META[mode]
    risk = meta["risk"]
    if risk == "none":
        encoding = ["未形成稳定风险编码；风险词或相关概念只作为召回线索。"]
    else:
        encoding = [f"主要按 {profile['primary']} 解构，属于{profile['name']}语境。"]
        if profile["secondary"]:
            encoding.append(f"辅助机制包括：{'、'.join(profile['secondary'])}。")
        if mode in {"obfuscated", "contextual", "weak_signal"}:
            encoding.append("该信号值得高召回关注，但仍需结合上下文确认具体指向。")
    return {
        "literal_analysis": [f"字面上是在表达：{text}"],
        "encoding_analysis": encoding,
        "context_analysis": [meta["context_note"]],
        "supporting_evidence": meta["support"],
        "counter_evidence": meta["counter"],
        "final_rationale": {
            "high": "风险意图与语境相互印证，按高召回目标暂标为 high。",
            "medium": "存在值得解构和召回的风险信号，但具体目标或行为链仍不完整，暂标为 medium。",
            "low": "存在弱风险联想，保留召回价值；普通解释目前更强，暂标为 low。",
            "none": "新闻、教育、举报或正常语境的反证完整，暂标为 none，避免仅凭词面误判。",
        }[risk],
    }


def build_rows() -> list[dict[str, Any]]:
    rows = []
    serial = 1
    for profile in PROFILES:
        per_mode = profile["quota"] // 5
        for mode in ("direct", "obfuscated", "contextual", "weak_signal", "safe_context"):
            texts = profile["texts"][mode]
            if len(texts) != per_mode:
                raise ValueError(
                    f"{profile['category']} {mode}: expected {per_mode} texts, got {len(texts)}"
                )
            for local_index, text in enumerate(texts, start=1):
                meta = MODE_META[mode]
                risk = meta["risk"]
                rows.append(
                    {
                        "id": f"PHASE3_W1_{serial:04d}_{profile['category'].upper()}_{mode.upper()}",
                        "source_type": "synthetic",
                        "platform": profile["platforms"][(local_index - 1) % len(profile["platforms"])],
                        "text": text,
                        "context": context_for(profile, mode, local_index),
                        "risk_level": risk,
                        "encoding_primary": "none" if risk == "none" else profile["primary"],
                        "encoding_secondary": [] if risk == "none" else profile["secondary"],
                        "context_required": True,
                        "ambiguity": meta["ambiguity"],
                        "evidence_strength": meta["evidence"],
                        "hard_negative": meta["hard_negative"],
                        "target_known": False,
                        "target_reference": "匿名化风险语境",
                        "should_explain_target": False,
                        "freshness": "stable",
                        "reasoning": reasoning(profile, mode, text),
                        "quality_status": "needs_revision",
                        "review_notes": (
                            f"source=phase3_first_wave; batch={BATCH}; category={profile['category']}; "
                            f"contrast_mode={mode}; cluster={profile['category']}_{mode}; "
                            "not_merged; needs_human_review"
                        ),
                    }
                )
                serial += 1
    return rows


def write_jsonl(rows: list[dict[str, Any]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False, separators=(",", ":")) + "\n")


def main() -> int:
    rows = build_rows()
    if len(rows) != 245:
        raise ValueError(f"Expected 245 rows, got {len(rows)}")
    write_jsonl(rows, OUTPUT_PATH)
    print(f"Wrote {len(rows)} phase-3 first-wave candidates to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
