import csv, os

dir_path = r'd:\pj\xx\ai-gen-quiz\mondai2_ordering\csv_filled\set_3_academic'
leakage_str = "Câu được chia thành các phần tương ứng để kiểm tra khả năng sắp xếp trật tự từ ngữ pháp trong tiếng Nhật một cách chính xác nhất"
robotic_patterns = [
    "thứ tự kết hợp", "thứ tự câu", "thứ tự cú pháp", "trình tự cú pháp",
    "thứ tự tự nhiên", "trình tự logic", "thứ tự phân cấp", "thứ tự cấu trúc",
    "thứ tự đúng", "cú pháp tự nhiên", "cú pháp bắt đầu", "thứ tự logic",
    "cú pháp phân chia", "cú pháp đi từ", "thứ tự sắp xếp", "thứ tự chuỗi",
    "thứ tự bổ ngữ", "thứ tự xuất hiện"
]

out = []
for i in range(51, 109):
    file = f'part_{i}.csv'
    path = os.path.join(dir_path, file)
    if not os.path.exists(path): continue
    
    with open(path, encoding='utf-8-sig') as f:
        r = list(csv.reader(f))
        
    headers = r[0]
    exp_idx = headers.index('Explanation') if 'Explanation' in headers else len(headers)-1
    
    for idx, row in enumerate(r):
        if idx == 0 or len(row) <= exp_idx: continue
        exp = row[exp_idx].lower()
        
        has_issue = False
        if leakage_str.lower() in exp:
            has_issue = True
        else:
            for p in robotic_patterns:
                if p in exp:
                    has_issue = True
                    break
        
        if has_issue:
            out.append(f'{file}:{idx}\nORIG: {row[exp_idx]}\n')

with open(r'd:\pj\xx\ai-gen-quiz\scratch\rest_set3_manual_review.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(out))
