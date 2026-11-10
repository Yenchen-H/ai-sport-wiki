---
type: concept
title: LLM 在運動中的應用
sources: [zhou2025, rahimian2025]
updated: 2026-11-10
---

# Large language models in sport（LLM 在運動）

## 定義

- NLP 是讓機器理解並回應人類語言的 AI 領域，在運動中可透過聊天機器人提供即時回饋 [Zhou 2025, p.2]。

## 各來源怎麼用

- 營養與健康：LLM 能提供建議、分析資料、產生洞察 [Zhou 2025, p.6]。
- 精準營養：有研究建立 ChatGPT-based 系統提供營養建議 [Zhou 2025, p.6]。
- 運動醫學：VICTOR 是專為運動醫學調整的 GPT 模型 [Zhou 2025, p.5]。
- 解釋模型：Rahimian 用 LLM 把 xG 模型的特徵貢獻寫成射門描述（wordalisation）[Rahimian 2025, p.2]，詳見 [Wordalisation](wordalisation.md)。
- Prompt engineering 是使用 LLM 的關鍵，好的 prompt 能提升輸出的相關性、準確度與創意 [Rahimian 2025, p.2]。
- Few-shot prompting：在 prompt 裡放人工撰寫的範例 [Rahimian 2025, p.7]。
- LLM 當評審：Rahimian 讓 Gemini 幫文字打 0–5 分的 engagement，並判斷特徵貢獻方向，結果取 10 次平均 [Rahimian 2025, p.8] [Rahimian 2025, p.10]。

## 限制

- "LLMs are very sensitive to context and prompts, with many current health monitoring studies based on a single prompt" [Zhou 2025, p.7]
- 只用單一 prompt，很難評估 LLM 在不同使用情境下的表現 [Zhou 2025, p.7]。

- Rahimian 的 model card 也提到 LLM 輸出對輸入措辭敏感 [Rahimian 2025, p.10]。

## 未來方向

- Rahimian 計畫請教練做人工評估，檢驗描述是否準確、是否有用 [Rahimian 2025, p.12]。

- "new research should focus on iterative and multi-prompt engagements with LLMs" [Zhou 2025, p.7]

## 相關頁面

- [健康監測](health-monitoring.md)
- [研究筆記：LLM 評估的研究缺口](../notes/llm-evaluation-gap.md)
