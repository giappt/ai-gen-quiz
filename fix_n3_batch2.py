import csv

file_path = 'mondai2_ordering/csv_filled/set_1_daily/part_38.csv'
lines = []
with open(file_path, 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row_idx, row in enumerate(reader):
        if row_idx == 19:
            row[4] = "もう、心配しなくても大丈夫だってば。"
            row[5] = "もう、"
            row[6] = "心配"
            row[7] = "しなくても"
            row[8] = "大丈夫"
            row[9] = "だってば。"
            row[10] = ""
            row[11] = "Trợ từ 'ってば' đứng cuối câu dùng để nhấn mạnh sự khẳng định, thường mang sắc thái mất kiên nhẫn khi lặp lại lời đã nói (Đã bảo là...). Động từ '心配する' chia thể phủ định 'しなくても' (không cần lo) kết hợp với tính từ '大丈夫だ' (không sao đâu) tạo thành cụm ý nghĩa an ủi mạnh mẽ."
        lines.append(row)

with open(file_path, 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(lines)
print("Fixed part_38.csv row 20")
