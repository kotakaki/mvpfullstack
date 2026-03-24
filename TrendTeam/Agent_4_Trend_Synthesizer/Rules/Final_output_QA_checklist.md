# Rules: Final Output QA Checklist

## Mục tiêu
Kiểm tra chất lượng cuối trước khi phát hành `Executive_Summary.md`, `Trend_Report.md`, và `NotebookLM_Slide_Brief.md`.

## 1. QA cho ưu tiên cuối
- `Executive_Summary.md` và `Trend_Report.md` có cùng MVP ưu tiên.
- `Executive_Summary.md` và `Trend_Report.md` có cùng marketing angle ưu tiên.
- Nếu có `NotebookLM_Slide_Brief.md`, slide `MVP Priority` và `Marketing Angle` không lệch với 2 file còn lại.

## 2. QA cho evidence và citation
- Kết luận chính có citation hoặc reference rõ.
- Recommendation lớn có evidence nền.
- Nếu có xung đột, đã ghi rõ cả xung đột và cách xử lý.

## 3. QA cho logic báo cáo
- Đã tách được:
  - `Evidence`
  - `Interpretation`
  - `Recommendation`
- Không lặp nguyên si output từ Agent 2 hoặc Agent 3.
- Không có recommendation vượt quá evidence hiện có.

## 4. QA cho tính nhất quán
- Risk và open question trong slide brief không mâu thuẫn với trend report.
- Các bước `Làm ngay`, `Test tiếp`, `Theo dõi` nhất quán giữa các file.
- Nếu đầu vào thiếu, mọi file đều gắn nhãn `Tạm thời`.

## 5. QA cho NotebookLM-friendly
- Heading đủ ngắn để dùng làm tiêu đề slide.
- Mỗi section chỉ có một ý chính.
- Bullet ngắn, không quá dày.
- Không có đoạn văn dài làm giảm khả năng lên slide.

## 6. Chỉ được phát hành khi
- Đạt đủ QA logic cơ bản.
- Đạt QA nhất quán giữa các output.
- Không còn lỗi lớn về thiếu evidence cho kết luận chính.
