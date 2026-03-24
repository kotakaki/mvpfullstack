# Knowledge: Sitemap and URL Discovery

Tri thức về việc khám phá cấu trúc toàn diện của một website thông qua Sitemap và các tệp chỉ dẫn.

## 1. Tầm quan trọng của Sitemap
Sitemap là "bản đồ" của website giúp công cụ tìm kiếm (và AI agent) hiểu được:
- Toàn bộ danh sách URL quan trọng.
- Cấu trúc phân cấp của website.
- Thời gian cập nhật nội dung cuối cùng (`lastmod`).
- Tần suất thay đổi nội dung (`changefreq`).

## 2. Các vị trí tìm kiếm Sitemap tiêu chuẩn
Khi bắt đầu nghiên cứu một doanh nghiệp, `LearnAgent` phải kiểm tra các đường dẫn sau:
1. `/sitemap.xml` (Phổ biến nhất)
2. `/sitemap_index.xml` (Dành cho web lớn có nhiều sitemap con)
3. `/robots.txt` (Thường chứa đường dẫn đến sitemap: `Sitemap: https://example.com/sitemap.xml`)
4. `/sitemap/` (Đường dẫn folder)

## 3. Phân loại URL từ Sitemap
Sau khi lấy được danh sách URL, cần phân loại để tập trung vào mục tiêu nghiên cứu:
- **Core Pages**: Trang chủ, Giới thiệu, Liên hệ.
- **Product Pages**: `/product/*`, `/features/*`, `/solutions/*`.
- **Business Pages**: `/pricing`, `/plans`, `/enterprise`.
- **Support Pages**: `/docs`, `/blog`, `/resources`.

## 4. Lưu ý về Robot Exclusion Protocol
Luôn kiểm tra `robots.txt` để biết các vùng bị cấm Scrape (`Disallow`), đảm bảo tuân thủ đạo đức dữ liệu và tránh bị chặn IP.
