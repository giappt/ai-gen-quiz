import csv
import re

def fix():
    # part_91.csv
    file_path = 'mondai2_ordering/csv_filled/set_3_academic/part_91.csv'
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        rows = list(reader)
    for row in rows:
        if len(row) > 11:
            row[11] = row[11].replace('A của みならずBも/Bまで', 'AのみならずBも/Bまで')
            # Replace single quotes
            row[11] = re.sub(r"'([^']+)'", r'「\1」', row[11])
    with open(file_path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(rows)

    # part_92.csv
    file_path = 'mondai2_ordering/csv_filled/set_3_academic/part_92.csv'
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        rows = list(reader)
    for row in rows:
        if len(row) > 11:
            row[11] = re.sub(r"'([^']+)'", r'「\1」', row[11])
            row[11] = row[11].replace('""không hề ghét/khá hài lòng/hớn hở ra mặt""', '「không hề ghét/khá hài lòng/hớn hở ra mặt」')
            row[11] = row[11].replace('""bộc lộ ra, thể hiện rõ""', '「bộc lộ ra, thể hiện rõ」')
    with open(file_path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(rows)

    # part_93.csv
    file_path = 'mondai2_ordering/csv_filled/set_3_academic/part_93.csv'
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        rows = list(reader)
    for row in rows:
        for i in range(len(row)):
            row[i] = row[i].replace('IT của 知識', 'ITの知識')
        if len(row) > 11:
            if row[4] == '':
                row[4] = "".join(row[5:11])
    with open(file_path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(rows)

    # part_94.csv
    file_path = 'mondai2_ordering/csv_filled/set_3_academic/part_94.csv'
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        rows = list(reader)
    for row in rows:
        if len(row) > 11:
            row[11] = row[11].replace('B của 方', 'Bの方')
    with open(file_path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(rows)

if __name__ == "__main__":
    fix()
    print("Fixed batch 19 manually")
