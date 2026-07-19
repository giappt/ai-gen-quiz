import csv
import re

# Fix part_69 and part_72 quotes
for f_name in ['part_69.csv', 'part_72.csv']:
    file_path = f'mondai2_ordering/csv_filled/set_1_daily/{f_name}'
    lines = []
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) > 11:
                exp = row[11]
                if exp.count('「') != exp.count('」'):
                    exp = re.sub(r'^([^「]+)」', r'「\1」', exp)
                    row[11] = exp
            lines.append(row)
    with open(file_path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(lines)

# Fix part_70
file_path = 'mondai2_ordering/csv_filled/set_1_daily/part_70.csv'
lines = []
with open(file_path, 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row_idx, row in enumerate(reader):
        if row_idx == 2:
            row[4] = "この壊れた商品について、店側の対応にはなんらの誠意も感じられなかった。"
            row[5] = "この壊れた商品について、"
            row[6] = "店側の"
            row[7] = "対応には"
            row[8] = "なんらの誠意も"
            row[9] = "感じられ"
            row[10] = "なかった。"
            # row[11] is fine
        lines.append(row)
with open(file_path, 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(lines)

print("Fixed Batch 4 issues")
