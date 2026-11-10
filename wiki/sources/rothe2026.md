---
type: source
title: Rothe et al. (2026) 用球員與球的位置自動偵測足球戰術狀態
sources: [rothe2026]
updated: 2026-11-10
---

# Rothe et al. (2026) Automatic detection of tactical states in football based on player and ball position

## 書目

- Rothe, F., Van Roy, M., Pinheiro, G., Davis, J., & Lames, M. (2026). *Journal of Sports Analytics, 12*, 1–25. DOI: 10.1177/22150218261432789
- 授權：CC BY 4.0
- 頁碼對照：**PDF 頁碼 = 期刊頁碼**（共 25 頁，p.17 起是參考文獻）
- 原檔：[raw/rothe2026.pdf](../../raw/rothe2026.pdf)
- 原始資料由 KINEXON Sports & Media 提供，不能再散布 [Rothe 2026, p.17]。

## 一句話摘要

- 先由專家定義足球戰術狀態，再用球員位置分群與「翻譯表」從位置資料自動偵測這些狀態 [Rothe 2026, p.1]。

## 研究問題

- 在比賽中辨識戰術狀態目前要靠人工觀察影片，主觀、耗時，而且需要專家知識 [Rothe 2026, p.2]。
- 兩個目標：建立手工的專家狀態系統，以及從位置資料自動偵測狀態的機器學習方法 [Rothe 2026, p.2]。

## 方法

- 9 種戰術狀態，大多數同時描述持球方與防守方，例如 Vertical Build-up vs. Mid-Block [Rothe 2026, p.4] [Rothe 2026, p.5] [Rothe 2026, p.6]。
- 例外是 Counter/Fast Attack，它的定義不分防守方的 block 類型 [Rothe 2026, p.11]。
- 場地分成 5 個球員區域（DefBox 到 OffBox）與 15 個球的區域 [Rothe 2026, p.3] [Rothe 2026, p.4]。
- 每秒把雙方在 5 個區域的人數記成一對 5-tuple [Rothe 2026, p.6]。
- 每個球區用 KMedoids（L1 距離）分群，群數用 elbow method 決定 [Rothe 2026, p.7]。
- 用專家規則替每群的組態貼標籤，以多數決建立「translation table」，新比賽查最近的群即可判斷狀態 [Rothe 2026, p.7] [Rothe 2026, p.8]。
- 資料：2021/2022 德甲 15 場（Tracab 25 Hz），3 場訓練、12 場測試，測試集刻意包含訓練時沒出現的球隊 [Rothe 2026, p.6]。
- 評估：訓練有素的觀察者逐秒標記測試比賽，容許 ±2 秒誤差，計算 precision、recall、F1 [Rothe 2026, p.8]。
- 和 3 個 baseline 比較：LOGREG-TUPLE、LOGREG-RAW、RULE-BASED [Rothe 2026, p.8]。

## 主要發現

- 各戰術狀態的 F1 介於 0.76–0.96 [Rothe 2026, p.10]。
- 最少見的兩個狀態最弱：Counter Build-up vs. High-Block（0.76）與 Counter/Fast Attack（0.84）[Rothe 2026, p.10]。
- 平均 macro F1：提出的方法 0.92、LOGREG-TUPLE 0.90、LOGREG-RAW 0.84、RULE-BASED 0.79 [Rothe 2026, p.10]。
- LOGREG-TUPLE 是 "a strong contender"，但在兩個最少見的狀態上，提出的方法較好 [Rothe 2026, p.10]。
- 位置轉成區域與 tuple、分群步驟，都比直接用原始座標或純規則更好 [Rothe 2026, p.16]。

## 限制

- 只測試了 2021/2022 德甲 12 場，其他球季與聯賽的適用性還沒驗證 [Rothe 2026, p.16]。
- 固定的區域邊界：少數球員在邊界附近移動，就可能讓判斷的狀態改變 [Rothe 2026, p.12]。
- 5-tuple 無法推得球員間距離與陣型緊密度 [Rothe 2026, p.12]。
- 反擊類狀態只靠位置組態很難偵測，作者建議加入球速 [Rothe 2026, p.16]。

## 相關頁面

- [戰術狀態](../concepts/tactical-states.md)、[表現與戰術分析](../concepts/performance-analysis.md)、[模型驗證方式](../concepts/model-validation.md)
