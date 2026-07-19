import csv

def fix_batch1():
    # part 1, row 21 (index 20)
    with open('mondai2_ordering/csv_filled/set_3_academic/part_1.csv', 'r') as f:
        reader = csv.reader(f)
        rows = list(reader)
    row = rows[20]
    row[4] = "部長の後について会議室へ静かに移動してください。"
    row[5] = "部長の"
    row[6] = "後について"
    row[7] = "会議室へ"
    row[8] = "静かに"
    row[9] = "移動してください。"
    row[10] = ""
    row[11] = "「部長の後について」 (đi theo sau trưởng phòng) là mệnh đề trạng ngữ chỉ phương thức di chuyển. Trạng từ 「静かに」 (một cách yên tĩnh) bổ nghĩa cho động từ yêu cầu 「移動してください」 (hãy di chuyển) tới địa điểm 「会議室へ」."
    with open('mondai2_ordering/csv_filled/set_3_academic/part_1.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(rows)

    # part 3, row 15 (index 14)
    with open('mondai2_ordering/csv_filled/set_3_academic/part_3.csv', 'r') as f:
        reader = csv.reader(f)
        rows = list(reader)
    row = rows[14]
    row[7] = "AIの技術を"
    with open('mondai2_ordering/csv_filled/set_3_academic/part_3.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(rows)

    # part 4, add missing 「
    with open('mondai2_ordering/csv_filled/set_3_academic/part_4.csv', 'r') as f:
        reader = csv.reader(f)
        rows = list(reader)
    for i in range(1, len(rows)):
        if rows[i][11].count('」') > rows[i][11].count('「'):
            parts = rows[i][11].split('」', 1)
            if '「' not in parts[0]:
                rows[i][11] = '「' + rows[i][11]
    with open('mondai2_ordering/csv_filled/set_3_academic/part_4.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(rows)

if __name__ == "__main__":
    fix_batch1()
    print("Fixed Batch 1 manually")
