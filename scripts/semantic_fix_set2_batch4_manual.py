import csv, os

dir_path = r'd:\pj\xx\ai-gen-quiz\mondai2_ordering\csv_filled\set_2_business'

fixes = {
    "part_17.csv-18": "Chủ ngữ vế đầu là `あの厳しい専務が`. Động từ `絶賛する` đi với `くらいだから` mang nghĩa 'chính vì đến mức khen ngợi hết lời như thế nên...'. Vế sau đưa ra phán đoán hợp lý với chủ ngữ `彼の企画書は`, tính từ bổ nghĩa `相当な` và dự đoán `完成度なのだろう`.",
    "part_19.csv-6": "Tính từ '新しい' bổ nghĩa cho danh từ 'プロジェクト'. Cấu trúc 'Nのこと' biến danh từ thành một chủ đề nội dung cụ thể (về dự án mới), kết hợp với trợ từ 'を' để làm tân ngữ trực tiếp cho động từ '話し合いました' (đã thảo luận), được bổ nghĩa bằng phó từ '熱心に' (nhiệt tình).",
    "part_19.csv-17": "Tính từ đuôi -na '几帳面な' (cẩn thận/ngăn nắp) bổ nghĩa cho danh từ chỉ người '佐藤さん'. Cấu trúc 'Nのことだから' dựa trên đặc điểm tính cách quen thuộc của đối tượng để đưa ra một phán đoán có cơ sở vững chắc. '資料は' làm chủ đề cho vế nhận định phía sau.",
    "part_19.csv-20": "'来週の' bổ nghĩa cho danh từ '契約'. Cấu trúc 'Nのことで' dùng để giới thiệu, khoanh vùng vào chủ đề cụ thể được nhắc đến (về việc hợp đồng). Từ chỉ số lượng 'いくつか' kết hợp cụm định ngữ '確認したい' bổ nghĩa trực tiếp cho danh từ '点' ở vế đuôi tôn kính ngữ.",
    "part_20.csv-12": "Cấu trúc N3 ことになる ở đây mang ý nghĩa diễn dịch hoặc quy đổi một hành động sang một bản chất tương đương (đồng nghĩa với việc). Động từ thể quá khứ 反対した kết hợp với ことになります để giải thích rõ ràng hệ quả của việc vắng mặt."
}

leakage_str1 = " Câu được chia thành các phần tương ứng để kiểm tra khả năng sắp xếp trật tự từ ngữ pháp trong tiếng Nhật một cách chính xác nhất."
leakage_str2 = "Câu được chia thành các phần tương ứng để kiểm tra khả năng sắp xếp trật tự từ ngữ pháp trong tiếng Nhật một cách chính xác nhất."

files = ['part_16.csv', 'part_17.csv', 'part_18.csv', 'part_19.csv', 'part_20.csv']

for file in files:
    path = os.path.join(dir_path, file)
    with open(path, encoding='utf-8-sig') as f:
        r = list(csv.reader(f))
    
    headers = r[0]
    exp_idx = headers.index('Explanation') if 'Explanation' in headers else -1
    if exp_idx == -1: exp_idx = len(headers) - 1
    
    changed = False
    for i, row in enumerate(r):
        if i == 0: continue
        key = f"{file}-{i}"
        
        # Global leakages
        if len(row) > exp_idx:
            orig = row[exp_idx]
            new = orig.replace(leakage_str1, "").replace(leakage_str2, "")
            if orig != new:
                row[exp_idx] = new
                changed = True
        
        # Specific fixes
        if key in fixes:
            new_exp = fixes[key]
            del row[exp_idx:]
            row.append(new_exp)
            changed = True
            
    if changed:
        with open(path, 'w', encoding='utf-8-sig', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(r)

print("Batch 4 of set 2 updated safely!")
