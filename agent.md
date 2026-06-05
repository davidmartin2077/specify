# 项目记忆

## 重要提醒：不要重复已完成工作

本文件记录的是项目交接记忆。接手新窗口时必须先读本文件，并把“已完成步骤”和“当前状态”视为事实来源；除非用户明确要求回滚、重跑或复核，否则不要重复执行已经完成的导入、合并、校验、SFT 重建、split 生成等流水线，避免浪费算力和意外覆盖数据。当前所有截至本文件记录的工作都已经做过：正式候选集为 675 条，SFT 为 675 条，默认 train/validation/test split 已生成且通过校验。

项目初衷是训练一个约 4B 规模的中文语义风险推理/审核微调模型，让小模型具备识别互联网鉴证梗、互联网黑话、风险词语境、隐喻、反讽、指桑骂槐、历史影射、人物代指、上下文风险和反证的能力。当前阶段仍然是数据集准备的初始阶段，还没有进入正式训练配置、训练运行或模型评测阶段。最初 330 条样本只是第一版数据骨架；当前虽已扩充至 675 条，但数量和人工复核深度仍不足以支撑 4B 模型稳定学会这些能力。后续大方向是继续分层扩充和复核高质量数据，而不是急着训练。

## 项目目标

本项目是“审查微调/语义风险推理”项目，目标是构建用于约 4B 小模型微调的数据、规则、评测与训练配置。模型目标不是做敏感词匹配，而是学习基于证据判断中文短文本中的互联网鉴证梗、黑话、风险词语境、非字面表达、编码机制、上下文风险和反证。

## 已完成步骤

