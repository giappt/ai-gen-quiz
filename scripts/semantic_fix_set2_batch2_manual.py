import csv, os

dir_path = r'd:\pj\xx\ai-gen-quiz\mondai2_ordering\csv_filled\set_2_business'

fixes = {
    "part_6.csv-1": "Danh từ '期待' kết hợp với '以上の' để bổ nghĩa cho danh từ '成果' phía sau tạo thành cụm 'thành quả vượt trên kỳ vọng'. Cụm danh từ này làm tân ngữ cho động từ '上げる', nối liền với vế câu nguyên nhân kết quả lịch sự với '～ことができる'.",
    "part_7.csv-1": "Cụm từ '身に余る' (vượt quá bổn phận/vinh hạnh lớn lao) bổ nghĩa cho danh từ '光栄'. Mẫu ngữ pháp 'Nのいたり' biểu thị cảm xúc cực kỳ cao độ (ở đây là vô cùng vinh hạnh), kết hợp thành '光栄のいたり'. Đuôi câu sử dụng khiêm nhường ngữ '存じます' (nghĩ/cảm thấy) để thể hiện sự tôn kính trong bối cảnh kinh doanh.",
    "part_7.csv-2": "Trạng từ 'いちがい（に）' luôn đi kèm với thể phủ định ở cuối câu tạo thành cấu trúc 'không thể nhất loạt cho rằng/không hẳn là...'. Cụm '品質が劣っている' (chất lượng kém hơn) đi với phó từ phán đoán 'とは限らない' (không hẳn là) để tạo ra sự phủ định hoàn toàn hợp lý với vế trước.",
    "part_8.csv-1": "Cấu trúc '今ごろになって' (đến tận bây giờ/giờ này mới...) diễn tả sự việc xảy ra muộn màng so với kỳ vọng. Trạng từ chỉ thời gian muộn màng bổ nghĩa cho hành động bị động mang tính phiền toái '提出されても' (dù có được nộp), tiếp đó là kết quả thể hiện sự khó xử '困ります' (thật là phiền phức). Các thành phần kết hợp thành một cấu trúc hoàn chỉnh để đảm bảo văn phong công sở tự nhiên.",
    "part_8.csv-2": "Cấu trúc 'V-たところで' (dù có làm V đi chăng nữa thì cũng vô ích). Trạng từ '今ごろ' (giờ này) đi kèm bổ nghĩa cho cụm danh từ tân ngữ 'プロジェクトの変更を' (việc thay đổi dự án) rồi kết hợp với động từ thể quá khứ + đuôi liên kết giả định '提案したところで' (dù có đề xuất). Phần đuôi đưa ra phán đoán phủ định 'もう承認は下りないでしょう' (có lẽ cũng không được phê duyệt nữa đâu).",
    "part_10.csv-3": "'おきに' mang ý nghĩa cứ cách... (một khoảng thời gian/không gian). Câu diễn tiến tự nhiên với trạng ngữ chỉ không gian 'この広いオフィスには', nối tiếp danh từ chỉ số lượng + おきに '3列おきに' và khép lại bằng cụm chủ vị bổ nghĩa cho đối tượng '高性能な空気清浄機が設置されている'.",
    "part_10.csv-4": "'おそらく' (có lẽ/có thể) là phó từ thường đi kèm với các từ phỏng đoán như 'だろう' ở cuối câu. 'サーバーの' bổ nghĩa cho danh từ '過負荷' (quá tải). Cụm 'おそらく' được đặt trước thành phần phỏng đoán 'サーバーの過負荷' và kết thúc bằng 'だろう'.",
    "part_10.csv-5": "'同じ' thể hiện sự giống nhau. '提出したもの' (cái đã nộp) đi với trợ từ 'と' để làm mốc so sánh. Cụm '前回弊社が' đóng vai trò định ngữ bổ nghĩa cho '提出したもの'. Câu kết nối nhịp nhàng: chủ ngữ đi liền với cụm định ngữ và từ so sánh kèm 同じです.",
    "part_10.csv-7": "'と思います' thể hiện suy nghĩ, phán đoán của người nói. Trợ từ 'と' đi sau mệnh đề phán đoán '先方の担当者も納得してくれる'. '先方の' bổ nghĩa cho danh từ '担当者も'. Vế câu được nối liền bằng cụm chủ ngữ vế sau đưa lên trước, tiếp đến là động từ và khép bằng と思います."
}

leakage_str1 = " Câu được chia thành các phần tương ứng để kiểm tra khả năng sắp xếp trật tự từ ngữ pháp trong tiếng Nhật một cách chính xác nhất."
leakage_str2 = "Câu được chia thành các phần tương ứng để kiểm tra khả năng sắp xếp trật tự từ ngữ pháp trong tiếng Nhật một cách chính xác nhất."

files = ['part_6.csv', 'part_7.csv', 'part_8.csv', 'part_9.csv', 'part_10.csv']

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
        
        # 1. Global replace for leakage in part_10
        if len(row) > exp_idx:
            orig_exp = row[exp_idx]
            new_exp = orig_exp.replace(leakage_str1, "").replace(leakage_str2, "")
            if new_exp != orig_exp:
                row[exp_idx] = new_exp
                changed = True
        
        # 2. Specific fixes
        key = f"{file}-{i}"
        if key in fixes:
            new_exp = fixes[key]
            del row[exp_idx:]
            row.append(new_exp)
            changed = True
            
    if changed:
        with open(path, 'w', encoding='utf-8-sig', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(r)

print("Batch 2 of set 2 updated safely!")
