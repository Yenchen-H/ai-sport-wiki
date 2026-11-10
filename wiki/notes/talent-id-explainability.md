---
type: note
title: 研究筆記：選才 × 可解釋性
sources: [zhou2025, cohan2021, majumdar2024, rahimian2025]
updated: 2026-11-10
---

# 選才 × 可解釋性

## 想法

- 綜述指出教練和球探看不懂預測理由時，可能難以信任 AI 建議 [Zhou 2025, p.8]，這可以直接當作「選才模型需要可解釋性」的研究動機。

## 依據

- [選才](../concepts/talent-identification.md)、[可解釋 AI](../concepts/explainable-ai.md)

## 和使用者研究的關係

- 使用者的 FAHP＋Random Forest＋SHAP 選才研究，正好回應「選才 AI 缺乏解釋機制」這個問題。
- 綜述也提到選手進步後模型要重新校正 [Zhou 2025, p.8]，可以思考指標權重是否需要定期更新。

- SHAP 整體解釋可能誤導：訓練資料中重要的特徵，在新資料裡不一定重要 [Majumdar 2024, p.10]。（推論）選才研究可在限制段討論這點，或同時報告測試資料的 SHAP 結果。

- Wordalisation 可以把特徵貢獻轉成教練看得懂的文字 [Rahimian 2025, p.2]。（推論）選才模型的權重或 SHAP 結果，也可以用四步驟 prompt 寫成給教練的選手評語；使用者動作分析研究架構中的 LLM 環節可參考這個做法與評估方式。

## 待查

- ~~後續來源中，有沒有實際把 SHAP 用在運動資料上的例子？~~ 已找到：Cohan 2021 用 SHAP kernel explainer 解釋 NBA 傷害模型 [Cohan 2021, p.7]，見 [SHAP](../concepts/shap.md)。
- Cohan 用 proxy dataset 和 Explainer Model 計算 SHAP [Cohan 2021, p.6] [Cohan 2021, p.7]，結論卻把結果歸給 METIC [Cohan 2021, p.10]。（推論）SHAP 解釋的可能是代理模型，選才研究若用 SHAP，要寫清楚解釋的是哪一個模型。
