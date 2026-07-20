---
name: manual-semantic-review
description: Quy trình rà soát và chỉnh sửa ngữ nghĩa thủ công (Tuyệt đối không dùng script replace hàng loạt)
---

# Mục đích
Quy trình này đảm bảo chất lượng của việc sửa lỗi ngữ nghĩa trong các file CSV. Tránh việc sửa chữa máy móc bằng công cụ thay thế chuỗi tự động (như `replace` trong Python hay `regex`), giúp câu văn tiếng Việt tự nhiên và trôi chảy.

# Nguyên tắc tối thượng
- **KHÔNG SỬ DỤNG LỆNH REPLACE HÀNG LOẠT** để thay thế cụm từ, ngay cả khi chúng có vẻ lặp lại.
- Phải đọc ngữ cảnh của từng câu trước khi sửa.

# Các bước thực hiện (Step-by-step)

1. **Khảo sát (Scanning):**
   - Được phép dùng script Python để quét toàn bộ file nhằm tìm ra *vị trí* các file/dòng bị lỗi (ví dụ: in ra console danh sách file và dòng có chứa từ khóa cứng nhắc).

2. **Duyệt thủ công (Manual Review):**
   - Mở trực tiếp các file CSV bị lỗi thông qua các script hoặc chỉnh sửa thủ công.
   - Không được dùng hàm `.replace()` cho cả batch. Nếu phải sửa nhiều, có thể viết script nhưng logic của script phải sửa **TOÀN BỘ CÂU** (rewrite sentence) thay vì chỉ thay một cụm từ.

3. **Chỉnh sửa ngữ nghĩa (Semantic Rewrite):**
   - Đọc hiểu ngữ cảnh của câu. 
   - Viết lại câu sao cho tự nhiên nhất trong tiếng Việt, đảm bảo tính sư phạm. 
   - Ví dụ: Thay vì đổi "Thứ tự câu:" thành "Mạch câu:", hãy viết lại cả câu "Mạch câu diễn tiến tự nhiên từ..." sao cho khớp với các thành phần khác.

4. **Kiểm tra mã hóa (Encoding Check):**
   - Lưu ý khi ghi đè hoặc tạo mới file CSV, phải luôn sử dụng `encoding='utf-8-sig'` để tránh lỗi font tiếng Nhật/tiếng Việt.

5. **Báo cáo (Reporting):**
   - Trình bày cho người dùng những câu cụ thể đã được viết lại.
