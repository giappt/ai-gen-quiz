import csv, os

dir_path = r'd:\pj\xx\ai-gen-quiz\mondai2_ordering\csv_filled\set_3_academic'

fixes = {
    "thể hiện quyết tâm hoặc nghĩa vụ mang tính logic.": "thể hiện quyết tâm hoặc nghĩa vụ tất yếu.",
    "Thứ tự đúng tạo thành câu tôn kính hoàn chỉnh.": "Mạch câu tạo thành câu tôn kính hoàn chỉnh.",
    
    "Thứ tự tự nhiên:": "Mạch câu diễn tiến tự nhiên:",
    "Thứ tự câu:": "Mạch câu:",
    "Thứ tự kết hợp:": "Mạch câu liên kết:",
    "Thứ tự từ trái sang phải phản ánh trình tự tư duy logic tự nhiên:": "Mạch câu diễn tiến theo trình tự tự nhiên:",
    "Thứ tự phân tách từ trái sang phải diễn tiến theo đúng cú pháp tiếng Nhật:": "Mạch câu diễn tiến theo cấu trúc tiếng Nhật:",
    "Mạch câu tiếp diễn theo thứ tự:": "Mạch câu tiếp diễn:",
    "Câu tuân theo cấu trúc cú pháp chuẩn mực:": "Cấu trúc câu:",
    "Thứ tự băm câu đi từ": "Mạch câu đi từ",
    "Thứ tự logic câu:": "Mạch câu diễn tiến:",
    "Thứ tự kết hợp câu:": "Sự kết hợp các phần:",
    "Mạch cú pháp câu phát triển tuyến tính:": "Mạch câu diễn tiến:",
    "xếp theo thứ tự từ": "bắt đầu từ",
    "được sắp xếp trước động từ theo đúng cú pháp tự nhiên.": "được liên kết trước động từ một cách tự nhiên.",
    "Thứ tự:": "Mạch câu:"
}

leakage_str1 = " Cấu trúc ngữ pháp cơ bản. Câu được chia thành các phần tương ứng để kiểm tra khả năng sắp xếp trật tự từ ngữ pháp trong tiếng Nhật một cách chính xác nhất."
leakage_str2 = "Câu được chia thành các phần tương ứng để kiểm tra khả năng sắp xếp trật tự từ ngữ pháp trong tiếng Nhật một cách chính xác nhất."

for i in range(6, 21):
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
        
        new_exp = exp.replace(leakage_str1, "").replace(leakage_str2, "")
        
        sorted_keys = sorted(fixes.keys(), key=len, reverse=True)
        for old in sorted_keys:
            if old in new_exp:
                new_exp = new_exp.replace(old, fixes[old])
                
        if exp != new_exp:
            row[exp_idx] = new_exp
            changed = True
            
    if changed:
        with open(path, 'w', encoding='utf-8-sig', newline='') as f:
            csv.writer(f).writerows(r)

print("Batches 2, 3, 4 (Set 3) fixed successfully!")
