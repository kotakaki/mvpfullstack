# Quy tắc: Yêu cầu đầu vào cho danh sách

## Mục tiêu
Chuẩn hóa cách người dùng đưa danh sách đầu vào để `SaleTeam` có thể quét và làm giàu thông tin nhất quán.

## Định dạng chấp nhận
- CSV
- Excel / Google Sheet
- bảng markdown
- danh sách dán trực tiếp trong chat

## Trường tối thiểu nên có
- `Tên công ty` hoặc `Tên người`
- `Nguồn`
- một trường nhận diện để quét tiếp, ưu tiên một trong các trường sau:
  - `Website công ty`
  - `Domain`
  - `LinkedIn`
  - `URL hồ sơ social`

## Trường khuyến nghị
- `Mã bản ghi`
- `Tên người`
- `Tên công ty`
- `Vai trò`
- `Website công ty`
- `LinkedIn / hồ sơ`
- `Khu vực`
- `Nguồn`
- `Ghi chú`

## Quy tắc
- Nếu người dùng chưa có `Mã bản ghi`, Agent 1 sẽ tự sinh cho mọi bản ghi.
- Nếu một dòng không có đủ trường nhận diện để quét tiếp, phải đánh dấu `Thiếu dữ liệu để làm giàu`.
- Không tự suy diễn website hoặc hồ sơ social nếu danh sách gốc không có đủ bằng chứng.

## Mẫu `00_Input_List.md`

```md
# 00_Input_List - <run_name>

## Bối cảnh
- Người cung cấp:
- Mục tiêu làm giàu:
- Ngày nhận:

## Bản ghi 01
- Mã bản ghi:
- Tên người:
- Tên công ty:
- Vai trò:
- Website công ty:
- LinkedIn / hồ sơ:
- Khu vực:
- Nguồn:
- Ghi chú:
```
