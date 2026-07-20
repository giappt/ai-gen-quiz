import csv, os

dir_path = r'd:\pj\xx\ai-gen-quiz\mondai2_ordering\csv_filled\set_3_academic'
leakage_str = "Câu được chia thành các phần tương ứng để kiểm tra khả năng sắp xếp trật tự từ ngữ pháp trong tiếng Nhật một cách chính xác nhất"

out = []
for i in range(36, 41):
    file = f'part_{i}.csv'
    path = os.path.join(dir_path, file)
    if not os.path.exists(path): continue
    
    with open(path, encoding='utf-8-sig') as f:
        r = list(csv.reader(f))
        
    headers = r[0]
    exp_idx = headers.index('Explanation') if 'Explanation' in headers else len(headers)-1
    
    for idx, row in enumerate(r):
        if idx == 0 or len(row) <= exp_idx: continue
        exp = row[exp_idx]
        
        if 'thứ tự' in exp.lower() or 'cú pháp' in exp.lower() or 'logic' in exp.lower() or 'trình tự' in exp.lower() or leakage_str.lower() in exp.lower():
            out.append(f'{file}:{idx}\nORIG: {exp}\n')

with open(r'd:\pj\xx\ai-gen-quiz\scratch\batch8_manual_review.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(out))
