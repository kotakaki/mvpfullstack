# Elite Agent Documentation Framework: Global Guideline (PO Edition)

## Chương 1: Triết lý & Giá trị cốt lõi (Philosophy & Value)

Hệ thống **Elite Agent Documentation Framework** là một quy trình khép kín gồm 4 Agent chuyên biệt, phối hợp để chuyển đổi một ý tưởng thô thành bộ hồ sơ dự án MVP (Minimum Viable Product) hoàn chỉnh và thiết kế UI/UX thực tế.

### 1.1 Triết lý JTBD (Job-to-be-Done)
Mọi sản phẩm được tạo ra không phải để tồn tại tính năng, mà để giải quyết một "Công việc" cốt lõi của người dùng. Framework bắt buộc các Agent phải liên tục đặt câu hỏi: *"Sản phẩm này được 'thuê' để làm gì?"* và loại bỏ mọi tính năng thừa thãi không phục vụ mục tiêu đó.

### 1.2 Mô hình 4 Lớp Chuyên biệt
1.  **Lớp Chiến lược (Agent 1)**: Định hình "What & Why" (Làm cái gì và tại sao?).
2.  **Lớp Kỹ thuật (Agent 2)**: Định hình "How" (Làm như thế nào?).
3.  **Lớp Hoàn thiện (Agent 3)**: Định hình "Quality & Detail" (Làm sao để đúng và đủ?).
4.  **Lớp Thiết kế (Agent 4)**: Định hình "Look & Feel" (Giao diện và trải nghiệm).

---

## Chương 2: Lộ trình phát triển sản phẩm (Product Lifecycle)

Quy trình đi qua 4 giai đoạn chuyển tiếp mượt mà:

### Phase 1: Business Strategy (Agent 1 - Elite Strategy PM)
Trọng tâm là làm rõ giá trị kinh doanh, nghiên cứu thị trường và thiết lập các tiêu chuẩn thành công.

### Phase 2: Technical Design (Agent 2 - AI Solution Architect)
Trọng tâm là thiết kế kiến trúc hệ thống, lựa chọn công nghệ và đảm bảo tính khả thi kỹ thuật.

### Phase 3: Documentation & QA (Agent 3 - MVP Documentation Agent)
Trọng tâm là đặc tả chi tiết (PRD, SRS) và xây dựng bộ kịch bản kiểm thử (Test Cases).

### Phase 4: Visual Design (Agent 4 - Product Designer)
Trọng tâm là biến các yêu cầu thành giao diện người dùng (UI) thực tế và nguyên mẫu tương tác trên Stitch.

### Bảng Bàn giao (Handoff Matrix)
| Giai đoạn | Bên gửi | Tài liệu bàn giao | Bên nhận | Nhiệm vụ tiếp theo |
| :--- | :--- | :--- | :--- | :--- |
| **Handoff 1** | Agent 1 | Folder `BRD/` | Agent 2 | Thiết kế kiến trúc kỹ thuật dựa trên BRD. |
| **Handoff 2** | Agent 2 | Technical Solution | Agent 3 | Chi tiết hóa Spec và xây dựng kịch bản Test. |
| **Handoff 3** | Agent 3 | MVP PRD & SRS | Agent 4 | Thiết kế UI/UX trên Stitch dựa trên PRD. |
| **Final Delivery**| Agent 4 | Master Project Index | Human | Nghiệm thu hồ sơ và thiết kế UI/UX. |

---

## Chương 3: Hướng dẫn bộ hồ sơ đầu ra (Deliverables Guide)

### 3.1 Vai trò từng tài liệu
*   **[Project]_BRD.md**: Kim chỉ nam nghiệp vụ và User Flow cốt lõi.
*   **[Project]_PPD.md**: Bản đồ đối thủ và chiến lược định vị sản phẩm.
*   **[Project]_SDK.md**: Bộ công cụ giúp Sales/BD thuyết phục đối tác/khách hàng.
*   **[Project]_Solution_Design.md**: Bản vẽ kiến trúc kỹ thuật (Tech Stack, ERD, API).
*   **Executive_Summary.md**: Bản tóm tắt "Executive View" dành cho lãnh đạo.
*   **MVP_PRD.md**: Đặc tả tính năng dưới góc nhìn sản phẩm (Stories & AC).
*   **[Project]_SRS.md**: Tài liệu hướng dẫn chi tiết dành cho đội ngũ phát triển (Bao gồm Agent Flow và User Flow).
*   **MVP_Test_Cases.md**: Bộ kịch bản kiểm thử chất lượng đầu ra.
*   **Master_Project_Index.md**: Bản đồ tra cứu nhanh toàn bộ kho tài liệu dự án.

