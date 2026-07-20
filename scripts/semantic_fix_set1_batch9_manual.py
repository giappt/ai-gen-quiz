import csv, os

dir_path = r'd:\pj\xx\ai-gen-quiz\mondai2_ordering\csv_filled\set_1_daily'

fixes = {
    "part_42.csv-1": "Cấu trúc 'V-てやってくれないか' dùng để nhờ vả đối phương làm việc gì đó cho người thứ ba (ở đây là đứa con trai). Vế sau được liên kết mạch lạc bắt đầu từ đối tượng tiếp nhận hành động '部屋を' đi với động từ '片付ける', cấu trúc 'ように' và kết thúc bằng cụm nhờ vả thân mật '言ってやってくれないか'.",
    "part_42.csv-3": "Cấu trúc 'V-てさしあげる' dùng khi người nói làm một việc tốt cho người bề trên hoặc người lớn tuổi với thái độ khiêm nhường. Định ngữ 'スマホの' bổ nghĩa cho danh từ '使い方を'. Hành động chính '説明して' kết hợp đuôi giả định 'さしあげたら' tạo thành vế giả thiết cho kết quả ở câu sau.",
    "part_42.csv-4": "Thành ngữ 'しかたがない' đi kèm với các từ chỉ cảm xúc hoặc trạng thái tâm lý để biểu thị mức độ cực kỳ, không kìm nén được. Vế chỉ nguyên nhân bắt đầu bằng trạng ngữ '旅行に' và động từ '行くので', kéo theo tính từ chỉ tâm trạng '楽しみで' nối liền với trạng thái 'しかたがない'.",
    "part_42.csv-6": "Mẫu 'V-てしまう' ở đây dùng để biểu thị sự hối tiếc hoặc tâm trạng lỡ làm một việc không hay. Từ hành động khởi phát '喧嘩して', câu tiếp diễn với cụm 'ひどいことを' đi kèm động từ '言って' và khép lại bằng sự hối hận 'しまった'.",
    "part_42.csv-9": "Mẫu 'A-くてたまらない' diễn tả một trạng thái sinh lý hoặc cảm xúc vô cùng mãnh liệt đến mức không chịu nổi. Tân ngữ '映画を' đi liền với nguyên nhân '見たから'. Trạng thái cơ thể '眠くて' bổ nghĩa trực tiếp cho vị ngữ 'たまらない'.",
    "part_42.csv-10": "Mẫu 'V-てちょうだい' là cách nói yêu cầu, nhờ vả nhẹ nhàng, thân mật thường dùng trong gia đình hoặc hội thoại hàng ngày của phụ nữ và trẻ em. Câu diễn tiến tự nhiên từ 'そこの', danh từ nơi chốn 'コンビニで', tân ngữ '牛乳を' đến cụm động từ hành động '買ってきて' và đuôi nhờ vả 'ちょうだい'.",
    "part_42.csv-11": "Cấu trúc phối hợp 'てっきり～と思う' dùng để diễn tả một suy đoán chắc chắn của người nói nhưng thực tế lại khác. Mệnh đề lý do '消えていたので' dẫn dắt cho phó từ đinh ninh 'てっきり今日はお休み'. Trợ từ trích dẫn 'だと' nối với cụm quá khứ '思っていました'.",
    "part_42.csv-12": "Cấu trúc 'V-てでも' thể hiện ý chí mãnh liệt, dù phải sử dụng biện pháp cực đoan hay vất vả đi chăng nữa vẫn muốn đạt được mục đích. Cụm phương thức hành động 'してでも' đứng trước đối tượng '母への誕生日プレゼントを' và động từ thể mong muốn '完成させたい'.",
    "part_42.csv-14": "Mẫu 'てならない' diễn tả một cảm xúc hay tâm trạng trào dâng một cách tự nhiên mà người nói không thể kiểm soát được. Cụm chủ ngữ '今回のアルバイトの面接の結果が' sử dụng chuỗi danh từ sở hữu nối tiếp, kết hợp với tính từ tâm trạng '心配で' và đuôi 'ならない'.",
    "part_42.csv-18": "Cấu trúc '～のでは' được dùng để đưa ra một thực tế khách quan làm tiền đề lý do, dẫn đến một đánh giá tiêu cực hoặc một khó khăn ở vế sau. Trạng ngữ cách thức '小さなことで' đi cùng cụm tiền đề '喧嘩しているのでは', kéo theo nhận định về chủ ngữ '一緒に暮らすのは' là '難しい'.",
    "part_42.csv-19": "Mẫu 'ようでは' thể hiện một giả định về một trạng thái không tốt hiện tại, nếu cứ tiếp diễn như vậy thì kết quả sẽ không ra sao (thường đi kèm 困る). Cụm bổ nghĩa '部屋を片付けた' đi liền trợ từ 'だけで'. Kế tiếp là nội dung phàn nàn '疲れたと言う', liên từ giả định 'ようでは' và hệ quả '困ります'.",
    "part_43.csv-3": "Liên từ 'では' đứng ở đầu câu của người B để đưa ra một hệ quả hợp lý dựa trên thông tin người A vừa cung cấp ('Nếu vậy thì...').",
    "part_44.csv-9": "Chuỗi hành động diễn ra theo trình tự tự nhiên: 'ダウンロードして' (tải về) rồi mới đến '使ってみたい' (muốn dùng thử). Câu kết thúc bằng 'と思っています' thể hiện dự định.",
    "part_44.csv-20": "Sử dụng cụm từ chỉ số lần '何回' đi cùng với thể lặp lại hành động '洗っても洗っても' để thể hiện nỗ lực vô vọng. Kết quả 'シミが綺麗に落ちない' là nguồn cơn của sự phiền não.",
    "part_45.csv-1": "Cấu trúc đi liền 'いくら...ても' (cho dù... bao nhiêu). 'いくら' bổ nghĩa cho '作っても'. 'レシピ通りに' (đúng như công thức) là trạng từ bổ nghĩa cho động từ '作る'. '母の味にはならない' là vế kết quả tự nhiên đi theo sau.",
    "part_45.csv-9": "'済んでしまったこと' (chuyện đã qua) là tân ngữ của '後悔しても'. '今さら' (đến bấy giờ) bổ nghĩa cho hành động hối hận. Cụm 'どうなるものでもない' khép lại ở cuối một cách tự nhiên."
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
        # replace the entire explanation columns with just one column containing new_exp
        row = r[idx]
        del row[exp_idx:]
        row.append(new_exp)
        
    with open(path, 'w', encoding='utf-8-sig', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(r)

print("Batch 9 updated safely!")
