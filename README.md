# AI-Gen Quiz Pipeline

Repository này là một submodule độc lập, đóng vai trò chứa toàn bộ dữ liệu (Templates, Filled CSVs, Cleaned CSVs) và các script tự động hóa (Cleaning, Auto-Heal, Validate) phục vụ cho tính năng sinh đề trắc nghiệm JLPT bằng AI (Claude).

Mục tiêu của submodule này là giữ cho repository chính không bị quá tải bởi hàng chục nghìn file CSV, đồng thời cho phép Data Team làm việc độc lập.

## 📂 Cấu trúc thư mục

- `mondai1_fill_blank/` và `mondai2_ordering/`: Chứa dữ liệu của từng dạng bài tập.
  - `csv_templates/`: Các file CSV chứa cấu trúc gốc (Original Example, Grammar...). Bạn sẽ gửi file này cho AI.
  - `csv_filled/`: Kết quả sau khi AI sinh xong. Bạn chép (copy/paste) dữ liệu từ AI đè vào các file trong thư mục này.
  - `csv_cleaned/`: Dữ liệu đã qua làm sạch và sẵn sàng chuẩn bị import vào DB (được gen ra bởi script `clean`).
- `scripts/`: Chứa các tool nội bộ hỗ trợ dọn dẹp và kiểm định chất lượng (QA).

## 🛠️ Hướng dẫn cài đặt

Vì thư mục này có thể chạy độc lập, trước khi bắt đầu, hãy cài đặt các thư viện cần thiết:
```bash
npm install
```
*(Yêu cầu Node.js >= 16)*

## 🚀 Các Script cốt lõi & Quy trình sử dụng

Dưới đây là vòng đời thao tác dữ liệu AI-Gen chuẩn mực (AI-Gen Data Pipeline Lifecycle):

### Bước 1: Dọn dẹp & Định dạng lại (Clean)
Sau khi bạn đã ném kết quả của AI vào thư mục `csv_filled/`, định dạng của AI thường rất lộn xộn (thừa ngoặc kép, sai tên cột, sai cấu trúc 4 cột đầu). Chạy lệnh sau để tự động lấy 4 cột gốc từ `csv_templates` đè sang và dọn rác:
```bash
npm run clean
```
-> Kết quả sẽ được xuất ra thư mục `csv_cleaned/`.

### Bước 2: Tự động vá lỗi (Auto-Heal)
AI thường bị "ảo giác" (Ví dụ: điền cả cụm từ thay vì đáp án A, B, C; Hoặc lỡ chèn thêm dấu phẩy vào câu sắp xếp). Thay vì sửa tay, hãy chạy lệnh vá lỗi tự động:
```bash
npm run heal
```
-> Code sẽ tự phân tích và tự "chữa lành" những lỗi cơ bản trong các file ở `csv_cleaned/`. 

### Bước 3: Rà soát & Kiểm định (Validate / Review)
Sau khi Auto-Heal xong, vẫn sẽ có những lỗi nặng (Ví dụ: AI tự sáng tác tiếng Việt vào câu Nhật, hoặc AI đổi hẳn cấu trúc ngữ pháp). Chạy lệnh sau để quét toàn bộ:
```bash
npm run review
```
-> Script sẽ xuất ra file `review_report.txt` liệt kê chi tiết đích danh file nào, dòng nào bị lỗi. Bạn sẽ phải **SỬA THỦ CÔNG** (bằng Excel) những dòng còn sót lại này dựa trên báo cáo.

---
*Lưu ý: Chỉ khi nào `npm run review` thông báo **Phát hiện 0 lỗi**, dữ liệu lúc đó mới đạt chuẩn 100% để bộ phận Backend nạp vào Database chính!*
