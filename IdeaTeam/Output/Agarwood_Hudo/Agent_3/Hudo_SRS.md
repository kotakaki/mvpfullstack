# Software Requirements Specification (SRS): Trầm Hương Hudo
**Project**: Trầm Hương Hudo
**Version**: 1.0
**Author**: Agent 3 (MVP Documentation Agent)

## 1. Introduction
SRS này định nghĩa các yêu cầu cho giai đoạn MVP của hệ thống bảo lãnh chất lượng và thương mại điện tử Trầm Hương Hudo.

## 2. Functional Requirements

### 2.1 Quản lý Sản phẩm (Product Management)
**ID: FR_01**
- **Description**: Cho phép khách xem sản phẩm theo danh mục và mức độ (VIP/SVIP). Hiển thị rõ nguồn gốc vùng trầm.
- **Inputs**: Click Category / Filter.
- **Outputs**: Danh sách sản phẩm với thẻ chứng nhận tự nhiên.

### 2.2 Luồng Thanh toán COD (Checkout System)
**ID: FR_02**
- **Description**: Tối ưu hóa checkout không cần đăng nhập để tăng tỷ lệ chuyển đổi. Khách chỉ cần nhập Tên, SĐT, Địa chỉ.
- **Validation**: Số điện thoại phải đúng định dạng VN (+84 hoặc 0...).

### 2.3 Quản lý Đơn hàng B2B/Quà tặng (Gift Management)
**ID: FR_03**
- **Description**: Hệ thống cho phép khách hàng sỉ/doanh nghiệp để lại ghi chú khắc logo hoặc yêu cầu thiết kế riêng cho các set quà SVIP.

## 3. External Interface Requirements
- **Web UI**: Giao diện mang đậm chất Á Đông, thanh tao, màu sắc gỗ trầm (Nâu/Vàng/Trắng).
- **Mobile UI**: Ưu tiên Mobile-First, nút Zalo/Hotline luôn nổi bật để khách gọi tư vấn nhanh.

## 4. Non-Functional Requirements (NFR)
- **Performance**: Trang chủ phải đạt điểm Core Web Vitals > 80.
- **Compliance**: Tuân thủ các quy định về kinh doanh lâm sản/đặc sản vùng miền (chỉ về mặt pháp lý thông tin).
- **Internal CMS**: Dashboard cho Admin quản lý đơn hàng phải dễ dùng trên thiết bị di động (để chủ xưởng ở Quảng Nam có thể check đơn nhanh).
