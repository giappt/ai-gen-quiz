import csv
import re

file_path = '/home/kakashi/sources/pj/ai-gen-quiz/mondai2_ordering/csv_filled/set_2_business/part_52.csv'

with open(file_path, 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    rows = list(reader)

for i in range(1, len(rows)):
    row = rows[i]
    if len(row) < 12:
        continue
    exp = row[11]
    # Replace '' with 「 and 」 alternately
    while "''" in exp:
        # replace the first '' with 「
        exp = exp.replace("''", "「", 1)
        # replace the next '' with 」
        exp = exp.replace("''", "」", 1)
    
    row[11] = exp

with open(file_path, 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(rows)

print("Fixed part_52.csv")
