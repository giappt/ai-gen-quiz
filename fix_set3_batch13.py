import csv
import re

def clean_quotes(text):
    text = re.sub(r'\'(.*?)\'', r'「\1」', text)
    text = re.sub(r'""(.*?)""', r'「\1」', text)
    text = re.sub(r'"(.*?)"', r'「\1」', text)
    return text

def fix():
    # part_61.csv
    file_path = 'mondai2_ordering/csv_filled/set_3_academic/part_61.csv'
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        rows = list(reader)
    for row in rows:
        if len(row) > 11:
            row[11] = clean_quotes(row[11])
    with open(file_path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(rows)

    # part_62.csv
    file_path = 'mondai2_ordering/csv_filled/set_3_academic/part_62.csv'
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        rows = list(reader)
    
    new_rows = []
    for row in rows:
        if len(row) > 11:
            # Fix Row 11
            if '木村さんは電話で話しながら' in row[4]:
                row[4] = '木村さんは電話で話しながら資料を確認しています。'
                row[5] = '木村さんは'
                row[6] = '電話で'
                row[7] = '話しながら'
                row[8] = '資料を確認して'
                row[9] = 'います'
                row[10] = '。'
                row[11] = '「電話で」 chỉ phương thức/phương tiện thực hiện (bằng điện thoại). 「話しながら」 (động từ thể Masu bỏ masu + ながら) biểu thị hành động phụ diễn ra đồng thời. 「資料を」 là tân ngữ trực tiếp của hành động chính 「確認しています」 (đang xác nhận tài liệu).'
            else:
                row[11] = clean_quotes(row[11])
                if 'パソコンは' in row[11] and 'パソコン' in row[11]:
                    row[11] = row[11].replace('「パソコン は', '「パソコン」は').replace('「パソコン là', '「パソコン」 là')
            new_rows.append(row)
        else:
            new_rows.append(row)
            
    with open(file_path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(new_rows)

    # part_63.csv
    file_path = 'mondai2_ordering/csv_filled/set_3_academic/part_63.csv'
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        rows = list(reader)
    for row in rows:
        if len(row) > 11:
            row[11] = clean_quotes(row[11])
            if 'でなけりゃ」' in row[11] and not '「でなけりゃ」' in row[11]:
                row[11] = row[11].replace('でなけりゃ」', '「でなけりゃ」')
            row[11] = row[11].replace('+Suffix)', '')
    with open(file_path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(rows)

    # part_64.csv
    file_path = 'mondai2_ordering/csv_filled/set_3_academic/part_64.csv'
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        rows = list(reader)
    for row in rows:
        if len(row) > 11:
            row[11] = clean_quotes(row[11])
    with open(file_path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(rows)

    # part_65.csv
    file_path = 'mondai2_ordering/csv_filled/set_3_academic/part_65.csv'
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        rows = list(reader)
    for row in rows:
        if len(row) > 11:
            row[11] = clean_quotes(row[11])
            if 'A：' in row[4]:
                row[4] = row[4].replace('A：', 'A「').replace('B：', '」B「') + '」'
                row[5] = row[5].replace('A：', 'A「').replace('B：', '」B「')
                row[10] = row[10] + '」'
    with open(file_path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(rows)

if __name__ == "__main__":
    fix()
    print("Fixed batch 13 manually")