1. 已将下载目录中的规则包加入项目。
2. 已创建 `docs/encoding_taxonomy.md`，作为编码方式分类手册。
3. 已创建 `docs/annotation_guideline.md`，作为数据标注规范。
4. 已创建 `docs/project_start_readme.md`，保存原始项目启动说明。
5. 已创建 `schemas/sample_schema.json`，作为单条 JSONL 标注样本的机器可读 schema。
6. 已创建项目入口 `README.md`，说明项目目标、规则入口、目录结构和第一阶段数据建议。
7. 已初始化基础目录：`data/raw/`、`data/processed/`、`data/mvp/`、`data/eval/`、`scripts/`、`configs/`。
8. 已创建 `scripts/validate_dataset.py`，用于校验 JSONL 标注数据的必填字段、枚举值、字段类型、推理链结构、反证要求、重复 id 和 hard negative 基本约束。
9. 已创建 `data/raw/label_examples.jsonl`，包含 high、medium、low、none 与 hard negative 的第一批结构化示例样本。
10. 已将 Grok 生成的 50 条候选样本原文加入 `data/raw/grok_candidates_50.txt`，作为待规整、待复核的原始输入。
11. 已将用户 Word 文档 `1.docx` 中的 7 条样本抽取为 `data/raw/user_candidates_1.txt`。
12. 已创建 `scripts/build_combined_candidates.py`，用于把 Grok 原始候选和用户手写候选规整为训练格式。
13. 已生成 `data/processed/combined_candidates.jsonl` 和 `data/processed/combined_candidates.json`，共 57 条结构化候选样本，并通过 `scripts/validate_dataset.py` 校验。
14. 已创建 `scripts/build_sft_dataset.py`，用于把标注 JSONL 转成 SFT 指令格式。
15. 已运行 `scripts/build_sft_dataset.py`，生成 `data/mvp/sft_candidates.jsonl` 和 `data/mvp/sft_candidates.json`，共 57 条 SFT 训练样本。
16. 已检查用户提供的两份模型扩写候选文件：`/Users/davidchankong/Downloads/meme_expand_candidates_120.jsonl` 和 `/Users/davidchankong/Downloads/gemini-code-1780556702163.json`。
17. 已对两份扩写候选运行 `scripts/validate_dataset.py`：`meme_expand_candidates_120.jsonl` 共 120 条，风险分布符合预期，但存在 29 个 schema/规则错误，主要是 `risk_level=none` 时未使用 `encoding_primary=none`；`gemini-code-1780556702163.json` 实际为 JSONL 形态但扩展名为 `.json`，共 120 条，存在 416 个校验错误，主要是 `context`、`reasoning`、`encoding_secondary` 字段类型不符合 schema，以及 `evidence_strength=none` 等枚举错误。
18. 已初步完成人工质量判断：第一份结构更接近项目 schema，适合作为后续清洗底稿；第二份覆盖了一些有价值的 A2/B1/B3/B4/E3 样本，但结构不合格、表达更直接、`should_explain_target` 与匿名化约束冲突较多，只适合作为灵感池，不应直接入库。
19. 已将两份扩写原始文件复制进项目原始数据目录：`data/raw/meme_expand_candidates_120.jsonl` 和 `data/raw/gemini_expand_candidates_120.jsonl`。
20. 已创建 `scripts/import_expand_candidates.py`，用于清洗两份外部扩写候选并合并入库。脚本会为两类来源分别生成 `MEME_EXPAND_*` 和 `GEMINI_EXPAND_*` ID，修复 `context`、`reasoning`、`encoding_secondary`、`evidence_strength`、`none` 样本主编码等 schema 问题，并统一将 `should_explain_target` 设为 `false`，保留匿名化目标表述。
21. 已用 `scripts/import_expand_candidates.py` 生成 `data/processed/expand_candidates_cleaned.jsonl`，共 240 条清洗后的扩写样本，并合并进 `data/processed/combined_candidates.jsonl` 与 `data/processed/combined_candidates.json`。
22. 已修正 `scripts/import_expand_candidates.py` 为幂等脚本：重复运行时会先排除已有 `MEME_EXPAND_*` 和 `GEMINI_EXPAND_*` 样本，避免扩写样本重复追加。
23. 已重新运行 `scripts/validate_dataset.py` 校验 `data/processed/expand_candidates_cleaned.jsonl` 和 `data/processed/combined_candidates.jsonl`，均通过校验；合并后总样本数为 297 条，无重复 ID。
24. 已重新运行 `scripts/build_sft_dataset.py`，生成新版 `data/mvp/sft_candidates.jsonl` 和 `data/mvp/sft_candidates.json`，共 297 条 SFT 训练样本。
25. 已按用户要求自动接入 `konsheng/Sensitive-lexicon` 词库，克隆到 `data/raw/third_party/Sensitive-lexicon`；当前本地分支为 `main`，commit 为 `b38d80aece9837a434c601811c202d7640adeb4b`。
26. 已创建 `scripts/import_sensitive_lexicon.py`，用于从 `data/raw/third_party/Sensitive-lexicon/Vocabulary/*.txt` 读取词库，去重、粗分类、识别词形特征和编码机制标签，并生成采样计划。
27. 已运行 `scripts/import_sensitive_lexicon.py`，生成 `data/processed/lexicon_terms.jsonl`、`data/processed/lexicon_seed_terms.jsonl` 和 `data/processed/lexicon_sampling_plan.json`。当前去重后词条数为 50,706，采样种子数为 444。
28. 已创建 `scripts/build_lexicon_seed_candidates.py`，用于从词库 seed 中按类别少量生成 schema 合规的候选样本，覆盖 direct、ambiguous、hard_negative 三类候选，全部标记为 `quality_status=needs_revision`。
29. 已运行 `scripts/build_lexicon_seed_candidates.py`，生成 `data/raw/lexicon_seed_candidates.jsonl`，共 66 条词库种子候选样本，并通过 `scripts/validate_dataset.py` 校验。该文件尚未合并进 `data/processed/combined_candidates.*`。
30. 根据用户反馈，已重写 `scripts/build_lexicon_seed_candidates.py`：废弃原先“词条填空式”模板，改为按 `strict_redline`、`contextual_risk`、`transactional_risk` 三类生成更自然的短评论/弹幕/回复链候选；敏感词命中项保留在 `review_notes.matched_term` 中用于溯源，不再机械塞进 `text`。
31. 已重新生成 `data/raw/lexicon_seed_candidates.jsonl`，新版共 33 条，风险分布为 high 11、medium 11、low 4、none 7，hard_negative 10 条；已通过 `scripts/validate_dataset.py` 校验。该文件仍未入库，等待人工复核。
32. 根据用户进一步反馈，已再次改写 `scripts/build_lexicon_seed_candidates.py`：明确 `text` 字段必须模拟“被审核对象本身”，即真实评论/弹幕/回复，而不是审核员对评论的评价。已移除 `text` 中的“这条评论如何”“建议人工复核”“管理员看一下”等审核备注口吻，改为更口语化的用户发言，例如“别打全称，看首字母就行，懂的都懂”“NB 这双偏大半码吗？”“公司官网也有这个岗位，面试地址在邮件里，别加私人号”等。
33. 已同步收紧 `scripts/import_sensitive_lexicon.py` 的粗分类规则：不再用单字“爆”粗暴归入枪爆武器，并补充低俗类字形信号，减少 `matched_term` 溯源类别错配。已重新生成 `lexicon_terms.jsonl`、`lexicon_seed_terms.jsonl`、`lexicon_sampling_plan.json` 和新版 `lexicon_seed_candidates.jsonl`，后者仍为 33 条且校验通过。
34. 根据用户反馈“整体仍偏引流型”，已继续调整 `scripts/build_lexicon_seed_candidates.py`，降低“私聊/别说/懂的都懂/主页/进群”等单一导流规避风格占比，补充炫耀、盘口暗示、历史影射、普通投诉、课程/科普、正规招聘等场景。新版 `data/raw/lexicon_seed_candidates.jsonl` 仍为 33 条并通过校验，正式训练集仍未合并这些词库候选。
35. 已检查 `data/raw/lexicon_seed_candidates.jsonl`，共 33 条，schema 校验通过；所有词库候选仍保持 `quality_status=needs_revision`。
36. 已将 33 条词库候选以待复核候选身份合并进 `data/processed/combined_candidates.jsonl` 和 `data/processed/combined_candidates.json`。合并时保持幂等处理，processed 中的 `LEXICON_SEED_*` 入库副本已将溯源备注从 `not_merged` 修正为 `merged_processed`，raw 文件仍保留原始生成状态。
37. 已重新运行 `scripts/validate_dataset.py data/processed/combined_candidates.jsonl`，合并后的 processed 数据校验通过；当前正式候选总数为 330 条。
38. 已重新运行 `scripts/build_sft_dataset.py`，更新 `data/mvp/sft_candidates.jsonl` 和 `data/mvp/sft_candidates.json`，当前 SFT 样本数为 330 条。
39. 已创建 `scripts/split_dataset.py`，用于按 group 切分 annotated 数据，避免 `meme_cluster`、词库 `category`、语义簇等同组样本跨 train/validation/test 泄漏。默认输出到 `data/processed/splits/`，包含 `train.jsonl/.json`、`validation.jsonl/.json`、`test.jsonl/.json` 和 `split_report.json`。
40. 已运行 `scripts/split_dataset.py` 默认 0.8/0.1/0.1 切分，并用 `scripts/validate_dataset.py` 校验三份 split JSONL，均通过校验。当前切分为 train 264 条、validation 33 条、test 33 条，`split_report.json` 显示无 group 泄漏。
41. 根据用户强调的长期目标，已把阶段定位更新为：现有 330 条只是第一版数据骨架，距离让约 4B 模型稳定具备“互联网鉴证梗 + 互联网黑话 + 风险词语境判断”能力还不够；当前仍处于数据集准备初始阶段，后续主线是继续分层扩充高质量数据，不急着训练。
42. 已创建 `docs/data_expansion_plan.md`，记录第二阶段数据扩充计划：按互联网鉴证梗/人物历史代指、平台黑话/规避表达、风险词语境判断、正常表达与 hard negative 等能力轴分层扩充；新增候选默认先进入 raw，保持 `needs_revision`，不直接合并 processed。
43. 已创建 `scripts/build_phase2_seed_candidates.py`，作为第二阶段候选生成入口。该脚本只写入 `data/raw/phase2_seed_candidates.jsonl`，不触碰现有 330 条正式 processed 数据，也不重跑旧导入/合并/SFT 流程。
44. 已运行 `scripts/build_phase2_seed_candidates.py` 生成第一批 phase2 raw 候选，共 35 条，批次为 `phase2_v1_context_hard_negative`。这批重点覆盖风险词语境判断和 hard negative，包括反赌/反诈/正规招聘/安全科普/平台黑话/历史影射/数字代指/低俗与暴力语境边界等。已运行 `scripts/validate_dataset.py data/raw/phase2_seed_candidates.jsonl`，校验通过。该文件尚未合并进正式 processed，所有样本仍为 `quality_status=needs_revision`。
45. 用户已人工确认第一批 35 条 phase2 raw 候选风格“没有毛病”，可以沿当前方向继续扩充。后续扩充仍应保持 text 像真实评论/弹幕本身，重点强化语境边界和 hard negative，不要直接合并 processed。
46. 已沿用户认可的 phase2 风格继续扩展 `scripts/build_phase2_seed_candidates.py`，将 `data/raw/phase2_seed_candidates.jsonl` 从 35 条扩到 100 条。扩展内容继续围绕风险词语境判断、平台黑话/规避表达、互联网鉴证梗/历史人物与符号代指、正常表达 hard negative 等方向。已运行 `scripts/validate_dataset.py data/raw/phase2_seed_candidates.jsonl`，校验通过；该 raw 文件仍未合并 processed，全部保持 `quality_status=needs_revision` 和 `not_merged`。
47. 用户已人工确认扩展后的 100 条 phase2 raw 候选“也很好”。这说明当前 phase2 生成方向可继续沿用：以真实评论/弹幕口吻构造语境边界样本，重点覆盖互联网鉴证梗、互联网黑话、风险词语境判断和 hard negative。下一步可以继续扩充，也可以准备独立导入脚本将已认可的 phase2 候选幂等合并进 processed，但合并前仍应保持 `needs_revision`，不直接标 approved。
48. 用户提出正式 330 条旧候选也应在映射含义不变的情况下向 phase2 风格靠拢，并强调模型服务于偏高召回的审查工具，解构抽象能力必须强，不必机械追求大量无风险样本。设计决策：高召回应主要通过强化弱信号解构、映射路径和 medium/low 召回复核表达实现，不直接批量把 none 改成风险；仍保留必要 hard negative，避免模型退化成关键词匹配器。
49. 已创建 `docs/high_recall_style_migration.md`，记录正式 330 条向 phase2 风格迁移的原则。短句和大量空格不应自动视为坏样本，因为它们可能正是鉴证梗、首字母、谐音或 `B4_符号/空格/Unicode 干扰` 机制。
50. 已创建 `scripts/build_phase2_style_preview.py`，从现有 330 条正式候选生成独立风格迁移预览：`data/raw/combined_candidates_phase2_style_preview.jsonl` 和 `.json`。该预览保持 id、text、risk_level、encoding、context、context_required、hard_negative 全部不变，只把 reasoning 改成更具体、偏高召回、接近 phase2 的解构表达；已通过 schema 校验。预览尚未覆盖 processed，也未用于重建 SFT。
51. 已创建并运行 `scripts/audit_text_style.py`，生成 `data/raw/combined_candidates_text_style_audit.json`。审计在 330 条中标出 14 条短句和 15 条大量空格样本作为人工复核提示；这些大多属于应保留的真实短梗或符号干扰机制，不能机械改写。
52. 用户已确认对 330 条 phase2 风格 reasoning 迁移预览满意，但当前决定“先这样”，暂不正式覆盖 processed。下一步重点转向利用 Sensitive-lexicon 建立风险词覆盖地图，识别当前数据尚未覆盖的类别、词形变体、编码机制和语境边界；不要逐词机械生成训练样本。
53. 已创建 `scripts/analyze_risk_coverage.py`，用于把 `data/processed/lexicon_terms.jsonl`、正式 330 条候选和 phase2 100 条 raw 候选连接起来，分析风险类别、词形/规避机制、风险等级、hard negative 和词面命中覆盖。该脚本只生成分析产物，不修改或合并训练数据。
54. 已运行风险词覆盖分析，共分析当前 430 条候选与 50,706 个去重词库条目，生成：`data/processed/risk_coverage_report.json`、`data/processed/phase3_sampling_plan.json` 和 `docs/risk_coverage_report.md`。
55. 覆盖分析显示当前明显薄弱类别包括色情低俗、辱骂/群体攻击、枪爆武器、网络黑产、暴力极端、违禁交易和赌博；政治历史/鉴证梗与平台规避已有相对较多基础样本，但仍需补长尾机制。完整第三阶段参考缺口约 788 条，建议第一波先定向扩充 245 条。
56. 风险词库使用原则进一步明确：词库只作为能力地图、召回器、采样池和压力测试来源。词库类别及代表 seed 属于粗分类结果，可能存在错配或普通词，使用前必须人工复核；不得直接把词库类别当训练标签，也不得逐词机械扩写。
57. 已创建 `scripts/build_phase3_first_wave_candidates.py`，按 `phase3_sampling_plan.json` 的第一波配额生成第三阶段定向扩充候选。脚本只写 raw，不覆盖 phase2，也不合并 processed。
58. 已运行 `scripts/build_phase3_first_wave_candidates.py`，生成 `data/raw/phase3_first_wave_candidates.jsonl`，共 245 条；已通过 `scripts/validate_dataset.py` 校验。所有样本均为 `quality_status=needs_revision` 和 `not_merged`。
59. 第三阶段第一波按五种对照模式构造：direct、obfuscated、contextual、weak_signal、safe_context 各 49 条。风险分布为 high 49、medium 98、low 49、none 49；hard negative 98 条。该分布偏高召回，none 仅占 20%，同时保留必要语境反证。
60. 第三阶段第一波类别配额：色情低俗、广告/诈骗/导流、辱骂/群体攻击、枪爆武器、网络黑产、暴力极端、违禁交易、赌博各 25 条；公共事务、政治历史/鉴证梗、平台规避/审查黑话各 15 条。
61. 已检查第三阶段第一波重复与风格：245 条无重复 ID、无重复 text；与正式 330 条和 phase2 100 条均无 text 重复；`data/raw/phase3_first_wave_text_style_audit.json` 未发现审核员口吻、异常短句或大量空格问题。该批尚待用户抽样确认，不应直接入库。
62. 用户已抽样确认第三阶段第一波 245 条“感觉还可以”，同意继续下一步。当前进入覆盖增益分析与统一幂等入库准备阶段；正式入库前先生成独立合并预览并校验，不直接覆盖 processed。
63. 已创建并运行 `scripts/analyze_phase3_coverage_delta.py`，生成 `data/processed/phase3_coverage_delta.json` 和 `docs/phase3_coverage_delta.md`。加入 phase3 第一波后，候选池从 430 条增至 675 条，八个 P0 薄弱类别各增加 25 条，公共事务、政治历史/鉴证梗、平台规避各增加 15 条。
64. 已创建 `scripts/import_expansion_batches.py`，用于统一、幂等导入 phase2 100 条和 phase3 第一波 245 条。脚本默认只生成合并预览，必须显式传入 `--apply` 才会修改正式 processed；重复运行会先排除已有 `PHASE2_SEED_*` 和 `PHASE3_W1_*`，避免重复追加。
65. 已用统一导入脚本生成 `data/processed/combined_candidates_expansion_preview.jsonl` 和 `.json`，共 675 条，并通过 schema 校验。预览中正式 330 条前缀逐条完全不变，新增 345 条均保持 `needs_revision`；预览入库副本标记为 `merged_processed`，raw 文件仍保持 `not_merged`。正式 `data/processed/combined_candidates.*` 当前仍为 330 条，尚未执行 `--apply`。
66. 已执行 `python3 scripts/import_expansion_batches.py --apply`，将 phase2 100 条和 phase3 第一波 245 条正式幂等合并进 `data/processed/combined_candidates.jsonl/.json`；正式候选集由 330 条增至 675 条，内容与已审核合并预览逐字节一致。
67. 已运行 `scripts/validate_dataset.py data/processed/combined_candidates.jsonl`，正式 675 条 processed 校验通过；675 个 ID 全部唯一，风险分布为 high 126、medium 234、low 145、none 170，hard negative 279 条，全部保持 `quality_status=needs_revision`。phase2/phase3 raw 文件仍保持 `not_merged`。
68. 已更新 `scripts/split_dataset.py`：补充 `PHASE2_SEED_*` 和 `PHASE3_W1_*` 来源识别；phase2 按 `axis/cluster`、phase3 按 `category/cluster/contrast_mode` 生成稳定模板组；split 报告新增 phase3 category 与 contrast_mode 分布，用于审计对照模板泄漏。
69. 已重新运行 `scripts/build_sft_dataset.py`，生成 675 条 `data/mvp/sft_candidates.jsonl/.json`；SFT ID 顺序与正式 processed 完全一致，JSONL 与 JSON 内容一致。
70. 已重新运行 `scripts/split_dataset.py` 并校验三份 split。当前 train 541、validation 67、test 67，合计覆盖 675 个唯一 ID；`split_report.json` 记录 226 个防泄漏组，0 个跨 split 泄漏组；55 个 phase3 模板组均未跨 split。
71. 已调整 `scripts/analyze_risk_coverage.py` 以适配正式 675 条状态：默认只分析 `data/processed/combined_candidates.jsonl`，支持重复传入 `--input` 分析多个独立候选集，并在输入间出现重复 ID 时直接报错，防止把已入库的 phase2/phase3 raw 再次重复计算。
72. 已基于正式 675 条重新生成 `data/processed/risk_coverage_report.json`、`data/processed/phase3_sampling_plan.json` 和 `docs/risk_coverage_report.md`。新版分析确认当前风险分布 high 126、medium 234、low 145、none 170，hard negative 279；完整参考缺口由 788 降至 593，下一波建议由 245 条降至 185 条。
73. 新版覆盖分析中，色情低俗与广告/诈骗/导流仍为 P0；辱骂/群体攻击、枪爆武器、公共事务、政治历史/鉴证梗降为 P1；平台规避、网络黑产、暴力极端、违禁交易、赌博降为 P2。该优先级仅作为抽样复核和下一波设计参考，不能替代人工标签判断。

