---
wiki: ../../../wiki/concepts/class-imbalance-metrics.md
---

# 證據卡：imbalance

> 只摘錄 wiki/concepts/class-imbalance-metrics.md，逐字複製，不改寫。

- 一直猜多數類就能拿到很高的 accuracy：No Injury 模型 accuracy 99.8%，卻完全沒用 [Cohan 2021, p.6]。
- 比較適合的指標是 ROC AUC 和 average precision [Cohan 2021, p.6]。
- 不平衡資料：某一類（例如「受傷」）佔比極低。Cohan 的 NBA 資料中，受傷不到 4% [Cohan 2021, p.3]。
