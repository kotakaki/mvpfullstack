# Business Requirement Document (BRD): Hệ thống E-commerce Trầm Hương Hudo
**Project**: Trầm Hương Hudo (Clone & Strategy Upgrade)
**Version**: 1.0
**Author**: Agent 1 (Idea Intake & Strategy)

## 1. Business Objective
Xây dựng nền tảng thương mại điện tử chuyên biệt cho sản phẩm Trầm Hương, tối ưu hóa trải nghiệm mua sắm từ "Xưởng sản xuất tận gốc" đến tay người tiêu dùng cuối và đối tác doanh nghiệp.

## 2. Business Process Flow (Sơ đồ quy trình nghiệp vụ)

### 2.1 Luồng Mua hàng & Checkout (B2C)
```mermaid
graph TD
    A[Khách vào web/blog] --> B{Tìm loại Trầm?}
    B -- Nhang/Nụ --> C[Xem chi tiết & Proof]
    B -- Vòng tay --> D[Xem tư vấn size/phong thủy]
    C --> E[Thêm vào giỏ]
    D --> E
    E --> F[Checkout nhanh - Không cần login]
    F --> G[Chọn hình thức: Giao hàng kiểm tra - COD]
    G --> H[Hệ thống tạo đơn & ping CSKH]
```

### 2.2 Luồng Đặt Set Quà tặng (B2B/Gift)
```mermaid
graph TD
    A[Truy cập danh mục Quà tặng] --> B[Chọn mức ngân sách: VIP/SVIP]
    B --> C{Yêu cầu khắc logo?}
    C -- Có --> D[Gửi yêu cầu & Upload Logo]
    C -- Không --> E[Đặt set sẵn]
    D --> F[CSKH báo giá số lượng lớn]
    E --> G[Checkout trực tiếp]
```

## 3. Product Features (Tóm tắt)
- **Danh mục linh hoạt**: Nụ, Nhang, Vòng, Tinh dầu, Dụng cụ thưởng trầm.
- **Set quà tặng doanh nghiệp**: Customize theo ngân sách.
- **Blog giáo dục**: Hệ thống bài viết "Hương Đạo" để tăng Trust.

## 4. Non-Functional Requirements (NFR)
- **NFR_01: Tốc độ (Performance)**: LCP < 2.5s trên Mobile (User mua trầm thường có độ tuổi trung niên, nhạy cảm với sự chậm trễ của công nghệ).
- **NFR_02: Độ tin cậy (Trust)**: Hiển thị minh bạch Chứng nhận trầm tự nhiên và hình ảnh thực tế tại xưởng Quảng Nam.
- **NFR_03: SEO**: Cấu trúc URL thân thiện (vd: `/nhang-tram-huong-sach-cao-cap`).
- **NFR_04: Bảo mật**: Mã hóa thông tin khách hàng mua làm quà tặng kín đáo.
