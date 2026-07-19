import csv

with open('mondai2_ordering/csv_filled/set_1_daily/part_43.csv', 'r', encoding='utf-8') as f:
    rows = list(csv.reader(f))

# Line 4 (index 3)
# Original Example: A「明日は雨みたいだよ。」B「では、今週末のお花見は中止にしよう。」
# Suffix: しよう。」
rows[3][4] = 'A「明日は雨みたいだよ。」B「では、今週末のお花見は中止にしよう。」'
rows[3][10] = 'しよう。」'

# Line 5 (index 4)
# Original Example: A「宿題の場所が分かりません。」B「では、机の上の私のノートを参考にしなさい。」
# Suffix: しなさい。」
rows[4][4] = 'A「宿題の場所が分かりません。」B「では、机の上の私のノートを参考にしなさい。」'
rows[4][10] = 'しなさい。」'

# Line 16 (index 15) (N2, but let's fix the quote anyway)
rows[15][4] = 'A「ごめん、牛乳を買い忘れた。」B「買い忘れたではないよ。コーヒーが飲めないじゃない。」'
rows[15][10] = 'コーヒーが飲めないじゃない。」'

# Line 19 (index 18) (N3 blank)
rows[18][4] = 'A「同級生に田中さんという女の子がいたじゃないか。」B「ああ、あの髪が長くてやせた子ね。」'
rows[18][5] = 'A「同級生に'
rows[18][6] = '田中さんという'
rows[18][7] = '女の子が'
rows[18][8] = 'いた'
rows[18][9] = 'じゃないか。」'
rows[18][10] = 'B「ああ、あの髪が長くてやせた子ね。」'
rows[18][11] = 'Mẫu câu kết hợp với động từ quá khứ (いた) + じゃないか để khơi gợi trí nhớ và xác nhận lại thông tin chắc chắn với người nghe.'

with open('mondai2_ordering/csv_filled/set_1_daily/part_43.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(rows)
