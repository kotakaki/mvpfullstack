# Master_Index - TrendTeam

## 1. ワークスペースの概要
`TrendTeam` は、プロダクトおよびマーケティング向けのトレンド調査チーム専用ワークスペースです。チームは以下のパイプラインに従って4つのサブエージェントで構成されています：
1. `Agent_1_Signal_Scout` (シグナル・スカウト)
2. `Agent_2_Product_Trend_Analyst` (プロダクト・トレンド・アナリスト)
3. `Agent_3_Marketing_Trend_Analyst` (マーケティング・トレンド・アナリスト)
4. `Agent_4_Trend_Synthesizer` (トレンド・シンセサイザー)

## 2. エージェント・ディレクトリ

### Agent 1
- [Agent_1_Signal_Scout](./Agent_1_Signal_Scout)
- **Knowledge (ナレッジ)**
  - [Signal_scout.md](./Agent_1_Signal_Scout/Knowledge/Signal_scout.md): Agent 1 の役割説明。
  - [Trusted_information_sources.md](./Agent_1_Signal_Scout/Knowledge/Trusted_information_sources.md): テーマ別の信頼できる情報源。
  - [Content_marketing_source_stack.md](./Agent_1_Signal_Scout/Knowledge/Content_marketing_source_stack.md): SNSやブログのコンテンツ作成に最適なソース一覧。
  - [Signal_collection_framework.md](./Agent_1_Signal_Scout/Knowledge/Signal_collection_framework.md): 体系的なシグナル収集フレームワーク。
  - [Source_evaluation_model.md](./Agent_1_Signal_Scout/Knowledge/Source_evaluation_model.md): 情報源の信頼性評価モデル。
  - [Signal_scoring_model.md](./Agent_1_Signal_Scout/Knowledge/Signal_scoring_model.md): シグナルのスコアリングモデル。
  - [Source_taxonomy_by_channel.md](./Agent_1_Signal_Scout/Knowledge/Source_taxonomy_by_channel.md): チャネル別の情報源分類。
  - [Source_watchlist.md](./Agent_1_Signal_Scout/Knowledge/Source_watchlist.md): 定期的に監視すべきソースリスト。
- **Skills (スキル)**
  - [Signal_sourcing_and_validation.md](./Agent_1_Signal_Scout/Skills/Signal_sourcing_and_validation.md): シグナルの収集と検証。
  - [Search_query_design.md](./Agent_1_Signal_Scout/Skills/Search_query_design.md): シグナル探索のためのクエリ設計。
  - [Signal_logging.md](./Agent_1_Signal_Scout/Skills/Signal_logging.md): 標準形式によるシグナルの記録。
  - [Noise_filtering_and_clustering.md](./Agent_1_Signal_Scout/Skills/Noise_filtering_and_clustering.md): ノイズ除去とシグナルのクラスター化（グループ化）。
- **Workflows (ワークフロー)**
  - [Research_intake_workflow.md](./Agent_1_Signal_Scout/Workflows/Research_intake_workflow.md): リサーチ開始前のインテーク（受付）フロー。
  - [Core_signal_scout_workflow.md](./Agent_1_Signal_Scout/Workflows/Core_signal_scout_workflow.md): Agent 1 の中核ワークフロー。
  - [Daily_signal_scan.md](./Agent_1_Signal_Scout/Workflows/Daily_signal_scan.md): 日次シグナルスキャン手順。
  - [Weekly_signal_scan.md](./Agent_1_Signal_Scout/Workflows/Weekly_signal_scan.md): 週次シグナルスキャン手順。
- **Rules (ルール)**
  - [Core_operating_principles.md](./Agent_1_Signal_Scout/Rules/Core_operating_principles.md): Agent 1 の運営原則。
  - [Intake_completeness_rule.md](./Agent_1_Signal_Scout/Rules/Intake_completeness_rule.md): ブリーフが実行可能か判断する規則。
  - [Signal_log_template.md](./Agent_1_Signal_Scout/Rules/Signal_log_template.md): `Signal_Log.md` の標準テンプレート。
  - [Handoff_to_analysts.md](./Agent_1_Signal_Scout/Rules/Handoff_to_analysts.md): アナリストへの引き継ぎ基準。
  - [Signal_update_and_dedup_rules.md](./Agent_1_Signal_Scout/Rules/Signal_update_and_dedup_rules.md): シグナルの更新と重複排除の規則。
  - [Handoff_sample.md](./Agent_1_Signal_Scout/Rules/Handoff_sample.md): Agent 1 の出力・引き継ぎサンプル。

