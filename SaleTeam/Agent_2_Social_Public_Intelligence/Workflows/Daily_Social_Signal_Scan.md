# Quy trình: Quét tín hiệu social hằng ngày

1. Nhận watchlist ưu tiên trong ngày và lọc ra các profile đến hạn theo `Watch_Tier_and_Cadence_Model.md`.
2. Nếu profile chưa có baseline:
   - tạo baseline trước
   - gắn `Ngày baseline gần nhất`
   - không coi vòng đầu là `thay đổi profile`
3. Rà các bài đăng mới, thay đổi hồ sơ, tín hiệu tuyển dụng, ra mắt, khen ngợi, phàn nàn và hoạt động sự kiện trong 24 giờ gần nhất.
4. So sánh profile hiện tại với baseline gần nhất nếu baseline đã tồn tại từ trước.
5. Ghi riêng:
   - `Quan sát được`
   - `Thay đổi profile`
   - `Hàm ý có thể có`
6. Chấm `Độ mạnh tín hiệu`, `Độ mới`, `Ưu tiên tín hiệu` theo `Social_Priority_Model.md`.
7. Cập nhật tín hiệu cũ hoặc tạo tín hiệu mới theo `Signal_Update_and_Dedup_Rule.md`.
8. Cập nhật `Nhật ký thay đổi profile` nếu có khác biệt đáng kể.
9. Cập nhật metadata ở cấp profile:
   - `Ngày quét gần nhất`
   - `Ngày quét tiếp theo`
   - `Lần có thay đổi profile gần nhất` nếu có
10. Cập nhật `Trạng thái theo dõi`, `Có cần follow-up không` và `Ngày quét tiếp theo cấp account`.
11. Ghi rõ profile hoặc account nào cần follow-up ngay trong ngày và vì sao.
