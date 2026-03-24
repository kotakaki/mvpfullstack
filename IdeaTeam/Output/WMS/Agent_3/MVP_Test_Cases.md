# MVP Test Cases: WMS Concept
**Project**: Warehouse Management System
**Version**: 1.0
**Author**: Agent 3 (MVP Documentation)

## 1. Test Suite: Inventory Accuracy
| ID | Scenario | Steps | Expected Result |
| :--- | :--- | :--- | :--- |
| **TC_I_01** | Nhập kho khớp số lượng | 1. Quét mã vạch sản phẩm.<br>2. Nhập số lượng 50.<br>3. Xác nhận vị trí Bin A1. | Tồn kho tổng tăng 50. Xem lịch sử nhập thấy dòng log mới. |
| **TC_I_02** | Xuất hàng vượt mức tồn | 1. SKU X có tồn = 10.<br>2. Tạo order xuất 15 đơn vị SKU X. | Hệ thống báo lỗi "Không đủ hàng trong kho" ngay tại bước tạo order. |

## 2. Test Suite: Mobile Interface
| ID | Scenario | Steps | Expected Result |
| :--- | :--- | :--- | :--- |
| **TC_M_01** | Quét mã bằng Camera | 1. Mở màn hình soạn hàng.<br>2. Chĩa camera vào mã QR. | Hệ thống nhận diện mã trong vòng < 1 giây và hiển thị thông tin sản phẩm. |
| **TC_M_02** | Cảnh báo sai vị trí | 1. Picking list yêu cầu lấy ở Bin B2.<br>2. Nhân viên quét mã tại Bin B3. | App phát âm thanh cảnh báo "Sai vị trí". |
