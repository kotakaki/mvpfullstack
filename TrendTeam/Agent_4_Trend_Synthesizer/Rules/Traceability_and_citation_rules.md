# Rules: Traceability and Citation

## Mục tiêu
Giữ cho mọi kết luận của Agent 4 có thể lần ngược về evidence cụ thể từ các agent trước.

## 1. Chuẩn tham chiếu
- Dùng nhãn ngắn, nhất quán:
  - `Signal 01`, `Signal 02`
  - `MVP 01`, `MVP 02`
  - `Marketing Trend 01`, `Marketing Trend 02`
  - `Marketing Angle 01`, `Marketing Angle 02`

## 2. Quy tắc cho `Executive_Summary.md`
- Mỗi kết luận chính nên gắn ít nhất 1-3 tham chiếu ngắn.
- Nếu bullet quá ngắn, có thể gom reference vào dòng `Evidence`.
- Không đưa recommendation lớn mà không có evidence nền.

## 3. Quy tắc cho `Trend_Report.md`
- Mỗi phần `Interpretation` phải chỉ ra đang dựa vào evidence nào.
- Mỗi phần `Recommendation` phải chỉ ra đang dựa vào evidence và interpretation nào.
- Nếu có xung đột, phải trích cả hai phía, không chỉ trích một phía thuận tiện hơn.

## 4. Quy tắc cho `NotebookLM_Slide_Brief.md`
- Giữ citation ngắn và dễ đọc.
- Chỉ trích những reference quan trọng nhất để tránh làm brief nặng.
- Ưu tiên citation ở các slide:
  - `Market Shift`
  - `MVP Priority`
  - `Marketing Angle`

## 5. Khi nào phải gắn nhãn `Suy luận`
- Khi kết luận không xuất hiện trực tiếp trong upstream output mà là phần Agent 4 suy ra.
- Khi đang nối nhiều evidence rời thành một narrative thống nhất.
- Khi đang chọn một hướng ưu tiên trong bối cảnh còn dữ liệu thiếu.

## 6. Không được làm
- Không dùng citation mơ hồ như `nhiều signal`, `một số insight`, `có vài nguồn`.
- Không bỏ citation khỏi các recommendation quan trọng.
- Không biến citation thành đoạn giải thích dài.
