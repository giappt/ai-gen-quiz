# Workspace Rules

## Quy tắc chỉnh sửa ngữ nghĩa (Semantic Review)
Khi thực hiện review và chỉnh sửa câu giải thích (explanation) trong các file dữ liệu:
- **TUYỆT ĐỐI KHÔNG** sử dụng các thuật toán/script cắt gọt hàng loạt hay lệnh `replace` chuỗi một cách mù quáng (ví dụ: `replace("Thứ tự", "Mạch câu")`).
- **BẮT BUỘC** phải đọc ngữ cảnh của từng dòng/câu, hiểu ý nghĩa thực sự của nó.
- Nếu cần sửa, hãy viết lại nguyên cả câu (rewrite) sao cho tự nhiên và liền mạch bằng tiếng Việt.
- Xem chi tiết tại workflow `/manual-semantic-review` (file: `.agents/workflows/manual-semantic-review.md`).
