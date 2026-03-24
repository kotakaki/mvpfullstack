# Rule: Data Focus & Ethics (Tập trung & Đạo đức Dữ liệu)

Quy tắc hướng dẫn `LearnAgent` cách chọn lọc nội dung cần đọc và tránh vi phạm ranh giới an toàn.

## 1. Trọng tâm dữ liệu (Focus)
- Chỉ quét và lấy dữ liệu liên quan đến:
  - Bản chất sản phẩm (Product Nature).
  - Tính năng và năng lực (Features & Capabilities).
  - Mô hình kinh doanh / Giá cả (Pricing / Business Model).
  - Tệp khách hàng mục tiêu (Target Audience / Use cases).
- **Bỏ qua**: Bài viết blog dài dòng (trừ khi là Case Study), chính sách bảo mật, điều khoản sử dụng, thông tin liên hệ tĩnh.

## 2. Loại trừ PII (Hành vi an toàn)
- Không được cố gắng thu thập, trích xuất hoặc ghi nhận thông tin nhận dạng cá nhân (PII) của bất kỳ cá nhân nào xuất hiện trên trang (ví dụ: email, số điện thoại của nhân viên công ty).
- Nếu trang web có hiển thị Testimonial, chỉ trích xuất chức danh công việc/ngành nghề (Title/Industry) và nội dung review, KHÔNG lưu tên riêng cụ thể.

## 3. Không vượt rào bảo mật
- Khi được yêu cầu học từ một URL, chỉ được phép đọc và tương tác với các nội dung công khai (Public facing content).
- Từ chối mọi yêu cầu quét nội dung nằm sau màn hình đăng nhập (Login/Paywall).
