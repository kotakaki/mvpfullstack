# Test Scenarios - Agile Team

## Mục tiêu

Kiểm tra xem `Agile Team` đã lưu được lịch sử prompt và lịch sử hoạt động đúng như thiết kế hay chưa.

Đồng thời xác minh cơ chế tracking này áp dụng được cho các team khác trong workspace như `IdeaTeam`, `TrendTeam`, `SaleTeam`.

## Kịch bản kiểm thử chính

### AG-LOG-01: Ghi lịch sử prompt cơ bản

- Bối cảnh: người dùng gửi một prompt bất kỳ trong workspace.
- Bước kiểm tra:
  1. Tạo `activity_summary`.
  2. Gọi `./Agent_2_Workspace_Secretary/Workflows/track_prompt.py`.
  3. Kiểm tra `./Logs/<Author>/prompt_history.md`.
- Kết quả mong đợi:
  - Có thêm một bản ghi mới trong `prompt_history.md` của author tương ứng.
  - Bản ghi có `Prompt Author`, `Prompt Content`, `Status`.

### AG-LOG-02: Ghi lịch sử hoạt động tương ứng

- Bối cảnh: sau khi một prompt được xử lý xong.
- Bước kiểm tra:
  1. Gọi `./Agent_2_Workspace_Secretary/Workflows/track_prompt.py` với đủ 4 tham số.
  2. Kiểm tra `./Logs/<Author>/activity_history.md`.
- Kết quả mong đợi:
  - Có thêm một bản ghi mới trong `activity_history.md` của author tương ứng.
  - Bản ghi có `Prompt Content`, `Activity Summary`, `Result / Output`, `Status`.

### AG-LOG-03: Đồng bộ 1 prompt -> 2 log

- Bối cảnh: cùng một prompt được tracking đầy đủ.
- Bước kiểm tra:
  1. Ghi log bằng script tracking.
  2. So sánh timestamp mới nhất giữa `./Logs/<Author>/prompt_history.md` và `./Logs/<Author>/activity_history.md`.
- Kết quả mong đợi:
  - Cả hai file đều có bản ghi mới tương ứng cùng mốc thời gian.

### AG-LOG-04: Áp dụng được cho workspace khác

- Bối cảnh: người dùng đang thao tác trong `IdeaTeam`, `TrendTeam`, hoặc `SaleTeam`.
- Bước kiểm tra:
  1. Thực hiện một prompt trong workspace đó.
  2. Gọi tracking rule toàn cục.
  3. Kiểm tra `./Logs/<Author>`.
- Kết quả mong đợi:
  - Log vẫn được lưu tại `./Logs/<Author>`.
  - Nội dung prompt thể hiện đúng hoạt động của workspace tương ứng.

### AG-LOG-05: Chỉ lưu vào Logs hiện tại

- Bối cảnh: hệ thống tracking đã được chuyển hoàn toàn sang `Logs`.
- Bước kiểm tra:
  1. Chạy một lượt tracking mới.
  2. Kiểm tra `./Logs/<Author>/prompt_history.md` và `./Logs/<Author>/activity_history.md`.
  3. Kiểm tra cây thư mục `Agile` để xác nhận không còn hệ log prompt song song ngoài `Logs/<Author>`.
- Kết quả mong đợi:
  - Bản ghi mới xuất hiện trong `./Logs/<Author>/prompt_history.md`.
  - Bản ghi mới xuất hiện trong `./Logs/<Author>/activity_history.md`.
  - Không tồn tại thêm một hệ log prompt song song ngoài `./Logs/<Author>`.

## Smoke Test đề xuất

Nên chạy tối thiểu 3 kịch bản sau:

1. `AG-LOG-01`
2. `AG-LOG-02`
3. `AG-LOG-04`

## Kết quả test nên lưu

Khi chạy test chính thức, nên tạo một run riêng trong `./Logs` gồm:

- `01_Test_Plan.md`
- `02_Test_Result.md`
- `03_Test_Summary.md`
