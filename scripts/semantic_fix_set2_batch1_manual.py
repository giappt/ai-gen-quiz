import csv, os

dir_path = r'd:\pj\xx\ai-gen-quiz\mondai2_ordering\csv_filled\set_2_business'

fixes = {
    "part_1.csv-1": "Cấu trúc chỉ không gian 'N1 と N2 のあいだ' (ở giữa N1 và N2). Ở đây N1 là '田中さんの机' và N2 là '鈴木さんの机'. Danh từ sở hữu '鈴木さんの' bổ nghĩa cho danh từ chỉ vật '机', kết hợp với trợ từ 'の' và danh từ không gian '間に' để xác định vị trí. Danh từ chỉ vật 'パソコン' đi với trợ từ chỉ tân ngữ 'を' bổ nghĩa cho hành động '置きます' ở cuối câu.",
    "part_1.csv-20": "Cấu trúc biểu thị vị trí không gian đi sau ai đó 'Nのあと'. Ở đây, bối cảnh câu mở đầu bằng vế chỉ điều kiện thời gian '工場を見学するときは'. Danh từ chỉ người hướng dẫn '案内係の' đi liền với từ chỉ người '人の' và kết hợp với cấu trúc vị trí 'あとに' (sau...). Tiếp theo là động từ liên kết thể Te 'ついていって' đi cùng cấu trúc yêu cầu lịch sự 'ください' ở cuối câu.",
    "part_2.csv-1": "Cấu trúc 'Nのあと' (Sau khi N) dùng để diễn tả hành động xảy ra sau một sự kiện. Danh từ '会議' (cuộc họp) đi với 'のあとに' tạo thành trạng ngữ chỉ thời gian. '大切なメールを' là cụm tân ngữ được bổ nghĩa bởi tính từ '大切な' (quan trọng). Trạng từ 'まとめて' (gộp lại/cùng lúc) bổ nghĩa cho động từ chính 'チェックします' (kiểm tra) ở phần cuối câu.",
    "part_2.csv-2": "Cấu trúc 'V-たあとで' biểu thị một hành động xảy ra sau khi một hành động khác đã hoàn thành. Động từ '送る' (gửi) chia sang thể quá khứ là '送った' kết hợp với 'あとで' thành '送ったあとで' (sau khi gửi). 'メールを' là tân ngữ của '送った'. '確認の' (xác nhận) là danh từ bổ nghĩa cho danh từ '電話' ở phần cuối câu.",
    "part_2.csv-3": "Cấu trúc 'V-たあとから' diễn tả một trạng thái hoặc hành động liên tục xảy ra ngay sau khi một hành động khác hoàn thành. Động từ '導入する' (áp dụng/đưa vào sử dụng) chia thể quá khứ '導入した' đi với 'あとから' thành '導入したあとから' (kể từ sau khi đưa vào sử dụng). '新しいシステムを' là tân ngữ của '導入した'. Định từ '多くの' (nhiều) bổ nghĩa cho danh từ '問い合わせ' (thắc mắc/yêu cầu) ở phần cuối câu.",
    "part_2.csv-4": "Từ 'あと' đứng đầu câu đóng vai trò như một liên từ bổ sung thông tin ('Ngoài ra', 'Thêm nữa'). Cụm từ 'この件について' nghĩa là 'về vụ việc này/vấn đề này' bổ nghĩa cho bối cảnh câu hỏi. '何か' (cái gì đó/nào đó) bổ nghĩa cho 'ご質問' (câu hỏi - kính ngữ). Câu hoàn chỉnh kết nối mượt mà từ liên từ, trạng ngữ chỉ đối tượng, đại từ cho đến cụm chủ vị nghi vấn.",
    "part_2.csv-5": "Cấu trúc 'あと + 数量詞' biểu thị số lượng còn lại cần thiết để hoàn thành một việc gì đó ('còn... nữa'). Ở đây, 'あと' kết hợp với lượng từ '2ページ' (2 trang) và trợ từ 'で' chỉ giới hạn thời gian/số lượng để thành 'あと2ページで' (chỉ còn 2 trang nữa là...). 'チェックは' (việc kiểm tra) làm chủ ngữ chính của câu, được bổ nghĩa bởi cụm từ sở hữu 'この資料の'. Trạng từ '全部' (toàn bộ) bổ nghĩa cho động từ '終わります' (kết thúc).",
    "part_2.csv-6": "Trạng từ 'あとから' nghĩa là 'sau đó/sau này', biểu thị một hành động xảy ra muộn hơn một thời điểm chuẩn. Trong bối cảnh kinh doanh, 'スケジュールを' là tân ngữ của hành động '変更する' (thay đổi). Cụm '変更することは' biến động từ thành danh từ làm chủ đề ('việc thay đổi...'). Cụm '原則として' (về nguyên tắc) đóng vai trò bổ nghĩa cho điều kiện phủ định ở cuối câu.",
    "part_2.csv-7": "'あとで' là trạng từ chỉ thời gian, mang nghĩa là 'lát nữa/sau đó'. '資料は' (tài liệu) được định ngữ bởi '会議の' đóng vai trò là chủ đề câu. Cụm 'メールに' đi với động từ thể て là '添付して' (đính kèm vào email) tạo thành phương thức thực hiện hành động. Hành động chính là '送信いたします' (tôi xin phép gửi - khiêm nhường ngữ của 送信する) nằm ở cuối câu.",
    "part_2.csv-8": "Cấu trúc 'あとは～だけ' diễn tả ý nghĩa 'chỉ còn lại... là xong/là đủ'. Ở đây, '作成は終わったので' (Vì việc lập/viết đã xong) đưa ra lý do ở đầu câu, được bổ nghĩa bởi '企画書の'. Tiếp theo, 'あとは' đóng vai trò chuyển ý sang phần việc còn lại. '部長の' (của Trưởng phòng) bổ nghĩa cho danh từ '承認' (phê duyệt), và '承認を' đóng vai trò tân ngữ cho hành động '得る' (nhận được) kết hợp với 'だけです'.",
    "part_2.csv-9": "Trạng từ 'あまり' đi với động từ hoặc tính từ thể phủ định ở phía sau để diễn tả ý nghĩa 'không... lắm'. Trong câu này, '打ち合わせは' (cuộc họp/trao đổi) là chủ đề câu, bổ nghĩa bởi '本日の' (hôm nay). 'あまり' bổ nghĩa phủ định cho cụm '時間がかからない' (không tốn thời gian). Cụm từ 'かからない予定です' có nghĩa là 'dự kiến là không tốn...'.",
    "part_2.csv-10": "'あまりにも' là trạng từ chỉ mức độ cực kỳ cao ('quá mức / quá chừng'), thường đi trước tính từ hoặc động từ để nhấn mạnh sự thái quá. Ở đây, nó bổ nghĩa cho tính từ '厳しい' (nghiêm ngặt/gắt gao). '厳しいため' (vì gắt gao) thể hiện nguyên nhân. '多少の' (một chút/phần nào) bổ nghĩa cho danh từ '変更' (thay đổi) ở cuối câu.",
    "part_2.csv-11": "Cấu trúc 'あまりの N に/で' dùng để diễn tả một trạng thái cảm xúc hoặc tình huống vượt quá mức bình thường, dẫn đến một kết quả tiêu cực. Danh từ ở đây là '忙しさ' (sự bận rộn). '業務の' (của công việc) bổ nghĩa cho mức độ bận rộn đó. Cụm 'あまりの忙しさに' tạo thành trạng ngữ chỉ nguyên nhân. '大切な' (quan trọng) là tính từ bổ nghĩa cho danh từ '連絡' (liên lạc) ở cuối câu.",
    "part_2.csv-12": "Cấu trúc 'あまりにも～と' kết hợp trạng từ chỉ mức độ thái quá 'あまりにも' với điều kiện 'と' (Nếu... thì dẫn đến kết quả tất yếu). '顧客からのメールへの' bổ nghĩa cho '返信' (sự phản hồi). '返信が' là chủ ngữ của mệnh đề phụ. '遅い' (chậm) là tính từ kết hợp với 'と' thành '遅いと'.",
    "part_2.csv-13": "Cấu trúc 'V-る + あまり（に）' diễn tả nguyên nhân do một hành động quá mức dẫn đến một kết quả không tốt (thường là ngoài ý muốn). Ở đây, '成果を' (thành quả) là tân ngữ của động từ '急ぐ' (vội vã/gấp rút), cả cụm được giới hạn bởi định ngữ 'プロジェクトの'. Động từ thể từ điển '急ぐ' kết hợp trực tiếp với 'あまりに' thành '急ぐあまりに' (vì quá nóng vội muốn có thành quả). Cụm 'データの' bổ nghĩa cho danh từ '確認'.",
    "part_2.csv-14": "Cấu trúc '数量詞 + あまり' mang nghĩa là 'hơn... một chút' hoặc 'trên... (về số lượng)'. Ở câu này, lượng từ là '50社' (50 công ty). Khi kết hợp với 'あまり' và bổ nghĩa cho danh từ '企業' (doanh nghiệp), ta thêm trợ từ 'の' thành '50社あまりの' (hơn 50 doanh nghiệp). Cụm '新商品発表会には' đóng vai trò trạng ngữ chỉ sự kiện, '取引先から' (từ phía đối tác) chỉ nguồn gốc.",
    "part_2.csv-15": "Cấu trúc 'V-あらためる' (Động từ bỏ ます + あらためる) dùng để biểu thị việc thực hiện lại hành động đó một lần nữa nhằm mục đích sửa đổi, cải tiến cho tốt hơn. Ở đây, động từ '書き改める' (viết lại/sửa đổi văn bản) được sử dụng. '指摘されたので' (vì được chỉ ra/góp ý) đưa ra nguyên nhân. '報告書の' bổ nghĩa cho tân ngữ '構成を' (cấu trúc của bản báo cáo). Trạng từ '一から' (từ đầu) bổ nghĩa cho hành động viết lại.",
    "part_2.csv-16": "Liên từ 'あるいは' dùng để nối hai danh từ thể hiện mối quan hệ lựa chọn 'hoặc là...'. Ở đây, lựa chọn giữa hai mốc thời gian là '来週の月曜日' (Thứ Hai tuần tới) và '火曜日' (Thứ Ba). Trợ từ 'に' gắn vào danh từ thời gian cuối cùng trước khi đi vào động từ kính ngữ 'お願いいたします' ở cuối câu.",
    "part_2.csv-17": "Cấu trúc '~か、あるいは' dùng để nối hai phương án hành động lựa chọn mang tính song song ('hoặc là... hoặc là...'). Hành động thứ nhất là 'メールで送る' kết hợp với 'か' tạo thành mệnh đề lựa chọn đầu tiên. Liên từ 'あるいは' đứng giữa để mở ra phương án thứ hai. Phương án thứ hai bắt đầu bằng cụm trạng ngữ 'USBに入れて' (cho vào USB) và kết thúc bằng hành động chính '直接渡してください'.",
    "part_2.csv-18": "Trạng từ 'あるいは' khi đi kèm với cấu trúc phỏng đoán ở cuối câu như 'かもしれない' sẽ tăng cường ý nghĩa phỏng đoán ('có lẽ là/chưa biết chừng là...'). Ở đây, '進捗状況では' (với tình hình tiến độ hiện tại) đưa ra căn cứ. 'あるいは' đứng trước mệnh đề phỏng đoán để định hướng thái độ. Cụm '納期に間に合わない' (không kịp hạn giao hàng) là nội dung bị phỏng đoán, kết hợp với 'かもしれません'.",
    "part_2.csv-19": "Cấu trúc 'あるいは～、あるいは～' được dùng trong văn viết trang trọng nhằm liệt kê các phương án, hành động hoặc trạng thái diễn ra song song hoặc tương phản nhau ('hoặc là... hoặc là...'). Ở đây, hai hành động của các doanh nghiệp vừa và nhỏ ('中小企業は') được liệt kê: 'あるいは規模を縮小し' (hoặc là thu nhỏ quy mô) và 'あるいは他社と合併し' (hoặc là sáp nhập với công ty khác). Cuối cùng, cụm tân ngữ '生き残りを' đi với động từ '図っている' (nỗ lực để sống sót).",
    "part_2.csv-20": "Cấu trúc 'N1にあるまじきN2' là một biểu hiện mang tính phê phán gay gắt, nghĩa là 'Hành vi N2 là điều hoàn toàn không được phép có ở một người có thân phận/vị trí là N1'. Ở đây, N1 là 'ビジネスパーソン' (người làm kinh doanh) và N2 là '行為' (hành vi). '機密情報を' là tân ngữ bổ nghĩa bởi '顧客の', đi với hành động '他社に漏洩するなど' (như là rò rỉ cho công ty khác). Các thành phần kết nối mạch lạc tạo thành ý phê phán mạnh mẽ.",
    "part_3.csv-1": "'あれで' thể hiện sự đánh giá trái ngược với vế trước (nghiêm khắc). '部下思いの' (biết nghĩ cho cấp dưới) và '良い' lần lượt là các tính từ bổ nghĩa cho danh từ '上司'.",
    "part_5.csv-2": "Cấu trúc 'Nいかんだ' mang ý nghĩa phụ thuộc vào danh từ N hoặc kết quả ra sao là tùy thuộc vào N. Trong câu này, danh từ trung tâm là '実績', được bổ nghĩa bởi cụm danh từ liên kết phía trước là '今期の' và '売上'. Mạch câu đi từ thành phần bổ ngữ đến danh từ chính rồi kết hợp đuôi khẳng định 'だ'.",
    "part_5.csv-5": "Từ nghi vấn 'いくら' kết hợp với trợ từ 'か' tạo thành mệnh đề nghi vấn lồng trong câu mang nghĩa bất định (cần bao nhiêu đi chăng nữa). Mệnh đề này bắt đầu bằng chủ ngữ '予算が', theo sau là từ hỏi 'いくら', tính từ bổ nghĩa '必要' và trợ từ nghi vấn kết thúc 'か'.",
    "part_5.csv-9": "Cấu trúc 'いくら～といっても' dùng để biểu thị ý nghĩa dù có nói là... đi chăng nữa. Ở giữa là mệnh đề danh từ kết thúc bằng thể thông thường '急ぎの案件だ'. Câu bắt đầu bằng từ nhấn mạnh giả định 'いくら', tiếp đến cụm tính từ định ngữ '急ぎの', danh từ kết hợp đuôi khẳng định '案件だ' và chốt bằng đuôi trích dẫn liên kết 'と言っても'.",
    "part_5.csv-10": "Cấu trúc 'いくら～からといって' mang nghĩa cho dù lý do là... đi chăng nữa (cũng không được làm vế sau). Giữa cấu trúc là mệnh đề chỉ nguyên nhân kết thúc bằng tính từ '忙しい'. Mạch câu đi từ từ mở đầu 'いくら', nối tiếp chủ ngữ mệnh đề phụ '業務が', tính từ '忙しい' và khép lại bằng đuôi liên kết giả định lý do 'からといって'.",
    "part_5.csv-11": "Tương tự như cấu trúc trước, 'いくら～からといっても' được thêm trợ từ 'も' ở cuối để tăng cường tính nhấn mạnh đối lập (cho dù nói là vì... đi chăng nữa thì vẫn không). Vế câu bắt đầu bằng từ mở đầu 'いくら', liền kề chủ ngữ của mệnh đề phụ '予算が', tính từ phủ định '足りない' và đuôi liên kết 'からといっても'.",
    "part_5.csv-12": "Cụm từ 'いくらなんでも' là một thành ngữ mang nghĩa dù thế nào đi nữa, quá mức chịu đựng, dùng để bổ nghĩa cho tính từ chỉ mức độ tiêu cực ở phía sau. Câu bắt đầu bằng từ định ngữ '提示された', danh từ chủ ngữ '納期は', nối tiếp cụm trạng từ 'いくらなんでも'.",
    "part_5.csv-13": "Cấu trúc điều kiện ngược 'いくら～たところで' mang ý nghĩa dù cho có thử làm V đi chăng nữa thì kết quả cũng vô ích. Động từ '交渉する' chia sang thể quá quá khứ là '交渉した' kết hợp với 'ところで'. Mạch câu đi từ phó từ mở đầu 'いくら', trạng ngữ phương thức '対面で', danh từ hành động '交渉' và khép bằng đuôi giả định kết nối 'したところで'.",
    "part_5.csv-14": "Cấu trúc bắt buộc '～なくてはいけない' biểu thị nghĩa phải làm gì đó. Động từ hành động '押す' (đóng dấu) chia sang thể phủ định biến đổi thành dạng liên kết '押さ' trước khi đi với đuôi ngữ pháp. Các bổ ngữ nối tiếp nhau: bổ ngữ nơi chốn '契約書に', tân ngữ '社印を', gốc động từ '押さ' và kết thúc bằng đuôi bắt buộc 'なくてはいけない'.",
    "part_5.csv-15": "Cấu trúc danh từ thời gian 'N ＋ 以後' mang ý nghĩa kể từ sau khi sự việc N diễn ra. Ở đây danh từ phức hợp chỉ sự kiện là '新システム導入'. Câu kết nối nhịp nhàng: danh từ bổ nghĩa hệ thống '新システム', danh từ hành động triển khai '導入', hậu tố thời gian '以後' và chủ ngữ của vế kết quả phía sau '業務の効率が'.",
    "part_5.csv-19": "Cấu trúc 'Nはいざしらず' mang ý nghĩa danh từ N thì không bàn tới hoặc không nói làm gì nhưng vế sau thì khác. Danh từ N ở đây là '状況' (tình hình). Tiếp theo là cấu trúc chỉ phạm vi bối cảnh hành động '我が社に' đi liền với 'おいては' (đối với công ty chúng tôi). Cấu trúc kết nối gọn gàng: '状況は' 'いざしらず' '我が社に' 'おいては'.",
    "part_5.csv-20": "Cấu trúc '数量詞＋以上' chỉ mức độ từ giới hạn số lượng đó trở lên. Danh từ chỉ số lượng người '5人' kết hợp trực tiếp với từ chỉ hạn định mức độ '以上'. Sau đó sử dụng trợ từ định ngữ 'の' để tạo mối liên kết bổ nghĩa cho danh từ chỉ đối tượng '参加者' ở vế sau."
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

print("Batch 1 of set 2 updated safely!")
