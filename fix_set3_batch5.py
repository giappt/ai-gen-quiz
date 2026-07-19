import csv

def fix():
    # part_21.csv
    file_path = 'mondai2_ordering/csv_filled/set_3_academic/part_21.csv'
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        rows = list(reader)
    
    # row 5 (index 4)
    if '締切はいつですか' in rows[4][4]:
        rows[4][4] = 'A「締切はいつですか」 B「さあ私にはよくわかりません」'
        rows[4][10] = '」'
        
    with open(file_path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(rows)

if __name__ == "__main__":
    fix()
    print("Fixed batch 5 manually")
