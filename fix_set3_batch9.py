import csv

def fix():
    # part_41.csv
    file_path = 'mondai2_ordering/csv_filled/set_3_academic/part_41.csv'
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        rows = list(reader)
    
    fixes_41 = {
        6: ['新しい社長が', '就任してから', 'というものは', '会社の', '雰囲気ががらりと', '変わった。'],
        8: ['部長が', '私の', '報告書を', 'チェックして', 'くださっ', 'た。'],
        9: ['明日の', '会議の', '資料を', '集めて', 'くださ', 'る？'],
        10: ['急いで', '資料を', '持って', '会議室へ', '走って', 'きました。'],
        11: ['先週', 'アメリカの', '出張から', '帰って', 'きま', 'した。'],
        15: ['最近', '新しい', '注文が', '増えて', 'きた', 'ようです。'],
        16: ['取引先が', '会議の', '予定を', '連絡して', 'きたので', '確認してください。'],
        19: ['同僚が', '私の', '仕事を', '手伝って', 'くれる', 'ので助かります。']
    }
    
    for row_idx, chunks in fixes_41.items():
        if row_idx < len(rows):
            rows[row_idx][5] = chunks[0]
            rows[row_idx][6] = chunks[1]
            rows[row_idx][7] = chunks[2]
            rows[row_idx][8] = chunks[3]
            rows[row_idx][9] = chunks[4]
            rows[row_idx][10] = chunks[5]
            rows[row_idx][4] = ''.join(chunks)

    with open(file_path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(rows)

    # part_43.csv
    file_path = 'mondai2_ordering/csv_filled/set_3_academic/part_43.csv'
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        rows = list(reader)
        
    for row in rows:
        for i in range(4, 11):
            if '指示 te' in row[i]:
                row[i] = row[i].replace('指示 te', '指示を')
                
        if len(row) > 10:
            row[4] = row[5] + row[6] + row[7] + row[8] + row[9] + row[10]

    with open(file_path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(rows)

    # part_45.csv
    file_path = 'mondai2_ordering/csv_filled/set_3_academic/part_45.csv'
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        rows = list(reader)
        
    for row in rows:
        for i in range(4, 11):
            row[i] = row[i].replace('\\', '')
            
        if 'メールのご返信は来週' in row[4] and not row[4].endswith('でもいいですよ。'):
            row[10] = 'でもいいですよ。'
            
        if len(row) > 11:
            row[11] = row[11].replace('đ đềいい', 'でもいい')
            row[11] = row[11].replace('độ đềしたら', 'でもしたら')
            row[11] = row[11].replace('N/Na đề', 'N/Naでも')
            row[11] = row[11].replace('để nối h', 'でも')
            row[11] = row[11].replace('để n', 'でも')
        
        if len(row) > 10:
            row[4] = row[5] + row[6] + row[7] + row[8] + row[9] + row[10]

    with open(file_path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(rows)

if __name__ == "__main__":
    fix()
    print("Fixed batch 9 manually")
