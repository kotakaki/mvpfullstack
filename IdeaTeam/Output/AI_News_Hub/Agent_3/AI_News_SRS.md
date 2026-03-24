# Software Requirements Specification (SRS): AI News Hub
**Project**: AI News Hub
**Version**: 1.0
**Author**: Agent 3 (MVP Documentation)

## 1. Functional Requirements

### 2.1 Thành phần Tự động hóa (Automated Factory)
**ID: FR_01**
- **Description**: Hệ thống phải tự quét ít nhất 10 nguồn/giờ.
- **Rules**: Không đăng tin trùng lặp (Deduplication bằng Embeddings).
- **Quality**: Bài viết tiếng Việt phải tự nhiên, không bị "mùi Google Translate".

### 2.2 Tương tác người dùng (User Interaction)
**ID: FR_02**
- **Description**: Cho phép sếp click "Generate Employee Prompt" để lấy đoạn text hướng dẫn nhân viên.
- **Sharing**: Tích hợp nút share nhanh qua Zalo, Messenger, Slack.

## 2. Non-Functional Requirements
- **Reliability**: Hệ thống phải Fact-check chéo. Nếu Agent Fact-checker báo lỗi > 50%, bài viết sẽ bị pending đợi PO duyệt (Fail-safe).
- **Usability**: Reader UI phải tối giản, font chữ to dễ đọc cho chủ doanh nghiệp.
- **Integrations**: Webhook đẩy tin sang Group Telegram/Zalo nội bộ.
