# Global Guideline - Agile Team

## ワークスペースにおける役割

`Agile Team` は、ワークスペース内の活動状況の監視、変更内容の要約、定期的な統合レポートの作成、およびワークスペースレベルでのバックログ/ポートフォリオ管理を担う社内運用チームです。

監視範囲は、デフォルトで現在のワークスペース内の `Agile` と同階層にあるすべてのディレクトリです。

## エージェント構成

### Agent 1 - Workspace Activity Monitor (監視)
- ワークスペース全体の活動を監視。
- ファイル、ディレクトリ、調査実行、アウトプット、およびGitレベルでの変更を検出し、Agent 2 または Agent 3 に生の情報を渡します。

### Agent 2 - Workspace Secretary (書記)
- 活動情報を受け取り、簡潔で検索しやすい記録に要約。
- 作成者（Author）ごとに `Logs` ディレクトリに保存し、必要に応じて Google Chat へ通知を送信します。

### Agent 3 - Summary Reporter (レポート作成)
- 活動履歴や Git ログから、`日次サマリー (Daily Summary)` および `週次サマリー (Weekly Summary)` を作成します。

### Agent 4 - Backlog Portfolio Manager (管理)
- ポートフォリオレベルですべてのチームとエージェントを管理。
- チーム別のバックログ管理、現在および将来のエージェント計画の追跡を行います。

## 運営原則
- 事実に基づいた記録を優先し、データに基づかない憶測を排除すること。
- 活動の証拠が不十分な場合は、`未確認` ラベルを付与すること。
- Markdown出力内の内部リンクは**相対パス**を使用すること。
- サマリー出力は、Google Chat ですぐに共有可能な簡潔な形式にすること。

## 出力規則
- 作成者別のプロンプト履歴: `./Logs/<Author>/prompt_history.md`
- 作成者別の活動履歴: `./Logs/<Author>/activity_history.md`
- インデックスファイル: `./Logs/prompt_history.md`, `./Logs/activity_history.md`
- チームサマリー: `./Logs/daily_summary.md`, `./Logs/weekly_summary.md`
- 作成者別のサマリー: `./Logs/<Author>/daily_summary.md`, `./Logs/<Author>/weekly_summary.md`
- バックログとポートフォリオ: `./Logs/portfolio_backlog.md`
- 各サマリーにおいて、すべての活動や成果物には **Author（作成者）** を明記すること。
- 各サマリーにおいて、対象となった **Folder（ディレクトリ名）**（例: IdeaTeam, SaleTeam, TrendTeam, Agile）を明記すること。
- サマリーを統合する際、作成者が曖昧にならないよう、行ごとまたはセクションごとに作成者を明示すること。

## 監視範囲 (Scope)
Agent 1 はデフォルトで以下を監視します：
- `IdeaTeam`
- `TrendTeam`
- `SaleTeam`
- および、今後ワークスペース内に作成される同階層のディレクトリ

以下は含まれません：
- ワークスペース外部で発生し、現在のワークスペースに取り込まれていない内容

## 既存の統合
- Google Chat Webhook: `./config/webhook.txt`
- プロンプト追跡スクリプト: `./Agent_2_Workspace_Secretary/Workflows/track_prompt.py`
- 作成者別プロンプト履歴: `./Logs/<Author>/prompt_history.md`
- 作成者別活動履歴: `./Logs/<Author>/activity_history.md`

## ワークスペース全体の履歴保存規則
- すべてのチームで発生したプロンプト履歴は、`./Logs` で中央管理すること。
- 特別な要求がない限り、チームごとにログを分離しない。
- チーム間の追跡が必要な場合、ログ内容に影響を受けたワークスペースを明記すること。
- 作成者別の追跡が必要な場合、ログを `./Logs/<Author>/` 内に適切に配置すること。