## 当前状态

项目已经具备规则文档、标注规范、schema、基础目录、数据校验脚本、第一批示例 JSONL 数据、Grok 50 条原始候选样本、用户 7 条原始候选样本、两份外部模型扩写候选原始文件、扩写候选清洗导入脚本、词库候选生成与导入脚本、675 条已规整的待复核训练格式数据、SFT 数据构建脚本、675 条 SFT 训练样本、按 group 防泄漏的数据切分脚本，以及第二、第三阶段扩充产物。当前还没有训练配置；当前重点仍是继续扩充和复核数据。

项目还已接入 `konsheng/Sensitive-lexicon` 作为大词库召回与采样池，但尚未把词库全量变成训练数据。当前词库处理产物：

1. `data/processed/lexicon_terms.jsonl`：50,706 条去重词条索引。
2. `data/processed/lexicon_seed_terms.jsonl`：444 条分层采样种子。
3. `data/processed/lexicon_sampling_plan.json`：词库类别统计、机制统计与候选样本配额建议。
4. `data/raw/lexicon_seed_candidates.jsonl`：33 条 schema 合规的词库种子候选样本，已校验通过；其 processed 入库副本已合并进 `data/processed/combined_candidates.*`，但质量状态仍为 `needs_revision`。最新版 `text` 已改成被审核评论/弹幕本身的口语化表达，而不是审核员评价。

