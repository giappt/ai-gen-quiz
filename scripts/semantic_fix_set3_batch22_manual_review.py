import csv, os

dir_path = r'd:\pj\xx\ai-gen-quiz\mondai2_ordering\csv_filled\set_3_academic'

rewrites = {
    # part_108.csv
    "Câu này diễn tả điều kiện giả định rút ra từ lời nói của khách hàng. 「そう言う」 (nói như vậy) đi liền với 「んじゃ」 (nếu là.../thế thì...) để tạo thành vế điều kiện 「Nếu khách hàng nói như thế...」. Tiếp theo; 「スケジュールを」 (lịch trình) là tân ngữ của động từ 「変更する」 (thay đổi). Cấu trúc 「V-るしかない」 (chỉ còn cách...) kết hợp với 「変更する」 thành 「変更するしかありません」 (không còn cách nào khác ngoài thay đổi). Thứ tự kết hợp tự nhiên là: [Chủ ngữ hoặc Đối tượng] + [Vế điều kiện giả định んじゃ] + [Tân ngữ] + [Hành động bắt buộc (しかない)].":
    "Câu này diễn tả điều kiện giả định dựa trên lời khách hàng. Khởi đầu với 「そう言うんじゃ」 (nếu khách hàng đã nói vậy thì...). Tân ngữ 「スケジュールを」 (lịch trình) đi liền với động từ 「変更する」 (thay đổi). Vế cuối sử dụng cấu trúc 「V-るしかない」 tạo thành 「変更するしかありません」 (chỉ còn cách phải thay đổi thôi).",
    
    "Câu thể hiện ý kiến mang tính phỏng đoán; nhận xét nhẹ nhàng trong cuộc họp. 「提案は」 (đề xuất thì...) là chủ đề của câu. Trạng từ 「少し」 (một chút) bổ nghĩa cho tính từ 「高すぎる」 (quá cao); bổ nghĩa cho danh từ 「リスク」 (rủi ro) qua trợ từ 「が」 (risk cao). Cấu trúc biểu thị phỏng đoán 「んじゃない」 đi sau thể thông thường của tính từ 「高すぎる」. Kết thúc bằng đuôi lịch sự 「ですか」 tạo thành câu hỏi 「Chẳng phải là... hay sao?」. Thứ tự đúng: [Chủ đề] + [Trạng từ] + [Chủ ngữ phụ và Tính từ] + [Phỏng đoán んじゃない] + [Đuôi lịch sự ですか].":
    "Câu nêu nhận xét nhẹ nhàng qua hình thức phỏng đoán. Bắt đầu bằng chủ đề 「提案は」 (đề xuất thì...). Cụm tính từ 「少し高すぎる」 (hơi cao quá) bổ nghĩa cho 「リスクが」 (rủi ro). Cuối cùng, cấu trúc phỏng đoán 「んじゃない」 gắn với đuôi lịch sự 「ですか」 tạo thành nghi vấn mềm mỏng (chẳng phải là rủi ro hơi cao sao?)."
}

for i in range(106, 109):
    file = f'part_{i}.csv'
    path = os.path.join(dir_path, file)
    if not os.path.exists(path): continue
    
    with open(path, encoding='utf-8-sig') as f:
        r = list(csv.reader(f))
    
    headers = r[0]
    exp_idx = headers.index('Explanation') if 'Explanation' in headers else len(headers)-1
    
    changed = False
    for idx, row in enumerate(r):
        if idx == 0 or len(row) <= exp_idx: continue
        exp = row[exp_idx]
        
        for orig, new_val in rewrites.items():
            if orig in exp:
                exp = exp.replace(orig, new_val)
                row[exp_idx] = exp
                changed = True
                
    if changed:
        with open(path, 'w', encoding='utf-8-sig', newline='') as f:
            csv.writer(f).writerows(r)

print("Batch 22 manually reviewed and rewritten successfully!")
