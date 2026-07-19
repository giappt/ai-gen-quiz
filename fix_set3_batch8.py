import csv

def fix():
    file_path = 'mondai2_ordering/csv_filled/set_3_academic/part_40.csv'
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        rows = list(reader)
    
    for i, row in enumerate(rows):
        if 'A：「資料は' in row[4]:
            rows[i][4] = 'A「資料はできましたか。」 B「いいえ、まだ終わっていません。」'
            rows[i][5] = 'A「資料は'
            rows[i][6] = 'できましたか。」'
            rows[i][7] = 'B「いいえ、'
            if rows[i][10] == 'いません。':
                rows[i][10] = 'いません。」'
            else:
                rows[i][10] = rows[i][10] + '」'
            
    with open(file_path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(rows)

if __name__ == "__main__":
    fix()
    print("Fixed batch 8 manually")
