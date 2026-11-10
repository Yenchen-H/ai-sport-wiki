---
type: source
title: Cohan et al. (2021) NBA 傷害預測的深度學習方法
sources: [cohan2021]
updated: 2026-11-10
---

# Cohan et al. (2021) A deep learning approach to injury forecasting in NBA basketball

## 書目

- Cohan, A., Schuster, J., & Fernandez, J. (2021). *Journal of Sports Analytics, 7*, 277–289. DOI: 10.3233/JSA-200529
- 授權：CC BY-NC 4.0
- 頁碼對照：**PDF p.N = 期刊 p.N+276**（PDF 共 13 頁，p.10 右欄起到 p.13 是參考文獻）
- 原檔：[raw/cohan2021.pdf](../../raw/cohan2021.pdf)

## 一句話摘要

- 用公開資料建立深度學習模型 METIC，依過去傷病、比賽活動與球員資料預測 NBA 球員的傷害 [Cohan 2021, p.1]。

## 研究問題

- 作者認為預測選手傷害風險 "has been a holy grail in sports medicine with little progress to date" [Cohan 2021, p.1]
- 原因包括樣本小、資料極度不平衡、統計方法不恰當 [Cohan 2021, p.1]。

## 方法

- 資料：2010–20 年 NBA 約 11k 筆傷害紀錄，從 Pro Sports Transactions 網站爬取 [Cohan 2021, p.2]。
- 傷害分成 8 類：back、contact、contusion、core、foot、ligament、muscle、upper body [Cohan 2021, p.3]。
- 238k 筆球員出賽紀錄；傷害歸到 30 天內最近一場比賽，共對應約 5k 筆傷害 [Cohan 2021, p.3]。
- 資料切分：85% 訓練、15% 驗證，用 iterative stratified 方法，驗證集有 750 筆傷害 [Cohan 2021, p.4]。
- METIC = Multiple bidirectional Encoder Transformers for Injury Classification，架構參考 BERT [Cohan 2021, p.4]。
- 輸入：前 5 場比賽與所有過去傷病；年齡等時間資料用 time2vec 嵌入；共 3.2 million 個參數 [Cohan 2021, p.4]。
- 和 Ridge、Extra Trees、Random Forest、Lasso、Naive Bayes、Logistic Regression、XGBoost 等模型比較 [Cohan 2021, p.4] [Cohan 2021, p.5]。

## 主要發現

- METIC 在 ROC AUC、average precision、recall、F1 都明顯優於其他模型，F1 是第二名的兩倍以上 [Cohan 2021, p.6]。
- METIC：accuracy 93.4%、ROC AUC 0.80、average precision 0.0087、recall 0.20、F1 0.020 [Cohan 2021, p.7]。
- 「永遠預測不會受傷」的 No Injury 模型 accuracy 高達 99.8%，但完全沒用 [Cohan 2021, p.6]。
- 接觸性傷害被認為無法預測，METIC 也預測不好（ROC AUC 0.74）[Cohan 2021, p.6] [Cohan 2021, p.7]。
- 年齡、比賽地點、身高、體重的單因子風險低，但作者寫 METIC 認為它們很重要，顯示變數間是非線性關係 [Cohan 2021, p.10]（與 p.4 的部分說法有出入，見 [傷害預測](../concepts/injury-prediction.md) 的說法分歧段落）。

## 限制

- 公開資料有雜訊，球隊有動機隱瞞傷情 [Cohan 2021, p.2] [Cohan 2021, p.3]。
- 沒有確切受傷時間、傷害細節、GPS 活動量與生物特徵資料 [Cohan 2021, p.2]。
- 風險因子分析是探索性的，而且看的是整體資料，抓不到個別選手的趨勢 [Cohan 2021, p.4]。

## 相關頁面

- [傷害預測](../concepts/injury-prediction.md)、[不平衡資料與評估指標](../concepts/class-imbalance-metrics.md)、[SHAP](../concepts/shap.md)、[可解釋 AI](../concepts/explainable-ai.md)
