# Design Specifications: AI News Hub
**Project**: AI News Hub
**Version**: 1.0
**Author**: Agent 4 (UI/UX Designer)

## 1. Design Strategy
- **Manager-Friendly**: Giao diện sạch sẽ, chuyên nghiệp, không màu mè. Font chữ Serif cao cấp cho tiêu đề (thông tin uy tín).
- **Color Palette**: Dark Mode (Xanh Navy đậm: `#0B132B`, Cam Accent: `#FF9F1C` cho các nút hành động).
- **Typography**: `Inter` cho nội dung, `Lora` cho tiêu đề phân tích.

## 2. Screen Inventory

### Luồng đọc tin tự động
| Bước | Screen ID | Tên màn hình | Core Components |
| :--- | :--- | :--- | :--- |
| **B1**: Dashboard | `SCR_01` | **CEO Dashboard** | 3 Tin Highlight (Carousel), Danh mục ROI High/Medium/Low. |
| **B2**: Bài phân tích | `SCR_02` | **Analysis Detail** | 2-min Brief Header, Implementation Roadmap Box, Action Button "Copy Prompt". |
| **B3**: Tư vấn | `SCR_03` | **AI Consultation Space** | Khung chat tư vấn chiến lược dựa trên tin tức. |

## 3. UI Concept
- **Card Design**: Mỗi card chứa bài báo có thêm badge "ROI Potential: High".
- **Action Button**: "Employee Instruction" (Nút nổi bật nhất bài viết).
