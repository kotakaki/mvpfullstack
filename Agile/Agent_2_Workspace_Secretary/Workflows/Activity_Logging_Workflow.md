# Activity Logging Workflow

1. Nhận danh sách sự kiện từ Agent 1.
2. Tóm tắt từng sự kiện thành activity log ngắn gọn.
3. Xác định author của prompt.
4. Lưu lịch sử prompt vào `./Logs/<Author>/prompt_history.md`.
5. Lưu tóm tắt hoạt động vào `./Logs/<Author>/activity_history.md`.
6. Nếu sự kiện quan trọng, tạo bản tóm tắt ngắn để gửi lên Google Chat.
7. Chuyển thông tin đã chuẩn hóa cho Agent 3 nếu cần đưa vào summary.
8. Khi cần ghi log tự động, dùng script `./track_prompt.py`.
