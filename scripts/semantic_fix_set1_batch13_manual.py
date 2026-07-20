import csv, os

dir_path = r'd:\pj\xx\ai-gen-quiz\mondai2_ordering\csv_filled\set_1_daily'

fixes = {
    "part_62.csv-6": "Sở hữu cách 「私の」 bổ nghĩa cho danh từ 「カバンの」. Cấu trúc vị trí 「Nのなか」 đi với trợ từ 「には」 để chỉ địa điểm tồn tại. Tính từ 「新しい」 bổ nghĩa cho danh từ 「スマホ」 làm chủ ngữ đi với trợ từ 「が」, kết thúc bằng tự động từ trạng thái 「入っています」.",
    "part_62.csv-7": "Cụm danh từ giới hạn phạm vi 「日本の料理の中で」 sử dụng cấu trúc 「Nのなかで」 kèm trợ từ 「は」 để nhấn mạnh. Tiếp theo là chủ ngữ 「私は」 và đối tượng thích 「お寿司が」. Phó từ chỉ mức độ cao nhất 「一番」 đứng trước để bổ nghĩa cho tính từ đuôi na 「好きです」.",
    "part_63.csv-13": "「なぜかといえば」 là cách diễn đạt lý do mang tính lập luận chặt chẽ. Phần giải thích phía sau gồm tính từ đuôi na 「高級な」 bổ nghĩa cho danh từ 「食材」 làm tân ngữ cho động từ dạng tiếp diễn 「使っている」. Cuối cùng câu được chốt bằng 「～からです」 để làm rõ nguyên nhân.",
    "part_64.csv-1": "Cụm từ cố định 「なに不自由なく」 nghĩa là 'hoàn toàn không thiếu thốn thứ gì'. Câu đi từ bối cảnh trạng ngữ chỉ nơi chốn (この街は近くに...), nối tiếp bằng bộ cụm phó từ 「なに」 + 「不自由」 + 「なく」 bổ nghĩa cho động từ chính ở dạng khả năng 「暮らせます」.",
    "part_64.csv-2": "Trình độ N5. 「何か」 đóng vai trò đại từ 'cái gì đó'. Các thành phần được sắp xếp tự nhiên: Trạng ngữ chỉ vị trí (テーブルの上に) đi liền đại từ bất định 「何か」, tiếp đến tính từ 「美味しい」 bổ nghĩa trực tiếp cho danh từ 「お菓子」 và khép lại bằng trợ từ 「が」 đi kèm động từ tồn tại 「あります」.",
    "part_64.csv-3": "Trình độ N4. 「何か」 đóng vai trò phó từ chỉ trạng thái 'có gì đó/hơi hơi'. Chủ ngữ (今日の彼女の服は) đứng đầu câu, theo sau là phó từ 「何か」 kết hợp cụm so sánh 「いつもと」 cùng thể Te 「違って」 (khác với mọi khi), cuối cùng phó từ chỉ mức độ 「とても」 bổ nghĩa cho tính từ 「おしゃれだ」.",
    "part_64.csv-4": "Cấu trúc 「Nか何か」 nghĩa là 'N hoặc thứ gì đó tương tự'. Vế sau diễn tiến tự nhiên: Tính từ bổ nghĩa danh từ (冷たい) đi kèm danh từ 「ジュース」, trợ từ lựa chọn 「か」 và 「何か」, sau cùng là động từ bỏ masu 「飲み」 kết hợp cấu trúc chỉ mục đích ra ngoài làm gì.",
    "part_64.csv-5": "Cấu trúc 「Nや何か」 dùng để liệt kê không triệt để 'game hay những thứ đại loại thế'. Thành phần chỉ thời gian và đối tượng (日曜日は友達と) dẫn đầu, nối tiếp bằng danh từ 「ゲーム」 đi với trợ từ liệt kê 「や」 và 「何かを」. Động từ hành động thể Te 「して」 đi kèm vế kết thúc câu biểu thị thói quen thường làm.",
    "part_64.csv-6": "Cấu trúc 「それならなにか」 dùng để hạch sách đối phương trong giao tiếp đời sống 'Nếu thế thì ý cậu là gì?'. Câu dẫn dắt bằng từ nối 「それなら」, từ hỏi chất vấn 「なにか」, tiếp đó là vế làm rõ nội dung tranh cãi '私が嘘をついていると' (đang nói dối) và kết thúc bằng mẫu nghi vấn ngữ khí mạnh 「〜とでも言いたいのか」.",
    "part_64.csv-7": "「なにかしら」 mang nghĩa 'một cái gì đó (không rõ cụ thể)'. Câu mở đầu bằng chủ từ và thời gian (母は毎日), theo sau là phó từ 「なにかしら」, cụm danh từ định ngữ 「料理の」 bổ nghĩa cho 「新しいレシピを」 và cuối cùng là động từ hành động thể hiện trạng thái duy trì 「試している」.",
    "part_64.csv-8": "「なにかと」 mang nghĩa 'chuyện này chuyện kia/nhiều thứ'. Câu bắt đầu với trạng ngữ thời gian bối cảnh (引っ越しの直後は), phó từ 「なにかと」 nối tiếp chủ ngữ của vế tính từ '買うものが', tính từ thể Te chỉ nguyên nhân 「多くて」 và dẫn đến cụm động từ kết quả 「お金がかかる」.",
    "part_64.csv-9": "Cấu trúc 「なにかというと」 nghĩa là 'hễ có chuyện gì là lại.../hở một tí là...'. Chủ ngữ (夫は) đứng trước cụm từ ngữ pháp 'なにかというと', tiếp đến là phó từ và tân ngữ 'すぐにスマホを', cuối cùng là động từ thể Te 「触って」 đi kèm cấu trúc chỉ tần suất tiêu cực 「ばかりいる」.",
    "part_64.csv-10": "「なにがなんでも」 biểu thị quyết tâm cực kỳ mạnh mẽ 'bằng mọi giá/dù thế nào đi nữa'. Bối cảnh thời gian địa điểm (今週末のバーゲンセールでは) đứng trước cụm trạng từ quyết tâm 'なにがなんでも', sau đó là tân ngữ tác động 「あの靴を」 và động từ bỏ masu 「買い」 kết hợp đuôi mong muốn 「たい」.",
    "part_64.csv-11": "Trình độ N1. 「なにがなんでも」 kết hợp tính từ mang nghĩa tiêu cực để biểu thị sự phê phán 'dù thế nào đi nữa cũng quá vô lý/quá mức'. Vế giả định bối cảnh mang tính trách móc đi liền với cụm từ nhấn mạnh phê phán 'なにがなんでも', nối tiếp bằng tính từ trạng thái tiêu cực 「不親切」 và vĩ tố chỉ sự quá đà 「すぎる」.",
    "part_64.csv-12": "Cấu trúc 「なにかにつけて」 nghĩa là 'mỗi khi có dịp/hễ gặp chuyện gì cũng...'. Chủ ngữ (両親は) đứng đầu câu, tiếp đến là cấu trúc ngữ pháp 'なにかにつけて', nội dung thúc giục đóng vai trò gián tiếp '私に早く結婚しろと' và khép lại bằng động từ hành động hướng về phía người nói 「言ってくる」.",
    "part_64.csv-13": "「なにげない」 là tính từ bổ nghĩa cho danh từ mang nghĩa 'vô tình/bâng quơ/không cố ý'. Sở hữu cách (友達の) và tính từ định ngữ 「なにげない」 bổ nghĩa cho danh từ 「一言に」. Phía sau là chủ ngữ và phó từ mức độ '私はとても', đi cùng động từ thể bị động tính từ hóa 「救われた」 bổ nghĩa cho danh từ tâm trạng 「気持ちになった」.",
    "part_64.csv-14": "「なにしろ」 dùng để đưa ra lý do cốt lõi mang tính nhấn mạnh 'vì dù sao đi nữa/bởi vì...'. Chủ đề câu (最近の夏は) đi kèm phó từ nhấn mạnh lý do 「なにしろ」, tính từ nêu nguyên nhân 「暑い」 kết hợp liên từ 「から」. Vế sau gồm đối tượng tác động 「エアコンを」, cấu trúc duy trì trạng thái bỏ mặc 「つけっぱなしに」 và động từ duy trì 「している」.",
    "part_64.csv-15": "Cấu trúc 「なににもまして」 mang ý nghĩa 'hơn bất cứ điều gì/trên hết'. Thành phần nêu quan điểm bối cảnh (私にとって...) đứng đầu, theo sau là cụm từ cấu trúc so sánh bậc nhất 'なににもまして', và khép lại bằng tính từ bổ nghĩa danh từ kết thúc câu '幸せなひとときだ'.",
    "part_64.csv-16": "Cấu trúc phủ định hoàn toàn 「なにも～ない」 ở trình độ N4 nghĩa là 'không... một cái gì'. Từ nguyên nhân bối cảnh thời gian (お腹がいっぱいなので、今は), câu tiếp diễn với đại từ phủ định chia nhỏ 「なに」 cùng trợ từ nhấn mạnh 「も」, động từ bỏ masu biểu thị ý muốn 「食べ」 đi với đuôi phủ định ý muốn 「たく」 và thành phần kết thúc lịch sự 「ないです」.",
    "part_64.csv-17": "Trình độ N2, 「なにも～ない」 mang sắc thái phản bác hoặc khuyên nhủ 'làm gì mà phải.../đâu cần thiết phải...'. Từ nguyên nhân sự việc (そんな小さなミスで), phó từ biểu thị thái độ phản bác 「なにも」 đi liền cụm chỉ mức độ cực đoan 「そこまで」. Vế sau là cụm danh từ hành động 「怒ることは」 cùng phủ định kết thúc 「ない」 và phán đoán giảm nhẹ 「でしょう」.",
    "part_64.csv-18": "Cấu trúc phủ định một phần 「なにも～わけではない」 nghĩa là 'không phải là... (như bạn nghĩ đâu)'. Đối tượng được nói đến (あなたの料理が) đứng trước từ giảm nhẹ mang tính phân trần 「なにも」. Tiếp theo là tính từ đuôi na định ngữ 「嫌いな」 và cấu trúc phủ định giải thích 'わけではないが' để mở ra vế đối lập phía sau.",
    "part_64.csv-19": "Cấu trúc 「Nもなにも」 dùng để khái quát hóa 'N và tất cả mọi thứ khác đều...'. Từ nguyên nhân khách quan dẫn dắt vế trước, câu tiếp nối bằng danh từ đại diện 「服」 cùng trợ từ 「も」 và từ khái quát 「なにも」. Vế kết thúc gồm phó từ chỉ mức độ toàn bộ 「全部」 và động từ trạng thái kết quả tiêu cực 「汚れてしまった」.",
    "part_64.csv-20": "Cấu trúc 「Vもなにも」 dùng trong hội thoại đời sống để phủ định hoặc gạt phăng ý kiến của đối phương 'làm gì có chuyện V/V gì mà V'. Sau lời dẫn hội thoại, động từ lặp lại nguyên thể từ câu hỏi 「抜く」 kết hợp trợ từ 「も」 và cụm từ gạt bỏ 「なにも、」. Vế cuối là lý do thực tế mang tính nhân quả 'お腹が空いて' và hệ quả phủ định khả năng 「眠れないよ」。"
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

print("Batch 13 updated safely!")
