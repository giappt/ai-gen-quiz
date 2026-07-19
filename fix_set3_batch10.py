import csv

def fix():
    # part_46.csv
    file_path = 'mondai2_ordering/csv_filled/set_3_academic/part_46.csv'
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        rows = list(reader)
        
    for i, row in enumerate(rows):
        if len(row) > 11:
            row[11] = row[11].replace('đem', 'でも')
        
    rows[5][4] = '言葉だけでなく過去の確かな実績でもって弊社の技術力を証明いたします。'
    rows[5][9] = 'でもって'
    
    rows[6][4] = '我が社はアジア進出を果たした。でもって現地の有力企業との提携も進める方針です。'
    rows[6][6] = 'でもって'
    
    rows[7][4] = '新規事業の計画に対して彼は明確に反対するでもありませんが慎重な姿勢を崩しません。'
    rows[7][9] = 'でもありませんが'
    
    with open(file_path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(rows)

    # part_48.csv
    file_path = 'mondai2_ordering/csv_filled/set_3_academic/part_48.csv'
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        rows = list(reader)
        
    for row in rows:
        if len(row) > 4 and 'A「この企画書' in row[4]:
            row[4] = 'A「この企画書は修正が必要です」 B「というと」 A「データの数値が古いからです」'
            row[5] = 'A「この企画書は修正が必要です」 B「'
            row[6] = 'と'
            row[7] = 'いう'
            row[8] = 'と」 A「データの'
            row[9] = '数値が古い'
            row[10] = 'からです」'
        
    with open(file_path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(rows)
        
if __name__ == "__main__":
    fix()
    print("Fixed batch 10 manually")
