# TrendTeam: Global Guideline

## 1. Mục tiêu
Team `TrendTeam` chuyên nghiên cứu và chuyển hóa tín hiệu thị trường thành đầu ra phục vụ:
- Product
- Marketing

Mục tiêu không phải là tổng hợp tin tức, mà là tạo insight có thể hành động.

## 2. Cấu trúc team
Team được tổ chức thành 4 sub-agent chuyên biệt:

1. `Agent_1_Signal_Scout`
2. `Agent_2_Product_Trend_Analyst`
3. `Agent_3_Marketing_Trend_Analyst`
4. `Agent_4_Trend_Synthesizer`

Mỗi sub-agent có cấu trúc riêng:
- `Knowledge/`
- `Workflows/`
- `Skills/`
- `Rules/`

## 3. Cấu trúc workspace

### Root level
- `Agent_1_Signal_Scout/`
- `Agent_2_Product_Trend_Analyst/`
- `Agent_3_Marketing_Trend_Analyst/`
- `Agent_4_Trend_Synthesizer/`
- `Output/`
- `Global_Guideline.md`
- `README.md`

### Output
`Output/` dùng để lưu các nghiên cứu hoàn chỉnh, ví dụ:
- `Output/weekly-ai-trends-2026-03/`
- `Output/social-commerce-signals-q2/`

Mỗi thư mục output nên có:
- `Master_Index.md`
- các file output được prefix theo thứ tự đọc khuyến nghị, ví dụ:
  - `01_Signal_Log.md`
  - `02_MVP_Proposals.md`
  - `03_Marketing_Trend_Insights.md`
  - `04_MVP_Marketing_Angles.md`
  - `05_Executive_Summary.md`
  - `06_Trend_Report.md`
  - `07_NotebookLM_Slide_Brief.md`

Ý nghĩa:
- Prefix số giúp người đọc nhận ra ngay `Recommended Reading Order`.
- `Master_Index.md` là entry point điều hướng, không bắt buộc thêm prefix số.

## 4. Vai trò từng sub-agent

### Agent_1_Signal_Scout
- Tìm tín hiệu mới
- Ghi log nguồn
- Loại nhiễu ban đầu
- Tạo `01_Signal_Log.md` trong mỗi research run

### Agent_2_Product_Trend_Analyst
- Đọc tín hiệu dưới góc nhìn nhu cầu, hành vi, JTBD, opportunity, risk
- Tạo output product theo vị trí số 02 trong reading order của research run

### Agent_3_Marketing_Trend_Analyst
- Đọc tín hiệu dưới góc nhìn message, kênh, nội dung, attention
- Tạo output marketing theo vị trí số 03-04 trong reading order của research run

### Agent_4_Trend_Synthesizer
- Hợp nhất các lớp phân tích
- Chốt narrative cuối
- Tạo:
  - `05_Executive_Summary.md`
  - `06_Trend_Report.md`
  - `07_NotebookLM_Slide_Brief.md` nếu cần dùng cho slide
  - `Master_Index.md`

## 5. Handoff logic
1. `Agent_1_Signal_Scout` thu thập tín hiệu
2. `Agent_2_Product_Trend_Analyst` và `Agent_3_Marketing_Trend_Analyst` phân tích song song
3. `Agent_4_Trend_Synthesizer` hợp nhất và đóng gói output cuối

## 6. Nguyên tắc vận hành
- Signal first
- Evidence over hype
- Actionability bắt buộc
- Ghi rõ time sensitivity
- Mọi insight quan trọng phải có confidence level

## 7. Quy tắc chất lượng
- Không dùng một nguồn duy nhất cho kết luận lớn
- Không mô tả trend mà thiếu implication
- Không đưa recommendation nếu chưa nêu rõ evidence
- Nếu dữ liệu chưa đủ, phải ghi rõ `Chưa đủ tín hiệu`

---
*Trend Research Team - Turning weak signals into usable decisions.*
