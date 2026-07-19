import csv
import re
import os

files_to_process = [f'part_{i}.csv' for i in range(1, 51)]
base_dir = 'mondai2_ordering/csv_filled/set_2_business/'

log = []

for f_name in files_to_process:
    file_path = os.path.join(base_dir, f_name)
    if not os.path.exists(file_path):
        continue
        
    lines = []
    modified = False
    
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        header = next(reader)
        lines.append(header)
        for row_idx, row in enumerate(reader, start=2):
            if len(row) > 11:
                exp = row[11]
                
                # Fix quotes
                if exp.count('「') != exp.count('」'):
                    exp = re.sub(r'^([^「]+)」', r'「\1」', exp)
                    row[11] = exp
                    modified = True
                    log.append(f"{f_name} Row {row_idx}: Fixed mismatched quotes.")
                
            lines.append(row)
            
    if modified:
        with open(file_path, 'w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(lines)

with open('set2_batch1_10_fix_log.txt', 'w', encoding='utf-8') as f:
    if log:
        f.write('\n'.join(log))
    else:
        f.write("No errors found in the first 50 files.")
print("Fix completed.")
