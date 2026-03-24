# Quy tắc: Mẫu danh sách lead

`01_Lead_List.md` nên dùng cấu trúc sau:

```md
# 01_Lead_List - <run_name>

## Bối cảnh
- Gói nguồn:
- ICP mục tiêu:
- Ngày thu thập:

## Lead 01
- Mã bản ghi:
- Batch / run nguồn:
- Ngày thêm vào run:
- Ngày cập nhật gần nhất:
- Nguồn scan gần nhất:
- Tên trong danh sách gốc:
- Loại lead:
- Tên người:
- Tên công ty:
- Vai trò / chức năng:
- Khu vực:
- Website công ty:
- LinkedIn / hồ sơ:
- Nguồn:
- Lý do đưa vào:
- Độ phù hợp ICP:
- Trạng thái xác minh:
- Trạng thái enrichment:
- Mã trùng đã gộp:
- Chuyển Agent 2:
- Chuyển Agent 3:
- Ghi chú:
```

## Quy tắc
- `Mã bản ghi` là trường bắt buộc nếu run bắt đầu từ danh sách người dùng cung cấp.
- `Batch / run nguồn` giúp truy ngược lead về đúng đợt quét hoặc gói nguồn.
- `Ngày thêm vào run` và `Ngày cập nhật gần nhất` giúp vận hành daily/weekly scan.
- `Nguồn scan gần nhất` nên ghi rõ nguồn hoặc batch vừa chạm vào bản ghi.
- `Loại lead` nên dùng `Cá nhân` hoặc `Công ty`.
- `Độ phù hợp ICP` nên tham chiếu `ICP_Fit_Scoring_Model.md`.
- `Trạng thái enrichment` nên tham chiếu `Enrichment_Status_Rule.md`.
- `Mã trùng đã gộp` dùng để lưu các mã phụ đã hợp nhất vào `Mã bản ghi` chính.
- `Lý do đưa vào` là trường bắt buộc.
- `Trạng thái xác minh` nên dùng:
  - `Đã xác minh`
  - `Chưa xác minh`
  - `Có thể trùng`
- `Chuyển Agent 2` và `Chuyển Agent 3` nên dùng:
  - `Có`
  - `Không`
  - `Thiếu dữ liệu`
