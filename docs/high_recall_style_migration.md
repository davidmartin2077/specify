# 高召回风格迁移说明

## 目标

将现有 330 条正式候选的回答风格向用户已认可的 phase2 候选靠拢，同时保持原始 text、映射含义、风险等级、编码方式和上下文不变。

本项目面向偏高召回的语义风险解构场景。模型应当对弱黑话、梗、谐音、人物代指、历史影射和平台规避保持敏感，并说明为什么值得召回复核；但高召回不等于把所有正常文本改标为风险。

## 高召回与误杀的关系

高召回训练应主要通过以下方式实现：

1. 对 low/medium 样本明确写出可疑编码和映射路径。
2. 即使目标不完整，也说明为什么该信号值得召回复核。
3. 对 high 样本强调编码机制与上下文如何相互印证。
4. 保留 none/hard negative，训练模型识别反赌、反诈、新闻、科普、课程、正规招聘等普通语境。
5. 不批量把 none 改成 medium/high；否则模型会退化成关键词匹配器，解构能力反而变弱。

## text 改写原则

1. 短句不等于质量差。真实互联网鉴证梗经常只有几个字，例如人物称呼、数字、外号和一句回复。
2. 不为了拉长句子而补充解释，否则会破坏原始映射和真实评论口吻。
3. 已经自然的 meme、Grok、词库候选 text 应尽量保留。
4. 后续只定向修改明显的审核员口吻、说明文口吻、机械模板或不自然词串。
5. text 改写必须独立人工复核，不能仅靠规则批量覆盖正式数据。

## 当前预览产物

`scripts/build_phase2_style_preview.py` 会读取现有 330 条正式候选，并生成：

1. `data/raw/combined_candidates_phase2_style_preview.jsonl`
2. `data/raw/combined_candidates_phase2_style_preview.json`

预览只重写 reasoning：

1. 更具体地说明主要和次要编码机制。
2. 将标题、上级评论、回复链、话题和时间节点写进语境分析。
3. 对弱信号使用“值得高召回关注，但不足以直接确认目标”的表达。
4. 对 high 强调编码与语境互相印证。
5. 对 none/low 保留普通解释和反证，避免只凭命中误判。

预览不修改：

1. id
2. text
3. risk_level
4. encoding_primary / encoding_secondary
5. context
6. context_required
7. hard_negative

该预览尚未替换 processed，也没有用于重建 SFT。
