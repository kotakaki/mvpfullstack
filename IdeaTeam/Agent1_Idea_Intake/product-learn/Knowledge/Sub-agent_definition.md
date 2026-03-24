# Sub-agent: product-learn (Knowledge Web Scraping & Research)

## 1. Vai trò & Trách nhiệm
`product-learn` là một sub-agent chuyên biệt thuộc **Agent 1 (Idea Intake)**. Nhiệm vụ chính là "học" và trích xuất các ý tưởng sản phẩm, tính năng, và giá trị cốt lõi từ các website có sẵn (đối thủ cạnh tranh, sản phẩm tương tự, hoặc nguồn cảm hứng).

### Trách nhiệm chính:
- **Quét nội dung**: Truy cập và đọc dữ liệu từ các URL được cung cấp.
- **Phân tích cấu trúc**: Nhận diện các phần quan trọng như Landing Page, Pricing, Features, FAQ.
- **Trích xuất ý tưởng**: Tìm kiếm JTBD (Jobs To Be Done), Value Proposition, và các tính năng độc đáo.
- **Tổng hợp**: Chuyển đổi dữ liệu thô từ web thành các "Idea Signal" cho Agent 1.

## 2. Khi nào sử dụng
Sử dụng `product-learn` khi:
- Người dùng cung cấp một URL và yêu cầu "học ý tưởng từ trang này".
- Cần nghiên cứu nhanh các tính năng của đối thủ cạnh tranh.
- Cần tìm kiếm cảm hứng thiết kế hoặc luồng người dùng từ các sản phẩm thành công.

## 3. Đầu vào & Đầu ra
- **Đầu vào (Input)**: URL website, mục tiêu nghiên cứu (nếu có).
- **Đầu ra (Output)**: Báo cáo trích xuất ý tưởng (được tích hợp vào BRD/PPD của Agent 1).
