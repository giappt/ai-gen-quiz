import csv

def fix():
    # part_54.csv
    file_path = 'mondai2_ordering/csv_filled/set_3_academic/part_54.csv'
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        rows = list(reader)
        
    for row in rows:
        if len(row) > 11:
            row[11] = row[11].replace('事実にづき', '事実に基づき')
            
    with open(file_path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(rows)

    # part_55.csv
    file_path = 'mondai2_ordering/csv_filled/set_3_academic/part_55.csv'
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        rows = list(reader)
        
    for row in rows:
        # Row 10
        if len(row) > 4 and '見直さざる得ないだろう' in row[4]:
            row[4] = row[4].replace('見直さざる得ないだろう', '見直さざるを得ないだろう')
            row[9] = row[9].replace('見直さざる', '見直さざるを')
            row[11] = row[11].replace('見直さざる', '見直さざるを')
            
        # Row 11
        if len(row) > 4 and 'A「先方から納期の変更要請' in row[4] and not row[4].endswith('」'):
            row[4] = row[4] + '」'
            row[10] = row[10] + '」'
            
    with open(file_path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(rows)

if __name__ == "__main__":
    fix()
    print("Fixed batch 11 manually")
