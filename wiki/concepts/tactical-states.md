---
type: concept
title: 戰術狀態與自動偵測
sources: [rothe2026]
updated: 2026-11-10
---

# Tactical states（戰術狀態）

## 定義

- State-transition model 需要一套狀態類別系統，讓每個比賽情境都能對應到唯一一個狀態 [Rothe 2026, p.1]。
- 和只看單一表現指標的統計方法相比，state-transition models 保留了比賽的動態與互動特性 [Rothe 2026, p.2]。

## 中文說明

- 現有足球狀態系統多半只有少數抽象狀態，或只看控球與球的位置，戰術資訊有限 [Rothe 2026, p.1]。
- 戰術階段（phases of play）在學術上沒有一致定義 [Rothe 2026, p.3]。
- Rothe 的狀態系統：持球方有 build-up、progression、attacking play、counter/fast attack；防守方有 high、mid、low block [Rothe 2026, p.3]。
- 作者也承認這套系統仍然很抽象，例如沒有描述哪些位置的球員在各區 [Rothe 2026, p.11]。

## 自動偵測的做法

- 位置組態用 5-tuple 表示，再分群；每群以專家規則的多數決決定戰術狀態，形成翻譯表 [Rothe 2026, p.6] [Rothe 2026, p.7] [Rothe 2026, p.8]。
- 分群讓方法對組態的小變化比較穩健，純規則法則不行 [Rothe 2026, p.16]。
- 用 L1 距離加上轉換後的 tuple，分群品質（silhouette score）最好 [Rothe 2026, p.14] [Rothe 2026, p.16]。

## 相關頁面

- [表現與戰術分析](performance-analysis.md)
- [研究筆記：專家知識 × 機器學習](../notes/expert-knowledge-ml-hybrid.md)
