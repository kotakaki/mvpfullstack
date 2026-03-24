# Quy tắc: Ma trận định tuyến enrichment

## Mục tiêu
Quy định khi nào một bản ghi nên được chuyển sang Agent 2, Agent 3 hoặc giữ lại ở Agent 1.

## Ma trận định tuyến
- Nếu có `LinkedIn`, `URL hồ sơ social` hoặc dấu hiệu nhận diện social rõ:
  - `Chuyển Agent 2`: `Có`
- Nếu có `Website công ty` hoặc `Domain`:
  - `Chuyển Agent 3`: `Có`
- Nếu có cả social handle và website/domain:
  - chuyển cả Agent 2 và Agent 3
- Nếu chỉ có tên công ty hoặc tên người mà không có field nhận diện để quét tiếp:
  - `Chuyển Agent 2`: `Thiếu dữ liệu`
  - `Chuyển Agent 3`: `Thiếu dữ liệu`
- Nếu bản ghi đang ở trạng thái `Có thể trùng`:
  - không chuyển tiếp cho đến khi Agent 1 xử lý xong bước loại trùng

## Quy tắc
- Không suy diễn social profile hoặc website chỉ dựa trên tên nếu chưa có bằng chứng.
- Không chuyển bản ghi sang Agent 2 hoặc Agent 3 khi trường nhận diện còn mơ hồ.
- Nếu một bản ghi chỉ đủ điều kiện cho một agent, agent còn lại phải để `Không` hoặc `Thiếu dữ liệu`, không để trống.
