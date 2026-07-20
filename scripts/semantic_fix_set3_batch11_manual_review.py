import csv, os

dir_path = r'd:\pj\xx\ai-gen-quiz\mondai2_ordering\csv_filled\set_3_academic'

rewrites = {
    # part_51.csv
    "Mẫu 「とうとう～V-なかった」 diễn tả kết quả cuối cùng sau một quá trình chờ đợi hay nỗ lực là đã không xảy ra điều mong muốn. Thứ tự câu: 「待ちましたが、」 (đã chờ nhưng) -> 「とうとう」 (cuối cùng thì) -> 「今日中には」 (trong ngày hôm nay - nhấn mạnh giới hạn thời gian) -> Động từ phủ định dạng lịch sự 「来ませんでした」 (đã không đến).":
    "Mẫu 「とうとう～V-なかった」 diễn tả kết quả cuối cùng sau một quá trình chờ đợi hay nỗ lực là đã không xảy ra điều mong muốn. Mạch câu triển khai từ 「待ちましたが、」 (đã chờ nhưng) sang phó từ 「とうとう」 (cuối cùng thì), tiếp nối bằng 「今日中には」 (trong ngày hôm nay - nhấn mạnh giới hạn thời gian) và kết thúc bằng động từ phủ định dạng lịch sự 「来ませんでした」 (đã không đến).",
    
    "「どうにか」 có nghĩa là 「bằng cách nào đó, suýt soát vừa kịp」. Thứ tự kết hợp từ trái sang phải: Chủ ngữ 「準備は、」 (Sự chuẩn bị thì) -> Phó từ bổ nghĩa 「どうにか」 (bằng cách nào đó) -> Trạng từ chỉ trạng thái 「予定通りに」 (đúng theo kế hoạch) -> Động từ kết thúc câu 「間に合いました」 (đã kịp giờ).":
    "「どうにか」 có nghĩa là 「bằng cách nào đó, suýt soát vừa kịp」. Câu văn được liên kết logic từ chủ ngữ 「準備は、」 (Sự chuẩn bị thì) đi kèm phó từ bổ nghĩa 「どうにか」 (bằng cách nào đó) và trạng từ chỉ trạng thái 「予定通りに」 (đúng theo kế hoạch), sau cùng khép lại bằng động từ 「間に合いました」 (đã kịp giờ).",
    
    "「どうにかする」 nghĩa là 「xoay xở, tìm cách giải quyết」. Đi kèm cấu trúc điều kiện 「～ないと」 (nếu không... thì). Thứ tự câu logic: Trạng từ 「早く」 (nhanh chóng) -> Vế giả định điều kiện 「どうにかしないと、」 (nếu không giải quyết bằng cách nào đó) -> Chủ ngữ vế sau 「業務に支障が」 (trở ngại cho công việc) -> Hệ quả tất yếu 「出てしまいます」 (sẽ xảy ra mất).":
    "「どうにかする」 nghĩa là 「xoay xở, tìm cách giải quyết」, thường đi kèm cấu trúc điều kiện 「～ないと」 (nếu không... thì). Mạch diễn đạt đi từ trạng từ 「早く」 (nhanh chóng) gắn với vế giả định 「どうにかしないと、」 (nếu không giải quyết bằng cách nào đó), làm tiền đề cho chủ ngữ vế sau 「業務に支障が」 (trở ngại cho công việc) và hệ quả tất yếu 「出てしまいます」 (sẽ xảy ra mất).",
    
    "「どうにかなる」 nghĩa là 「bằng cách nào đó rồi sẽ ổn thỏa」. Thứ tự cấu trúc: Vế điều kiện giả định 「協力すれば」 (nếu hợp tác) -> Cụm tính từ bổ nghĩa cho danh từ 「この厳しい」 (gay gắt này) -> Chủ ngữ 「交渉も」 (cuộc đàm phán cũng) -> Cụm nội dung đi với trợ từ と 「どうにかなると」 (rằng sẽ ổn thỏa) -> Động từ chỉ suy nghĩ 「思います」.":
    "「どうにかなる」 nghĩa là 「bằng cách nào đó rồi sẽ ổn thỏa」. Câu được xây dựng từ vế giả định 「協力すれば」 (nếu hợp tác), tiếp đến là cụm tính từ bổ nghĩa 「この厳しい」 (gay gắt này) cho chủ ngữ 「交渉も」 (cuộc đàm phán cũng). Nối tiếp là cụm nội dung 「どうにかなると」 (rằng sẽ ổn thỏa) và động từ chỉ suy nghĩ 「思います」 ở cuối câu.",
    
    "Mẫu 「どうにも～ない」 biểu thị ý nghĩa 「chẳng thể làm gì được, hoàn toàn không thể」. Thứ tự sắp xếp câu: Vế nguyên nhân nguyên do 「厳しすぎて、」 (vì quá khắc nghiệt) -> Phạm vi/năng lực 「弊社の力では」 (bằng năng lực của công ty chúng tôi thì) -> Phó từ đi kèm phủ định 「どうにも」 -> Động từ thể khả năng phủ định 「受け入れられません」 (không thể chấp nhận được).":
    "Mẫu 「どうにも～ない」 biểu thị ý nghĩa 「chẳng thể làm gì được, hoàn toàn không thể」. Sự việc được diễn giải từ nguyên nhân 「厳しすぎて、」 (vì quá khắc nghiệt) kết hợp với phạm vi năng lực 「弊社の力では」 (bằng năng lực của công ty chúng tôi thì). Phần phó từ 「どうにも」 đứng ngay trước động từ phủ định 「受け入れられません」 (không thể chấp nhận được) để nhấn mạnh sự bất lực.",
    
    "「どうにもならない」 nghĩa là 「vô ích, không thể cứu vãn hoặc thay đổi được nữa」. Thứ tự kết hợp từ: Định ngữ và tân ngữ 「予算を」 (ngân sách) -> Cụm danh từ hóa làm chủ ngữ 「変更することは、」 (việc thay đổi...) -> Trạng từ thời gian tâm trạng 「今さら」 (đến mức này rồi/giờ này thì) -> Cụm kết thúc câu mang tính phủ định tuyệt đối 「どうにもならない」.":
    "「どうにもならない」 nghĩa là 「vô ích, không thể cứu vãn hoặc thay đổi được nữa」. Mạch câu bắt đầu từ tân ngữ 「予算を」 (ngân sách) kết hợp cụm danh từ hóa 「変更することは、」 (việc thay đổi...) làm chủ ngữ. Điểm nhấn là trạng từ thời gian 「今さら」 (đến mức này rồi) làm nền cho kết luận mang tính phủ định tuyệt đối 「どうにもならない」.",
    
    "「どうも」 ở đây diễn tả tâm trạng mơ hồ, không chắc chắn (hình như, không hiểu sao). Thứ tự câu: Chủ ngữ chính 「数字は、」 (những con số thì) -> Phó từ chỉ sự không chắc chắn 「どうも」 -> Cụm bổ nghĩa cho danh từ chỉ cảm giác 「間違っているような」 (có vẻ sai sót) -> Cụm từ kết thúc câu 「気がします」 (tôi có cảm giác là).":
    "「どうも」 diễn tả tâm trạng mơ hồ, không chắc chắn (hình như, không hiểu sao). Ở đây chủ ngữ chính 「数字は、」 (những con số thì) được theo sau bởi phó từ 「どうも」. Cụm bổ nghĩa 「間違っているような」 (có vẻ sai sót) gắn trực tiếp với cụm từ kết thúc 「気がします」 (tôi có cảm giác là) để hoàn thiện ý.",
    
    "Phó từ 「どうも」 thường đi kèm với các cấu trúc phán đoán ước đoán như 「～そうだ」 để nhấn mạnh sự mập mờ, dễ có khả năng xảy ra. Thứ tự câu: Vế căn cứ phán đoán 「見る限り、」 (theo như quan sát...) -> Phó từ và định từ 「どうもこの」 (hình như... này) -> Chủ ngữ 「交渉は」 (cuộc đàm phán) -> Kết thúc bằng hình thái dự đoán hành động 「長引きそうです」 (có vẻ sẽ kéo dài).":
    "Phó từ 「どうも」 thường đi kèm các cấu trúc phán đoán như 「～そうだ」 để nhấn mạnh sự mập mờ, khả năng xảy ra cao. Từ căn cứ phán đoán 「見る限り、」 (theo như quan sát...), câu văn chuyển sang chủ ngữ 「どうもこの交渉は」 (hình như cuộc đàm phán này) và kết luận bằng hình thái dự đoán 「長引きそうです」 (có vẻ sẽ kéo dài).",
    
    "「どうも」 dùng để biểu thị sự bối rối, e ngại hoặc khó xử (困惑) trước một tình huống xấu. Thứ tự câu: Định ngữ bổ nghĩa cho tân ngữ 「何度も同じ」 (nhiều lần cùng một...) -> Vế nguyên nhân lý do 「ミスを繰り返すので、」 (vì lặp lại sai lầm) -> Phó từ diễn tả sự bất lực/khó xử 「どうも」 -> Cụm từ cảm thán kết thúc 「困ったものです」 (thật là đáng ngại/khó xử).":
    "「どうも」 dùng để biểu thị sự bối rối, khó xử (困惑) trước tình huống xấu. Diễn tiến câu bắt đầu bằng nguyên nhân 「何度も同じミスを繰り返すので、」 (vì lặp lại sai lầm nhiều lần cùng một lỗi). Sự bất lực được nhấn mạnh qua phó từ 「どうも」 đặt trước cụm cảm thán kết thúc 「困ったものです」 (thật là đáng ngại).",
    
    "「どうも」 đứng trước các từ cảm ơn để nhấn mạnh lòng biết ơn sâu sắc trong văn hóa giao tiếp công sở. Thứ tự câu: Trạng từ thời gian 「今日は」 -> Tân ngữ của hành động 「お時間を」 -> Động từ nhận hành động thể khiêm nhường 「いただき、」 (được nhận) -> Phó từ nhấn mạnh 「どうも」 -> Lời cảm ơn quá khứ lịch sự 「ありがとうございました」.":
    "「どうも」 đứng trước các từ cảm ơn để nhấn mạnh lòng biết ơn trong môi trường công sở. Khởi đầu với trạng từ thời gian 「今日は」, tiếp nối bằng hành động khiêm nhường 「お時間をいただき、」 (được nhận thời gian quý báu). Cuối cùng, phó từ 「どうも」 bổ trợ mạnh mẽ cho lời cảm ơn lịch sự 「ありがとうございました」.",
    
    "「どうもない」 có nghĩa là 「không có vấn đề gì, không bị sao cả」. Thứ tự logic ngữ pháp: Chủ ngữ của câu 「データへの影響は、」 (ảnh hưởng tới dữ liệu thì) -> Vế liên kết chỉ điều kiện/kết quả kiểm tra 「確認したところ」 (sau khi xác nhận) -> Cụm từ chỉ tình trạng bình thường 「どうもない」 (không có vấn đề gì) -> Thể đánh giá, suy đoán nhẹ nhàng 「ようです」 (có vẻ như).":
    "「どうもない」 có nghĩa là 「không có vấn đề gì, không bị sao cả」. Logic ngữ pháp được hình thành từ chủ ngữ 「データへの影響は、」 (ảnh hưởng tới dữ liệu thì) và kết quả kiểm tra 「確認したところ」 (sau khi xác nhận). Tình trạng bình thường được nêu ra qua cụm 「どうもない」 (không có vấn đề gì) và đánh giá nhẹ nhàng bằng 「ようです」 (có vẻ như).",
    
    "「どうやら～そうだ」 biểu thị sự suy đoán dựa trên các dấu hiệu thực tế, mang nghĩa là 「có vẻ như cuối cùng thì/bằng cách nào đó...」. Thứ tự câu: Căn cứ đưa ra nhận định 「見ると、」 (nhìn từ...) -> Phó từ ước đoán trạng thái 「どうやら」 -> Trạng ngữ bổ nghĩa 「納期に」 (kịp thời hạn giao hàng) -> Thể suy đoán kết thúc 「間に合いそうです」.":
    "「どうやら～そうだ」 biểu thị sự suy đoán dựa trên dấu hiệu thực tế (có vẻ như...). Mạch câu bắt nguồn từ căn cứ 「見ると、」 (nhìn từ...), theo sau là phó từ ước đoán 「どうやら」. Trạng ngữ 「納期に」 (kịp thời hạn giao hàng) được gắn liền với phán đoán kết thúc 「間に合いそうです」.",
    
    "Cụm trạng từ 「どうやらこうやら」 mang nghĩa là 「vất vả lắm mới..., bằng cách này hay cách khác rốt cuộc cũng...」. Thứ tự câu: Vế nguyên nhân 「手伝ってくれたので、」 (vì đã giúp đỡ) -> Trạng từ phương thức 「どうやらこうやら」 (bằng cách này cách khác) -> Chủ ngữ vế kết quả 「資料が」 (tài liệu) -> Động từ kết quả hoàn thành 「完成しました」.":
    "Cụm trạng từ 「どうやらこうやら」 diễn tả ý 「vất vả lắm mới..., bằng cách này cách khác rốt cuộc cũng...」. Nhờ vế nguyên nhân 「手伝ってくれたので、」 (vì đã giúp đỡ), trạng từ phương thức 「どうやらこうやら」 được dùng làm bước đệm dẫn tới kết quả hoàn thành 「資料が完成しました」 (tài liệu đã hoàn thành).",
    
    "「どうりで～わけだ」 nghĩa là 「hèn chi, thảo nào mà...」. Thứ tự kết hợp câu: Phó từ nối câu 「どうりで」 đặt ở đầu vế câu kết luận -> Từ hạn định sở hữu 「彼の」 (của anh ấy) -> Chủ ngữ vế kết luận 「プレゼンが」 (bài thuyết trình) -> Cấu trúc nhấn mạnh kết luận tất yếu hiển nhiên 「上手なわけだ」 (giỏi là phải).":
    "「どうりで～わけだ」 mang nghĩa 「hèn chi, thảo nào mà...」. Phó từ 「どうりで」 mở đầu vế kết luận, kết hợp nhịp nhàng với chủ ngữ 「彼のプレゼンが」 (bài thuyết trình của anh ấy) và cấu trúc nhấn mạnh sự tất yếu hiển nhiên 「上手なわけだ」 (giỏi là phải).",
    
    "Cấu trúc 「V-Renshoukei + 通し」 biểu thị một hành động diễn ra liên tục không hề dừng nghỉ. Thứ tự logic: Trạng từ chỉ thời gian liên tục 「一日中」 (suốt cả ngày) -> Động từ liên hợp mang ngữ pháp 「立ち通し」 (đứng liên tục không nghỉ) -> Vế chỉ nguyên nhân dạng lịch sự 「だったので」 (vì là như vậy nên...) -> Hệ quả kết thúc câu 「疲れました」 (đã mệt nhoài).":
    "Cấu trúc 「V-Renshoukei + 通し」 biểu thị hành động diễn ra liên tục. Logic câu bắt đầu từ thời gian 「一日中」 (suốt cả ngày) ghép với động từ 「立ち通し」 (đứng liên tục không nghỉ). Phần này trở thành vế nguyên nhân 「だったので」 (vì... nên) dẫn đến hệ quả 「疲れました」 (đã mệt nhoài).",
    
    "Mẫu 「Nを通して」 biểu thị ý nghĩa thông qua một trung gian, người môi giới hoặc đại lý. Thứ tự cấu trúc câu: Cụm tân ngữ làm trung gian 「代理店を」 (đại lý...) -> Trạng từ chỉ phương thức 「通して」 (thông qua) -> Tân ngữ hành động chính 「新しい顧客を」 (khách hàng mới) -> Động từ kết thúc câu hành động 「開拓しました」 (đã khai thác/mở rộng).":
    "Mẫu 「Nを通して」 biểu thị việc thông qua một trung gian, người môi giới. Câu được cấu trúc với trung gian 「代理店を」 (đại lý) đi liền với trạng từ phương thức 「通して」 (thông qua). Tiếp đến là tân ngữ 「新しい顧客を」 (khách hàng mới) và động từ hoàn tất hành động 「開拓しました」 (đã khai thác).",
    
    "Mẫu 「V-ることを通して」 dùng khi muốn nói 「thông qua việc thực hiện hành động V」 để tiếp thu, học hỏi được một điều gì đó. Thứ tự câu: Tân ngữ của vế phụ 「直接お話を」 (việc trò chuyện trực tiếp) -> Cấu trúc danh từ hóa và chỉ phương thức 「することを通して、」 (thông qua việc thực hiện...) -> Tân ngữ vế chính 「ビジネスマナーを」 (văn hóa ứng xử kinh doanh) -> Cụm động từ kết thúc 「身につけます」 (tiếp thu/trang bị cho bản thân).":
    "Mẫu 「V-ることを通して」 biểu thị việc học hỏi/tiếp thu thông qua một hành động. Cấu trúc danh từ hóa 「直接お話をすることを通して、」 (thông qua việc trò chuyện trực tiếp) được dùng làm phương thức dẫn dắt đến tân ngữ chính 「ビジネスマナーを」 (văn hóa ứng xử) và động từ tiếp thu 「身につけます」.",
    
    # part_52.csv
    "Cấu trúc 「～かと思うほど」 diễn tả mức độ cao của một trạng thái, đến mức người ta tưởng chừng như điều đó xảy ra. Ở đây, các cuộc gọi khiếu nại đổ về liên tục (ひっきりなしに) đến mức cảm giác tiếng chuông điện thoại không bao giờ ngừng reo (鳴りやまない). Thứ tự kết hợp tự nhiên: Chủ ngữ bổ nghĩa cho hành động reo 「電話のベルが」 -> Vị ngữ phủ định nghi vấn 「鳴りやまないかと」 -> Cấu trúc so sánh mức độ 「思うほど」 -> Phó từ bổ nghĩa cho vế sau 「ひっきりなしに」.":
    "Cấu trúc 「～かと思うほど」 diễn tả mức độ cao của một trạng thái đến mức tưởng chừng như điều đó sắp xảy ra. Ở đây, các cuộc gọi đổ về liên tục (ひっきりなしに) khiến người ta cảm tưởng tiếng chuông không bao giờ ngừng reo (鳴りやまない). Mạch diễn đạt tự nhiên khi chủ ngữ 「電話のベルが」 đi với vị ngữ 「鳴りやまないかと」 và cấu trúc so sánh 「思うほど」, bổ nghĩa trực tiếp cho phó từ 「ひっきりなしに」 phía sau.",
    
    # part_55.csv
    "Cấu trúc `V-たところで` ở đây biểu thị một thời điểm ngắt quãng, ngay sau khi hành động kết thúc. Thứ tự câu: `印刷し終えた` (hoàn thành in) kết hợp với `ところで` (ngay khi) tạo thành mệnh đề trạng ngữ thời gian, tiếp theo là đối tượng `上司から内容の` + `変更を` (thay đổi nội dung từ cấp trên) để làm tân ngữ bổ nghĩa cho hành động chính ở vĩ tố `指示されました` (được chỉ thị).":
    "Cấu trúc `V-たところで` biểu thị một thời điểm ngắt quãng ngay sau khi hành động kết thúc. Mệnh đề trạng ngữ thời gian `印刷し終えたところで` (ngay khi hoàn thành in) làm nền cho vế sau, trong đó đối tượng `上司から内容の変更を` (thay đổi nội dung từ cấp trên) đóng vai trò tân ngữ bổ nghĩa cho hành động bị động `指示されました` (được chỉ thị).",
    
    "Cấu trúc `V-たところで～ない` diễn tả ý nghĩa 「dẫu có làm gì đi nữa thì cũng không có kết quả/vô ích」. Thứ tự kết hợp: bổ ngữ `スケジュールを修正した` (sửa đổi lịch trình) + `ところで` (dẫu có) đi liền nhau để mở đầu giả định vô ích, theo sau là danh từ chỉ mục tiêu thời gian `今月の納期には` và trạng từ đi kèm phủ định `到底間に合いそうに` để kết thúc bằng vĩ tố phủ định `ありません`.":
    "Cấu trúc `V-たところで～ない` mang ý nghĩa dẫu có làm gì đi nữa thì cũng vô ích. Giả định vô ích `スケジュールを修正したところで` (dẫu có sửa đổi lịch trình) được mở đầu, theo sau là mục tiêu thời gian `今月の納期には` và trạng từ `到底間に合いそうに` gắn với vĩ tố phủ định `ありません` để nhấn mạnh sự bất khả thi.",
    
    "Cấu trúc `～ところを` kết hợp với từ mang tính chào hỏi, thể hiện sự ái ngại khi làm phiền ai đó trong hoàn cảnh nhất định. Thứ tự câu: danh từ sở hữu `ご多忙の` bổ nghĩa cho hoàn cảnh, `ところを` đứng ngay sau, tiếp đến là cụm từ xin lỗi mang tính đệm đầu `大変恐縮ですが`, tạo tiền đề cho lời yêu cầu lịch sự gồm tân ngữ `こちらの契約書を` và cụm động từ kính ngữ kèm câu hỏi `ご一読いただけます` + `でしょうか`.":
    "Cấu trúc `～ところを` kết hợp các từ mào đầu thể hiện sự ái ngại khi làm phiền người khác. Cụm bổ nghĩa hoàn cảnh `ご多忙のところを` đi với lời xin lỗi đệm `大変恐縮ですが` để tạo tiền đề mềm mỏng. Theo sau đó là tân ngữ `こちらの契約書を` và yêu cầu lịch sự `ご一読いただけますでしょうか`.",
    
    "Cấu trúc `Nとしては` dùng để chỉ một trường hợp so sánh mang tính ngoại lệ so với tiêu chuẩn, mức độ trung bình thông thường của nhóm N đó. Thứ tự câu: định ngữ `入社したばかりの` bổ nghĩa cho danh từ nhóm tiêu chuẩn `新入社員`, đi liền với `としては` để tạo điểm so sánh, theo sau là chủ ngữ của đặc điểm `営業の成績が` đi kèm trạng từ nhấn mạnh `極めて` bổ nghĩa cho tính từ kết thúc câu ở dạng trang trọng `優秀である`.":
    "Cấu trúc `Nとしては` dùng để chỉ một trường hợp ngoại lệ so với mức trung bình của nhóm N. Điểm so sánh được tạo ra qua cụm `入社したばかりの新入社員としては`. Phần đặc điểm phía sau có chủ ngữ `営業の成績が` kết hợp cùng trạng từ `極めて` bổ nghĩa cho tính từ trang trọng `優秀である`.",
    
    "Cấu trúc `～とする` kết hợp với phó từ mô tả trạng thái cảm xúc (như ほっと). Thứ tự kết hợp logic: bổ ngữ hướng đối tượng `取引先への` bổ nghĩa cho danh từ chủ ngữ của mệnh đề nguyên nhân `プレゼンテーションが`, kết hợp trạng từ chỉ tính chất `無事に` bổ nghĩa cho động từ nối `終わって`, dẫn tới kết quả trạng thái tâm lý là từ mô phỏng trạng thái `ほっと` kết hợp với vĩ tố chia thì quá khứ lịch sự `しました`.":
    "Cấu trúc `～とする` thường kết hợp với phó từ mô tả trạng thái cảm xúc (ví dụ ほっと). Mệnh đề nguyên nhân `取引先へのプレゼンテーションが無事に終わって` dẫn tới kết quả trạng thái tâm lý là từ mô phỏng `ほっと` kết hợp với vĩ tố thì quá khứ lịch sự `しました`."
}

for i in range(51, 56):
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

print("Batch 11 manually reviewed and rewritten successfully!")
