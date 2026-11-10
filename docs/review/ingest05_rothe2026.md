# AI 審查報告：ingest #5 rothe2026（精簡模式）

- 審查者：獨立子代理，只寫報告不改檔；只修必修
- 範圍：40 句；所有數字（macro F1 0.92/0.90/0.84/0.79、F1 0.76–0.96、3/12 場、±2 秒、14 秒）皆正確

## 寫入前的自我修正（檢查往前移的效果）

- 確認清單中原本預告一個「同一來源內部分歧」：結果段說方法 "clearly outperforms" 2 個 baseline，但 logistic regression baseline 很接近。
- 寫入前對照 Table 6–9 和 p.10 才發現：被 "clearly outperforms" 的兩個是 LOGREG-RAW 與 RULE-BASED，作者本來就說 LOGREG-TUPLE 是 "a strong contender"。**這不是矛盾**，所以沒有標 ⚠。
- 這是上一輪「過度標記分歧」的教訓，在寫入前就被擋下來。

## 必修（已修正）

| 檔案 | 問題 | 處理 |
|---|---|---|
| sources/rothe2026.md | 「每種狀態都同時描述雙方」以偏概全，Counter/Fast Attack 是例外（Table 1 防守方為 N.A.） | 改為「大多數」，補例外 |
| concepts/class-imbalance-metrics.md | 「少見狀態 F1 低 = 不平衡問題」是 Wiki 的推論卻標了出處；作者自己的解釋是前處理刪除控球時間 | 推論加標註，補上作者解釋 |
| concepts/performance-analysis.md | Rahimian 的問句（解釋方法是否需要 SHAP）被寫成「簡單模型就夠了」，引文脫離上下文 | 改寫為原本的問句與脈絡 |

## 建議（只記錄，未修）

1. 「反擊類狀態」範圍太寬，只有 Counter/Fast Attack 建議加球速
2. p.10 原文是 "appears to outperform"，少了 hedge
3. p.2 原文是 "typically requires expert knowledge"，少了 "typically"

## 審查者對「比較（不是分歧）」的判斷

- 結論合理，但原本的理由「任務不同」不夠準確；真正原因是兩篇談的「複雜度」不是同一個維度，而且 Rahimian 是問句。已依此改寫。

## 觀察

- 必修 3 個中有 2 個又是「把可能性或問句寫成肯定的結論」，和 ingest #1 的錯誤類型相同。前移檢查擋掉了過度標記，但**語氣問題從頭到尾都沒消失**。
