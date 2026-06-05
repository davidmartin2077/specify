# 项目启动说明

本目录包含两个初始规范文档：

1. `编码方式分类手册_v1.0_draft.md`
   - 定义编码方式分类体系。
   - 用于指导数据构造、模型输出字段、评测维度设计。

2. `数据标注规范_v1.0_draft.md`
   - 定义 JSONL 数据结构、标注流程、风险等级、hard negative、DPO/GRPO 数据规范。
   - 可直接作为 Codex 搭建项目 schema、数据校验脚本和样例生成脚本的依据。

建议下一步让 Codex 先生成以下文件：

```text
risk-reasoning-model/
├── docs/
│   ├── encoding_taxonomy.md
│   └── annotation_guideline.md
├── data/
│   ├── raw/
│   ├── processed/
│   ├── mvp/
│   └── eval/
├── schemas/
│   └── sample_schema.json
├── scripts/
│   ├── validate_dataset.py
│   ├── split_dataset.py
│   ├── build_sft_dataset.py
│   └── build_preference_dataset.py
├── configs/
│   ├── llamafactory_sft_qwen3b_lora.yaml
│   └── grpo_config_draft.yaml
└── README.md
```
