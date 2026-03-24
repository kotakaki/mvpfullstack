# Kỹ năng: Tiếp nhận danh sách và gán mã bản ghi

## Mục tiêu
Biến danh sách đầu vào do người dùng cung cấp thành tập bản ghi sạch, có thể làm giàu tiếp bởi Agent 2 và Agent 3.

## Các bước chính
1. Đọc cấu trúc danh sách gốc.
2. Xác định mỗi dòng là lead cá nhân, lead công ty hoặc bản ghi hỗn hợp.
3. Gán `Mã bản ghi` nếu danh sách chưa có.
4. Chuẩn hóa các trường nhận diện như tên công ty, domain, LinkedIn, role.
5. Đánh dấu dòng nào đủ điều kiện chuyển sang Agent 2 và Agent 3.

## Kết quả cần có
- danh sách đầu vào đã được chuẩn hóa
- `Mã bản ghi` ổn định cho từng dòng
- ghi chú rõ dòng nào:
  - đủ để quét social
  - đủ để quét website
  - thiếu dữ liệu để làm giàu thêm

## Lỗi thường gặp
- đổi thứ tự bản ghi rồi làm mất liên kết với danh sách gốc
- không tách rõ tên người và tên công ty
- thiếu field nhận diện nhưng vẫn đưa sang Agent 2 hoặc Agent 3