### Agent 2
- [Agent_2_Product_Trend_Analyst](./Agent_2_Product_Trend_Analyst)
- **Knowledge**
  - [Product_trend_analyst.md](./Agent_2_Product_Trend_Analyst/Knowledge/Product_trend_analyst.md): Agent 2 の役割説明。
  - [MVP_prioritization_model.md](./Agent_2_Product_Trend_Analyst/Knowledge/MVP_prioritization_model.md): MVPの優先順位付けモデル。
- **Skills**
  - [Product_trend_analysis.md](./Agent_2_Product_Trend_Analyst/Skills/Product_trend_analysis.md): シグナルを簡潔なMVP提案に変換するスキル。
- **Workflows**
  - [Core_product_trend_analysis_workflow.md](./Agent_2_Product_Trend_Analyst/Workflows/Core_product_trend_analysis_workflow.md): `MVP_Proposals.md` 作成フロー。
- **Rules**
  - [Core_operating_principles.md](./Agent_2_Product_Trend_Analyst/Rules/Core_operating_principles.md): Agent 2 の運営原則。
  - [MVP_Proposals_template.md](./Agent_2_Product_Trend_Analyst/Rules/MVP_Proposals_template.md): Agent 2 アウトプットの標準テンプレート。
  - [Handoff_to_synthesizer.md](./Agent_2_Product_Trend_Analyst/Rules/Handoff_to_synthesizer.md): Agent 4 への引き継ぎ基準。

### Agent 3
- [Agent_3_Marketing_Trend_Analyst](./Agent_3_Marketing_Trend_Analyst)
- **Knowledge**
  - [Marketing_trend_analyst.md](./Agent_3_Marketing_Trend_Analyst/Knowledge/Marketing_trend_analyst.md): 2つの独立したフローを持つ Agent 3 の役割。
  - [Marketing_priority_model.md](./Agent_3_Marketing_Trend_Analyst/Knowledge/Marketing_priority_model.md): マーケティング・アングルの優先順位付けモデル。
  - [Message_and_channel_selection_framework.md](./Agent_3_Marketing_Trend_Analyst/Knowledge/Message_and_channel_selection_framework.md): メッセージ、チャネル、形式の選択フレームワーク。
- **Skills**
  - [Marketing_trend_analysis.md](./Agent_3_Marketing_Trend_Analyst/Skills/Marketing_trend_analysis.md): 2つのフローによるマーケティング分析スキル。
- **Workflows**
  - [Core_marketing_trend_analysis_workflow.md](./Agent_3_Marketing_Trend_Analyst/Workflows/Core_marketing_trend_analysis_workflow.md): Agent 3 の全体ワークフロー。
  - [Flow_1_signal_to_marketing_trends.md](./Agent_3_Marketing_Trend_Analyst/Workflows/Flow_1_signal_to_marketing_trends.md): フロー1：Agent 1 からマーケティングトレンドへ。
  - [Flow_2_signal_and_mvp_to_marketing_angles.md](./Agent_3_Marketing_Trend_Analyst/Workflows/Flow_2_signal_and_mvp_to_marketing_angles.md): フロー2：Agent 1 と Agent 2 の組み合わせ。
- **Rules**
  - [Core_operating_principles.md](./Agent_3_Marketing_Trend_Analyst/Rules/Core_operating_principles.md): Agent 3 の運営原則。
  - [Input_requirements_for_flow_1_and_flow_2.md](./Agent_3_Marketing_Trend_Analyst/Rules/Input_requirements_for_flow_1_and_flow_2.md): 2つのフローの最小入力要件。
  - [Marketing_Trend_Insights_template.md](./Agent_3_Marketing_Trend_Analyst/Rules/Marketing_Trend_Insights_template.md): フロー1のアウトプットテンプレート。
  - [MVP_Marketing_Angles_template.md](./Agent_3_Marketing_Trend_Analyst/Rules/MVP_Marketing_Angles_template.md): フロー2のアウトプットテンプレート。
  - [Flow_conflict_resolution.md](./Agent_3_Marketing_Trend_Analyst/Rules/Flow_conflict_resolution.md): フロー間で結論が矛盾した場合の解決規則。
  - [Handoff_to_synthesizer.md](./Agent_3_Marketing_Trend_Analyst/Rules/Handoff_to_synthesizer.md): Agent 4 への引き継ぎ基準。

### Agent 4
- [Agent_4_Trend_Synthesizer](./Agent_4_Trend_Synthesizer)
- **Knowledge**
  - [Trend_synthesizer.md](./Agent_4_Trend_Synthesizer/Knowledge/Trend_synthesizer.md): Agent 4 の役割説明。
  - [Synthesis_priority_model.md](./Agent_4_Trend_Synthesizer/Knowledge/Synthesis_priority_model.md): 最終的な結論の優先順位付けモデル。
  - [Sub-agent_architecture.md](./Agent_4_Trend_Synthesizer/Knowledge/Sub-agent_architecture.md): チーム全体の連携アーキテクチャ。
