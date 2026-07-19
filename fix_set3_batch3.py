import csv

def fix_batch3():
    # part 12 (row 18 is index 17)
    with open('mondai2_ordering/csv_filled/set_3_academic/part_12.csv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        rows = list(reader)
    if 'R-gabori' in rows[17][11]:
        rows[17][11] = rows[17][11].replace('R-gabori', 'R-がかり')
    with open('mondai2_ordering/csv_filled/set_3_academic/part_12.csv', 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(rows)

    # part 13 (row 18 is index 17)
    with open('mondai2_ordering/csv_filled/set_3_academic/part_13.csv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        rows = list(reader)
    if 'がchí' in rows[17][11]:
        rows[17][11] = rows[17][11].replace('がchí', 'がち')
    with open('mondai2_ordering/csv_filled/set_3_academic/part_13.csv', 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(rows)

if __name__ == "__main__":
    fix_batch3()
    print("Fixed Batch 3 manually")
