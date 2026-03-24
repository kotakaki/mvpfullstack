# Hướng dẫn thư mục Output

Mỗi lần chạy xây dựng lead hoặc nghiên cứu tài khoản nên có một thư mục riêng trong `Output/`.

Ví dụ:
- `Output/saas-founders-apac-2026-03/`
- `Output/top-20-target-accounts-q2/`
- `Output/customer-nurture-watchlist-2026-03/`

Bên trong nên có:
- `Master_Index.md`
- `ICP_Input_Brief.md` nếu có brief ICP riêng
- `00_Input_List.md` nếu người dùng đưa sẵn danh sách đầu vào
- `01_Lead_List.md`
- `02_Public_Customer_Intelligence.md`
- `03_Company_Website_Intelligence.md`
- `04_Enriched_Record_Summary.md`

Quy tắc:
- Prefix số để biết ngay thứ tự đọc.
- `Master_Index.md` là điểm vào chính.
- Nếu run bắt đầu từ danh sách người dùng cung cấp, nên luôn lưu lại `00_Input_List.md`.
- Nếu đã có output từ Agent 2 và Agent 3, nên tạo thêm `04_Enriched_Record_Summary.md` để sales dùng nhanh.
- Nếu run không cần đủ cả các output trên, vẫn nên giữ prefix theo logic thực tế.
