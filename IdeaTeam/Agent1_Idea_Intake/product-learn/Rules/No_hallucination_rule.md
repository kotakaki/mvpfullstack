# Rule: No Hallucination (Nghiêm cấm bịa đặt thông tin)

Quy tắc tối thượng áp dụng cho mọi tác vụ đọc và phân tích web của `product-learn`.

## 1. Chân thực tuyệt đối với văn bản gốc
- Chỉ được phép trích xuất những tính năng, thông số, hoặc lời hứa có xuất hiện **rõ ràng bằng văn bản** trên website.
- Không được dùng kiến thức bên ngoài về sản phẩm đó để tự ý "bù đắp" vào báo cáo nếu website không hề nhắc đến.

## 2. Cấm suy đoán vô căn cứ
- **SAI**: "Website này có tính năng A, do đó chắc chắn họ sẽ tích hợp AI để làm B."
- **ĐÚNG**: "Website liệt kê tính năng A. Trạng thái không đề cập đến tích hợp AI."
- Nếu không tìm thấy thông tin về một yếu tố nào đó (ví dụ: Pricing), phải ghi rõ là `"Không tìm thấy thông tin trên trang"`, tuyệt đối không tự bịa ra một mức giá giả định.

## 3. Trích dẫn nguyên văn (Quoting)
- Khi nhắc đến Core Value hoặc JTBD quan trọng, hãy cố gắng đặt câu từ của bản thân website vào trong dấu ngoặc kép `""` để Agent 1 có thể thấy được ngôn ngữ gốc của nguồn.
