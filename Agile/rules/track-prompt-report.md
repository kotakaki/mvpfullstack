# Báo Cáo Nghiên Cứu: Track Prompt Workflow

## 1. Mục Đích & Tổng Quan
Workflow `track-prompt` ra đời nhằm mục đích tự động theo dõi, phân tích và hệ thống hóa mọi đầu vào (prompt) từ phía người sử dụng. Bằng việc lưu trữ dấu vết và gửi thông báo, workflow đảm bảo quá trình giao tiếp với AI luôn có tính kế thừa, minh bạch và có thể tra cứu khi cần (audit/traceability).

## 2. Luồng Hoạt Động (Flow)
Workflow này tự động chạy nền mỗi khi hệ thống nhận được một prompt mới. Chu trình được định hình chuẩn với 4 giai đoạn cụ thể:
1. **Tiếp nhận Prompt**: Trigger hệ thống.
2. **Xử lý Tóm tắt**: Phân tích nội dung.
3. **Cập nhật Log**: Lưu trữ thông tin.
4. **Thông báo Webhook**: Cảnh báo theo thời gian thực (real-time notification).

## 3. Cách Thức Thực Hiện & Các Thao Tác Chi Tiết

### Bước 1: Tiếp nhận Prompt
- **Cơ chế**: Dựa vào hành vi nhập liệu của người dùng, hệ thống sinh ra sự kiện (event) để kích hoạt toàn bộ workflow mà không cần can thiệp thủ công.
- **Thao tác**: Capture dữ liệu thô (raw prompt) từ giao diện xuống backend/luồng thực thi.

### Bước 2: Xử lý tóm tắt (Activity)
- **Công cụ áp dụng**: Giao việc phân tích này cho kỹ năng *Thư ký (Secretary)*.
- **Thao tác**:
  - Lấy nguyên văn bản đầu vào.
  - Sử dụng AI để lược bỏ các từ ngữ dư thừa, rút gọn thành văn bản mô tả ngắn gọn nhất (Activity Summary) để làm nổi bật tác vụ chính cần xử lý.

### Bước 3: Cập nhật Log
Dữ liệu tại bước này được phân tách và lưu vào hai cơ sở dữ liệu dạng văn bản riêng biệt nhằm đảm bảo không bị mất đi dữ liệu sơ cấp và giúp báo cáo đọc lại gọn gàng.
- **Ghi nhật ký hệ thống (Raw Prompt)**:
  - **Mục tiêu**: Lưu lại chính xác 100% những gì người dùng yêu cầu.
  - **Tệp tin đích**: `.agent/knowledge/prompt_history.md`.
  - **Thao tác**: Thực hiện ghép nối (append) dữ liệu theo trình tự thời gian vào đuôi tệp.
- **Ghi hoạt động (Activity History)**:
  - **Mục tiêu**: Giúp con người nhanh chóng nắm được chuỗi quá trình AI đã hỗ trợ qua tóm tắt.
  - **Tệp tin đích**: `.agent/knowledge/activity_history.md`.
  - **Thao tác**: Tương tự như raw prompt, dữ liệu tóm tắt được nối thêm vào tệp dạng nhật ký thời gian.

### Bước 4: Gửi Thông Báo Google Chat (Webhook)
- **Cơ chế**: Đóng gói nội dung và đẩy liên lạc qua giao thức HTTP/POST.
- **Thao tác**:
  - Đọc chuỗi URL Webhook chuyên biệt từ tệp `.agent/config/webhook.txt`.
  - Đóng gói chuỗi JSON chứa tóm tắt prompt (Activity) theo định dạng thẻ: `[NEW PROMPT ACTIVITY] - <Nội_dung_tóm_tắt>`.
  - Kích hoạt lệnh `curl` gửi yêu cầu POST cho server của nền tảng Google Chat.
  - **Lệnh mẫu (cơ bản)**:
    ```bash
    curl -X POST -H "Content-Type: application/json" \
         -d "{\"text\": \"[NEW PROMPT ACTIVITY] - <Nội dung tóm tắt>\"}" \
         "<URL_WEBHOOK>"
    ```

## 4. Kết Luận
Quy trình theo dõi prompt trong workflow `track-prompt` tuân thủ nguyên tắc quản lý dữ liệu hiện đại qua việc bảo vệ nguyên vẹn "Source of Truth" (raw prompt) và tăng cường trải nghiệm dọc bằng một file tóm lược (activity history). Việc tự động gọi webhook tới Google Chat làm khép kín chu trình kiểm duyệt dự án.
