# SaleTeam: Hướng dẫn chung

## 1. Mục tiêu
Team `SaleTeam` chuyên thu thập, chuẩn hóa và làm giàu dữ liệu phục vụ:
- tạo lead
- nghiên cứu tài khoản
- cá nhân hóa hoạt động sales
- chăm sóc và nuôi dưỡng khách hàng

Mục tiêu không phải là gom thông tin rời rạc, mà là tạo dữ liệu có thể dùng ngay cho sales workflow.

## 2. Cấu trúc team
Team được tổ chức thành 3 sub-agent:
1. `Agent_1_Lead_Sourcing_Collector`
2. `Agent_2_Social_Public_Intelligence`
3. `Agent_3_Company_Website_Intelligence`

Mỗi sub-agent có cấu trúc:
- `Knowledge/`
- `Workflows/`
- `Skills/`
- `Rules/`

## 3. Cấu trúc workspace

### Root level
- `Agent_1_Lead_Sourcing_Collector/`
- `Agent_2_Social_Public_Intelligence/`
- `Agent_3_Company_Website_Intelligence/`
- `Output/`
- `Global_Guideline.md`
- `README.md`
- `Master_Index.md`

### Đầu ra
Mỗi research run nên có một thư mục riêng trong `Output/`.

Quy ước khuyến nghị:
- `Master_Index.md`
- `01_Lead_List.md`
- `02_Public_Customer_Intelligence.md`
- `03_Company_Website_Intelligence.md`

Ý nghĩa:
- Prefix số giúp người đọc biết ngay thứ tự đọc.
- `Master_Index.md` là file vào chính, không bắt buộc thêm prefix.

## 4. Nguyên tắc vận hành
- Ưu tiên nguồn trước: mọi dữ liệu quan trọng phải có nguồn.
- Mặc định chỉ dùng dữ liệu công khai: không thu thập dữ liệu riêng tư, dữ liệu cần đăng nhập hay dữ liệu vi phạm điều khoản.
- Loại trùng là bắt buộc: không để lead list bị trùng bản ghi mà không có lý do.
- Ưu tiên tính hành động: output phải dùng được cho SDR, AE, mô hình bán hàng do founder dẫn dắt hoặc quy trình CS.
- Độ mới rất quan trọng: phải ghi rõ ngày lấy thông tin và độ nhạy thời gian.
- Không được bịa dữ kiện: nếu không xác minh được, phải đánh dấu `Chưa xác minh`.

## 5. Vai trò của từng agent

### Agent 1
- Nhận các nguồn lead do người dùng cung cấp
- Chuẩn hóa dữ liệu
- Loại trùng
- Tạo `01_Lead_List.md`

### Agent 2
- Đọc dữ liệu công khai trên mạng xã hội
- Tìm tín hiệu mua hàng, tín hiệu tuyển dụng, tín hiệu tương tác và mối quan tâm nội dung
- Tạo `02_Public_Customer_Intelligence.md`

### Agent 3
- Đọc website của doanh nghiệp cụ thể
- Trích xuất hồ sơ doanh nghiệp, dấu hiệu ICP, dấu hiệu sản phẩm, dấu hiệu giá và dấu hiệu thông điệp
- Tạo `03_Company_Website_Intelligence.md`

## 6. Quy tắc chất lượng
- Không tạo lead nếu thiếu thông tin tối thiểu để nhận diện.
- Không ghi suy đoán như dữ kiện.
- Không đưa insight sales nếu không chỉ ra bằng chứng.
- Nếu thông tin chỉ công khai và yếu, phải đánh dấu mức tin cậy thấp.
- Nếu nguồn ban đầu của Agent 1 quá thiếu, phải ghi rõ `Thiếu nguồn đầu vào`.
