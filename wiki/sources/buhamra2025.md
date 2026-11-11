---
type: source
title: Buhamra et al. (2025) 網球大滿貫的機器學習與預測策略比較
sources: [buhamra2025]
updated: 2026-11-11
---

# Buhamra et al. (2025) Comparing modern machine learning approaches and different forecast strategies on Grand Slam tennis tournaments

## 書目

- Buhamra, N., Groll, A., & Gerharz, A. (2025). *Journal of Sports Analytics, 11*, 1–18. DOI: 10.1177/22150218251338954
- 授權：CC BY-NC 4.0
- 頁碼對照：**PDF 頁碼 = 期刊頁碼**（共 18 頁，p.16 起是參考文獻）
- 原檔：[raw/buhamra2025.pdf](../../raw/buhamra2025.pdf)

## 一句話摘要

- 用 2011–2022 年男子大滿貫 5,013 場比賽，比較迴歸與機器學習模型，並比較三種預測策略對預測表現的影響 [Buhamra 2025, p.1]。

## 研究問題

- 預測「第一位選手」獲勝的機率，第一位選手是隨機指定的 [Buhamra 2025, p.1] [Buhamra 2025, p.2]。
- 機器學習方法在預測新比賽時，是否比先前研究的傳統迴歸方法更好 [Buhamra 2025, p.3]。

## 方法

- 特徵：年齡差、ATP 排名與積分差、賭盤賠率換算的勝率差、Elo 差，以及兩個考慮最佳年齡 28–32 歲的年齡變數 [Buhamra 2025, p.1] [Buhamra 2025, p.2] [Buhamra 2025, p.3]。
- 模型：邏輯迴歸（線性與 spline）、LASSO、分類樹、隨機森林、XGBoost、SVM、ANN，以及以賭盤賠率為準的 benchmark [Buhamra 2025, p.14] [Buhamra 2025, p.15]。
- 三種預測策略：leave-one-tournament-out CV（2011–2021）、expanding window（持續擴大訓練資料，預測 2022）、rolling window（只用最近 3 年）[Buhamra 2025, p.1]。
- 評估指標：分類正確率、predictive Bernoulli likelihood、Brier score [Buhamra 2025, p.9] [Buhamra 2025, p.10]。
- 用 PDP 與 ICE 解釋最佳的 XGBoost 模型 [Buhamra 2025, p.14]。

## 主要發現

- CV 策略下，各迴歸模型的正確率都略高於 77% [Buhamra 2025, p.15]。
- Expanding window 明顯優於 CV：正確率約 0.757–0.831 [Buhamra 2025, p.15] [Buhamra 2025, p.16]。
- XGBoost 在 expanding window 下的正確率最高，為 0.8306 [Buhamra 2025, p.14]。
- Rolling window（3 年）表現略差，作者認為 3 年的訓練資料不夠 [Buhamra 2025, p.16]。
- 作者結論：模型之間差異不大，"the specific forecast strategy used seems to play an even more important role" [Buhamra 2025, p.16]

## 限制

- 只有男子大滿貫，排除未實際比賽的退賽場次 [Buhamra 2025, p.3]。
- 作者計畫未來加入「statistical enhanced covariates」這類特徵工程 [Buhamra 2025, p.16]。

## 相關頁面

- [比賽結果預測](../concepts/match-outcome-prediction.md)、[模型驗證方式](../concepts/model-validation.md)、[可解釋 AI](../concepts/explainable-ai.md)
