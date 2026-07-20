import csv, os

dir_path = r'd:\pj\xx\ai-gen-quiz\mondai2_ordering\csv_filled\set_2_business'

fixes_part64 = {
    "Thứ tự tự nhiên theo cú pháp tiếng Nhật:": "Các thành phần kết nối tự nhiên:",
    "Thứ tự sắp xếp câu tuân theo logic từ chỉ vị trí không gian": "Mạch câu đi từ chỉ vị trí không gian",
    "Thứ tự sắp xếp câu:": "Mạch câu diễn tiến:",
    "Thứ tự cú pháp:": "Cấu trúc câu:",
    "Thứ tự tự nhiên:": "Sự liên kết tự nhiên:",
    "Thứ tự kết nối logic:": "Sự kết nối chặt chẽ:",
    "Thứ tự câu:": "Mạch câu:",
    "Thứ tự liên kết:": "Các thành phần nối tiếp:",
    "Thứ tự kết hợp câu:": "Các phần kết hợp:",
    "Thứ tự kết cấu logic câu:": "Mạch câu diễn tiến:",
    "Thứ tự từ tự nhiên:": "Các phần liên kết tự nhiên:",
    "Thứ tự logic:": "Các thành phần tiếp nối:",
    "Thứ tự cấu trúc câu:": "Cấu trúc câu:",
    "Thứ tự đúng:": "Mạch câu diễn tiến:"
}

leakage_str1 = " Cấu trúc ngữ pháp cơ bản. Câu được chia thành các phần tương ứng để kiểm tra khả năng sắp xếp trật tự từ ngữ pháp trong tiếng Nhật một cách chính xác nhất."
leakage_str2 = "Cấu trúc ngữ pháp cơ bản. Câu được chia thành các phần tương ứng để kiểm tra khả năng sắp xếp trật tự từ ngữ pháp trong tiếng Nhật một cách chính xác nhất."

# Fix part 64
file_64 = os.path.join(dir_path, 'part_64.csv')
if os.path.exists(file_64):
    with open(file_64, encoding='utf-8-sig') as f:
        r = list(csv.reader(f))
    headers = r[0]
    exp_idx = headers.index('Explanation') if 'Explanation' in headers else len(headers)-1
    changed = False
    for i, row in enumerate(r):
        if i == 0 or len(row) <= exp_idx: continue
        exp = row[exp_idx]
        
        new_exp = exp.replace(leakage_str1, "").replace(leakage_str2, "")
        
        for old, new in fixes_part64.items():
            if old in new_exp:
                new_exp = new_exp.replace(old, new)
                
        if exp != new_exp:
            row[exp_idx] = new_exp
            changed = True
            
    if changed:
        with open(file_64, 'w', encoding='utf-8-sig', newline='') as f:
            csv.writer(f).writerows(r)

# Fix part 65
file_65 = os.path.join(dir_path, 'part_65.csv')
if os.path.exists(file_65):
    with open(file_65, encoding='utf-8-sig') as f:
        r = list(csv.reader(f))
    headers = r[0]
    exp_idx = headers.index('Explanation') if 'Explanation' in headers else len(headers)-1
    changed = False
    for i, row in enumerate(r):
        if i == 0 or len(row) <= exp_idx: continue
        exp = row[exp_idx]
        if "dẫn cú pháp cho hành động" in exp:
            row[exp_idx] = exp.replace("dẫn cú pháp cho hành động", "dẫn dắt hành động")
            changed = True
    if changed:
        with open(file_65, 'w', encoding='utf-8-sig', newline='') as f:
            csv.writer(f).writerows(r)

print("Batch 13 fixes applied successfully!")
