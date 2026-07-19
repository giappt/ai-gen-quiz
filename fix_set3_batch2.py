import csv

def fix_batch2():
    with open('mondai2_ordering/csv_filled/set_3_academic/part_7.csv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        rows = list(reader)
    # Row 12 (index 11)
    if 'いつしか' in rows[11][0]:
        rows[11][11] = 'Phó từ 「いつしか」 (lúc nào không biết) chỉ sự thay đổi âm thầm theo thời gian, bổ nghĩa cho hành động vế sau. Cụm từ định ngữ 「入社当時の」 bổ nghĩa cho danh từ tân ngữ 「新鮮な気持ちを」, tiếp theo là cụm hành động mang nghĩa đánh mất dần 「忘れかけてしまっておりました」。'
    
    with open('mondai2_ordering/csv_filled/set_3_academic/part_7.csv', 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(rows)

if __name__ == "__main__":
    fix_batch2()
    print("Fixed Batch 2 manually")