当前 `data/processed/combined_candidates.jsonl` 风险分布：

1. high：126 条。
2. medium：234 条。
3. low：145 条。
4. none：170 条。

当前 hard negative 为 279 条，`context_required=true` 为 624 条，全部 675 条保持 `quality_status=needs_revision`。

当前来源分布：

1. grok：50 条。
2. user：7 条。
3. meme_expansion：120 条。
4. gemini_expansion：120 条。
5. sensitive_lexicon_seed：33 条。
6. phase2_seed：100 条。
7. phase3_first_wave：245 条。

当前 `data/processed/splits/` 默认切分状态：

1. train：541 条；风险分布 high 108、medium 170、low 123、none 140；hard negative 229 条；`context_required=true` 492 条。
2. validation：67 条；风险分布 high 7、medium 38、low 10、none 12；hard negative 21 条；`context_required=true` 67 条。
3. test：67 条；风险分布 high 11、medium 26、low 12、none 18；hard negative 29 条；`context_required=true` 65 条。
4. `data/processed/splits/split_report.json` 记录 226 个 group 分配；当前无 `meme_cluster`、词库 `category`、phase2 `axis/cluster`、phase3 `category/cluster/contrast_mode` 或语义簇跨 split 泄漏。

当前 `data/processed/lexicon_sampling_plan.json` 词库粗分类分布：

