# Logs

Thư mục này lưu log vận hành của `Agile Team`.

## Cấu trúc

- `./prompt_history.md`: file chỉ mục cho lịch sử prompt theo author.
- `./activity_history.md`: file chỉ mục cho lịch sử hoạt động theo author.
- `./<Author>/prompt_history.md`: lịch sử prompt của một author cụ thể.
- `./<Author>/activity_history.md`: lịch sử hoạt động của một author cụ thể.
- `./daily_summary.md`: tổng hợp ngày dùng chung của team.
- `./weekly_summary.md`: tổng hợp tuần dùng chung của team.
- `./portfolio_backlog.md`: backlog và portfolio dùng chung của team.
- `./<Author>/daily_summary.md`: tổng hợp ngày riêng của author.
- `./<Author>/weekly_summary.md`: tổng hợp tuần riêng của author.

## Nguyên tắc

- Mỗi prompt đều phải được ghi vào thư mục author tương ứng.
- Mỗi prompt cũng phải có một bản tóm tắt hoạt động tương ứng trong cùng thư mục author đó.
- Các file ở root `Logs` chỉ đóng vai trò điều hướng hoặc tổng hợp dùng chung.
- Log được lưu ở đây thay vì `knowledge/` để tách rõ giữa `tri thức` và `nhật ký vận hành`.
