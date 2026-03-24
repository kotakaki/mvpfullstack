# Quy trình: Phân tích thông tin công khai trên mạng xã hội

1. Nhận watchlist và kiểm tra đầu vào theo `Watchlist_Input_Requirements.md`.
2. Map đầy đủ các hồ sơ cần theo dõi theo `Tracked_Profile_Coverage_Rule.md`.
3. Gắn `Profile ID`, `Watch tier` và nhịp quét theo `Watch_Tier_and_Cadence_Model.md`.
4. Tạo hoặc rà baseline cho từng hồ sơ theo `Profile_Baseline_Template.md`.
5. Nếu hồ sơ chưa có baseline:
   - tạo baseline trước
   - chưa ghi `thay đổi profile` cho vòng đầu
6. Thu thập tín hiệu theo `Public_Signal_Taxonomy.md`.
7. Tách rõ:
   - `Quan sát được`
   - `Hàm ý có thể có`
   - `Thay đổi profile`
8. Ghi change log profile theo `Profile_Change_Log_Rule.md`.
9. Đánh giá `Độ mạnh tín hiệu`, `Độ mới`, `Mức tin cậy` và `Ưu tiên tín hiệu` theo `Social_Priority_Model.md`.
10. Cập nhật hoặc gộp tín hiệu theo `Signal_Update_and_Dedup_Rule.md`.
11. Tạo `Tóm tắt cấp account` theo `Account_Care_Summary_Template.md`.
12. Ghi `Bối cảnh follow-up gần nhất` nếu có theo `Followup_Feedback_Context_Template.md`.
13. Cập nhật metadata ở cấp profile:
   - `Ngày quét gần nhất`
   - `Ngày quét tiếp theo`
   - `Ngày baseline gần nhất`
   - `Lần có thay đổi profile gần nhất`
14. Cập nhật metadata ở cấp account:
   - `Mức ưu tiên account`
   - `Có cần follow-up không`
   - `Ngày quét tiếp theo cấp account`
15. Tạo hoặc cập nhật `02_Public_Customer_Intelligence.md`.
