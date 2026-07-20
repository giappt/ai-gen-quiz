import json
import csv
import os

dir_path = r'd:\pj\xx\ai-gen-quiz\mondai2_ordering\csv_filled\set_1_daily'

fixes = {
    "part_2.csv-3": "Mẫu 'V-たあとから' diễn tả sự việc muộn màng xảy ra ngay sau khi một quyết định đã cố định. Hành động gốc '決めた' (đã quyết định) nối với 'あとから', tiếp đến là nội dung yêu cầu '時間を変更したいと' đi với thể bị động giả định '言われても'.",
    "part_2.csv-6": "'あとから' làm trạng từ chỉ thời gian hành động diễn ra muộn hơn người khác. Chủ ngữ '私は' (tôi) đi cùng trạng từ thời gian 'あとから', tiếp theo là trạng từ mức độ 'すぐに' (ngay lập tức) và kết thúc bằng động từ chính '追いかける' (đuổi theo).",
    "part_2.csv-9": "'あんまり' bổ nghĩa cho thể phủ định của tính từ để giảm nhẹ mức độ phán đoán. Chủ ngữ '値段が' (giá cả) đi với phó từ 'あんまり' (không quá), tính từ đuôi i đổi thành thể liên dụng '安く' và kết thúc bằng trợ động từ phủ định 'ない'.",
    "part_2.csv-11": "'あまりの + Danh từ + に' chỉ nguyên nhân cực đại gây ra một trạng thái bất khả kháng. Cụm nguyên nhân 'あまりの辛さに' (vì quá cay) tác động lên chủ thể 'スープが', dẫn đến hệ quả '一口も飲むことができなかった' (một ngụm cũng không thể uống).",
    "part_2.csv-18": "'あるいは' đứng đầu mệnh đề phỏng đoán để tăng sắc thái cho cấu trúc '～かもしれない'. Trạng từ 'あるいは' (hoặc là) dẫn nhập cho chủ ngữ '雨が' và cụm động từ phỏng đoán '降るかもしれない' (có thể sẽ mưa) kết hợp trợ từ chỉ lý do 'から'.",
    "part_2.csv-19": "Cấu trúc lặp lại 'あるいは...あるいは...' dùng để liệt kê các hành động song song. Hành động một 'あるいは海へ行き、' (hoặc là đi biển) được nối với hành động hai '山へ登ったりして' (hoặc là leo núi) để mô tả các lựa chọn khác nhau.",
    "part_2.csv-20": "Cấu trúc 'N1にあるまじきN2' phê phán hành vi N2 không được phép có ở cương vị N1. Danh từ cương vị '親に' đi kèm thành phần hạn định 'あるまじき' (không thể chấp nhận được đối với), bổ nghĩa cho tính từ '卑劣な' và danh từ '行為' (hành vi đê hèn).",
    "part_3.csv-1": "'あれで' dùng để đưa ra đánh giá tích cực trái ngược với vế tiêu cực trước đó. Cụm 'あれで' (nhìn thế thôi mà) dẫn vào vế sau đánh giá tích cực '料理を作るのが得意なんですよ' (việc nấu ăn rất là giỏi đấy).",
    "part_3.csv-2": "'あれで' thể hiện sự ngạc nhiên về giá cả hoặc mức độ so với tính chất của vật. Cụm từ 'あれで' (như thế mà) đi liền với '千円なら' (nếu là 1000 yên) để đưa ra nhận định 'すごくお買い得だね' (thì hời quá nhỉ).",
    "part_3.csv-3": "'あれでも' nghĩa là 'dù như thế đi nữa'. Cụm 'あれでも' kết hợp với '一応' (dù sao thì) để nhấn mạnh sự ngạc nhiên về danh phận '店長なのです' (là cửa hàng trưởng đấy).",
    "part_3.csv-4": "'あんまり' đi với dạng phủ định '～ない' biểu thị ý nghĩa 'không... lắm'. Phó từ 'あんまり' bổ nghĩa cho cụm 'ご飯を食べていない' (không ăn cơm) để diễn tả việc ăn rất ít.",
    "part_3.csv-5": "'あんまり' đứng trước tính từ thể hiện mức độ quá mức dẫn đến kết quả ở vế sau. Cụm 'あんまり嬉しくて' (vì quá đỗi vui mừng) là nguyên nhân dẫn đến hệ quả '遅くまで眠れなかった' (không thể ngủ được cho đến tận khuya).",
    "part_3.csv-6": "Cấu trúc '～なんてあんまりだ' dùng để trách móc hành động của ai đó là quá đáng. Việc '食べてくれないなんて' (không chịu ăn cho tôi) được đánh giá là 'あんまりだ' (thật là quá đáng).",
    "part_3.csv-7": "'いい' dùng để khen ngợi món đồ của đối phương trong giao tiếp. Ở đây 'いい' (đẹp/tốt) được dùng để khen 'スニーカー' (giày thể thao) kèm theo câu hỏi tìm hiểu 'どこで' (mua ở đâu thế).",
    "part_3.csv-8": "'もういいです' dùng để từ chối một cách lịch sự khi đã cảm thấy đủ. Ở đây 'もういいですよ' (đã đủ rồi nhé) đi kèm với 'お腹' (bụng, ý chỉ đã no) để từ chối lời mời ăn uống thêm.",
    "part_3.csv-9": "'いいね' đứng đầu câu dùng để nhắc nhở hoặc lưu ý đối phương. Cụm 'いいね' (nghe rõ chưa/nhớ nhé) đóng vai trò dẫn nhập để căn dặn '買い物に行くときは気をつける' (khi đi mua sắm thì phải cẩn thận).",
    "part_3.csv-10": "'～はいいから' dùng để gạt bỏ một vấn đề qua một bên để thực hiện hành động tiếp theo. Cụm 'そのことはいいから' (chuyện đó thì thôi bỏ qua đi) thúc giục hành động '早く映画館に' (nhanh vào rạp chiếu phim).",
    "part_3.csv-11": "Cấu trúc 'V-る + がいい' mang sắc thái mỉa mai hoặc phó mặc cho hậu quả xảy ra. Cụm 'みんなに嫌われるがいい' (đáng đời bị tất cả bạn bè ghét bỏ) là lời rủa xả hướng tới đối tượng.",
    "part_3.csv-12": "'～と言った' dùng để trích dẫn nội dung đã nói với ai đó. Cụm '片付けると言った' (đã nói là sẽ dọn dẹp) trích dẫn lại lời hứa, đi kèm trợ từ 'が' (nhưng) để chỉ sự trái ngược với thực tế.",
    "part_3.csv-13": "'～と言っている' dùng để truyền đạt lại lời nói hoặc ý định của người khác. Cụm '遅れて来ると言って' (nói rằng sẽ đến muộn) thuật lại lời nhắn của ai đó đang truyền tới người nghe.",
    "part_3.csv-14": "'～と言われている' diễn tả một nhận định, lời đồn phổ biến trong xã hội. Cụm '大盛りで有名だと言われている' (được đồn đại là nổi tiếng với suất ăn lớn) đưa ra thông tin khách quan.",
    "part_3.csv-15": "Cấu trúc '～ように言われる' diễn tả việc được hoặc bị ai đó yêu cầu làm gì. Ở đây '買ってくるように言われた' (đã được dặn là phải mua về) thuật lại mệnh lệnh hoặc lời nhờ vả.",
    "part_3.csv-16": "'文句を言う' là cụm từ đi liền mang nghĩa phàn nàn, cằn nhằn. Cụm '文句を言う' được danh từ hóa bằng 'のが' để tạo thành chủ đề của câu (việc cằn nhằn thì...).",
    "part_3.csv-17": "Mẫu câu 'N1をN2だと言う' nghĩa là khẳng định N1 là N2. Cụm '男性を婚約者だと言った' thuật lại lời xác nhận rằng người đàn ông đó chính là vị hôn phu.",
    "part_3.csv-18": "'～という' đặt ở cuối câu dùng để truyền đạt thông tin nghe nói lại từ nguồn khác. Câu 'ケーキがとても美味しいという' (nghe nói bánh kem rất ngon) truyền đạt thông tin một cách khách quan.",
    "part_3.csv-19": "Mẫu câu '名前を～といいます' dùng để giới thiệu tên gọi của ai đó. Cụm '名前を健太といい' (tên gọi là Kenta) là cách nói trang trọng để giới thiệu tên người.",
    "part_3.csv-20": "'Nのことを～という' dùng để định nghĩa hoặc gọi tên một đối tượng cụ thể. Ở đây 'ことを略して何といい' là câu hỏi về cách gọi tắt của một cụm từ nào đó.",
}

