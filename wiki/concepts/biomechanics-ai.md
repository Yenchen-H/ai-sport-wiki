---
type: concept
title: 生物力學中的 AI
sources: [zhou2025]
updated: 2026-11-10
---

# AI in biomechanics（生物力學）

## 定義

- "Biomechanics focuses on describing motion (kinematics) and the factors driving it (kinetics)" [Zhou 2025, p.3]

## 中文說明

- 衝刺觸地、投擲出手這類短時間動作需要高頻取樣，有時每秒超過 1000 筆 [Zhou 2025, p.3]。
- 即使技術進步，標準 3D 動作擷取仍然複雜又耗時 [Zhou 2025, p.3]。

## AI 的兩個主要貢獻

- 在實驗室以外蒐集資料 [Zhou 2025, p.3]。
- 整合不同類型資料，更準確預測傷害風險等結果 [Zhou 2025, p.3]。

## 各來源怎麼用

- 深蹲姿勢分類：22 位男性受試者，IMU＋gated LSTM transformer，判斷正確姿勢的準確率 96.3% [Zhou 2025, p.3]。
- 組織負荷估算：ANN 估算髕股關節壓力、脛骨壓力、阿基里斯腱應變，輸入來自壓力鞋墊與 3D 動作擷取 [Zhou 2025, p.3] [Zhou 2025, p.4]。
- Computer vision：用攝影機或空拍機影片，自動追蹤姿勢、關節角度與動作順序 [Zhou 2025, p.4]。

## 限制與未來方向

- "the required data inputs, such as force plate data, IMUs and 3D motion capture, limit accessibility beyond elite sports settings" [Zhou 2025, p.4]
- 需要更簡單、平價的方案，例如手機影片分析，讓一般運動者也能使用 [Zhou 2025, p.4]。
- 未來要在衝刺、跳躍等動態任務上驗證，並加入個人化資料提高準確度 [Zhou 2025, p.4]。

## 相關頁面

- [AI 在運動總覽](ai-in-sport.md)、[傷害預測](injury-prediction.md)
- [研究筆記：平價動作分析](../notes/accessible-motion-analysis.md)
