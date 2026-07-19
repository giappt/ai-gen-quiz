import csv
import re
import os

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

def process_file(file_path):
    if not os.path.exists(file_path):
        return
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        rows = list(reader)
    
    for i in range(1, len(rows)):
        row = rows[i]
        
        # fix leaks
        for j in range(len(row)):
            row[j] = row[j].replace(' của ', 'の')
            
        if len(row) > 11:
            # fix empty original example
            if row[4] == '':
                row[4] = "".join(row[5:11])
            
            # fix quotes
            row[11] = fix_quotes(row[11])

    with open(file_path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(rows)
    print(f"Fixed {file_path}")

def fix():
    base_dir = '/home/kakashi/sources/pj/ai-gen-quiz/mondai2_ordering/csv_filled/set_4_literature/'
    for i in range(1, 51):
        process_file(os.path.join(base_dir, f'part_{i}.csv'))

if __name__ == "__main__":
    fix()
    print("Fixed Set 4 Batches 1-10")
