import csv, os

dir_path = r'd:\pj\xx\ai-gen-quiz\mondai2_ordering\csv_filled\set_3_academic'

rewrites = {
    # part_97.csv
    "Ngữ pháp 「もし～としても」 thể hiện giả định ngược 「ngay cả khi...」. Thứ tự đúng: 「もし」 (giả sử) đứng đầu để bổ nghĩa cho mệnh đề giả định, 「他社製品の方が安かった」 (sản phẩm công ty đối thủ rẻ hơn) kết hợp với cấu trúc giả định ngược 「としても」 (ngay cả khi) để tạo thành vế điều kiện, tiếp theo là cụm danh từ nhấn mạnh đối tượng 「我が社の品質には」 (đối với chất lượng của công ty chúng tôi) và kết thúc bằng động từ khẳng định chắc chắn 「自信がございます」 (chúng tôi có sự tự tin) để hoàn thiện câu.":
    "Ngữ pháp 「もし～としても」 thể hiện giả định ngược \"ngay cả khi\". Từ 「もし」 (giả sử) mở đầu, đi kèm vế giả định 「他社製品の方が安かった」 (sản phẩm đối thủ rẻ hơn) và cấu trúc 「としても」 (ngay cả khi). Tiếp đó, cụm nhấn mạnh 「我が社の品質には」 (về chất lượng của chúng tôi) làm điểm tựa cho sự khẳng định 「自信がございます」 (hoàn toàn tự tin) ở cuối câu.",
    
    "Ngữ pháp 「もしかしたら～かもしれない」 thể hiện sự phỏng đoán không chắc chắn 「có lẽ/có thể」. Thứ tự đúng: 「もしかしたら」 đứng đầu câu để báo hiệu sự phỏng đoán, tiếp theo là cụm định ngữ chỉ thời gian và địa điểm 「明日の会議の」 (của cuộc họp ngày mai) bổ nghĩa cho danh từ chỉ vật thể 「資料に一部」 (một phần tài liệu), tiếp đến là cụm chủ-vị phụ 「誤りが」 (lỗi sai) đi kèm phần đầu của phỏng đoán 「あるかも」 (có thể có), kết thúc bằng đuôi kính ngữ 「しれません」 để hoàn thành cấu trúc lịch sự.":
    "Ngữ pháp 「もしかしたら～かもしれない」 thể hiện sự phỏng đoán (có lẽ/có thể). Trạng từ 「もしかしたら」 mở đầu câu, kết hợp cùng định ngữ 「明日の会議の」 để bổ trợ cho 「資料に一部」 (một phần tài liệu). Sau đó, chủ ngữ phụ 「誤りが」 (lỗi sai) đi liền với đuôi phỏng đoán 「あるかも」 và kết thúc lịch sự bằng 「しれません」.",
    
    "Cấu trúc phỏng đoán nghi vấn 「もしかしたら～か」 dùng để hỏi nhẹ nhàng, lịch sự về một khả năng có thể xảy ra. Thứ tự đúng: 「部長、もしかしたら」 mở đầu câu hỏi thăm dò với cấp trên, tiếp theo là cụm định ngữ chỉ phạm vi 「このプロジェクトの」 (của dự án này) bổ nghĩa cho chủ thể 「スケジュールは」 (lịch trình), theo sau là cụm động từ chuyển trạng thái 「変更に」 (thay đổi) đi với động từ 「なります」 (trở thành/diễn ra), và kết thúc bằng trợ từ nghi vấn 「か」 tạo câu hỏi.":
    "Cấu trúc 「もしかしたら～か」 dùng để hỏi dò một khả năng. Sau lời gọi 「部長、もしかしたら」, cụm định ngữ 「このプロジェクトの」 làm rõ cho chủ ngữ 「スケジュールは」 (lịch trình dự án). Sự thay đổi được biểu đạt bằng 「変更になります」 và chốt lại bằng trợ từ nghi vấn 「か」.",
    
    "Ngữ pháp 「AもしくはB」 biểu thị sự lựa chọn 「hoặc là A hoặc là B」 trong văn phong thương mại trang trọng. Thứ tự đúng: 「契約書は」 (Tờ hợp đồng thì...) làm chủ đề chính của câu, tiếp theo là hai phương án hành động dạng danh từ 「郵送」 (gửi qua bưu điện) và 「PDFファイルの添付にて」 (bằng việc đính kèm tệp PDF) được liên kết với nhau bằng liên từ 「もしくは」 (hoặc là), kết thúc bằng yêu cầu kính ngữ lịch sự 「お送りください」 (xin vui lòng gửi).":
    "Ngữ pháp 「AもしくはB」 biểu thị sự lựa chọn giữa hai phương án. Chủ đề 「契約書は」 (hợp đồng) mở đầu. Hai cách thức gửi là 「郵送」 (đường bưu điện) và 「PDFファイルの添付にて」 (đính kèm PDF) được nối với nhau bằng 「もしくは」 (hoặc là), kết lại bởi yêu cầu lịch sự 「お送りください」 (vui lòng gửi).",
    
    "Cấu trúc hành chính trang trọng 「V1-るか、もしくは V2-るか」 dùng để đưa ra hai sự lựa chọn về hành động hành vi. Thứ tự đúng: Trạng ngữ thời gian 「期限までに」 (trước thời hạn) đứng đầu, tiếp theo là lựa chọn hành động thứ nhất 「費用を支払うか」 (thanh toán chi phí hay là), liên kết bằng liên từ tuyển lựa 「もしくは」 (hoặc là), tiếp đến là lựa chọn hành động thứ hai 「契約を」 (hợp đồng) đi kèm động từ hỏi ý kiến 「解除するか」 (có hủy bỏ hay không), và kết thúc bằng động từ yêu cầu dứt khoát 「選択してください」 (xin hãy lựa chọn).":
    "Cấu trúc 「V1-るか、もしくは V2-るか」 đưa ra hai lựa chọn hành động trang trọng. Trạng ngữ 「期限までに」 (trước thời hạn) đi kèm lựa chọn thứ nhất 「費用を支払うか」 (trả phí hay là). Liên từ 「もしくは」 nối với lựa chọn thứ hai 「契約を解除するか」 (hủy hợp đồng hay là), và chốt lại bằng yêu cầu dứt khoát 「選択してください」 (hãy lựa chọn).",
    
    "Ngữ pháp giả định tình huống ít khả năng xảy ra hoặc mang tính hệ trọng 「もしも～たら」. Thứ tự đúng: 「もしも」 đứng đầu dẫn dắt giả định, tiếp theo là cụm định ngữ bổ nghĩa nguồn gốc 「他社からより良い」 (tốt hơn từ công ty đối thủ) bổ nghĩa trực tiếp cho danh từ chủ ngữ phụ 「条件の提案が」 (đề xuất điều kiện), đi liền với động từ điều kiện 「あったら」 (nếu có), kết hợp với trạng từ chỉ mức độ khẩn trương 「すぐに」 (ngay lập tức), tân ngữ chỉ đối tượng nhận thông tin 「私に」 (cho tôi), và kết thúc bằng mệnh lệnh lịch sự 「報告してください」 (hãy báo cáo).":
    "Ngữ pháp 「もしも～たら」 đặt ra một giả định hệ trọng. 「もしも」 mở đầu, theo sau là định ngữ 「他社からより良い」 (tốt hơn từ đối thủ) làm rõ cho 「条件の提案が」 (đề xuất điều kiện). Việc này đi với điều kiện 「あったら」 (nếu có) và yêu cầu khẩn trương 「すぐに私に報告してください」 (hãy báo cáo tôi ngay lập tức).",
    
    "Ngữ pháp 「もしものN」 mang ý nghĩa 「N xảy ra khi có sự cố bất ngờ」. Thứ tự đúng: 「万が一」 (vạn nhất/lỡ như) làm trạng từ nhấn mạnh rủi ro, cụm danh từ ghép 「もしものの」 bổ nghĩa cho danh từ 「事態に」 (đối phó tình huống khẩn cấp) kết hợp ngữ pháp 「備えて」 (để chuẩn bị trước), tiếp theo là cụm danh từ chỉ mục tiêu 「バックアップ用」 (dùng để dự phòng) bổ nghĩa cho danh từ tân ngữ 「サーバーを」 (máy chủ), kết thúc bằng cấu trúc chuẩn bị sẵn 「準備しておきます」 (sẽ chuẩn bị sẵn).":
    "Ngữ pháp 「もしものN」 chỉ sự cố bất ngờ. Phó từ 「万が一」 (lỡ như) kết hợp cùng 「もしものの事態に備えて」 (để đề phòng tình huống khẩn cấp). Điều này làm lý do cho hành động chuẩn bị 「バックアップ用サーバーを準備しておきます」 (sẽ chuẩn bị máy chủ dự phòng) ở vế sau.",
    
    "Trạng từ 「もちろん」 đứng đầu câu phản hồi để thể hiện sự đồng ý chắc chắn và hiển nhiên. Thứ tự đúng: Mở đầu bằng lời thoại của nhân vật A làm bối cảnh hỏi thăm, nhân vật B đáp lại bằng 「もちろん」 (tất nhiên rồi), tiếp đến dùng trạng từ lịch sự 「喜んで」 (rất sẵn lòng) để bổ nghĩa cho động từ, kết hợp danh từ hành động 「参加」 (tham gia) và động từ khiêm nhường ngữ 「いたします」 để hoàn chỉnh cấu trúc trả lời lịch sự trong môi trường công sở.":
    "Trạng từ 「もちろん」 (tất nhiên) thể hiện sự đồng ý chắc chắn. Phản hồi bằng 「もちろん」, tiếp nối bằng trạng từ thái độ 「喜んで」 (rất sẵn lòng). Cụm này làm nổi bật hành động khiêm nhường 「参加いたします」 (chúng tôi xin tham gia) ở cuối câu.",
    
    "Ngữ pháp 「N1はもちろんN2も」 biểu thị ý nghĩa 「N1 là tất nhiên rồi, ngay cả N2 cũng...」. Thứ tự đúng: Chủ đề chính đặt đầu câu 「新しいシステムは」 (Hệ thống mới thì...), tiếp theo là danh từ so sánh cơ bản 「パソコンは」 đi với cấu trúc 「もちろん」 (máy tính là đương nhiên), theo sau là vế bổ sung rộng hơn 「スマートフォンでも」 (ngay cả trên điện thoại), trạng từ 「スムーズに」 (một cách mượt mà) bổ nghĩa cho động từ khả năng kết thúc câu 「操作できます」 (có thể thao tác).":
    "Ngữ pháp 「N1はもちろんN2も」 nghĩa là \"N1 là tất nhiên, ngay cả N2 cũng\". Chủ đề 「新しいシステムは」 dẫn vào sự so sánh cơ bản 「パソコンはもちろん」. Tính năng được mở rộng sang 「スマートフォンでも」 và khẳng định tính ưu việt qua hành động 「スムーズに操作できます」 (thao tác mượt mà).",
    
    "Ngữ pháp 「～をもって」 biểu thị trạng thái mang theo thái độ, tình cảm hoặc tư thế khi thực hiện hành vi (tương đương với 「を持って」). Thứ tự đúng: Danh từ chỉ thái độ tinh thần 「誠意を」 (sự thành tâm) đi liền với cấu trúc liên kết hành động 「もって」 (mang theo/bằng), tiếp theo là cụm danh từ chỉ đối tác 「お客様の」 (của khách hàng) bổ nghĩa cho 「ご要望に」 (đối với yêu cầu), cụm chỉ mục đích hướng tới 「お応えできるよう」 (để có thể đáp ứng), và kết thúc bằng lời hứa hẹn trang trọng 「努力いたします」 (chúng tôi sẽ nỗ lực).":
    "Ngữ pháp 「～をもって」 biểu thị tâm thế khi thực hiện hành vi. Tâm thế ở đây là 「誠意をもって」 (bằng tất cả sự thành tâm). Nó là cơ sở để tiếp cận 「お客様のご要望に」 (yêu cầu của khách hàng) và hướng tới mục đích 「お応えできるよう努力いたします」 (nỗ lực để có thể đáp ứng).",
    
    "Ngữ pháp 「Nをもって」 dùng để chỉ rõ mốc thời gian kết thúc hoặc phương tiện thực hiện hành động một cách trang trọng (Vào ngày/Bằng...). Thứ tự đúng: Cụm danh từ chỉ thời gian đóng cổng đăng ký 「今月末日を」 kết hợp cấu trúc giới hạn 「をもって」 (kể từ ngày cuối tháng này), tiếp theo là tính từ sở hữu 「現在の」 (hiện tại) bổ nghĩa cho danh từ 「製品仕様の」 (của thông số kỹ thuật sản phẩm), cụm danh từ tân ngữ 「変更受付を」 (việc tiếp nhận thay đổi), và kết thúc bằng động từ khiêm nhường trang trọng 「終了いたします」 (xin phép kết thúc).":
    "Ngữ pháp 「Nをもって」 trang trọng chỉ ra mốc thời gian kết thúc. Mốc thời gian 「今月末日をもって」 (kể từ ngày cuối tháng này) áp dụng cho việc tiếp nhận thay đổi thông số hiện tại 「現在の製品仕様の変更受付を」, và chốt bằng lời thông báo 「終了いたします」 (xin kết thúc).",
    
    "Ngữ pháp 「Nをもちまして」 là hình thức tôn kính, cực kỳ lịch sự (kính ngữ) của 「Nをもって」 dùng trong văn bản hoặc tuyên bố trang trọng của công ty. Thứ tự đúng: Chỉ mốc sự kiện chính thức 「本日の総会を」 đi kèm cấu trúc kính ngữ chỉ ranh giới 「もちまして」 (thông qua/kể từ đại hội hôm nay), tiếp theo là cụm định ngữ chỉ đối tượng ban điều hành 「新役員の」 (của các ủy viên mới), cụm danh từ ghép chỉ hành vi nhân sự 「人事」 và 「異動を」 (việc điều chuyển nhân sự), kết thúc bằng động từ khiêm nhường phát ngôn 「発表いたします」 (chúng tôi xin công bố).":
    "Cấu trúc 「Nをもちまして」 là cách nói cực kỳ trang trọng của 「Nをもって」. Mốc sự kiện 「本日の総会をもちまして」 (thông qua đại hội hôm nay) đóng vai trò nền tảng. Tiếp theo, chủ đề công bố 「新役員の人事異動を」 (điều chuyển nhân sự ủy viên mới) được đưa ra và kết bằng hành động khiêm nhường 「発表いたします」 (xin công bố).",
    
    "Trạng từ tăng tiến mức độ 「もっと」 (hơn nữa) dùng để bổ nghĩa cho trạng từ hoặc tính từ đứng sau nó. Thứ tự đúng: Xác định bối cảnh giao tiếp 「取引先との電話では」 (Trong cuộc gọi với đối tác), tiếp theo là trạng từ 「もっと」 đứng trước để nhấn mạnh trạng từ bổ trợ cách thức 「はっきりと」 (một cách rõ ràng), theo sau là tính từ đuôi na 「丁寧な」 bổ nghĩa cho danh từ phương tiện 「言葉で」 (bằng ngôn từ lịch sự), kết thúc bằng yêu cầu hành vi 「話してください」 (xin hãy nói chuyện).":
    "Trạng từ 「もっと」 (hơn nữa) dùng để nhấn mạnh mức độ. Trong bối cảnh gọi điện 「取引先との電話では」, phó từ 「もっと」 kết hợp cùng 「はっきりと丁寧な言葉で」 (bằng từ ngữ rõ ràng và lịch sự hơn). Từ đó dẫn đến lời khuyên hành xử 「話してください」 (hãy nói chuyện) ở cuối câu.",
    
    "Liên từ 「もっとも」 đặt đầu câu thứ hai nhằm đính chính, thêm điều kiện hoặc giới hạn phạm vi áp dụng cho thông tin ở câu thứ nhất (Tuy nhiên/Mặc dù nói thế...). Thứ tự đúng: Đưa ra thông tin tổng quát 「新規事業案は全員一致で承認されました」 (Đề án kinh doanh mới đã được đồng thuận thông qua), bắt đầu câu đính chính bằng liên từ tuyển lựa hạn chế 「もっとも」 (tuy nhiên), tiếp theo là danh từ mục tiêu 「予算案に」 đi liền cấu trúc giới hạn 「関しては」 (đối với phương án ngân sách), theo sau là chủ ngữ phụ chỉ hành động 「再検討が」 (việc xem xét lại), và kết thúc bằng tính từ khẳng định trạng thái 「必要です」 (là cần thiết).":
    "Liên từ 「もっとも」 (tuy nhiên) đứng đầu câu để đính chính hoặc giới hạn. Sau khi nêu việc thông qua đề án, 「もっとも」 mở đầu câu sau, nhắm vào 「予算案に関しては」 (riêng về phương án ngân sách). Kết quả là bước lùi nhẹ với nhận định 「再検討が必要です」 (cần phải xem xét lại).",
    
    "Cấu trúc liên từ đính chính kết hợp đuôi lấp lửng 「もっとも～が」 (Tuy nhiên, nếu... thì sẽ... nhưng). Thứ tự đúng: Đưa ra nhận định ban đầu 「来期の売上目標は達成できる見込みです」 (Mục tiêu doanh thu kỳ tới dự kiến sẽ đạt được), tiếp theo là liên từ đính chính 「もっとも」 (tuy vậy), mệnh đề giả định nghịch cảnh bắt đầu bằng chủ ngữ phụ 「円高が」 (đồng Yên tăng giá) kết hợp động từ điều kiện 「進めば」 (nếu tiếp tục tăng), theo sau là cụm trạng thái tiêu cực 「厳しい状況に」 (trở thành tình huống khó khăn) đi liền động từ kết thúc có tính chất rụt rè, e dè 「なりますが」.":
    "Cấu trúc đính chính lấp lửng 「もっとも～が」 mang ý \"tuy nhiên nếu... thì sẽ... nhưng\". Sau dự kiến lạc quan ban đầu, 「もっとも」 đưa ra điều kiện rủi ro 「円高が進めば」 (nếu đồng Yên tiếp tục tăng). Điều này sẽ dẫn đến kết quả bất lợi 「厳しい状況になりますが」 (tình hình sẽ trở nên khó khăn nhưng...).",
    
    "Trạng từ 「もっぱら」 mang ý nghĩa 「hầu hết, chủ yếu tập trung vào một nội dung」. Thứ tự đúng: Xác định bối cảnh thời gian địa điểm 「最近の社内会議では」 (Trong các cuộc họp nội bộ gần đây), trạng từ 「もっぱら」 đứng trước để giới hạn tiêu điểm thảo luận, tiếp theo là cụm bổ nghĩa sở hữu 「新規AI技術の」 (của công nghệ AI mới) bổ nghĩa cho danh từ mục tiêu 「導入計画に」 (về kế hoạch áp dụng), đi liền với cấu trúc thảo luận 「ついて議論」 (thảo luận về), kết thúc bằng thể bị động khách quan chỉ hành động đang diễn ra 「されています」 (đang được thực hiện).":
    "Trạng từ 「もっぱら」 (hầu hết, chủ yếu) dùng để tập trung vào một tiêu điểm. Trong bối cảnh 「最近の社内会議では」 (họp nội bộ gần đây), 「もっぱら」 đi liền với tiêu điểm 「新規AI技術の導入計画について」 (về kế hoạch áp dụng AI mới). Sự việc này tiếp diễn với động từ thảo luận ở dạng bị động 「議論されています」.",
    
    "Cấu trúc 「もっぱらのN」 dùng để biểu thị danh tiếng, tin đồn đang được mọi người bàn tán xôn xao (tin đồn phổ biến/ai cũng nói). Thứ tự đúng: Đặt mệnh đề chủ thể định nghĩa ở đầu câu 「A社が新商品を開発中だというのは」 (Việc công ty A đang phát triển sản phẩm mới thì...), xác định phạm vi lan truyền tin đồn 「業界内で」 (trong nội bộ ngành), cụm tính từ bổ nghĩa 「もっぱらの」 (xôn xao) đi liền trước bổ nghĩa trực tiếp cho danh từ 「噂に」 (tin đồn), kết thúc bằng động từ trạng thái khiêm nhường trang trọng 「なっております」 (đang trở thành).":
    "Cụm từ 「もっぱらの噂」 diễn tả một tin đồn đang được bàn tán xôn xao. Chủ đề 「A社が新商品を開発中だというのは」 làm khởi điểm. Nó lan truyền 「業界内で」 (trong ngành) và được nhấn mạnh bởi cụm 「もっぱらの噂に」 trước khi chốt bằng trạng từ lịch sự 「なっております」 (đang trở thành).",
    
    "Ngữ pháp 「Nのもとで」 thể hiện ý nghĩa 「Dưới sự hướng dẫn, chỉ bảo, ảnh hưởng trực tiếp của ai đó」. Thứ tự đúng: Chủ ngữ chính 「私は」 (Tôi thì...), tiếp đến là danh từ chỉ người hướng dẫn có kính ngữ 「鈴木部長のご指導の」 (sự chỉ dẫn của trưởng phòng Suzuki) liên kết với cấu trúc bối cảnh 「もとで」 (dưới sự...), theo sau là cụm từ bổ nghĩa chuyên môn 「営業の」 (của nghiệp vụ kinh doanh) bổ nghĩa cho cụm tân ngữ và trạng từ hành vi 「基礎を熱心に」 (kiến thức cơ bản một cách chăm chỉ), kết thúc bằng động từ hành động ở quá khứ 「学びました」 (đã học tập).":
    "Ngữ pháp 「Nのもとで」 mang ý nghĩa \"dưới sự hướng dẫn của ai đó\". Trạng ngữ bối cảnh 「鈴木部長のご指導のもとで」 (dưới sự hướng dẫn của trưởng phòng Suzuki) là tiền đề để chủ thể hướng tới 「営業の基礎を熱心に」 (chăm chỉ học kiến thức kinh doanh cơ bản) và đọng lại ở hành động 「学びました」 (đã học).",
    
    "Ngữ pháp 「Nのもとに」 mang ý nghĩa 「Dưới điều kiện, sự bảo quản, nguyên tắc mang tính ràng buộc của N」. Thứ tự đúng: Tính từ bổ nghĩa tính chất 「厳格な」 (nghiêm ngặt) bổ nghĩa cho danh từ điều kiện ràng buộc pháp lý 「情報管理の」 (quản lý thông tin) kết hợp cấu trúc điều kiện 「もとに」 (dưới điều kiện...), tiếp đến xác định nguồn gốc sở hữu 「お客様から」 (từ phía khách hàng) đi liền động từ định ngữ kính ngữ 「お預かりした」 (chúng tôi nhận ký gửi/lưu trữ), cụm tân ngữ đích 「個人情報を」 (thông tin cá nhân), kết thúc bằng hành động duy trì trạng thái lịch sự 「保護しております」 (chúng tôi đang bảo vệ).":
    "Ngữ pháp 「Nのもとに」 mang nghĩa \"dưới điều kiện quản lý/ràng buộc\". Điều kiện ở đây là 「厳格な情報管理のもとに」 (dưới sự quản lý thông tin nghiêm ngặt). Cụm này làm căn cứ để giữ gìn 「お客様からお預かりした個人情報を」 (thông tin cá nhân nhận từ khách hàng) và kết thúc bằng 「保護しております」 (đang bảo vệ).",
    
    "Trạng từ 「もともと」 chỉ bản chất nguyên bản, nguồn gốc xuất phát của sự vật sự việc ngay từ đầu. Thứ tự đúng: Chủ ngữ của câu đặt trước 「この企画は」 (Dự án này thì...), tiếp theo là trạng từ chỉ thời điểm khởi đầu 「もともと」 (vốn dĩ ngay từ ban đầu), cụm từ sở hữu phân cấp 「弊社の」 (của công ty chúng tôi) bổ nghĩa cho cụm từ chỉ chủ thể đề xuất 「若手社員の」 (của nhân viên trẻ), mốc khởi điểm ý tưởng 「発案から」 (từ đề xuất ý tưởng), kết thúc bằng cụm danh từ hóa khẳng định sự kiện trong quá khứ 「スタートしたものです」 (là thứ đã được khởi động).":
    "Trạng từ 「もともと」 (vốn dĩ) chỉ nguồn gốc ban đầu của sự việc. Khởi đầu với chủ đề 「この企画はもともと」 (Dự án này vốn dĩ...), tiếp nối bằng nguồn gốc ý tưởng 「弊社の若手社員の発案から」 (từ đề xuất của nhân viên trẻ). Sự kiện này được chốt lại ở thể quá khứ bằng cụm 「スタートしたものです」 (đã được khởi động).",

    # part_99.csv
    "Cấu trúc 「V-るものではない」 thể hiện một lời khuyên, đạo đức hoặc quy tắc ứng xử chung (không nên làm gì). Thứ tự kết hợp: Trạng ngữ chỉ bối cảnh 「取引先との会議中に、」 (Trong cuộc họp với đối tác) -> Định ngữ sở hữu 「他社の」 (của công ty khác) -> Tân ngữ 「悪口を」 (lời nói xấu) -> Trạng từ chỉ địa điểm 「公の場で」 (ở nơi công cộng) -> Động từ chính 「言う」 -> Vĩ tố kết luận chỉ quy tắc ứng xử 「ものではない」.":
    "Cấu trúc 「V-るものではない」 mang ý khuyên răn không nên làm trái quy tắc chung. Bối cảnh 「取引先との会議中に」 (trong cuộc họp đối tác) kết hợp với hành động sai trái 「他社の悪口を公の場で言う」 (nói xấu đối thủ chốn công cộng). Câu được chốt lại bằng vĩ tố 「ものではない」 (không nên).",
    
    "Cấu trúc 「V-たものではない」 (thường dùng thể khả năng) biểu thị ý nghĩa phủ định mạnh mẽ, khẳng định một việc hoàn toàn không thể thực hiện được do chất lượng quá tệ. Thứ tự logic: Chủ thể nhận định 「この契約書の草案は」 (Bản thảo hợp đồng này) -> Chủ ngữ của vế nguyên nhân 「誤字が」 (lỗi chính tả) -> Trạng thái nguyên nhân 「あまりに多く、」 (quá nhiều) -> Đối tác hướng tới 「取引先に」 (cho đối tác) -> Động từ khả năng quá khứ bổ nghĩa 「提出できた」 (đã có thể nộp) -> Đuôi phủ định phán xét 「ものではない」.":
    "Cấu trúc 「V-たものではない」 mang ý phủ định mạnh do chất lượng kém. Lời nhận định nhắm vào 「この契約書の草案は」 (bản thảo hợp đồng này), với lý do 「誤字があまりに多く」 (quá nhiều lỗi). Điều đó khiến nó không thể mang đi cho đối tác 「取引先に提出できたものではない」 (chẳng thể nào nộp được).",
    
    "Cấu trúc 「V-たものでもない」 mang ý nghĩa 「không hẳn là hoàn toàn... (không thể phủ nhận hoàn toàn)」. Thứ tự logic: Định ngữ sở hữu 「新入社員の」 (của nhân viên mới) -> Chủ thể đối chiếu tương phản 「提案だが、」 (dù là đề xuất nhưng) -> Thành phần bổ sung tích cực 「斬新なアイデアも」 (ý tưởng mới mẻ cũng) -> Trạng thái tồn tại 「含まれており、」 (được bao gồm) -> Cụm phủ định nhẹ nhàng 「全く無視した」 (hoàn toàn bỏ qua) -> Vĩ tố kết thúc 「ものでもない」.":
    "Cấu trúc 「V-たものでもない」 mang nghĩa \"không hẳn là hoàn toàn\". Lời khen 「新入社員の提案だが」 (dù là đề xuất của nhân viên mới) nhấn mạnh điểm tích cực 「斬新なアイデアも含まれており」 (bao gồm ý tưởng mới). Nhờ vậy, dẫn tới kết luận trân trọng 「全く無視したものでもない」 (không hẳn là đáng vứt bỏ hoàn toàn).",
    
    "Cấu trúc 「V-ないものでもない」 sử dụng phủ định kép để thể hiện khả năng có thể thực hiện một hành động nào đó dưới một điều kiện nhất định. Thứ tự logic: Trạng từ và tân ngữ vế điều kiện 「納期を少し」 (hạn giao hàng một chút) -> Hành động giúp đỡ 「調整して」 (điều chỉnh) -> Thể giả định khiêm nhường 「いただけるなら、」 (nếu được giúp đỡ) -> Tân ngữ vế kết quả 「この案件を」 (dự án này) -> Động từ phủ định bổ nghĩa 「引き受けない」 (không tiếp nhận) -> Đuôi phủ định giảm nhẹ 「ものでもない」.":
    "Phủ định kép 「V-ないものでもない」 ám chỉ khả năng có thể làm được. Nếu điều kiện 「納期を少し調整していただけるなら」 (nếu anh nới hạn giao hàng) được đáp ứng, thì hành động 「この案件を引き受けないものでもない」 (cũng không phải là không thể nhận dự án này) sẽ khả thi.",
    
    "Cấu trúc 「ものと思う」 thể hiện sự tin tưởng, giả định chắc chắn của người nói dựa trên một căn cứ nào đó. Thứ tự logic: Trạng ngữ chỉ phạm vi 「今回の報告書に」 (Trong báo cáo lần này) -> Định ngữ bổ nghĩa 「致命的な」 (nghiêm trọng) -> Chủ ngữ bị phủ định 「ミスは」 (lỗi sai) -> Đuôi phán đoán giả định 「ないものと」 (tin rằng không có) -> Động từ suy nghĩ nối tiếp 「思うが、」 (nghĩ vậy nhưng...) -> Hành động cẩn thận ở Suffix 「念のため再確認いたします」 (tôi xin phép xác nhận lại cho chắc chắn).":
    "Cấu trúc 「ものと思う」 thể hiện niềm tin dựa trên căn cứ nhất định. Lời khẳng định 「今回の報告書に致命的なミスはないものと思うが」 (tôi tin báo cáo lần này không có lỗi nghiêm trọng, nhưng...) làm nền cho hành động cẩn trọng 「念のため再確認いたします」 (để chắc ăn tôi sẽ kiểm lại).",
    
    "Cấu trúc mang tính khách quan 「ものと思われる」 dùng nhiều trong văn phong trang trọng, báo cáo doanh nghiệp để đưa ra dự báo có căn cứ. Thứ tự logic: Nguyên nhân khách quan 「新商品の発売により、」 (Nhờ việc ra mắt sản phẩm mới) -> Định ngữ thời gian 「来期の」 (của kỳ tới) -> Chủ ngữ 「売上は」 (doanh thu) -> Trạng từ chỉ mức độ 「大幅に」 (mạnh mẽ) -> Động từ bổ nghĩa 「増加する」 (tăng lên) -> Vĩ tố kết luận phán đoán khách quan 「ものと思われる」.":
    "Cấu trúc 「ものと思われる」 đưa ra dự báo mang tính khách quan và trang trọng. Bắt nguồn từ lý do 「新商品の発売により」 (do ra mắt sản phẩm mới), dẫn tới dự đoán 「来期の売上は大幅に増加する」 (doanh thu kỳ tới tăng mạnh) và khép lại bằng cụm khách quan 「ものと思われる」.",
    
    "Cấu trúc 「V-ようものなら」 thiết lập một giả định mang tính cảnh báo (nếu lỡ xảy ra việc tồi tệ đó thì hậu quả khôn lường sẽ đến). Thứ tự logic: Bối cảnh trạng ngữ 「この契約内容に」 (Trong nội dung hợp đồng này) -> Tính từ bổ nghĩa 「重大な」 (nghiêm trọng) -> Danh từ chủ thể 「不備が」 (sai sót) -> Động từ thể ý chí của ある là 「あろう」 -> Đuôi liên từ giả định tiêu cực 「ものなら、」 (nếu lỡ...) -> Suffix là kết quả cực kỳ xấu 「弊社の信用は失墜してしまう」 (uy tín của công ty chúng tôi sẽ sụp đổ hoàn toàn).":
    "Giả định 「V-ようものなら」 cảnh báo hậu quả thảm khốc nếu lỡ xảy ra việc xấu. Điều kiện 「この契約内容に重大な不備があろうものなら」 (nếu lỡ có sai sót nghiêm trọng trong hợp đồng) dẫn tới hậu quả nặng nề 「弊社の信用は失墜してしまう」 (uy tín công ty sẽ sụp đổ).",
    
    "Cấu trúc 「ものの」 mang ý nghĩa tương phản nghịch lý 「mặc dù đã làm việc A nhưng thực tế kết quả lại không tốt như mong đợi」. Thứ tự logic: Định ngữ 「新規」 (mới) -> Tân ngữ 「プロジェクトを」 (dự án) -> Động từ xác nhận đã làm 「引き受けた」 (đã tiếp nhận) -> Từ nối tương phản 「ものの、」 -> Nguyên nhân gây cản trở 「人手不足で」 (do thiếu nhân lực) -> Suffix chỉ thực tế bế tắc 「計画通りに進んでいない」 (vẫn chưa tiến hành theo đúng kế hoạch).":
    "Cấu trúc 「ものの」 chỉ sự tương phản thực tế (mặc dù... nhưng). Vế đầu xác nhận 「新規プロジェクトを引き受けたものの」 (dù đã nhận dự án mới). Vế sau lật ngược với nguyên nhân cản trở 「人手不足で計画通りに進んでいない」 (do thiếu người nên chậm tiến độ).",
    
    "Cấu trúc 「～とはいうものの」 mang ý nghĩa nhượng bộ, thừa nhận một thực tế ở vế trước nhưng vế sau lại đưa ra kết quả vượt ngoài mong đợi hoặc khác biệt. Thứ tự logic: Chủ ngữ 「彼女は」 (Cô ấy) -> Tính từ bổ nghĩa danh từ tách thành 「新入」 (mới vào) -> Danh từ đi kèm liên từ 「社員とは」 (nhân viên) -> Động từ 「いう」 -> Từ nối tương phản 「ものの、」 (dẫu nói là...) -> Suffix thể hiện thực lực xuất sắc thực tế 「すでに中堅社員並みの仕事をこなしている」 (đã giải quyết công việc tương đương nhân viên kỳ cựu).":
    "Cấu trúc 「～とはいうものの」 mang tính nhượng bộ, dẫn tới bất ngờ. Lời mào đầu 「彼女は新入社員とはいうものの」 (dẫu nói cô ấy là nhân viên mới) đối lập hẳn với năng lực 「すでに中堅社員並みの仕事をこなしている」 (đã làm được việc như nhân viên kỳ cựu).",
    
    "Cấu trúc liên từ đứng đầu câu 「とはいうものの」 dùng để nối tiếp và phản biện hoặc hạn chế thông tin mang tính tích cực của câu trước. Thứ tự logic: Câu tiền đề hoàn chỉnh 「今期の売上目標は達成した。」 (Mục tiêu doanh số kỳ này đã đạt được.) -> Liên từ chuyển ý tách rời 「とは」 -> 「いう」 -> 「ものの、」 (Tuy nhiên nói là vậy nhưng...) -> Định ngữ sở hữu nguyên nhân 「原材料費の」 (của chi phí nguyên vật liệu) -> Suffix chỉ thực trạng cần lo ngại 「高騰もあり、依然として楽観はできない」 (cũng tăng cao nên vẫn chưa thể lạc quan được).":
    "Liên từ 「とはいうものの」 giới hạn lại sự tích cực của câu trước. Sau khi báo tin vui 「今期の売上目標は達成した」, liên từ 「とはいうものの」 (nói vậy nhưng) đảo chiều bằng thực trạng 「原材料費の高騰もあり、依然として楽観はできない」 (nguyên liệu tăng giá nên chưa thể lạc quan).",
    
    "Cấu trúc 「ものを」 dùng ở giữa câu để thể hiện sự nuối tiếc, bất mãn hoặc trách móc khi một giả định tốt đẹp đã không xảy ra, dẫn đến thực tế tồi tệ. Thứ tự logic: Trạng từ chỉ thời gian 「もっと早く」 (sớm hơn nữa) -> Động từ hành động mong đợi 「相談して」 (thảo luận) -> Thể điều kiện giả định tích cực 「くれれば」 (nếu làm cho) -> Kết quả khả năng giả định 「解決できた」 (đã có thể giải quyết) -> Từ nối nuối tiếc 「ものを、」 (vậy mà...) -> Suffix là hành động thực tế đáng tiếc 「彼は一人で抱え込んでしまった」 (cậu ấy lại tự mình chịu đựng mất rồi).":
    "Cấu trúc 「ものを」 dùng giữa câu để tỏ thái độ tiếc nuối, bất mãn. Vế giả định 「もっと早く相談してくれれば解決できたものを」 (giá mà bàn sớm thì đã giải quyết được rồi) bị đập tan bởi sự thật đáng buồn 「彼は一人で抱え込んでしまった」 (vậy mà cậu ta lại tự mình gồng gánh).",
    
    "Cấu trúc 「～すればいいものを」 diễn tả sự phê phán hoặc vô cùng tiếc nuối vì đối phương đã không chọn giải pháp an toàn/đúng đắn nhất mà lại làm ngược lại. Thứ tự logic: Trạng ngữ thời gian 「送信する前に」 (Trước khi gửi) -> Trạng từ cách thức 「きちんと」 (cẩn thận) -> Động từ giả định tốt đẹp 「確認すれば」 (nếu xác nhận) -> Tính từ bổ nghĩa 「いい」 (thì tốt) -> Từ nối nuối tiếc 「ものを、」 (vậy mà...) -> Suffix chỉ nguyên nhân và hậu quả sai lầm thực tế 「急いで送ったからミスが発生したのだ」 (do vội vàng gửi đi nên đã phát sinh lỗi).":
    "Cấu trúc 「～すればいいものを」 phê phán sự thiếu cẩn trọng. Lời trách 「送信する前にきちんと確認すればいいものを」 (kiểm tra kỹ trước khi gửi đi có phải hơn không) dẫn đến hậu quả hiển nhiên 「急いで送ったからミスが発生したのだ」 (gửi vội quá nên mới có lỗi đấy).",
    
    "Cấu trúc phó từ 「もはや」 đi kèm câu khẳng định thể hiện một trạng thái đã hoàn toàn thay đổi và đạt đến mức độ hiển nhiên ở hiện tại (đã... rồi). Thứ tự logic: Chủ ngữ chính 「AIの活用は、」 (Việc ứng dụng AI) -> Phó từ nhấn mạnh trạng thái 「もはや」 (giờ đây đã) -> Trạng từ chỉ phạm vi 「ビジネスに」 -> Trợ từ kép 「おいて」 (trong kinh doanh) -> Tính từ bổ nghĩa 「不可欠な」 (không thể thiếu) -> Suffix chỉ kết quả hiện tại 「技術となっている」 (đã trở thành một công nghệ).":
    "Phó từ 「もはや」 diễn tả tình thế đã hoàn toàn thay đổi thành hiển nhiên (giờ đây đã). Câu mở đầu với 「AIの活用は」 (việc ứng dụng AI) kết hợp cùng 「もはやビジネスにおいて不可欠な技術となっている」 (giờ đây đã thành công nghệ thiết yếu trong kinh doanh).",
    
    "Cấu trúc 「もはや～ない」 mang tính khẳng định phủ định mạnh mẽ, diễn tả một tình thế đã thay đổi hoàn toàn khiến cho một việc nào đó không còn khả thi nữa (đã không còn... nữa). Thứ tự logic: Bối cảnh trạng thái 「この市場は飽和状態にあり、」 (Thị trường này đang bão hòa) -> Chủ ngữ vế sau 「我々が」 (chúng ta) -> Động từ định ngữ 「新規参入する」 (gia nhập mới) -> Danh từ chỉ cơ hội 「余地は」 (khoảng trống/cơ hội) -> Phó từ phủ định 「もはや」 (đã... không còn) -> Suffix động từ bị động phủ định 「残されていない」 (được để lại).":
    "Cấu trúc phủ định 「もはや～ない」 chỉ sự cạn kiệt cơ hội (đã không còn). Bối cảnh 「この市場は飽和状態にあり」 (thị trường đã bão hòa) làm nền cho lời khẳng định dứt khoát 「我々が新規参入する余地はもはや残されていない」 (chúng ta chẳng còn cơ hội nào chen chân vào nữa).",
    
    "Cấu trúc trợ từ 「や」 dùng để liệt kê không triệt để các danh từ tiêu biểu ở trình độ N5. Thứ tự logic: Định ngữ nơi chốn 「会議室の」 (Của phòng họp) -> Vị trí 「机の上に」 (trên bàn) -> Danh từ liệt kê thứ nhất kèm trợ từ 「資料や」 (tài liệu và...) -> Danh từ liệt kê thứ hai 「筆記用具」 (dụng cụ viết) -> Trợ từ khái quát 「などが」 (như là...) -> Suffix là trạng thái chuẩn bị 「用意されています」 (đang được chuẩn bị sẵn).":
    "Trợ từ 「や」 dùng để liệt kê mang tính tiêu biểu. Nơi chốn 「会議室の机の上に」 (trên bàn họp) là vị trí cho các món đồ liệt kê 「資料や筆記用具などが」 (tài liệu và dụng cụ viết...). Việc đó kết hợp với đuôi bị động 「用意されています」 (đang được chuẩn bị sẵn).",
    
    "Cấu trúc 「数量詞＋や＋数量詞」 dùng để ước lượng một khoảng số lượng nhỏ hoặc thời gian ngắn (một hai ngày, một hai cái...). Thứ tự logic: Cụm định ngữ chỉ mức độ 「この程度の」 (Cỡ mức này) -> Chủ đề giả định 「システムエラーなら、」 (nếu là lỗi hệ thống) -> Số từ thứ nhất kèm trợ từ nối 「1日や」 (1 ngày hoặc) -> Số từ thứ hai 「2日」 (2 ngày) -> Động từ điều kiện 「あれば」 (nếu có) -> Suffix chỉ khả năng giải quyết 「修正可能です」 (là có thể sửa chữa được).":
    "Cấu trúc 「数量詞＋や＋数量詞」 ước lượng đại khái số lượng. Nếu ở mức độ nhẹ 「この程度のシステムエラーなら」 (tầm lỗi này), thì chỉ cần lượng thời gian 「1日や2日あれば」 (cỡ 1, 2 ngày) là kết quả 「修正可能です」 (sửa được) sẽ nằm trong tầm tay.",
    
    "Cấu trúc 「V-るや」 (vừa mới... đã ngay lập tức) diễn tả hành động ở vế sau xảy ra gần như đồng thời và tức thì sau hành động vế trước. Thứ tự logic: Chủ ngữ vế đầu 「社長が」 (Giám đốc) -> Địa điểm 「会議室に」 (vào phòng họp) -> Động từ liên kết 「入って」 -> Động từ chính kèm trợ từ thời gian 「くるや、」 (vừa bước vào là...) -> Định ngữ bối cảnh 「その場の」 (của nơi đó) -> Suffix chỉ phản ứng trạng thái tức thì 「空気が一瞬で緊張した」 (bầu không khí lập tức trở nên căng thẳng).":
    "Cấu trúc 「V-るや」 diễn tả hai hành động nối tiếp chớp nhoáng (vừa mới... đã). Ngay khi 「社長が会議室に入ってくるや」 (sếp vừa bước vào phòng), hệ quả tất yếu là 「その場の空気が一瞬で緊張した」 (bầu không khí căng như dây đàn ngay lập tức).",
    
    "Cấu trúc 「V-るやいなや」 diễn tả một sự việc xảy ra gần như cùng lúc, ngay lập tức sau một hành động khác. Thứ tự logic: Chủ ngữ vế đầu 「新商品が」 (Sản phẩm mới) -> Danh động từ 「発売」 (bán ra) -> Động từ bị động kèm liên từ thời gian 「されるや」 -> 「いなや、」 (ngay khi được mở bán...) -> Định ngữ chỉ phạm vi 「全国の」 (trên toàn quốc) -> Suffix chỉ phản ứng mạnh mẽ tức thì 「顧客から注文が殺到した」 (đơn hàng từ khách hàng đổ về dồn dập).":
    "Cấu trúc 「V-るやいなや」 mang tính nhấn mạnh việc xảy ra ngay tắp lự. Sự kiện châm ngòi 「新商品が発売されるやいなや」 (ngay khi hàng vừa bán ra) lập tức dẫn đến phản ứng bùng nổ 「全国の顧客から注文が殺到した」 (khách toàn quốc đặt mua ầm ầm)."
}

for i in range(96, 101):
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

print("Batch 20 manually reviewed and rewritten successfully!")
