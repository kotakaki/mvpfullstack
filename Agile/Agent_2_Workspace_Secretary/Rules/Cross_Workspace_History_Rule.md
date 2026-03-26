# Cross Workspace History Rule

## Mục tiêu

Đảm bảo mọi prompt phát sinh trong các folder cùng cấp với `Agile` đều được lưu lịch sử tập trung tại `./Logs`.

## Phạm vi áp dụng

- `IdeaTeam`
- `TrendTeam`
- `SaleTeam`
- `Agile`
- các folder cùng cấp khác trong workspace hiện tại

## Rule

1. Không tạo một hệ log prompt riêng tách biệt ở từng team nếu chưa có yêu cầu đặc biệt.
2. Lịch sử prompt toàn workspace phải được gom về:
   - `./Logs/<Author>/prompt_history.md`
   - `./Logs/<Author>/activity_history.md`
3. Mỗi bản ghi trong `activity_history.md` phải nêu rõ `Folder` ở cấp cùng cấp với `Agile`.
4. Nếu prompt diễn ra trong folder khác, phần `Activity Summary` và `Result / Output` phải bám đúng folder đó, không ghi mơ hồ là `workspace`.
5. Nếu cần summary theo team, Agent 3 sẽ tổng hợp lại từ log chung, không tách nguồn log gốc.
