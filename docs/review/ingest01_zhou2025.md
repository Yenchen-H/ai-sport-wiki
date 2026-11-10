# AI 審查報告：ingest #1 zhou2025

- 審查者：獨立子代理（看不到與使用者的對話，只拿到 wiki/ 頁面與 raw/zhou2025.pdf），只寫報告不改檔
- 範圍：122 句帶出處的句子，逐句對照 PDF 原文
- 結果：必修 0、建議 6；所有數字（96.3%、mAP 0.94、F1 0.57、96→98% 等）皆正確

| 檔案 | 問題類型 | 說明 | 處理 |
|---|---|---|---|
| sources/zhou2025.md:20 | 頁碼 | p.2 摘要列的挑戰是隱私、倫理、組織採用，沒提即時資料可靠性 | 改寫為「資料隱私、倫理與組織採用」 |
| sources/zhou2025.md:36 | 忠實度 | 原文 "many studies"，Wiki 寫「多數」，講太強 | 改為「許多」 |
| notes/llm-evaluation-gap.md:12 | 忠實度 | 同上，研究缺口的依據被誇大 | 改為「許多」 |
| notes/accessible-motion-analysis.md:12 | 忠實度 | 原文是 "limit accessibility beyond elite settings"，Wiki 寫成「只能在菁英環境使用」 | 改為「限制了菁英環境以外的可及性」 |
| notes/talent-id-explainability.md:12 | 忠實度 | 原文 "may find it challenging to trust"，Wiki 寫成「不信任」 | 改為「可能難以信任」 |
| concepts/performance-analysis.md:31 | 頁碼 | 句子跨 p.9–p.10，只標 p.10 | 補標 p.9 |

## 觀察

- 程式檢查（lint.py）第一次就全過，但 AI 審查仍抓到 6 個語氣與頁碼問題：腳本只能檢查格式、頁碼範圍和逐字引用，**抓不到「中文改寫把語氣講太強」**。
- 6 個問題裡有 4 個是「把可能性寫成定論」（many → 多數、may → 不），而且集中在研究筆記頁，因為筆記頁是在「推論」，最容易順手加強語氣。
