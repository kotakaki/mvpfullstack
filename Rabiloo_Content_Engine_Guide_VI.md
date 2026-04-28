# Hướng dẫn sử dụng Rabiloo Content Engine (Công cụ sản xuất bài viết)

Tài liệu này là hướng dẫn dành cho nhóm để sử dụng "Content Engine (Quy trình sản xuất bài viết)" nhằm tạo ra các bài viết chất lượng cao, tuân thủ đúng văn phong và tiêu chuẩn (Tone & Manner) của Rabiloo bằng cách ứng dụng AI.

## 1. Content Engine là gì?

Công cụ này không chỉ là một công cụ "tự động tạo bài viết" đơn thuần khi bạn nhập từ khóa và chủ đề. Nó định nghĩa một quy trình **"hợp tác giữa người và AI để tạo ra bài viết chất lượng cao"**.

Để đảm bảo tính chuyên môn và thông tin gốc (E-E-A-T) đặc trưng của Rabiloo, AI sẽ không tự động viết từ đầu đến cuối. Thay vào đó, AI bắt buộc phải thông qua các bước **"Phê duyệt dàn ý"** và **"Kiểm tra từng chương"** (phương pháp phase-gate).

## 2. Cách sử dụng (Cách khởi động)

Hãy bắt đầu bằng cách gửi lệnh dưới đây cho Trợ lý AI (chat).

```text
/content-engine [Từ khóa mục tiêu] [Chủ đề hoặc bối cảnh bổ sung]
```

**【Ví dụ】**
> `/content-engine Vietnam offshore development Xu hướng mới nhất năm 2026 và kết hợp thế mạnh của Rabiloo (như HEDSPI)`

※ AI sẽ tự động đọc các quy tắc trong file `.agents/workflows/content-engine.md` và bắt đầu quy trình.

---

## 3. Quy trình 3 giai đoạn (Phase) sản xuất bài viết

Việc sản xuất bài viết sẽ diễn ra qua 3 giai đoạn dưới đây. **AI sẽ không chuyển sang giai đoạn tiếp theo nếu không có sự xác nhận/phê duyệt của con người (bạn).**

### PHASE 1: Đề xuất dàn ý (Thiết kế)
- AI sẽ đề xuất độc giả mục tiêu, mục đích tìm kiếm, ý tưởng tiêu đề, cấu trúc các thẻ Heading (H2, H3), và thông tin gốc dự kiến chèn vào.
- **Hành động của con người:** Đọc dàn ý và nếu không có vấn đề gì, hãy báo "OK" hoặc "Tiếp tục viết với dàn ý này". Nếu cần chỉnh sửa, hãy yêu cầu AI sửa lại ngay ở bước này.

### PHASE 2: Viết chi tiết từng chương (Viết nội dung)
- Sau khi dàn ý được phê duyệt, AI sẽ bắt đầu viết **từng chương một (từng phần H2)**.
- Viết xong 1 chương, AI sẽ dừng lại và yêu cầu bạn kiểm tra.
- **Hành động của con người:** Kiểm tra nội dung, yêu cầu bổ sung/chỉnh sửa, hoặc báo "OK, tiếp tục chương tiếp theo".

### PHASE 3: Hoàn thiện và tối ưu hóa
- Sau khi tất cả các chương hoàn thành, AI sẽ xem xét tổng thể, tạo phần FAQ, và đề xuất các liên kết nội bộ (internal link).
- Trải qua bước kiểm tra cuối cùng, bài viết sẽ hoàn thiện.

---

## 4. Các quy tắc thành viên trong nhóm cần tuân thủ

Để sử dụng hiệu quả công cụ này, hãy lưu ý các điểm sau:

1. **Không phó mặc hoàn toàn (Hãy tương tác với AI)**
   - Bắt buộc phải kiểm tra bằng mắt thường dàn ý do AI đề xuất (PHASE 1). Việc các điểm mạnh hay case study độc quyền của Rabiloo có được đưa vào đây hay không sẽ quyết định chất lượng bài viết.
2. **Thúc đẩy việc thêm thông tin gốc (Case study/Kinh nghiệm của công ty)**
   - AI có kiến thức chung, nhưng không có "tiếng nói thực tế từ hiện trường" của Rabiloo. Bằng cách chỉ thị "Hãy thêm case study về dự án 〇〇 vào chương này" khi duyệt dàn ý hoặc khi viết, tính độc bản (E-E-A-T) của bài viết sẽ tăng cao.
3. **Không được bỏ qua các giai đoạn (Skip phase)**
   - Nếu AI tự ý chạy trước và định viết toàn bộ bài, hãy yêu cầu: "Dừng lại. Chỉ đưa ra dàn ý của PHASE 1 trước" để bắt AI tuân thủ quy tắc.

## 5. Các sự cố thường gặp và cách khắc phục

*   **Q. AI viết sai quy tắc tên công ty Rabiloo**
    *   **A.** Công cụ đã được cài đặt quy tắc: lần đầu tiên xuất hiện phải là `Rabiloo（ラビロー）`, các lần sau là `Rabiloo`. Nếu AI viết sai, hãy nhắc: "Hãy sửa lại theo đúng quy tắc ghi tên công ty".
*   **Q. Ký hiệu in đậm (Markdown) bị lỗi (Khó copy & paste)**
    *   **A.** Công cụ đã có quy tắc "Đặt dấu in đậm ở bên trong dấu ngoặc (Ví dụ: `「**Quan trọng**」`)". Nếu bị lệch, hãy yêu cầu AI sửa lại.
*   **Q. Bài viết đơn điệu và nhàm chán**
    *   **A.** Khi viết ở PHASE 2, hãy yêu cầu tinh chỉnh Tone & Manner, ví dụ: "Hãy viết với giọng văn đồng cảm với người đọc hơn" hoặc "Hãy nhấn mạnh góc nhìn chuyên gia của Rabiloo".

---

> 💡 **Tip:** Quy trình làm việc này được quản lý tại file `.agents/workflows/content-engine.md`. Nếu muốn cải thiện quy trình, bạn có thể chỉnh sửa trực tiếp file này để nâng cấp cách AI hoạt động cho toàn bộ nhóm.
