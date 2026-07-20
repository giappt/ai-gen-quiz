import csv, os

dir_path = r'd:\pj\xx\ai-gen-quiz\mondai2_ordering\csv_filled\set_1_daily'

fixes = {
    "part_46.csv-20": "Prefix chỉ địa điểm tiếp nhận vật thể. Tân ngữ và động từ kết hợp thành 'お金を入れて', dùng thể て để liên kết chuỗi hành động diễn ra liên tiếp. Tiếp theo là tân ngữ 'ボタンを' đi với động từ hành động '押す'. Động từ ở dạng từ điển kết hợp trợ từ điều kiện 'と' tạo thành mẫu cấu trúc điều kiện hiển nhiên, dẫn đến vế kết quả tự động 'ジュースが出ます'.",
    "part_48.csv-10": "Cụm vị trí và trạng thái '家に明かりがついていない' là sự thật quan sát được. Cấu trúc 'ということは' biến vế này thành tiền đề suy luận. Vế sau 'みんな出かけている' là nội dung kết luận hợp lý dựa trên thực tế đó, đi với kết cấu khẳng định 'ということだ'.",
    "part_49.csv-7": "Cụm danh từ chủ đề được giới hạn bằng '日本の食べ物', đi liền với cấu trúc đưa ra đề tài câu chuyện 'といえば' (nói về...). Vế sau bắt đầu bằng phó từ 'やっぱり' kết hợp tân ngữ 'お寿司を'. Phó từ '一番に' (đầu tiên/trước nhất) bổ nghĩa cho động từ kết thúc câu '思い浮かべます' (nghĩ ngay đến)."
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

print("Batch 10 updated safely!")
