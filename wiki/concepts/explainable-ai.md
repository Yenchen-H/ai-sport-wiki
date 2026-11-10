---
type: concept
title: 可解釋 AI（XAI）
sources: [zhou2025, cohan2021, majumdar2024, rahimian2025]
updated: 2026-11-10
---

# Explainable AI（XAI，可解釋 AI）

## 定義

- "Explainable AI (XAI) (Arrieta et al., 2020) aims to make AI model decisions transparent, showing which factors influence predictions and recommendations" [Zhou 2025, p.9]

## 中文說明

- White-box 模型（線性迴歸、logistic regression、kNN、決策樹）能清楚對應輸入與輸出 [Majumdar 2024, p.3]。
- Black-box 模型（集成方法、隨機森林、ANN、SVM）不易解讀但可能更強，需要事後（post-hoc）方法解釋 [Majumdar 2024, p.3]。

- Black box 模型會產生結果，卻沒有容易理解的理由 [Zhou 2025, p.8]。
- 很多運動 AI 工具沒有內建解釋機制或好用的介面 [Zhou 2025, p.8]。

## 為什麼需要 XAI

- 運動醫學：black box 降低信任，醫師不願依賴無法理解的結果 [Zhou 2025, p.6]。
- 選才：教練和球探看不懂預測理由，就難以信任 AI 建議 [Zhou 2025, p.8]。
- 傷害風險與訓練建議：XAI 能說明生物特徵或動作模式如何影響評估 [Zhou 2025, p.9]。

## 實際例子

- Cohan 2021：深度學習的 feature learning "can be an opaque process"，因此另外檢視模型的可解釋性 [Cohan 2021, p.2]。
- 做法是建立簡化的代理資料集，再用 [SHAP](shap.md) kernel explainer 解釋 [Cohan 2021, p.7]。

- Majumdar 2024：XGBoost 與 ANN 是 black-box，因此用 SHAP 呈現重要特徵 [Majumdar 2024, p.10]。

- Rahimian 2025：用可解釋的 logistic regression 建 xG，再把特徵貢獻轉成文字給教練 [Rahimian 2025, p.2]。
- Rahimian 指出 SHAP 的數值 "do not automatically translate into actionable insights for football practitioners" [Rahimian 2025, p.2]

### ⚠ 說法分歧：black-box 加事後解釋，還是一開始就用可解釋模型？

- Majumdar：black-box 模型 "can provide better predictive performance, but at the expense of being difficult to interpret and understand" [Majumdar 2024, p.10]
- Rahimian：把方法推廣到一般 ML 模型是開放問題，但 "An important question, however, is whether such an approach is really needed when a more mechanistic approach (based on logistic regression) is so effective." [Rahimian 2025, p.12]
- 兩篇的任務不同：Majumdar 是傷害預測，Rahimian 是射門品質（xG）[Majumdar 2024, p.1] [Rahimian 2025, p.1]。

## 未來方向

- 運動醫學的未來方向之一是提供 explainable and reliable 的診斷結果 [Zhou 2025, p.6]。

## 相關頁面

- [Wordalisation](wordalisation.md)、[SHAP](shap.md)、[選才](talent-identification.md)、[運動醫學](sports-medicine-ai.md)、[傷害預測](injury-prediction.md)、[倫理與隱私](ethics-privacy.md)
