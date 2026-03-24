# SaleTeam

Workspace này được tổ chức thành 3 sub-agent phục vụ sales workflow:

- `Agent_1_Lead_Sourcing_Collector/`
- `Agent_2_Social_Public_Intelligence/`
- `Agent_3_Company_Website_Intelligence/`

Mỗi sub-agent có cấu trúc KWSR riêng:
- `Knowledge/`
- `Workflows/`
- `Skills/`
- `Rules/`

Ngoài ra:
- `Output/` chứa các lần chạy nghiên cứu, lần chạy nghiên cứu tài khoản và lần chạy xây dựng lead
- `Global_Guideline.md` là hướng dẫn chung của team
- `Master_Index.md` là file điều hướng nhanh

## Luồng làm việc
1. `Agent_1_Lead_Sourcing_Collector` nhận các nguồn lead do người dùng cung cấp và tạo danh sách lead có cấu trúc.
2. `Agent_2_Social_Public_Intelligence` thu thập thông tin công khai trên mạng xã hội để hỗ trợ nuôi dưỡng và chăm sóc khách hàng.
3. `Agent_3_Company_Website_Intelligence` phân tích website doanh nghiệp để bổ sung bối cảnh doanh nghiệp, thông điệp, use case và tín hiệu mua hàng.
