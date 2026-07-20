import csv, os

dir_path = r'd:\pj\xx\ai-gen-quiz\mondai2_ordering\csv_filled\set_1_daily'

fixes = {
    "part_57.csv-14": "Cấu trúc 'Nのこととなったら' mang nghĩa 'cứ nói đến chuyện N là...'. Danh từ 'ゲーム' kết hợp với 'のこととなったら' tạo thành vế điều kiện, chỉ ra chủ đề gây sự thay đổi. Trạng ngữ '寝る時間も' và động từ '惜しんで' bổ nghĩa cho hành động '熱中してしまう' ở vế sau.",
    "part_58.csv-1": "Cấu trúc 'Nのこととなると' có nghĩa là 'khi nói đến chuyện về N'. Tính từ '新しい' bổ nghĩa cho danh từ 'バッグ'. Cụm 'バッグのこと' đi với 'となると' tạo thành vế điều kiện thúc đẩy một phản ứng đặc biệt ở vế sau.",
    "part_58.csv-5": "Cấu trúc 'Nのこととなれば' diễn tả ý 'nếu là chuyện liên quan đến N'. Tính từ '大好きな' bổ nghĩa cho 'アニメ'. Cụm 'アニメのこと' đi kèm 'となれば' tạo thành điều kiện giả định dẫn đến sự thay đổi trạng thái nhiệt tình ở vế sau."
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

print("Batch 12 updated safely!")
