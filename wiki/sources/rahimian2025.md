---
type: source
title: Rahimian et al. (2025) 用文字自動解釋足球機器學習模型
sources: [rahimian2025]
updated: 2026-11-10
---

# Rahimian et al. (2025) Automated explanation of machine learning models of footballing actions in words

## 書目

- Rahimian, P., Flisar, J., & Sumpter, D. (2025). *Journal of Sports Analytics, 11*, 1–14. DOI: 10.1177/22150218251353089
- 授權：CC BY 4.0
- 頁碼對照：**PDF 頁碼 = 期刊頁碼**（共 14 頁，p.13 起是參考文獻）
- 原檔：[raw/rahimian2025.pdf](../../raw/rahimian2025.pdf)

## 一句話摘要

- 用 logistic regression 建 xG 模型，把每個特徵的貢獻寫成句子，再交給 LLM 寫成教練看得懂的射門描述，稱為 wordalisation [Rahimian 2025, p.1]。

## 研究問題

- 作者認為 "there remains a communication gap between machine learning practice and how coaching staff talk about football" [Rahimian 2025, p.1]
- 目標不是做出更準的 xG 模型，而是讓非技術使用者看得懂模型輸出 [Rahimian 2025, p.2]。

## 方法

- 資料：StatsBomb 事件與 360 資料，6 個賽事（EURO 2024／2022、NWSL 2018、FIFA 2022、FAWSL、AFCON 2023），只取 open-play、非頭球的射門 [Rahimian 2025, p.2]。
- 每個賽事各自訓練一個 logistic regression xG 模型，用同一組特徵 [Rahimian 2025, p.3] [Rahimian 2025, p.4]。
- 特徵貢獻 = 係數 × 平均中心化後的特徵值，代表這次射門和其他射門相比哪裡不尋常 [Rahimian 2025, p.4] [Rahimian 2025, p.5]。
- 四步驟 prompt：Tell it who it is、Tell it what it knows、Tell it what data to use、Tell it how to answer [Rahimian 2025, p.5]。
- 評估：用 LLM（Gemini）幫 5 種文字版本打 engagement 分數，並判斷特徵貢獻方向是否正確 [Rahimian 2025, p.8] [Rahimian 2025, p.9]。

### ⚠ 說法分歧：特徵篩選前後不一（同一來源內部）

- 篩選步驟：goalkeeper distance to goal 和 angle to the nearest opponent 的 p 值大於 0.05，"so we dropped them from the model" [Rahimian 2025, p.4]
- 最終特徵清單：卻仍包含 goalkeeper distance to goal [Rahimian 2025, p.4]。
- 作者另外說明，有些 p 值大於 0.05 的特徵會因為可解釋性而保留，但舉的例子是 throw in 和 nearby opponents [Rahimian 2025, p.4]。

## 主要發現

- xG 模型在 6 個賽事的 ROC 為 76%–84%，Brier score 0.05–0.09 [Rahimian 2025, p.4]。
- Engagement 和 accuracy 之間有取捨：只列描述與貢獻的 Case 2 accuracy 最高但 engagement 低 [Rahimian 2025, p.10]。
- 完整 wordalisation（Case 4）accuracy 第二高、engagement 最高，作者認為最適合實務 [Rahimian 2025, p.10]。
- 同樣方法也能用在傳球、帶球與防守動作（expected threat 模型）[Rahimian 2025, p.10] [Rahimian 2025, p.11]。

## 限制

- 文字品質目前由 LLM 評估，作者計畫之後請教練做人工評估 [Rahimian 2025, p.12]。
- Model card 列出 LLM 輸出的限制：對輸入措辭敏感、缺乏領域知識基礎 [Rahimian 2025, p.10]。
- ±0.1 log-odds 的門檻是 "somewhat heuristic" [Rahimian 2025, p.7]

## 相關頁面

- [Wordalisation](../concepts/wordalisation.md)、[LLM 在運動](../concepts/llms-in-sport.md)、[可解釋 AI](../concepts/explainable-ai.md)、[SHAP](../concepts/shap.md)
