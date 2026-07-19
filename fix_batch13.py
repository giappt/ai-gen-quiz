import csv
import re
import os

base_dir = '/home/kakashi/sources/pj/ai-gen-quiz/mondai2_ordering/csv_filled/set_2_business/'

def fix_quotes(text):
    # Replace matched pairs of single or double quotes with Japanese brackets
    text = re.sub(r"(['\"])(.*?)\1", r"「\2」", text)
    # If there are still remaining single or double quotes, replace them alternately
    for q in ["'", '"']:
        while q in text:
            text = text.replace(q, "「", 1)
            if q in text:
                text = text.replace(q, "」", 1)
            else:
                # Odd number of quotes, close it at the end of the string
                text += "」"
    
    # Fix missing opening quotes at the beginning like `先ほど」`
    text = re.sub(r'^([^「]+)」', r'「\1」', text)
    return text

def process_file(file_name):
    file_path = os.path.join(base_dir, file_name)
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        rows = list(reader)
    
    for i in range(1, len(rows)):
        row = rows[i]
        if len(row) < 12:
            continue
        
        # Specific language leaks
        if file_name == 'part_65.csv':
            if "最新 of モデル" in row[4]:
                row[4] = row[4].replace("最新 of モデル", "最新のモデル")
                row[5] = row[5].replace("最新 of モデル", "最新のモデル")
                row[10] = row[10].replace("最新 of モデル", "最新のモデル")
        
        row[11] = fix_quotes(row[11])

    with open(file_path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(rows)
    print(f"Fixed {file_name}")

for i in range(61, 66):
    process_file(f'part_{i}.csv')