1. spam_ads_fraud：21,133 条。
2. mixed_unknown：18,633 条，暂不直接生成训练样本。
3. platform_censorship_evasion：5,171 条。
4. political_history：1,631 条。
5. sexual_content：1,255 条。
6. weapons_explosives：1,036 条。
7. insulting_abuse：803 条。
8. public_affairs：605 条。
9. illegal_goods：185 条。
10. violence_extremism：155 条。
11. gambling：77 条。
12. cyber_abuse：22 条。

当前第二阶段 raw 扩充状态：

1. `docs/data_expansion_plan.md`：第二阶段数据扩充计划，明确 330 条只是第一版骨架，后续需要按能力轴继续扩充到更适合 4B SFT 起步的数据规模。
2. `scripts/build_phase2_seed_candidates.py`：phase2 候选生成脚本，只生成 raw 候选，不合并 processed。
3. `data/raw/phase2_seed_candidates.jsonl`：第一批 phase2 raw 候选共 100 条，已通过 schema 校验，raw 全部保持 `quality_status=needs_revision/not_merged`；其 processed 入库副本已正式合并。
4. 当前 phase2 风险分布：high 8、medium 39、low 1、none 52。
5. 当前 phase2 hard negative 为 53 条，`context_required=true` 为 100 条。
6. 当前 phase2 能力轴分布：risk_word_context 57 条、platform_black_slang 17 条、meme_forensics 26 条。
7. `data/raw/combined_candidates_phase2_style_preview.jsonl/.json`：现有正式 330 条的 phase2 风格 reasoning 迁移预览，已校验通过，尚未覆盖 processed。
8. `data/raw/combined_candidates_text_style_audit.json`：正式 330 条 text 风格审计报告，用于定向人工复核，不自动改写 text。

