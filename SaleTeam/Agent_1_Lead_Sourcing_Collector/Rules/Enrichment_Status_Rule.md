# Quy tắc: Trạng thái enrichment

## Mục tiêu
Giúp Agent 1 và các bước downstream theo dõi được vòng đời xử lý của từng bản ghi.

## Trường nên có
- `Trạng thái enrichment`

## Giá trị khuyến nghị
- `Chưa quét`
- `Đang quét`
- `Đã enrich`
- `Thiếu dữ liệu`
- `Cần rà tay`
- `Tạm dừng`

## Cách dùng
- `Chưa quét`: bản ghi mới nhận, chưa đi qua Agent 2 hoặc Agent 3
- `Đang quét`: đã định tuyến và đang trong quá trình làm giàu
- `Đã enrich`: đã có đủ output cần thiết theo ma trận định tuyến và mục tiêu run
- `Thiếu dữ liệu`: không đủ trường nhận diện để tiếp tục
- `Cần rà tay`: có xung đột, trùng lặp hoặc kết quả không rõ
- `Tạm dừng`: người dùng chưa muốn xử lý tiếp bản ghi này

## Quy tắc chốt `Đã enrich`
- Nếu `Chuyển Agent 2 = Có` và `Chuyển Agent 3 = Có`:
  - chỉ đánh dấu `Đã enrich` khi đã có đủ output từ cả Agent 2 và Agent 3, hoặc mục tiêu run ghi rõ chỉ cần một nhánh
- Nếu chỉ một trong hai agent được định tuyến là `Có`:
  - chỉ cần output từ agent đó để được coi là `Đã enrich`
- Nếu cả `Chuyển Agent 2` và `Chuyển Agent 3` đều là `Không`:
  - chỉ đánh dấu `Đã enrich` khi Agent 1 xác nhận bản ghi đã đủ dùng theo mục tiêu run mà không cần làm giàu thêm
- Nếu một nhánh là `Thiếu dữ liệu`:
  - không được dùng trạng thái `Đã enrich hoàn chỉnh`; phải giữ `Thiếu dữ liệu`, `Đang quét` hoặc ghi rõ phạm vi đã enrich

## Quy tắc
- Mỗi bản ghi trong `01_Lead_List.md` nên có một trạng thái enrichment rõ ràng.
- Khi tạo `04_Enriched_Record_Summary.md`, chỉ những bản ghi `Đã enrich` mới nên có phần tổng hợp hoàn chỉnh.
