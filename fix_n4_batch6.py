import csv

file_path = 'mondai2_ordering/csv_filled/set_1_daily/part_46.csv'
lines = []
with open(file_path, 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        if len(row) > 11:
            if "でもって" in row[0] and "crumbs" in row[11]:
                row[11] = row[11].replace("crumbs", "でもって")
            if "でもない" in row[0] and "crumbs" in row[11]:
                row[11] = row[11].replace("crumbs", "でもなく")
        lines.append(row)

with open(file_path, 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(lines)
print("Fixed part_46.csv")
