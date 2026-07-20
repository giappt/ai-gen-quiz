import csv, os

dir_path = r'd:\pj\xx\ai-gen-quiz\mondai2_ordering\csv_filled\set_2_business'

fixes = {
    "Thứ tự kết hợp: (1)": "Mạch câu bắt đầu với (1)",
    "Thứ tự câu: (1)": "Mạch câu bắt đầu với (1)",
    "Thứ tự: (1)": "Mạch câu bắt đầu với (1)",
    
    "Trình tự tự nhiên:": "Mạch câu diễn tiến tự nhiên:",
    "Thứ tự bổ nghĩa:": "Sự bổ nghĩa diễn tiến:",
    "Thứ tự từ sau cụm điều kiện phản đề:": "Các thành phần liên kết sau cụm điều kiện phản đề:",
    "Thứ tự từ:": "Mạch câu kết nối:",
    "Thứ tự cú pháp tự nhiên:": "Cấu trúc câu diễn tiến tự nhiên:",
    "Thứ tự cú pháp gồm:": "Cấu trúc câu gồm:",
    "Thứ tự cú pháp:": "Cấu trúc câu:",
    "Thứ tự cấu trúc:": "Cấu trúc câu:",
    "Thứ tự câu:": "Mạch câu:",
    "Thứ tự:": "Mạch câu kết nối:"
}

leakage_str1 = " Cấu trúc ngữ pháp cơ bản. Câu được chia thành các phần tương ứng để kiểm tra khả năng sắp xếp trật tự từ ngữ pháp trong tiếng Nhật một cách chính xác nhất."
leakage_str2 = "Câu được chia thành các phần tương ứng để kiểm tra khả năng sắp xếp trật tự từ ngữ pháp trong tiếng Nhật một cách chính xác nhất."

for i in range(96, 109):
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
        
        # Sort keys by length descending to ensure longer matches are replaced first
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

print("Batches 20, 21, 22 fixed successfully!")
