# 审查微调项目

本项目用于构建“语义风险推理”方向的审查微调数据、评测集与训练配置。

核心目标不是训练敏感词分类器，而是让模型学习：

1. 识别文本中的非字面表达。
2. 拆解谐音、字形、语义、修辞、语境与组合编码机制。
3. 结合上下文判断风险等级。
4. 给出简洁、可审计、不过度联想的证据与反证。

## 已加入规则

- [docs/encoding_taxonomy.md](/Users/davidchankong/Documents/审查微调/docs/encoding_taxonomy.md)：编码方式分类手册，定义 A-F 六类编码机制与风险判断原则。
- [docs/annotation_guideline.md](/Users/davidchankong/Documents/审查微调/docs/annotation_guideline.md)：数据标注规范，定义 JSONL 样本结构、风险等级、hard negative、SFT/DPO/GRPO 数据要求。
- [docs/project_start_readme.md](/Users/davidchankong/Documents/审查微调/docs/project_start_readme.md)：原始规则包中的项目启动说明。
- [schemas/sample_schema.json](/Users/davidchankong/Documents/审查微调/schemas/sample_schema.json)：根据标注规范整理的单条 JSONL 样本 schema。

## 目录结构

```text
docs/              规则与标注规范
data/raw/          原始样本
data/processed/    清洗后样本
data/mvp/          MVP 训练/验证/测试数据
data/eval/         专项评测集
schemas/           数据结构约束
scripts/           数据校验、切分和构建脚本
configs/           训练与强化学习配置
```

## 数据入口约定

训练数据建议使用 JSONL，每行一条样本，并遵循 `schemas/sample_schema.json`。

最小样本骨架：

```json
{
  "id": "C1_HIGH_0001",
  "split": "train",
  "source_type": "synthetic",
  "platform": "bilibili",
  "text": "示例文本",
  "context": {},
  "risk_level": "high",
  "encoding_primary": "C1_历史人物类比",
  "encoding_secondary": [],
  "context_required": true,
  "ambiguity": "medium",
  "evidence_strength": "strong",
  "hard_negative": false,
  "target_reference": "",
  "should_explain_target": false,
  "reasoning": {
    "literal_analysis": [],
    "encoding_analysis": [],
    "context_analysis": [],
    "supporting_evidence": [],
    "counter_evidence": [],
    "final_rationale": ""
  },
  "quality_status": "draft",
  "review_notes": ""
}
```

## 第一阶段建议

优先构建 1000 条 MVP 数据：

```text
high: 250
medium: 250
low: 200
none: 300
hard_negative: >= 150
context_required: >= 250
```

第一批类别建议从 `C1`、`C2`、`C4`、`D1`、`E2`、`E3`、`B1`、`A1` 开始。
