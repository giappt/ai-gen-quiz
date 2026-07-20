import csv, os

dir_path = r'd:\pj\xx\ai-gen-quiz\mondai2_ordering\csv_filled\set_1_daily'

fixes = {
    "part_53.csv-3": "Cụm '会社から' bổ nghĩa cho '帰る途中で' để chỉ hoàn cảnh trên đường đi làm về. Đại từ bất định 'どこかに' đi với động từ '落とした' tạo thành mệnh đề bổ nghĩa cho danh từ hình thức 'もの'. Cấu trúc '～ものと考えられる' dùng để đưa ra suy luận khách quan về một sự việc.",
    "part_54.csv-4": "Mẫu 'V-ているところをみると' mang ý nghĩa 'nhìn vào tình trạng/hành động đang diễn ra của ai đó để đưa ra phán đoán'. Cụm từ 'スマホを見ている' kết hợp với mẫu ngữ pháp làm căn cứ trực quan, dẫn tới mệnh đề phán đoán hợp lý ở vế sau về việc nhận tin nhắn của em gái '彼氏から返信が来たのだろう'.",
    "part_55.csv-1": "Trạng từ 'ちょうど' (vừa vặn) bổ nghĩa cho hành động xảy ra đúng thời điểm. Cấu trúc 'V-たところで' diễn tả mốc thời gian ngay sau khi một hành động vừa kết thúc thì có một sự việc khác xảy ra. Các vế câu lần lượt tiếp nối nhau: Tân ngữ 'お皿を' đi với động từ '洗い終わった', cấu trúc 'ところで', sau đó là chủ ngữ mới '夫が' và kết thúc bằng '帰ってきた'.",
    "part_55.csv-6": "Cấu trúc 'Nのところを' là lời mào đầu lịch sự khi làm phiền ai đó đang trong một trạng thái nhất định (ở đây là đang nghỉ ngơi 'お休みの'). Tiếp theo là hành động gây phiền hà cho đối phương được chia ở thể Te chỉ nguyên nhân '呼び出してしまって'. Cuối câu là trạng từ nhấn mạnh '本当に' đi kèm cụm từ xin lỗi quen thuộc '申し訳ありません'.",
    "part_55.csv-10": "Từ nối liên kết câu 'だとしたら' đứng đầu lời thoại của nhân vật B nhằm tiếp nhận thông tin từ nhân vật A và thiết lập giả định 'nếu đúng như vậy'. Vế sau tiếp diễn tự nhiên: Đối tượng chính '買い物は' được đưa lên trước, tiếp đến là trạng từ '今日中に' và khép lại bằng hành động hướng tới giải pháp '済ませよう'."
}

from collections import defaultdict
file_to_fixes = defaultdict(list)
for k, v in fixes.items():
    file, idx = k.split('-')
    file_to_fixes[file].append((int(idx), v))

for file, fix_list in file_to_fixes.items():
    path = os.path.join(dir_path, file)
    with open(path, encoding='utf-8-sig') as f:
        r = list(csv.reader(f))
    
    headers = r[0]
    exp_idx = headers.index('Explanation') if 'Explanation' in headers else -1
    if exp_idx == -1: exp_idx = len(headers) - 1
    
    for idx, new_exp in fix_list:
        row = r[idx]
        del row[exp_idx:]
        row.append(new_exp)
        
    with open(path, 'w', encoding='utf-8-sig', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(r)

print("Batch 11 updated safely!")
