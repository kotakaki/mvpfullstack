# Quy tắc: Nhật ký thay đổi profile

Agent 2 phải tách `thay đổi profile` ra khỏi `tín hiệu social`.

## Loại thay đổi cần theo dõi
- đổi headline hoặc bio
- đổi vai trò / công ty hiện tại
- đổi link bio, website, CTA
- đổi bài ghim hoặc nội dung nổi bật
- đổi chủ đề nội dung chính
- đổi nhịp đăng hoặc mức độ hoạt động
- đổi giọng điệu hoặc thông điệp lặp lại

## Mẫu ghi log
```md
### Thay đổi profile 01
- Ngày phát hiện:
- Profile ID:
- Loại thay đổi:
- Trạng thái cũ:
- Trạng thái mới:
- Thay đổi quan sát được:
- Vì sao đáng chú ý:
- Mức chú ý:
- Có tạo tín hiệu mới không:
- Có cập nhật baseline không:
- Lý do cập nhật baseline:
- Refs:
```

## Quy tắc
- `Trạng thái cũ` phải lấy từ baseline hoặc log trước đó.
- `Trạng thái mới` chỉ ghi điều quan sát được ở lần quét này.
- Nếu thay đổi profile dẫn tới một tín hiệu chăm sóc mới, phải nối sang `Mã tín hiệu`.
- Nếu thay đổi chỉ mang tính hình thức và không có ý nghĩa vận hành, vẫn có thể ghi log nhưng để `Mức chú ý: Thấp`.
- Không cập nhật baseline trước khi ghi change log.
- Trường `Có cập nhật baseline không` phải bám theo `Baseline_Update_Decision_Rule.md`.
