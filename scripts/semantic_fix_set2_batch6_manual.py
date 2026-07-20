import csv, os

dir_path = r'd:\pj\xx\ai-gen-quiz\mondai2_ordering\csv_filled\set_2_business'

fixes = {
    "part_28.csv-1": "Liên từ 'そうして' dùng để liệt kê thành phần cuối cùng trong chuỗi. Câu mở đầu bằng chủ đề '本日の会議では', tiếp theo là các danh từ được liệt kê '新しい企画と' và '予算', sau đó là 'そうして' bổ sung cho danh từ cuối '今後のスケジュールについて' trước động từ '話し合います。'",
    "part_28.csv-4": "Trong bối cảnh hội thoại, 'そうすると' được người B dùng ở đầu câu để đưa ra kết luận từ lời nói của người A. Tiếp theo là định ngữ '週末の' bổ nghĩa cho '会議には', và cuối cùng là cụm động từ khả năng dạng phủ định '出席できませんね'.",
    "part_28.csv-20": "Liên từ 'そして' dùng để nối thành phần cuối cùng trong chuỗi liệt kê song song danh từ (A, B, và C). Câu liệt kê lần lượt các địa danh '東京', '大阪', sau đó dùng 'そして' kết nối với danh từ cuối cùng '福岡の'. Cụm này bổ nghĩa cho danh từ trung tâm '支店を' trước cụm vị ngữ '訪問する予定です'.",
    "part_29.csv-13": "Hành động đầu tiên được chỉ định bằng trạng từ 'まず' đi với danh từ 'この資料を' và cấu trúc sai khiến lịch sự '読んでください' (hãy đọc). Liên từ 'それから' (sau đó) đứng đầu câu tiếp theo để chuyển tiếp nhịp nhàng, dẫn đến hành động tiếp theo là '報告書を書いてください' (hãy viết báo cáo).",
    "part_30.csv-5": "'それとも' được dùng để nối hai lựa chọn danh từ '月曜日' và '火曜日'. Cấu trúc câu diễn tiến bằng danh từ thứ nhất đi kèm dấu phẩy, liên từ nối, danh từ thứ hai bổ nghĩa cho cụm từ nghi vấn 'どちらが' và kết thúc bằng đuôi kính ngữ 'よろしいでしょうか'.",
    "part_30.csv-13": "Cấu trúc 'それはそれでいい' biểu thị sự chấp nhận tạm thời đối với sự việc ở vế trước. Câu bắt đầu với 'それは' (chủ ngữ/chủ đề), 'それで' (bằng cách đó/như vậy), tính từ đi kèm trợ từ nối 'いいが、' để tạo tương phản, và kết thúc bằng mệnh đề chỉ cốt lõi '問題は...'.",
    "part_30.csv-17": "'それゆえ' là liên từ trang trọng biểu thị quan hệ nguyên nhân - kết quả. Vế sau được liên kết chặt chẽ: định ngữ '製品の' bổ nghĩa cho '品質管理には' (chủ đề), tiếp theo là cụm tân ngữ '一切の妥協を' và động từ phủ định ở cuối câu '許しません'.",
    "part_30.csv-19": "Cấu trúc 'V-たい' thể hiện nguyện vọng của người nói. Các thành phần kết hợp uyển chuyển: định ngữ 'クライアントの' bổ nghĩa cho danh từ nơi chốn 'オフィスへ', động từ bỏ masu '行き' kết hợp trực tiếp với 'たい' và kết thúc bằng 'です' để giữ tính lịch sự.",
    "part_30.csv-20": "Cấu trúc '～たいんですが' dùng để mở lời nhờ vả lịch sự. Trình tự cấu trúc gồm lượng từ '3冊' đứng trước động từ khiêm nhường bỏ masu 'いただき', liên kết với đuôi uớc muốn 'たい', từ mào đầu 'んですが、' và câu hỏi xin phép 'よろしいでしょうか'."
}

leakage_str1 = " Câu được chia thành các phần tương ứng để kiểm tra khả năng sắp xếp trật tự từ ngữ pháp trong tiếng Nhật một cách chính xác nhất."
leakage_str2 = "Câu được chia thành các phần tương ứng để kiểm tra khả năng sắp xếp trật tự từ ngữ pháp trong tiếng Nhật một cách chính xác nhất."

files = ['part_26.csv', 'part_27.csv', 'part_28.csv', 'part_29.csv', 'part_30.csv']

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

print("Batch 6 of set 2 updated safely!")