---

## Chương 4: Từ điển Nội lực Agents (Full KWSR Dictionary)

Đây là phần đặc tả chi tiết tác dụng của từng tệp tin cấu thành nên năng lực của các Agent.

### 4.1 Agent 1: Elite Strategy PM
*   **Knowledge (Tri thức)**:
    *   `PO_framework_jtbd.md`: Khung tư duy "thuê" sản phẩm để giải quyết nhu cầu cốt lõi.
    *   `BA_risk_management_raid_log.md`: Phương pháp quản trị rủi ro và các điểm phụ thuộc (RAID).
    *   `BD_marketing_positioning_framework.md`: Cách xác định "vùng xanh" cho sản phẩm trên thị trường.
    *   `BD_sales_kit_essentials.md`: Danh mục các tài liệu cần cho bộ SDK thuyết phục.
    *   `Core_definition_of_done_framework.md`: Bộ tiêu chuẩn nghiệm thu "Xong" cho mọi tác vụ.
    *   `BA_mindset_mba_ecba.md`: Tư duy phân tích nghiệp vụ thực dụng theo chuẩn IIBA.
    *   `PO_mindset_product_owner.md`: Tư duy tập trung vào giá trị (Value) và ưu tiên (Prioritization).
    *   `BD_mindset_growth_marketing.md`: Tư duy thu hút và giữ chân người dùng qua sản phẩm.
    *   `PO_business_requirement_framework.md`: Cấu trúc chuẩn hóa cho yêu cầu kinh doanh.
    *   `Core_cross_validation_matrix.md`: Công cụ đối soát tính đồng bộ của các yêu cầu.
*   **Workflows (Quy trình)**:
    *   `Core_idea_intake_process.md`: Quy trình 5 bước biến ý tưởng thô thành hồ sơ chiến lược.
*   **Skills (Kỹ năng)**:
    *   `BD_market_intelligence_research.md`: Kỹ năng trinh sát thị trường và đối thủ.
    *   `BA_visual_modeling_mermaid.md`: Kỹ năng trực quan hóa quy trình bằng biểu đồ.
    *   `BA_babok_elicitation_techniques.md`: Kỹ thuật phỏng vấn và khơi gợi nhu cầu thầm kín.
    *   `Core_information_architecture_formatting.md`: Kỹ năng cấu trúc thông tin tài liệu chuyên nghiệp.
    *   `Core_self_reflection_and_critique.md`: Kỹ năng tự kiểm chứng và phản biện kết quả.
*   **Rules (Quy chuẩn)**:
    *   `Core_persona_guidelines.md`: Quy tắc về giọng văn và thái độ của một Strategy PM.
    *   `Core_output_standards.md`: Tiêu chuẩn định dạng Markdown và trình bày tài liệu.
    *   `Core_interaction_protocol.md`: Giao thức tương tác đa phương tiện.

### 4.2 Agent 2: AI Solution Architect
*   **Knowledge (Tri thức)**:
    *   `Arch_design_perspectives.md`: Các tiêu chuẩn thiết kế (Scalability, Security, Maintenance).
    *   `Arch_system_architecture_patterns.md`: Kho các mẫu kiến trúc hệ thống hiện đại.
    *   `Stack_ai_tech_stack_guide.md`: Hướng dẫn lựa chọn công nghệ tối ưu cho AI MVP.
    *   `Stack_ai_cost_and_performance.md`: Phân tích cân bằng giữa chi phí vận hành và hiệu suất.
    *   `Arch_ai_strategy_decision_matrix.md`: Ma trận ra quyết định kiến trúc chiến lược.
    *   `Arch_srd_template.md`: Mẫu đặc tả giải pháp kỹ thuật chuyên sâu.
    *   `Arch_ai_observability_and_devops.md`: Kiến thức về vận hành và giám sát hệ thống AI.
*   **Workflows (Quy trình)**:
    *   `Core_solution_design_workflow.md`: Quy trình thiết kế kiến trúc từ BRD.
*   **Skills (Kỹ năng)**:
    *   `Arch_architecture_design.md`: Kỹ năng thiết kế các lớp của hệ thống.
    *   `Arch_diagramming_architecture.md`: Kỹ năng vẽ sơ đồ Sequence, ERD, Infrastructure.
    *   `Arch_technical_solution_drafting.md`: Kỹ năng viết nội dung đặc tả kỹ thuật.
    *   `Arch_project_estimation_manhours.md`: Kỹ năng ước tính nỗ lực thực thi (Man-hours).
    *   `Arch_ai_risk_and_testing.md`: Kỹ năng đánh giá rủi ro kỹ thuật và lập kế hoạch kiểm thử AI.
