---
type: concept
title: Wordalisation（把模型輸出寫成文字）
sources: [rahimian2025]
updated: 2026-11-10
---

# Wordalisation

## 定義

- "The key idea is to use large language models (LLMs) to convert numbers into natural language narratives" [Rahimian 2025, p.2]
- Rahimian 把它從「描述原始資料」延伸到「描述機器學習模型的輸出與特徵貢獻」[Rahimian 2025, p.2]。

## 中文說明

- xG（expected goals）依射門位置、角度、防守壓力等因素，估計一次射門的進球機率 [Rahimian 2025, p.1]。
- 很多 xG 模型是 black box，只給機率，不說明各特徵怎麼影響結果 [Rahimian 2025, p.1]。
- 作者強調這個系統是 model-agnostic，可以換成其他可分解或可解釋輸出的模型 [Rahimian 2025, p.2]。

## 怎麼做（四步驟 prompt）

- Tell it who it is：用 system prompt 設定角色，例如射門評論員 [Rahimian 2025, p.5]。
- Tell it what it knows：提供 43 組專家寫的問答範例 [Rahimian 2025, p.5]。
- Tell it what data to use：把 xG 和特徵貢獻轉成文字，例如用百分位分成 slim chance 到 excellent chance 五級 [Rahimian 2025, p.5]。
- 只有貢獻大於 0.1 或小於 −0.1（log-odds）的特徵才寫進描述 [Rahimian 2025, p.7]。
- Tell it how to answer：規定句數與每句內容，並提供 3 個人工撰寫的 few-shot 範例 [Rahimian 2025, p.7]。

## 評估與限制：宣稱 vs. 證據範圍

- 討論段宣稱："The resulting text is both engaging and factually correct." [Rahimian 2025, p.11]
- 但 accuracy 只評估 2 個特徵（distance to goal、vertical distance to centre）的貢獻方向，而且評分者是 LLM [Rahimian 2025, p.8] [Rahimian 2025, p.10]。
- Engagement 和 accuracy 的取捨指的是「不描述射門的所有面向」，不是寫錯事實；作者認為這是可預期的 [Rahimian 2025, p.11]。
- 完整 wordalisation 的 accuracy 第二高、engagement 最高 [Rahimian 2025, p.10]。

## 相關頁面

- [LLM 在運動](llms-in-sport.md)、[可解釋 AI](explainable-ai.md)
- [來源：Rahimian 2025](../sources/rahimian2025.md)
