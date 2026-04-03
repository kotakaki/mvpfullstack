# Master_Index - SaleTeam

## 1. ワークスペースの概要
`SaleTeam` は、セールス活動を支援するためのデータ収集と拡充（Enrichment）を行うチーム専用のワークスペースです。

3つの主要サブエージェント：
1. `Agent_1_Lead_Sourcing_Collector` (リード探索・収集)
2. `Agent_2_Social_Public_Intelligence` (SNS・公開情報インテリジェンス)
3. `Agent_3_Company_Website_Intelligence` (企業ウェブサイト・インテリジェンス)

## 2. エージェント・ディレクトリ

### Agent 1
- [Agent_1_Lead_Sourcing_Collector](./Agent_1_Lead_Sourcing_Collector)
- **Knowledge (ナレッジ)**
  - [Lead_Sourcing_Collector.md](./Agent_1_Lead_Sourcing_Collector/Knowledge/Lead_Sourcing_Collector.md)
  - [Lead_Source_Taxonomy.md](./Agent_1_Lead_Sourcing_Collector/Knowledge/Lead_Source_Taxonomy.md)
  - [ICP_Fit_Scoring_Model.md](./Agent_1_Lead_Sourcing_Collector/Knowledge/ICP_Fit_Scoring_Model.md)
- **Skills (スキル)**
  - [Lead_List_Building.md](./Agent_1_Lead_Sourcing_Collector/Skills/Lead_List_Building.md)
  - [Source_Normalization_and_Dedup.md](./Agent_1_Lead_Sourcing_Collector/Skills/Source_Normalization_and_Dedup.md)
  - [List_Intake_and_Record_Keying.md](./Agent_1_Lead_Sourcing_Collector/Skills/List_Intake_and_Record_Keying.md)
  - [LinkedIn_Profile_Sourcing.md](./Agent_1_Lead_Sourcing_Collector/Skills/LinkedIn_Profile_Sourcing.md)
- **Workflows (ワークフロー)**
  - [Research_Intake_Workflow.md](./Agent_1_Lead_Sourcing_Collector/Workflows/Research_Intake_Workflow.md)
  - [Core_Lead_Collection_Workflow.md](./Agent_1_Lead_Sourcing_Collector/Workflows/Core_Lead_Collection_Workflow.md)
  - [LinkedIn_Lead_Sourcing_Workflow.md](./Agent_1_Lead_Sourcing_Collector/Workflows/LinkedIn_Lead_Sourcing_Workflow.md)
  - [List_Based_Enrichment_Workflow.md](./Agent_1_Lead_Sourcing_Collector/Workflows/List_Based_Enrichment_Workflow.md)
  - [Missing_Data_Resolution_Workflow.md](./Agent_1_Lead_Sourcing_Collector/Workflows/Missing_Data_Resolution_Workflow.md)
  - [Daily_Lead_Source_Scan.md](./Agent_1_Lead_Sourcing_Collector/Workflows/Daily_Lead_Source_Scan.md)
  - [Weekly_Lead_Source_Scan.md](./Agent_1_Lead_Sourcing_Collector/Workflows/Weekly_Lead_Source_Scan.md)
- **Rules (ルール)**
  - [Core_Operating_Principles.md](./Agent_1_Lead_Sourcing_Collector/Rules/Core_Operating_Principles.md)
  - [Intake_Completeness_Rule.md](./Agent_1_Lead_Sourcing_Collector/Rules/Intake_Completeness_Rule.md)
  - [LinkedIn_Sourcing_Input_Requirements.md](./Agent_1_Lead_Sourcing_Collector/Rules/LinkedIn_Sourcing_Input_Requirements.md)
  - [Input_List_Requirements.md](./Agent_1_Lead_Sourcing_Collector/Rules/Input_List_Requirements.md)
  - [ICP_Input_Brief_Template.md](./Agent_1_Lead_Sourcing_Collector/Rules/ICP_Input_Brief_Template.md)
  - [00_Input_List_Template.md](./Agent_1_Lead_Sourcing_Collector/Rules/00_Input_List_Template.md)
  - [Record_ID_and_Handoff_Rule.md](./Agent_1_Lead_Sourcing_Collector/Rules/Record_ID_and_Handoff_Rule.md)
  - [Enrichment_Routing_Matrix.md](./Agent_1_Lead_Sourcing_Collector/Rules/Enrichment_Routing_Matrix.md)
  - [Enrichment_Status_Rule.md](./Agent_1_Lead_Sourcing_Collector/Rules/Enrichment_Status_Rule.md)
  - [LinkedIn_Profile_Selection_Rule.md](./Agent_1_Lead_Sourcing_Collector/Rules/LinkedIn_Profile_Selection_Rule.md)
  - [Lead_List_Template.md](./Agent_1_Lead_Sourcing_Collector/Rules/Lead_List_Template.md)
  - [Enriched_Record_Summary_Template.md](./Agent_1_Lead_Sourcing_Collector/Rules/Enriched_Record_Summary_Template.md)

