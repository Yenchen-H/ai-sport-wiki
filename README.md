# AI 在運動科學的應用：LLM Wiki

生成式人工智慧課程第十週作業。依 Karpathy 的 LLM Wiki 構想，用「先討論、後生成」建立的研究用知識庫，再以 Wiki 為唯一知識來源產生教學 HTML 簡報。

- Wiki 目錄：[wiki/index.md](wiki/index.md)
- 規則檔：[AGENTS.md](AGENTS.md)
- 需求訪談紀錄：[docs/需求訪談紀錄.md](docs/需求訪談紀錄.md)
- 原始資料（9 篇 Open Access 期刊）：[raw/README.md](raw/README.md)
- 教學簡報：[slides/ai-in-sport/](slides/ai-in-sport/index.html)（GitHub Pages：https://yenchen-h.github.io/ai-sport-wiki/slides/ai-in-sport/ ）
- 作業說明（流程圖、檢查紀錄、反思）：[docs/作業說明.md](docs/作業說明.md)
- 檢查腳本：`python3 scripts/lint.py --final`、`python3 scripts/check_slides.py <關卡> slides/ai-in-sport`

## AI 協作說明

本專案由使用者與 Claude（Anthropic）協作完成：需求、資料挑選與每次 ingest 的確認由使用者決定，頁面撰寫、檢查腳本與簡報由 Claude 依 AGENTS.md 產生。
