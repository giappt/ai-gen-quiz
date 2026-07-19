import csv
import re

def fix():
    # part_81.csv
    file_path = 'mondai2_ordering/csv_filled/set_3_academic/part_81.csv'
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        rows = list(reader)
    
    for row in rows:
        if len(row) > 11:
            if 'A「' in row[4]:
                if row[0] == 'はい' and row[1] == 'はい＜肯定＞':
                    row[4] = 'A「これは今日の会議の資料ですか」B「はい、そうです。」'
                    row[5] = 'A「これは'
                    row[6] = '今日の会議の'
                    row[7] = '資料ですか」'
                    row[8] = 'B「はい、'
                    row[9] = 'そうです'
                    row[10] = '。」'
                elif row[0] == 'はい' and row[1] == 'はい＜承諾＞':
                    row[4] = 'A「この資料のコピーをお願いします」B「はい、かしこまりました。」'
                    row[5] = 'A「この'
                    row[6] = '資料の'
                    row[7] = 'コピーをお願いします」'
                    row[8] = 'B「はい、'
                    row[9] = 'かしこまりました'
                    row[10] = '。」'
                elif row[0] == 'はい' and row[1] == 'はい＜応答＞':
                    row[4] = 'A「田中さん、ちょっといいですか」B「はい、何でしょうか。」'
                    row[5] = 'A「田中さん、'
                    row[6] = 'ちょっと'
                    row[7] = 'いいですか」'
                    row[8] = 'B「はい、'
                    row[9] = '何でしょうか'
                    row[10] = '。」'
                elif row[0] == 'はい' and row[1] == 'はい＜あいづち＞':
                    row[4] = 'A「明日の会議の件ですが」B「はい」A「午後3時に変更になりました」B「承知いたしました。」'
                    row[5] = 'A「明日の会議の件ですが」'
                    row[6] = 'B「はい」'
                    row[7] = 'A「午後3時に'
                    row[8] = '変更になりました」'
                    row[9] = 'B「承知いたしました'
                    row[10] = '。」'

    with open(file_path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(rows)

    # part_83.csv
    file_path = 'mondai2_ordering/csv_filled/set_3_academic/part_83.csv'
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        rows = list(reader)
    for row in rows:
        if len(row) > 11:
            if '主要取引先ををはじめ' in row[4]:
                row[4] = row[4].replace('主要取引先ををはじめ', '主要取引先をはじめ')
                row[6] = '主要取引先'
                row[7] = 'をはじめ、'
    with open(file_path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(rows)

    # part_85.csv
    file_path = 'mondai2_ordering/csv_filled/set_3_academic/part_85.csv'
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        rows = list(reader)
    for row in rows:
        if len(row) > 11:
            if 'ふuに' in row[11]:
                row[11] = row[11].replace('ふuに', 'ふうに')
    with open(file_path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(rows)

if __name__ == "__main__":
    fix()
    print("Fixed batch 17 manually")
