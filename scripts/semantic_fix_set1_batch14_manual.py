import csv, os

dir_path = r'd:\pj\xx\ai-gen-quiz\mondai2_ordering\csv_filled\set_1_daily'

fixes = {
    "part_66.csv-2": "Biểu thức điều kiện '～ならば' nối sau tính từ đuôi i '良い' để giả định tình huống 'nếu thời tiết tốt'. Vế sau diễn tiến mạch lạc với thành phần chỉ đối tượng '家族で', địa điểm '公園へ' và kết thúc bằng hành động đề xuất 'ピクニックに行きましょう'.",
    "part_66.csv-9": "Cấu trúc 'V-たなり' nghĩa là giữ nguyên trạng thái sau khi thực hiện hành động. Động từ '着る' chia quá quá khứ '着た' đi với 'なり' tạo thành cụm 'cứ mặc nguyên bộ vest'. Phần tiếp theo nối liền tự nhiên với trạng ngữ nơi chốn 'ベッドで', hành động '横になって' và kết quả '寝てしまった'.",
    "part_66.csv-16": "Cấu trúc '言うなりに' nghĩa là 'nghe theo/tuân theo hoàn toàn những gì ai đó nói'. Cụm danh từ sở hữu '主人の' đi trước cụm từ '言うなりになって' tạo thành nghĩa 'hoàn toàn nghe theo lời chủ nhân'. Tiếp nối mạch lạc ở vế sau là phó từ '静かに' và cấu trúc chỉ khả năng '待つことができる'.",
    "part_67.csv-1": "Đầu tiên, danh từ お茶 kết hợp với cấu trúc なりとも để đưa ra một gợi ý tiêu biểu (trà hay thứ gì đó tương tự). Tiếp theo, động từ kính ngữ 召し上がり đi với đuôi liên kết ながら để diễn tả hành động vừa dùng nước vừa trò chuyện. Các thành phần được sắp xếp tự nhiên từ danh từ đi với cấu trúc chọn lựa, đến động từ chính và trợ từ liên kết hành động đồng thời.",
    "part_69.csv-3": "Cụm 'なんということもなく' mang ý nghĩa 'không có chuyện gì đặc biệt/chẳng có gì đáng nói'. Ở đây, nó đóng vai trò trạng ngữ chỉ trạng thái cho hành động '一日中家でテレビを見て過ごした' ở vế sau.",
    "part_69.csv-7": "Cụm 'なんとか言ってやって' mang nghĩa 'hãy nói điều gì đó đi (để nhắc nhở)'. Mạch câu tiếp diễn từ đối tượng thực hiện hành động '父から' đến động từ hành vi và khép lại bằng cấu trúc cầu khiến 'ほしい'.",
    "part_69.csv-10": "Cấu trúc '～とかなんとか言って' dùng để trích dẫn lý do một cách mơ hồ hoặc mỉa mai. Các thành phần kết nối tự nhiên từ chủ ngữ nhỏ '仕事が' đến tính từ '忙しいとか', từ nối 'なんとか' và động từ trích dẫn '言って'.",
    "part_69.csv-18": "Cấu trúc 'A-くも何ともない' dùng để phủ định hoàn toàn tính chất của tính từ đuôi i (không hề... một chút nào). Câu dẫn dắt từ cụm đối tượng '私にとっては' đến phần phủ định tính từ gốc '辛くも' và kết thúc bằng '何ともない'.",
    "part_69.csv-19": "'なんにしても' mang nghĩa dù sao đi nữa. Nó đứng đầu vế để định hướng cho lời khuyên, theo sau là các cụm từ diễn tiến mạch lạc: danh từ sở hữu '旅行の', chủ ngữ hành động '準備は早めに' và cấu trúc khuyên bảo '始めたほうが'.",
    "part_70.csv-8": "Cấu trúc 'Nにあっても' tương đương với '～という特別な状況でも', mang nghĩa 'ngay cả trong hoàn cảnh N'. Các thành phần được sắp xếp từ chủ ngữ '母は', cụm trạng huống 'どんなに忙しい朝にあっても', tiếp theo là tân ngữ '笑顔を' đi liền với động từ phủ định ở đuôi câu '絶やさない'.",
    "part_70.csv-9": "Cấu trúc 'Nにあっては' dùng để nhấn mạnh một hoàn cảnh thời gian/không gian đặc thù (thời kỳ nắng nóng gay gắt '猛暑の時期'). Câu đi từ việc xác định bối cảnh thời gian cụ thể sang chủ đề được nhấn mạnh 'エアコンをつけるのは' và kết thúc bằng phán đoán mang tính phóng đại trong đời sống '死活問題だ'.",
    "part_70.csv-10": "Cấu trúc 'Nにあっては' đi sau một đối tượng người đặc biệt để chỉ ra rằng 'đối với người đó thì sẽ có năng lực xuất chúng'. Dòng diễn đạt bắt đầu bằng việc định danh người có năng lực 'うちの母にあっては', theo sau là điều kiện giả định 'どんなに安い食材でも' và kết thúc bằng hành động biến đổi bất ngờ.",
    "part_70.csv-13": "Cấu trúc '～に至って' chỉ một giai đoạn hoặc thời điểm cụ thể khi sự việc diễn tiến đến mức đó thì một hành động khác mới xảy ra. Các vế câu nối tiếp từ việc di chuyển tới vị trí quầy thu ngân 'レジの前に至って', đến từ chỉ mốc thời gian '初めて' kết hợp bổ ngữ cho động từ nhận thức '気づいた'.",
    "part_70.csv-16": "Cấu trúc 'Nにいわせれば' thể hiện góc nhìn, quan điểm cá nhân mang tính chủ quan của một người. Câu dẫn nguồn ý kiến 'うちの母に言わせれば', xác định đối tượng bị đánh giá 'ダメージジーンズは', nội dung đánh giá và khép lại bằng hình thức truyền ngôn 'そうだ'.",
    "part_70.csv-17": "Cấu trúc 'Nにおいて' dùng để chỉ địa điểm xảy ra sự kiện (thay cho 'で' trong văn viết hoặc thông báo trang trọng). Vế câu mở đầu bằng chủ ngữ sự kiện 'タイムセールは', tiếp đến là cụm danh từ chỉ nơi chốn kết hợp ngữ pháp '特設会場において' và đi liền với động từ bị động '行われます'.",
    "part_70.csv-18": "Cấu trúc 'Nにおいて' ở đây xác định phạm vi, lĩnh vực (về mặt/xét về). Cụm giới hạn lĩnh vực '手際の良さにおいて' đứng trước để làm nền tảng, vế sau là cấu trúc thành ngữ so sánh bậc nhất '姉の右に出る者はいない' (không ai vượt qua được chị) nhằm hoàn thiện ý nghĩa phán đoán."
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

print("Batch 14 updated safely!")
