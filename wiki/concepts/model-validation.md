---
type: concept
title: 模型驗證方式
sources: [cohan2021, majumdar2024, rothe2026, buhamra2025, goel2021]
updated: 2026-11-10
---

# Model validation（模型驗證方式）

## 定義

- 驗證的目的是知道模型在「沒看過的資料」上表現如何；用同一份資料訓練和評估會造成過度自信 [Cohan 2021, p.4]。

## 各來源怎麼用

- Cohan 2021：用 iterative stratified 方法切分，85% 訓練、15% 驗證（原文沒有說是否依時間切）[Cohan 2021, p.4]。
- Majumdar 2024：前 4.5 季訓練（內部再做 10-fold cross-validation），之後半季當獨立測試集 [Majumdar 2024, p.4]。
- Rothe 2026：3 場訓練、12 場測試，測試集刻意包含訓練時沒出現的球隊，用來檢驗能否推廣到沒看過的球隊 [Rothe 2026, p.6]。
- Rothe 也指出，其他球季與聯賽的適用性還沒測試，翻譯表可能需要定期更新 [Rothe 2026, p.16]。
- Buhamra 2025（網球）：比較三種策略，依時間順序擴大訓練資料的 expanding window 明顯優於 leave-one-tournament-out CV [Buhamra 2025, p.15]。
- 作者認為 "the predictions should occur in chronological order" [Buhamra 2025, p.13]
- 但只用最近 3 年的 rolling window 又表現較差，訓練資料必須夠大 [Buhamra 2025, p.16]。
- Buhamra 與 Majumdar 都支持依時間順序驗證，兩篇結論一致 [Buhamra 2025, p.16] [Majumdar 2024, p.11]。
- Goel 2021（板球）：依球季切分，用 2019 年當測試資料，訓練集內再用 KFold TimeSeriesSplit [Goel 2021, p.3]。

### ⚠ 說法分歧：測試集真的完全獨立嗎？（同一來源內部）

- Majumdar 寫測試集 "was not included for any of the data balancing, training, and validation phases" [Majumdar 2024, p.6]
- 但類別權重是跑 cross-validation 後 "noticed how they perform on the test data" 調出來的 [Majumdar 2024, p.6]
- 超參數調整的目標也是讓結果最佳 "when tested on the independent test dataset" [Majumdar 2024, p.5]

### ⚠ 說法分歧：怎樣才算可靠的驗證？（取捨，不是正面衝突）

- Cohan：切分訓練／驗證集並報告驗證集指標，"helps to ensure the generalizability of the presented algorithm" [Cohan 2021, p.10]
- Cohan 的資料本身涵蓋多隊多球季 [Cohan 2021, p.10]，並報告適合不平衡資料的指標 [Cohan 2021, p.10]。
- Majumdar：批評的對象是只用一季資料做 cross-validation 或 train-validation split 的研究，它們在「下一季」這類未見過的資料上表現如何仍有疑問 [Majumdar 2024, p.2]。
- Majumdar 沒有引用 Cohan，兩篇的差別比較像「切分方式」的取捨：Cohan 原文說切分 "helps to ensure" 泛化，語氣不是保證 [Cohan 2021, p.10]。
- Majumdar 的例子：EWMA of meta energy 在訓練資料是前三重要的特徵，訓練資料多數傷害發生在它超過 6.14 時，但測試資料中沒有任何資料點超過 6.14 [Majumdar 2024, p.10]。
- 作者認為如果改用隨機的 train-test split，會高估這個特徵的重要性 [Majumdar 2024, p.11]。

## 模型和情境有關

- Majumdar 用自己的資料重現 Rossi 的方法，預測結果不如 Rossi 原本報告的高 [Majumdar 2024, p.12]。
- 重現 Vallance 的方法時，模型預測出大部分的非傷害；兩篇原研究的最佳演算法，在 Majumdar 的資料上也只有 XGBoost 表現好 [Majumdar 2024, p.12]。
- "the choice of the best performing machine learning algorithm for each dataset is likely dependent on the context and the quality of those data" [Majumdar 2024, p.12]

## 相關頁面

- [不平衡資料與評估指標](class-imbalance-metrics.md)、[SHAP](shap.md)、[傷害預測](injury-prediction.md)
- [研究筆記：選才模型的評估陷阱](../notes/talent-id-evaluation-pitfalls.md)
