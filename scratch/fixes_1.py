import json

fixes_1 = {
    "part_22.csv-9": {
        "Prefix": "かれは", "Chunk1": "さも", "Chunk2": "おいしそうに", "Chunk3": "ビールを", "Chunk4": "飲みほした。", "Suffix": "",
        "Explanation": "Phó từ 'さも' (cứ như thể là) thường đi kèm với 'そうに' để diễn tả vẻ mặt hay điệu bộ, bổ nghĩa cho hành động uống cạn bia ở vế sau."
    },
    "part_22.csv-19": {
        "Prefix": "女は", "Chunk1": "遠慮", "Chunk2": "しいしい", "Chunk3": "部屋の片隅に", "Chunk4": "座った。", "Suffix": "",
        "Explanation": "Cấu trúc 'V-masu + しいしい' diễn tả hành động vừa làm vừa có cảm giác e ngại (vừa làm vừa...). Trong câu này nó bổ nghĩa cho hành động ngồi ở góc phòng."
    },
    "part_29.csv-9": {
        "Prefix": "父が事業に手を出したことが、", "Chunk1": "わが家の", "Chunk2": "苦労の", "Chunk3": "そもそもの", "Chunk4": "始まりだった。", "Suffix": "",
        "Explanation": "Phó từ 'そもそも' (vốn dĩ/ngay từ đầu) kết hợp với '始まり' (sự khởi đầu) để nhấn mạnh nguyên nhân gốc rễ của sự việc."
    },
    "part_30.csv-3": {
        "Prefix": "いろいろ説明してもらったが、", "Chunk1": "それでも", "Chunk2": "まだ", "Chunk3": "納得", "Chunk4": "できない。", "Suffix": "",
        "Explanation": "Liên từ 'それでも' (mặc dù vậy) nối tiếp vế nhượng bộ ở trước để dẫn đến kết quả ngược lại mong đợi ở vế sau."
    },
    "part_32.csv-7": {
        "Prefix": "スポーツは", "Chunk1": "ただ", "Chunk2": "見る", "Chunk3": "だけでは", "Chunk4": "面白くない。", "Suffix": "",
        "Explanation": "Cấu trúc 'ただ V-ru だけでは' mang ý nghĩa 'nếu chỉ có làm V thì...'. Ở đây nó đi với phủ định '面白くない' để chỉ ra sự không đủ."
    },
    "part_32.csv-12": {
        "Prefix": "その野菜は", "Chunk1": "めずらしいと", "Chunk2": "いう", "Chunk3": "だけで", "Chunk4": "よく売れている。", "Suffix": "",
        "Explanation": "'というだけで' diễn tả ý nghĩa 'chỉ với lý do là... thì đã...'. Lý do là 'hiếm' đã đủ để dẫn đến kết quả 'bán chạy'."
    },
    "part_34.csv-5": {
        "Prefix": "近くに大きなホテルができるのは確実です。", "Chunk1": "だとすると、", "Chunk2": "この町の", "Chunk3": "雇用率が上がる", "Chunk4": "かもしれませんね。", "Suffix": "",
        "Explanation": "Liên từ 'だとすると' (nếu đúng như vậy thì) lấy thông tin ở vế trước làm giả định để đưa ra suy luận về tỷ lệ việc làm ở vế sau."
    },
    "part_34.csv-7": {
        "Prefix": "今頃になって", "Chunk1": "気が変わった", "Chunk2": "だなんて", "Chunk3": "よく言えます", "Chunk4": "ね。", "Suffix": "",
        "Explanation": "'だなんて' biểu thị sự ngạc nhiên hoặc chỉ trích đối với một lời nói hay sự việc khó tin, kết nối trực tiếp với đánh giá mỉa mai ở cuối câu."
    },
    "part_34.csv-9": {
        "Prefix": "彼女は市場に出かけると、", "Chunk1": "肉だの", "Chunk2": "野菜だの", "Chunk3": "持ちきれないほど", "Chunk4": "買ってきた。", "Suffix": "",
        "Explanation": "Trợ từ 'だの' dùng để liệt kê ví dụ (nào là thịt, nào là rau), đi kèm với hệ quả 'mua nhiều không cầm xuể' ở vế sau."
    },
    "part_36.csv-4": {
        "Prefix": "試験まであと一カ月しかない。", "Chunk1": "一日", "Chunk2": "たりとも", "Chunk3": "無駄には", "Chunk4": "できない。", "Suffix": "",
        "Explanation": "Cấu trúc '1 + từ chỉ đơn vị + たりとも... ない' mang nghĩa 'dù chỉ một... cũng không'. Ở đây nhấn mạnh việc không thể lãng phí dù chỉ một ngày."
    },
    "part_36.csv-8": {
        "Prefix": "そのショーの", "Chunk1": "意外性", "Chunk2": "たるや、", "Chunk3": "すべての人の注目を集めるに", "Chunk4": "十分であった。", "Suffix": "",
        "Explanation": "Cấu trúc 'Nたるや' dùng để nhấn mạnh chủ đề, mang sắc thái phóng đại (Sự bất ngờ của buổi biểu diễn đó thì thật là...)."
    },
    "part_36.csv-9": {
        "Prefix": "母は", "Chunk1": "若いころは", "Chunk2": "ずいぶん", "Chunk3": "美人", "Chunk4": "だったろう。", "Suffix": "",
        "Explanation": "Đuôi 'だったろう' là thể quá khứ của trợ động từ suy đoán 'だろう', dùng để người nói phỏng đoán về một sự thật trong quá khứ."
    },
    "part_36.csv-12": {
        "Prefix": "この計画に、", "Chunk1": "母は", "Chunk2": "賛成して", "Chunk3": "くれる", "Chunk4": "だろうか。", "Suffix": "",
        "Explanation": "Đuôi 'だろうか' được đặt cuối câu để biểu thị sự tự hỏi hoặc phỏng đoán mang tính nghi vấn của người nói đối với thái độ của người mẹ."
    },
    "part_36.csv-13": {
        "Prefix": "さっきすれちがった人は、", "Chunk1": "高校の", "Chunk2": "ときの同級生", "Chunk3": "ではない", "Chunk4": "だろうか。", "Suffix": "",
        "Explanation": "Cấu trúc 'ではないだろうか' (chẳng phải là... hay sao) thể hiện sự phán đoán khá chắc chắn của người nói về một sự việc."
    },
    "part_36.csv-14": {
        "Prefix": "相手が", "Chunk1": "重役だろうが、", "Chunk2": "社長だろうが、", "Chunk3": "彼は遠慮せずに", "Chunk4": "言いたいことを言う。", "Suffix": "",
        "Explanation": "Cấu trúc 'AだろうがBだろうが' (cho dù là A hay B thì cũng) đưa ra các điều kiện nhượng bộ khác nhau nhưng vế sau vẫn không thay đổi."
    },
    "part_36.csv-15": {
        "Prefix": "その山道は、", "Chunk1": "子供には", "Chunk2": "厳しかった", "Chunk3": "だろうに、", "Chunk4": "よく歩き通した。", "Suffix": "",
        "Explanation": "'だろうに' (chắc hẳn là... thế mà) mang hàm ý nhượng bộ kết hợp với cảm xúc khen ngợi hoặc tiếc nuối. Trong câu này thể hiện sự thán phục."
    },
    "part_36.csv-16": {
        "Prefix": "もっと", "Chunk1": "やさしい", "Chunk2": "言い方も", "Chunk3": "あった", "Chunk4": "だろうに。", "Suffix": "",
        "Explanation": "Cấu trúc 'だろうに' đặt ở cuối câu biểu cảm sự hối tiếc hoặc trách móc nhẹ nhàng về một điều đã không xảy ra trong quá khứ."
    },
    "part_36.csv-17": {
        "Prefix": "あんなすばらしい車に乗っているのだから、", "Chunk1": "田村さんは", "Chunk2": "金持ちに", "Chunk3": "ちがい", "Chunk4": "ない。", "Suffix": "",
        "Explanation": "Cấu trúc 'にちがいない' (chắc chắn là) được dùng khi người nói đưa ra phán đoán chắc chắn dựa trên một căn cứ rõ ràng ở vế trước."
    },
    "part_36.csv-18": {
        "Prefix": "この前の", "Chunk1": "旅行は", "Chunk2": "ちっとも", "Chunk3": "楽しく", "Chunk4": "なかった。", "Suffix": "",
        "Explanation": "Phó từ 'ちっとも' (một chút cũng không) luôn đi kèm với thể phủ định để nhấn mạnh sự phủ định hoàn toàn."
    },
    "part_36.csv-19": {
        "Prefix": "", "Chunk1": "ちなみに", "Chunk2": "迷子の数も", "Chunk3": "千人と去年の", "Chunk4": "倍近くありました。", "Suffix": "",
        "Explanation": "Liên từ 'ちなみに' (nhân tiện, nói thêm) được đặt ở đầu câu để bổ sung thêm một thông tin phụ có liên quan đến chủ đề vừa nói."
    },
    "part_36.csv-20": {
        "Prefix": "めがねを新しいのに変えたら、", "Chunk1": "ちゃんと", "Chunk2": "見える", "Chunk3": "ように", "Chunk4": "なった。", "Suffix": "",
        "Explanation": "Phó từ 'ちゃんと' (đàng hoàng, rõ ràng) bổ nghĩa cho sự thay đổi trạng thái khả năng '見えるようになった' sau khi đổi kính."
    },
    "part_39.csv-3": {
        "Prefix": "来年は", "Chunk1": "ヨーロッパヘ", "Chunk2": "旅行", "Chunk3": "する", "Chunk4": "つもりだ。", "Suffix": "",
        "Explanation": "Cấu trúc 'V-ru + つもりだ' biểu thị dự định của người nói sẽ thực hiện một hành động trong tương lai."
    },
    "part_39.csv-9": {
        "Prefix": "私は", "Chunk1": "そんなことを", "Chunk2": "言った", "Chunk3": "つもりは", "Chunk4": "ない。", "Suffix": "",
        "Explanation": "Cấu trúc 'V-ta + つもりはない' diễn tả việc bản thân người nói không hề có chủ ý hay ý định thực hiện hành động đó."
    },
    "part_40.csv-1": {
        "Prefix": "この部屋にあるものは", "Chunk1": "自由に", "Chunk2": "使って", "Chunk3": "いい", "Chunk4": "ですよ。", "Suffix": "",
        "Explanation": "Cấu trúc 'V-te ii' (được phép làm V) đi với phó từ '自由に' để biểu thị sự cho phép nhẹ nhàng."
    },
    "part_40.csv-2": {
        "Prefix": "学校まで", "Chunk1": "走って", "Chunk2": "いこう", "Chunk3": "と", "Chunk4": "思います。", "Suffix": "",
        "Explanation": "Cấu trúc 'V-te iku' mang ý nghĩa hướng đi hoặc sự tiếp diễn. Ở đây chia thể ý chí 'いこう' diễn tả quyết tâm thực hiện hành động chạy đến trường."
    },
    "part_40.csv-3": {
        "Prefix": "あの子は、", "Chunk1": "友達とけんかして、", "Chunk2": "泣きながら", "Chunk3": "帰って", "Chunk4": "いった。", "Suffix": "",
        "Explanation": "Cấu trúc 'V-te iku' kết hợp với động từ '帰る' diễn tả hành động đi ra xa khỏi vị trí người nói."
    },
    "part_40.csv-4": {
        "Prefix": "あと少しだから", "Chunk1": "この仕事を", "Chunk2": "すませて", "Chunk3": "いき", "Chunk4": "ます。", "Suffix": "",
        "Explanation": "Cấu trúc 'V-te iku' mang sắc thái làm nốt một việc gì đó rồi mới rời đi. 'すませていきます' nghĩa là hoàn thành xong rồi mới đi."
    },
    "part_40.csv-5": {
        "Prefix": "結婚してからも", "Chunk1": "仕事は", "Chunk2": "続けて", "Chunk3": "いくつもり", "Chunk4": "です。", "Suffix": "",
        "Explanation": "Cấu trúc 'V-te iku' kết hợp với '続ける' diễn tả một trạng thái hay hành động sẽ tiếp diễn từ hiện tại đến tương lai."
    }
}

with open(r'd:\pj\xx\ai-gen-quiz\scratch\fixes_1.json', 'w', encoding='utf-8') as f:
    json.dump(fixes_1, f, ensure_ascii=False, indent=4)
