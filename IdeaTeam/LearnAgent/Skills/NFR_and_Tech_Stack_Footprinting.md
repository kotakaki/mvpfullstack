# Skill: NFR & Tech Stack Footprinting

Kỹ thuật "đánh hơi" các yêu cầu phi chức năng (Non-Functional Requirements) và đặc tính công nghệ thông qua dấu vết để lại trên website.

## 1. Mục tiêu (Objective)
Thu thập tự động các tiêu chuẩn về bảo mật, hiệu năng, nền tảng hỗ trợ mà thị trường (hoặc đối thủ) đang áp dụng, từ đó làm cơ sở thiết lập NFR cho dự án của mình.

## 2. Nguồn dữ liệu cần phân tích (Data Sources)
- **Footer**: Cuối trang thường chứa liên kết đến "Security", "Privacy", "Compliance", "Terms".
- **Badges/Certificates**: Các logo chứng nhận (SOC 2, GDPR, ISO 27001, HIPAA).
- **Thẻ Meta / HTTP Headers / Console**: Nhận biết sơ bộ công nghệ (vd: Next.js, React, Tailwind, AWS).
- **Download/App Platform**: Khả năng tương thích nền tảng (Web, iOS, Android, Mac, Windows, Linux).

## 3. Quy trình thực hiện (Execution Steps)

### Bước 1: Quét nền tảng và tương thích (Platform & Availability)
- Sản phẩm có App Mobile không? (Tìm logo App Store \u0026 Google Play).
- Sản phẩm có Extension trình duyệt không?
- Ứng dụng là Web-based hay Desktop App?

### Bước 2: Quét tiêu chuẩn Bảo mật & Tuân thủ (Security & Compliance)
- Tìm kiếm từ khóa: "SOC 2 Type II", "GDPR / CCPA Compliant", "End-to-end encryption", "SSO/SAML".
- Đọc lướt trang `/security` để xem họ cam kết gì về vị trí lưu trữ máy chủ (Data residency).

### Bước 3: Quét cam kết Hiệu năng (Performance & Reliability)
- Tìm trang `/status` (Status-page) nếu có để xem SLA (vd: 99.99% uptime).
- Tìm các keyword như "Real-time", "Lightning fast", "Offline support".

## 4. Output
Một danh sách các NFR thị trường đang dùng, trích xuất cho Agent 1 đưa vào phần **6. Non-Functional Requirements (NFR)** của tệp BRD.
