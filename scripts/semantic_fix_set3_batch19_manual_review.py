import csv, os

dir_path = r'd:\pj\xx\ai-gen-quiz\mondai2_ordering\csv_filled\set_3_academic'

rewrites = {
    # part_91.csv
    "Câu mô tả lịch trình họp công sở. Trợ từ chỉ thời hạn 「まで」(đến lúc) đi sau danh từ chỉ thời gian 「午後5時」. Trình tự logic: Chủ ngữ cuộc họp 「本日の会議は」 -> mốc thời gian giới hạn 「午後5時まで」 -> cụm trạng ngữ địa điểm 「執務室で」(tại văn phòng làm việc) -> động từ thể bị động trang trọng 「行われます」(được tổ chức).":
    "Câu mô tả lịch trình họp công sở. Logic bắt đầu bằng chủ ngữ cuộc họp 「本日の会議は」. Tiếp theo, mốc thời gian 「午後5時まで」 (đến 5 giờ chiều) kết hợp cùng trạng ngữ địa điểm 「執務室で」 (tại văn phòng làm việc). Động từ thể bị động trang trọng 「行われます」 (được tổ chức) khép lại câu.",
    
    "Cấu trúc 「V-るまでもない」 nghĩa là 「không cần thiết phải làm V (vì quá đơn giản hoặc hiển nhiên)」. Trình tự logic: Đưa ra giả định mức độ nhẹ 「この程度の軽微なバグなら」 -> phó từ nhấn mạnh sự cất công vô ích 「わざわざ」 -> hành động sửa tài liệu 「仕様書を修正する」 đi kèm dạng từ điển kết hợp trực tiếp với đuôi 「までもありません」.":
    "Cấu trúc 「V-るまでもない」 biểu thị việc không cần thiết phải làm V. Câu dẫn nhập bằng giả định mức độ nhẹ 「この程度の軽微なバグなら」 (nếu chỉ là lỗi nhẹ cỡ này). Phó từ 「わざわざ」 nhấn mạnh sự vô ích khi kết nối với hành động 「仕様書を修正する」 và vĩ tố 「までもありません」 (không cần cất công sửa).",
    
    "Cấu trúc 「V-られるがままに」 thể hiện sự nhu nhược, hoàn toàn tuân theo ý muốn hay sự sắp đặt của đối tác thương mại mà không có chủ kiến. Ở đây dùng dạng bị động 「言われる」(bị nói/yêu cầu) kết hợp với 「がままに」. Trình tự logic: Chủ thể tác động 「先方の担当者に」 -> Trạng thái bị động cuốn theo 「言われるがままに」 -> cách thức bất lợi 「不利な条件で」 -> hành động cấm đoán 「合意してはいけません」.":
    "Cấu trúc 「V-られるがままに」 thể hiện sự nhu nhược, hoàn toàn tuân theo đối tác. Chủ thể tác động 「先方の担当者に」 gắn liền trạng thái bị động 「言われるがままに」 (cứ để họ nói sao nghe vậy). Việc này dẫn đến điều kiện bất lợi 「不利な条件で」 và kết thúc bằng lời cấm đoán 「合意してはいけません」 (không được đồng ý).",

    # part_92.csv
    "Trạng từ 「まもなく」 (sắp sửa, chẳng mấy chốc) đứng đầu mệnh đề để bổ nghĩa cho hành động sắp diễn ra. 「弊社の」 đóng vai trò định ngữ sở hữu bổ nghĩa cho danh từ chỉ sự kiện 「新商品発表会」. Trợ từ 「が」 đi sau danh từ chỉ chủ ngữ cho tự động từ 「始まります」. Do đó, thứ tự logic tự nhiên từ trái qua phải là: まもなく -> 弊社の -> 新商品発表会が -> 始まります。":
    "Trạng từ 「まもなく」 (chẳng mấy chốc) đứng đầu bổ nghĩa cho hành động sắp diễn ra. Định ngữ sở hữu 「弊社の」 bổ trợ cho sự kiện 「新商品発表会」. Cụm chủ ngữ này kết hợp cùng tự động từ 「始まります」 để báo hiệu việc bắt đầu.",
    
    "Cấu trúc so sánh ví von 「まるで～のようだ」 (nhìn hệt như là...). Trạng từ 「まるで」 luôn đứng đầu cụm so sánh để nhấn mạnh mức độ. Tiếp theo là danh từ phụ thuộc sở hữu 「ホテルの」 bổ nghĩa cho 「ロビー」. Thêm trợ từ 「の」 để liên kết danh từ 「ロビー」 với phán đoán 「ようです」. Thứ tự tự nhiên là: まるで -> ホテルの -> ロビーの -> ようです。":
    "Trạng từ 「まるで」 đứng đầu để nhấn mạnh cấu trúc so sánh ví von 「まるで～のようだ」 (hệt như là). Kế đến, danh từ sở hữu 「ホテルの」 bổ nghĩa cho 「ロビー」. Trợ từ 「の」 khéo léo kết nối danh từ này với phán đoán 「ようです」.",
    
    "Cấu trúc phủ định hoàn toàn mang tính nhấn mạnh 「まるで～ない」 (hoàn toàn không...). Trạng từ 「まるで」 đứng trước để bổ nghĩa cho vị ngữ phủ định. Cụm từ phủ định 「何も聞いていない」 (chưa nghe bất kỳ điều gì) đi sau cùng. Trong đó 「何も」 bổ trợ thêm cho ý nghĩa phủ định của động từ 「聞いていない」. Do đó, thứ tự tự nhiên là: 私は -> まるで -> 何も -> 聞いていない。":
    "Trạng từ 「まるで」 đứng trước bổ nghĩa cho vị ngữ phủ định, làm nổi bật cấu trúc 「まるで～ない」 (hoàn toàn không). Đại từ 「何も」 tăng thêm mức độ phủ định cho động từ 「聞いていない」 (chưa nghe thấy gì), khép lại câu văn.",
    
    "Cấu trúc phủ định kép mang tính giảm nhẹ khẳng định 「まんざら～ない/でもない」 (không hẳn là hoàn toàn tệ/không hoàn toàn...). Trạng từ 「まんざら」 đứng trước tính từ phủ định phủ nhận nhẹ nhàng 「悪くもない」 (cũng không phải là tệ). Cụm bổ ngữ này bổ nghĩa trực tiếp cho danh từ 「交渉結果」. Trợ từ liên kết 「と」 đứng sau danh từ để kết hợp với động từ truyền đạt phát ngôn 「言えます」. Thứ tự tự nhiên là: 我が社にとって -> まんざら -> 悪くもない -> 交渉結果と。":
    "Trạng từ 「まんざら」 đứng trước tính từ 「悪くもない」 (cũng không tệ), tạo thành cụm phủ định kép nhằm khẳng định nhẹ nhàng. Cụm này bổ nghĩa trực tiếp cho 「交渉結果」 (kết quả đàm phán). Trợ từ 「と」 liên kết tân ngữ với động từ truyền đạt 「言えます」 (có thể nói là).",
    
    r"Cụm quán dung từ 「まんざらでもない」 đứng trước danh từ với vai trò bổ nghĩa, mang nghĩa là \「không hề ghét/khá hài lòng/hớn hở ra mặt\」. Trong câu này, nó bổ nghĩa trực tiếp cho danh từ tân ngữ 「表情」. Trợ từ 「を」 kết nối tân ngữ với động từ thể hiện biểu cảm 「浮かべていました」. Do đó, thứ tự cú pháp logic là: 彼は -> まんざらでもない -> 表情を -> 浮かべて。":
    "Cụm quán dụng ngữ 「まんざらでもない」 (khá hài lòng, hớn hở) đóng vai trò bổ nghĩa trực tiếp cho tân ngữ 「表情」 (biểu cảm). Trợ từ 「を」 sau đó kết nối tân ngữ này với động từ 「浮かべていました」 (lộ rõ trên mặt).",
    
    "Trạng từ 「まんまと」 (trơn tru, ngọt xớt, lọt bẫy hoàn hảo) thường đi kèm với các động từ thể hiện kết quả tiêu cực, bị lừa dối như 「乗せられる」 (bị dắt mũi, bị lừa gạt). Động từ bị động dạng liên kết 「乗せられて」 đi liền trước cấu trúc chỉ kết quả ngoài ý muốn 「しまう」 (ở dạng quá khứ 「しまった」). Do đó, thứ tự tự nhiên là: 我々は -> まんまと -> 乗せられて -> しまった。":
    "Trạng từ 「まんまと」 (lọt bẫy hoàn hảo, trơn tru) thường đi kèm các động từ tiêu cực như 「乗せられる」 (bị dắt mũi). Thể liên kết 「乗せられて」 đi liền với trợ động từ chỉ sự nuối tiếc 「しまった」 (mất rồi) để nhấn mạnh hậu quả ngoài ý muốn.",
    
    "Cấu trúc phán đoán trạng thái dựa trên vẻ bề ngoài 「～そうに見える」 (trông có vẻ như...). Động từ phức 「分かりやすい」 (dễ hiểu) bỏ 「い」 thêm 「そうに」 đi kèm với 「見える」 tạo thành cụm từ 「分かりやすそうに見える」. Trạng từ bổ nghĩa mức độ 「とても」 đứng trước toàn bộ cụm này. Chỉ định từ 「この」 bổ nghĩa cho danh từ chủ ngữ 「グラフは」. Thứ tự tự nhiên là: この -> グラフは -> とても -> 分かりやすそうに見える。":
    "Động từ phức 「分かりやすい」 bỏ 「い」 thêm 「そうに」 và kết nối với 「見える」 tạo thành cụm phán đoán 「分かりやすそうに見える」 (trông có vẻ dễ hiểu). Trạng từ mức độ 「とても」 (rất) đứng trước bổ trợ cho toàn cụm, trong khi chỉ định từ 「この」 bổ nghĩa cho chủ ngữ 「グラフは」.",
    
    "Cấu trúc so sánh giả định biểu hiện trạng thái 「V-thông thường + かのように見える」 (nhìn hệt như thể là...). Ở đây động từ thể từ điển 「進む」 kết hợp với 「かのように見えた」. Trạng từ bổ nghĩa cách thức 「スムーズに」 đứng trước để bổ nghĩa cho động từ 「進む」. Trợ từ 「が」 đi sau danh từ để làm rõ chủ thể của hành động tiến triển là 「交渉が」. Thứ tự logic là: 交渉が -> スムーズに -> 進む -> かのように見えた。":
    "Cấu trúc so sánh giả định 「V + かのように見えた」 (nhìn hệt như thể là). Động từ 「進む」 đi kèm với trạng từ cách thức 「スムーズに」 (một cách trơn tru). Chủ thể của toàn bộ tiến trình này được xác định rõ qua cụm 「交渉が」 (cuộc đàm phán).",
    
    "Động từ tôn kính ngữ kính trọng của 「来る / 来た」 (đến, ghé qua) là 「見えました」. Chủ ngữ là đối tượng được tôn kính 「田中様が」 đi kèm trợ từ 「が」. Cụm định từ bổ nghĩa cho vị khách hàng này bao gồm từ chỉ thời gian 「本日」 kết hợp với danh từ định ngữ sở hữu 「お約束の」 (cuộc hẹn trước) đứng trước để bổ nghĩa trực tiếp cho 「田中様が」. Thứ tự đúng là: 本日 -> お約束の -> 田中様が -> 見えました。":
    "Tôn kính ngữ của 「来た」 (đã đến) là 「見えました」. Cụm định ngữ thời gian 「本日」 và cuộc hẹn 「お約束の」 kết hợp làm rõ cho đối tượng được tôn kính 「田中様が」. Sự xuất hiện của vị khách này gắn liền với động từ kính ngữ ở cuối câu.",
    
    "Cấu trúc biểu thị triển vọng hay khả năng xảy ra hành động 「V-thông thường + 見込みがある」 (có khả năng, triển vọng để làm...). Ở đây động từ thể khả năng 「得られる」 (có thể đạt được) bổ nghĩa cho danh từ 「見込み」. Cụm trạng từ chỉ giới hạn thời gian 「今期中に」 đứng trước để bổ nghĩa cho động từ 「得られる」. Trợ từ nhấn mạnh 「は」 đi kèm danh từ thành 「見込みは」 để làm chủ ngữ cho dạng câu hỏi nghi vấn 「あるのだろうか」. Thứ tự tự nhiên: 今期中に -> 得られる -> 見込みは -> あるのだろうか。":
    "Cấu trúc 「見込みがある」 biểu thị triển vọng hay khả năng xảy ra. Động từ khả năng 「得られる」 (có thể đạt được) đi kèm cụm thời gian 「今期中に」 (trong kỳ này). Toàn bộ khối này bổ nghĩa cho 「見込みは」 (triển vọng thì), làm nền tảng cho câu hỏi nghi vấn 「あるのだろうか」.",
    
    "Cấu trúc chỉ dự kiến hoặc phán đoán tương lai 「V-thông thường + 見込みだ」 (dự kiến là...). Động từ thể từ điển 「決定する」 liên kết trực tiếp với danh từ vị ngữ 「見込みです」. Trạng từ khẳng định mức độ trang trọng 「正式に」 bổ nghĩa trực tiếp cho động từ 「決定する」. Chủ ngữ của hành động là 「経営方針が」 được bổ nghĩa bởi tính từ 「新しい」 ở phía trước. Thứ tự logic sẽ là: 新しい -> 経営方針が -> 正式に -> 決定する見込みです。":
    "Động từ 「決定する」 liên kết với danh từ vị ngữ 「見込みです」 để nêu dự kiến tương lai. Trạng từ 「正式に」 (chính thức) bổ trợ trực tiếp cho hành động. Phía trước đó, chủ ngữ 「経営方針が」 (phương châm kinh doanh) được bổ nghĩa hoàn hảo bởi tính từ 「新しい」 (mới).",

    # part_93.csv
    "Cấu trúc 「Nを見込んで」 nghĩa là dự tính trước, kỳ vọng vào điều gì đó. Trong câu này, định ngữ 「来期の」 (quý tới) bổ nghĩa cho danh từ chỉ sự gia tăng doanh số 「大幅な売上増」. Cụm danh từ này làm tân ngữ cho động từ 「見込んで」. Sau đó, cụm 「新規プロジェクトの」 bổ nghĩa cho danh từ 「立ち上げ」 ở phần Suffix. Thứ tự sắp xếp đúng theo mạch ý nghĩa logic là 1-2-3-4.":
    "Cấu trúc 「Nを見込んで」 dùng để chỉ sự dự tính, kỳ vọng. Định ngữ 「来期の」 (kỳ tới) bổ nghĩa cho tân ngữ 「大幅な売上増」 (việc tăng doanh số đáng kể). Tân ngữ này đi với động từ 「見込んで」, tạo tiền đề để triển khai việc 「立ち上げ」 (khởi động) cho cụm 「新規プロジェクトの」 ở phần sau.",
    
    "Cấu trúc cơ bản 「N1が N2に N3を見せる」 nghĩa là N1 cho N2 xem N3. Ở đây, 「山田部長に」 là người nhận hành động (chỉ đối tượng), 「新しい」 là tính từ bổ nghĩa cho danh từ chỉ vật 「カタログを」, và động từ hành động 「見せました」 đứng ở cuối để hoàn thành câu. Thứ tự sắp xếp tự nhiên theo ngữ pháp tiếng Nhật là 1-2-3-4.":
    "Dựa trên cấu trúc cơ bản 「N1 cho N2 xem N3」. Đối tượng nhận hành động là 「山田部長に」. Tân ngữ chỉ vật 「カタログを」 được tính từ 「新しい」 (mới) bổ nghĩa và kết hợp với hành động 「見せました」 (đã cho xem) ở cuối câu.",
    
    "Cấu trúc 「Vように見せる」 mang ý nghĩa giả vờ, tỏ ra như thể là đang thực hiện hành động V. Ở đây, mệnh đề bổ nghĩa cho 「ように見せている」 là 「プロジェクトが順調に進んでいる」 (dự án đang tiến triển thuận lợi), với chủ ngữ phụ là 「プロジェクトが」, trạng từ 「順調に」 bổ nghĩa cho động từ tiếp diễn 「進んでいる」. Thứ tự sắp xếp logic là 1-2-3-4.":
    "Cấu trúc 「Vように見せる」 mang ý nghĩa giả vờ như thể đang làm V. Mệnh đề phụ 「プロジェクトが順調に進んでいる」 (dự án tiến triển thuận lợi) được đặt vào cấu trúc này để diễn tả một vẻ ngoài che đậy bản chất thật.",
    
    "Cấu trúc 「N1みたいなN2」 dùng để so sánh, ví von 「N2 giống như N1」. Trong câu này, tính từ 「優秀な」 đóng vai trò bổ nghĩa cho danh từ 「田中さん」, tạo thành cụm 「優秀な田中さん」. Cụm này đi kèm với 「みたいな」 để bổ nghĩa tiếp cho danh từ 「営業担当者」 làm mục tiêu hướng tới của động từ 「なりたい」. Thứ tự sắp xếp chính xác là 1-2-3-4.":
    "Cấu trúc 「N1みたいなN2」 ví von 「N2 giống như N1」. Tính từ 「優秀な」 bổ nghĩa cho 「田中さん」, tiếp nối bằng liên từ 「みたいな」. Toàn cụm này làm rõ thêm cho danh từ mục tiêu 「営業担当者」 (người phụ trách kinh doanh) mà chủ thể mong muốn trở thành (なりたい).",
    
    "Cấu trúc 「Vみたいに + Adj/V」 diễn tả cách thức thực hiện hành động (như là..., giống như là...). Ở đây, cụm động từ bổ nghĩa cho 「みたいに」 là 「初心者に優しく教える」 (dạy cho người mới bắt đầu một cách nhẹ nhàng). Cả cụm này bổ nghĩa cho trạng từ 「分かりやすく」 và động từ chính ở Suffix. Thứ tự sắp xếp tự nhiên theo bổ nghĩa là 1-2-3-4.":
    "Cấu trúc 「Vみたいに + Adj/V」 mô tả cách thức hành động \"giống như là\". Cụm hành động 「初心者に優しく教える」 (dạy nhẹ nhàng cho người mới) đi liền với 「みたいに」, tạo thành bổ ngữ hình ảnh sinh động cho trạng từ 「分かりやすく」 và động từ chính.",
    
    "Cấu trúc 「Vみたいだ」 dùng để thể hiện sự suy đoán, phỏng đoán của người nói dựa trên thông tin gián tiếp (dường như/nghe nói là). Trạng từ thời gian 「来期から」 và danh từ chỉ nơi chốn 「東京本社へ」 bổ nghĩa trực tiếp cho hành động điều chuyển công tác 「異動する」. Cả cụm này kết hợp với đuôi phán đoán 「みたいだ」. Thứ tự sắp xếp đúng theo cấu trúc ngữ pháp là 1-2-3-4.":
    "Đuôi phán đoán 「みたいだ」 thể hiện sự suy đoán gián tiếp (nghe nói là). Trạng từ thời gian 「来期から」 và danh từ nơi chốn 「東京本社へ」 bổ nghĩa trực tiếp cho hành động thuyên chuyển 「異動する」, sau đó gắn mượt mà với phần đuôi phán đoán.",
    
    "Phó từ 「みだりに」 mang nghĩa là tự tiện, bừa bãi, không có lý do chính đáng hoặc không được phép. Từ này thường bổ nghĩa cho một hành động bị cấm đoán (đi kèm vế 「～てはいけない」). Ở đây, hành động 「持ち出しては」 (mang ra ngoài) được bổ nghĩa bởi 「みだりに」. Cụm từ định ngữ 「社外秘の」 bổ nghĩa cho danh từ 「顧客情報」. Do đó, thứ tự sắp xếp hợp lý là 1-2-3-4.":
    "Phó từ 「みだりに」 (tự tiện) thường gắn liền với hành vi bị cấm đoán. Ở đây, nó trực tiếp bổ nghĩa cho hành động 「持ち出しては」 (không được mang ra). Phía trước đó, định ngữ 「社外秘の」 (mật) xác định rõ tính chất của tân ngữ 「顧客情報」 (thông tin khách hàng).",
    
    "Cấu trúc 「Nを A-くみる」 ở đây sử dụng cụm 「安くみる」 với nghĩa là đánh giá quá thấp, xem nhẹ chi phí. Phó từ chỉ mức độ vượt ngưỡng 「あまりにも」 (quá mức) đứng ngay trước để bổ nghĩa trực tiếp cho 「安くみると」. Việc đánh giá quá thấp này sẽ dẫn đến kết quả xấu 「計画が頓挫する」 (kế hoạch bị đình trệ). Thứ tự sắp xếp các thành phần từ trái sang phải là 1-2-3-4.":
    "Cụm 「安くみる」 mang nghĩa đánh giá quá thấp, xem nhẹ. Phó từ vượt ngưỡng 「あまりにも」 (quá mức) đặt ngay phía trước để nhấn mạnh hậu quả. Việc xem nhẹ chi phí này sẽ làm tiền đề cho hệ lụy xấu 「計画が頓挫する」 (kế hoạch đình trệ) ở vế sau.",
    
    "Cấu trúc 「N1にみるN2」 đóng vai trò làm định ngữ bổ nghĩa cho N2, mang nghĩa là 「N2 được nhìn thấy/thể hiện ở N1」. Ở đây, 「ベンチャー企業にみる」 bổ nghĩa cho cụm danh từ chủ ngữ 「人材の流動化は」 (sự lưu động của nhân sự). Sau đó, cụm 「組織の成長にとって」 làm trạng ngữ chỉ đối tượng chịu ảnh hưởng của vấn đề nêu ở phần Suffix. Thứ tự sắp xếp đúng cú pháp là 1-2-3-4.":
    "Cấu trúc 「N1にみるN2」 mang nghĩa \"N2 được thể hiện ở N1\". Cụm 「ベンチャー企業にみる」 bổ nghĩa cho chủ ngữ 「人材の流動化は」 (sự lưu động nhân sự). Từ đó dẫn dắt sang đối tượng chịu tác động 「組織の成長にとって」 (đối với sự phát triển tổ chức).",
    
    "Cấu trúc 「V-たところをみると」 mang ý nghĩa 「nhìn vào trạng thái/hành động V mà phán đoán」. Ở đây, hành động làm căn cứ là 「担当者が笑顔で戻ってきた」 (người phụ trách quay lại với nụ cười). Dựa vào căn cứ này, người nói đưa ra phán đoán về kết quả hợp đồng ở vế sau 「契約は無事に締結できたようです」. Trình tự logic của câu là: Căn cứ phán đoán (1-2) -> Cấu trúc phán đoán (3) -> Nội dung phán đoán (4).":
    "Cấu trúc 「V-たところをみると」 dựa vào hành động làm căn cứ để đưa ra phán đoán. Căn cứ ở đây là 「担当者が笑顔で戻ってきた」 (người phụ trách tươi cười quay về). Nhờ đó, người nói mới có thể phán đoán kết quả tích cực 「契約は無事に締結できたようです」.",
    
    "Cấu trúc 「Nむき」 dùng để chỉ phương hướng (ở đây là 「南向き」 - hướng Nam). Trong câu này, cụm 「南向きの」 đóng vai trò định ngữ bổ nghĩa cho cụm danh từ 「明るい窓」. Tiếp theo là nguyên nhân 「多いので」 dẫn đến kết quả ở phần Suffix 「非常に快適です」. Trình tự logic: Chủ ngữ phòng làm việc (1) -> hướng Nam (2) -> cửa sổ sáng sủa (3) -> nguyên nhân nhiều (4).":
    "Hậu tố 「向き」 chỉ phương hướng (南向き - hướng Nam). Cụm 「南向きの」 đóng vai trò định ngữ bổ nghĩa cho danh từ 「明るい窓」. Khối nguyên nhân 「多いので」 (vì có nhiều) này trực tiếp tạo nên trạng thái 「非常に快適です」 (cực kỳ thoải mái) ở cuối câu.",
    
    "Cấu trúc 「N向き」 mang ý nghĩa 「phù hợp cho N, dành cho N」 (ở đây là 「初心者向きに」 - dành cho người mới bắt đầu). Định ngữ 「ITの知識が少ない」 bổ nghĩa cho danh từ chỉ đối tượng 「初心者」. Động từ ở dạng bị động lịch sự 「設計されております」 thể hiện thiết kế hướng tới đối tượng đó. Thứ tự sắp xếp tự nhiên theo ngữ pháp bổ nghĩa là 1-2-3-4.":
    "Hậu tố 「向き」 mang nghĩa phù hợp cho đối tượng (初心者向きに - dành cho người mới). Định ngữ 「ITの知識が少ない」 mô tả chi tiết đối tượng 「初心者」. Sự chuẩn bị chu đáo này được nhấn mạnh qua động từ bị động lịch sự 「設計されております」 (được thiết kế).",
    
    "Cấu trúc 「Vむきもある」 (trong đó 向き mang ý nghĩa chỉ nhóm người hoặc xu hướng ý kiến) được dùng để biểu thị 「cũng có những người lo ngại/có ý kiến làm V」. Ở đây, 「懸念する向きもある」 có nghĩa là 「cũng có những người lo ngại」. Thứ tự logic: Đối với sự thay đổi (1) -> từ phía nội bộ (2) -> lo ngại về sự hỗn loạn công việc (3-4).":
    "Cấu trúc 「Vむきもある」 chỉ một nhóm người hay xu hướng ý kiến (ví dụ: 懸念する向きもある - cũng có luồng ý kiến lo ngại). Câu triển khai từ bối cảnh (sự thay đổi) đến đối tượng (phía nội bộ) và kết đọng lại ở những e ngại về sự xáo trộn công việc.",

    # part_94.csv
    "Trong bối cảnh công sở, khi đối mặt với chỉ trích của khách hàng, thái độ bình tĩnh là cần thiết. Cụm ngữ pháp 「むきになって」 (nổi nóng, nghiêm trọng hóa vấn đề) kết hợp với động từ 「反論する」 (phản bác) tạo thành 「むきになって反論する」 (nổi nóng phản bác lại). Tiếp theo, 「のではなく」 (thay vì) được dùng để phủ định hành động trước đó và chuyển hướng sang hành động đúng đắn ở vế sau. Trạng từ 「冷静に」 (một cách bình tĩnh) bổ nghĩa cho động từ kết thúc câu 「対応すべきです」 (nên đối ứng). Thứ tự sắp xếp tự nhiên: Đối tượng chỉ trích -> Hành động sai lầm bị phủ định (むきになって反論するのではなく) -> Hành động đúng đắn được khuyên làm (冷静に対応すべきです)。":
    "Cụm ngữ pháp 「むきになって」 (nổi nóng) kết hợp với 「反論する」 (phản bác). Cấu trúc 「のではなく」 (thay vì) dùng để gạt bỏ hành vi sai lầm này, từ đó nhấn mạnh thái độ xử lý đúng đắn 「冷静に対応すべきです」 (cần bình tĩnh đối ứng) ở vế sau.",
    
    "Mẫu ngữ pháp 「N向け」 nghĩa là dành cho N, hướng tới đối tượng N. Khi bổ nghĩa cho một danh từ phía sau, ta dùng dạng 「N向けのN」. Ở đây, 「個人事業主」 (chủ doanh nghiệp cá thể/tự doanh) là đối tượng mục tiêu. Cụm 「個人事業主向けの」 đóng vai trò bổ nghĩa cho danh từ 「管理システム」 (hệ thống quản lý). Tính từ 「新しい」 (mới) cũng bổ nghĩa trực tiếp cho 「管理システム」. Trợ từ 「を」 chỉ đối tượng của động từ khiêm nhường ngữ kết câu 「開発いたしました」 (chúng tôi đã phát triển). Thứ tự đúng là: Chủ ngữ -> Đối tượng khách hàng mục tiêu -> Tính chất sản phẩm -> Danh từ sản phẩm -> Động từ hành động.":
    "Mẫu ngữ pháp 「N向け」 có nghĩa là hướng tới đối tượng N. Cụm định ngữ 「個人事業主向けの」 (dành cho người tự doanh) kết hợp với tính từ 「新しい」 để làm rõ cho sản phẩm 「管理システム」 (hệ thống quản lý). Tân ngữ này đi liền với hành động khiêm nhường 「開発いたしました」 ở cuối câu.",
    
    "Mẫu ngữ pháp 「N向けに」 mang nghĩa là làm một việc gì đó hướng tới/dành cho đối tượng N. Ở đây, đối tượng là 「海外の投資家」 (các nhà đầu tư nước ngoài). Cụm 「海外の投資家向けに」 đóng vai trò trạng ngữ bổ nghĩa cho hành động công khai thông tin ở vế sau. Danh từ 「財務情報」 (thông tin tài chính) đi kèm trợ từ 「を」 làm tân ngữ cho động từ 「公開する」. Cấu trúc quyết định mang tính chủ động của tổ chức 「〜ことにいたしました」 (chúng tôi đã quyết định việc...) đứng ở cuối câu lịch sự. Thứ tự tự nhiên: Chủ thể -> Đối tượng hướng đến (海外の投資家向けに) -> Tân ngữ bị tác động -> Hành động và quyết định.":
    "Trạng ngữ 「海外の投資家向けに」 (hướng tới nhà đầu tư nước ngoài) làm bối cảnh cho hành động công khai thông tin. Tân ngữ 「財務情報」 (thông tin tài chính) đi với động từ 「公開する」 và chốt lại bằng cấu trúc quyết định chủ động 「～ことにいたしました」.",
    
    "Mẫu ngữ pháp 「Nに向けて」 chỉ hướng tới một mục tiêu hoặc một mốc thời gian/sự kiện cụ thể để chuẩn bị hoặc thực hiện hành động. Ở đây, đích đến là 「新規プロジェクトの発表」 (buổi công bố dự án mới). Danh từ ghép 「新規プロジェクト」 bổ nghĩa cho 「発表」 bằng trợ từ 「の」. Cụm 「発表に向けて」 đóng vai trò trạng ngữ chỉ mục đích. Trạng từ 「チーム一丸となって」 (cả đội đồng lòng như một) bổ nghĩa cho cụm động từ kết câu 「準備を進めております」 (đang tiến hành chuẩn bị - dạng tôn kính/khiêm nhường). Thứ tự logic: Mục tiêu hướng tới -> Cách thức thực hiện (đồng lòng) -> Hành động cụ thể.":
    "Cấu trúc 「Nに向けて」 chỉ hướng tới mục tiêu/sự kiện cụ thể. Ở đây, trạng ngữ mục đích 「発表に向けて」 (hướng tới buổi công bố) dẫn dắt trạng từ thái độ 「チーム一丸となって」 (cả đội đồng lòng). Toàn bộ bổ trợ cho hành động khiêm nhường 「準備を進めております」 (đang tiến hành chuẩn bị).",
    
    "Cấu trúc so sánh 「AよりむしろBの方（が）...」 thể hiện việc coi trọng B hơn là A. Trong câu này, vế A là việc làm ra tài liệu hoàn hảo 「完璧な資料を作るよりも」. Vế B là việc báo cáo tiến độ sớm 「早く進捗を報告すること」. Phó từ 「むしろ」 đứng trước trạng từ 「早く」 để nhấn mạnh tính ưu tiên của vế sau. Danh từ hóa vế B bằng cách thêm 「こと」, sau đó kết hợp với cấu trúc so sánh 「〜の方が重要です」 (thì quan trọng hơn). Thứ tự tự nhiên: Bối cảnh -> Hành động bị hạ thấp (作るよりも) -> Nhấn mạnh phương án ưu tiên (むしろ早く) -> Nội dung phương án (進捗を報告することの) -> Kết luận so sánh (方が重要です).":
    "Cấu trúc 「AよりむしろBの方が...」 thể hiện việc coi trọng B hơn A. Hành động bị xem nhẹ 「作るよりも」 nhường chỗ cho phó từ nhấn mạnh 「むしろ早く」. Mệnh đề B sau đó được danh từ hóa (報告すること) để so sánh và chốt lại bằng 「方が重要です」.",
    
    "Phó từ 「むやみに」 mang nghĩa là một cách khinh suất, thiếu suy nghĩ, bừa bãi. Trong câu cấm đoán bảo mật công sở, tính từ sở hữu 「社内の」 (nội bộ công ty) bổ nghĩa cho danh từ 「機密情報」 (thông tin mật). Trợ từ 「を」 biểu thị đối tượng chịu tác động. Phó từ 「むやみに」 đứng ngay trước động từ 「話す」 để bổ nghĩa cho hành vi nói chuyện. Cấu trúc cấm đoán 「〜てはいけません」 (không được phép làm gì) khép lại câu. Thứ tự sắp xếp logic: Đối tượng tiếp nhận thông tin -> Loại thông tin nhạy cảm -> Thái độ bất cẩn (むやみに) -> Hành động bị cấm đoán (話してはいけません).":
    "Phó từ 「むやみに」 (bừa bãi, khinh suất) thường đứng trước hành vi bị cấm đoán. Định ngữ 「社内の」 làm rõ loại dữ liệu nhạy cảm 「機密情報を」. Phó từ khinh suất kết hợp cùng động từ 「話す」 và đuôi cấm đoán 「てはいけません」 tạo lời cảnh cáo mạnh mẽ.",
    
    "Mẫu ngữ pháp 「無理（を）する」 mang nghĩa là cố quá sức, làm việc quá khả năng. Ở thể lịch sự kính ngữ dùng cho đối tác/đồng nghiệp, ta chuyển thành kính ngữ 「無理はなさらないでください」 (xin đừng quá sức). Trong câu điều kiện lịch sự, phó từ 「非常に」 (rất) bổ nghĩa cho tính từ 「厳しい」 (nghiêm ngặt/gấp rút). Đuôi giả định lịch sự 「〜ようでしたら」 (nếu có vẻ như là...) liên kết vế giả định với lời khuyên bảo. Thứ tự cấu trúc: Chủ ngữ phụ (スケジュール) -> Mức độ tính chất (非常に厳しい) -> Giả định tình huống (ようでしたら) -> Lời khuyên kính ngữ bảo vệ sức khỏe (無理はなさらないでください).":
    "Cụm từ 「無理をする」 (cố quá sức) chuyển thành kính ngữ 「無理はなさらないでください」 để thể hiện sự quan tâm. Phó từ 「非常に」 bổ nghĩa cho tính từ 「厳しい」 (gấp rút), liên kết với đuôi giả định lịch sự 「ようでしたら」 làm nền cho lời khuyên sức khỏe.",
    
    "Cụm từ 「〜には無理がある」 mang nghĩa là có điểm bất hợp lý, quá sức, không khả thi đối với một kế hoạch/phương án nào đó. Trong câu này, cụm danh từ chỉ phương tiện/con người 「わずか二人のメンバーで」 (chỉ với 2 thành viên) làm tiền đề. Hành động 「立ち上げる」 (khởi nghiệp/thành lập) tác động lên tân ngữ 「新規事業を」. Cụm động từ 「新規事業を立ち上げる」 bổ nghĩa trực tiếp cho danh từ 「計画」 (kế hoạch). Trợ từ 「には」 chỉ đối tượng chứa đựng sự bất hợp lý. Thứ tự tự nhiên: Điều kiện nhân sự -> Đối tượng tác động -> Hành động định vị cho kế hoạch (立ち上げる計画には) -> Kết luận sự bất hợp lý (無理がある).":
    "Cụm từ 「無理がある」 chỉ ra sự bất hợp lý hay không khả thi của một kế hoạch. Tiền đề nhân sự 「わずか二人のメンバーで」 đi liền hành động tác động 「新規事業を立ち上げる」. Cụm này làm định ngữ cho 「計画には」, dọn đường cho kết luận phản biện ở cuối câu.",
    
    "Phó từ 「無理に」 có nghĩa là cố ép, cưỡng ép làm một việc gì đó một cách không tự nhiên. Trong câu này, mệnh đề quan hệ 「顧客が必要としていない」 (khách hàng không cần đến - trợ từ 「が」 được dùng làm chủ ngữ phụ trong mệnh đề phụ bổ nghĩa cho danh từ) bổ nghĩa cho danh từ 「商品」 (sản phẩm). Phó từ 「無理に」 bổ nghĩa trực tiếp cho hành động 「勧める」 (giới thiệu/chèo kéo). Đuôi câu phủ định nghĩa vụ mang tính đạo đức kinh doanh 「〜べきではありません」 (không nên làm gì). Thứ tự kết hợp: Đối tượng chủ thể phụ -> Mệnh đề định rõ tính chất sản phẩm (必要としていない商品を) -> Cách thức chèo kéo cưỡng ép (無理に) -> Lời khuyên ngăn răn (勧めるべきではありません).":
    "Phó từ 「無理に」 (cưỡng ép) bổ nghĩa trực tiếp cho hành động chèo kéo 「勧める」. Mệnh đề phụ 「顧客が必要としていない」 nêu rõ tính chất của sản phẩm, gắn kết chặt chẽ với động từ và khép lại bằng quy tắc đạo đức 「べきではありません」 (không nên).",
    
    "Mẫu câu yêu cầu lịch sự phủ định 「〜ないでください」 đi kèm với cụm động từ 「無理をする」 (làm việc quá sức) tạo thành lời khuyên 「無理をしないでください」. Đầu câu bắt đầu bằng phó từ chỉ mức độ giả định 「どんなに」 (cho dù thế nào đi nữa) bắt buộc phải đi kèm với đuôi giả định tương phản 「〜ても」 ở tính từ 「忙しい」. Phó từ phủ định nhẹ 「あまり」 (quá nhiều) bổ nghĩa trực tiếp cho cụm từ phía sau nhằm giảm nhẹ mức độ khuyên răn. Thứ tự sắp xếp cấu trúc: Trạng từ liên kết mức độ (どんなに) -> Điều kiện giả định (仕事が忙しくても) -> Trạng từ giảm nhẹ (あまり) -> Hành động khuyên răn (無理をしないでください).":
    "Cụm từ 「どんなに」 (cho dù thế nào) luôn đi cặp với đuôi tương phản 「～ても」 ở tính từ (忙しくても). Phó từ 「あまり」 đứng trước làm giảm nhẹ sắc thái của lời khuyên 「無理をしないでください」, thể hiện sự tinh tế trong giao tiếp.",
    
    "Cấu trúc 「〜のも無理はない」 mang nghĩa là việc ai đó làm gì/trở nên như thế nào là điều đương nhiên, không có gì đáng trách. Ở vế nguyên nhân, danh từ 「納期」 (hạn giao hàng) đi kèm động từ 「遅れた」 và đuôi giải thích nguyên nhân khách quan 「〜のだから」 (vì thực tế là...). Ở vế kết quả, danh từ chủ thể hành động 「先方の担当者」 (người phụ trách phía đối tác) thực hiện hành động 「怒る」 (nổi giận). Động từ này được danh từ hóa bằng trợ từ 「の」 để tạo thành cụm danh từ làm chủ ngữ cho tính từ phủ định 「無理はない」 (không có gì vô lý). Thứ tự logic: Tiền đề lỗi lầm (事前連絡なしで納期が遅れたのだから) -> Chủ thể chịu ảnh hưởng (先方の担当者が) -> Động thái được thấu hiểu (怒るのも) -> Khẳng định tính hợp lý (無理はない).":
    "Cấu trúc 「〜のも無理はない」 thể hiện thái độ cảm thông (việc đó là đương nhiên). Nguyên nhân khách quan 「遅れたのだから」 dẫn đến phản ứng tức giận của đối tác 「怒る」. Hành động này được danh từ hóa bằng trợ từ 「の」 để làm chủ ngữ cho phán đoán hợp lý ở đuôi câu.",
    
    "Mẫu ngữ pháp 「Nをめぐって」 mang nghĩa là xoay quanh vấn đề N, tranh luận hay bàn tán về N (thường dùng trong văn nghị luận hoặc báo cáo công sở). Ở đây, trung tâm tranh chấp là danh từ ghép 「予算配分」 (phân bổ ngân sách). Việc băm tách danh từ ghép này thành 「予算」 và 「配分を」 nhằm kiểm tra việc kết hợp danh từ tiếng Nhật. Cụm trạng ngữ 「社内で」 (trong nội bộ công ty) kết hợp với tính từ bổ nghĩa 「激しい」 (gay gắt) đứng trước để bổ nghĩa trực tiếp cho danh từ chủ ngữ 「議論」 (cuộc thảo luận/tranh luận). Động từ bị động tôn kính 「交わされました」 (đã được trao đổi/diễn ra) kết thúc câu. Thứ tự sắp xếp hợp lý: Phạm vi dự án -> Đề tài tranh chấp cốt lõi (予算配分をめぐって) -> Bối cảnh và tính chất (社内で激しい) -> Hành động kết thúc.":
    "Mẫu ngữ pháp 「Nをめぐって」 mang nghĩa xoay quanh vấn đề N. Tâm điểm tranh luận là danh từ ghép 「予算配分」. Cụm trạng ngữ bối cảnh 「社内で」 đi kèm tính từ 「激しい」 để bổ nghĩa trực tiếp cho chủ ngữ 「議論」 (cuộc tranh luận), kết thúc bằng động từ bị động trang trọng 「交わされました」."
}

for i in range(91, 95):
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

print("Batch 19 manually reviewed and rewritten successfully!")