# Lỗi "N của..."
fixes_n_cua = {
    "N của あいだ": "Nのあいだ",
    "N của 後で": "Nのあとで",
    "N của ことを": "Nのことを",
    "N của こと": "Nのこと",
}

for file_id, fix_text in fixes.items():
    file_name, row_str = file_id.split('-')
    row_idx = int(row_str) - 1
    full_path = os.path.join(dir_path, file_name)
    
    with open(full_path, 'r', encoding='utf-8-sig') as f:
        reader = list(csv.DictReader(f))
        fieldnames = reader[0].keys()
        
    old_exp = reader[row_idx]["Explanation"]
    reader[row_idx]["Explanation"] = fix_text
    
    with open(full_path, 'w', encoding='utf-8-sig', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(reader)

# Áp dụng thay thế lỗi "N của..." cho toàn bộ Batch 1 (file 1 -> 5)
files = ['part_1.csv', 'part_2.csv', 'part_3.csv', 'part_4.csv', 'part_5.csv']
for file_name in files:
    full_path = os.path.join(dir_path, file_name)
    with open(full_path, 'r', encoding='utf-8-sig') as f:
        reader = list(csv.DictReader(f))
        fieldnames = reader[0].keys()
    
    modified = False
    for row in reader:
        exp = row.get("Explanation", "")
        for k, v in fixes_n_cua.items():
            if k in exp:
                row["Explanation"] = exp.replace(k, v)
                modified = True
                
    if modified:
        with open(full_path, 'w', encoding='utf-8-sig', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(reader)

print(f"Hoàn tất sửa 27 câu giải thích máy móc và sửa lỗi 'N của...' cho Batch 1.")
