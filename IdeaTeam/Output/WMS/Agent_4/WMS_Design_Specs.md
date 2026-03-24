# Design Specifications v2: WMS Industrial UI
**Project**: Warehouse Management System
**Version**: 2.0
**Author**: Agent 4 (UI/UX Designer)

## 1. Advanced UI Strategy
- **Audit-First Mode**: Màn hình kiểm kê được tối ưu để nhân viên quét liên tục không cần chạm vào màn hình (Continuous Scan Mode).
- **Status Branding**: Dùng màu sắc chủ đạo để phân biệt trạng thái:
  - `Xanh`: Hàng đạt chuẩn (Pass QC).
  - `Đỏ`: Hàng lỗi/Hàng hoàn chờ xử lý.
  - `Cam`: Hàng sắp hết hạn.

## 2. Screen Inventory (V2 Extensions)

### Luồng 3: Kiểm kê (Stock-taking)
| Bước | Screen ID | Tên màn hình | Core Components |
| :--- | :--- | :--- | :--- |
| **B1**: Chọn đợt | `SCR_06` | **Audit Session** | List các khu vực cần kiểm kê, tiến độ hoàn thành (%). |
| **B2**: Quét xác nhận| `SCR_07` | **Audit Scan** | Chế độ quét liên tục, hiển thị số lượng dự kiến vs thực tế. |

### Luồng 4: Trả hàng (Returns & QC)
| Bước | Screen ID | Tên màn hình | Core Components |
| :--- | :--- | :--- | :--- |
| **B1**: Tiếp nhận | `SCR_08` | **Return Portal** | Quét mã đơn hoàn, hiển thị lý do hoàn hàng. |
| **B2**: Kiểm định | `SCR_09` | **QC Checklist** | Nút bấm Pass/Fail cho từng SKU, ô chụp ảnh minh chứng. |

### Luồng 5: In nhãn (Printing)
| Bước | Screen ID | Tên màn hình | Core Components |
| :--- | :--- | :--- | :--- |
| **B1**: Thiết lập in | `SCR_10` | **Print Config** | Chọn máy in (LAN/BlueTooth), chọn khổ giấy, test in. |

## 3. Interaction Patterns (v2)
- **Long Press**: Trên màn hình Inventory để xem chi tiết các Lô (Batch) của sản phẩm đó.
- **Swipe Action**: Swipe đơn hàng sang phải để đánh dấu "Đã đóng gói".
