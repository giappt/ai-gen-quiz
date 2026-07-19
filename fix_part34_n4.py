import csv

new_lines = {
    1: 'だといい,,N4,①A：みんな今頃安全な場所に避難していますよ。B：だといいが。心配だ。,明日は晴れるといいですね。,明日は,晴れると,いい,ですね,。,"Cấu trúc だといい/といい diễn tả mong muốn, hy vọng của người nói. Chủ ngữ 明日は đi với động từ 晴れる và cấu trúc といい, kết thúc bằng trợ từ cảm thán ですね."\n',
    14: 'ため,Nのため＜利益＞,N4,①こんなにきついことをいうのも君のためだ。,これは家族のために作った料理です。,これは,家族の,ために,作った,料理,です。,"Cấu trúc Nのために biểu thị mục đích (vì lợi ích của N). Danh từ 家族 đi với のために bổ nghĩa cho động từ 作った. Cụm 作った đóng vai trò định ngữ cho danh từ 料理."\n',
    15: 'ため,～ために　Nのために　V－るために,N4,①世界平和のために国際会議が開かれる。,日本語を勉強するために、日本へ来ました。,日本語を,勉強する,ために、,日本へ,来ました,。,"Cấu trúc Vるために diễn tả mục đích thực hiện hành động. Động từ 勉強する đi với ために (để học tiếng Nhật). Vế sau 日本へ来ました chỉ hành động đã thực hiện."\n'
}

with open('mondai2_ordering/csv_filled/set_1_daily/part_34.csv', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for idx, line in new_lines.items():
    if idx < len(lines):
        lines[idx] = line

with open('mondai2_ordering/csv_filled/set_1_daily/part_34.csv', 'w', encoding='utf-8') as f:
    f.writelines(lines)
