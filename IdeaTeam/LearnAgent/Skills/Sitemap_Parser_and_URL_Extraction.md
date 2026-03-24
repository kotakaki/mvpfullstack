# Skill: Sitemap Parser and URL Extraction

Kỹ thuật trích xuất và lọc danh sách URL từ tệp XML Sitemap để tạo bản đồ nghiên cứu.

## 1. Input Requirements
- URL của Sitemap chính (hoặc Sitemap Index).
- Định dạng: Tệp XML hoặc văn bản thô từ `robots.txt`.

## 2. Quy trình thực hiện (Execution Steps)

### Bước 1: Trích xuất Sitemap Index (nếu có)
Nếu Sitemap là một Index (chứa các thẻ `<sitemap>`), thực hiện đệ quy để lấy toàn bộ các sitemap con liên quan đến sản phẩm/tính năng.

### Bước 2: Parsing URL
Trích xuất dữ liệu từ các thẻ `<url>`:
- **`<loc>`**: Địa chỉ URL tuyệt đối (Bắt buộc).
- **`<lastmod>`**: Để ưu tiên các trang mới cập nhật nhất.
- **`<priority>`**: Để xác định các trang quan trọng nhất của doanh nghiệp.

### Bước 3: Lọc & Phân nhóm (Filtering)
Sử dụng Regex hoặc từ khóa để phân loại URL vào các nhóm nghiên cứu:
- `features|product|solution` -> Nhóm tìm hiểu tính năng.
- `pricing|plan|billing` -> Nhóm tìm hiểu mô hình kinh doanh.
- `blog|news|case-study` -> Nhóm tìm hiểu thực tế triển khai.

## 3. Tooling Recommendation
- Sử dụng `curl` hoặc `Invoke-WebRequest` để tải XML.
- Sử dụng trình phân tích XML (XPath) để lấy dữ liệu chính xác thay vì chỉ Regex chuỗi thô.

## 4. Output
Một danh sách các URL được phân loại theo cấu trúc ưu tiên, sẵn sàng cho bước Scrape nội dung chi tiết.
