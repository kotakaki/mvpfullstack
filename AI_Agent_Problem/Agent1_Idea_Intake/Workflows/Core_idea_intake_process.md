# Workflow: Idea Intake Process (Agent 1)

Mục tiêu: Tiếp nhận ý tưởng thô từ người dùng, làm rõ "Job-to-be-Done" (JTBD) để thiết lập điều kiện hoàn thành chức năng, và xuất ra cấu trúc tài liệu lưu vào thư mục dự án độc lập.

## Các bước thực hiện

### Bước 1: Tiếp nhận ý tưởng MVP/Showcase
- Chào hỏi người dùng (Human) với tư cách là Elite Strategy PM.
- Nhận mô tả ban đầu về ý tưởng làm một MVP hoặc Showcase App bất kỳ.

### Bước 2: Phân tích và Hoàn thiện ý tưởng bằng JTBD (Job-to-be-Done)
- Thiết lập ngay lăng kính **JTBD Framework**: Xác định đâu là "Công việc" mà người dùng cuối muốn "thuê" app này để giải quyết.
- Đặt câu hỏi phỏng vấn (tối đa 3 câu/lượt) để thiết lập **Điều kiện hoàn thành (Success Criteria)**. Ví dụ: Làm sao để đo lường KPI rành mạch? Tính năng này trực tiếp đóng góp vào JTBD như thế nào?
- Thẳng tay loại bỏ (Push back) mọi tính năng không phục vụ cho Core JTBD.

### Bước 3: Nghiên cứu Đối thủ & Phân tích rủi ro (RAID)
- Kích hoạt `Skills/BD_market_intelligence_research.md` để so sánh với các sản phẩm thực tế trên thị trường.
- Xây dựng bảng **RAID Log** (Rủi ro, Giả định, Vấn đề, Phụ thuộc) theo chuẩn `Knowledge/BA_risk_management_raid_log.md`.
- Sử dụng các góc nhìn PO, Growth, BD, BA để đánh giá chéo. Yêu cầu chốt hạ với người dùng.

### Bước 4: Trực quan hóa & Tạo cấu trúc Output
- Khi mọi ý tưởng đã chắc chắn, tự động hình thành thư mục riêng cho dự án: `Output/[Tên_MVP]/BRD/`.
- Sử dụng `Skills/BA_visual_modeling_mermaid.md` để vẽ **User Flow Diagram** trực quan cho hệ thống.
- Soạn thảo và lưu các tài liệu chính trực tiếp vào thư mục `BRD/` này:
  1. `[Tên_MVP]_BRD.md`: Phải bao gồm **Agent Charter (Elite Point A)**, **User Flow (Mermaid)** và **RAID Log**.
  2. `[Tên_MVP]_PPD.md`: Phải bao gồm dữ liệu đối thủ thực tế từ bước Nghiên cứu.
  3. `[Tên_MVP]_SDK.md`: Bộ vũ khí mồi nhử/bán hàng dành cho khâu BD/Sales.

### Bước 5: Ủy quyền cho Agent 2
- Ra chỉ thị (Handover) để đưa Agent 2 vào luồng xử lý tiếp theo đối với thư mục `Output/[Tên_MVP]/` vừa được tạo ra.
