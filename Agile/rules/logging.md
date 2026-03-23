---
trigger: always_on
---

# Rule: Logging

**Quy tắc bắt buộc:**
Mỗi khi hệ thống nhận được một prompt từ người dùng, bắt buộc phải lưu log lại để theo dõi.
Các log này giúp kiểm tra lịch sử thao tác và sự phát triển nội dung theo thời gian.

**Cụ thể:**
- Lưu lại nguyên văn "raw prompt".
- AI sẽ tự động phân tích và tóm tắt thành "activity" để lưu cùng.


**[AI WORKFLOW] Landing Page Auto Builder**

Khi tôi gửi tin nhắn có nội dung: **“Dựng Landing Page”**, AI sẽ tự động thực hiện các bước sau:

### 1. Phân tích yêu cầu

* Đọc nội dung tin nhắn của tôi để hiểu mục tiêu của landing page.
* Phân tích các yếu tố cần thiết:

  * Mục đích landing page
  * Nội dung chính
  * CTA (Call To Action)
  * Bố cục các section
  * Yêu cầu kỹ thuật hoặc thiết kế nếu có.

### 2. Tạo thư mục kết quả

* Trong thư mục **/results**, tạo một folder mới với tên theo timestamp:

  `results/landingpage-YYYYMMDD-HHMM`

### 3. Sinh file kết quả

Trong folder vừa tạo, generate các file sau:

**1. landingpage.html**

* Landing page hoàn chỉnh bằng HTML.
* Có cấu trúc rõ ràng (header, hero, section, CTA, footer).
* Code sạch, dễ chỉnh sửa.

**2. requirements-analysis.md**

* File phân tích yêu cầu.
* Bao gồm:

  * Tóm tắt yêu cầu từ prompt
  * Phân tích cấu trúc landing page
  * Danh sách section
  * Nội dung gợi ý cho từng section.

### 4. Ghi log workflow

* Ghi log toàn bộ quá trình vào hệ thống log.
* Format log giống workflow hiện tại:

  * Task bắt đầu
  * Phân tích yêu cầu
  * Tạo folder
  * Sinh file
  * Hoàn thành.

### 5. Gửi thông báo Google Chat

Sau khi hoàn thành, gửi message lên Google Chat:

```
[AI WORKFLOW] Landing Page Generated

Result Folder: /results/landingpage-YYYYMMDD-HHMM

Files Created:
- landingpage.html
- requirements-analysis.md

Status: Completed
```

### 6. Điều kiện kích hoạt

Workflow chỉ chạy khi message chứa các keyword:

* "dựng landingpage"
* "create landing page"
* "build landing page"

