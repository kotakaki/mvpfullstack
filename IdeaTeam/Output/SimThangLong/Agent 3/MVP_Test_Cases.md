# MVP Test Cases
**Project**: Nền tảng E-commerce Sim Thăng Long (Clone)
**Version**: 1.0
**Author**: Agent 3 (MVP Documentation Agent)

## 1. Test Suite: Search & Filter (Tính năng Tìm Kiếm)
| Test ID | Tên chức năng | Quy trình test (Steps) | Kết quả mong đợi (Expected) | Trạng thái |
| :---: | :--- | :--- | :--- | :---: |
| **TC_S_01** | Tìm kiếm wildcard | 1. Vào trang chủ.<br>2. Nhập `*88` vào ô tìm kiếm.<br>3. Ấn Search. | Hiện các số bất kỳ kết thúc bằng `88`. | TBD |
| **TC_S_02** | Chọn mạng viễn thông | 1. Click vào Logo Mạng (vd: VinaPhone). | Chỉ hiển thị các đầu số thuộc VinaPhone (091, 094, 088...) | TBD |
| **TC_S_03** | Lọc theo giá kết hợp | 1. Chọn Mạng Viettel.<br>2. Kéo thanh trượt Giá từ 5 - 10 triệu.<br>3. Bấm Lọc. | Danh sách thỏa mãn đồng thời 2 điều kiện (Viettel & 5-10tr). | TBD |

## 2. Test Suite: Checkout (Thanh Toán & Đặt Hàng)
| Test ID | Tên chức năng | Quy trình test (Steps) | Kết quả mong đợi (Expected) | Trạng thái |
| :---: | :--- | :--- | :--- | :---: |
| **TC_C_01** | Đặt SIM mua đứt | 1. Chọn số có giá 10tr -> Click `Mua ngay`.<br>2. Điền form thiếu Số điện thoại -> Bấm Gửi.<br>3. Điền đủ Form -> Bấm Gửi. | 2. Báo lỗi Validator Form.<br>3. Đặt thành công, nhảy trang Thanks, sinh Order ID. | TBD |
| **TC_C_02** | Tính toán trả góp | 1. Chọn số giá 10tr -> Click `Trả góp`.<br>2. Chỉnh "Trả trước 50%" và "Kỳ hạn 6 tháng". | Hiển thị gốc phải trả: 5 triệu. Tháng trả: ~833.000 + Lãi. Công thức chuẩn. | TBD |

## 3. Test Suite: Concurrency (Tính Đóng Chốt)
| Test ID | Tên chức năng | Quy trình test (Steps) | Kết quả mong đợi (Expected) | Trạng thái |
| :---: | :--- | :--- | :--- | :---: |
| **TC_H_01** | Lock số khi Checkout | 1. Tải web làm 2 Tab khác IP (cho 1 số đặc biệt).<br>2. Tab A ấn Mua ngay (đang điền form).<br>3. Tab B F5 lại trang chi tiết. | Ở Tab B, hệ thống báo "Đang có khách giao dịch" hoặc nút Mua mờ đi trong 15p. | TBD |
