import csv
import os
import re
import json

dir_path = r'd:\pj\xx\ai-gen-quiz\mondai2_ordering\csv_filled\set_1_daily'

robotic_pattern = re.compile(r'(Thứ tự|Cú pháp chia tách|Câu cấu trúc theo|Thứ tự logic|Thứ tự cấu trúc|Thứ tự kết hợp tự nhiên|Thứ tự bổ nghĩa bắt buộc|Thứ tự tự nhiên).*?[:+->]', re.IGNORECASE)

missing_items = []
modifications = []

def clean_explanation(text):
    original_text = text
    patterns = [
        r"(?:Thứ tự|Cú pháp chia tách|Câu cấu trúc theo).*?(?:[:+->]).*$",
        r"Thứ tự logic:.*$",
        r"Thứ tự cấu trúc:.*$",
        r"Thứ tự kết hợp tự nhiên:.*$",
        r"Thứ tự bổ nghĩa bắt buộc:.*$",
        r"Thứ tự tự nhiên:.*$",
        r"Thứ tự:.*$",
    ]
    for p in patterns:
        text = re.sub(p, "", text, flags=re.IGNORECASE).strip()
    text = re.sub(r'\s+([A-Z][a-z]+.*?\.)\s*$', r' \1', text).strip()
    return text

for i in range(1, 109):
    file_name = f'part_{i}.csv'
    full_path = os.path.join(dir_path, file_name)
    
    if not os.path.exists(full_path):
        continue
        
    with open(full_path, 'r', encoding='utf-8-sig') as f:
        reader = list(csv.DictReader(f))
        fieldnames = reader[0].keys() if len(reader) > 0 else []
        
    file_modified = False
        
    for index, row in enumerate(reader):
        file_id = f"{file_name}-{index + 1}"
        orig_example = str(row.get("Original Example") or "").strip()
        exp = str(row.get("Explanation") or "")
        
        # 1. Collect missing
        if not orig_example:
            missing_items.append({
                "id": file_id,
                "Grammar": str(row.get("Grammar") or ""),
                "JLPT Level": str(row.get("JLPT Level") or ""),
                "Reference Example": str(row.get("Reference Example") or "")
            })
            
        # 2. Clean robotic phrasing
        if robotic_pattern.search(exp) and "nhấn mạnh sự đối lập với quá khứ" not in exp: # exclude known false positive part_8-12
            new_exp = clean_explanation(exp)
            if old_exp := exp != new_exp:
                row["Explanation"] = new_exp
                modifications.append({
                    "id": file_id,
                    "old": exp,
                    "new": new_exp
                })
                file_modified = True
                
    if file_modified:
        with open(full_path, 'w', encoding='utf-8-sig', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(reader)

with open(r'd:\pj\xx\ai-gen-quiz\scratch\missing_items.json', 'w', encoding='utf-8') as f:
    json.dump(missing_items, f, ensure_ascii=False, indent=4)

print(f"Cleaned {len(modifications)} robotic phrasings.")
print(f"Dumped {len(missing_items)} missing items to scratch/missing_items.json.")
