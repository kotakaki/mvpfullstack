# Rules: Documentation Standards (Agent 3)

Mục tiêu: Các tiêu chuẩn định dạng bắt buộc cho tất cả hồ sơ dự án.

## 1. Markdown Standards
- **Header Structure**: Luôn bắt đầu bằng H1 (`#`) cho tiêu đề tệp. Không dùng Header cấp 4 trở xuống trừ khi thực sự cần thiết.
- **Lists**: Sử dụng gạch đầu dòng (`-`) thay vì số (`1.`) cho các danh sách không có thứ tự ưu tiên.
- **Code Blocks**: Mọi đoạn code, API endpoint, JSON model hoặc Markdown snippet phải nằm trong dấu backtick (fenced code blocks).

## 2. Elite Agent Documentation Standard (Bắt buộc)
Tất cả hồ sơ dự án phải tuân thủ khung **Elite A-G**, bao quát toàn bộ 10 điểm đặc tả Agent:

### A. Agent Charter (Tầm nhìn)
- Bao gồm: **1. Business Objective** (Bài toán, Giá trị, KPI) và **2. Agent Scope** (Nhiệm vụ, Actor).
- Hình thức: Tài liệu 1 trang quản trị cao cấp.

### B. Agent Workflow / Decision Map (Logic)
- Bao gồm: **4. Conversation/Task Flow** (Luồng chính/ngoại lệ/leo thang).
- Hình thức: Sơ đồ Mermaid mô tả luồng tư duy và ra quyết định.

### C. Tool Permission Matrix (Quyền hạn)
- Bao gồm: **6. Tools & Actions** (Tools, Policy, Fallback) và **3. Autonomy & Oversight** (Mức tự chủ, Phê duyệt).
- Hình thức: Bảng ma trận quyền hạn và điều kiện sử dụng công cụ.

### D. Prompt Requirement Spec (Cấu trúc)
- Bao gồm: **8. Response Requirements** (Format, Tone) và **5. Knowledge & Context** (Context boundary).
- Hình thức: Đặc tả Persona, chỉ dẫn ưu tiên và các hành vi bị cấm.

### E. Knowledge Source Map (Tri thức)
- Bao gồm: **5. Knowledge & Context** (Tri thức, Ưu tiên nguồn, Source of Truth).
- Hình thức: Bảng thống kê nguồn tri thức, Owner và chu kỳ cập nhật.

### F. Risk & Guardrail Matrix (An toàn)
- Bao gồm: **7. Guardrails & Compliance** (Cấm, Giới hạn, Bảo mật).
- Hình thức: Ma trận xử lý rủi ro (Hallucination, Leakage, Compliance).

### G. Evaluation & Monitoring Plan (Chất lượng)
- Bao gồm: **9. Evaluation & AC** (Accuracy, Latency) và **10. Logging & Monitoring** (Logs, Feedback).
- Hình thức: Kê hoạch đo lường và giám sát vận hành hệ thống.

## 3. SRS Mandatory Components
Mọi tài liệu SRS/FSD do Agent 3 soạn thảo phải bao gồm:
1. **Glossary**: Định nghĩa thuật ngữ.
2. **Detailed Functional Logic**: Logic xử lý chi tiết kèm Error Handling.
3. **Data Models**: Cấu trúc dữ liệu mẫu (JSON/Schema).
4. **Traceability Table**: Ánh xạ tới BRD và SDD.

## 2. Mermaid Diagram Rules
- Chỉ sử dụng Mermaid khi biểu đồ giúp làm rõ logic hơn văn bản.
- Sơ đồ phải đơn giản, ẩn đi các chi tiết kỹ thuật không cần thiết cho Non-tech.

## 3. Storage Rules (Bắt buộc)
- Tài liệu kinh doanh phải nằm trong `Output/[Project_Name]/BRD/`.
- Tài liệu kỹ thuật phải nằm trong `Output/[Project_Name]/Design/`.
- Các tệp của Agent 3 (**Master_Project_Index.md**, **Executive_Summary.md**, **MVP_PRD.md**, **MVP_Test_Cases.md**, **[Project_Name]_SRS.md**) phải nằm trong danh mục quản lý của Agent 3.
  - *Lưu ý*: Tệp **SRS.md** vẫn được ưu tiên lưu tại `Output/[Project_Name]/BRD/` để đồng bộ với các tài liệu đặc tả khác.

## 4. Language
- Luôn sử dụng Tiếng Việt chuyên nghiệp làm ngôn ngữ chính, thuật ngữ tiếng Anh chuyên ngành giữ nguyên hoặc mở ngoặc giải thích.
