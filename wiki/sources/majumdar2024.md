---
type: source
title: Majumdar et al. (2024) 英超訓練負荷與傷害的多球季機器學習
sources: [majumdar2024]
updated: 2026-11-10
---

# Majumdar et al. (2024) A multi-season machine learning approach to examine the training load and injury relationship in professional soccer

## 書目

- Majumdar, A., Bakirov, R., Hodges, D., McCullagh, S., & Rees, T. (2024). *Journal of Sports Analytics, 10*, 47–65. DOI: 10.3233/JSA-240718
- 授權：CC BY-NC 4.0
- 頁碼對照：**PDF p.N = 期刊 p.N+46**（PDF 共 19 頁，p.13 起是參考文獻與附錄）
- 原檔：[raw/majumdar2024.pdf](../../raw/majumdar2024.pdf)
- 研究經費來自 AFC Bournemouth 與 Bournemouth University，共同作者包含球隊的運動科學人員 [Majumdar 2024, p.13]。

## 一句話摘要

- 用英超一支球隊 5 個球季的訓練負荷資料，以 XGBoost 與 ANN 預測球員未來 7 天內的非接觸性傷害，再用 SHAP 解釋 [Majumdar 2024, p.1] [Majumdar 2024, p.3]。

## 研究問題

- 用機器學習檢視訓練負荷與足球傷害的關係 [Majumdar 2024, p.1]。
- 作者指出既有研究的限制：評估指標交代不清、前處理細節不足、多半只用單一球季 [Majumdar 2024, p.2]。

## 方法

- 受試者：35 位男性職業球員，資料從 2014–2015 到 2018–2019 球季 [Majumdar 2024, p.1]。
- 106 個負荷變數：40 個 GPS、6 個個人資料、14 個體能、4 個心理、ACWR／MSWR／EWMA 各 14 個 [Majumdar 2024, p.4]。
- 133 筆非接觸性傷害，原始資料不平衡比 0.013；轉成 7 天預測資料集後是 378 筆傷害、不平衡比 0.037 [Majumdar 2024, p.4]。
- 另外自建兩個特徵：「last injury area」和「days since last injury」[Majumdar 2024, p.3]。
- 預測目標是未來 7 天內是否受傷，對應英超大約每 7 天一場比賽 [Majumdar 2024, p.3] [Majumdar 2024, p.4]。
- 前 4.5 季資料訓練，之後半季沒看過的資料測試 [Majumdar 2024, p.4]。
- Logistic regression、kNN、決策樹、隨機森林表現差，XGBoost 與 ANN 最好 [Majumdar 2024, p.4]。
- 處理不平衡：SMOTE，加上把傷害類權重設為 9 倍（XGBoost）和 11 倍（ANN）[Majumdar 2024, p.6]。

## 主要發現

- XGBoost 預測對 26／37 筆傷害，precision 10%、recall 73% [Majumdar 2024, p.8]。
- ANN 預測對 28／37 筆傷害，precision 13%、recall 77% [Majumdar 2024, p.8]。
- 兩個 baseline 模型的 AUC 都是 0.50，等於隨機猜 [Majumdar 2024, p.7]。
- 在訓練與驗證資料中，ANN 的 SHAP 前五名 "appear to be" last injury area、EWMA of meta energy、weight、meta energy、age [Majumdar 2024, p.7]
- 多數傷害發生在 ACWR 0.5–1.5 之間，作者說這 "appeared to differ" 於既有文獻 [Majumdar 2024, p.11]

## 限制

- 有新資料就要重新訓練，預測結果可能改變 [Majumdar 2024, p.12]。
- 傷害與非傷害資料點在特徵空間中重疊，作者認為可能是能區分兩類的特徵還沒被蒐集 [Majumdar 2024, p.4]。
- 作者提到最佳演算法可能取決於情境與資料品質 [Majumdar 2024, p.12]。
- 測試集可能間接參與調參，見 [模型驗證方式](../concepts/model-validation.md) [Majumdar 2024, p.6]。
- （Wiki 觀察，非作者所列）資料只來自一支球隊 [Majumdar 2024, p.1]。

## 相關頁面

- [傷害預測](../concepts/injury-prediction.md)、[訓練負荷](../concepts/training-load.md)、[模型驗證方式](../concepts/model-validation.md)、[不平衡資料與評估指標](../concepts/class-imbalance-metrics.md)、[SHAP](../concepts/shap.md)
