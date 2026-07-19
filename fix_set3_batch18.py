import csv
import re

def fix():
    # part_86.csv
    file_path = 'mondai2_ordering/csv_filled/set_3_academic/part_86.csv'
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        rows = list(reader)
    for row in rows:
        if len(row) > 11:
            if '新規契約 of 交渉' in row[4]:
                row[4] = row[4].replace('新規契約 of 交渉', '新規契約の交渉')
            if '新規契約 of 交渉' in row[5]:
                row[5] = row[5].replace('新規契約 of 交渉', '新規契約の交渉')
            row[11] = row[11].replace("'ので'", "「ので」")
            row[11] = row[11].replace("'が'", "「が」")
            row[11] = row[11].replace("'は'", "「は」")
    with open(file_path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(rows)

    # part_87.csv
    file_path = 'mondai2_ordering/csv_filled/set_3_academic/part_87.csv'
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        rows = list(reader)
    for row in rows:
        if len(row) > 11:
            # Replace [ ] with 「 」
            row[11] = row[11].replace('[', '「').replace(']', '」')
            # Fix "N của ほう" -> "Nのほう"
            row[11] = row[11].replace('N của ほう', 'Nのほう')
            row[11] = row[11].replace('A của ほうが Bより', 'Aのほうが Bより')
            row[11] = row[11].replace('N của ほか', 'Nのほか')
            if 'メンバー全員 of たゆまぬ努力' in row[11]:
                row[11] = row[11].replace('メンバー全員 of たゆまぬ努力', 'メンバー全員のたゆまぬ努力')
    with open(file_path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(rows)

    # part_88.csv
    file_path = 'mondai2_ordering/csv_filled/set_3_academic/part_88.csv'
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        rows = list(reader)
    for row in rows:
        if len(row) > 11:
            row[11] = row[11].replace(' trợ từ を ', ' trợ từ 「を」 ')
            row[11] = row[11].replace('A là Bほど', 'AはBほど')
            row[11] = row[11].replace('N là ない', 'Nはない')
            if '大切な顧客 of' in row[4]:
                row[4] = row[4].replace('大切な顧客 of', '大切な顧客の')
            if '大切な顧客 of' in row[5]:
                row[5] = row[5].replace('大切な顧客 of', '大切な顧客の')
            if '大切な顧客 of' in row[11]:
                row[11] = row[11].replace('大切な顧客 of', '大切な顧客の')
    with open(file_path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(rows)

    # part_89.csv
    file_path = 'mondai2_ordering/csv_filled/set_3_academic/part_89.csv'
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        rows = list(reader)
    for row in rows:
        if len(row) > 11:
            row[11] = re.sub(r"'([^']+)'", r'「\1」', row[11])
            row[11] = row[11].replace('「N đềあるまい」', '「Nであるまい」')
            row[11] = row[11].replace('「V của ではあるまいか」', '「Vのではあるまいか」')
            row[11] = row[11].replace('「N của 前で」', '「Nの前で」')
    with open(file_path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(rows)

    # part_90.csv
    file_path = 'mondai2_ordering/csv_filled/set_3_academic/part_90.csv'
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        rows = list(reader)
    for row in rows:
        if len(row) > 11:
            row[11] = row[11].replace('B của 方がまだいい', 'Bの方がまだいい')
            row[11] = row[11].replace('V của もまた', 'Vのもまた')
    with open(file_path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(rows)

if __name__ == "__main__":
    fix()
    print("Fixed batch 18 manually")
