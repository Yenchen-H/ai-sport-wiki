---
type: concept
title: 傷害預測
sources: [zhou2025, cohan2021, majumdar2024]
updated: 2026-11-10
---

# Injury prediction（傷害預測）

## 定義

- Machine learning 在運動中的核心角色之一是 "predicting injury risks" [Zhou 2025, p.2]。

## 中文說明

- 綜述層級：AI 被用來估算走路、跑步時膝與髖的傷害風險 [Zhou 2025, p.3]。
- 生物力學資料整合後，可以更準確預測傷害風險等重要結果 [Zhou 2025, p.3]。
- 穿戴裝置的即時資料可支援負荷管理與傷害預防，前提是資料蒐集流程標準化、感測器可靠 [Zhou 2025, p.9]。

## 各來源怎麼用

- Zhou 2025（綜述）：ANN 估算常見受傷部位的組織負荷，例如脛骨壓力與阿基里斯腱應變 [Zhou 2025, p.3]。
- Cohan 2021（NBA）：深度學習模型 METIC 用過去傷病、前 5 場比賽與球員資料預測 8 類傷害 [Cohan 2021, p.4]。
- METIC 的 ROC AUC 0.80、F1 0.020，F1 是第二名模型的兩倍以上 [Cohan 2021, p.6] [Cohan 2021, p.7]。
- 依傷害類型，背部傷害最好預測（ROC AUC 0.87），接觸性與上半身傷害最低（皆為 ROC AUC 0.74）[Cohan 2021, p.7]。
- Majumdar 2024（英超）：用訓練負荷預測未來 7 天的非接觸性傷害，ANN recall 77%、precision 13% [Majumdar 2024, p.8]。
- Precision 低代表很多 false alarm，可能讓球員不必要地休息；但多數真正高風險的球員也會被休息保護 [Majumdar 2024, p.8] [Majumdar 2024, p.9]。

### ⚠ 說法分歧：誰是「第一個」？

- Majumdar 摘要：自稱 "the first study of its kind to use Artificial Neural Network and a multi-season dataset for injury prediction" [Majumdar 2024, p.1]
- 但 Cohan 2021 已用深度學習（Transformer）處理 2010–20 年多球季的 NBA 傷害資料 [Cohan 2021, p.2] [Cohan 2021, p.4]。
- Majumdar 內文的說法範圍比較窄：ANN "has never been used for soccer injury prediction" [Majumdar 2024, p.9]

## 風險因子

- 近 5 場上場超過 100 分鐘，會提高所有傷害的發生率，特別是肌肉與挫傷 [Cohan 2021, p.4]。

### ⚠ 說法分歧：過去傷病重不重要？（同一來源內部）

- 單因子分析：作者說 "previous injury was a meaningful indicator of future injury" [Cohan 2021, p.4]
- 模型解釋（SHAP）：作者先說結果 "corroborate the literature in showing previous injuries to be important factors for predicting future injuries of any type" [Cohan 2021, p.7]
- 接著說它們 "are not in the top-five factors found by our model for any type of injuries examined here" [Cohan 2021, p.7]
- 兩者分析方法不同：前者是探索性的單因子分析，不是模型推導出來的 [Cohan 2021, p.4]。

### ⚠ 說法分歧：過去傷病重不重要？（跨來源）

- Cohan（NBA，SHAP）：過去傷病重要，但不在任何傷害類型的前五名 [Cohan 2021, p.7]。
- Majumdar（英超，SHAP）：last injury area 在訓練資料排第一，套到測試的三個月份也都排前二 [Majumdar 2024, p.7] [Majumdar 2024, p.8]。
- 比較時要注意三個差異：Majumdar 的 last injury area 是自建的「上次受傷部位」特徵 [Majumdar 2024, p.3]；Majumdar 只看非接觸性傷害 [Majumdar 2024, p.3]，Cohan 包含接觸性傷害 [Cohan 2021, p.3]；兩篇是不同運動。

### ⚠ 說法分歧：身高等基本資料的角色（同一來源內部）

- 單因子分析：身高 "may influence risk of back and ligament injuries" [Cohan 2021, p.4]
- 結論處：年齡、比賽地點、身高、體重的單因子風險 "are relatively low" [Cohan 2021, p.10]
- 但這些變數在模型中很重要，作者認為代表變數間是非線性、多因子的關係 [Cohan 2021, p.10]。

## 資料與評估

- 傷害資料極度不平衡，評估時不能只看 accuracy，詳見 [不平衡資料與評估指標](class-imbalance-metrics.md) [Cohan 2021, p.6]。
- 公開資料的限制：沒有 GPS 活動量、主觀健康、睡眠等生物特徵資料 [Cohan 2021, p.3]。
- 未來可整合光學追蹤等生物力學資料 [Cohan 2021, p.10]。

## 風險與倫理

- 傷害風險預測這類生物特徵資料，可能被球隊或贊助商拿來排除選手，即使沒有臨床症狀或選手同意 [Zhou 2025, p.9]。
- XAI 可以說明哪些指標影響傷害風險評估，幫助選手和教練做出可信的決定 [Zhou 2025, p.9]。

## 相關頁面

- [來源：Cohan 2021](../sources/cohan2021.md)、[SHAP](shap.md)、[生物力學](biomechanics-ai.md)、[運動醫學](sports-medicine-ai.md)、[可解釋 AI](explainable-ai.md)、[倫理與隱私](ethics-privacy.md)
