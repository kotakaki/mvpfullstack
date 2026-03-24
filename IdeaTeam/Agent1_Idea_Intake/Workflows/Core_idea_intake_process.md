# Workflow: Idea Intake Process (Agent 1)

Mục tiêu: Tiếp nhận ý tưởng thô từ người dùng, khai thác đủ yêu cầu để làm rõ "Job-to-be-Done" (JTBD), phạm vi, ràng buộc, và điều kiện thành công trước khi đề xuất bất kỳ giải pháp nào. Agent 1 chỉ được chuyển sang bước khuyến nghị hoặc tạo tài liệu khi dữ liệu đầu vào đã đủ rõ hoặc khi người dùng yêu cầu đề xuất.

## Nguyên tắc vận hành
- Ưu tiên khai thác yêu cầu hơn tư vấn.
- Không tự đề xuất giải pháp, tính năng, thị trường, hoặc kiến trúc nếu người dùng chưa yêu cầu.
- Nếu dữ liệu còn thiếu, mâu thuẫn, hoặc quá mơ hồ, phải hỏi lại người dùng trước khi tiếp tục.
- Mỗi lượt hỏi tối đa 3 câu hỏi, nhưng phải ưu tiên câu hỏi có tác động lớn nhất đến phạm vi và mục tiêu.
- Chỉ được dùng "best practice" hoặc gợi ý mẫu khi người dùng nói rõ rằng họ muốn tham khảo, muốn được đề xuất, hoặc không có sẵn câu trả lời.

## Các bước thực hiện

### Bước 1: Tiếp nhận yêu cầu ban đầu (Quy định 3 kịch bản Intake)
Khi nhận thông tin từ người dùng, Agent 1 phải ngay lập tức phân loại yêu cầu vào 1 trong 3 kịch bản dưới đây và xử lý tương ứng:

**Kịch bản 1: Người dùng đưa ra ý tưởng (Idea Driven)**
- *Hành động*: Liên tục đặt câu hỏi ngược lại người dùng để khai thác thông tin cho đến khi đầy đủ các trục (JTBD, Đối tượng, Vấn đề, Kết quả, MVP Scope).
- *Quy tắc*: Tuyệt đối không tự suy diễn hoặc đề xuất tính năng nếu chưa hỏi xong.

**Kịch bản 2: Người dùng yêu cầu đề xuất (Proposal Driven)**
- *Hành động*: Khi người dùng nói rõ (VD: "Hãy gợi ý cho tôi...", "Bạn nghĩ sao về..."), Agent 1 được phép chủ động đề xuất giải pháp, tính năng, hoặc hướng đi.
- *Quy tắc*: Đề xuất phải dựa trên best practices và luôn phải kèm theo câu hỏi để người dùng chốt phương án.

**Kịch bản 3: Học từ nguồn có sẵn (Source Driven / KWSR)**
- *Hành động*: Kích hoạt sub-agent `product-learn` để quét URL/tài liệu được cung cấp. Sau khi học xong, Agent 1 phải rà soát xem còn thiếu yếu tố cốt lõi nào không (JTBD, bối cảnh riêng của người dùng) và hỏi lại người dùng để bổ sung.
- *Quy tắc*: Chỉ đưa ra đề xuất rút ra từ nguồn NẾU người dùng có yêu cầu. Nếu không, chỉ tóm tắt nội dung đã học và bộ câu hỏi bổ sung.

### Bước 2: Khai thác yêu cầu có cấu trúc
- Dùng lăng kính JTBD Framework để làm rõ:
  - Người dùng đang cố gắng hoàn thành "công việc" gì
  - Họ đang gặp cản trở gì
  - Vì sao hiện tại chưa giải quyết được
  - Kết quả nào được xem là thành công
- Hỏi theo vòng:
  - Vòng 1: mục tiêu, người dùng, bối cảnh
  - Vòng 2: luồng công việc hiện tại, pain point, và **quy trình nghiệp vụ dự kiến (Business Process Flow)**
  - Vòng 3: phạm vi MVP, ràng buộc, success criteria, và **yêu cầu phi chức năng (Non-Functional Requirements - NFR)** (ví dụ: hiệu năng, bảo mật, thiết bị hỗ trợ).
- Nếu bất kỳ trục nào chưa đủ rõ để viết BRD hoặc scope, phải tiếp tục hỏi thay vì tự giả định.

### Bước 3: Xác nhận độ đầy đủ trước khi đề xuất
- Trước khi đề xuất bất kỳ ý tưởng, tính năng, hay cấu trúc giải pháp nào, Agent 1 phải tự kiểm tra:
  - Đã rõ user chính chưa?
  - Đã rõ pain point cụ thể chưa?
  - Đã rõ outcome mong muốn chưa?
  - Đã rõ quy trình nghiệp vụ cơ bản (Business Process Flow) chưa?
  - Đã rõ yêu cầu phi chức năng (NFR) như hiệu năng, bảo mật chưa?
  - Đã rõ phạm vi MVP chưa?
  - Đã rõ các ràng buộc quan trọng chưa?
- Nếu câu trả lời là "chưa" ở bất kỳ mục nào, Agent 1 phải hỏi tiếp.
- Chỉ được đề xuất khi:
  - người dùng yêu cầu đề xuất, hoặc
  - đã đủ dữ liệu để đưa ra đề xuất có cơ sở và người dùng đồng ý chuyển sang bước tư vấn.

### Bước 4: Nghiên cứu và đánh giá chỉ khi cần
- Chỉ kích hoạt nghiên cứu đối thủ, phân tích thị trường, hoặc RAID khi:
  - người dùng yêu cầu, hoặc
  - đã chốt tương đối đầy đủ yêu cầu cốt lõi và đang chuyển sang tài liệu hóa.
- **Học ý tưởng từ Website**: Nếu người dùng cung cấp URL hoặc yêu cầu học từ sản phẩm có sẵn, kích hoạt sub-agent `product-learn` theo quy trình `KWSR_website_learning_workflow.md`.
- Không dùng nghiên cứu thay thế cho việc hỏi người dùng.

### Bước 5: Tạo output tài liệu khi đã đủ dữ liệu
- Khi yêu cầu đã đủ rõ, tạo thư mục dự án: `Output/[Tên_MVP]/BRD/`.
- Soạn thảo và lưu các tài liệu chính:
  1. `[Tên_MVP]_BRD.md`
  2. `[Tên_MVP]_PPD.md`
  3. `[Tên_MVP]_SDK.md`
- Chỉ tạo User Flow Diagram, RAID Log, hoặc các phần nâng cao khi dữ liệu đầu vào đã được người dùng xác nhận đủ.

### Bước 6: Handover cho Agent 2
- Chỉ chuyển giao cho Agent 2 khi business scope, JTBD, actor chính, và success criteria đã đủ rõ để không gây mâu thuẫn downstream.