当前风险词覆盖分析状态：

1. `scripts/analyze_risk_coverage.py`：风险词覆盖分析脚本，默认只读正式 processed 与词库索引；可通过多个 `--input` 分析额外独立候选集，并拒绝重复 ID。
2. `data/processed/risk_coverage_report.json`：机器可读覆盖报告。
3. `data/processed/phase3_sampling_plan.json`：下一波定向采样参考；完整参考缺口 593 条，建议下一波 185 条。
4. `docs/risk_coverage_report.md`：可读版覆盖分析报告。
5. 当前正式 675 条候选合计风险分布：high 126、medium 234、low 145、none 170；hard negative 279。
6. 下一波仍优先机制：拼音/首字母、字形/符号干扰、语义映射/鉴证梗、平台/时间/话题上下文。
7. 当前 P0 类别：色情低俗、广告/诈骗/导流，各建议下一波约 25 条。
8. 当前 P1 类别：辱骂/群体攻击、枪爆武器、公共事务、政治历史/鉴证梗，各建议下一波约 15 条。
9. 当前 P2 类别：平台规避/审查黑话、网络黑产、暴力极端、违禁交易、赌博；已有一定基础，下一波应优先补真实长尾与困难边界，而非重复现有模板。

当前第三阶段第一波 raw 状态：

