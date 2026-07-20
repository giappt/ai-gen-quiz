import csv, os

dir_path = r'd:\pj\xx\ai-gen-quiz\mondai2_ordering\csv_filled\set_3_academic'

rewrites = {
    # part_71.csv (Batch 15)
    "「交渉における」 bổ nghĩa cho danh từ 「最重要課題」 phía sau nhằm chỉ bối cảnh diễn ra (「trong cuộc đàm phán」). 「信頼関係の」 bổ nghĩa cho 「構築」. Thứ tự sắp xếp logic đi từ bối cảnh đến chủ ngữ và cụm vị ngữ.":
    "「交渉における」 bổ nghĩa cho danh từ 「最重要課題」 phía sau nhằm chỉ bối cảnh diễn ra (trong cuộc đàm phán). Ngoài ra, định ngữ 「信頼関係の」 bổ trợ cho danh từ 「構築」. Sự liên kết các thành phần diễn ra rất hợp lý: dẫn dắt từ bối cảnh, đến chủ ngữ và cuối cùng là cụm vị ngữ.",

    # part_76.csv
    r"\Thứ tự sắp xếp dựa trên cấu trúc kính ngữ business: 「取引先の」 (đối tác) bổ nghĩa cho danh từ chỉ người 「みなさまがたにも」 (đến quý vị). Sau đó là cụm tân ngữ 「格別のご高配を」 (sự quan tâm đặc biệt) đi với động từ thể khiêm nhường 「賜り」 (nhận được) để thể hiện sự biết ơn từ phía công ty.\\":
    r"\Dựa trên cấu trúc kính ngữ business, định ngữ 「取引先の」 (đối tác) bổ nghĩa cho danh từ chỉ người 「みなさまがたにも」 (đến quý vị). Cụm tân ngữ 「格別のご高配を」 (sự quan tâm đặc biệt) kết hợp nhịp nhàng với động từ thể khiêm nhường 「賜り」 (nhận được) để thể hiện sự biết ơn từ phía công ty.\\",
    
    # part_77.csv
    "「V-ぬ」 là dạng phủ định cổ (văn viết), trong kinh doanh thường gặp trong các cụm từ cố định như 「知らぬ顔」 (vẻ mặt không biết/giả vờ không biết). Thứ tự cú pháp: 「たとえ～であっても」 (cho dù là...) bổ nghĩa cho tình huống, 「知らぬ顔を」 là tân ngữ đi với động từ 「突き通すべきです」 (phải giữ vững đến cùng) để tạo thành một quy tắc bảo mật trong công ty.":
    "「V-ぬ」 là dạng phủ định cổ, thường gặp trong cụm từ cố định như 「知らぬ顔」 (vẻ mặt không biết). Trong câu này, 「たとえ～であっても」 (cho dù là...) bổ nghĩa cho tình huống. Cụm tân ngữ 「知らぬ顔を」 đi liền với động từ 「突き通すべきです」 (phải giữ vững đến cùng) tạo thành nguyên tắc bảo mật.",
    
    "「V-ぬまに」 là biến thể của 「ない間に」 (trong lúc chưa/trong lúc không có). Trong văn phòng, cụm 「席を外しているぬまに」 (trong lúc sếp đang rời khỏi chỗ) được dùng để tranh thủ làm việc khác. Thứ tự tự nhiên: Chủ ngữ nhỏ 「課長が」 + hành động 「席を外している」 + ngữ pháp 「ぬまに」, sau đó đến đối tượng 「この至急の書類を」 và hành động 「確認しておこう」.":
    "「V-ぬまに」 là biến thể của 「ない間に」. Cụm 「席を外しているぬまに」 (trong lúc sếp rời chỗ) dùng để diễn tả việc tranh thủ làm việc khác. Chủ ngữ nhỏ 「課長が」 đi kèm hành động 「席を外している」 và ngữ pháp 「ぬまに」 tạo thành vế đầu. Vế sau tiếp nối bằng đối tượng 「この至急の書類を」 và hành động 「確認しておこう」.",
    
    "Lưu ý: Cột cấu trúc gốc của tài liệu nguồn biểu thị mệnh đề định ngữ 「NがVた＋の＋N」 (hoặc danh từ hóa tùy biến thể, ở đây ám chỉ cấu trúc bổ nghĩa cho danh từ đổi が thành の hoặc bổ nghĩa thông thường). Để đúng cú pháp tự nhiên: 「鈴木さんが作成した」 là mệnh đề bổ nghĩa cho danh từ 「企画書」. Chủ ngữ trong mệnh đề phụ dùng 「が」. 「企画書は」 là chủ ngữ chính, theo sau là mức độ 「非常に」 và tính từ 「完成度が高いです」 (độ hoàn thiện cao).":
    "Lưu ý: Cột cấu trúc gốc của tài liệu nguồn biểu thị mệnh đề định ngữ 「NがVた＋の＋N」. Để diễn đạt tự nhiên hơn, mệnh đề phụ 「鈴木さんが作成した」 bổ nghĩa cho danh từ 「企画書」, với chủ ngữ dùng 「が」. Chủ ngữ chính 「企画書は」 dẫn dắt người đọc đến phần đánh giá mức độ 「非常に」 và tính từ 「完成度が高いです」 (độ hoàn thiện cao).",

    # part_78.csv
    "Thứ tự kết hợp: Tính từ đuôi i 広い (rộng) đi với danh từ hóa の để chỉ 「phòng rộng」 thay cho việc lặp lại 「会議室」. Tiếp theo là trợ từ は đóng vai trò chủ ngữ cho vị ngữ 空いていませんか (còn trống không).":
    "Tính từ đuôi i 広い (rộng) đi với danh từ hóa の để chỉ 「phòng rộng」, tránh lặp lại từ 「会議室」. Trợ từ は làm chủ ngữ, kết nối trực tiếp với vị ngữ 空いていませんか (còn trống không).",
    
    "Thứ tự kết hợp: Tính từ đuôi na 斬新 (tính tân tiến/độc đáo) bổ nghĩa cho danh từ hóa の (thay cho パンフレット) phải thêm な thành 斬新な. Trợ từ を chỉ đối tượng của hành động đằng sau là 「用意してください」 (hãy chuẩn bị).":
    "Tính từ đuôi na 斬新 (tính tân tiến/độc đáo) khi bổ nghĩa cho danh từ hóa の (thay cho パンフレット) sẽ chuyển thành 斬新な. Trợ từ を nối phần này với hành động đằng sau là 「用意してください」 (hãy chuẩn bị).",
    
    "Thứ tự kết hợp: Thể thông thường của tính từ đuôi na 大丈夫 khi đi với danh từ hóa の ở cuối câu hỏi để nhấn mạnh sự xác nhận sẽ đi kèm với な thành 大丈夫なの.":
    "Thể thông thường của tính từ đuôi na 大丈夫 khi đi với danh từ hóa の ở cuối câu nhằm nhấn mạnh sự xác nhận, do đó sẽ chuyển thành 大丈夫なの.",
    
    "Thứ tự kết hợp: Động từ あった (đã có) ở thể thông thường đi trực tiếp với の ở cuối câu nhằm giải thích, trình bày sự việc một cách nhẹ nhàng với cấp trên thân thiết hoặc đồng nghiệp.":
    "Động từ あった (đã có) ở thể thông thường kết hợp trực tiếp với の ở cuối câu nhằm giải thích, trình bày sự việc một cách nhẹ nhàng với đồng nghiệp.",
    
    "Thứ tự kết hợp: Liệt kê các lý do mang tính than phiền: động từ/tính từ thể thông thường + の + động từ/tính từ thể thông thường + の + と (kết hợp với 理由をつけて để chỉ nội dung viện cớ).":
    "Câu này liệt kê các lý do mang tính than phiền bằng cấu trúc: động từ/tính từ thể thông thường + の + động từ/tính từ thể thông thường + の + と. Cấu trúc này liên kết chặt chẽ với 理由をつけて để chỉ nội dung viện cớ.",
    
    "Thứ tự kết hợp: Cấu trúc thể hiện sự phân vân hoặc tranh cãi giữa hai lựa chọn khẳng định và phủ định: V-る (参加する) + の + V-ない (参加しない) + の + と (chỉ nội dung tranh cãi).":
    "Cấu trúc này thể hiện sự phân vân, tranh cãi giữa hai lựa chọn khẳng định và phủ định qua hình thức: V-る (参加する) + の + V-ない (参加しない) + の + と (chỉ nội dung tranh cãi).",
    
    "Thứ tự kết hợp: Động từ 行く ở thể từ điển kết hợp với のか ở cuối câu hỏi tự vấn hoặc hỏi xác nhận một sự thật mang tính ngạc nhiên hoặc làm rõ sự việc.":
    "Động từ 行く ở thể từ điển đi liền với のか ở cuối câu hỏi tự vấn, thể hiện sự ngạc nhiên hoặc muốn làm rõ sự việc.",
    
    "Thứ tự kết hợp: Động từ 考えている kết hợp với のか tạo thành mệnh đề câu hỏi gián tiếp (Đang suy nghĩ cái gì...), làm bổ ngữ cho hành động 確認させてください ở phía sau.":
    "Động từ 考えている kết hợp với のか tạo thành mệnh đề câu hỏi gián tiếp (Đang suy nghĩ cái gì...). Mệnh đề này làm bổ ngữ khéo léo cho hành động 確認させてください ở phía sau.",
    
    "Thứ tự kết hợp: Động từ thể thông thường 集中している (đang tập trung) kết hợp với のだ ở cuối câu để đưa ra lời giải thích cho nguyên nhân dẫn đến sự cố sập máy chủ.":
    "Động từ thể thông thường 集中している (đang tập trung) kết hợp với のだ ở cuối câu để đưa ra lời giải thích thuyết phục cho nguyên nhân sự cố sập máy chủ.",
    
    "Thứ tự kết hợp: Động từ 開発していく (sẽ tiếp tục phát triển) ở thể thông thường đi với のだ để thể hiện quyết tâm mạnh mẽ hoặc khẳng định chủ trương của doanh nghiệp.":
    "Động từ 開発していく (sẽ tiếp tục phát triển) ở thể thông thường gắn liền với のだ nhằm thể hiện quyết tâm mạnh mẽ và khẳng định chủ trương của doanh nghiệp.",
    
    "Thứ tự kết hợp: Từ nghi vấn (何) đi với danh từ 原因. Vì 原因 là danh từ nên khi kết hợp với cấu trúc なのだ phải thêm な thành 原因なのだ để nhấn mạnh câu hỏi lý do.":
    "Từ nghi vấn 何 đi với danh từ 原因. Vì 原因 là danh từ, cấu trúc tiếp nối phải biến đổi thành 原因なのだ để làm nổi bật và nhấn mạnh lý do.",
    
    "Thứ tự kết hợp: Từ nối つまり (Tóm lại) đưa ra kết luận. Động từ 間違っていた ở thể quá khứ kết hợp với のだ để khẳng định và giải thích bản chất mang tính đúc kết của vấn đề.":
    "Từ nối つまり (Tóm lại) dùng để đưa ra kết luận. Động từ 間違っていた ở thể quá khứ gắn chặt với のだ, qua đó khẳng định và giải thích bản chất đúc kết của vấn đề.",
    
    "Thứ tự kết hợp: Từ nối だから (Do đó) chỉ kết quả. Động từ 成功した (đã thành công) bổ nghĩa trực tiếp cho のだ để nhấn mạnh lý do tại sao kết quả tốt đẹp đó lại xảy ra.":
    "Từ nối だから (Do đó) chỉ kết quả. Động từ 成功した (đã thành công) bổ nghĩa trực tiếp cho のだ, nhấn mạnh lý do đằng sau kết quả tốt đẹp đó.",
    
    "Thứ tự kết hợp: Danh từ ビジネスパーソン đi với なのだから (Vì là... nên đương nhiên) yêu cầu danh từ phải đi kèm な, thể hiện một lý do hiển nhiên mang tính trách nhiệm.":
    "Khi danh từ ビジネスパーソン kết hợp với cấu trúc なのだから (Vì là... nên đương nhiên), từ な là thành phần bắt buộc để thể hiện một lý do hiển nhiên mang tính trách nhiệm.",
    
    "Thứ tự kết hợp: Hành động làm sẵn (確認しておく) chuyển về thể quá khứ của danh từ hóa のだった (đáng lẽ nên...) thể hiện sự hối hận vì đã không kiểm tra lại kỹ lưỡng.":
    "Hành động chuẩn bị sẵn 確認しておく được chuyển sang dạng quá khứ のだった (đáng lẽ nên...). Điều này thể hiện sự hối hận vì đã không kiểm tra lại kỹ lưỡng.",
    
    "Thứ tự kết hợp: Động từ ありました chuyển thành thể thông thường quá khứ あった kết hợp với のだった nhằm tổng kết, kể lại một sự thật đầy cảm xúc hoặc mang tính thuyết minh lịch sử sự việc.":
    "Động từ ありました chuyển thành thể thông thường quá khứ あった và nối với のだった nhằm tổng kết, kể lại một sự kiện mang tính lịch sử đầy cảm xúc.",

    # part_79.csv
    r"\Thứ tự sắp xếp: 進捗報告 (báo cáo tiến độ) + 会議に (vào cuộc họp) -> tạo cụm danh từ chỉ mục đích; tiếp theo là động từ thể kính ngữ 出席される (tham dự); cuối cùng kết hợp với đuôi ngữ pháp のだろう + か để diễn tả sự suy đoán, tự hỏi về một sự việc trong công sở.\\":
    r"\Cụm danh từ chỉ mục đích 進捗報告 (báo cáo tiến độ) kết hợp với 会議に (vào cuộc họp). Tiếp theo, động từ thể kính ngữ 出席される (tham dự) gắn kết cùng đuôi ngữ pháp のだろうか để diễn tả sự suy đoán, tự hỏi về sự việc trong công sở.\\",
    
    r"\Thứ tự sắp xếp: 我が社の (của công ty chúng ta) bổ nghĩa cho danh từ 開発部で (tại phòng phát triển); tiếp theo là động từ thể bị động 却下された (bị bác bỏ/loại bỏ); kết thúc bằng cấu trúc nghi vấn tự hỏi のだろうか để tìm kiếm lý do tại sao một quyết định kinh doanh lại diễn ra.\\":
    r"\Định ngữ 我が社の (của công ty chúng ta) bổ nghĩa cho danh từ 開発部で (tại phòng phát triển). Nối tiếp là động từ thể bị động 却下された (bị bác bỏ), và câu khép lại bằng cấu trúc nghi vấn tự hỏi のだろうか để tìm hiểu lý do đưa ra quyết định.\\",
    
    r"\Thứ tự sắp xếp: Cụm từ chỉ lý do được cấu tạo bởi danh từ 社内会議が (có cuộc họp nội bộ) đi với động từ trang trọng ございます; sau đó nối bằng kính ngữ từ lý do の で,; tiếp theo là trạng từ bổ nghĩa cho hành động 折り返し (gọi lại ngay); cuối cùng là hành động khiêm nhường ngữ お電話いたします.\\":
    r"\Cụm lý do mở đầu bằng danh từ 社内会議が (có cuộc họp nội bộ) đi kèm động từ trang trọng ございます và từ nối nguyên nhân ので. Vế sau dùng trạng từ 折り返し (gọi lại ngay) bổ nghĩa cho hành động khiêm nhường ngữ お電話いたします.\\",
    
    r"\Thứ tự sắp xếp: Cụm danh từ 全社一丸 (toàn công ty như một thể thống nhất) bổ nghĩa cho danh từ kết hợp với động từ なった努力が (nỗ lực trở thành); tiếp đến là trạng từ và cụm động từ 実を結び、ついに (đơm hoa kết trái, cuối cùng thì); đi kèm tân ngữ 大口契約を (hợp đồng lớn); kết thúc bằng cấu trúc kể chuyện, nhấn mạnh thực tế trong quá khứ 獲得したのであった.\\":
    r"\Cụm danh từ 全社一丸 (toàn công ty như một thể thống nhất) bổ nghĩa cho cấu trúc なった努力が (những nỗ lực). Diễn biến tiếp nối bằng trạng từ và cụm động từ 実を結び、ついに (đơm hoa kết trái, cuối cùng thì), đi kèm tân ngữ 大口契約を (hợp đồng lớn), rồi chốt lại bằng cấu trúc kể chuyện 獲得したのであった.\\",
    
    r"\Thứ tự sắp xếp: Động từ nguyên dạng 築く (xây dựng) đi với cấu trúc ためには (để mà); tiếp theo là chủ ngữ của vế sau 迅速な対応が (sự ứng biến/phản hồi nhanh chóng); bổ nghĩa bằng trạng từ + tính từ đuôi na làm vị ngữ 最mも重要な (là quan trọng nhất); kết thúc bằng đuôi khẳng định/giải thích mang tính luận điểm のである.\\":
    r"\Động từ nguyên dạng 築く (xây dựng) đi với cấu trúc ためには (để mà) tạo thành vế mục đích. Vế sau bắt đầu bằng chủ ngữ 迅速な対応が (sự ứng biến nhanh chóng), được làm rõ qua vị ngữ 最も重要な (là quan trọng nhất) và kết thúc bằng đuôi khẳng định luận điểm のである.\\",
    
    r"\Thứ tự sắp xếp: Diễn giải nguyên nhân bắt đầu từ sự cố システムエラーが (lỗi hệ thống) thể liên dụng của động từ 発生し (phát sinh); tiếp theo là chủ ngữ kết quả メールの送信が (việc gửi email); đi kèm động từ dạng lỡ/tiếc nuối 遅れてしまった (đã bị muộn); kết thúc bằng のです để giải thích lý do một cách lịch sự cho khách hàng.\\":
    r"\Diễn giải nguyên nhân bắt đầu từ sự cố システムエラーが (lỗi hệ thống) với động từ 発生し (phát sinh). Kết quả theo sau là メールの送信が (việc gửi email) đi kèm động từ tiếc nuối 遅れてしまった (đã bị muộn), chốt bằng のです để giải thích lịch sự cho khách hàng.\\",
    
    r"\Thứ tự sắp xếp: Định ngữ 新商品の (của sản phẩm mới) bổ nghĩa cho tân ngữ 魅力を (sức hút); tiếp theo là trạng từ bổ nghĩa cho hành động 最大限に (ở mức tối đa); đi với động từ hành động アピールする (khẳng định, làm nổi bật); kết thúc bằng đuôi khẳng định mang tính chủ trương mạnh mẽ của tập thể のです.\\":
    r"\Định ngữ 新商品の (của sản phẩm mới) bổ trợ cho tân ngữ 魅力を (sức hút). Trạng từ 最大限に (ở mức tối đa) đi liền với động từ hành động アピールする (làm nổi bật) và khép lại bằng đuôi khẳng định chủ trương のです.\\",
    
    r"\Thứ tự sắp xếp: Cụm danh từ chủ đề 新製品の (về sản phẩm mới) kết hợp với danh từ 件 (vụ việc, vấn đề); đi kèm từ nối な (do 「件」 là danh từ) + のですが tạo thành tiền đề mồi đầu câu chuyện; tiếp theo là đại từ chỉ định và danh từ chỉ vật こちらが (đây là); kết thúc bằng kính ngữ 見積書でございます (bản báo giá).\\":
    r"\Cụm chủ đề 新製品の件 (vấn đề sản phẩm mới) đi kèm từ nối な và のですが để làm tiền đề mở đầu câu chuyện. Vế sau giới thiệu trực tiếp bằng đại từ こちらが (đây là) và kính ngữ 見積書でございます (bản báo giá).\\",
    
    r"\Thứ tự sắp xếp: Đại từ nghi vấn và định ngữ どちらの (đại lý nào) bổ nghĩa cho danh từ nơi chốn/phương tiện 旅行代理店で (tại đại lý du lịch); tiếp theo là động từ thể bị động kính ngữ 手配された (đã được sắp xếp/chuẩn bị); kết thúc bằng đuôi hỏi lịch sự, tìm kiếm thông tin のですか.\\":
    r"\Đại từ nghi vấn どちらの bổ nghĩa cho danh từ nơi chốn 旅行代理店で (tại đại lý du lịch nào). Theo sau đó là động từ bị động kính ngữ 手配された (được sắp xếp) và đuôi hỏi lịch sự のですか.\\",
    
    r"\Thứ tự sắp xếp: Tính từ 多い (nhiều) đi trực tiếp với đuôi điều kiện kết quả tiêu cực のでは (nếu tình trạng nhiều như thế này); vế sau bắt đầu bằng cụm bổ nghĩa định ngữ 納期に間に合わない (không kịp kỳ hạn giao hàng); bổ nghĩa cho danh từ 可能性が (khả năng); kết thúc bằng tính từ vị ngữ 高い (cao).\\":
    r"\Tính từ 多い (nhiều) nối trực tiếp với điều kiện kết quả tiêu cực のでは (nếu thế này). Vế sau có định ngữ 納期に間に合わない (không kịp kỳ hạn) bổ nghĩa cho danh từ 可能性が (khả năng), và khép lại bằng tính từ vị ngữ 高い (cao).\\",
    
    r"\Thứ tự sắp xếp: Chủ ngữ vế sau 予算案は (bản dự thảo ngân sách); đi kèm động từ thể bị động 承認された (đã được phê duyệt); kết hợp lần lượt với các phần tách nhỏ của đuôi phủ định nghi vấn mang tính lịch sự, dò hỏi nhẹ nhàng trong công sở: のでは + なかった + でしょうか.\\":
    r"\Chủ ngữ 予算案は (bản dự thảo ngân sách) đi cùng động từ thể bị động 承認された (đã được phê duyệt). Cụm này gắn kết trơn tru với đuôi phủ định nghi vấn のではなかったでしょうか nhằm dò hỏi nhẹ nhàng lịch sự.\\",
    
    r"\Thứ tự sắp xếp: Cụm trích dẫn hành động 報告すると (rằng sẽ báo cáo); bổ nghĩa bằng danh từ phương thức 報告ラインで (bằng tuyến báo cáo/quy trình báo cáo); đi kèm động từ thể quy định, trạng thái 定めていた (đã quy định); kết thúc bằng cấu trúc phán xét, khiển trách, nhắc nhở trách nhiệm のでは + なかったか.\\":
    r"\Cụm trích dẫn hành động 報告すると (rằng sẽ báo cáo) kết nối với danh từ phương thức 報告ラインで (bằng quy trình báo cáo). Động từ trạng thái 定めていた (đã quy định) kết thúc bằng cấu trúc phán xét trách nhiệm のではなかったか.\\",
    
    r"\Thứ tự sắp xếp: Cụm thời gian 入社1年目 (năm đầu tiên vào công ty) kết hợp danh từ + なのに (mặc dù mới là...); tiếp theo là cụm định ngữ chỉ mức độ ベテラン社員並みの (tương đương với nhân viên kỳ cựu) bổ nghĩa cho tân ngữ 売上を (doanh số); kết thúc bằng động từ trạng thái kết quả 達成している (đang đạt được).\\":
    r"\Cụm thời gian 入社1年目 kết hợp với なのに (mặc dù mới năm đầu). Vế tiếp theo dùng định ngữ chỉ mức độ ベテラン社員並みの (tương đương nhân viên kỳ cựu) để bổ trợ cho tân ngữ 売上を (doanh số), và khép lại bằng động từ trạng thái 達成している (đang đạt được).\\",
    
    r"\Thứ tự sắp xếp: Tính từ vế thứ nhất 安い (rẻ) kết hợp nối nghịch cảnh/đối lập のに,; vế thứ hai có chủ ngữ đối ứng 我が社のプランは (kế hoạch của công ty chúng ta); đi kèm cụm danh từ chủ điểm đối lập 保守管理費が (phí bảo trì quản lý); kết thúc bằng tính từ chỉ mức độ vượt ngưỡng 高すぎる (quá đắt).\\":
    r"\Tính từ 安い (rẻ) kết hợp từ nối nghịch cảnh のに. Vế đối lập sau đó đưa ra chủ ngữ 我が社のプランは (kế hoạch của chúng ta) với điểm nhấn 保守管理費が (phí bảo trì) và tính từ vượt ngưỡng 高すぎる (quá đắt).\\",
    
    r"\Thứ tự sắp xếp: Cụm động từ vế đầu 万全を期した (đã chuẩn bị hoàn hảo) đi trực tiếp với trợ từ biểu thị sự bất ngờ/trái mong đợi のに,; vế sau bắt đầu bằng trạng huống 本番のプレゼンで (tại buổi thuyết trình thực tế); đi kèm chủ ngữ sự cố 機材トラブルが (sự cố thiết bị); kết thúc bằng động từ ngoài ý muốn 起きてしまった (đã xảy ra mất rồi).\\":
    r"\Cụm động từ 万全を期した (đã chuẩn bị hoàn hảo) nối với trợ từ bất ngờ のに. Trạng huống đối lập 本番のプレゼンで (tại buổi thuyết trình thực tế) làm nền cho sự cố 機材トラブルが (sự cố thiết bị) và động từ ngoài ý muốn 起きてしまった (đã xảy ra mất rồi).\\",
    
    r"\Thứ tự sắp xếp: Cụm phó từ chỉ cách thức 慎重に (một cách thận trọng) bổ nghĩa cho cấu trúc tân ngữ 交渉を (cuộc đàm phán); đi kèm hành động duy trì, lặp lại từ quá khứ đến nay 重ねてきた (đã tích lũy, tiến hành nhiều lần); kết thúc lửng ở cuối câu bằng のに để thể hiện sự tiếc nuối, bất lực trước kết quả kinh doanh không như ý.\\":
    r"\Phó từ 慎重に (một cách thận trọng) bổ nghĩa cho cụm tân ngữ 交渉を (cuộc đàm phán). Hành động lặp lại 重ねてきた (tiến hành nhiều lần) kết thúc lửng bằng のに, qua đó thể hiện sự tiếc nuối, bất lực trước kết quả kinh doanh.\\",
    
    r"\Thứ tự sắp xếp: Cụm bổ nghĩa 役員向けの (dành cho ban giám đốc) bổ nghĩa cho tân ngữ 提案資料を (tài liệu đề xuất); đi kèm động từ thể quá khứ 完成させた (đã hoàn thành); kết hợp với trợ từ のに thể hiện sự uổng công (đi kèm 「せっかく」 ở đầu); kết thúc bằng cụm tình huống đáng tiếc ở vế sau 延期になってしまった (đã bị hoãn mất rồi).\\":
    r"\Cụm bổ nghĩa 役員向けの (dành cho ban giám đốc) bổ trợ cho tân ngữ 提案資料を (tài liệu đề xuất). Động từ quá khứ 完成させた (đã hoàn thành) kết hợp với trợ từ のに nhằm nhấn mạnh sự uổng công, dẫn tới kết cục đáng tiếc 延期になってしまった (đã bị hoãn).\\",

    # part_80.csv
    "[計算するのに] là cấu trúc [V-るのに] biểu thị mục đích, kết hợp với [役立ちます] (có ích). Thứ tự tự nhiên: bổ ngữ cho danh từ (新規プロジェクトの) -> danh từ trung tâm (予算を) -> hành động mục đích (計算するのに) -> phó từ (非常に) -> động từ chính.":
    "[計算するのに] là cấu trúc [V-るのに] biểu thị mục đích, kết hợp với [役立ちます] (có ích). Logic câu đi từ bổ ngữ (新規プロジェクトの), đến danh từ (予算を), gắn với hành động mục đích (計算するのに), và kết thúc bằng phó từ (非常に) bổ nghĩa cho động từ chính."
}

for i in range(71, 81):
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

print("Batch 15 and 16 manually reviewed and rewritten successfully!")
