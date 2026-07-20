import csv, os

dir_path = r'd:\pj\xx\ai-gen-quiz\mondai2_ordering\csv_filled\set_3_academic'

rewrites = {
    # part_57.csv
    "Cấu trúc 「Nとともに」 (cùng với N). 「取引先の」 bổ nghĩa cho danh từ 「皆様」. 「と」 và 「ともに」 tách ra theo thứ tự cú pháp tự nhiên để tạo thành cụm trạng ngữ chỉ sự đồng hành. Vế sau là động từ nguyện vọng kính ngữ 「発展してまいりたいと存じます」.":
    "Cấu trúc 「Nとともに」 mang nghĩa \"cùng với N\". Trong câu này, định ngữ 「取引先の」 bổ nghĩa cho danh từ 「皆様」. Các thành phần 「と」 và 「ともに」 kết hợp nhịp nhàng với nhau để tạo thành cụm trạng ngữ chỉ sự đồng hành. Vế sau là động từ nguyện vọng kính ngữ 「発展してまいりたいと存じます」."
}

for i in range(56, 61):
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

print("Batch 12 manually reviewed and rewritten successfully!")
