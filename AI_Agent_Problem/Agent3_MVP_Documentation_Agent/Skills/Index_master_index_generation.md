# Skill: Master Project Index Generation

Mục tiêu: Tạo ra một "Trang chủ" (Wiki) cho toàn bộ dự án để điều hướng dễ dàng.

## 1. Cấu trúc Master Project Index
Tệp `Master_Project_Index.md` phải bao gồm:
- **Project Identity**: Tên dự án, Slogan, Phiên bản.
- **Executive Summary**: Tóm tắt giá trị dự án trong 3-5 câu.
- **Documentation Map (Sitemap)**: Bảng liên kết đến tất cả tài liệu:
    - Kinh doanh (BRD, PPD, SDK).
    - Kỹ thuật (SDD, API, Schema).
    - Vận hành (Manuals, Roadmap).
- **Current Status**: Trạng thái hiện tại của dự án (Concept/MVP/Scaling).

## 2. Automation Logic
Agent 3 tự động quét các thư mục `Output/` để cập nhật index mỗi khi có tệp mới được tạo ra.
