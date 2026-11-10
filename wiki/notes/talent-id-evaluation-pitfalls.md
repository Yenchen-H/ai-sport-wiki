---
type: note
title: 研究筆記：選才模型的評估陷阱
sources: [cohan2021, majumdar2024]
updated: 2026-11-10
---

# 選才模型的評估陷阱

## 想法

- 傷害預測的資料極度不平衡，只看 accuracy 會被「永遠猜多數類」的模型騙到 [Cohan 2021, p.6]。
- 選才也有類似結構：真正進入菁英層級的選手是少數，這點來源沒有討論，是本筆記的推論（待查）。

## 依據

- [不平衡資料與評估指標](../concepts/class-imbalance-metrics.md)

## 和使用者研究的關係

- 選才研究用 Random Forest 時，除了 accuracy，應同時報告 ROC AUC、average precision、recall。
- 要明確切分訓練與驗證資料，只報驗證集的結果，避免 Cohan 批評的「用同一份資料訓練和評估」[Cohan 2021, p.4]。

- 時間切分：Majumdar 用前 4.5 季訓練、後半季測試 [Majumdar 2024, p.4]。（推論）選才研究可考慮「用前幾屆選手建模、後一屆選手測試」，而且測試資料不能拿來調參數（Majumdar 這點做得不夠乾淨，見 [模型驗證方式](../concepts/model-validation.md)）。
- 換一個情境最佳模型就可能不同 [Majumdar 2024, p.12]。（推論）選才模型推廣到別的運動或年齡層時，要重新驗證。

## 待查

- 選才資料的類別比例實際有多不平衡？
