---
type: note
title: 研究筆記：LLM 評估的研究缺口
sources: [zhou2025, rahimian2025]
updated: 2026-11-10
---

# LLM 評估的研究缺口

## 想法

- 運動健康領域的 LLM 研究，許多只測單一 prompt [Zhou 2025, p.7]，作者建議改成多輪、多 prompt 的評估 [Zhou 2025, p.7]。

## 依據

- [LLM 在運動](../concepts/llms-in-sport.md)

## 和使用者研究的關係

- 若研究中用 LLM 產生報告或解釋，評估方法要避免只測一次 prompt。

## 待查

- ~~後續來源中，有沒有人用 LLM 解釋運動模型的結果？~~ 已找到：Rahimian 2025 的 wordalisation [Rahimian 2025, p.2]，見 [Wordalisation](../concepts/wordalisation.md)。
- 但 Rahimian 的文字品質也是交給 LLM 評估，作者自己說下一步要請教練做人工評估 [Rahimian 2025, p.12]，所以「缺少人類專家評估」的缺口仍在。
- Rahimian 有比較 5 種 prompt 版本、跑 10 次取平均 [Rahimian 2025, p.8] [Rahimian 2025, p.10]，算是部分回應了 Zhou 提到的單一 prompt 問題。（推論）
