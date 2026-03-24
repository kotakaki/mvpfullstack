# Rules: Input Validation Checklist

## Mục tiêu
Đảm bảo Agent 4 chỉ tổng hợp khi đầu vào đủ tối thiểu và đủ sạch để tạo kết luận đáng tin.

## 1. Kiểm tra đầu vào bắt buộc
- Có `Signal_Log.md`.
- Có ít nhất một trong hai:
  - `MVP_Proposals.md`
  - `Marketing_Trend_Insights.md`

## 2. Kiểm tra đầu vào đầy đủ khuyến nghị
- Có `Signal_Log.md`.
- Có `MVP_Proposals.md`.
- Có `Marketing_Trend_Insights.md`.
- Có `MVP_Marketing_Angles.md`.

## 3. Kiểm tra chất lượng đầu vào
- `Signal_Log.md` có signal cụ thể, không chỉ có nhận định chung.
- `MVP_Proposals.md` có mức độ ưu tiên, giả định chính, câu hỏi còn mở.
- `Marketing_Trend_Insights.md` và `MVP_Marketing_Angles.md` có message, channel, hoặc implication rõ.
- Các file đầu vào không mâu thuẫn do dùng phiên bản cũ và mới lẫn nhau.

## 4. Kiểm tra khả năng traceability
- Signal có định danh hoặc có thể tham chiếu ngắn gọn như `Signal 01`, `Signal 02`.
- MVP có định danh hoặc có thể tham chiếu như `MVP 01`, `MVP 02`.
- Marketing insight hoặc marketing angle có thể tham chiếu như `Marketing Trend 01`, `Marketing Angle 01`.

## 5. Khi đầu vào chưa đủ
- Phải ghi rõ file nào chưa có.
- Phải gắn nhãn output là `Tạm thời`.
- Không được viết như thể đã có đủ góc nhìn Product và Marketing.
- Nếu thiếu nhánh marketing hoặc product, phải nêu đây là `kết luận một phần`.

## 6. Quyết định trước khi chạy Agent 4
- Nếu đạt đầu vào tối thiểu: được phép tổng hợp, nhưng có thể phải gắn nhãn `Tạm thời`.
- Nếu đạt đầu vào đầy đủ: được phép tổng hợp đầy đủ.
- Nếu không đạt đầu vào tối thiểu: chưa được tạo kết luận cuối.
