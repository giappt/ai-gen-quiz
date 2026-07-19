import csv
import re

def clean_quotes(text):
    text = re.sub(r'\'(.*?)\'', r'「\1」', text)
    text = re.sub(r'""(.*?)""', r'「\1」', text)
    text = re.sub(r'"(.*?)"', r'「\1」', text)
    return text

def fix():
    # part_56.csv
    file_path = 'mondai2_ordering/csv_filled/set_3_academic/part_56.csv'
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        rows = list(reader)
        
    for row in rows:
        if len(row) > 11:
            row[11] = clean_quotes(row[11])
            if 'A：田中部長は' in row[4]:
                row[4] = row[4].replace('A：', 'A「').replace('B：', '」B「') + '」'
                row[5] = row[5].replace('A：', 'A「').replace('B：', '」B「')
                row[10] = row[10] + '」'
            if 'A：企画書が' in row[4]:
                row[4] = row[4].replace('A：', 'A「').replace('B：', '」B「') + '」'
                row[5] = row[5].replace('A：', 'A「').replace('B：', '」B「')
                row[10] = row[10] + '」'
                
    with open(file_path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(rows)

    # part_57.csv
    file_path = 'mondai2_ordering/csv_filled/set_3_academic/part_57.csv'
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        rows = list(reader)
        
    new_rows = []
    for row in rows:
        if len(row) > 11:
            if 'A「来月から予算が削減されます' in row[4]:
                continue
            if '開発を中止するとなると役員会の' in row[4]:
                continue
            if '何度もプレゼンの練習を重ねましたが' in row[4]:
                continue
            row[11] = clean_quotes(row[11])
            new_rows.append(row)
        else:
            new_rows.append(row)
            
    row19 = [
        'となると', 'となると', 'N2', '①A：先生はご病気で昨日入院されました。B：となると、しばらく授業は休講ということになりますね。',
        'A「来月から予算が削減されます」B「となると出張の計画を見直す必要がありますね」',
        'A「来月から予算が削減されます」B「', 'となると', '出張の', '計画を', '見直す', '必要がありますね」',
        '「となると」 đứng đầu câu phản hồi của nhân vật B mang nghĩa 「Nếu vậy thì...」. Theo sau là cụm danh từ 「出張の計画を」 đóng vai trò tân ngữ cho động từ 「見直す」 (xem xét lại). Cụm này bổ nghĩa trực tiếp cho phần kết câu 「必要がありますね」.'
    ]
    row20 = [
        'となると', 'となると', 'N2', '①A：先生はご病気で昨日入院されました。B：となると、しばらく授業は休講ということになりますね。',
        '開発を中止するとなると役員会の承認が必要になります。',
        '開発を', '中止する', 'と', 'なると', '役員会の', '承認が必要になります。',
        'Ngữ pháp 「V-る + となると」 (Nếu rơi vào trường hợp làm V). 「開発を」 là tân ngữ của 「中止する」. Động từ nguyên thể đi với 「と」 + 「なると」 tạo vế giả định. Vế sau chỉ kết quả tất yếu mang tính thủ tục công sở: 「役員会の承認が必要になります」.'
    ]
    row21 = [
        'となると', 'いざとなると', 'N2', '①危険は承知の手術だが、いざとなると不安になるものだ。',
        '何度もプレゼンの練習を重ねましたが、いざとなると緊張してうまく話せませんでした。',
        '何度もプレゼンの練習を重ねましたが、', 'いざ', 'となると', '緊張して', 'うまく', '話せませんでした。',
        'Cụm từ cố định 「いざとなると」 mang nghĩa 「đến lúc đó thì / đến khi thực sự đối mặt thì」. Dù đã luyện tập nhiều nhưng khi đến lúc thuyết trình lại căng thẳng (緊張して) dẫn đến kết quả (うまく話せませんでした).'
    ]
    
    new_rows.append(row19)
    new_rows.append(row20)
    new_rows.append(row21)
    
    with open(file_path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(new_rows)

    # part_58.csv
    file_path = 'mondai2_ordering/csv_filled/set_3_academic/part_58.csv'
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        rows = list(reader)
        
    for row in rows:
        if len(row) > 11:
            row[11] = clean_quotes(row[11]).replace('markdown/', '')
            
    with open(file_path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(rows)

    # part_59.csv
    file_path = 'mondai2_ordering/csv_filled/set_3_academic/part_59.csv'
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        rows = list(reader)
        
    for row in rows:
        if len(row) > 11:
            row[11] = clean_quotes(row[11])
            
    with open(file_path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(rows)

    # part_60.csv
    file_path = 'mondai2_ordering/csv_filled/set_3_academic/part_60.csv'
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        rows = list(reader)
        
    for row in rows:
        if len(row) > 11:
            row[11] = clean_quotes(row[11])
            if 'だったとやら」 là dạng' in row[11]:
                if not row[11].startswith('「'):
                    row[11] = '「' + row[11]
            
            if 'A「英語のプレゼンが' in row[4] and not row[4].endswith('」'):
                row[4] = row[4] + '」'
                row[10] = row[10] + '」'
                
    with open(file_path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(rows)

if __name__ == "__main__":
    fix()
    print("Fixed batch 12 manually")
