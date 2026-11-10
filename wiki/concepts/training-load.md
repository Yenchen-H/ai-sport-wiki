---
type: concept
title: 訓練負荷（ACWR、EWMA）
sources: [majumdar2024]
updated: 2026-11-10
---

# Training load（訓練負荷）

## 定義

- 監測選手在訓練與比賽中的負荷，對判斷訓練適應、評估疲勞恢復、降低受傷風險很重要 [Majumdar 2024, p.1] [Majumdar 2024, p.2]。
- ACWR（Acute Chronic Workload Ratio）是 "the most popular and well-researched model of the injury process" [Majumdar 2024, p.2]

### ⚠ 說法分歧：ACWR 本身有沒有效？

- 一方：ACWR 是最受歡迎、研究最多的傷害模型 [Majumdar 2024, p.2]。
- 另一方："there have been recent methodological and theoretical criticisms of ACWR" [Majumdar 2024, p.2]
- 被引用的批評文獻標題是 "Time to Dismiss ACWR" [Majumdar 2024, p.13]

## 中文說明

- Majumdar 使用的負荷類型：GPS、體能（皮脂、體脂率）、心理（RPE）與個人資料 [Majumdar 2024, p.3]。
- 除了 ACWR，也計算 MSWR 和 EWMA（指數加權移動平均）[Majumdar 2024, p.4]。
- 計算時用的是「過去 7 天」的訓練，不是「過去 7 次」訓練，兩者可能不同 [Majumdar 2024, p.4]。
- 機器學習可以從 ACWR 這類簡化模型，擴展到同時考慮多種生理與心理負荷 [Majumdar 2024, p.2]。

### ⚠ 說法分歧：ACWR 多少算危險？

- Hulin（板球）：最佳範圍 0.85–1.5，超過 1.5 受傷風險增加 2–4 倍 [Majumdar 2024, p.2]。
- Bowen（英超）：慢性負荷低時 ACWR 超過 2，風險增加 5–7 倍 [Majumdar 2024, p.2]。
- Rossi（義大利職業足球）：沒有任何訓練超過 2，最高風險出現在 ACWR 小於 1 [Majumdar 2024, p.2]。因為資料中沒有大於 2 的情況，Rossi 其實無法檢驗 Bowen 的門檻。
- Majumdar 自己的資料：多數傷害發生在 ACWR 0.5–1.5 之間，作者說這 "appeared to differ" 於既有文獻 [Majumdar 2024, p.11]。
- 比較基準不同：Hulin、Bowen、Rossi 講的是風險倍數，Majumdar 講的是傷害次數的分布，沒有考慮各區間的暴露量 [Majumdar 2024, p.2] [Majumdar 2024, p.11]。
- 以上都是 Majumdar 轉述的文獻，原始研究不在本 Wiki 中 [Majumdar 2024, p.2]。

## 相關頁面

- [傷害預測](injury-prediction.md)
