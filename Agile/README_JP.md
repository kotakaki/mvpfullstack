# Agile Team

`Agile` は、ワークスペース全体の活動を監視、記録、集約し、バックログやポートフォリオを管理するための4つのエージェントが連携する `Agile Team` ワークスペースとして再定義されました。

## チーム構成

1. **Agent_1_Workspace_Activity_Monitor**（ワークスペース活動モニター）
   - `Agile` と同階層のディレクトリにおける活動を監視します。
   - 変更、新しい実行、新しいファイル、新しいコミット、および追跡が必要なイベントを検出します。

2. **Agent_2_Workspace_Secretary**（ワークスペース秘書）
   - 各活動を要約します。
   - ログの保存、活動履歴の更新、および必要に応じた通知の送信を行います。

3. **Agent_3_Summary_Reporter**（要約レポーター）
   - 日報（daily summary）を作成します。
   - 週報（weekly summary）を作成します。
   - Google Chat 送信用または内部保存用にアウトプットをパッケージ化します。

4. **Agent_4_Backlog_Portfolio_Manager**（バックログ・ポートフォリオマネージャー）
   - `エージェント・ポートフォリオ` レベルで既存のすべてのチームとエージェントを管理します。
   - 各チームごとに具体的に分割されたバックログを管理します。
   - 現在のバックログと将来のエージェント計画の両方を追跡します。

## 目標

- ワークスペース全体の活動を追跡できるようにすること。
- 各重要活動に対して一貫した要約ログを保持すること。
- 再利用可能な日報および週報を作成すること。

## 運用原則

- 正しいイベントと正しい範囲を正確に記録することを優先します。
- 正確な要約のために情報が不足している場合は、`未確認` と明記しなければなりません。
- ユーザーの要求がある場合にのみ、スコープの拡張や次のアクションを提案してください。

## クイックナビゲーション

- [Global_Guideline_JP.md](./Global_Guideline_JP.md)（日本語版）
- [Master_Index.md](./Master_Index.md)
- [Agent_1_Workspace_Activity_Monitor](./Agent_1_Workspace_Activity_Monitor)
- [Agent_2_Workspace_Secretary](./Agent_2_Workspace_Secretary)
- [Agent_3_Summary_Reporter](./Agent_3_Summary_Reporter)
- [Agent_4_Backlog_Portfolio_Manager](./Agent_4_Backlog_Portfolio_Manager)
- [Logs](./Logs)
- [config](./config)
