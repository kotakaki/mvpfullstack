# Software Requirements Specification (SRS) v2: WMS Functional Details
**Project**: Warehouse Management System
**Version**: 2.0
**Author**: Agent 3 (MVP Documentation)

## 1. Advanced Functional Requirements

### 1.3 Quản lý Lô & Hạn sử dụng (Lot Management)
**ID: FR_03**
- **Description**: Hệ thống bắt buộc nhập Hạn sử dụng (Expiry Date) cho các SKU thuộc nhóm thực phẩm/mỹ phẩm.
- **Logic**: Khi tạo phiếu soạn hàng, hệ thống ưu tiên chỉ định lấy hàng từ Lô có hạn sử dụng gần nhất (**FEFO**).

### 1.4 In nhãn tự động (In-app Printing)
**ID: FR_04**
- **Description**: Tại màn hình nhập kho, nút "In nhãn QR" phải sinh ra mã đúng chuẩn vị trí/SKU và đẩy lệnh in ngay lập tức.
- **Format**: QR Code kích thước 50x30mm hoặc 35x22mm.

### 1.5 Module Kiểm kê (Inventory Count)
**ID: FR_05**
- **Description**: Cho phép khóa tạm thời một khu vực kho (Lock Region) để thực hiện kiểm kê. Hệ thống ghi nhận sự chênh lệch và chỉ cập nhật tồn chính thức sau khi Admin phê duyệt phiếu kiểm kê.

## 2. Interface Requirements (v2)
- **Sound & Haptics**: Phải có phản hồi âm thanh/rung khác nhau cho từng loại kết quả quét: "Tít" (Thành công), "Bíp bíp" (Lỗ chênh lệch), "Buzz" (Sai mã).

## 3. Compliance
- Tuân thủ tiêu chuẩn GS1 cho mã vạch nếu khách hàng yêu cầu xuất khẩu/bán vào siêu thị.
