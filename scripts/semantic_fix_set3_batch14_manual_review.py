import csv, os

dir_path = r'd:\pj\xx\ai-gen-quiz\mondai2_ordering\csv_filled\set_3_academic'

rewrites = {
    # part_69.csv
    "Cụm từ cố định 「なんということもなく」 mang nghĩa không có gì đặc biệt hoặc diễn ra suôn sẻ. Được tách thành các khúc cú pháp tự nhiên để bổ nghĩa cho trạng từ chỉ cách thức 「予定通りに」 đứng trước động từ trang trọng 「終了いたしました」.":
    "Cụm từ cố định 「なんということもなく」 mang nghĩa không có gì đặc biệt hoặc diễn ra suôn sẻ. Cụm từ này được dùng để mở đầu, dẫn dắt tự nhiên cho trạng từ chỉ cách thức 「予定通りに」 và động từ trang trọng kết thúc câu 「終了いたしました」.",
    
    # part_70.csv
    "Cấu trúc phó từ 「なんら」 đi kèm với thể phủ định 「しない」 nhằm nhấn mạnh ý nghĩa 「hoàn toàn không...」. Thứ tự kết hợp logic trong câu công sở: Chủ ngữ 「仕様変更は」 -> Cụm sở hữu bổ nghĩa 「当方の」 đi với danh từ đối tượng 「開発計画に」 -> Phó từ định ngữ 「なんら」 đứng trước động từ phủ định định vị kết quả 「影響しない」 -> Kết thúc bằng cụm nhận định khách quan 「と考えられます」.":
    "Cấu trúc phó từ 「なんら」 đi kèm với thể phủ định nhằm nhấn mạnh ý nghĩa 「hoàn toàn không...」. Mạch câu đi từ chủ ngữ 「仕様変更は」 đến cụm đối tượng chịu tác động 「当方の開発計画に」. Sau đó, phó từ 「なんら」 đứng ngay trước động từ phủ định 「影響しない」, khép lại bằng nhận định khách quan 「と考えられます」.",
    
    "Hình thức 「R-にV」 (với R là thể ます bỏ ます của động từ, và V là cùng động từ đó chia thể quá khứ hoặc hiện tại) dùng để nhấn mạnh mức độ lặp lại hoặc sự kỹ lưỡng tối đa của hành động. Ở đây 「練りに練った」 nghĩa là hoạch định vô cùng kỹ càng. Thứ tự cú pháp: Trạng từ thời gian và mức độ 「今回、長期間」 -> Tính ngữ bổ nghĩa cấu trúc lặp 「練りに練った」 bổ nghĩa cho danh từ chủ ngữ 「事業計画書が」 -> Nơi chốn/phương tiện thông qua 「取締役会で」 -> Động từ bị động kính ngữ kết câu 「承認されました」.":
    "Hình thức 「R-にV」 được dùng để nhấn mạnh sự kỹ lưỡng tối đa của hành động (ví dụ 「練りに練った」 là hoạch định vô cùng kỹ càng). Khởi đầu câu là trạng từ 「今回、長期間」 và cấu trúc lặp 「練りに練った」 bổ nghĩa cho chủ ngữ 「事業計画書が」. Cụm nơi chốn 「取締役会で」 được đặt trước động từ bị động kính ngữ kết câu 「承認されました」.",
    
    "Ngữ pháp 「V-るにV-れない」 biểu thị tình trạng dù rất muốn làm một hành động nào đó nhưng do hoàn cảnh ràng buộc nên không thể thực hiện được. Vế 「断るに断れない」 nghĩa là muốn từ chối mà bất khả kháng không thể từ chối. Trình tự logic: Vế nguyên nhân khách quan 「急な依頼なだけに」 -> Định ngữ chỉ đối tượng 「今回の案件は」 -> Cụm ngữ pháp lưỡng lự chọn lựa 「断るに断れない」 đóng vai trò định ngữ bổ nghĩa cho danh từ chỉ thực tế 「状況」 -> Động từ trạng thái 「にあります」.":
    "Ngữ pháp 「V-るにV-れない」 biểu thị tình trạng muốn nhưng không thể thực hiện vì hoàn cảnh (ví dụ 「断るに断れない」 là muốn từ chối cũng không được). Câu diễn tiến logic từ nguyên nhân 「急な依頼なだけに」 sang đối tượng 「今回の案件は」. Sau đó, cụm ngữ pháp lưỡng lự 「断るに断れない」 làm định ngữ bổ nghĩa cho danh từ thực tế 「状況」 và động từ trạng thái 「にあります」.",
    
    "Mẫu 「～にあたり」 là dạng văn viết, trang trọng hơn của 「にあたって」, thường thấy trong các thông báo, văn bản công sở. Trình tự cú pháp diễn tiến tự nhiên: Định ngữ thời gian tương lai 「次半期の」 -> Cụm danh từ chỉ sự kiện công nghệ 「新システムの導入に」 đi kèm quán ngữ chỉ bối cảnh chuẩn bị 「あたり」 -> Cụm tân ngữ xác định đối tượng phục vụ 「全社員向けの研修を」 -> Động từ khiêm nhường ngữ trang trọng kết câu 「実施いたします」.":
    "Mẫu 「～にあたり」 là dạng văn viết trang trọng của 「にあたって」, thường dùng trong văn bản công sở. Câu dẫn dắt tự nhiên từ thời gian 「次半期の」 đến sự kiện 「新システムの導入に」 kèm quán ngữ bối cảnh 「あたり」. Phần sau chỉ rõ đối tượng phục vụ qua tân ngữ 「全社員向けの研修を」 và động từ khiêm nhường trang trọng 「実施いたします」.",
    
    "Ngữ pháp 「Nにあっても」 mang ý nghĩa nhượng bộ 「ngay cả trong hoàn cảnh N đặc biệt/bất lợi đi chăng nữa」. Thứ tự sắp xếp câu: Cụm bổ nghĩa định hình tính chất 「今回のような不測の」 gắn với danh từ bối cảnh 「事態に」 -> Liên từ nhượng bộ ngữ pháp 「あっても」 -> Cụm danh từ chủ ngữ vế sau 「冷静な対応が」 -> Động từ bị động khách quan chỉ quy định/yêu cầu 「求められます」.":
    "Ngữ pháp 「Nにあっても」 mang ý nghĩa nhượng bộ (ngay cả trong hoàn cảnh N đặc biệt). Sự việc bắt đầu bằng bối cảnh 「今回のような不測の事態に」 kết hợp với liên từ nhượng bộ 「あっても」. Vế tiếp theo nhấn mạnh chủ ngữ 「冷静な対応が」 và động từ bị động khách quan chỉ quy định 「求められます」.",
    
    "Động từ định ngữ 「に至る」 diễn tả kết quả đạt đến một trạng thái hoặc mốc cụ thể sau một quá trình dài. Thứ tự logic câu: Cụm thời gian kéo dài 「数ヶ月に及ぶ」 bổ nghĩa cho danh từ tiến trình 「交渉を」 -> Động từ liên kết chuỗi thời gian 「経て」 -> Trạng từ và danh từ đích đến 「ようやく最終合意に」 -> Động từ kết quả đóng vai trò bổ nghĩa bổ ngữ 「至る」 -> Cụm danh từ chỉ viễn cảnh kết câu 「見通しとなりました」.":
    "Động từ định ngữ 「に至る」 diễn tả kết quả đạt đến sau một quá trình dài. Logic câu xuất phát từ thời gian kéo dài 「数ヶ月に及ぶ」 bổ nghĩa cho tiến trình 「交渉を」 và động từ liên kết 「経て」. Đích đến 「ようやく最終合意に」 đi liền với động từ kết quả 「至る」, trở thành cụm bổ nghĩa cho viễn cảnh kết câu 「見通しとなりました」.",
    
    "Mẫu 「～に至っても」 diễn tả sự phê phán hoặc kinh ngạc: 「ngay cả khi tình hình đã tồi tệ đến mức... mà vẫn không thay đổi hành vi」. Thứ tự kết hợp câu: Cụm bổ ngữ hành động khởi đầu 「クライアントから正式な抗議を」 -> Cụm động từ bổ nghĩa danh từ sự cố 「受ける事態に」 -> Cấu trúc nhượng bộ tương phản ngữ pháp 「至っても」 -> Tân ngữ bổ nghĩa vế sau 「適切な対応を」 -> Cụm vị ngữ phủ định kèm phán đoán khách quan kết câu 「行わなかったようです」.":
    "Mẫu 「～に至っても」 diễn tả sự phê phán: ngay cả khi tình hình đã tồi tệ đến mức... mà vẫn không thay đổi. Câu mở đầu bằng bối cảnh 「クライアントから正式な抗議を受ける事態に」 kết hợp với cấu trúc nhượng bộ tương phản 「至っても」. Vế sau tiếp nối bằng tân ngữ 「適切な対応を」 và cụm vị ngữ phủ định phán đoán 「行わなかったようです」.",
    
    "Mẫu 「Nにおいて」 ở đây dùng để khoanh vùng khía cạnh, lĩnh vực hoặc năng lực được đem ra đánh giá, so sánh (「về mặt.../ trong lĩnh vực...」). Thứ tự cú pháp logic: Định ngữ nội dung thương mại 「製造コストの」 bổ nghĩa danh từ khía cạnh kèm cấu trúc 「削減において」 -> Chủ ngữ tự xưng trang trọng 「弊社は」 -> Cụm đối tượng đối chiếu cạnh tranh 「競合他社に対して」 -> Cụm tân ngữ kết quả 「大きな優位性を」 -> Động từ khiêm nhường ngữ trạng thái kết câu 「持っております」.":
    "Mẫu 「Nにおいて」 dùng để khoanh vùng khía cạnh được đánh giá (về mặt...). Khía cạnh đó được nêu rõ qua cụm 「製造コストの削減において」. Tiếp đến, chủ ngữ 「弊社は」 (công ty chúng tôi) so sánh với đối thủ cạnh tranh 「競合他社に対して」, dẫn tới kết quả tân ngữ 「大きな優位性を」 và động từ khiêm nhường trạng thái 「持っております」.",
    
    "Cấu trúc 「Nに応じて」 diễn tả sự điều chỉnh, thay đổi sao cho tương thích và phù hợp với sự biến đổi của N (「tùy theo.../ ứng với...」). Thứ tự câu chuẩn mực kinh doanh: Định ngữ kế hoạch tương lai 「来期の」 bổ nghĩa chủ ngữ câu hành động 「予算配分は」 -> Cụm sở hữu bộ phận 「各プロジェクトの」 đi liền danh từ tiêu chuẩn thay đổi kèm ngữ pháp 「進捗状況に応じて」 -> Phó từ cách thức thích ứng 「柔軟に」 -> Động từ khiêm nhường ngữ thể hiện quyết tâm tổ chức kết câu 「決定いたします」.":
    "Cấu trúc 「Nに応じて」 diễn tả sự điều chỉnh sao cho tương thích với sự biến đổi (tùy theo...). Câu chuẩn mực này bắt đầu bằng chủ ngữ 「来期の予算配分は」. Cơ sở điều chỉnh được xác định qua cụm tiêu chuẩn 「各プロジェクトの進捗状況に応じて」. Sau đó, phó từ cách thức 「柔軟に」 bổ trợ mạnh mẽ cho động từ quyết định 「決定いたします」 ở cuối câu."
}

for i in range(66, 71):
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

print("Batch 14 manually reviewed and rewritten successfully!")
