import csv

def fix():
    file_path = 'mondai2_ordering/csv_filled/set_3_academic/part_34.csv'
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        rows = list(reader)
    
    for i, row in enumerate(rows):
        if 'なぜ来ないの' in row[4]:
            rows[i][4] = 'A「なぜ来ないの？」 B「だって会議が長引いているんだもん。」'
            rows[i][5] = 'A「なぜ来ないの？」 B「'
            if not rows[i][10].endswith('」'):
                if rows[i][10] == 'もん。':
                    rows[i][10] = 'もん。」'
                else:
                    rows[i][10] = rows[i][10] + '」'
            
    with open(file_path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(rows)

if __name__ == "__main__":
    fix()
    print("Fixed batch 7 manually")
