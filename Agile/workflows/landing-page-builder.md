---
description: Tự động dựng Landing Page, lưu file yêu cầu, sinh HTML và thông báo kết quả.
---

# Landing Page Auto Builder Workflow

Khi người dùng gửi tin nhắn chứa các keyword có điều kiện kích hoạt, AI sẽ tự động thực hiện các bước sau:

### 1. Phân tích yêu cầu
- Đọc nội dung tin nhắn của người dùng để hiểu mục tiêu của landing page.
- Phân tích các yếu tố cần thiết:
  - Mục đích landing page
  - Nội dung chính
  - CTA (Call To Action)
  - Bố cục các section
  - Yêu cầu kỹ thuật hoặc thiết kế nếu có.

### 2. Tạo thư mục kết quả
- Dựa trên system timestamp lúc người dùng gửi yêu cầu (định dạng `YYYYMMDD-HHMM`), tạo một folder mới trong thư mục `.agent/results/`.
  Cấu trúc tên: `.agent/results/landingpage-YYYYMMDD-HHMM`

### 3. Sinh file kết quả
Trong folder vừa tạo, AI sinh các file sau:

**1. landingpage.html**
- Landing page hoàn chỉnh bằng HTML.
- Có cấu trúc rõ ràng (header, hero, section, CTA, footer).
- Code sạch, dễ chỉnh sửa và tuân thủ các quy tắc thiết kế cơ bản nếu không được chỉ định thêm.

**2. requirements-analysis.md**
- File phân tích yêu cầu.
- Bao gồm:
  - Tóm tắt yêu cầu từ prompt.
  - Phân tích cấu trúc landing page.
  - Danh sách section.
  - Nội dung gợi ý cho từng section.

### 4. Ghi log workflow
- Ghi log toàn bộ quá trình vào hệ thống log (theo các file log hiện có của hệ thống `activity_history.md` / `prompt_history.md` nếu phù hợp).
- Format log mô tả rõ ràng:
  - Task bắt đầu
  - Phân tích yêu cầu
  - Tạo folder
  - Sinh file
  - Hoàn thành.

### 5. Gửi thông báo Google Chat
- Đọc URL webhook (nếu không có sẵn, mặc định từ `.agent/config/webhook.txt`).
- Sau khi hoàn thành, sử dụng webhook để gửi message lên Google Chat theo mẫu:

```text
[AI WORKFLOW] Landing Page Generated

Result Folder: /.agent/results/landingpage-YYYYMMDD-HHMM

Files Created:
- landingpage.html
- requirements-analysis.md

Status: Completed
```

### 6. Điều kiện kích hoạt
Workflow chỉ chạy khi message nhận vào có chứa một trong các keyword sau (không phân biệt chữ hoa, chữ thường):
- "dựng landingpage"
- "create landing page"
- "build landing page"
