# MVP Test Cases: Trầm Hương Hudo
**Project**: Trầm Hương Hudo
**Version**: 1.0
**Author**: Agent 3 (MVP Documentation Agent)

## 1. Test Suite: Product Discovery
| Test ID | Scenario | Steps | Expected Result |
| :--- | :--- | :--- | :--- |
| **TC_D_01** | Lọc theo cấp độ VIP | 1. Vào danh mục Nhang trầm.<br>2. Chọn filter "Cấp độ: VIP". | Chỉ hiện các sản phẩm có tag VIP. |
| **TC_D_02** | Xem video thực tế | 1. Vào trang chi tiết Nụ trầm SVIP.<br>2. Ấn Play video. | Video xưởng Quảng Nam load dưới 3s và xem được. |

## 2. Test Suite: Order & Checkout
| Test ID | Scenario | Steps | Expected Result |
| :--- | :--- | :--- | :--- |
| **TC_C_01** | Checkout Guest thành công | 1. Thêm 1 hộp nhang vào giỏ.<br>2. Điền tên, sđt, địa chỉ.<br>3. Bấm Đặt hàng. | Trang cảm ơn hiện ra, SMS xác nhận gửi về SĐT khách. |
| **TC_C_02** | Form quà tặng B2B | 1. Truy cập trang Quà tặng.<br>2. Điền form yêu cầu kèm logo.<br>3. Bấm Gửi. | Hệ thống báo: "Hudo đã nhận yêu cầu, CSKH sẽ gọi lại trong 10p". |

## 3. Test Suite: Performance (NFR)
| Test ID | Scenario | Steps | Expected Result |
| :--- | :--- | :--- | :--- |
| **TC_P_01** | Mobile Speed Test | 1. Chạy Lighthouse trên trang chủ (Profile Mobile). | Điểm Performance > 80. |
