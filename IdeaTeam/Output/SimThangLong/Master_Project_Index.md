# Master Project Index: Nền tảng E-commerce Sim Thăng Long

Dự án này là kết quả trích xuất tự động (Reverse-engineering) từ website thực tế thông qua **Agent 1** và sub-agent `LearnAgent`.

## Trạng thái dự án
- [x] **Agent 1 (Idea Intake & Market Research)** - Hoàn thành (BRD, PPD, SDK)
- [x] **Agent 2 (AI Solution Architect)** - Hoàn thành (SDD)
- [x] **Agent 3 (MVP Documentation)** - Hoàn thành (SRS, PRD, Test Cases)
- [x] **Agent 4 (UI/UX Designer)** - Hoàn thành (Design Specs)

---

## Danh mục tài liệu đã sinh ra

### Thư mục: Agent 1
- **BRD (Business Requirement Document)** - (Dịch ngược luồng nghiệp vụ thực tế)
- **PPD (Product Position Document)** - (Phân tích Target Persona & Giá trị độc bản)
- **SDK (Sales Description Kit)** - (Chứa nguyên liệu Social Proof)

### Thư mục: Agent 2
- **SimThangLong_Solution_Design.md**: Kiến trúc Microservices kết hợp Elasticsearch để tăng tốc độ truy vấn +45 triệu bản ghi. Mô hình Database Schema PostgreSQL.

### Thư mục: Agent 3
- **SimThangLong_SRS.md**: Yêu cầu chức năng và giao diện kết nối bên thứ 3 (SMS).
- **SimThangLong_PRD.md**: Các Epics (Khách hàng \u0026 CSKH), Các logic lọc số và User stories chi tiết.
- **MVP_Test_Cases.md**: Bộ khung test từ Search, Checkout đến xử lý Concurrency (khóa số khi có 2 người cùng tranh mua).

### Thư mục: Agent 4
- **Design_Specs.md**: Triển khai thiết kế Mobile-First. Bảng Screen Inventory tuân thủ chuẩn mới, map trực tiếp vào User Flow giúp UI dễ dàng hiểu. Yêu cầu font Monospace cho số điện thoại.
