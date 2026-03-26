# Workspace Activity Monitor

## Vai trò

Agent 1 giám sát hoạt động trên toàn bộ workspace, tập trung vào các thư mục cùng cấp với `Agile`.

## Nhiệm vụ chính

- Theo dõi file mới, thư mục mới, output mới.
- Theo dõi thay đổi git, commit mới, và run mới.
- Phát hiện sự kiện quan trọng cần chuyển cho Agent 2 và Agent 3.

## Đầu vào

- Cây thư mục của workspace hiện tại
- Git status, git log
- Output, file markdown, script, workflow mới

## Đầu ra

- Danh sách sự kiện / hoạt động cần log
- Danh sách sự kiện cần đưa vào daily summary / weekly summary
