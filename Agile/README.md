# Agile Team

`Agile` được tái định nghĩa thành một workspace `Agile Team` có 4 agent phối hợp để giám sát, ghi nhận, tổng hợp hoạt động, và quản lý backlog/portfolio trong toàn bộ workspace.

## Cấu trúc team

1. `Agent_1_Workspace_Activity_Monitor`
   - Giám sát hoạt động trên các thư mục cùng cấp với `Agile`.
   - Phát hiện thay đổi, run mới, file mới, commit mới, và các sự kiện cần theo dõi.

2. `Agent_2_Workspace_Secretary`
   - Tóm tắt từng hoạt động.
   - Lưu log, cập nhật lịch sử hoạt động, và gửi thông báo khi cần.

3. `Agent_3_Summary_Reporter`
   - Tạo `daily summary`.
   - Tạo `weekly summary`.
   - Đóng gói output để gửi Google Chat hoặc lưu nội bộ.

4. `Agent_4_Backlog_Portfolio_Manager`
   - Quản lý tất cả team và agent hiện có ở cấp `agent portfolio`.
   - Quản lý backlog phân chia cụ thể theo từng team.
   - Theo dõi cả backlog hiện có và kế hoạch agent tương lai.

## Mục tiêu

- Theo dõi được hoạt động trong toàn bộ workspace.
- Có log tóm tắt nhất quán cho từng hoạt động quan trọng.
- Tạo được báo cáo ngày và báo cáo tuần có thể tái sử dụng.

## Nguyên tắc vận hành

- Ưu tiên ghi nhận đúng sự kiện và đúng phạm vi.
- Nếu thông tin chưa đủ để tóm tắt chính xác, phải ghi rõ `Chưa xác minh`.
- Chỉ đề xuất mở rộng phạm vi hoặc hành động tiếp theo khi người dùng yêu cầu.

## Điều hướng nhanh

- [Global_Guideline.md](./Global_Guideline.md)
- [Master_Index.md](./Master_Index.md)
- [Agent_1_Workspace_Activity_Monitor](./Agent_1_Workspace_Activity_Monitor)
- [Agent_2_Workspace_Secretary](./Agent_2_Workspace_Secretary)
- [Agent_3_Summary_Reporter](./Agent_3_Summary_Reporter)
- [Agent_4_Backlog_Portfolio_Manager](./Agent_4_Backlog_Portfolio_Manager)
- [Logs](./Logs)
- [config](./config)
