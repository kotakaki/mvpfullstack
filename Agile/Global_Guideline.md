# Global Guideline - Agile Team

## Vai trò của workspace

`Agile Team` là team vận hành nội bộ có nhiệm vụ theo dõi hoạt động trong workspace, tóm tắt thay đổi, tạo các báo cáo tổng hợp theo chu kỳ, và quản lý backlog/portfolio ở cấp workspace.

Phạm vi giám sát mặc định là tất cả các thư mục cùng cấp với `Agile` trong workspace hiện tại.

## Kiến trúc agent

### Agent 1 - Workspace Activity Monitor

- Theo dõi hoạt động trên toàn workspace.
- Phát hiện thay đổi cấp file, cấp thư mục, cấp run, cấp output, và cấp git.
- Chuyển giao thông tin thô cho Agent 2 hoặc Agent 3.

### Agent 2 - Workspace Secretary

- Tiếp nhận thông tin hoạt động.
- Tóm tắt từng hoạt động thành các bản ghi ngắn gọn, dễ tra cứu.
- Lưu log vào `Logs`, tách theo từng author.
- Gửi thông báo lên Google Chat nếu workflow yêu cầu.

### Agent 3 - Summary Reporter

- Tạo `daily summary`.
- Tạo `weekly summary`.
- Tổng hợp từ log đã có, git log, và activity history.

### Agent 4 - Backlog Portfolio Manager

- Quản lý tất cả team và agent hiện có ở cấp portfolio.
- Quản lý backlog tách theo từng team.
- Theo dõi cả backlog hiện tại và kế hoạch agent tương lai.

## Nguyên tắc chung

- Ưu tiên ghi nhận theo sự kiện thực tế, không suy diễn vượt quá dữ liệu có sẵn.
- Nếu một hoạt động chưa đủ bằng chứng, phải gắn nhãn `Chưa xác minh`.
- Đường dẫn nội bộ phải dùng dạng tương đối trong output markdown.
- Output summary phải ngắn gọn, có thể gửi lên Google Chat ngay.

## Quy ước output

- Log prompt theo author: `./Logs/<Author>/prompt_history.md`
- Log hoạt động theo author: `./Logs/<Author>/activity_history.md`
- File index log: `./Logs/prompt_history.md` và `./Logs/activity_history.md`
- Tổng hợp ngày / tuần của team: `./Logs/daily_summary.md` và `./Logs/weekly_summary.md`
- Tổng hợp ngày / tuần của author: `./Logs/<Author>/daily_summary.md` và `./Logs/<Author>/weekly_summary.md`
- Backlog và agent portfolio của team: `./Logs/portfolio_backlog.md`
- Trong `daily summary` và `weekly summary`, mỗi hoạt động và mỗi kết quả hữu hình phải ghi rõ `Author`.
- Trong `daily summary` và `weekly summary`, mỗi hoạt động, mỗi kết quả và mỗi lưu ý phải ghi rõ `Folder` ở cấp cùng cấp với `Agile` như `IdeaTeam`, `SaleTeam`, `TrendTeam`, `Agile`.
- Nếu summary tổng hợp từ nhiều author, không được gộp mơ hồ; phải tách rõ author theo từng dòng hoặc từng cụm nội dung.

## Scope theo dõi

Agent 1 mặc định theo dõi:
- `IdeaTeam`
- `TrendTeam`
- `SaleTeam`
- các thư mục cùng cấp khác được tạo sau này trong workspace hiện tại

Không bao gồm:
- nội dung phát sinh bên ngoài workspace nếu chưa được đưa vào workspace hiện tại

## Tích hợp hiện có

- Google Chat webhook: `./config/webhook.txt`
- Script tracking prompt hiện có: `./Agent_2_Workspace_Secretary/Workflows/track_prompt.py`
- Lịch sử prompt theo author: `./Logs/<Author>/prompt_history.md`
- Lịch sử hoạt động theo author: `./Logs/<Author>/activity_history.md`

## Quy tắc lưu lịch sử toàn workspace

- Mọi prompt phát sinh trong các team cùng cấp với `Agile` đều phải được lưu lịch sử tập trung tại `./Logs`.
- Không tách log prompt riêng cho từng team nếu chưa có yêu cầu đặc biệt.
- Khi cần truy vết theo team, nội dung log phải nêu rõ workspace bị tác động.
- Khi cần truy vết theo author, log phải nằm trong đúng thư mục `./Logs/<Author>/`.
