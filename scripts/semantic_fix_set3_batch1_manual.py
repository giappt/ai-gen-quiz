import csv, os

dir_path = r'd:\pj\xx\ai-gen-quiz\mondai2_ordering\csv_filled\set_3_academic'

fixes = {
    "Thứ tự cú pháp tự nhiên là": "Mạch câu diễn tiến tự nhiên từ",
    "Thứ tự cú pháp tự nhiên:": "Mạch câu diễn tiến tự nhiên:",
    "Theo thứ tự cú pháp:": "Theo mạch câu:",
    "Thứ tự tiếp nối là": "Các phần liên kết là",
    "Cú pháp bắt đầu từ": "Mạch câu bắt đầu từ",
    "Thứ tự logic:": "Mạch câu diễn tiến:",
    "Thứ tự phân cấp tự nhiên:": "Sự liên kết tự nhiên:",
    "Cú pháp phân chia tuần tự:": "Mạch câu diễn tiến:",
    "Thứ tự logic sắp đặt:": "Mạch câu diễn tiến logic:"
}

leakage_str1 = " Cấu trúc ngữ pháp cơ bản. Câu được chia thành các phần tương ứng để kiểm tra khả năng sắp xếp trật tự từ ngữ pháp trong tiếng Nhật một cách chính xác nhất."
leakage_str2 = "Câu được chia thành các phần tương ứng để kiểm tra khả năng sắp xếp trật tự từ ngữ pháp trong tiếng Nhật một cách chính xác nhất."

for i in range(1, 6):
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

print("Batch 1 (Set 3) fixed successfully!")
