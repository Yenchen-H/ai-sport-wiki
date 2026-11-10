---
wiki: ../../../wiki/concepts/injury-prediction.md
---

# 證據卡：injury

> 只摘錄 wiki/concepts/injury-prediction.md，逐字複製，不改寫。

- Cohan 2021（NBA）：深度學習模型 METIC 用過去傷病、前 5 場比賽與球員資料預測 8 類傷害 [Cohan 2021, p.4]。
- Majumdar 2024（英超）：用訓練負荷預測未來 7 天的非接觸性傷害，ANN recall 77%、precision 13% [Majumdar 2024, p.8]。
- Precision 低代表很多 false alarm，可能讓球員不必要地休息；但多數真正高風險的球員也會被休息保護 [Majumdar 2024, p.8] [Majumdar 2024, p.9]。
- Cohan（NBA，SHAP）：過去傷病重要，但不在任何傷害類型的前五名 [Cohan 2021, p.7]。
- Majumdar（英超，SHAP）：last injury area 在訓練資料排第一，套到測試的三個月份也都排前二 [Majumdar 2024, p.7] [Majumdar 2024, p.8]。
- 比較時要注意三個差異：Majumdar 的 last injury area 是自建的「上次受傷部位」特徵 [Majumdar 2024, p.3]；Majumdar 只看非接觸性傷害 [Majumdar 2024, p.3]，Cohan 包含接觸性傷害 [Cohan 2021, p.3]；兩篇是不同運動。