1. `scripts/build_phase3_first_wave_candidates.py`：第三阶段第一波定向候选生成脚本。
2. `data/raw/phase3_first_wave_candidates.jsonl`：245 条，已校验通过，raw 全部保持 `needs_revision/not_merged`；其 processed 入库副本已正式合并。
3. 风险分布：high 49、medium 98、low 49、none 49；hard negative 98。
4. 对照模式：direct、obfuscated、contextual、weak_signal、safe_context 各 49 条。
5. 与正式 330 条和 phase2 100 条均无 text 重复。
6. `data/raw/phase3_first_wave_text_style_audit.json`：第三阶段第一波 text 风格审计，当前无标记问题。

当前统一入库准备状态：

1. `scripts/analyze_phase3_coverage_delta.py`：phase3 加入前后覆盖增益分析脚本。
2. `data/processed/phase3_coverage_delta.json`、`docs/phase3_coverage_delta.md`：覆盖增益报告。
3. `scripts/import_expansion_batches.py`：phase2 + phase3 统一幂等导入脚本；已执行 `--apply`，内存复核确认在正式 675 条基础上再次构建仍为完全相同的 675 条。
4. `data/processed/combined_candidates_expansion_preview.jsonl/.json`：675 条合并预览，已校验通过。
5. 正式 processed 当前为 675 条；风险分布为 high 126、medium 234、low 145、none 170，hard negative 279。

