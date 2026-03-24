# Template: Design Specs (Agent 4)

Tài liệu này là chuẩn đầu ra của Agent 4, dùng để bàn giao cho Developer hoặc để review thiết kế. Bắt buộc phải tuân theo cấu trúc dưới đây.

## 1. Design Direction & Atomic Tokens
- **Theme/Vibe**: (Ví dụ: Dark mode, Professional, Trustworthy, Kinetic Experience)
- **Color Palette**:
  - Primary: `[Mã màu]`
  - Background: `[Mã màu]`
  - Surface/Card: `[Mã màu]`
  - Text: `[Mã màu]`
- **Typography**: `[Tên Font]` (Heading sizes, Body sizes)
- **Spacing & Radius**: (Ví dụ: Base 8px, Radius 12px)

## 2. Screen Inventory (Danh sách màn hình)
Dựa trên chuỗi (User Flow) từ PRD/SRS, hệ thống cần thiết kế các màn hình cụ thể sau để đáp ứng trọn vẹn luồng người dùng:

| STT | Tên Màn Hình | Mục Đích | Trạng Thái / Biến Thể |
| :--- | :--- | :--- | :--- |
| 1 | `[Screen_Name]` | (Ví dụ: Landing page để convert user) | X |
| 2 | `[Screen_Name]` | (Ví dụ: Form nhập liệu của bước 1) | Trạng thái lỗi thiếu trường |
| 3 | `[Screen_Name]` | (Ví dụ: Loading/Processing data) | X |
| 4 | `[Screen_Name]` | (Ví dụ: Dashboard kết quả thành công) | Trống (Empty State) |
*(Bảng này phải phủ kín tất cả các bước trong User Flow, không được bỏ sót các màn hình phụ như Đang tải, Báo lỗi, hoặc Trạng thái trống).*

## 3. Hướng dẫn Tương tác (Micro-interactions)
- Mô tả các hiệu ứng quan trọng (Hover button, transition giữa các màn hình).
- Các lưu ý khi lập trình frontend để đảm bảo trải nghiệm "Glassmorphism" hoặc "Tonal Layering".

## 4. Stitch Resources
- [Link đến Collection/Dự án trên Stitch]
- Danh sách các assets đã được gen (nếu có).
