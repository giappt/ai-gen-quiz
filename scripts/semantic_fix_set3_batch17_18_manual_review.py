import csv, os

dir_path = r'd:\pj\xx\ai-gen-quiz\mondai2_ordering\csv_filled\set_3_academic'

rewrites = {
    # part_84.csv
    "Cấu trúc 「V/A/N (thể bổ nghĩa danh từ) + 範囲で」 nghĩa là 「trong phạm vi...」. Trình tự logic của câu: Chủ đề thảo luận (今回の件は) -> chủ ngữ của mệnh đề bổ ngữ (私が) -> hành động giới hạn phạm vi (把握している範囲で) -> hành động khiêm nhường ngữ hướng tới đối phương (お答えいたします)。":
    "Cấu trúc 「V/A/N (thể bổ nghĩa danh từ) + 範囲で」 nghĩa là 「trong phạm vi...」. Logic câu bắt đầu từ chủ đề (今回の件は) và chủ ngữ phụ (私が). Tiếp đến, hành động được giới hạn trong phạm vi (把握している範囲で) làm nền tảng cho động từ khiêm nhường ngữ ở cuối câu (お答えいたします).",
    
    "Ngữ pháp N4 「反対に」 (trái ngược, ngược lại). Ở đây đóng vai trò là trạng từ bổ nghĩa cho động từ hành động. Thứ tự tự nhiên: Chủ ngữ (新人の鈴木さんは) -> cụm danh từ làm tân ngữ (配布資料の綴じる向きを) -> trạng từ chỉ cách thức (反対に) -> hành động (セットして) -> kết cục ngoài ý muốn, thể hiện sự tiếc nuối (しまった)。":
    "Ngữ pháp N4 「反対に」 (ngược lại) đóng vai trò trạng từ bổ nghĩa cho hành động. Cấu trúc câu diễn tiến từ chủ ngữ (新人の鈴木さんは) sang tân ngữ (配布資料の綴じる向きを). Trạng từ (反対に) đi kèm hành động (セットして) dẫn tới một kết cục ngoài ý muốn, mang sắc thái tiếc nuối (しまった).",
    
    "Cấu trúc 「～とは反対に」 biểu thị sự tương phản, trái ngược hoàn toàn với một sự việc/đối tượng trước đó. 「の」 được dùng để danh từ hóa mệnh đề 「値上げした」. Thứ tự tự nhiên: Đối tượng so sánh (競合他社が値上げしたの) -> liên từ chỉ sự tương phản (とは反対に) -> chủ ngữ vế sau (我が社は) -> tân ngữ (価格を) -> hành động đối lập (据え置いた)。":
    "Cấu trúc 「～とは反対に」 biểu thị sự tương phản hoàn toàn. Mệnh đề 「値上げした」 được danh từ hóa bằng 「の」. Câu bắt đầu bằng đối tượng so sánh (競合他社が値上げしたの) gắn với liên từ tương phản (とは反対に). Vế sau làm rõ sự đối lập thông qua chủ ngữ (我が社は), tân ngữ (価格を) và hành động giữ nguyên (据え置いた).",
    
    "Cấu trúc 「ひとつ間違えば」 nghĩa là 「chỉ cần một sai lầm nhỏ/sơ suất nhỏ xảy ra thì... (sẽ dẫn đến hậu quả nghiêm trọng)」. Trình tự logic: Chủ đề hành động nhạy cảm (契約書の作成は) -> trạng từ giả định rủi ro (ひとつ) -> điều kiện giả định (間違えば) -> định ngữ chỉ quy mô hậu quả (巨額の) -> mệnh đề chỉ hướng kết quả tiêu cực (損失につながる) -> danh từ chỉ mối nguy hại/lo sợ (恐れがあります)。":
    "Cấu trúc 「ひとつ間違えば」 nghĩa là chỉ cần một sai lầm nhỏ sẽ dẫn đến hậu quả nghiêm trọng. Logic câu đi từ chủ đề nhạy cảm (契約書の作成は) sang điều kiện giả định rủi ro (ひとつ間違えば). Hậu quả được cảnh báo qua định ngữ (巨額の) gắn với kết quả tiêu cực (損失につながる) và khép lại bằng cụm từ chỉ mối nguy hại (恐れがあります).",

    # part_86.csv
    "Cấu trúc 「V-るべからず」 dùng để biểu thị sự cấm đoán mạnh mẽ trong văn viết (không được làm gì). 「開示す」 là dạng văn viết của 「開示する」, kết hợp với 「べからず」 tạo thành 「開示すべからず」 (không được tiết lộ). Trạng từ 「許可なく」 (không phép) và cụm 「他社に」 (cho công ty khác) bổ nghĩa cho hành động 「開示する」. Thứ tự cú pháp tự nhiên: Phần đầu câu (đối tượng thông tin) -> Trạng thái hành động (許可なく) -> Đối tượng nhận (他社に) -> Động từ (開示) -> Đuôi liên kết (す) -> Vĩ tố cấm chỉ (べからず)。":
    "Cấu trúc 「V-るべからず」 dùng để biểu thị sự cấm đoán mạnh mẽ trong văn viết. Trạng từ 「許可なく」 (không phép) và cụm 「他社に」 (cho công ty khác) bổ nghĩa trực tiếp cho động từ 「開示」. Động từ này đi với đuôi liên kết 「す」 và vĩ tố cấm chỉ 「べからず」 tạo thành lời cảnh báo nghiêm ngặt 「開示すべからず」.",
    
    "Cấu trúc 「V-るべきだ」 thể hiện nghĩa vụ hoặc lời khuyên mạnh mẽ (nên/phải làm gì). Ở đây động từ thể từ điển 「考える」 đi trực tiếp với 「べきだ」. Cụm trạng từ và tân ngữ 「常に顧客の利益を最優先に」 (luôn đặt lợi ích của khách hàng lên hàng đầu) bổ nghĩa cho động từ 「考える」. 「我々は」 đóng vai trò chủ ngữ đứng đầu phân khúc. Thứ tự sắp xếp tự nhiên theo cấu trúc câu tiếng Nhật: Chủ ngữ -> Trạng từ/Tân ngữ -> Động từ chính -> Đuôi ngữ pháp 「べきだ」。":
    "Cấu trúc 「V-るべきだ」 thể hiện nghĩa vụ mạnh mẽ. Chủ ngữ 「我々は」 đứng đầu, tiếp nối bằng cụm trạng từ và tân ngữ 「常に顧客の利益を最優先に」 (luôn đặt lợi ích khách hàng lên hàng đầu). Khối bổ nghĩa này gắn chặt với động từ 「考える」 và đuôi ngữ pháp 「べきだ」 để tạo tính thuyết phục.",
    
    "Cấu trúc 「V-るべきだった」 thể hiện sự hối hận, tiếc nuối về một việc đáng lẽ ra nên làm trong quá khứ nhưng đã không làm. 「確認しておくべきだった」 được kết hợp từ động từ 「確認する」 chia sang thể て là 「確認して」 kết hợp với 「おくべきだった」 (đáng lẽ nên chuẩn bị trước). Các thành phần bổ nghĩa bao gồm: phó từ 「もう一度」 (một lần nữa), tân ngữ 「添付ファイルを」 (file đính kèm) và trạng từ 「念入りに」 (một cách cẩn thận). Thứ tự tự nhiên từ khái quát đến chi tiết: Trạng từ tần suất -> Tân ngữ -> Trạng từ chỉ cách thức -> Động từ chính -> Trợ động từ bổ trợ。":
    "Cấu trúc 「V-るべきだった」 thể hiện sự hối hận về việc đáng lẽ nên làm. Câu được triển khai từ phó từ 「もう一度」 (một lần nữa), qua tân ngữ 「添付ファイルを」 (file đính kèm), đến trạng từ 「念入りに」 (cẩn thận). Tất cả kết tụ vào động từ chính 「確認して」 và trợ động từ bổ trợ 「おくべきだった」 (đáng lẽ nên kiểm tra kỹ).",
    
    "Cấu trúc 「V-すべきN」 là cấu trúc định ngữ, trong đó động từ 「する」 ở dạng 「すべき」 bổ nghĩa cho danh từ 「N」 theo sau (những việc cần phải làm). Ở đây, 「検討すべき」 bổ nghĩa cho danh từ 「課題」 tạo thành cụm 「検討すべき課題」 (những vấn đề cần thảo luận/xem xét). Trạng từ 「事前に」 (trước/trước mắt) bổ nghĩa cho động từ 「検討する」. Thứ tự cú pháp tự nhiên: Trạng từ bổ nghĩa -> Động từ nhóm 3 thể gốc -> Đuôi định ngữ 「すべき」 -> Danh từ được bổ nghĩa。":
    "Cấu trúc 「V-すべきN」 là cấu trúc định ngữ, dùng để chỉ những việc cần làm. Trạng từ 「事前に」 (trước mắt) bổ nghĩa cho động từ 「検討」. Động từ này kết hợp với đuôi 「すべき」 trở thành định ngữ bổ trợ hoàn hảo cho danh từ 「課題」 ở cuối cụm.",
    
    "Cấu trúc 「V-るべく」 dùng trong văn viết trang trọng để chỉ mục đích (để/nhằm mục đích làm gì). Động từ thể từ điển 「開拓する」 (khai phá/phát triển) đi với 「べく」 làm vế chỉ mục đích. Vế sau thể hiện hành động thực tế nhằm đạt mục đích đó: 「我が社は」 (chủ ngữ) thực hiện hành động 「設立することにいたしました」 (quyết định thành lập) đối với tân ngữ 「現地法人」 (pháp nhân tại địa phương). Thứ tự logic là: Cụm mục đích (Mục tiêu + Động từ mục tiêu + べく) -> Chủ ngữ hành động -> Tân ngữ -> Động từ quyết định hành động chính。":
    "Cấu trúc 「V-るべく」 dùng trong văn viết trang trọng để chỉ mục đích. Vế mục đích 「開拓すべく」 mở đầu câu, dẫn dắt sang hành động thực tế ở vế sau. Chủ ngữ 「我が社は」 tiến hành với tân ngữ 「現地法人」 (pháp nhân tại địa phương) và khép lại bằng quyết định 「設立することにいたしました」.",
    
    "Cấu trúc 「V-るべくしてV-た」 diễn tả một sự việc xảy ra là kết quả tất yếu của một quá trình (đương nhiên phải xảy ra như thế). Ở đây, động từ 「成功する」 được lặp lại: thể từ điển 「成功する」 + 「べくして」 + thể quá khứ 「成功した」. Từ nối 「と」 dẫn đề cho động từ phán đoán 「言えるでしょう」 (có thể nói là) ở phần đuôi câu. Thứ tự sắp xếp: Động từ thể từ điển -> Liên từ 「べくして」 -> Thân động từ lặp lại -> Đuôi chia thì quá khứ và trợ từ liên kết。":
    "Cấu trúc 「V-るべくしてV-た」 diễn tả một kết quả tất yếu đương nhiên phải xảy ra. Sự lặp lại động từ 「成功するべくして成功した」 tạo điểm nhấn mạnh mẽ. Trợ từ 「と」 đóng vai trò dẫn đề cho phán đoán khách quan 「言えるでしょう」 (có thể nói là) ở cuối câu.",
    
    "Cấu trúc 「V-るべくもない」 là cách nói trang trọng mang nghĩa 「hoàn toàn không thể/làm sao có thể làm V được」. Động từ nhóm 3 「対抗する」 ở thể từ điển kết hợp với 「べくもない」. 「我が社が」 (công ty chúng tôi) là chủ ngữ thực hiện hành động 「対抗する」. Thứ tự cú pháp tự nhiên: Chủ ngữ hành động (我が社が) -> Động từ nhóm 3 (対抗) -> Đuôi liên kết động từ (する) -> Thành phần phủ định khả năng (べくもない)。":
    "Cấu trúc 「V-るべくもない」 là cách nói trang trọng mang nghĩa hoàn toàn không thể làm gì đó. Chủ ngữ 「我が社が」 gắn trực tiếp với động từ 「対抗する」 và cụm phủ định khả năng 「べくもない」 để nhấn mạnh sự bất lực trong việc đối kháng.",
    
    "Cấu trúc 「V-るべし」 là lối nói cổ mang tính văn viết, diễn tả mệnh lệnh, nghĩa vụ hoặc ý chí mạnh mẽ (phải/nên làm gì). Động từ thể từ điển 「対応する」 kết hợp với 「べし」. Trạng từ bổ nghĩa cho hành động bao gồm hai tính từ 「誠実」 (thành thật) và 「迅速に」 (nhanh chóng) liên kết bằng từ nối 「かつ」 (và). Thứ tự logic: Trạng từ chỉ thái độ -> Từ nối và trạng từ tiếp theo -> Động từ hành động -> Vĩ tố mệnh lệnh cổ 「べし」。":
    "Cấu trúc 「V-るべし」 diễn tả mệnh lệnh, nghĩa vụ mạnh mẽ trong văn viết. Trạng từ chỉ thái độ 「誠実かつ迅速に」 (thành thật và nhanh chóng) làm nổi bật yêu cầu khắt khe đối với hành động 「対応する」. Vĩ tố mệnh lệnh cổ 「べし」 chốt lại câu với sự uy nghiêm.",
    
    "Tính từ đuôi na 「へた」 chỉ sự yếu kém trong một lĩnh vực. Khi đứng trước liên từ chỉ nguyên nhân 「ので」, 「へた」 chuyển thành 「へたな」. Cụm 「プレゼンがへたな」 nghĩa là 「dở thuyết trình」. Phó từ 「何度も」 (nhiều lần) bổ nghĩa cho hành động 「練習を重ねています」 (luyện tập nhiều lần). Thứ tự cú pháp tự nhiên: Đối tượng kém (プレゼンが) -> Tính từ đuôi na biến đổi theo 「ので」 (へたな) -> Liên từ nguyên nhân và thời điểm (ので、事前に) -> Phó từ chỉ tần suất (何度も)。":
    "Tính từ đuôi na 「へた」 chỉ sự yếu kém, khi đứng trước liên từ nguyên nhân 「ので」 sẽ biến đổi thành 「へたな」. Cụm nguyên nhân 「プレゼンがへたなので」 (vì dở thuyết trình) được dùng làm tiền đề cho hành động phía sau, nơi phó từ tần suất 「何度も」 kết hợp với hành động 「練習を重ねています」 (không ngừng luyện tập).",
    
    "Cấu trúc cơ bản là 「N1は N2がへただ」 (N1 thì dở N2). Ở đây, N1 là 「新人の鈴木さんは」 (cậu Suzuki mới vào làm), N2 là 「電話応対」 (nhận điện thoại) được bổ nghĩa bằng cụm định ngữ 「敬語を使った」 (sử dụng kính ngữ). 「まだ少し」 là phó từ chỉ mức độ bổ nghĩa cho tính từ 「へたです」 ở cuối câu. Thứ tự sắp xếp: Định ngữ của N2 -> Danh từ N2 kèm trợ từ 「が」 -> Phó từ chỉ mức độ -> Tính từ kết thúc câu。":
    "Cấu trúc cơ bản là 「N1は N2がへただ」 (N1 thì dở N2). N2 là 「電話応対」 được định ngữ 「敬語を使った」 bổ nghĩa. Phó từ mức độ 「まだ少し」 được đặt khéo léo ngay trước tính từ 「へたです」 ở cuối câu để làm nhẹ nhàng lời nhận xét.",
    
    "「へたをすると」 là một cụm phó từ cố định có nghĩa là 「nếu không cẩn thận/trong trường hợp xấu nhất thì...」. Nó bổ nghĩa cho toàn bộ vế sau chỉ kết quả tiêu cực. Cụm 「数億円の損失が」 (tổn thất vài trăm triệu yên) làm chủ ngữ cho tự động từ 「出る」 (phát sinh), kết hợp với cấu trúc chỉ mối nguy hại 「恐れがあります」 (có nguy cơ). Thứ tự sắp xếp: Cụm từ cố định chia đôi (へたを -> すると) -> Danh từ chỉ lượng tiền và thiệt hại -> Chủ ngữ đi kèm trợ từ 「が」。":
    "Cụm phó từ cố định 「へたをすると」 mang ý nghĩa cảnh báo \"nếu không cẩn thận/trong trường hợp xấu nhất thì...\". Cụm này bổ nghĩa cho toàn bộ kết quả tiêu cực phía sau, gồm chủ ngữ 「数億円の損失が」 (thiệt hại hàng trăm triệu yên) gắn với tự động từ 「出る」 và cấu trúc nguy hại 「恐れがあります」.",
    
    "Cấu trúc 「別段～ない」 có nghĩa là 「không có gì đặc biệt/đáng kể」. Phó từ phủ định 「別段」 đi kèm với dạng phủ định lịch sự ở cuối câu 「おりません」 (dạng khiêm nhường của いません/ありません). 「大きな問題は」 (vấn đề lớn) đóng vai trò chủ ngữ được nhấn mạnh bằng trợ từ 「は」. Động từ 「生じる」 (phát sinh) chia sang thể て là 「生じて」 để kết hợp với phụ động từ phủ định 「おりません」. Thứ tự sắp xếp: Phó từ phủ định -> Tính từ bổ nghĩa danh từ -> Danh từ chủ ngữ -> Động từ chính thể 「て」。":
    "Cấu trúc 「別段～ない」 có nghĩa là không có gì đáng kể. Phó từ phủ định 「別段」 đi kèm với chủ ngữ nhấn mạnh 「大きな問題は」. Hành động 「生じて」 nối với phụ động từ phủ định khiêm nhường 「おりません」 giúp câu văn lịch sự và chuyên nghiệp hơn.",
    
    "「別段のN」 mang nghĩa 「sự N đặc biệt/khác thường」. Ở đây 「別段の」 bổ nghĩa cho danh từ kính ngữ 「ご愛顧」 (sự nâng đỡ/ủng hộ từ khách hàng). Động từ kính ngữ 「賜り」 (nhận được - dạng liên dụng trang trọng) kết nối hai vế câu. Phó từ 「心より」 (từ tận đáy lòng) bổ nghĩa cho cụm từ cảm ơn trang trọng 「厚く御礼申し上げます」. Thứ tự cú pháp tự nhiên: Tính từ bổ nghĩa danh từ -> Danh từ tân ngữ -> Động từ liên kết -> Phó từ bổ nghĩa cho hành động cảm ơn ở cuối câu。":
    "「別段のN」 mang nghĩa sự N đặc biệt. Cụm bổ nghĩa 「別段のご愛顧」 gắn liền với động từ kính ngữ 「賜り」 (nhận được) để nối hai vế. Ở vế sau, phó từ 「心より」 (từ tận đáy lòng) nâng tầm trang trọng cho lời cảm ơn 「厚く御礼申し上げます」.",
    
    "Cấu trúc 「N là 別として」 có nghĩa là 「chưa nói đến N/ngoại trừ N ra」. Danh từ N ở đây là 「通常の打ち合わせ」 (buổi họp thường lệ) được bổ nghĩa bởi tính từ 「通常の」. Vế sau chỉ ra trường hợp đặc biệt 「重要な役員会議には」 (đối với cuộc họp ban giám đốc quan trọng) đòi hỏi hành động bắt buộc 「必ずスーツを着用してください」 (nhất định phải mặc vest). Thứ tự sắp xếp: Định ngữ của N -> Danh từ N đi kèm trợ từ 「は」 -> Cụm liên từ ngoại trừ 「別として」 -> Đối tượng đặc biệt của vế sau。":
    "Cấu trúc 「Nは別として」 có nghĩa là ngoại trừ N ra. Đối tượng bị loại trừ là 「通常の打ち合わせ」 (buổi họp thường lệ). Vế sau nhấn mạnh trường hợp đặc biệt 「重要な役員会議には」 (đối với cuộc họp giám đốc) đi kèm yêu cầu bắt buộc 「必ずスーツを着用してください」.",
    
    "Cấu trúc 「別に～ない」 biểu thị ý nghĩa 「không có gì đặc biệt / không... lắm」. Phó từ 「別に」 đi kèm với động từ phủ định 「ありません」 (không có). 「急ぎの予定」 (kế hoạch gấp) đóng vai trò chủ ngữ đi với trợ từ nhấn mạnh phủ định 「は」. Liên từ 「ので」 (vì) kết nối vế giải thích lý do này với đề xuất gặp mặt ở vế sau. Thứ tự sắp xếp: Phó từ phủ định -> Tính từ bổ nghĩa -> Danh từ chủ ngữ -> Động từ phủ định。":
    "Cấu trúc 「別に～ない」 biểu thị ý nghĩa không có gì đặc biệt. Phó từ 「別に」 kết hợp với chủ ngữ 「急ぎの予定は」 và động từ phủ định 「ありません」. Thông qua liên từ nguyên nhân 「ので」, vế này làm nền tảng tự nhiên cho đề xuất gặp mặt ở vế sau.",
    
    "Hậu tố 「～っぽい」 (mang đậm tính chất/có vẻ...) kết hợp với tính từ đuôi i 「安い」 bằng cách bỏ 「い」 và thêm 「っぽい」 tạo thành 「安っぽい」 (trông rẻ tiền). Khi bổ nghĩa cho động từ 「見える」 (trông có vẻ), tính từ đuôi i này đổi đuôi thành 「安っぽく」. 「ので」 chỉ nguyên nhân dẫn đến đề xuất 「修正すべきです」 ở vế sau. Thứ tự sắp xếp: Thân tính từ -> Hậu tố biến đổi phó từ -> Động từ trạng thái -> Liên từ chỉ nguyên nhân。":
    "Hậu tố 「～っぽい」 (có vẻ...) biến tính từ 「安い」 thành 「安っぽい」 (trông rẻ tiền). Để bổ nghĩa cho động từ 「見える」, tính từ này đổi dạng thành 「安っぽく」. Toàn bộ vế này đóng vai trò nguyên nhân (thông qua ので) dẫn đến đề xuất 「修正すべきです」 ở vế sau."
}

for i in range(81, 91):
    file = f'part_{i}.csv'
    path = os.path.join(dir_path, file)
    if not os.path.exists(path): continue
    
    with open(path, encoding='utf-8-sig') as f:
        r = list(csv.reader(f))
    
    headers = r[0]
    exp_idx = headers.index('Explanation') if 'Explanation' in headers else len(headers)-1
    
    changed = False
    for idx, row in enumerate(r):
        if idx == 0 or len(row) <= exp_idx: continue
        exp = row[exp_idx]
        
        for orig, new_val in rewrites.items():
            if orig in exp:
                exp = exp.replace(orig, new_val)
                row[exp_idx] = exp
                changed = True
                
    if changed:
        with open(path, 'w', encoding='utf-8-sig', newline='') as f:
            csv.writer(f).writerows(r)

print("Batch 17 and 18 manually reviewed and rewritten successfully!")
