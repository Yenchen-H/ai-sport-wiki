# AI 在運動科學的應用：Wiki 目錄

> 由 AI 依 [AGENTS.md](../AGENTS.md) 維護。每次 ingest 後更新。出處格式 `[作者 年份, p.PDF頁碼]`。

## 來源頁（9）

| 來源 | 一句話 |
|---|---|
| [Zhou 2025](sources/zhou2025.md) | 綜述：AI 在運動的五大應用、挑戰與未來趨勢 |
| [Cohan 2021](sources/cohan2021.md) | NBA 傷害預測：Transformer 模型 METIC＋SHAP |
| [Majumdar 2024](sources/majumdar2024.md) | 英超訓練負荷與傷害：XGBoost／ANN＋SHAP，多球季 |
| [Rahimian 2025](sources/rahimian2025.md) | xG 模型＋LLM，把模型輸出寫成教練看得懂的文字 |
| [Rothe 2026](sources/rothe2026.md) | 用位置資料分群，自動偵測足球戰術狀態 |
| [Buhamra 2025](sources/buhamra2025.md) | 網球大滿貫：ML 與迴歸、三種預測策略比較 |
| [Goel 2021](sources/goel2021.md) | 板球 IPL：第二局逐球即時預測，ML vs. LSTM／GRU |
| [Ferreira 2026](sources/ferreira2026.md) | 區塊鏈＋MCP：LLM 查詢運動資料時的溯源與選手同意 |
| [Rongen 2026](sources/rongen2026.md) | 世界籃網球的培育路徑與選才制度（非 AI 研究） |

## 概念頁

| 概念 | 說明 | 來源 |
|---|---|---|
| [AI 在運動總覽](concepts/ai-in-sport.md) | 定義、主要技術、共同挑戰、未來趨勢 | zhou2025 |
| [生物力學](concepts/biomechanics-ai.md) | 實驗室外蒐集資料、組織負荷估算 | zhou2025 |
| [表現與戰術分析](concepts/performance-analysis.md) | YOLO 追蹤、防守成功預測、戰術狀態偵測 | zhou2025, rothe2026 |
| [戰術狀態](concepts/tactical-states.md) | 專家狀態系統＋分群翻譯表 | rothe2026 |
| [比賽結果預測](concepts/match-outcome-prediction.md) | 網球、板球即時預測；正確率上限的分歧 | buhamra2025, goel2021 |
| [傷害預測](concepts/injury-prediction.md) | 傷害風險預測、風險因子與倫理風險 | zhou2025, cohan2021, majumdar2024 |
| [訓練負荷](concepts/training-load.md) | ACWR、EWMA 與危險門檻的分歧 | majumdar2024 |
| [模型驗證方式](concepts/model-validation.md) | 隨機切分、時間切分、expanding window、沒看過的球隊 | cohan2021, majumdar2024, rothe2026, buhamra2025, goel2021 |
| [不平衡資料與評估指標](concepts/class-imbalance-metrics.md) | accuracy 陷阱、ROC AUC、SMOTE、少見類別 | cohan2021, majumdar2024, rothe2026 |
| [SHAP](concepts/shap.md) | Shapley 值解釋模型與其限制 | cohan2021, majumdar2024, rahimian2025 |
| [運動醫學](concepts/sports-medicine-ai.md) | second opinion、DDSS、復健 | zhou2025 |
| [健康監測](concepts/health-monitoring.md) | 穿戴裝置、智慧衣、LLM 營養建議 | zhou2025 |
| [教練與選才](concepts/talent-identification.md) | 資料驅動選才、信任與成本、選才制度本身 | zhou2025, rongen2026 |
| [可解釋 AI](concepts/explainable-ai.md) | white-box／black-box、SHAP、PDP／ICE | zhou2025, cohan2021, majumdar2024, rahimian2025, buhamra2025 |
| [倫理與隱私](concepts/ethics-privacy.md) | differential privacy、federated learning、區塊鏈 | zhou2025, ferreira2026 |
| [選手同意與資料溯源](concepts/athlete-consent-provenance.md) | MCP、區塊鏈、可驗證憑證 | ferreira2026 |
| [LLM 在運動](concepts/llms-in-sport.md) | 應用、few-shot、LLM 當評審、MCP、幻覺 | zhou2025, rahimian2025, ferreira2026 |
| [Wordalisation](concepts/wordalisation.md) | 用 LLM 把模型輸出寫成文字 | rahimian2025 |

## 研究筆記頁

| 筆記 | 重點 |
|---|---|
| [選才 × 可解釋性](notes/talent-id-explainability.md) | 教練可能難以信任 black box → 選才研究需要 SHAP |
| [選才模型的評估陷阱](notes/talent-id-evaluation-pitfalls.md) | 不平衡資料不能只看 accuracy |
| [平價動作分析](notes/accessible-motion-analysis.md) | 手機影片取代實驗室設備 |
| [LLM 評估的研究缺口](notes/llm-evaluation-gap.md) | 單一 prompt 評估不足、缺人工評估 |
| [專家知識 × 機器學習](notes/expert-knowledge-ml-hybrid.md) | 專家定義＋資料分群的混合方法 |
