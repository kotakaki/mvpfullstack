# Quy trình: Quét thông tin social hằng tuần

1. Tổng hợp toàn bộ tín hiệu social và thay đổi profile đã ghi nhận trong tuần theo từng account.
2. Rà lại mức độ đầy đủ coverage theo `Tracked_Profile_Coverage_Rule.md`.
3. Gộp tín hiệu lặp lại theo `Signal_Update_and_Dedup_Rule.md`.
4. Loại bỏ tín hiệu yếu, tín hiệu đã cũ hoặc tín hiệu không còn liên quan.
5. Chấm lại `Mức ưu tiên account` và `Watch tier` theo `Social_Priority_Model.md` và `Watch_Tier_and_Cadence_Model.md`.
6. Đánh giá từng change log theo `Baseline_Update_Decision_Rule.md`.
7. Chỉ cập nhật baseline cho các profile thỏa rule cập nhật baseline.
8. Cập nhật `Ngày quét tiếp theo` cho từng profile theo tier hiện tại.
9. Tính `Ngày quét tiếp theo cấp account` bằng mốc sớm nhất trong các profile đang theo dõi.
10. Rút ra `Tóm tắt cấp account` theo `Account_Care_Summary_Template.md`.
11. Cập nhật `Bối cảnh follow-up gần nhất` nếu đội sales hoặc CS có thông tin mới.
12. Cập nhật `Trạng thái theo dõi` và watchlist tuần sau.
