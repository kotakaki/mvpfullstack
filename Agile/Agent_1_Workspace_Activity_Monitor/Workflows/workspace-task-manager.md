# Workspace Task Manager Workflow

File này được giữ lại để tham chiếu tương thích ngược trong phạm vi `Agent 1`.

Từ phiên bản hiện tại, `Agile` đã được tái định nghĩa thành `Agile Team` gồm 3 agent:

1. `Agent 1`: theo dõi hoạt động toàn workspace
2. `Agent 2`: thư ký tóm tắt và lưu log
3. `Agent 3`: daily summary và weekly summary

Nếu cần workflow mới, ưu tiên đọc:

- [Workspace_Monitoring_Workflow.md](./Workspace_Monitoring_Workflow.md)
- [Activity_Logging_Workflow.md](../../Agent_2_Workspace_Secretary/Workflows/Activity_Logging_Workflow.md)
- [Daily_Summary_Workflow.md](../../Agent_3_Summary_Reporter/Workflows/Daily_Summary_Workflow.md)
- [Weekly_Summary_Workflow.md](../../Agent_3_Summary_Reporter/Workflows/Weekly_Summary_Workflow.md)

## Vai trò cũ của file này

Nó từng được dùng để quản lý task theo Epic/Story ở cấp workspace.
Hiện nay, nội dung này được chia lại:

- phát hiện thay đổi: Agent 1
- ghi log hoạt động: Agent 2
- tổng hợp theo chu kỳ: Agent 3
