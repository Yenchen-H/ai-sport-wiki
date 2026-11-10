---
wiki: ../../../wiki/concepts/model-validation.md
---

# 證據卡：validation

> 只摘錄 wiki/concepts/model-validation.md，逐字複製，不改寫。

- 驗證的目的是知道模型在「沒看過的資料」上表現如何；用同一份資料訓練和評估會造成過度自信 [Cohan 2021, p.4]。
- Majumdar 的例子：EWMA of meta energy 在訓練資料是前三重要的特徵，訓練資料多數傷害發生在它超過 6.14 時，但測試資料中沒有任何資料點超過 6.14 [Majumdar 2024, p.10]。
- Rothe 2026：3 場訓練、12 場測試，測試集刻意包含訓練時沒出現的球隊，用來檢驗能否推廣到沒看過的球隊 [Rothe 2026, p.6]。
