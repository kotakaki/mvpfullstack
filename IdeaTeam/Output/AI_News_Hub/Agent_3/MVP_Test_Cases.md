# MVP Test Cases: AI News Hub
**Project**: AI News Hub
**Version**: 1.0
**Author**: Agent 3 (MVP Documentation)

## 1. Test Suite: Automated Pipeline
| ID | Scenario | Steps | Expected Result |
| :--- | :--- | :--- | :--- |
| **TC_A_01** | Kiểm tra trùng lặp | 1. Thêm 2 bài viết cùng nội dung từ 2 nguồn.<br>2. Chạy pipeline xử lý. | Chỉ 1 bài được đăng, bài còn lại bị lọc bỏ (Deduplicated). |
| **TC_A_02** | Kiểm chứng Fact-check | 1. Đưa 1 tin giả vào nguồn.<br>2. Agent Fact-checker kiểm tra. | Bài báo phải bị dán nhãn Warning hoặc không được đăng. |

## 2. Test Suite: Feature Interaction
| ID | Scenario | Steps | Expected Result |
| :--- | :--- | :--- | :--- |
| **TC_F_01** | Sinh Prompt cho nhân viên | 1. Click "Generate Prompt" ở cuối bài báo. | AI sinh ra 1 đoạn text hướng dẫn hành động cụ thể, có cấu trúc tốt. |
| **TC_F_02** | Daily Briefing | 1. Thiết lập giờ nhận tin 8:00 AM. | Notification được đẩy đi đúng giờ với các bài highlight trong ngày. |
