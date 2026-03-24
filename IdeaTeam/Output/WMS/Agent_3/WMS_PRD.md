# Product Requirements Document (PRD) v2: WMS Core Features
**Project**: Warehouse Management System
**Version**: 2.0
**Author**: Agent 3 (MVP Documentation)

## 1. Value Proposition (Industry Ready)
"WMS v2 không chỉ quản lý hàng hóa mà còn bảo vệ lợi nhuận doanh nghiệp thông qua việc giảm hủy hàng (hết hạn) và minh bạch hóa trách nhiệm từng nhân viên."

## 2. Detailed User Stories

### Epic: Smart FIFO/FEFO
- **Story**: Là chủ doanh nghiệp, tôi muốn hệ thống tự động cảnh báo các lô hàng sắp hết hạn trước 30 ngày để tôi đẩy chương trình khuyến mãi giảm tồn kho.
- **Acceptance Criteria**:
  - Dashboard hiển thị mục "Hàng sắp hết hạn".
  - Báo cáo gửi qua Email vào thứ 2 hàng tuần.

### Epic: Return Management (Reverse Logistics)
- **Story**: Là nhân viên tiếp nhận, tôi muốn quét mã vận đơn đơn hàng bị hoàn trả để hệ thống tự động hiện ra danh sách sản phẩm cần kiểm tra lại.
- **Acceptance Criteria**:
  - Luồng QC: Pass/Fail cho từng SKU trong đơn hoàn.
  - Tự động tạo phiếu nhập kho cho hàng đạt chuẩn.

## 3. Product Roadmap (Phases)
- **Phase 1 (Basic)**: Nhập/Xuất/Tồn đơn giản. (Đã hoàn thành thiết kế)
- **Phase 2 (Hardened)**: Batch/Lot, In nhãn, Kiểm kê, Hàng hoàn. (Hiện tại)
- **Phase 3 (Optimization)**: AI gợi ý lộ trình soạn hàng ngắn nhất, Dự báo nhu cầu nhập hàng dựa trên dữ liệu lịch sử.
