---
type: source
title: Ferreira & Gonçalves (2026) 區塊鏈加 MCP：LLM 運動分析的信任與同意
sources: [ferreira2026]
updated: 2026-11-11
---

# Ferreira & Gonçalves (2026) Blockchain-enabled Model Context Protocol (MCP) for trust and consent in LLM-orchestrated sports analytics

## 書目

- Ferreira, J. C., & Gonçalves, F. (2026). *Journal of Sports Analytics, 12*, 1–26. DOI: 10.1177/22150218261448184
- 授權：CC BY 4.0
- 頁碼對照：**PDF 頁碼 = 期刊頁碼**（共 26 頁，p.24 起是參考文獻）
- 原檔：[raw/ferreira2026.pdf](../../raw/ferreira2026.pdf)

## 一句話摘要

- "The Model Context Protocol (MCP) enables large language models to query and synthesize sports data across distributed sources, yet it lacks built-in mechanisms for provenance, integrity, and athlete-controlled access." [Ferreira 2026, p.1]
- 作者提出 MCP 加區塊鏈的混合架構，用於自行微調的運動領域模型 LLM4Sports [Ferreira 2026, p.1]。

## 研究問題

- RQ1：區塊鏈錨定 MCP 查詢與資料包雜湊值，能否提供不可竄改的資料溯源與完整性驗證 [Ferreira 2026, p.3]。
- RQ2：智慧合約與可驗證憑證能否在自然語言 LLM 流程中，做到細分、有時效、由選手控制的同意 [Ferreira 2026, p.3]。
- RQ3：混合架構的實際負擔（驗證正確率、延遲、對帳時間）有多大 [Ferreira 2026, p.3]。

## 方法

- 作者明確定位為 proof-of-concept 架構與模擬資料評估，大規模部署與實地試驗只是未來願景 [Ferreira 2026, p.3]。
- 依 PRISMA 做文獻回顧：45 筆紀錄，納入 12 篇 [Ferreira 2026, p.3]。
- 模擬資料用 Monte Carlo 產生，參數參考運動文獻（例如心率 140–180 bpm）[Ferreira 2026, p.15]。
- Baseline：沒有區塊鏈的 MCP，以及集中式紀錄加角色權限控管；每項指標跑 30 次並報告 95% 信賴區間 [Ferreira 2026, p.15]。

## 主要發現

- 模擬資料上的驗證正確率 95–97% [Ferreira 2026, p.23]。
- 作者提出的應用情境包含反禁藥稽核、粉絲互動、傷害預防、選才 [Ferreira 2026, p.11] [Ferreira 2026, p.23]。

### ⚠ 說法分歧：是否符合 GDPR？（同一來源內部）

- 摘要：框架能提升 "regulatory compliance (e.g., GDPR)" [Ferreira 2026, p.1]
- 內文：完整的法律合規還需要組織措施，並說明 "All references to “GDPR compliance” have been rephrased as “enhanced support for regulatory alignment”." [Ferreira 2026, p.11]

### ⚠ 說法分歧：證明了實際可行嗎？（同一來源內部）

- 結論：架構與案例 "demonstrate practical feasibility and real-world applicability" [Ferreira 2026, p.23]
- 同一段結論又說評估都是模擬資料，需要用真實的表現與生物特徵資料進一步測試 [Ferreira 2026, p.23]。

## 限制

- 模擬工作負載可能低估不同球隊與聯賽之間的實際差異 [Ferreira 2026, p.9]。
- 混合區塊鏈在交易量與節點數增加時，有吞吐量與延遲的限制 [Ferreira 2026, p.23]。
- 中小型運動組織可能負擔不起初期導入成本 [Ferreira 2026, p.23]。

## 相關頁面

- [選手同意與資料溯源](../concepts/athlete-consent-provenance.md)、[倫理與隱私](../concepts/ethics-privacy.md)、[LLM 在運動](../concepts/llms-in-sport.md)
- [研究筆記：LLM 評估的研究缺口](../notes/llm-evaluation-gap.md)
