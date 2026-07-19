import csv

def fix():
    # part_71.csv
    file_path = 'mondai2_ordering/csv_filled/set_3_academic/part_71.csv'
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        rows = list(reader)
    
    for row in rows:
        if len(row) > 11:
            # Row 2
            if '取引先との交渉における' in row[4]:
                row[4] = '取引先との交渉における最重要課題は、信頼関係の構築であると考えます。'
                row[5] = '取引先との'
                row[6] = '交渉における'
                row[7] = '最重要課題は、'
                row[8] = '信頼関係の'
                row[9] = '構築で'
                row[10] = 'あると考えます。'
            
            # Row 13
            if 'にかかまけて' in row[4]:
                row[4] = row[4].replace('にかかまけて', 'にかまけて')
                row[6] = row[6].replace('にかかまけて', 'にかまけて')
            
            # Row 15
            if '就任いたすこと' in row[4]:
                row[4] = row[4].replace('就任いたす', '就任する')
                row[9] = row[9].replace('就任いたす', '就任する')

    with open(file_path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(rows)

    # part_73.csv
    file_path = 'mondai2_ordering/csv_filled/set_3_academic/part_73.csv'
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        rows = list(reader)
    for row in rows:
        if len(row) > 11:
            # Row 2
            if '田中部長にしても今回の急な仕様変更には' in row[4]:
                row[5] = '田中部長'
                row[6] = 'にしても'
                row[7] = '今回の急な仕様変更には'
                row[8] = '困惑している'
                row[9] = 'ようです'
                row[10] = '。'
            # Row 4
            if 'メールにしても郵送にしても' in row[4]:
                row[6] = 'メールにしても'
                row[7] = '郵送にしても'
                row[8] = '今月末までに'
                row[9] = 'ご送付'
                row[10] = 'ください。'
    with open(file_path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(rows)

    # part_74.csv
    file_path = 'mondai2_ordering/csv_filled/set_3_academic/part_74.csv'
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        rows = list(reader)
    for row in rows:
        if len(row) > 11:
            if 'narimashita' in row[4]:
                row[4] = row[4].replace('narimashita', 'なりました')
                row[10] = row[10].replace('narimashita', 'なりました')
                row[11] = row[11].replace('narimashita', 'なりました')
    with open(file_path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(rows)

if __name__ == "__main__":
    fix()
    print("Fixed batch 15 manually")
