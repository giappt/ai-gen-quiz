import csv
import re

file_path = 'mondai2_ordering/csv_filled/set_1_daily/part_8.csv'
lines = []
with open(file_path, 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        if len(row) > 11:
            exp = row[11]
            if exp.count('「') != exp.count('」'):
                exp = re.sub(r'^([^「]+)」', r'「\1」', exp)
                
                # For row 20 which might have "N của 上では」"
                if "N của 上では」" in exp:
                    exp = exp.replace("N của 上では」", "「Nの上では」")
                elif "N của 上では" in exp:
                     exp = exp.replace("N của 上では", "「Nの上では」")
                
                row[11] = exp
        lines.append(row)

with open(file_path, 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(lines)
print("Fixed part_8.csv quotes")
