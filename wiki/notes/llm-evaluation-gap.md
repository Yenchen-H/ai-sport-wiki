---
type: note
title: 研究筆記：LLM 評估的研究缺口
sources: [zhou2025, rahimian2025, ferreira2026]
updated: 2026-11-10
---

# LLM 評估的研究缺口

## 想法

- 運動健康領域的 LLM 研究，許多只測單一 prompt [Zhou 2025, p.7]，作者建議改成多輪、多 prompt 的評估 [Zhou 2025, p.7]。

## 依據

- [LLM 在運動](../concepts/llms-in-sport.md)

- Ferreira 的 LLM 架構也只用模擬資料評估，作者自己說需要真實資料進一步測試 [Ferreira 2026, p.23]。缺少真實使用者與專家評估的缺口仍在。

## 和使用者研究的關係

- （推論）研究中若用 LLM 產生解釋，可參考 Ferreira 提出的降低幻覺方法：RAG 與高影響建議的人工審核 [Ferreira 2026, p.23]。

- 若研究中用 LLM 產生報告或解釋，評估方法要避免只測一次 prompt。

## 待查

- **引用 Ferreira 2026 前要自己查證**：論文寫「OpenAI's Model Context Protocol (MCP)」[Ferreira 2026, p.3]，但 MCP 的提出者可能是 Anthropic，這點來源沒有其他佐證，是 Wiki 撰寫者（Claude）的知識，需要使用者自行查證後再引用。

- ~~後續來源中，有沒有人用 LLM 解釋運動模型的結果？~~ 已找到：Rahimian 2025 的 wordalisation [Rahimian 2025, p.2]，見 [Wordalisation](../concepts/wordalisation.md)。
- 但 Rahimian 的文字品質也是交給 LLM 評估，作者自己說下一步要請教練做人工評估 [Rahimian 2025, p.12]，所以「缺少人類專家評估」的缺口仍在。
- Rahimian 有比較 5 種 prompt 版本、跑 10 次取平均 [Rahimian 2025, p.8] [Rahimian 2025, p.10]，算是部分回應了 Zhou 提到的單一 prompt 問題。（推論）