- **Skills**
  - [Trend_synthesis_and_prioritization.md](./Agent_4_Trend_Synthesizer/Skills/Trend_synthesis_and_prioritization.md): 統合と優先順位付けのスキル。
  - [NotebookLM_slide_reporting.md](./Agent_4_Trend_Synthesizer/Skills/NotebookLM_slide_reporting.md): NotebookLMのソースとして出力を標準化するスキル。
- **Workflows**
  - [Core_trend_synthesis_workflow.md](./Agent_4_Trend_Synthesizer/Workflows/Core_trend_synthesis_workflow.md): Agent 4 のワークフロー。
  - [NotebookLM_reporting_workflow.md](./Agent_4_Trend_Synthesizer/Workflows/NotebookLM_reporting_workflow.md): アウトプットを NotebookLM 用に変換するワークフロー。
- **Rules**
  - [Core_output_standards.md](./Agent_4_Trend_Synthesizer/Rules/Core_output_standards.md): 最終アウトプット基準。
  - [Input_requirements_from_agents.md](./Agent_4_Trend_Synthesizer/Rules/Input_requirements_from_agents.md): 先行エージェントからの入力要件。
  - [Input_validation_checklist.md](./Agent_4_Trend_Synthesizer/Rules/Input_validation_checklist.md): 統合前の入力検証チェックリスト。
  - [Traceability_and_citation_rules.md](./Agent_4_Trend_Synthesizer/Rules/Traceability_and_citation_rules.md): 追跡可能性と引用の基準。
  - [Executive_Summary_template.md](./Agent_4_Trend_Synthesizer/Rules/Executive_Summary_template.md): エグゼクティブサマリーのテンプレート。
  - [Trend_Report_template.md](./Agent_4_Trend_Synthesizer/Rules/Trend_Report_template.md): 統合レポートのテンプレート。
  - [NotebookLM_Slide_Brief_template.md](./Agent_4_Trend_Synthesizer/Rules/NotebookLM_Slide_Brief_template.md): NotebookLM 専用のブリーフテンプレート。
  - [Final_output_QA_checklist.md](./Agent_4_Trend_Synthesizer/Rules/Final_output_QA_checklist.md): 公開前の最終QAチェックリスト。

## 3. 共用ワークスペース・ファイル
- [Global_Guideline.md](./Global_Guideline.md): チーム全体の総合ガイドライン。
- [README.md](./README.md): ワークスペースのクイック概要。
- [Output](./Output): 完了したリサーチ結果の保存場所。

## 4. サンプル・アウトプット
- [sample_ai_agent_signals/Signal_Log.md](./Output/sample_ai_agent_signals/Signal_Log.md): ベトナム語の `Signal_Log.md` サンプル。
- [sample_ai_agent_signals/MVP_Proposals.md](./Output/sample_ai_agent_signals/MVP_Proposals.md): Agent 2 のサンプル（シグナルを簡潔なMVP提案に変換）。
- [sample_ai_agent_signals/Marketing_Trend_Insights.md](./Output/sample_ai_agent_signals/Marketing_Trend_Insights.md): Agent 3 フロー1のサンプル。
- [sample_ai_agent_signals/MVP_Marketing_Angles.md](./Output/sample_ai_agent_signals/MVP_Marketing_Angles.md): Agent 3 フロー2のサンプル。
- [sample_ai_agent_signals/Executive_Summary.md](./Output/sample_ai_agent_signals/Executive_Summary.md): Agent 4 の最終要約サンプル。
- [sample_ai_agent_signals/Trend_Report.md](./Output/sample_ai_agent_signals/Trend_Report.md): Agent 4 の統合レポートサンプル。
- [sample_ai_agent_signals/NotebookLM_Slide_Brief.md](./Output/sample_ai_agent_signals/NotebookLM_Slide_Brief.md): NotebookLM 用の入力ソースサンプル。

## 5. 推奨される閲覧順序
1. [Global_Guideline.md](./Global_Guideline.md)
2. [README.md](./README.md)
3. [Sub-agent_architecture.md](./Agent_4_Trend_Synthesizer/Knowledge/Sub-agent_architecture.md)
4. [Signal_scout.md](./Agent_1_Signal_Scout/Knowledge/Signal_scout.md)
5. [Trusted_information_sources.md](./Agent_1_Signal_Scout/Knowledge/Trusted_information_sources.md)
... (以下略。基本的には番号順にナレッジからスキル、ルール、ワークフローへと読み進めることを推奨します)
