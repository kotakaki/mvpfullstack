# Quy tắc: Mã bản ghi và bàn giao

## Mục tiêu
Giữ cho mọi output của `SaleTeam` truy ngược được về đúng dòng trong danh sách gốc.

## Nguyên tắc
- Mỗi dòng trong danh sách đầu vào phải có một `Mã bản ghi` ổn định.
- `Mã bản ghi` phải được giữ nguyên khi đi qua Agent 1, Agent 2 và Agent 3.
- Mọi output làm giàu đều phải tham chiếu lại `Mã bản ghi`.

## Cách dùng
- Nếu danh sách gốc đã có `Mã bản ghi`, giữ nguyên.
- Nếu chưa có, Agent 1 sinh mã theo run, ví dụ:
  - `RID-001`
  - `RID-002`
- Nếu hai dòng được xác định là trùng nhau:
  - giữ một `Mã bản ghi` chính
  - ghi mã còn lại vào `Mã trùng đã gộp`

## Quy tắc với run một bản ghi
- Dù danh sách chỉ có một dòng, vẫn phải có `Mã bản ghi`.
- Không được bỏ `Mã bản ghi` chỉ vì cho rằng chưa cần bàn giao downstream.

## Bắt buộc khi bàn giao
- Agent 1 sang Agent 2 và Agent 3 phải có:
  - `Mã bản ghi`
  - `Tên bản ghi gốc`
  - `Website` hoặc `LinkedIn / hồ sơ` nếu có
  - trạng thái xác minh hiện tại

## Không được làm
- Không đổi `Mã bản ghi` ở giữa các bước.
- Không tạo output của Agent 2 hoặc Agent 3 mà thiếu `Mã bản ghi`.
- Không làm mất lịch sử hợp nhất của các mã trùng sau khi đã loại trùng.
