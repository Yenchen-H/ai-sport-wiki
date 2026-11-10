# Wiki 紀錄（只往下加）

## 2026-11-10 建立 Wiki
- 完成 9 題需求訪談並由使用者確認需求摘要（見 docs/需求訪談紀錄.md）
- 主題由「AI Agents 入門」改為「AI 在運動科學的應用」：使用者提供的 5 篇期刊都是運動科學 AI 應用
- 建立 AGENTS.md、CLAUDE.md（@AGENTS.md）、資料夾結構、scripts/lint.py
- raw/ 放入 5 篇 PDF：zhou2025、cohan2021、majumdar2024、rahimian2025、rothe2026
- 預定 ingest 順序：zhou2025（綜述，先建架構）→ cohan2021 → majumdar2024 → rahimian2025 → rothe2026

## 2026-11-10 ingest #1：zhou2025（綜述）
- 確認清單經使用者同意（10 概念頁＋3 研究筆記）
- 新增：sources/zhou2025.md；concepts/ ai-in-sport、biomechanics-ai、performance-analysis、injury-prediction、sports-medicine-ai、health-monitoring、talent-identification、explainable-ai、ethics-privacy、llms-in-sport；notes/ talent-id-explainability、accessible-motion-analysis、llm-evaluation-gap
- 撰寫時自我修正 1 處：來源頁「限制」原本寫了來源沒提到的推論（綜述沒說明檢索方法），違反 AGENTS.md §3-4，刪除改用原文
- lint.py：第 1 輪全過（14 頁，警告：來源 1/5）
- AI 審查（獨立子代理）：122 句，必修 0、建議 6 → 全部修正（報告：docs/review/ingest01_zhou2025.md）
- 修正後 lint.py：全過

## 2026-11-10 ingest #2：cohan2021（NBA 傷害預測）
- 確認清單經使用者同意
- 新增：sources/cohan2021.md；concepts/ class-imbalance-metrics、shap；notes/ talent-id-evaluation-pitfalls
- 更新：concepts/ injury-prediction、explainable-ai；notes/ talent-id-explainability（上一輪的「待查」已解決）
- lint.py 第 1 輪：全過
- AI 審查（獨立子代理）：47 句，必修 2、建議 5 → 全部修正（docs/review/ingest02_cohan2021.md）
- 規則調整：同一來源內部的矛盾也要標「⚠ 說法分歧」（AGENTS.md §3-3、lint.py 第 9 項）
- 修正後 lint 第 1 輪：1 錯（連結文字含 ⚠ 被誤判）→ 第 2 輪全過

## 2026-11-10 ingest #3：majumdar2024（英超訓練負荷與傷害）
- 確認清單經使用者同意；這一輪起，確認清單先列出預期的說法分歧（檢查往前移）
- 新增：sources/majumdar2024.md；concepts/ training-load、model-validation
- 更新：concepts/ injury-prediction、class-imbalance-metrics、shap、explainable-ai；notes/ talent-id-evaluation-pitfalls、talent-id-explainability
- lint.py 第 1 輪：1 錯（分歧檢查誤套到 log.md）→ 修 lint，全過
- AI 審查（獨立子代理）：90 句，必修 3、建議 15 → 全部修正（docs/review/ingest03_majumdar2024.md）
- 修正後 lint：第 1 輪 3 錯（跨頁引用、概念頁推論沒出處、參考文獻頁碼）→ 第 2 輪全過；另修 lint 跨頁範圍 bug

## 2026-11-10 ingest #4：rahimian2025（xG＋LLM wordalisation）
- 確認清單經使用者同意（先列 3 個預期分歧）；這一輪起採精簡模式：AI 審查只修必修
- 新增：sources/rahimian2025.md；concepts/wordalisation
- 更新：concepts/ llms-in-sport、explainable-ai、shap；notes/ llm-evaluation-gap（待查已解決）、talent-id-explainability
- lint.py 第 1 輪：全過
- AI 審查：48 句，必修 2、建議 3 → 修必修 2 個，建議只記錄（docs/review/ingest04_rahimian2025.md）
- 必修之一是 ingest #3 留下的結構錯置（句子被接在 ⚠ 段落底下）
- 修正後 lint：全過

## 2026-11-10 ingest #5：rothe2026（足球戰術狀態自動偵測）
- 確認清單經使用者同意
- 寫入前自我修正：確認清單預告的「clearly outperforms」分歧，對照表格後發現不矛盾，沒有標 ⚠
- 新增：sources/rothe2026.md；concepts/tactical-states；notes/expert-knowledge-ml-hybrid
- 更新：concepts/ performance-analysis、model-validation、class-imbalance-metrics
- lint.py --final 第 1 輪：全過（26 頁、5 篇來源）
- AI 審查（精簡）：40 句，必修 3、建議 3 → 修必修（docs/review/ingest05_rothe2026.md）
- 修正後 lint --final：全過
- **5 篇 ingest 完成**

## 2026-11-10 簡報 graph：AI 在運動科學能做什麼？（①–④）
- 新增 scripts/check_slides.py（coverage／cards／outline／drafts／render 五個關卡）
- ① 檢索：sources.md 列 14 個概念頁（不用研究筆記頁）
- ② 覆蓋率關卡：通過（14 頁 ≥ 3）
- ③ 證據卡：16 張，用腳本逐字摘錄；第 1 次執行失敗（把標題當成句子挑選）→ 修正；check_slides 路徑解析錯誤 → 修正；第 2 次通過
- ④ 大綱：14 張，check_slides outline 通過
- ⑤ 等待使用者確認大綱

## 2026-11-10 簡報 graph（⑤–⑩）
- ⑤ 使用者確認大綱
- ⑥ 逐頁稿 14 頁：check_slides drafts 通過；送審前自我修正 2 頁
- ⑦ 忠實度檢查（獨立子代理）：第 1 輪退回 4 頁 → 其中 2 頁退回 ③ 補 4 句證據卡 → 只重寫 4 頁 → 第 2 輪全過
- ⑧ render_slides.py 輸出 index.html
- ⑨ 渲染檢查：第 1 次腳本 bug（封面沒算到）→ 修正後通過，14 張無溢出，截圖存 screenshots/
- ⑩ 交件報告：slides/ai-in-sport/report.md
