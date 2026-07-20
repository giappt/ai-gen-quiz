import csv
import os
import re

dir_path = r'd:\pj\xx\ai-gen-quiz\mondai2_ordering\csv_filled\set_1_daily'

robotic_pattern = re.compile(r'(Thứ tự|Cú pháp chia tách|Câu cấu trúc theo|Thứ tự logic|Thứ tự cấu trúc|Thứ tự kết hợp tự nhiên|Thứ tự bổ nghĩa bắt buộc|Thứ tự tự nhiên).*?[:+->]', re.IGNORECASE)
n_cua_pattern = re.compile(r'N của (あいだ|後で|こと)')

issues = {
    'empty_original': [],
    'robotic_phrasing': [],
    'n_cua': []
}

for i in range(1, 109):
    file_name = f'part_{i}.csv'
    full_path = os.path.join(dir_path, file_name)
    
    if not os.path.exists(full_path):
        continue
        
    with open(full_path, 'r', encoding='utf-8-sig') as f:
        reader = list(csv.DictReader(f))
        
    for index, row in enumerate(reader):
        file_id = f"{file_name}-{index + 1}"
        orig_example = str(row.get("Original Example") or "").strip()
        exp = str(row.get("Explanation") or "")
        
        if not orig_example:
            issues['empty_original'].append(file_id)
            
        if robotic_pattern.search(exp):
            issues['robotic_phrasing'].append(file_id)
            
        if n_cua_pattern.search(exp):
            issues['n_cua'].append(file_id)

print(f"Empty Original Example: {len(issues['empty_original'])}")
if issues['empty_original']:
    print(issues['empty_original'][:10])
    
print(f"Robotic Phrasing: {len(issues['robotic_phrasing'])}")
if issues['robotic_phrasing']:
    print(issues['robotic_phrasing'][:10])

print(f"N của...: {len(issues['n_cua'])}")
if issues['n_cua']:
    print(issues['n_cua'][:10])
