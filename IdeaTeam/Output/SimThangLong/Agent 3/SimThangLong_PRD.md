# Product Requirements Document (PRD)
**Project**: Nền tảng E-commerce Sim Thăng Long (Clone)
**Version**: 1.0
**Author**: Agent 3 (MVP Documentation Agent)

## 1. Product Context & Scope
Sản phẩm này tái tạo nền tảng cốt lõi của Sim Thăng Long nhằm phục vụ việc phân phối SIM số đẹp trên môi trường online. MVP sẽ bao gồm 2 nhóm User (Khách hàng \u0026 CSKH/Admin).

## 2. Epics & User Stories

### Epic 1: Giao dịch & Mua sắm
- **Story**: Là một khách hàng, tôi muốn kết hợp tìm đầu số `098` và đuôi `6868`, ở mức giá dưới 1 triệu, để tôi dễ chọn SIM phong thủy giá bèo.
- **Acceptance Criteria**:
  - Tích chọn "Viettel" hoặc đầu "098".
  - Gõ `*6868` vào search box.
  - Chọn khoảng giá `0 - 1.000.000 VNĐ`.
  - Kết quả trả ra ngay lập tức và chính xác theo mệnh giá nhỏ hơn hoặc bằng 1 triệu.

- **Story**: Là một sinh viên (ngân sách ít), tôi muốn mua trả góp một SIM ngũ quý giá 10 triệu để dễ phân bổ tài chính.
- **Acceptance Criteria**:
  - Tại trang Chi tiết SIM, có nút "Mua Trả Góp".
  - Hiển thị công cụ tính Số tiền trả trước (20-30-50%) và Kỳ hạn (3-6-9-12 tháng).
  - Tự động nhảy công thức ra số tiền phải trả mỗi tháng (bao gồm lãi/nếu có).

### Epic 2: Vận hành nội bộ (CSKH)
- **Story**: Là nhân viên CSKH, tôi cần xem danh sách đơn hàng real-time đổ về để kịp thời gọi điện thoại ngay trong 5 phút.
- **Acceptance Criteria**:
  - Dashboard có âm thanh push notification ping khi có đơn.
  - Phân loại tab trạng thái: `Đơn mới` | `Đang xử lý` | `Hoàn tất` | `Thất bại`.

## 3. Assumptions & Constraints
- Khách hàng không cần đăng nhập (No Authentication) để xem SIM hay Mua SIM. Mua nhanh dạng "Guest Checkout" để tối đa hóa Conversion Rate.
- Quản trị viên phải đăng nhập với JWT (Role-Based Access Control).

## 4. Key Metrics
1. **Lượt tìm kiếm không ra kết quả (Zero-result rate)**: Cần < 5% để đo lường độ phủ của thuật toán.
2. **Tốc độ thêm vào giỏ (Add-to-cart rate)**.
