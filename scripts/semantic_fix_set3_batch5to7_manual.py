import csv, os

dir_path = r'd:\pj\xx\ai-gen-quiz\mondai2_ordering\csv_filled\set_3_academic'

fixes = {
    "Trình tự câu:": "Mạch câu:",
    "Thứ tự tự nhiên là": "Mạch câu diễn tiến tự nhiên:",
    "Thứ tự hợp lý là": "Mạch câu liên kết hợp lý:",
    "Thứ tự đúng là": "Mạch câu liên kết đúng là:",
    "Thứ tự bắt buộc là": "Mạch câu bắt buộc đi từ",
    "Thứ tự logic là": "Mạch câu liên kết logic:",
    "Thứ tự tự nhiên:": "Mạch câu diễn tiến tự nhiên:",
    "Về mặt cú pháp,": "Xét về cấu trúc,",
    "Thứ tự đúng:": "Mạch câu:",
    "Thứ tự câu:": "Mạch câu:",
    "Thứ tự đi từ": "Mạch câu đi từ",
    "Thứ tự tự nhiên của câu:": "Mạch câu diễn tiến tự nhiên:",
    "Thứ tự chuỗi cụm danh từ đồng dạng bổ nghĩa từ phạm vi rộng đến hẹp:": "Mạch câu bổ nghĩa từ phạm vi rộng đến hẹp:",
    "Thứ tự bổ ngữ tự nhiên ở N5:": "Sự bổ nghĩa tự nhiên diễn tiến:",
    "Thứ tự xuất hiện tự nhiên là": "Mạch câu xuất hiện tự nhiên là",
    "Thứ tự cấu trúc tự nhiên:": "Mạch câu diễn tiến tự nhiên:",
    "Thứ tự sắp xếp:": "Mạch câu diễn tiến:",
    "Thứ tự câu tự nhiên:": "Mạch câu diễn tiến tự nhiên:",
    "trình tự cú pháp:": "trình tự cấu trúc:",
    "Thứ tự câu logic:": "Mạch câu liên kết logic:",
    "Thứ tự sắp xếp tự nhiên trong tiếng Nhật:": "Mạch câu diễn tiến tự nhiên:",
    "Trình tự:": "Mạch câu diễn tiến:",
    "Thứ tự logic:": "Mạch câu liên kết logic:",
    "Thứ tự bắt đầu bằng": "Mạch câu bắt đầu bằng",
    "Cú pháp tự nhiên bắt đầu từ": "Mạch câu bắt đầu từ",
    "Thứ tự logic trong bối cảnh công sở:": "Mạch câu logic trong bối cảnh công sở:",
    "Cú pháp đi từ": "Mạch câu đi từ",
    "Theo thứ tự:": "Theo mạch câu:",
    "Thứ tự:": "Mạch câu:"
}

leakage_str1 = " Cấu trúc ngữ pháp cơ bản. Câu được chia thành các phần tương ứng để kiểm tra khả năng sắp xếp trật tự từ ngữ pháp trong tiếng Nhật một cách chính xác nhất."
leakage_str2 = "Câu được chia thành các phần tương ứng để kiểm tra khả năng sắp xếp trật tự từ ngữ pháp trong tiếng Nhật một cách chính xác nhất."

for i in range(21, 36):
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
        
        # Sort keys by length descending
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

print("Batches 5, 6, 7 (Set 3) fixed successfully!")