## 数据来源计划

用户将提供两类原始内容：

1. 用户手写的一批简中互联网风险表达样本。
2. 由 Grok 生成的一批候选表达样本。

后续处理方式：

1. 先把原始内容作为待标注输入，不直接默认其标签正确。
2. 基于 `docs/encoding_taxonomy.md` 和 `docs/annotation_guideline.md` 逐条识别风险等级、编码方式、上下文依赖、证据与反证。
3. 输出符合 `schemas/sample_schema.json` 的 JSONL 数据。
4. 用 `scripts/validate_dataset.py` 校验生成结果。
5. 对证据不足、可能过度联想或标签争议较大的样本，优先降级到 medium/low 或标记为需要复核。

## 训练目标边界

用户当前只负责模型训练、微调和强化学习环节，不负责后续审核系统、拦截策略或产品动作设计。

当前模型目标：

1. 输入中文弹幕、评论或短文本后，模型能识别其中是否存在黑话、隐喻、讽刺、指桑骂槐、历史影射、人物代指等非字面表达。
2. 模型需要输出风险等级、编码方式、证据、反证和简洁结论。
3. 训练重点是让模型学会“看到黑话大概知道它在讽刺/隐喻/代指什么类型的对象”，而不是直接实现审核系统的 `block/review/allow` 动作。
4. 后续工作应围绕 SFT 数据、偏好数据、GRPO/RL 奖励、评测集和训练配置展开。

## 词库扩展策略

用户提出可参考 `konsheng/Sensitive-lexicon` 这类数以万计中文敏感词库，但不希望围绕每个词逐条构造训练数据。后续设计原则：

1. 不把大词库当成“逐词扩写任务”，而是当成召回器、分层采样池和弱标注来源。
2. 先对词库做类别归并，例如政治/色情/辱骂/暴恐/赌博/诈骗/广告导流/个人信息/地域与群体攻击/平台规避等，再按类别和子簇抽样。
3. 每个类别只做少量代表词和变体模式，重点训练模型理解“机制”和“上下文判断”，不是背完整词表。
4. 大词库适合配合规则系统做高召回，模型负责判断语境、歧义、反证、hard negative 和风险等级。
5. 数据构造应优先覆盖词语类型、构词模式、规避方式和上下文场景，而不是覆盖每一个词。
6. 后续可建立“词库命中但低风险/无风险”的 hard negative 专项，避免模型或规则因关键词撞车误杀。
7. 用户复核反馈：`data/raw/lexicon_seed_candidates.jsonl` 当前 text 过于模板化，像机器生成，不适合直接入库；部分词属于明显红线，不应构造宽松语境，另一些词如“赌博”需要结合反赌宣传、新闻、科普等语境判断。词库驱动数据必须区分“绝对红线/近似强规则类”和“语境依赖类”，不能一刀切。
8. 用户目标不是让模型把正常话全封掉，而是避免普通表达被误杀；同时承认审核场景本身会偏高召回。后续模型训练应重点训练“不要把正常话封掉”的语境判断能力，而不是替代规则系统放行所有可疑内容。

## 建议下一步

下一步优先围绕第二阶段扩数据继续推进：

1. 对 675 条候选分层抽样复核，优先检查 phase3 的 P0 类别、弱信号与 safe_context 对照质量；不要直接批量标 approved。
2. 根据新版覆盖报告设计下一波约 185 条定向扩充，重点补色情低俗、广告/诈骗/导流及 P1 类别的真实长尾与困难边界，避免机械重复第一波模板。
3. 下一波继续保持 raw-first、`needs_revision/not_merged`，经抽样确认和独立合并预览后再考虑入库。
4. 330 条 reasoning 迁移预览已获认可，但暂不正式覆盖 processed；后续需要时再执行。

## 工作约定

每推进一个阶段，都在本文件追加或更新：

- 新完成的步骤。
- 当前状态。
- 下一步建议。
- 重要设计决策或约束。

每完成一个可独立交接的阶段，还应创建本地 Git commit 并推送到 `origin/main`，确保 GitHub 与本地进度同步。
