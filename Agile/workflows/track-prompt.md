---
description: Theo dõi prompt, cập nhật log và gửi thông báo Google Chat
---

# Track Prompt Workflow

Đây là workflow chính để triển khai việc theo dõi (track) prompt từ hệ thống:

1. **Nhận Prompt:**
   - Hệ thống trigger khi người dùng gõ vào một prompt mới.

2. **Xử lý tóm tắt (Activity):**
   - Áp dụng kỹ năng Thư ký (Secretary) để tóm tắt nội dung của prompt.

3. **Cập nhật Log:**
   - **Lưu raw prompt**: Nối (append) raw prompt vào file `.agent/knowledge/prompt_history.md`. Bạn có thể sử dụng tool ghi file hoặc lệnh bash (ví dụ: `echo "... " >> .agent/knowledge/prompt_history.md`).
   - **Lưu activity**: Nối (append) activity summary vào file `.agent/knowledge/activity_history.md`.

4. **Gửi Google Chat (Webhook):**
   - Đọc URL Webhook từ file `.agent/config/webhook.txt`.
   - Dùng lệnh `curl` (qua `run_command`) để gửi thông báo tóm tắt hoạt động lên Google Chat, báo cho người dùng hoặc nhóm rằng đã có một tác vụ mới.
   - Ví dụ lệnh:
     ```bash
     curl -X POST -H "Content-Type: application/json" \
          -d "{\"text\": \"[NEW PROMPT ACTIVITY] - <Nội dung tóm tắt>\"}" \
          "<URL_WEBHOOK>"
     ```