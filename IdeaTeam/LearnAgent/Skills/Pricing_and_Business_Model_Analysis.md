# Skill: Pricing & Business Model Analysis

Kỹ thuật phân tích cách doanh nghiệp đối thủ tạo ra doanh thu và cấu trúc sản phẩm thương mại của họ.

## 1. Mục tiêu (Objective)
Hiểu được mô hình kinh doanh (Business Model) để định hướng phạm vi tính năng (MVP Scope) – tính năng nào nên miễn phí, tính năng nào là "mỏ vàng" để thu phí.

## 2. Nguồn dữ liệu cần phân tích (Data Sources)
- Trang `/pricing`.
- Các câu hỏi thường gặp (FAQ) trên trang giá.
- Trang `/enterprise` hoặc "Contact Sales".
- Các nút CTA mồi (Trial, Freemium).

## 3. Quy trình thực hiện (Execution Steps)

### Bước 1: Nhận diện Mô hình Doanh thu (Revenue Model)
Xác định sản phẩm thuộc loại nào:
- **Freemium**: Có gói miễn phí vĩnh viễn với tính năng giới hạn.
- **Free Trial**: Dùng thử full tính năng trong X ngày (14-day trial).
- **Usage-based / Pay-as-you-go**: Trả tiền theo lượng dùng (vd: API calls, số GB, số token).
- **Flat-rate / Tiered Subscription**: Thuê bao cố định hàng tháng/năm.

### Bước 2: Phân tích Tiers (Các bậc giá)
Liệt kê các ranh giới nâng cấp. Ví dụ:
- Gói Free: Chỉ được 1 User, 3 Projects.
- Gói Pro: Không giới hạn Projects.

### Bước 3: Xác định Gated Features (Paywalls)
- Tính năng nào bị dán nhãn "Enterprise Only" (Thường là SSO, Audit Logs, Dedicated Support)?
- Tính năng nào buộc người dùng phải nâng cấp từ Free lên Pro? Đây chính là "Killer Features" của họ.

## 4. Output
Bản tóm tắt mô hình kinh doanh giúp Agent 1 cấu trúc phần **Business Process Flow (Luồng nâng cấp/Thanh toán)** trong BRD.
