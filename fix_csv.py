import csv

def fix_csv(filename, line_idx_map):
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    for idx, new_line in line_idx_map.items():
        if idx < len(lines):
            lines[idx] = new_line + '\n'
            
    with open(filename, 'w', encoding='utf-8') as f:
        f.writelines(lines)

# Fix part_97.csv
# Line 10 (index 9)
fix_csv('mondai2_ordering/csv_filled/set_1_daily/part_97.csv', {
    9: 'もちろん,Nはもちろん,N3,①彼は、英語はもちろん、ドイツ語も中国語もできる。,私は、リンゴはもちろん、バナナも大好きです。,私は、,リンゴは,もちろん、,バナナも,大好き,です。,"Cấu trúc 「N1はもちろんN2も」 nghĩa là \'N1 là đương nhiên, N2 cũng...\'. Thứ tự: Danh từ 1 kèm trợ từ 「リンゴは」 + phó từ 「もちろん、」 + Danh từ 2 kèm trợ từ も 「バナナも」 + tính từ trạng thái 「大好き」 + đuôi câu khẳng định 「です」。"'
})

# Fix part_31.csv
# Line 18 (index 17)
# Line 20 (index 19)
# Line 21 (index 20)
fix_csv('mondai2_ordering/csv_filled/set_1_daily/part_31.csv', {
    17: 'だから,丁寧な形に「ですから」がある。だから＜帰結＞,N5,①踏切で事故があった。だから、学校に遅刻してしまった。,朝寝坊した。だから、約束の電車に乗り遅れた。,朝寝坊した。,だから、,約束の,電車に,乗り,遅れた。,Liên từ \'だから\' đặt ở đầu câu thứ hai đóng vai trò nối kết biểu thị kết quả tất yếu xảy ra.',
    19: 'だから,だから＜質問＞,N3,①A：みんなお前のためにこんなに遅くまで働いているんだ。B：だから、どうだって言うの。,A「私が全部やったのよ」B「だから、私にどうしろって言うの？」,A「私が全部やったのよ」B「,だから、,私に,どうしろ,って,言うの？」,"Người A đưa ra một sự kiện đời sống. Người B sử dụng \'だから\' ở đầu câu phản hồi với ngữ điệu hỏi ngược lại mang sắc thái vặn vẹo hoặc bất cần (Thế thì sao chứ?). Cấu trúc \'私にどうしろって言うの\' mang nghĩa \'Muốn tôi phải làm thế nào đây?\' thể hiện sự phản kháng."',
    20: 'だから,だから＜主張＞,N3,①A：ちょっと、どういうことですか。B：別に特別のことはないよ。A：だから、どういうことって聞いているんだよ。,A「もう食べられない」B「だから、残してもいいって言っているんだよ」,A「もう食べられない」B「,だから、,残しても,いい,って,言っているんだよ」,"Câu đầu tiên thể hiện sự từ chối hoặc bế tắc của đối phương. Trạng từ/Liên từ \'だから\' ở câu sau được dùng để lặp lại một ý kiến đã nói trước đó nhằm nhấn mạnh sự khẳng định hoặc mất kiên nhẫn (Đã bảo là...). Cụm ngữ pháp xin phép \'残してもいい\' đi với trợ từ trích dẫn ngắn \'って\' bổ nghĩa cho động từ \'言っているんだよ\'."'
})
