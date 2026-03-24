# Workflow: KWSR Website Learning

Quy trình chuẩn để `LearnAgent` thực hiện việc học ý tưởng từ website.

## Bước 1: Tiếp nhận & Kiểm tra URL
1. Nhận URL từ người dùng hoặc Agent 1.
2. Kiểm tra tính hợp lệ của URL và khả năng truy cập.
3. **Sitemap Discovery (Bắt đầu tại đây)**:
   - Tìm kiếm `sitemap.xml` hoặc `robots.txt`.
   - Sử dụng kỹ thuật `Sitemap_Parser_and_URL_Extraction.md` để lấy toàn bộ danh sách URL.
   - Lập bản đồ (Site Map) của website doanh nghiệp để xác định các trang "Vàng" cần nghiên cứu sâu.

## Bước 2: Quét nội dung (Web Scraping)
1. Truy cập trang chủ để nắm bắt thông điệp chính (Hero Section).
2. Quét các trang con quan trọng:
   - **Features/Product**: Tìm kiếm các tính năng thực tế.
   - **Pricing**: Hiểu về mô hình kinh doanh và phân khúc khách hàng.
   - **About/Mission**: Hiểu về tầm nhìn và bài toán họ đang giải quyết.
3. Sử dụng kỹ thuật `KWSR_web_extraction_techniques.md` để lọc nhiễu.

## Bước 3: Phân tích & Trích xuất (Idea Extraction & Synthesis)
### 3.1. Cấu trúc & Tính năng (Product Capabilities)
1. Xác định **JTBD**: Người dùng "thuê" sản phẩm này để làm gì?
2. **Reverse Engineering User Flows**: Sử dụng `User_Flow_Reverse_Engineering.md` để vẽ lại luồng người dùng chính.
3. **Information Architecture (IA)**: Sử dụng `Information_Architecture_Synthesis.md` để mô tả cấu trúc phân cấp thông tin.
4. **Feature Inventory**: Sử dụng `Feature_Inventory_Synthesis.md` để liệt kê danh sách chức năng thực tế.

### 3.2. Thị trường & Định vị (Market & Positioning)
1. **Target Audience**: Sử dụng `Target_Audience_and_Persona_Reverse_Engineering.md` để vẽ chân dung người dùng mục tiêu.
2. **Business Model**: Sử dụng `Pricing_and_Business_Model_Analysis.md` để hiểu ranh giới thu phí và luồng nâng cấp.
3. **Social Proof**: Sử dụng `Social_Proof_and_Positioning_Extraction.md` để thu thập case studies và metrics.

### 3.3. Dấu vết Công nghệ (Footprinting)
1. **NFR & Tech Stack**: Sử dụng `NFR_and_Tech_Stack_Footprinting.md` để bóc tách tiêu chuẩn bảo mật, nền tảng, và hiệu năng.

## Bước 4: Tổng hợp & Bàn giao
1. Tóm tắt các ý tưởng học được bằng ngôn ngữ chuyên môn theo 3 trục: Sản phẩm, Thị trường, Kỹ thuật.
2. Cung cấp các Artifacts và Data Lists sẵn sàng cho Agent 1:
   - Sơ đồ User Flow (cho BRD).
   - Danh sách tính năng theo phân loại (cho BRD).
   - Bản mô tả cấu trúc IA.
   - Target Persona & Business Model (cho PPD/BRD).
   - Danh sách NFR (cho BRD).
   - Ngân hàng nguyên liệu Social Proof (cho PPD/SDK).
3. Đề xuất các điểm tinh hoa có thể áp dụng cho dự án hiện tại.
4. Bàn giao để Agent 1 viết tài liệu chính thức.
