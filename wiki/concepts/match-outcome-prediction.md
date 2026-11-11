---
type: concept
title: 比賽結果預測
sources: [buhamra2025, goel2021]
updated: 2026-11-11
---

# Match outcome prediction（比賽結果預測）

## 定義

- 預測一場比賽誰會贏；在網球中，可以建模「第一位選手」獲勝的機率 [Buhamra 2025, p.1]。

## 各來源怎麼用

- Buhamra 2025（網球大滿貫）：用排名、積分、Elo、賭盤賠率、年齡等差值作為特徵，比較迴歸與機器學習模型 [Buhamra 2025, p.1]。
- 最佳結果是 expanding window 下的 XGBoost，正確率 0.8306 [Buhamra 2025, p.14]。
- 解釋結果：Elo 差越大，第一位選手的預測勝率越高，但個別比賽的影響差異很大 [Buhamra 2025, p.14]。

## 比賽中即時預測

- Goel 2021（板球 IPL）：第二局開始後每投一球就更新一次預測，特徵包含會動態變化的目標分數 [Goel 2021, p.1] [Goel 2021, p.3]。
- 作者觀察到大約從第 15 輪開始，幾乎所有模型都預測得很好 [Goel 2021, p.9]。
- 特徵太多反而表現差：90 個特徵篩成 30 個後才改善 [Goel 2021, p.3]。

### ⚠ 說法分歧：網球預測的正確率上限

- Wilkens：平均預測正確率 "cannot exceed approximately 70%" [Buhamra 2025, p.2]
- Gao 與 Kowalczyk：用隨機森林達到超過 80% 的正確率 [Buhamra 2025, p.2]。
- Buhamra 自己在大滿貫資料上最高達 0.8306 [Buhamra 2025, p.14]。
- 注意：前兩者是 Buhamra 轉述的文獻，三者的資料範圍不同（Wilkens 含男女職業賽，Gao 用 2000–2016 ATP 資料，Buhamra 只有男子大滿貫）[Buhamra 2025, p.1] [Buhamra 2025, p.2]。

## 比較（不是分歧）：模型選擇重不重要？

- Buhamra：模型間差異不大，預測策略與特徵工程更關鍵 [Buhamra 2025, p.16]。
- Majumdar：logistic regression、kNN、決策樹、隨機森林都表現差，只有 XGBoost 與 ANN 表現好 [Majumdar 2024, p.4]。
- 兩篇的任務與資料不同（網球勝負 vs. 足球傷害，傷害資料極度不平衡），所以不視為說法分歧 [Majumdar 2024, p.4] [Buhamra 2025, p.2]。

## 比較（不是分歧）：深度學習一定比較好嗎？

- Cohan（NBA 傷害）：METIC "performs significantly better than the other examined approaches in terms of ROC AUC, average precision, recall, and F1 score" [Cohan 2021, p.6]
- Goel（板球）：整場模型的測試準確率，深度學習與傳統機器學習都約 72% [Goel 2021, p.6]；但作者認為深度學習的 recall 與 F1 較高 [Goel 2021, p.5]。
- Buhamra（網球）：各模型差異不大，預測策略更重要 [Buhamra 2025, p.16]。
- 三篇的任務與資料都不同，所以只是比較，不視為說法分歧 [Cohan 2021, p.4] [Goel 2021, p.1] [Buhamra 2025, p.1]。

## 相關頁面

- [來源：Goel 2021](../sources/goel2021.md)、[模型驗證方式](model-validation.md)、[可解釋 AI](explainable-ai.md)
