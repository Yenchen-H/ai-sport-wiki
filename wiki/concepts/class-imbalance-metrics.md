---
type: concept
title: 不平衡資料與評估指標
sources: [cohan2021, majumdar2024, rothe2026, buhamra2025]
updated: 2026-11-10
---

# Class imbalance and evaluation metrics（不平衡資料與評估指標）

## 定義

- 不平衡資料：某一類（例如「受傷」）佔比極低。Cohan 的 NBA 資料中，受傷不到 4% [Cohan 2021, p.3]。
- "accuracy does not give meaningful results when dealing with skewed data where the classes are unbalanced" [Cohan 2021, p.6]

## 中文說明

- Majumdar 的英超資料：原始資料 10,520 筆非傷害、133 筆傷害，不平衡比 0.013；改成「7 天內會受傷」的建模資料後是 10,142 比 378，不平衡比 0.037 [Majumdar 2024, p.4]。
- 只預測多數類，或依類別比例隨機猜的 baseline 模型，AUC 都是 0.50 [Majumdar 2024, p.6] [Majumdar 2024, p.7]。
- 除了不平衡，傷害與非傷害資料點在特徵空間還會重疊，傳統模型常常認不出模式 [Majumdar 2024, p.4]。

- 一直猜多數類就能拿到很高的 accuracy：No Injury 模型 accuracy 99.8%，卻完全沒用 [Cohan 2021, p.6]。
- 比較適合的指標是 ROC AUC 和 average precision [Cohan 2021, p.6]。
- 不平衡問題常見「precision 低、recall 高」的結果 [Cohan 2021, p.6]。
- Rothe 的戰術狀態中，最少見的兩個狀態 F1 最低（0.76、0.84），所有 baseline 也都在這兩個狀態表現最弱 [Rothe 2026, p.10]。（推論）這和不平衡資料的問題類似。
- 但作者自己的解釋不同：這兩個狀態受到「失球後刪除控球時間」與「控球片段太短」的前處理影響特別大 [Rothe 2026, p.16]。
- Counter Build-up vs. High-Block 平均每場只有約 14 秒，作者認為這種數值不穩定可能影響戰術結論 [Rothe 2026, p.15]。

## 反例：什麼時候可以用 accuracy

- Buhamra 的網球資料中，第一位選手是隨機指定的 [Buhamra 2025, p.2]。
- （推論）因此勝負兩類應大致平衡，分類正確率是合理的指標；Buhamra 也同時報告 Brier score 等指標 [Buhamra 2025, p.10]。

## 常見陷阱：沒有切分資料

- 很多傷害預測研究用同一份資料訓練和評估，造成對模型能力過度自信 [Cohan 2021, p.4]。
- 98% accuracy、0.97 ROC AUC 這類結果看起來亮眼，但泛化能力未知，因此有誤導性 [Cohan 2021, p.4]。

## 處理不平衡的方法

### ⚠ 說法分歧：重抽樣和加權有沒有用？

- Cohan：over-sampling、under-sampling、加權、合成樣本，全部讓 METIC 的驗證集表現變差，最後都沒採用 [Cohan 2021, p.4]。
- 但 Cohan 也提到部分傳統模型加了 over-sampling 後表現變好 [Cohan 2021, p.5]。
- Majumdar：SMOTE 加上 cost-sensitive 加權（傷害類 9 倍或 11 倍），"we were able to maximize the accurate prediction of injuries" [Majumdar 2024, p.9]
- Majumdar 的權重是多次跑 cross-validation，並 "noticed how they perform on the test data" 後依經驗調整出來的 [Majumdar 2024, p.6]
- 注意：Majumdar 沒有列出「不做平衡」的對照結果，「有效」是作者的主張；兩篇的模型與資料都不同，比較像效果依情境而異，不是正面衝突 [Majumdar 2024, p.9]。

## 相關頁面

- [傷害預測](injury-prediction.md)
- [研究筆記：選才模型的評估陷阱](../notes/talent-id-evaluation-pitfalls.md)
