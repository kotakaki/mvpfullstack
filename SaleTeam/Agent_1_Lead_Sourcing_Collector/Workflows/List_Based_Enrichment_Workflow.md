# Quy trình: Làm giàu thông tin từ danh sách người dùng cung cấp

1. Nhận danh sách đầu vào từ người dùng.
2. Kiểm tra danh sách theo `Input_List_Requirements.md`.
3. Nếu có, tiếp nhận `ICP_Input_Brief.md`; nếu chưa có thì ghi rõ `Chưa xác định`.
4. Chuẩn hóa các trường cơ bản và gán `Mã bản ghi`.
5. Tạo `00_Input_List.md` theo `00_Input_List_Template.md`.
6. Tạo `01_Lead_List.md` với trạng thái xác minh, ICP fit, trạng thái enrichment và định tuyến enrichment.
7. Định tuyến bản ghi theo `Enrichment_Routing_Matrix.md`.
8. Xử lý các bản ghi `Thiếu dữ liệu` theo `Missing_Data_Resolution_Workflow.md`.
9. Chuyển các bản ghi đủ điều kiện sang Agent 2 và Agent 3.
10. Đối chiếu output downstream với ma trận định tuyến để cập nhật `Trạng thái enrichment`.
11. Tổng hợp output làm giàu theo cùng `Mã bản ghi`.
12. Tạo `04_Enriched_Record_Summary.md` theo `Enriched_Record_Summary_Template.md`.
