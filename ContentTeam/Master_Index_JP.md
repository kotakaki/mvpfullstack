# ContentTeam：マスター・インデックス（日本語版）

> [!TIP]
> **マーケティング担当者の方へ**
> このAIエージェントたちの使い方（プロンプトのコピペ手順など）は、[マーケティング向け利用ガイド](Marketing_Team_Portal_JP.md) をご覧ください。

## 🚀 記事制作オートメーション（Rabiloo Content Engine）

本チームの各エージェントを自動連携させ、市場分析から執筆までを一気通貫で実行する仕組みです。

- **実行コマンド**: `/content-engine [対象キーワード] [補足トピック]`
- **仕組みの脳**: [.agents/workflows/content-engine.md](file:///Users/dvcong/.gemini/antigravity/scratch/mvpfullstack/.agents/workflows/content-engine.md)

このコマンドを実行すると、後述の各エージェントが自動的にバトンリレーを行い、完成原稿まで出力します。

### 0. 最重要ピラー（柱）記事

- **中小企業向けDXの進め方と実例**: [SME_DX_Pillar_JP.md](SME_DX_Pillar_JP.md)
  - ※全ての「DX」「デジタルリテラシー」系記事のハブとなる最優先参照ドキュメント。

### 0.1 トピッククラスター：POS・AI・事例

- **POSシステム独自開発の要諦**: [POS_System_Development_JP.md](POS_System_Development_JP.md)
  - パッケージの限界を突破し、54店舗拡大を支えた技術と戦略の解説。
- **AIエージェント最新トレンド（2026年3月版）**: [AI_Agent_Trend_2026_JP.md](AI_Agent_Trend_2026_JP.md)
  - ソフトバンクやガートナーの最新動向と、中小企業が取るべき「自律型AI」戦略。
- **【導入事例】株式会社ほねごり様インタビュー**: [Honegori_Interview_JP.md](Honegori_Interview_JP.md)
  - 年商100億・54店舗。急成長を支えた「伴走型パートナー戦略」の真髄。

## 1. チーム構成とサブエージェント

1. **Agent 1: SEO Writer（本ドキュメントの核）**
   - **役割**: 構成案作成、各セクションの執筆。SEO/GEOの両立、トーンの管理。
2. **Agent 2: Content Auditor & Strategist**
   - **役割**: 既存記事の診断とリライト戦略の立案。GSC/GA4データに基づいた意思決定。
3. **Agent 3: Short Movie Scriptwriter**
   - **役割**: 既存ブログからショート動画（TikTok/Shorts）用の台本を作成。3秒フックと実績の凝縮。
4. **Agent 4: Fact Checker（将来拡張予定）**
   - **役割**: Rabilooの過去実績データとの照合。技術的ハルシネーションの検知。
5. **Agent 5: Layout & Image Designer（将来拡張予定）**
   - **役割**: 記事内の図解指示書の作成、メタデータの記述。

### ショート動画台本作成フロー（Agent 3 担当）

1. **ソース入力**: 既存のブログ記事またはURLを提示。
2. **要素抽出**: Agent 3 がブログから「最もインパクトのある結論」と「数値データ」を抽出。
3. **台本構成**: 「HOOK -> PROBLEM -> SOLUTION -> PROOF -> CTA」の60秒構成で執筆。
4. **実績補強**: `IdeaTeam/Knowledge/` 等から最新の一次情報を、ナレッジ・レジストリ経由で取得し統合。

### 既存記事の診断・リライトフロー（Agent 2 担当）

1. **データ入力**: URL、タイトル、現在の構成、GSC/GA4データを提示。
2. **現状診断**: Agent 2 がカテゴリー（A〜D）を判定し、課題を特定。
3. **戦略策定**: リライト・統合・削除のいずれかを提案。リライトの場合は構成案を作成。
4. **執筆実行**: 必要に応じて Agent 1 が執筆（または既存部分を修正）。

### 新規記事の制作ワークフロー（Agent 1 担当）

新規記事の制作手順は `.agents/workflows/content-engine.md` に唯一の定義があります。
ここでは重複定義を避けるため、詳細は記載しません。content-engine.md を参照してください。