*   **Rules (Quy chuẩn)**:
    *   `Core_architect_persona.md`: Persona chuyên gia logic, thực tế và chính xác.
    *   `Core_architectural_standards.md`: Các nguyên tắc kiến trúc "bất di bất dịch".
    *   `Core_handover_alignment_rules.md`: Quy tắc đối soát bàn giao 1:1 với Agent 1.
    *   `Core_constraints.md`: Các hạn chế về công nghệ và hạ tầng.

### 4.3 Agent 3: MVP Documentation Agent
*   **Knowledge (Tri thức)**:
    *   `BA_brd_sdd_mapping.md`: Kỹ thuật ánh xạ từ nghiệp vụ sang giải pháp.
    *   `BA_ai_agent_documentation_pitfalls.md`: Cảnh báo các lỗi tài liệu AI thường gặp.
    *   `QA_tester_mindset.md`: Tư duy của người kiểm thử (tìm lỗi và đảm bảo chất lượng).
    *   `BA_documentation_style_guide.md`: Quy tắc viết tài liệu cho người đọc dễ hiểu nhất.
    *   `Index_cataloging_best_practices.md`: Quy tắc sắp xếp và lưu trữ kho tài liệu.
*   **Workflows (Quy trình)**:
    *   `Core_project_finalization_workflow.md`: Quy trình đóng gói bộ hồ sơ cuối cùng.
*   **Skills (Kỹ năng)**:
    *   `BA_mvp_prd_writing.md`: Kỹ năng viết yêu cầu sản phẩm (Stories, Use Cases).
    *   `BA_system_documentation_writing.md`: Kỹ năng viết đặc tả hệ thống chi tiết (SRS).
    *   `QA_test_case_writing.md`: Kỹ năng xây dựng kịch bản kiểm thử Acceptance Tests.
    *   `BA_executive_summary_drafting.md`: Kỹ năng chắt lọc thông tin cho ban lãnh đạo.
    *   `PM_product_management_oversight.md`: Kỹ năng rà soát và đảm bảo tính nhất quán của dự án.
    *   `Index_master_index_generation.md`: Kỹ năng tạo chỉ mục tự động cho toàn bộ dự án.
*   **Rules (Quy chuẩn)**:
    *   `Core_documentation_persona.md`: Persona người soạn thảo tài liệu chuyên nghiệp.
    *   `Core_documentation_standards.md`: Tiêu chuẩn về tính hệ thống và liên kết của hồ sơ.

### 4.4 Agent 4: Product Designer
*   **Knowledge (Tri thức)**:
    *   `UIUX_design_principles.md`: Các nguyên lý cốt lõi về trải nghiệm người dùng.
    *   `Product_design_mindset.md`: Tư duy thiết kế dựa trên sản phẩm và chỉ số kinh doanh.
    *   `Atomic_design_system.md`: Tri thức xây dựng UI nhất quán và dễ mở rộng.
*   **Workflows (Quy trình)**:
    *   `Core_ui_design_workflow.md`: Quy trình thiết kế trực quan trên công cụ Stitch.
*   **Skills (Kỹ năng)**:
    *   `Designer_stitch_ui_management.md`: Kỹ năng vận hành bộ cộng cụ Stitch để tạo giao diện.
    *   `Interactive_prototyping_stitch.md`: Kỹ năng tạo nguyên mẫu có thể tương tác (Clickthrough).
    *   `UX_audit_and_optimization.md`: Kỹ năng đánh giá và tối ưu hóa trải nghiệm người dùng.
*   **Rules (Quy chuẩn)**:
    *   `Core_designer_rules.md`: Tiêu chuẩn thiết kế đồng nhất và Persona Designer sáng tạo.

---

## Chương 5: Quản trị & Vận hành (Governance)

1.  **Living Document Policy**: Guideline này là tài liệu sống. Mọi thay đổi về tri thức hay kỹ năng phải được cập nhật ngay lập tức.
2.  **Strict Handover**: Agent sau không tự ý thay đổi Scope của Agent trước mà không có sự đồng ý.
3.  **Consistency Rule**: Tên dự án, tên file và thuật ngữ phải đồng nhất tuyệt đối xuyên suốt 4 Agent.

---
*Elite Agent Documentation Framework - Standardizing Excellence.*
