import csv, os

dir_path = r'd:\pj\xx\ai-gen-quiz\mondai2_ordering\csv_filled\set_2_business'

fixes = {
    "part_22.csv-16": "Nêu lý do tiến cử nhân sự. '経験が豊富だし、' (kinh nghiệm phong phú và...) đi trước, tiếp theo là cụm '人脈も' (mối quan hệ cũng) ghép với '広いから、新規プロジェクトの' (...rộng, nên rất thích hợp làm người chịu trách nhiệm của dự án mới).",
    "part_23.csv-1": "Cấu trúc 「Nでしかない」 biểu thị ý nghĩa chỉ là N, không hơn không kém. Danh từ 「計画」 được bổ nghĩa bởi từ 「ただの」. Các thành phần kết hợp nhịp nhàng: bổ ngữ đứng trước danh từ, sau đó đi liền với trợ từ 「で」, 「しか」 và kết thúc bằng vị ngữ phủ định 「ない」。",
    "part_23.csv-10": "Cấu trúc 「V-た次第だ」 dùng để trình bày diễn biến, lý do của sự việc trong bối cảnh lịch sự. Tân ngữ 「原因を」 bổ nghĩa cho động từ 「調査した」, cụm này bổ nghĩa cho danh từ 「結果」。 Hành động khiêm nhường ngữ 「ご報告申し上げた」 đứng ngay trước 「次第」 để hoàn thành vế câu.",
    "part_23.csv-18": "Từ nối khẩu ngữ 「じゃあ」 biểu thị sự suy luận dựa vào câu nói trước của đối phương. Các thành phần phát triển nhịp nhàng: Chủ ngữ ngôi thứ nhất 「私は」 -> Trạng ngữ thời gian 「月曜日に」 -> Tân ngữ trực tiếp 「資料を」 bổ nghĩa trực tiếp cho hành động ở phần đuôi câu.",
    "part_24.csv-1": "Chủ ngữ chính của câu là 「このファイルは」 (File này là). Vị ngữ chính kết thúc bằng danh từ 「資料」 đi kèm thể phủ định thông thường 「じゃない」 (không phải là tài liệu). Các cụm danh từ và tính từ bổ nghĩa cho tài liệu kết nối hợp lý từ bao quát đến chi tiết: thuộc về công ty A 「A社の」, tính chất quan trọng 「大切な」, và phục vụ cho cuộc họp 「会議の」。",
    "part_24.csv-3": "Trạng từ liên kết hành động 「連絡もせずに」 (mà không thèm liên lạc) mở đầu câu. Tiếp theo là các thành phần bổ nghĩa cho cuộc họp phát triển mượt mà: 「大切な」 (quan trọng) -> 「今日の」 (hôm nay) -> danh từ chỉ nơi chốn/sự kiện 「会議に」 đi với động từ chỉ hành vi bị phê phán 「遅れるなんて」 (việc đi muộn...). Đuôi tính từ tính chất 「ひどい」 (tồi tệ) đi liền với cấu trúc khiển trách 「じゃないか」。"
}

leakage_str1 = " Câu được chia thành các phần tương ứng để kiểm tra khả năng sắp xếp trật tự từ ngữ pháp trong tiếng Nhật một cách chính xác nhất."
leakage_str2 = "Câu được chia thành các phần tương ứng để kiểm tra khả năng sắp xếp trật tự từ ngữ pháp trong tiếng Nhật một cách chính xác nhất."

files = ['part_21.csv', 'part_22.csv', 'part_23.csv', 'part_24.csv', 'part_25.csv']

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
        
        # Remove leakages globally
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

print("Batch 5 of set 2 updated safely!")
