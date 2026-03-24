# Design Specifications: Trầm Hương Hudo
**Project**: Trầm Hương Hudo
**Version**: 1.0
**Author**: Agent 4 (UI/UX Designer)

## 1. Design Strategy
- **Aesthetic**: Zen / Minimalism Á Đông. Sử dụng không gian trắng (white space) rộng rãi để tạo cảm giác thanh tịnh.
- **Color Palette**:
  - Primary: `#5D4037` (Nâu trầm - Sang trọng, truyền thống).
  - Secondary: `#FFC107` (Vàng hổ phách - Màu của tinh dầu trầm).
  - Background: `#FFFBF2` (Trắng ngà - Dịu mắt, tinh tế).
- **Typography**: `Playfair Display` (Serif) cho tiêu đề để tạo sự sang trọng; `Montserrat` (Sans-serif) cho nội dung để dễ đọc.

## 2. Screen Inventory (Bắt buộc khớp User Flow)

Dưới đây là danh sách màn hình (Screen Inventory) tương ứng với hành trình khách hàng.

### Luồng 1: Mua Nhang/Nụ Trầm (B2C)
| Bước hành trình | Screen ID | Tên màn hình | Thành phần chính (Core Components) |
| :--- | :--- | :--- | :--- |
| **B1**: Vào xem Home | `SCR_01` | **Homepage** | Video Hero (Xưởng Quảng Nam), Danh mục nổi bật, Khối "Cam kết Trầm Sạch". |
| **B2**: Tìm loại nhang | `SCR_02` | **Category Page** | Bộ lọc (Theo giá, Theo cấp độ VIP), Grid sản phẩm. |
| **B3**: Xem chi tiết | `SCR_03` | **Product Detail** | Gallery ảnh gỗ, Video đốt thực tế, Tab "Câu chuyện vùng nguyên liệu". |
| **B4**: Checkout | `SCR_04` | **Checkout Page** | Form nhập liệu tối giản (3 ô), Phương thức vận chuyển GHTK. |
| **B5**: Hoàn tất | `SCR_05` | **Thank You** | Mã đơn hàng, Nút "Chat Zalo tư vấn thêm". |

### Luồng 2: Yêu cầu Set Quà tặng (B2B)
| Bước hành trình | Screen ID | Tên màn hình | Thành phần chính (Core Components) |
| :--- | :--- | :--- | :--- |
| **B1**: Vào mục Quà | `SCR_06` | **Corporate Gift Page** | Slide các set VIP, Form "Gửi yêu cầu chế tác/khắc logo". |

## 3. UI Components Guideline
- **Buttons**: Bo góc nhẹ (4px), hiệu ứng đổ bóng mờ (soft shadow).
- **Cards**: Border mỏng `#E0E0E0`, ảnh sản phẩm chiếm 70% diện tích card.
- **Badges**: Tag "SVIP" màu Vàng Hổ Phách, tag "VIP" màu Nâu Trầm.

## 4. Imagery & Media
- Ảnh sản phẩm phải chụp theo style Zen (đặt trên nền gỗ, cạnh chén trà hoặc hoa sen).
- Bắt buộc có video quay chậm làn khói trầm tan chảy (đối với nụ trầm thác khói) để kích thích giác quan.
