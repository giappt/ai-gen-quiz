import csv
import re
import os
import sys

base_dir = '/home/kakashi/sources/pj/ai-gen-quiz/mondai2_ordering/csv_filled/set_3_academic/'

def fix_quotes(text):
    text = re.sub(r"(['\"])(.*?)\1", r"「\2」", text)
    for q in ["'", '"']:
        while q in text:
            text = text.replace(q, "「", 1)
            if q in text:
                text = text.replace(q, "」", 1)
            else:
                text += "」"
    
    text = re.sub(r'^([^「]+)」', r'「\1」', text)
    return text

def process_file(file_name):
    file_path = os.path.join(base_dir, file_name)
    if not os.path.exists(file_path):
        return
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        rows = list(reader)
    
    for i in range(1, len(rows)):
        row = rows[i]
        if len(row) < 12:
            continue
        row[11] = fix_quotes(row[11])

    with open(file_path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(rows)
    print(f"Fixed {file_name}")

if __name__ == "__main__":
    start = int(sys.argv[1])
    end = int(sys.argv[2])
    for i in range(start, end + 1):
        process_file(f'part_{i}.csv')
