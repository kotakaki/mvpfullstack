# Agent Portfolio Model

## Mục tiêu

Định nghĩa cách nhìn toàn cục về tất cả team và agent trong workspace.

## Cấp quản lý

### Cấp 1: Team

Mỗi team là một đơn vị quản lý riêng.

Ví dụ:
- `Agile`
- `IdeaTeam`
- `TrendTeam`
- `SaleTeam`

### Cấp 2: Agent

Mỗi team có một hoặc nhiều agent với vai trò cụ thể.

### Cấp 3: Backlog

Mỗi team có backlog riêng, và mỗi agent có thể có backlog con nếu cần.

## Nhóm portfolio nên có

- `Đang hoạt động`: agent đã tồn tại và đang vận hành
- `Đang hoàn thiện`: agent đã được tạo nhưng còn backlog mở
- `Kế hoạch tương lai`: agent chưa tạo, mới ở mức kế hoạch

## Nguyên tắc

- Không trộn backlog của nhiều team vào một danh sách duy nhất.
- Mọi backlog item phải gắn được với ít nhất một team.
- Nếu là ý tưởng tương lai, phải gắn nhãn `Kế hoạch tương lai`.
