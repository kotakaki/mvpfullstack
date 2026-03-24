# Design Specifications
**Project**: Nền tảng E-commerce Sim Thăng Long (Clone)
**Version**: 1.0
**Author**: Agent 4 (UI/UX Designer)

## 1. Design Strategy (Chiến lược thiết kế)
- **Nhanh & Tối giản (Fast & Minimal)**: Website phải load dưới 2 giây vì user chủ yếu dùng mobile 3G/4G để rảnh rỗi tìm số.
- **Tập trung vào Chuyển đổi (Conversion-Centric)**: Nút "Tìm Kiếm" và Thanh Bar lọc số (Filter) luôn ghim cứng (Sticky) ở đầu trang trên Mobile.
- **Tin cậy (Trustworthy)**: Sử dụng tone màu Đỏ/Cam (giống các mạng viettel/mobifone) hoặc Xanh dương (uy tín).

## 2. User Flow & Screen Inventory (Bắt buộc theo chuẩn Elite)

Dưới đây là liên kết luồng người dùng (User Flow) với danh sách màn hình cụ thể cần thiết kế (Screen Inventory).

### Luồng 1: Tìm kiếm SIM & Mua đứt
| Bước (User Flow) | Screen ID | Tên Màn hình (Screen Name) | Core Components |
| :--- | :--- | :--- | :--- |
| **B1**: Mở Home, nhập từ khóa `*098` | `SCR_01` | **Homepage** | Hero Banner, Search Box (Nổi bật), Top Network Logos. |
| **B2**: Xem danh sách 50k kết quả | `SCR_02` | **Search Results Page** | Grid/List view SIM, Advanced Filters (Mạng, Giá), Pagination. |
| **B3**: Chọn SIM ưng ý | `SCR_03` | **SIM Detail Modal/Page** | Thông số SIM, Điểm phong thủy, Ưu đãi, Nút "Mua ngay", Nút "Trả góp". |
| **B4**: Ấn Mua ngay | `SCR_04` | **Checkout Step 1** | Form thu thập (Tên, SĐT liên hệ, Địa chỉ nhận SIM). Khóa số countdown. |
| **B5**: Hoàn tất | `SCR_05` | **Thank You Page** | Thông báo thành công, Mã Đơn Hàng `[SIM-XXXX]`, Lời khuyên đợi ĐT. |

### Luồng 2: Mua Trả Góp
| Bước (User Flow) | Screen ID | Tên Màn hình (Screen Name) | Core Components |
| :--- | :--- | :--- | :--- |
| **B3**: Ấn "Mua Trả Góp" | `SCR_03_A` | **Installment Calculator Modal**| Slider (Phần trăm trả trước), Dropdown (Kỳ hạn 3,6,9,12T), Bảng tính gốc + lãi hàng tháng. |

## 3. Design System (Chỉ định cơ bản)
- **Typography**: `Inter` hoặc `Roboto` cho dễ đọc các dãy số dài. Text chứa số điện thoại luôn dùng font `Monospace` hoặc font có chiều rộng ký tự cố định để dễ dóng hàng dọc.
- **Color Palette**: 
  - Primary: `#E63946` (Đỏ Tín Nhiệm - Mượn ý niệm viễn thông).
  - Background: `#F8F9FA` (Trắng xám - Tôn lên màu chữ của dãy số).
  - Text: `#1D3557` (Xanh hải quân đậm).
- **Icons**: Sử dụng bộ Phosphor Icons (Line/Solid) cho mượt mà trên UI.

## 4. Key Components Design (Thiết kế Component cốt lõi)
**SIM Card Item**: 
- Dãy số hiển thị siêu lớn và có dấu chấm cách (vd: `098.365.6699`).
- Dưới dãy số là Logo mạng viễn thông cực nhỏ để tiết kiệm không gian.
- Bên trái là Giá gốc (gạch sọc), Giá khuyến mãi in đậm màu Đỏ.
- Nút "Mua ngay" luôn nằm góc dưới phải thẻ (`Button Primary`).
