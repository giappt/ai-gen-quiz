import csv

with open('mondai2_ordering/csv_filled/set_1_daily/part_35.csv', 'r', encoding='utf-8') as f:
    rows = list(csv.reader(f))

# Line 11 (index 10)
rows[10][4] = 'スマホはあったらあったで時間を無駄にするし、なかったらないで不便だ。'
rows[10][5] = 'スマホは'
rows[10][6] = 'あったら'
rows[10][7] = 'あったで'
rows[10][8] = '時間を'
rows[10][9] = '無駄にするし、'
rows[10][10] = 'なかったらないで不便だ。'

# Line 18 (index 17)
rows[17][4] = 'あの新しいゲーム機、昨日安いうちに買ったらよかったなあ。'
rows[17][5] = 'あの新しいゲーム機、'
rows[17][6] = '昨日'
rows[17][7] = '安いうちに'
rows[17][8] = '買ったら'
rows[17][9] = 'よかった'
rows[17][10] = 'なあ。'

# Line 21 (index 20)
rows[20][4] = '休みの日には、本を読んだり音楽を聞いたりしてのんびり過ごす。'
rows[20][5] = '休みの日には、'
rows[20][6] = '本を'
rows[20][7] = '読んだり'
rows[20][8] = '音楽を'
rows[20][9] = '聞いたりして'
rows[20][10] = 'のんびり過ごす。'

with open('mondai2_ordering/csv_filled/set_1_daily/part_35.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(rows)
