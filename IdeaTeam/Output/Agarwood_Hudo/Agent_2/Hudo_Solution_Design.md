# Solution Design Document (SDD): Trầm Hương Hudo
**Project**: Trầm Hương Hudo
**Version**: 1.0
**Author**: Agent 2 (AI Solution Architect)

## 1. High-Level Architecture
Hệ thống được xây dựng theo kiến trúc **Monolithic Modular** để dễ dàng vận hành và SEO tốt nhất cho giai đoạn MVP.

- **Technology Stack**:
  - **Frontend**: Next.js (App Router) - Tối ưu SEO, SSR cho trang sản phẩm và blog.
  - **Styling**: Tailwind CSS (nếu có yêu cầu) hoặc SCSS.
  - **Backend**: Node.js với Express hoặc NestJS.
  - **Database**: PostgreSQL (quản lý quan hệ: sản phẩm, đơn hàng, khách hàng).
  - **Storage**: AWS S3 hoặc Cloudinary để lưu trữ hình ảnh trầm chất lượng cao.
  - **Search**: PostgreSQL Full-text Search (đủ cho số lượng < 10.000 SKU).

## 2. Database Schema (Lược đồ cốt lõi)

### Bảng `Products`
- `id` (UUID)
- `name` (String) - Tên sản phẩm (vd: Nụ trầm SVIP)
- `slug` (String) - URL thân thiện
- `category_id` (FK) - Nụ, Nhang, Vòng, etc.
- `price` (Decimal), `discount_price` (Decimal)
- `origin` (String) - Vùng nguyên liệu (vd: Tiên Phước)
- `quality_level` (Enum: Standard, VIP, SVIP)
- `stock_quantity` (Int)
- `description_html` (Text)

### Bảng `Orders` & `OrderItems`
- Lưu trữ thông tin khách hàng (Guest hoặc User), tổng tiền, trạng thái thanh toán (COD/Banking), trạng thái vận chuyển.

### Bảng `Gift_Customization` (Mở rộng cho B2B)
- `order_id` (FK)
- `logo_url` (String) - File logo khách gửi
- `note` (Text) - Yêu cầu khắc/in riêng.

## 3. Key Integrations
- **Payment**: Tích hợp mã QR Pay (VietQR) để khách thanh toán nhanh.
- **Shipping**: Tích hợp Giao Hàng Tiết Kiệm (GHTK) hoặc Giao Hàng Nhanh (GHN) để tính phí ship tự động.
- **Communication**: Zalo OA (Open API) để gửi tin nhắn xác nhận đơn hàng tự động.

## 4. Non-Functional Requirements (Technical)
- **Scalability**: Thiết kế DB sẵn sàng cho việc mở rộng thêm các đại lý/cộng tác viên (Dropshipping).
- **Security**: HTTPS/SSL bắt buộc. Validate input để tránh SQL Injection.
- **Cache**: Sử dụng Redis để cache dữ liệu danh mục và trang chủ nhằm giảm tải cho DB.
