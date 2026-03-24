# Quy tắc: Yêu cầu đầu vào watchlist cho Agent 2

`Agent_2_Social_Public_Intelligence` chỉ nên bắt đầu quét khi đầu vào đủ tối thiểu để truy ra hồ sơ công khai và nối lại với danh sách gốc.

## Trường bắt buộc
- `Mã bản ghi`
- `Tên bản ghi gốc`
- Ít nhất một điểm vào công khai:
  - URL hồ sơ LinkedIn
  - URL hồ sơ X/Twitter
  - URL trang Facebook công khai
  - URL kênh YouTube
  - URL website công ty
  - tên công ty kèm tên người cần theo dõi

## Trường nên có
- `Tên người / công ty`
- `Persona mục tiêu`
- `Vai trò`
- `Lý do cần theo dõi`
- `Mức ưu tiên từ Agent 1`
- `ICP mục tiêu` nếu có

## Phân loại mức sẵn sàng đầu vào
- `Quét ngay`:
  - Có `Mã bản ghi`
  - Có ít nhất một URL công khai hoặc một cặp `Tên công ty + Tên người`
- `Quét hạn chế`:
  - Có `Mã bản ghi`
  - Chỉ có tên công ty hoặc domain
  - Chỉ nên quét cấp công ty hoặc trang thương hiệu
- `Chưa đủ điều kiện`:
  - Thiếu `Mã bản ghi`
  - Không có URL, không có domain, không có cặp tên đủ rõ để tra cứu

## Quy tắc nhận đầu vào từ Agent 1
- Agent 2 không tự tạo `Mã bản ghi`.
- Nếu danh sách từ Agent 1 chưa có `Mã bản ghi`, phải trả về yêu cầu bổ sung.
- Nếu bản ghi chỉ có website công ty nhưng không có hồ sơ mạng xã hội rõ ràng, Agent 2 chỉ được quét các trang social công khai của công ty.
- Nếu bản ghi là cá nhân, phải ghi rõ đang quét cấp cá nhân hay cấp công ty để tránh trộn tín hiệu.

## Quy tắc fallback
- Ưu tiên URL trực tiếp trước.
- Nếu không có URL trực tiếp, được phép tra cứu từ:
  - tên công ty
  - tên người
  - domain công ty
- Nếu sau một vòng tra cứu vẫn không xác định được hồ sơ công khai đáng tin cậy, phải gắn trạng thái `Không đủ dữ liệu để quét social`.
