# 项目记忆

## 当前基准

正式数据 1255 条。已融合 ToxiCN/COLD/ChineseSafe 各 160 条真实评论。**platform 字段已全局移除。**

核心产物：

- `data/processed/combined_candidates.jsonl`：正式样本 1255 条。
- `data/processed/sft/sft_candidates.jsonl`：SFT 格式。
- `data/processed/splits/`：train 1005、validation 125、test 125。

正式分布：

```text
high    253
medium  485
low     132
none    385

hard_negative    510
needs_context    237
```

来源分布：

```text
batch1-4_natural          176  ← 自然中文口吻（已替换 grok/meme/gemini）
phase3_first_wave         245
phase3_second_wave        185
toxicn                    160
cold                      160
chinesesafe               160
phase2_seed                93
gemini_expansion           29
sensitive_lexicon_seed     33
user                        7
meme_expansion              0  ← 已清空
grok                        0  ← 已清空
```

## 已做完

- 项目结构清理：从 ~85 文件精简至 ~40 文件。
- platform 字段从所有数据文件和 SFT 格式中移除。
- **批次替换**：176 条自然口吻样本替换了全部 grok(50) + meme(35) + gemini(91) + phase2_seed(7)。
  - batch1: 56 条（C1/C2/C3/C4/D1/D2/D3/E1/E2/F）
  - batch2: 27 条（C1/C2/C4/D1/E2/B1/F + HN）
  - batch3: 46 条（侧重 LOW 边界和 underrepresented B1/B3/A3/C5/E4）
  - batch4: 47 条（混合补齐）
- 所有替换样本具有非模板 reasoning、自然中文互联网口吻、完整反证。
- merge 脚本已幂等化（`scripts/merge_replacements.py`）。
- 覆盖分析已基于 1255 条重跑。

## 当前决策

- 单条文本能判断风险就训练模型裸判，不硬凑上下文。
- high 不强制需要上下文；上下文只给真正单句无法稳定判断的样本。
- 目标场景是弹幕、应用评论、音乐评论等短文本。
- 已固化、出圈、高频的鉴证圈结构梗本身就是文本证据，可判 high。
- 外部数据的真实评论感有价值。

## 下一步

1. 继续替换剩余的 phase2/phase3 旧合成样本（~523 条）。
2. 建离线评测脚本，测 unsafe recall 和 false positive。
3. 后续扩充优先复用真实评论数据。

## 工作纪律

- 不要重新跑已完成的导入。
- 修改正式数据后必须重建 SFT、split，并校验 JSONL。
- 不要 `git push`，除非用户明确要求。
