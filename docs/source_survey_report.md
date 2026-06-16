# Source Survey Report

This report is generated without printing raw sensitive lexicon terms. It is safe to paste into a strict downstream API.

## Canonical Dataset

- Rows: 1295
- SHA256: `e2820b668c1a8c30df98228660ef018ee39cb07f074246e170db6f42e31b071d`
- Risk: `{'high': 444, 'low': 131, 'medium': 383, 'none': 337}`
- Source type: `{'real': 480, 'synthetic': 815}`
- Hard negative: 405
- Needs context: 45

## Derived Artifacts

- SFT rows: 1295
- Split rows: train 1037 / validation 129 / test 129

## Raw Batches

- `data/raw/batch10_new_patterns.jsonl`: 50 rows
- `data/raw/batch11_gap_fill.jsonl`: 59 rows
- `data/raw/batch12_doxxing.jsonl`: 40 rows
- `data/raw/batch1_natural_replacements.jsonl`: 56 rows
- `data/raw/batch2_natural_replacements.jsonl`: 27 rows
- `data/raw/batch3_natural_replacements.jsonl`: 46 rows
- `data/raw/batch4_natural_replacements.jsonl`: 47 rows
- `data/raw/batch5_gap_fill.jsonl`: 64 rows
- `data/raw/batch6_gap_fill.jsonl`: 69 rows
- `data/raw/batch7_high_risk.jsonl`: 50 rows
- `data/raw/batch8_tieba_style.jsonl`: 40 rows
- `data/raw/batch9_national_security.jsonl`: 45 rows
- `data/raw/batch_replace_01_dismantling.jsonl`: 20 rows
- `data/raw/batch_replace_02_abbr.jsonl`: 20 rows
- `data/raw/batch_replace_03_homophone.jsonl`: 20 rows
- `data/raw/batch_replace_04_taiwan.jsonl`: 20 rows
- `data/raw/batch_replace_05_history.jsonl`: 20 rows
- `data/raw/batch_replace_06_newslang1.jsonl`: 20 rows
- `data/raw/batch_replace_07_newslang2.jsonl`: 20 rows
- `data/raw/batch_replace_08_pronunciation.jsonl`: 20 rows
- `data/raw/batch_replace_09_numbers.jsonl`: 25 rows

## Sensitive Lexicon Files

- `data/raw/third_party/Sensitive-lexicon/Vocabulary/COVID-19词库.txt`: 76 terms, length p50=7, digits=3, latin=2, symbols=37
- `data/raw/third_party/Sensitive-lexicon/Vocabulary/GFW补充词库.txt`: 6414 terms, length p50=4, digits=264, latin=474, symbols=493
- `data/raw/third_party/Sensitive-lexicon/Vocabulary/其他词库.txt`: 157 terms, length p50=4, digits=25, latin=97, symbols=12
- `data/raw/third_party/Sensitive-lexicon/Vocabulary/反动词库.txt`: 557 terms, length p50=4, digits=22, latin=76, symbols=0
- `data/raw/third_party/Sensitive-lexicon/Vocabulary/广告类型.txt`: 123 terms, length p50=3, digits=2, latin=14, symbols=0
- `data/raw/third_party/Sensitive-lexicon/Vocabulary/政治类型.txt`: 326 terms, length p50=3, digits=0, latin=42, symbols=0
- `data/raw/third_party/Sensitive-lexicon/Vocabulary/新思想启蒙.txt`: 14 terms, length p50=5, digits=0, latin=0, symbols=0
- `data/raw/third_party/Sensitive-lexicon/Vocabulary/暴恐词库.txt`: 178 terms, length p50=3, digits=5, latin=36, symbols=1
- `data/raw/third_party/Sensitive-lexicon/Vocabulary/民生词库.txt`: 571 terms, length p50=3, digits=10, latin=70, symbols=9
- `data/raw/third_party/Sensitive-lexicon/Vocabulary/涉枪涉爆.txt`: 437 terms, length p50=7, digits=15, latin=32, symbols=41
- `data/raw/third_party/Sensitive-lexicon/Vocabulary/网易前端过滤敏感词库.txt`: 7746 terms, length p50=4, digits=228, latin=375, symbols=158
- `data/raw/third_party/Sensitive-lexicon/Vocabulary/色情类型.txt`: 304 terms, length p50=2, digits=0, latin=14, symbols=0
- `data/raw/third_party/Sensitive-lexicon/Vocabulary/色情词库.txt`: 929 terms, length p50=2, digits=10, latin=75, symbols=0
- `data/raw/third_party/Sensitive-lexicon/Vocabulary/补充词库.txt`: 1064 terms, length p50=3, digits=0, latin=0, symbols=0
- `data/raw/third_party/Sensitive-lexicon/Vocabulary/贪腐词库.txt`: 244 terms, length p50=3, digits=1, latin=18, symbols=22
- `data/raw/third_party/Sensitive-lexicon/Vocabulary/零时-Tencent.txt`: 53308 terms, length p50=7, digits=15986, latin=25601, symbols=24312
- `data/raw/third_party/Sensitive-lexicon/Vocabulary/非法网址.txt`: 14594 terms, length p50=13, digits=9162, latin=14594, symbols=14594

## Slang Reference Files

- `中国大陆网络用语列表整理.md`: 375 nonempty lines, table rows=0, sha256=`8c63aca0d6b61d33ae74ee879ccb124d96ce88ca468dbc9cde28a984b3741ef8`
- `中国大陆网络用语列表整理_v2.md`: 8571 nonempty lines, table rows=0, sha256=`d407a60b6ea1c4cdf2b72c6ac58c1c66d29c872b1496daa97f0ecefe7396ea6e`
- `docs/中国大陆网络用语列表_维基学院完整版.md`: 649 nonempty lines, table rows=577, sha256=`bd22856d7aca480d32707b1ad69e68c0f7da6d0301ed17653930ba68c51d386f`
