import csv, os

dir_path = r'd:\pj\xx\ai-gen-quiz\mondai2_ordering\csv_filled\set_2_business'

fixes = {
    "part_67.csv-1": {
        "Do đó thứ tự hợp lý là 1-2-3-4.": "Mạch câu vì thế được liên kết liền mạch."
    },
    "part_69.csv-14": {
        "Về mặt cú pháp,": "Xét về cấu trúc,"
    },
    "part_69.csv-17": {
        "Các thành phần được sắp xếp theo thứ tự tự nhiên:": "Các thành phần liên kết tự nhiên:"
    },
    "part_71.csv-1": {
        "Thứ tự bổ nghĩa tự nhiên chạy từ bối cảnh đến chủ ngữ và bổ ngữ của vị ngữ.": "Sự bổ nghĩa diễn tiến tự nhiên từ bối cảnh đến chủ ngữ và bổ ngữ của vị ngữ."
    },
    "part_72.csv-1": {
        "Thứ tự cú pháp tự nhiên:": "Mạch câu diễn tiến tự nhiên:"
    },
    "part_80.csv-16": {
        "1. Định ngữ": "Bắt đầu với định ngữ",
        "2. Động từ": "Tiếp nối là động từ",
        "3. Trạng từ": "Sau đó là trạng từ",
        "4. Tân ngữ": "Cuối cùng, tân ngữ"
    },
    "part_80.csv-20": {
        "1. Trạng ngữ": "Đầu tiên là trạng ngữ",
        "2. Cụm danh từ": "Kế tiếp là cụm danh từ",
        "3. Cụm định lượng": "Sau đó là cụm định lượng",
        "4. Trạng thái": "Cuối cùng là trạng thái"
    }
}

leakage_str1 = " Cấu trúc ngữ pháp cơ bản. Câu được chia thành các phần tương ứng để kiểm tra khả năng sắp xếp trật tự từ ngữ pháp trong tiếng Nhật một cách chính xác nhất."
leakage_str2 = "Câu được chia thành các phần tương ứng để kiểm tra khả năng sắp xếp trật tự từ ngữ pháp trong tiếng Nhật một cách chính xác nhất."

for i in range(66, 81):
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
        
        # Remove leakages globally
        new_exp = exp.replace(leakage_str1, "").replace(leakage_str2, "")
        
        # Specific fixes
        key = f"{file}-{idx}"
        if key in fixes:
            for old, new in fixes[key].items():
                if old in new_exp:
                    new_exp = new_exp.replace(old, new)
                    
        if exp != new_exp:
            row[exp_idx] = new_exp
            changed = True
            
    if changed:
        with open(path, 'w', encoding='utf-8-sig', newline='') as f:
            csv.writer(f).writerows(r)

print("Batches 14, 15, 16 fixed successfully!")
