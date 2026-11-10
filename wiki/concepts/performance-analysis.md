---
type: concept
title: 表現與戰術分析
sources: [zhou2025, rothe2026]
updated: 2026-11-10
---

# Performance analysis（表現與戰術分析）

## 定義

- 團隊侵入性運動（team invasion sports）被視為雙方互動的 dynamic systems [Zhou 2025, p.4]。
- 表現分析的六個主題：game actions、dynamic actions、movement patterns、collective team behaviour、social network analysis、game styles [Zhou 2025, p.4]。

## 中文說明

- AI 可以透過自動化分析、找出複雜模式、提供即時洞察來影響這六個主題 [Zhou 2025, p.4]。
- 研究焦點從單一體能指標，轉向 GPS 移動、技術執行、戰術行為等比賽資料 [Zhou 2025, p.4]。
- 但這些資料處理很耗時，常常來不及在比賽中提供即時回饋 [Zhou 2025, p.4]。

## 各來源怎麼用

- YOLO 追蹤澳式足球對手位置：17 場 2019 AFL 比賽，mAP = 0.94、F1 = 0.96 [Zhou 2025, p.4]。
- Random forest 預測足球防守成功（奪回球權）：德甲 2020–2021 位置資料，16 個特徵，accuracy = 0.82、F1 = 0.57 [Zhou 2025, p.4]。
- 這個模型找出的關鍵防守戰術是 ball pressing 和靠近球的緊密陣型 [Zhou 2025, p.4]。

- Rothe 2026：從位置資料自動偵測 9 種戰術狀態，取代人工逐秒觀察標記，詳見 [戰術狀態](tactical-states.md) [Rothe 2026, p.2]。
- 足球資料量已經很大：每場約 1,500 個事件，追蹤資料通常 25 frames per second [Rothe 2026, p.2]。

## 比較（不是分歧）

- Rahimian 提出疑問：既然 logistic regression 這種機制型模型已經很有效，用 SHAP 解釋黑箱模型的做法是否真有必要 [Rahimian 2025, p.12]。
- Rothe 則認為在少見狀態上的穩健性 "justifying the proposed methodological complexity" [Rothe 2026, p.16]
- 兩者談的「複雜度」不是同一件事：Rahimian 談解釋方法，而且是問句；Rothe 談分類表現，所以不視為說法分歧 [Rahimian 2025, p.2] [Rothe 2026, p.16]。
- Rothe 最強的 baseline 正好是 logistic regression（macro F1 0.90 vs. 0.92），優勢主要在少見狀態 [Rothe 2026, p.10]。

## 未來方向

- Digital twin：建立對手球隊的虛擬模型，模擬戰術並找出最佳對策 [Zhou 2025, p.5]。
- 分析對手的移動、技術與戰術模式，提供量身訂做的戰術建議 [Zhou 2025, p.5]。
- 即時分析的挑戰是如何和教練的情境判斷取得平衡 [Zhou 2025, p.9] [Zhou 2025, p.10]。

## 相關頁面

- [AI 在運動總覽](ai-in-sport.md)、[戰術狀態](tactical-states.md)
