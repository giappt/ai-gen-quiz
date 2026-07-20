import csv, os

dir_path = r'd:\pj\xx\ai-gen-quiz\mondai2_ordering\csv_filled\set_1_daily'

fixes = {
    "part_71.csv-1": "'における' đi sau danh từ '我が家' tạo thành cụm định ngữ '我が家における' (tại nhà tôi) để bổ nghĩa cho danh từ 'ルール' (quy tắc) phía sau thông qua từ nối '掃除の'. Các thành phần bổ nghĩa cho nhau một cách tự nhiên.",
    "part_71.csv-2": "Mẫu 'にかかっては' đi sau danh từ chỉ người '母' thể hiện ý 'nếu rơi vào tay ai/dưới tài năng của ai'. Mạch câu dẫn dắt tự nhiên từ chủ thể đến đối tượng '残り物も' và kết quả biến đổi '豪華なディナーになります'.",
    "part_71.csv-3": "Mẫu 'にかかわらず' kết hợp với danh từ '曜日' thành cụm '曜日にかかわらず' mang nghĩa 'bất kể thứ mấy'. Câu diễn tiến mạch lạc từ danh từ mốc điều kiện đến trạng từ chỉ tần suất 'いつも' và khép lại bằng trạng thái của vị ngữ.",
    "part_71.csv-4": "Cấu trúc 'V-るかV-ないかにかかわらず' thể hiện ý 'bất kể hành động có xảy ra hay không'. Câu mở đầu bằng cụm '降るか降らないかにかかわらず', sau đó bổ sung trạng từ thời gian '毎日' và kết nối với hành động '散歩に出かけます'.",
    "part_71.csv-6": "Mẫu 'にかけたら' đặt sau danh từ chỉ lĩnh vực '腕前' để nhấn mạnh khía cạnh tài năng. Vế sau nối tiếp với cụm diễn đạt so sánh quen thuộc 'うちの弟の右に出る者はいない' (không ai vượt qua được em trai tôi).",
    "part_71.csv-11": "Mẫu 'にかたくない' thường đi cố định với danh từ '想像' tạo thành '想像にかたくない' (không khó để tưởng tượng). Câu phát triển theo chuỗi bổ nghĩa liên tiếp: định ngữ chỉ tình huống phức tạp bổ nghĩa cho '時', cụm '時の' bổ nghĩa cho tâm trạng '親の心配は' trước khi kết thúc bằng vị ngữ.",
    "part_71.csv-12": "Mẫu 'にかまけて' diễn tả việc quá bận rộn/cuốn vào danh từ 'ゲーム' dẫn đến lơ là việc khác. Các thành phần nối tiếp từ danh từ bổ nghĩa '趣味の' đến cụm từ chứa ngữ pháp, rồi dẫn đến hành động bị lãng quên '宿題をやるのを忘れていた'.",
    "part_71.csv-13": "Mẫu 'にかわって' biểu thị sự thay thế cho đối tượng danh từ đứng trước '父'. Cụm '忙しい父にかわって' làm trạng ngữ, theo sau là chủ ngữ mới '私が' thực hiện hành động '散歩に行っています' một cách tự nhiên.",
    "part_71.csv-14": "Mẫu 'にかわり' là biến thể văn viết mang tính trang trọng của 'にかわって' (thay mặt cho). Câu bắt đầu bằng định ngữ bổ nghĩa cho người được thay thế 'ひいた妻にかわり', nối tiếp là chủ ngữ thực tế và danh từ chỉ mục đích cuộc họp đứng trước vị ngữ.",
    "part_71.csv-16": "Mẫu 'にきまっている' thể hiện sự phán đoán chắc chắn của người nói và luôn đứng ở cuối câu làm vị ngữ. Các thành phần tạo thành một mệnh đề danh từ hóa đóng vai trò chủ ngữ '食べたのは', sau đó nối với đích danh đối tượng '弟に' rồi kết thúc câu.",
    "part_71.csv-18": "Mẫu 'に比べて' đứng sau danh từ mốc so sánh '夏'. Câu phân chia rõ ràng vế so sánh '昨年の夏に比べて' đứng trước, tiếp theo là trạng thái hiện tại '今年の夏は' kèm phó từ nhấn mạnh '一段と' để bổ nghĩa cho cụm '気がします'.",
    "part_71.csv-19": "Mẫu 'にくわえ' là thể liên dụng dùng để liệt kê thêm danh từ đồng loại. Câu diễn tiến từ trạng ngữ thời gian '最近は', nối với danh từ bất lợi thứ nhất '値上げにくわえ', rồi đến bất lợi thứ hai '電気代も' và khép lại bằng hệ quả kéo theo.",
    "part_71.csv-20": "Mẫu 'にくわえて' dùng để bổ sung thêm tính chất cho danh từ '安さ'. Câu đi từ chủ đề 'この店は', nối tiếp tính chất tích cực thứ nhất '安さに くわえて', sau đó là '味も', liền kề mệnh đề nguyên nhân '良いので' và cuối cùng là kết quả."
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

print("Batch 15 updated safely!")
