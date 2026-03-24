# Solution Design Document (SDD) v2: WMS Architecture
**Project**: Warehouse Management System
**Version**: 2.0
**Author**: Agent 2 (Solution Architect)

## 1. High-Precision Architecture

### 1.1 Message Queue (Hệ thống hàng đợi)
Sử dụng **BullMQ (Redis-based)** để xử lý các tác vụ bất đồng bộ:
- Đồng bộ đơn hàng từ Shopee/Lazada (tránh quá tải API).
- Xử lý lệnh in nhãn hàng loạt (tránh treo giao diện người dùng).
- Gửi thông báo thông qua Webhook cho các hệ thống ERP bên thứ 3.

### 1.2 Printing Integration
Tích hợp dịch vụ **Browser-to-Print**:
- Sử dụng thư viện `jsprintmanager` hoặc `qz-tray` để gửi lệnh **ZPL/EPL** trực tiếp từ trình duyệt web mobile đến máy in Zebra/Xprinter thông qua mạng nội bộ (LAN/Wifi).

## 2. Database Schema (V2 Extensions)
- `Batches`: id, sku_id, batch_number, manufacturer_date, expiry_date, supplier_id.
- `Stock_Inventory`: (...bổ sung batch_id).
- `Inventory_Audits`: id, start_time, end_time, auditor_user_id, status (Pending/Approved).
- `Audit_Details`: audit_id, location_id, expected_qty, actual_qty, variance.

## 3. High Performance Strategies
- **Database Partitioning**: Phân vùng bảng `Warehouse_Logs` theo tháng để tối ưu truy vấn báo cáo lịch sử.
- **Optimistic Concurrency**: Sử dụng `version` column cho bảng Stock để xử lý tranh chấp dữ liệu khi nhiều người cùng thao tác.

## 4. Disaster Recovery
- Backup DB định kỳ mỗi 6 tiếng lên Cloud (AWS S3/GCS).
- Hệ thống có khả năng chuyển đổi sang Slave DB (Read Replica) trong vòng < 60 giây nếu Master gặp sự cố.
