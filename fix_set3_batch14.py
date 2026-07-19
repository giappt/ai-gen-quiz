import csv
import re

def fix():
    # part_66.csv
    file_path = 'mondai2_ordering/csv_filled/set_3_academic/part_66.csv'
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        rows = list(reader)
    for row in rows:
        if len(row) > 11:
            row[11] = row[11].replace("(được tách và .", "(được tách thành 「提案して」 và 「みる」).")
            row[11] = row[11].replace("(tách và để tạo thành", "(được tách ra để tạo thành")
            row[11] = row[11].replace("(nếu thành công, tách và dẫn tới", "(nếu thành công) dẫn tới")
    with open(file_path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(rows)

    # part_67.csv
    file_path = 'mondai2_ordering/csv_filled/set_3_academic/part_67.csv'
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        rows = list(reader)
    for row in rows:
        if len(row) > 11:
            if 'オフィスは」' in row[11] and '「オフィスは」' not in row[11]:
                row[11] = row[11].replace('オフィスは」', '「オフィスは」')
            if 'ビジネスの」' in row[11] and '「ビジネスの」' not in row[11]:
                row[11] = row[11].replace('ビジネスの」', '「ビジネスの」')
            
            # Row 16 fix translation leak
            if 'AI của' in row[7]:
                row[7] = 'AIの'
                row[4] = row[5] + row[6] + row[7] + row[8] + row[9] + row[10]
                row[11] = row[11].replace('AI của ', 'AIの').replace('AI của', 'AIの')
    with open(file_path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(rows)

    # part_68.csv
    file_path = 'mondai2_ordering/csv_filled/set_3_academic/part_68.csv'
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        rows = list(reader)
    for row in rows:
        if len(row) > 11:
            # Row 3
            if 'して、本当に' in row[9]:
                row[9] = 'して、'
                row[10] = '本当に申し訳ございませんでした。'
            # Row 9
            if "'na-nda'" in row[11]:
                row[11] = row[11].replace("'na-nda'", "「なんだ」")
    with open(file_path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(rows)

    # part_69.csv
    file_path = 'mondai2_ordering/csv_filled/set_3_academic/part_69.csv'
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        rows = list(reader)
    for row in rows:
        if len(row) > 11:
            # Row 7
            if 'かなる' in row[7] and 'なんと' in row[6]:
                row[6] = 'なんとか'
                row[7] = 'なる'
                row[8] = 'と'
                row[9] = '思っております'
            # Row 10
            if 'クラウド」とか' in row[6]:
                row[4] = row[4].replace('クラウド」とか', 'クラウドとか')
                row[6] = 'クラウドとか'
                row[11] = row[11].replace('クラウド」とか', 'クラウドとか')
    with open(file_path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(rows)

if __name__ == "__main__":
    fix()
    print("Fixed batch 14 manually")
