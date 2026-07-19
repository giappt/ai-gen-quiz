import csv
import re

# Fix part_73 and part_105 quotes
for f_name in ['part_73.csv', 'part_105.csv']:
    file_path = f'mondai2_ordering/csv_filled/set_1_daily/{f_name}'
    lines = []
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) > 11:
                exp = row[11]
                if exp.count('「') != exp.count('」'):
                    exp = re.sub(r'^([^「]+)」', r'「\1」', exp)
                    row[11] = exp
            lines.append(row)
    with open(file_path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(lines)

# Fix part_75
file_path = 'mondai2_ordering/csv_filled/set_1_daily/part_75.csv'
lines = []
with open(file_path, 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row_idx, row in enumerate(reader):
        if row_idx == 1:
            row[11] = "Cấu trúc 'Vるには' mang nghĩa 'Để làm V thì...'. Ở đây, '美味しいカレーを作る' (Làm món cà ri ngon) đi với 'には', vế sau là điều kiện bắt buộc 'スパイスをたくさん炒めなければならない' (Phải xào thật nhiều gia vị)."
        elif row_idx == 2:
            row[4] = "料理を作るには作るが、あまり美味しくないかもしれない。"
            row[5] = ""
            row[6] = "料理を"
            row[7] = "作るには"
            row[8] = "作るが、"
            row[9] = "あまり美味しくない"
            row[10] = "かもしれない。"
            row[11] = "Cấu trúc 'VるにはVが' mang ý nghĩa nhượng bộ 'Có làm V thì có làm thật, nhưng...'. '作る' lặp lại hai lần, theo sau là mệnh đề ngược hướng 'あまり美味しくないかもしれない' (có lẽ không ngon lắm)."
        elif row_idx == 10:
            row[4] = "彼が成功したのは、日々の努力の賜物にほかならない。"
            row[5] = ""
            row[6] = "彼が成功したのは、"
            row[7] = "日々の努力の"
            row[8] = "賜物に"
            row[9] = "ほかならない。"
            row[10] = ""
            row[11] = "Cấu trúc '～にほかならない' mang ý nghĩa 'chính là/không gì khác ngoài...'. Dùng để khẳng định mạnh mẽ nguyên nhân hay bản chất của sự việc. Ở đây, '努力の賜物' (thành quả của nỗ lực) kết hợp trực tiếp với 'にほかならない'."
        lines.append(row)
with open(file_path, 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(lines)

print("Fixed remaining issues")
