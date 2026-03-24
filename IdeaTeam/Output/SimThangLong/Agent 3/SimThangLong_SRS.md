# Software Requirements Specification (SRS)
**Project**: Nền tảng E-commerce Sim Thăng Long (Clone)
**Version**: 1.0
**Author**: Agent 3 (MVP Documentation Agent)

## 1. Introduction
SRS này định nghĩa các yêu cầu chức năng và phi chức năng cho MVP của nền tảng bán SIM đa mạng dành cho thị trường Việt Nam.

## 2. Functional Requirements

### 2.1. Cổng Tìm kiếm & Lọc (Search & Filter Gateway)
**ID: FR_01**
- **Description**: Cho phép tìm kiếm ngẫu nhiên, theo cú pháp wildcard (vd: `*8888`), kết hợp với bộ lọc (Nhà mạng, Giá, Đầu số).
- **Inputs**: Từ khóa người dùng, lựa chọn Dropdown.
- **Outputs**: Danh sách Grid/List SIM phù hợp, Update URL params (để dễ chia sẻ link SEO).
- **Constraints**: Response time < 200ms bằng Elasticsearch.

### 2.2. Chức năng Thanh Toán (Checkout System)
**ID: FR_02**
- **Description**: Gồm 3 hình thức: Trả thẳng, Mua trả góp, Thuê SIM.
- **Inputs**: Hình thức thanh toán, Thông tin người mua (có validation định dạng sđt VN).
- **Outputs**: Mã Đơn Hàng (Order ID), trạng thái Pending. Gửi Webhook sang ERP nội bộ.

### 2.3. Khóa giỏ hàng tạm thời (Locking Mechanism)
**ID: FR_03**
- **Description**: Ngăn chặn tình trạng 1 SIM được giao dịch bởi 2 khách hàng cùng lúc.
- **Thực thi**: Khi khách ấn "Mua ngay", khóa state trong 15 phút. Hiển thị UI countdown.

## 3. External Interface Requirements

### 3.1. User Interfaces
- Giao diện đáp ứng (Responsive) 100%. Ưu tiên Mobile-First vì 80% khách hàng tìm SIM trên điện thoại.
- Màu sắc chủ đạo nhất quán với nhận diện thương hiệu.

### 3.2. Hardware Interfaces
- None required (Thuần túy phần mềm đám mây).

### 3.3. API/Software Interfaces
- Cổng tích hợp API Gửi tin nhắn SMS ZNS Zalo để gửi xác nhận đơn hàng thành công.
- Cổng Elasticsearch nội bộ (chỉ server-to-server).

## 4. Logical Database Requirements
- Tuân thủ Schema trong tài liệu SDD của Agent 2.
- Áp dụng Indexing mạnh trên cột `PhoneNumber` và `FormatNumber` trong Postgres để query cơ bản khi ES bảo trì.

## 5. Non-functional Requirements (NFR)
- Bảo mật (Tuân thủ luật An ninh mạng).
- Uptime 99.9%.
- Hệ thống Audit Logs lưu lại nhân viên nào đã sửa giá của SIM nào.
