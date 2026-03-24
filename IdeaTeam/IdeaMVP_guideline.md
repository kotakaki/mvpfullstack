# Elite Agent Documentation Framework: Global Guideline (PO Edition)

## Chương 1: Triết lý & Giá trị cốt lõi

Hệ thống **Elite Agent Documentation Framework** là một quy trình khép kín gồm **5 Agent** chuyên biệt, phối hợp để chuyển đổi một ý tưởng thô thành bộ hồ sơ dự án MVP hoàn chỉnh và tài liệu thiết kế UI/UX chuyên nghiệp.

### 1.1 Triết lý JTBD
Mọi sản phẩm được tạo ra không phải để tồn tại vì tính năng, mà để giải quyết một "công việc" cốt lõi của người dùng. Framework bắt buộc các Agent phải liên tục đặt câu hỏi: *"Sản phẩm này được thuê để làm gì?"* và loại bỏ mọi phần thừa không phục vụ mục tiêu đó.

### 1.2 Mô hình 5 Agent chuyên biệt
1. **LearnAgent (Research & Strategy)**: Thu thập tri thức từ website đối thủ/thị trường (KWSR).
2. **Agent 1 (Intake & Strategy)**: Định hình `What & Why` - Cấu trúc BRD/PPD/SDK.
3. **Agent 2 (Architecture)**: Định hình `How` - Cấu trúc kỹ thuật SDD.
4. **Agent 3 (Detailing)**: Định hình `Quality & Detail` - Cấu trúc PRD/SRS/Test Cases.
5. **Agent 4 (UI/UX Designer)**: Định hình `Look & Feel` - Cấu trúc Design Specs.

---

## Chương 2: Lộ trình phát triển sản phẩm

### Phase 0: Knowledge Acquisition (LearnAgent)
Dịch ngược (Reverse-engineering) website đối thủ để lấy User Flow, Business Model, Features và NFR thực tế.

### Phase 1: Business Strategy (Agent 1)
Làm rõ bài toán, người dùng, JTBD thông qua 3 kịch bản: Idea Driven, Proposal Driven, hoặc Source Driven (từ LearnAgent).
> [!IMPORTANT]
> **BRD bắt buộc phải có**: Business Process Flow chi tiết và Khai thác yêu cầu phi chức năng (NFR).

### Phase 2: Technical Design (Agent 2)
Thiết kế kiến trúc, DB Schema và API Design dựa trên BRD của Agent 1.

### Phase 3: Documentation & QA (Agent 3)
Hệ thống hóa yêu cầu chi tiết (SRS/PRD) và viết Test Cases đồng bộ với logic nghiệp vụ.

### Phase 4: Visual Design (Agent 4)
Chuyển đổi yêu cầu thành giao diện.
> [!IMPORTANT]
> **Design Specs bắt buộc phải có**: Screen Inventory được đánh mã và map trực tiếp với User Flow trong PRD/BRD.

---

## Chương 3: Cấu trúc output chuẩn

Mỗi dự án trong `Output/[Project_Name]/` phải được tổ chức theo các thư mục:

- `LearnAgent/`: Dữ liệu nghiên cứu thô và phân tích đối thủ.
- `Agent 1/`: `[Project]_BRD.md`, `[Project]_PPD.md`, `[Project]_SDK.md`.
- `Agent 2/`: `[Project]_Solution_Design.md`.
- `Agent 3/`: `MVP_PRD.md`, `[Project]_SRS.md`, `MVP_Test_Cases.md`.
- `Agent 4/`: `Design_Specs.md`, `Screens/`.

Tại thư mục gốc dự án:
- `Master_Project_Index.md`: Bản đồ điều hướng toàn bộ hồ sơ.

---

## Chương 4: Vai trò & Yêu cầu cụ thể của Tài liệu

### 4.1 Agent 1: Bộ 3 Quyền lực
- **BRD**: Kim chỉ nam nghiệp vụ. **BẮT BUỘC** mô tả luồng quy trình (Business Process Flow) và các ràng buộc phi chức năng (NFR).
- **PPD**: Định vị thị trường và chân dung khách hàng mục tiêu.
- **SDK**: Bộ nguyên liệu Social Proof và nội dung bán hàng.

### 4.2 Agent 4: Design Specs chuẩn Elite
- Phải có **Screen Inventory**: Danh sách tất cả màn hình cần thiết kế.
- Phải khớp với **User Flow**: Đảm bảo không bỏ sót bước nào trong hành trình trải nghiệm người dùng.

---

## Chương 5: Quản trị & vận hành

1. **Living Document Policy**: Guideline này phải được cập nhật ngay khi thay đổi quy tắc.
2. **Strict Handover**: Agent sau kế thừa dữ liệu của Agent trước, mọi thay đổi scope lớn phải được PO phê duyệt.
3. **Consistency Rule**: Tên dự án, tên file và thuật ngữ phải nhất quán xuyên suốt 5 Agent.
4. **Relative Path Rule**: Tất cả các liên kết (links) trong tài liệu và `Master_Project_Index.md` bắt buộc phải sử dụng **đường dẫn tương đối (Relative Path)**. Tuyệt đối không sử dụng đường dẫn tuyệt đối (Absolute Path) hoặc định dạng `file:///d:/` để đảm bảo tính di động của hồ sơ.

---
*Elite Agent Documentation Framework - Standardizing Excellence.*
