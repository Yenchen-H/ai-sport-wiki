---
type: concept
title: SHAP（Shapley 值解釋）
sources: [cohan2021, majumdar2024, rahimian2025]
updated: 2026-11-10
---

# SHAP（SHapley Additive exPlanations）

## 定義

- "The Shapely values represent feature importance for particular data points considering perturbations around the data" [Cohan 2021, p.7]

## 中文說明

- SHAP 是基於賽局理論的可解釋性框架，計算每個特徵對預測的貢獻 [Majumdar 2024, p.3]。

- Cohan 用 SHAP 同時考慮多個交互作用的因子並給出重要性排序，對比許多只看單一因子統計顯著性的研究 [Cohan 2021, p.7]。

## 各來源怎麼用

- Cohan 2021：為了讓特徵空間更容易解讀，先建一個 proxy dataset（用次數、最大值、最小值彙整），再用 SHAP kernel explainer 計算 [Cohan 2021, p.7]。
- 這個資料集對應 Table 1 的 Explainer Model，輸入特徵比 METIC 少 [Cohan 2021, p.6]。
- 內文寫：挫傷（contusion）次數對上半身、肌肉等多種傷害都很重要 [Cohan 2021, p.7]。

- Majumdar 2024：在訓練與驗證資料中，ANN 的 SHAP 前五名 "appear to be" last injury area、EWMA of meta energy、weight、meta energy、age [Majumdar 2024, p.7]。
- 同一個 ANN 套到測試的三個月份，last injury area 和 weight 都是前二 [Majumdar 2024, p.7] [Majumdar 2024, p.8]。

- Rahimian 2025（轉述）：Anzer 與 Bauer 用 SHAP 解釋 xG 模型，發現射門距離是影響進球機率最大的因素 [Rahimian 2025, p.2]。
- Rahimian 認為他們的 wordalisation 是對這種 SHAP 特徵重要性做法的改進 [Rahimian 2025, p.11]。

### ⚠ 說法分歧：挫傷次數到底重不重要？（同一來源內部，文字 vs. 圖）

- 內文：the number of contusion injuries "was found to be important for many of the injury types such as upper body and muscle injuries" [Cohan 2021, p.7]
- Fig. 7：Upper Body 與 Muscle 的圖中，Number of Contusion Injuries 都排在列出特徵的最後一名，前五名是 Age、Location、Height、Weight、Total Minutes in Last 5 Games [Cohan 2021, p.9]。

## 限制

- SHAP 只給數值，不會自動變成教練可用的建議 [Rahimian 2025, p.2]。

- "despite the power of SHAP explanations, the output from such global explanations can sometimes be misleading" [Majumdar 2024, p.10]
- 例子：EWMA of meta energy 在訓練資料排前三，但在測試月份中不重要，因為訓練資料中多數傷害發生在 EWMA 超過 6.14 時，測試資料卻沒有任何點超過 6.14 [Majumdar 2024, p.10] [Majumdar 2024, p.11]。

### ⚠ 說法分歧：SHAP 解釋的是哪個模型？（同一來源內部）

- 方法段：SHAP 是用 proxy dataset 和 Table 1 的 Explainer Model 計算 [Cohan 2021, p.6] [Cohan 2021, p.7]。
- Table 1 標題把它稱為 "METIC model and METIC explainability model input features"，表示作者把它定位成解釋 METIC 的模型 [Cohan 2021, p.6]
- 結論段：卻寫 "METIC found these factors to be highly important" [Cohan 2021, p.10]
- 論文沒有說清楚兩者的關係；「解釋的是代理模型而非 METIC 本身」是本 Wiki 的推論，見研究筆記 [選才 × 可解釋性](../notes/talent-id-explainability.md) [Cohan 2021, p.7]。

## 相關頁面

- [可解釋 AI](explainable-ai.md)、[傷害預測](injury-prediction.md)
