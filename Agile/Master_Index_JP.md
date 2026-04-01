# Master Index - Agile Team

## 概要
`Agile Team` は4つのエージェントで構成されています：

1. `Agent 1`: ワークスペース全体の活動監視。
2. `Agent 2`: 活動の要約とログ保存を行う書記。
3. `Agent 3`: 日次および週次サマリーの作成。
4. `Agent 4`: バックログとエージェント・ポートフォリオの管理。

## エージェント別のアウトプット

### Agent 1 (Monitor)
- [Workspace_Activity_Monitor.md](./Agent_1_Workspace_Activity_Monitor/Knowledge/Workspace_Activity_Monitor.md)
- [Workspace_Scope_Definition.md](./Agent_1_Workspace_Activity_Monitor/Knowledge/Workspace_Scope_Definition.md)
- [Activity_Signal_Collection.md](./Agent_1_Workspace_Activity_Monitor/Skills/Activity_Signal_Collection.md)
- [Workspace_Monitoring_Workflow.md](./Agent_1_Workspace_Activity_Monitor/Workflows/Workspace_Monitoring_Workflow.md)
- [workspace-task-manager.md](./Agent_1_Workspace_Activity_Monitor/Workflows/workspace-task-manager.md)
- [Scope_and_Change_Detection_Rule.md](./Agent_1_Workspace_Activity_Monitor/Rules/Scope_and_Change_Detection_Rule.md)

### Agent 2 (Secretary)
- [Workspace_Secretary.md](./Agent_2_Workspace_Secretary/Knowledge/Workspace_Secretary.md)
- [Activity_Log_Standards.md](./Agent_2_Workspace_Secretary/Knowledge/Activity_Log_Standards.md)
- [Activity_Summarization.md](./Agent_2_Workspace_Secretary/Skills/Activity_Summarization.md)
- [Activity_Logging_Workflow.md](./Agent_2_Workspace_Secretary/Workflows/Activity_Logging_Workflow.md)
- [track_prompt.py](./Agent_2_Workspace_Secretary/Workflows/track_prompt.py)
- [Activity_Log_Template.md](./Agent_2_Workspace_Secretary/Rules/Activity_Log_Template.md)
- [Cross_Workspace_History_Rule.md](./Agent_2_Workspace_Secretary/Rules/Cross_Workspace_History_Rule.md)

### Agent 3 (Reporter)
- [Summary_Reporter.md](./Agent_3_Summary_Reporter/Knowledge/Summary_Reporter.md)
- [Summary_Output_Model.md](./Agent_3_Summary_Reporter/Knowledge/Summary_Output_Model.md)
- [Daily_and_Weekly_Summary_Writing.md](./Agent_3_Summary_Reporter/Skills/Daily_and_Weekly_Summary_Writing.md)
- [Daily_Summary_Workflow.md](./Agent_3_Summary_Reporter/Workflows/Daily_Summary_Workflow.md)
- [daily-summary.md](./Agent_3_Summary_Reporter/Workflows/daily-summary.md)
- [Weekly_Summary_Workflow.md](./Agent_3_Summary_Reporter/Workflows/Weekly_Summary_Workflow.md)
- [Summary_Template.md](./Agent_3_Summary_Reporter/Rules/Summary_Template.md)

### Agent 4 (Project/Portfolio Manager)
- [Backlog_Portfolio_Manager.md](./Agent_4_Backlog_Portfolio_Manager/Knowledge/Backlog_Portfolio_Manager.md)
- [Agent_Portfolio_Model.md](./Agent_4_Backlog_Portfolio_Manager/Knowledge/Agent_Portfolio_Model.md)
- [Backlog_Taxonomy.md](./Agent_4_Backlog_Portfolio_Manager/Knowledge/Backlog_Taxonomy.md)
- [Portfolio_Backlog_Planning.md](./Agent_4_Backlog_Portfolio_Manager/Skills/Portfolio_Backlog_Planning.md)
- [Team_Backlog_Segmentation_Rule.md](./Agent_4_Backlog_Portfolio_Manager/Rules/Team_Backlog_Segmentation_Rule.md)
- [Backlog_Item_Template.md](./Agent_4_Backlog_Portfolio_Manager/Rules/Backlog_Item_Template.md)
- [Portfolio_Backlog_Management_Workflow.md](./Agent_4_Backlog_Portfolio_Manager/Workflows/Portfolio_Backlog_Management_Workflow.md)
- [Future_Agent_Planning_Workflow.md](./Agent_4_Backlog_Portfolio_Manager/Workflows/Future_Agent_Planning_Workflow.md)

## 共用リソース
- [README.md](./README.md)
- [Global_Guideline.md](./Global_Guideline.md)
- [Logs (ログディレクトリ)](./Logs)
- [Prompt History (プロンプト履歴索引)](./Logs/prompt_history.md)
- [Activity History (活動履歴索引)](./Logs/activity_history.md)
- [Team Daily Summary (日次要約)](./Logs/daily_summary.md)
- [Team Weekly Summary (週次要約)](./Logs/weekly_summary.md)
- [Team Portfolio Backlog (ポートフォリオバックログ)](./Logs/portfolio_backlog.md)
- [config (設定ディレクトリ)](./config)
- [Test_Scenarios.md (テストシナリオ)](./Test_Scenarios.md)

## 推奨される閲覧順序
1. [README.md](./README.md)
2. [Global_Guideline.md](./Global_Guideline.md)
3. [Workspace_Activity_Monitor.md](./Agent_1_Workspace_Activity_Monitor/Knowledge/Workspace_Activity_Monitor.md)
4. [Workspace_Monitoring_Workflow.md](./Agent_1_Workspace_Activity_Monitor/Workflows/Workspace_Monitoring_Workflow.md)
... (以下、各役割やワークフローに応じて読み進めてください)
