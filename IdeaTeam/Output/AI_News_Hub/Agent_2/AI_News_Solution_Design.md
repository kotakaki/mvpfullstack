# Solution Design Document (SDD): AI News Hub
**Project**: AI News Hub
**Version**: 1.0
**Author**: Agent 2 (Solution Architect)

## 1. System Architecture
Kiến trúc **Agentic Workflow Service** (Sử dụng LangChain/LangGraph - hoặc mô hình Agent độc lập).

- **Pipeline Components**:
  - **Fetcher Service**: Node.js/Python crawler (Puppeteer/Playwright) quét RSS và các trang web chỉ định.
  - **LLM Processing (GPT-4/Claude 3)**: 
    - Agent A: Tóm tắt & Dịch.
    - Agent B: Trích xuất ROI & Roadmap.
    - Agent C: Kiểm chứng (Fact-checker).
  - **Database**: PostgreSQL (Store metadata) + Vector Database (Pinecone/Milvus) để hỗ trợ "Chat with News".
  - **CMS**: Headless CMS (Strapi/Directus) tích hợp Next.js Frontend.

## 2. Automation Flow
1. Trình dọn dẹp dữ liệu (Cleaning) -> 2. Agent xử lý -> 3. Auto-SEO Tagging -> 4. Auto-Thumbnail (DALL-E 3/Midjourney) -> 5. Đăng bài -> 6. Push thông báo Social.

## 3. Database Schema
- `Articles`: title, summary, roi_score, implementation_roadmap (JSON), source_url, publish_date.
- `Categories`: Retail, HR, Marketing, Operations.
- `Users`: Subscription status (Free/Premium).

## 4. Scalability
- Sử dụng Serverless Functions (AWS Lambda/Vercel) để tiết kiệm chi phí cho các agent chỉ chạy định kỳ.
- Redis để cache kết quả tóm tắt cho hàng nghìn khách truy cập cùng lúc.
