# Quy trình: Quét nguồn lead hằng ngày

1. Nhận watchlist nguồn hoặc gói nguồn mới cần theo dõi trong ngày.
2. Kiểm tra nguồn nào có bản ghi mới hoặc thay đổi đáng chú ý.
3. Trích xuất nhanh các lead mới có đủ trường tối thiểu để nhận diện.
4. Chuẩn hóa các trường dữ liệu cơ bản, gắn `Mã bản ghi` nếu cần và ghi rõ nguồn.
5. Cập nhật metadata vận hành cho từng bản ghi:
   - `Batch / run nguồn`
   - `Ngày thêm vào run` nếu là lead mới
   - `Ngày cập nhật gần nhất`
   - `Nguồn scan gần nhất`
6. Đánh dấu `Chưa xác minh` hoặc `Có thể trùng` nếu chưa đủ chắc chắn.
7. Nếu hợp nhất bản ghi trùng, giữ `Mã bản ghi` chính và cập nhật `Mã trùng đã gộp`.
8. Bổ sung vào `01_Lead_List.md` của run đang theo dõi hoặc tạo run mới nếu là nhóm nguồn mới.
9. Ghi rõ ngày quét, số lượng lead mới và các điểm cần rà lại trong ngày tiếp theo.
