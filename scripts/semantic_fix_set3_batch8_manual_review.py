import csv, os

dir_path = r'd:\pj\xx\ai-gen-quiz\mondai2_ordering\csv_filled\set_3_academic'

rewrites = {
    # part_37.csv
    "Cấu trúc biểu thị việc thực hiện hành động một cách cẩn thận, chuẩn chỉ, không sai sót (「ちゃんと」). Thứ tự tự nhiên của câu: Trạng ngữ chỉ thời gian (「明日の会議の前に、」) -> Tân ngữ chịu tác động (「この大切な資料を」) -> Mục đích/Trạng thái (「ミスがないように」) -> Phó từ (「ちゃんと」) -> Động từ chia thể て đi liền với cấu trúc chuẩn bị trước (「確認しておいてください。」).":
    "Cấu trúc này dùng phó từ 「ちゃんと」 để biểu thị việc thực hiện hành động một cách cẩn thận, không sai sót. Mạch câu được triển khai một cách tự nhiên: khởi đầu bằng trạng ngữ chỉ thời gian 「明日の会議の前に、」, tiếp đến là tân ngữ chịu tác động 「この大切な資料を」, theo sau là mục đích 「ミスがないように」, và cuối cùng là phó từ 「ちゃんと」 bổ nghĩa trực tiếp cho động từ 「確認しておいてください。」.",
    
    "Hậu tố 「中（ちゅう）」 gắn sau danh từ hành động để chỉ một trạng thái đang diễn ra (「来客中」: đang tiếp khách). Thứ tự kết hợp logic: Chủ ngữ (「社長は」) -> Phó từ thời gian trang trọng lịch sự (「ただいま」) -> Mệnh đề chỉ lý do nguyên nhân (「来客中ですので、」) -> Trạng ngữ chỉ địa điểm (「受付のソファで」) -> Lượng từ/phó từ mức độ (「少々」) -> Cấu trúc kính ngữ cầu khiến tôn kính (「お待ちください。」).":
    "Hậu tố 「中（ちゅう）」 gắn sau danh từ hành động để chỉ một trạng thái đang diễn ra (ví dụ 「来客中」 là đang tiếp khách). Các thành phần trong câu được liên kết logic với nhau: bắt đầu từ chủ ngữ 「社長は」, đi kèm phó từ thời gian lịch sự 「ただいま」 và mệnh đề chỉ nguyên nhân 「来客中ですので、」. Tiếp nối là trạng ngữ chỉ địa điểm 「受付のソファで」, rồi đến phó từ mức độ 「少々」 bổ nghĩa cho cấu trúc kính ngữ cầu khiến 「お待ちください。」.",
    
    "Hậu tố 「中（ちゅう・じゅう）」 khi đi sau danh từ chỉ thời gian mang nghĩa là 「trong phạm vi thời hạn/khoảng thời gian đó」 (「今週中」: trong tuần này). Thứ tự các thành phần câu: Cụm danh từ làm chủ đề (「新しいプロジェクトの企画書は、」) -> Thời hạn thực hiện (「今週中には」) -> Cách thức bắt buộc (「必ずメールで」) -> Động từ làm định ngữ (「提出する」) bổ nghĩa cho danh từ kết thúc chỉ kế hoạch (「予定です。」).":
    "Hậu tố 「中（ちゅう・じゅう）」 đứng sau danh từ chỉ thời gian để biểu thị ý nghĩa 「trong phạm vi khoảng thời gian đó」 (ví dụ 「今週中」 là trong tuần này). Về mặt cấu trúc, cụm danh từ làm chủ đề 「新しいプロジェクトの企画書は、」 sẽ đi liền với thời hạn 「今週中には」 và cách thức bắt buộc 「必ずメールで」. Sau đó, động từ định ngữ 「提出する」 sẽ bổ nghĩa trực tiếp cho danh từ kết thúc câu 「予定です。」.",
    
    "Phó từ 「ちょっと」 dùng để chỉ mức độ nhẹ nhàng hoặc số lượng nhỏ (「một chút」). Thứ tự sắp xếp câu: Khởi đầu bằng lời xin lỗi (「すみません、」) -> Chủ ngữ (「私は」) -> Trạng ngữ thời gian và phó từ mức độ (「今ちょっと」) -> Tính từ mang đuôi chỉ nguyên nhân (「忙しいですから、」) -> Thời điểm tiếp theo (「後で」) -> Động từ hành động kết thúc (「電話します。」).":
    "Phó từ 「ちょっと」 được dùng để chỉ mức độ nhẹ nhàng hoặc số lượng nhỏ (một chút). Câu văn được sắp xếp khéo léo bắt đầu bằng lời xin lỗi 「すみません、」 và chủ ngữ 「私は」. Kế tiếp là cụm trạng ngữ 「今ちょっと」 đi liền với nguyên nhân 「忙しいですから、」, dẫn dắt tự nhiên đến mốc thời gian 「後で」 và kết thúc bằng hành động 「電話します。」.",
    
    "Phó từ 「ちょっと」 đặt trước động từ nhằm giảm bớt sự đường đột, làm giảm nhẹ mức độ của hành động hoặc lời nhờ vả để tăng tính lịch sự. Thứ tự câu: Gọi tên đối tượng (「田中さん、」) -> Mệnh đề định ngữ (「机の上にある」) bổ nghĩa cho tân ngữ (「その資料を」) -> Phó từ giảm nhẹ (「ちょっと」) -> Người tiếp nhận (「私に」) -> Động từ cầu khiến (「見せてください。」).":
    "Đặt phó từ 「ちょっと」 trước động từ giúp giảm bớt sự đường đột và tăng độ lịch sự cho lời nhờ vả. Mạch câu đi từ lời gọi tên đối tượng 「田中さん、」, nối với mệnh đề định ngữ 「机の上にある」 bổ nghĩa cho tân ngữ 「その資料を」. Tiếp đó, phó từ giảm nhẹ 「ちょっと」 và đại từ 「私に」 được đặt ngay trước động từ cầu khiến 「見せてください。」 để tạo sự mềm mại.",
    
    "Phó từ 「ちょっと」 đứng trước tính từ tiêu cực (「難しい」) nhằm nói giảm nói tránh, làm dịu giọng điệu nhận xét trong công sở để không làm mất lòng đồng nghiệp. Thứ tự cú pháp: Mệnh đề phụ bổ nghĩa (「木村さんが書いた」) gắn vào cụm danh từ chủ đề (「メールの日本語は、」) -> Phó từ giảm nhẹ giọng điệu (「ちょっと」) -> Tính từ tâm điểm (「難しい」) -> Vĩ từ cảm thán (「ですね。」) và câu phản hồi của đối phương.":
    "Khi đứng trước tính từ tiêu cực như 「難しい」, phó từ 「ちょっと」 có tác dụng nói giảm nói tránh, làm dịu đi nhận xét để giữ hòa khí nơi công sở. Cấu trúc câu bắt đầu bằng cụm chủ đề 「メールの日本語は、」 (được bổ nghĩa bởi mệnh đề 「木村さんが書いた」), sau đó phó từ 「ちょっと」 làm mềm đi tính từ 「難しい」, và kết thúc trọn vẹn bằng vĩ từ cảm thán 「ですね。」.",
    
    "Cách nói bỏ lửng 「ちょっと…」 là một hình thức từ chối khéo léo, tế nhị vô cùng đặc trưng và quan trọng trong môi trường công sở Nhật Bản. Thứ tự hội thoại logic: Lời dẫn dắt (「急な仕事ですが、」) -> Cụm thời gian định ngữ (「今週の土曜日に」) -> Câu hỏi khả năng hành động (「出勤できますか。」) -> Câu trả lời đưa mốc thời gian làm chủ đề nhấn mạnh (「B：土曜日は」) và kết thúc bằng phó từ lửng.":
    "Việc bỏ lửng câu bằng 「ちょっと…」 là hình thức từ chối khéo léo cực kỳ đặc trưng nơi công sở Nhật Bản. Hội thoại diễn tiến logic khi lời dẫn dắt 「急な仕事ですが、」 đi cùng mốc thời gian 「今週の土曜日に」 để đặt câu hỏi 「出勤できますか。」. Đáp lại, người nghe lấy ngay mốc thời gian đó làm chủ đề nhấn mạnh 「土曜日は」 rồi kết thúc nhẹ nhàng bằng phó từ lửng.",
    
    "Phó từ 「ちょっと」 khi đi kèm với một tính từ mang nghĩa tích cực (「面白い」) sẽ mang sắc thái nhấn mạnh, đánh giá cao (「khá là」, 「không phải dạng vừa đâu」). Thứ tự tự nhiên: Chủ ngữ mệnh đề định ngữ (「鈴木さんが」) -> Cụm động từ bổ nghĩa (「会議で提案した」) bổ sung ý nghĩa cho chủ đề câu (「新しいアイデアは、」) -> Phó từ đánh giá (「ちょっと」) -> Tính từ (「面白い」) -> Đuôi câu đồng tình (「ですね。」).":
    "Khi kết hợp với tính từ mang nghĩa tích cực như 「面白い」, phó từ 「ちょっと」 lại mang sắc thái đánh giá cao (nghĩa là \"khá là\" hay \"không đùa được đâu\"). Sự liên kết trong câu diễn ra rất tự nhiên: mệnh đề định ngữ 「鈴木さんが会議で提案した」 bổ sung ý nghĩa cho chủ đề 「新しいアイデアは、」, tiếp nối bằng phó từ đánh giá 「ちょっと」, tính từ 「面白い」 và kết thúc bằng vĩ từ đồng tình 「ですね。」.",
    
    "Cấu trúc 「ちょっと～ない」 đi với thể phủ định mang nghĩa là 「hiếm có」, 「không dễ gì tìm được」, dùng để khen ngợi mức độ xuất sắc của sự vật. Thứ tự từ: Định ngữ sở hữu (「佐藤さんの」) -> Cụm tính từ chỉ mức độ cao (「これほど素晴らしい」) bổ nghĩa cho danh từ chủ đề (「企画書は、」) -> Trạng từ thời gian (「最近」) -> Phó từ đi kèm phủ định (「ちょっと」) -> Động từ phủ định trang trọng (「ありません。」).":
    "Cấu trúc 「ちょっと～ない」 ở thể phủ định diễn tả sự \"hiếm có\", \"không dễ gì tìm được\", dùng để khen ngợi mức độ xuất sắc. Mạch câu tiến triển bằng cách dùng định ngữ sở hữu 「佐藤さんの」 và cụm từ chỉ mức độ 「これほど素晴らしい」 bổ nghĩa cho chủ đề 「企画書は、」. Trạng từ thời gian 「最近」 đi cùng phó từ 「ちょっと」 sẽ bổ nghĩa cho động từ phủ định trang trọng 「ありません。」 ở cuối câu.",
    
    "Cấu trúc 「ちょっと～ない」 phối hợp để làm nhẹ sắc thái của lời từ chối hoặc thừa nhận sự thiếu sót của bản thân, thể hiện sự lịch sự khi không thể đáp ứng thông tin. Thứ tự: Gọi tên cấp trên (「A：鈴木部長、」) -> Tân ngữ chủ đề của câu hỏi (「他社との契約書はどこですか。」) -> Lời xin lỗi của người phản hồi (「B：すみません、」) -> Đại từ nhân xưng đi kèm phó từ giới hạn (「私にはちょっと」) -> Động từ phủ định kết thúc (「わかりません。」).":
    "Cấu trúc 「ちょっと～ない」 còn giúp làm nhẹ sắc thái của lời từ chối hoặc thừa nhận sự thiếu sót, mang lại vẻ lịch sự khi ta không nắm rõ thông tin. Các phần của câu được kết nối bằng cách gọi tên cấp trên 「鈴木部長、」 rồi đặt câu hỏi 「他社との契約書はどこですか。」. Người đáp mở lời xin lỗi 「すみません、」, sau đó dùng đại từ nhân xưng kèm phó từ giới hạn 「私にはちょっと」 để dẫn vào động từ phủ định 「わかりません。」.",
    
    "Thán từ 「ちょっと」 đứng đầu câu dùng để gọi, gây sự chú ý với người nghe một cách nhẹ nhàng, thường dùng giữa đồng nghiệp thân thiết hoặc cấp trên gọi cấp dưới (君). Thứ tự sắp xếp câu: Thán từ gọi (「ちょっと、」) -> Tên người nhận lời gọi (「木村君、」) -> Tân ngữ chịu tác động (「この会議の資料を」) -> Lượng từ ước lượng (「5部ほど」) -> Động từ cầu khiến hành động (「コピーしてください。」).":
    "Thán từ 「ちょっと」 đứng đầu câu có tác dụng gọi và gây chú ý nhẹ nhàng, thường dùng giữa đồng nghiệp thân thiết hoặc cấp trên gọi cấp dưới. Mạch câu diễn tiến rất quen thuộc: Thán từ gọi 「ちょっと、」 đi liền với tên người nghe 「木村君、」, tiếp nối bằng tân ngữ 「この会議の資料を」 và lượng từ 「5部ほど」 trước khi đưa ra yêu cầu cụ thể bằng động từ 「コピーしてください。」.",
    
    "Cụm từ 「ちょっとした + Danh từ」 dùng để chỉ những việc nhỏ nhặt, không có gì to tát nhằm làm nhẹ bớt tính chất vấn đề ban đầu. Thứ tự ngữ pháp: Trạng ngữ nơi chốn bổ nghĩa (「社内での」) -> Cụm từ định ngữ (「ちょっとした」) bổ nghĩa cho cụm danh từ chủ ngữ (「連絡のミスが、」) -> Cụm danh từ kết quả biến đổi (「大きなトラブルに」) -> Động từ biểu thị kết quả đáng tiếc (「なってしまいました。」).":
    "Cụm từ 「ちょっとした + Danh từ」 dùng để chỉ những việc nhỏ nhặt, không có gì to tát nhằm làm nhẹ bớt tính chất của vấn đề. Xét về cấu trúc, trạng ngữ nơi chốn 「社内での」 và định ngữ 「ちょっとした」 cùng bổ nghĩa cho chủ ngữ 「連絡のミスが、」. Kế tiếp là cụm chỉ kết quả 「大きなトラブルに」 và động từ biểu thị kết cục đáng tiếc 「なってしまいました。」.",
    
    "Cụm từ 「ちょっとした + Danh từ」 ở đây mang ý nghĩa tích cực, biểu thị mức độ khá lớn, đáng kể, không thể coi thường. Thứ tự kết hợp câu: Mệnh đề phụ định ngữ thời gian (「先月発売された」) -> Định ngữ sở hữu (「弊社の」) -> Cụm từ chủ đề (「新しい製品は、」) -> Trạng ngữ địa điểm kết hợp cụm bổ nghĩa mức độ (「市場でちょっとした」) -> Danh từ mục tiêu (「ブームに」) -> Động từ trạng thái kéo dài (「なっています。」).":
    "Khi mang ý nghĩa tích cực, 「ちょっとした + Danh từ」 biểu thị mức độ đáng kể và không thể xem nhẹ. Sự kết hợp các phần trong câu rất logic: mệnh đề định ngữ thời gian 「先月発売された」 và định ngữ sở hữu 「弊社の」 làm rõ cho chủ đề 「新しい製品は、」. Phần sau của câu là trạng ngữ địa điểm 「市場でちょっとした」 bổ nghĩa trực tiếp cho danh từ mục tiêu 「ブームに」 và động từ trạng thái 「なっています。」.",
    
    "Mẫu ngữ pháp 「V1(Stem)つV2(Stem)つ」 biểu thị hai hành động đối lập diễn ra luân phiên liên tục hoặc một trạng thái giằng co gay gắt. Cụm 「抜きつ抜かれつ」 mang nghĩa vượt lên rồi lại bị vượt qua. Thứ tự câu: Định ngữ (「今回の」) -> Trạng ngữ phạm vi sự kiện (「大型プロジェクトの入札では、」) -> Đối tượng đối phó (「ライバル企業と」) -> Trạng từ thời gian (「最後まで」) -> Cụm ngữ pháp đóng vai trò tính từ bổ nghĩa (「抜きつ抜かれつの」) -> Cụm danh động từ kết thúc (「激しい競争となりました。」).":
    "Cấu trúc 「V1(Stem)つV2(Stem)つ」 biểu thị hai hành động đối lập diễn ra luân phiên liên tục, ví dụ cụm 「抜きつ抜かれつ」 nghĩa là vượt lên rồi lại bị vượt qua. Mạch câu bắt đầu từ định ngữ 「今回の」 đi với phạm vi sự kiện 「大型プロジェクトの入札では、」, nối với đối tượng 「ライバル企業と」 và thời gian 「最後まで」. Sau đó, cụm cấu trúc 「抜きつ抜かれつの」 bổ nghĩa ngay cho danh động từ kết thúc câu 「激しい競争となりました。」.",
    
    "Phó từ 「つい」 diễn tả một hành động lỡ xảy ra ngoài ý muốn hoặc vô ý thức do một trạng thái tâm lý/sức khỏe thúc đẩy, thường đi kèm đuôi câu 「～てしまう」. Thứ tự logic: Trạng ngữ chỉ nguyên nhân gốc (「連日の残業で」) -> Vế câu chỉ lý do trực tiếp (「大変疲れていたので、」) -> Trạng ngữ thời gian (「重要な会議中に」) -> Phó từ đứng ngay trước cụm hành động (「つい居眠りを」) -> Động từ thể hiện sự hối tiếc (「してしまった。」).":
    "Phó từ 「つい」 diễn tả một hành động lỡ xảy ra ngoài ý muốn do tâm lý hoặc sức khỏe thúc đẩy, thường đi kèm đuôi câu 「～てしまう」. Mạch diễn tiến logic bắt đầu từ nguyên nhân gốc 「連日の残業で」 dẫn tới lý do trực tiếp 「大変疲れていたので、」. Bối cảnh 「重要な会議中に」 được đặt trước phó từ 「つい居眠りを」 để nhấn mạnh sự vô tình, cuối cùng khép lại bằng động từ thể hiện sự hối tiếc 「してしまった。」.",
    
    "Liên từ 「ついでに」 đứng ở đầu câu thứ hai, mang nghĩa 「nhân tiện, tiện thể」, dùng để kết nối một hành động phụ phát sinh thuận đường với hành động chính ở câu thứ nhất. Thứ tự sắp xếp: Trạng từ thời gian (「午後から」) -> Cụm tân ngữ hành động chính (「郵便局へ契約書を」) -> Kết thúc câu thứ nhất (「出しに行きました。」) -> Liên từ nối (「ついでに、」) -> Địa điểm hành động phụ (「近くの銀行で」) -> Hoàn thành hành động phụ (「用事も済ませてきました。」).":
    "Liên từ 「ついでに」 đứng đầu câu thứ hai mang nghĩa \"nhân tiện\", dùng để kết nối một hành động phụ phát sinh thuận đường với hành động chính. Câu mở đầu trình bày hành động chính từ thời gian 「午後から」, tân ngữ 「郵便局へ契約書を」 và động từ 「出しに行きました。」. Liên từ 「ついでに、」 đóng vai trò cầu nối mượt mà sang địa điểm phụ 「近くの銀行で」 để hoàn thành hành động tiếp theo 「用事も済ませてきました。」.",
    
    "Cấu trúc 「V-る + ついでに」 dùng để lồng ghép hành động phụ vào một cơ hội hay một lộ trình của hành động chính có sẵn. Thứ tự cú pháp: Trạng từ thời gian tương lai (「来週」) -> Mệnh đề định ngữ chỉ hành động chính (「東京へ出張する」) -> Danh từ ngữ pháp chỉ sự nhân tiện (「ついでに、」) -> Đối tượng hướng tới của hành động phụ (「現地の取引先にも」) -> Mục đích hành động phụ gắn với cấu trúc kế hoạch (「挨拶に行く予定です。」).":
    "Cấu trúc 「V-る + ついでに」 lồng ghép hành động phụ vào lộ trình của một hành động chính có sẵn. Mạch liên kết đi từ trạng từ thời gian 「来週」, ghép với định ngữ hành động chính 「東京へ出張する」 và danh từ nhân tiện 「ついでに、」. Đối tượng phụ 「現地の取引先にも」 được đặt trước mục đích cuối cùng mang tính kế hoạch 「挨拶に行く予定です。」.",
    
    "Liên từ 「ついては」 mang tính chất trang trọng cao, dùng phổ biến trong thư tín thương mại, email kinh doanh với nghĩa 「về việc đó/chính vì lý do đó cho nên...」, mở đầu cho một đề xuất hoặc yêu cầu dựa trên bối cảnh đã nêu ở câu trước. Thứ tự câu: Thời gian (「来月、」) -> Sự tình dẫn nhập (「弊社は創立10周年を」 + 「迎えることとなりました。」) -> Liên từ trang trọng đầu câu hai (「ついては、」) -> Tân ngữ hành động tiếp sau (「記念パーティーを」) -> Vế kết quả kính ngữ thể hiện mong muốn (「開催いたしますので、ご出席いただけますと幸いです。」).":
    "Liên từ 「ついては」 mang sắc thái trang trọng, thường dùng trong email kinh doanh với nghĩa \"về việc đó cho nên...\", dùng để mở đầu một yêu cầu sau khi đã nêu bối cảnh. Cấu trúc câu triển khai từ mốc thời gian 「来月、」 và sự tình dẫn nhập 「弊社は創立10周年を迎えることとなりました。」. Liên từ 「ついては、」 sẽ chuyển hướng mượt mà sang tân ngữ 「記念パーティーを」 và kết thúc bằng vế kính ngữ mong mỏi 「開催いたしますので、ご出席いただけますと幸いです。」.",
    
    "Phó từ 「ついに」 diễn tả một kết quả cuối cùng đã đạt được, một cái đích đã chạm tới sau khi trải qua một quá trình dài nỗ lực, kiên trì, thường đi với thể quá khứ 「～た」. Thứ tự các thành phần: Đối tượng phối hợp hành động (「他社と何ヶ月も」) -> Hành động tích lũy (「交渉を重ねた」) -> Danh từ chỉ hệ quả (「結果、」) -> Phó từ nhấn mạnh kết cục (「ついに」) -> Chủ ngữ chịu tác động (「念願の新しい契約が」) -> Động từ kết thúc (「成立しました。」).":
    "Phó từ 「ついに」 diễn tả một kết quả đạt được sau cả quá trình dài nỗ lực và thường đi với thể quá khứ. Mạch câu xuất phát từ đối tượng và thời gian phối hợp 「他社と何ヶ月も」, gắn với hành động tích lũy 「交渉を重ねた」 và hệ quả 「結果、」. Phó từ 「ついに」 đóng vai trò nhấn mạnh kết cục, làm tiền đề cho cụm chủ-vị kết thúc 「念願の新しい契約が成立しました。」.",
    
    "Cấu trúc 「ついに + Động từ thể phủ định (～なかった)」 diễn tả một kết cục đáng tiếc, dù đã cố gắng hết sức hoặc đợi chờ rất lâu nhưng kết quả mong muốn cuối cùng đã không xảy ra. Thứ tự cú pháp: Trạng từ mức độ (「最後まで」) -> Tính từ bổ nghĩa cách thức (「粘り強く」) -> Vế câu hành động đối lập (「交渉を続けたが、」) -> Chủ đề câu phủ định (「先方の同意は」) -> Phó từ nhấn mạnh trạng thái phủ định (「ついに」) -> Động từ khả năng phủ định kết thúc (「得られませんでした。」).":
    "Cấu trúc 「ついに + Động từ phủ định」 lại diễn tả một kết cục đáng tiếc khi kết quả mong muốn không xảy ra dù đã rất cố gắng. Câu được diễn đạt theo mạch đi từ trạng từ mức độ 「最後まで」 và cách thức kiên trì 「粘り強く」, ghép với hành động đối lập 「交渉を続けたが、」. Sau đó, chủ đề 「先方の同意は」 đi liền với phó từ nhấn mạnh 「ついに」, báo hiệu cho sự nuối tiếc ở động từ phủ định 「得られませんでした。」.",
    
    # part_39.csv
    "Tân ngữ 「資料を」 đi với động từ chia thể て là 「印刷して」 để nối tiếp hành động theo trình tự thời gian. Vế tiếp theo bắt đầu bằng đối tượng nhận 「部長に」, phó từ 「すぐ」 và kết thúc bằng mẫu câu cầu khiến lịch sự 「渡してください」.":
    "Tân ngữ 「資料を」 đi cùng động từ chia thể て 「印刷して」 giúp tạo sự nối tiếp hành động mượt mà. Vế phía sau diễn tiến rất tự nhiên khi bắt đầu bằng đối tượng nhận 「部長に」, đi kèm phó từ 「すぐ」 và khép lại bằng mẫu câu cầu khiến lịch sự 「渡してください」."
}

for i in range(36, 41):
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
        
        # Check against dictionary of complete sentences to replace
        for orig, new_val in rewrites.items():
            if orig in exp:
                exp = exp.replace(orig, new_val)
                row[exp_idx] = exp
                changed = True
                
    if changed:
        with open(path, 'w', encoding='utf-8-sig', newline='') as f:
            csv.writer(f).writerows(r)

print("Batch 8 manually reviewed and rewritten successfully!")