### Agent 2
- [Agent_2_Social_Public_Intelligence](./Agent_2_Social_Public_Intelligence)
- **Knowledge**
  - [Social_Public_Intelligence_Analyst.md](./Agent_2_Social_Public_Intelligence/Knowledge/Social_Public_Intelligence_Analyst.md)
  - [Public_Signal_Taxonomy.md](./Agent_2_Social_Public_Intelligence/Knowledge/Public_Signal_Taxonomy.md)
  - [Social_Priority_Model.md](./Agent_2_Social_Public_Intelligence/Knowledge/Social_Priority_Model.md)
  - [Watch_Tier_and_Cadence_Model.md](./Agent_2_Social_Public_Intelligence/Knowledge/Watch_Tier_and_Cadence_Model.md)
- **Skills**
  - [Social_Profile_Research.md](./Agent_2_Social_Public_Intelligence/Skills/Social_Profile_Research.md)
  - [Customer_Care_Signal_Tracking.md](./Agent_2_Social_Public_Intelligence/Skills/Customer_Care_Signal_Tracking.md)
- **Workflows**
  - [Research_Intake_Workflow.md](./Agent_2_Social_Public_Intelligence/Workflows/Research_Intake_Workflow.md)
  - [Core_Social_Intelligence_Workflow.md](./Agent_2_Social_Public_Intelligence/Workflows/Core_Social_Intelligence_Workflow.md)
  - [Daily_Social_Signal_Scan.md](./Agent_2_Social_Public_Intelligence/Workflows/Daily_Social_Signal_Scan.md)
  - [Weekly_Social_Intelligence_Scan.md](./Agent_2_Social_Public_Intelligence/Workflows/Weekly_Social_Intelligence_Scan.md)
- **Rules**
  - [Core_Operating_Principles.md](./Agent_2_Social_Public_Intelligence/Rules/Core_Operating_Principles.md)
  - [Intake_Completeness_Rule.md](./Agent_2_Social_Public_Intelligence/Rules/Intake_Completeness_Rule.md)
  ... (中略。個別ファイルの日本語訳が必要な場合は別途対応いたします)
  - [Public_Customer_Intelligence_Template.md](./Agent_2_Social_Public_Intelligence/Rules/Public_Customer_Intelligence_Template.md)

### Agent 3
- [Agent_3_Company_Website_Intelligence](./Agent_3_Company_Website_Intelligence)
- **Knowledge**
  - [Company_Website_Intelligence_Analyst.md](./Agent_3_Company_Website_Intelligence/Knowledge/Company_Website_Intelligence_Analyst.md)
  - [Company_Website_Signal_Framework.md](./Agent_3_Company_Website_Intelligence/Knowledge/Company_Website_Signal_Framework.md)
  - [Website_Signal_Priority_Model.md](./Agent_3_Company_Website_Intelligence/Knowledge/Website_Signal_Priority_Model.md)
- **Skills**
  - [Website_Research_and_Extraction.md](./Agent_3_Company_Website_Intelligence/Skills/Website_Research_and_Extraction.md)
  - [Sitemap_Discovery_and_Page_Prioritization.md](./Agent_3_Company_Website_Intelligence/Skills/Sitemap_Discovery_and_Page_Prioritization.md)
  ...
- **Workflows**
  - [Research_Intake_Workflow.md](./Agent_3_Company_Website_Intelligence/Workflows/Research_Intake_Workflow.md)
  - [Core_Company_Website_Intelligence_Workflow.md](./Agent_3_Company_Website_Intelligence/Workflows/Core_Company_Website_Intelligence_Workflow.md)
  - [Weekly_Website_Change_Scan.md](./Agent_3_Company_Website_Intelligence/Workflows/Weekly_Website_Change_Scan.md)
- **Rules**
  - [Core_Operating_Principles.md](./Agent_3_Company_Website_Intelligence/Rules/Core_Operating_Principles.md)
  - [Company_Website_Intelligence_Template.md](./Agent_3_Company_Website_Intelligence/Rules/Company_Website_Intelligence_Template.md)

## 3. 共用ファイル
- [README.md](./README.md)
- [Global_Guideline.md](./Global_Guideline.md)
- [Test_Scenarios.md](./Test_Scenarios.md)
- [Output (出力先)](./Output)

## 4. 推奨される閲覧順序

### フロー A: 情報源からリードを構築する
1. [Global_Guideline.md](./Global_Guideline.md)
2. [README.md](./README.md)
3. [Lead_Sourcing_Collector.md](./Agent_1_Lead_Sourcing_Collector/Knowledge/Lead_Sourcing_Collector.md)
... (以下、目的や利用シーンに応じて各エージェントのワークフローやルールを参照してください)
