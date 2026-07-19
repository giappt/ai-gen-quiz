import csv
import re

def fix():
    # part_76.csv
    file_path = 'mondai2_ordering/csv_filled/set_3_academic/part_76.csv'
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        rows = list(reader)
    
    for row in rows:
        if len(row) > 11:
            row[11] = row[11].replace('\"""', '').replace('"""', '').replace('"', '')
            if 'Đây là một cấu trúc ngữ pháp quan trọng' in row[11]:
                if row[0] == 'にも' and row[1] == 'V－ようにもV－れない':
                    row[4] = 'プロジェクトの予算が底をつき、新しい機材を導入しようにも導入できない状況です。'
                    row[5] = 'プロジェクトの予算が底をつき、'
                    row[6] = '新しい'
                    row[7] = '機材を導入しようにも'
                    row[8] = '導入できない'
                    row[9] = '状況'
                    row[10] = 'です。'
                    row[11] = '「V-ようにもV-れない」 biểu thị việc dù rất muốn làm một hành động nhưng do hoàn cảnh không cho phép nên không thể thực hiện. 「新しい機材を」 làm tân ngữ cho động từ ý chí 「導入しようにも」. Động từ khả năng phủ định 「導入できない」 bổ nghĩa cho danh từ kết câu 「状況です」.'
                elif row[0] == 'にもなく' and row[1] == 'Nにもなく':
                    row[4] = '普段は温厚な彼が、今日の会議では柄にもなく声を荒らげて反論した。'
                    row[5] = '普段は温厚な彼が、'
                    row[6] = '今日の会議では'
                    row[7] = '柄にもなく'
                    row[8] = '声を荒らげて'
                    row[9] = '反論'
                    row[10] = 'した。'
                    row[11] = '「柄にもなく」 là cụm từ cố định mang nghĩa \'không giống với bản tính/tính cách thường ngày\'. 「普段は温厚な彼が」 (anh ấy vốn dĩ điềm đạm) là chủ ngữ. Trạng từ 「柄にもなく」 bổ nghĩa cho chuỗi hành động bất ngờ phía sau là 「声を荒らげて反論した」 (lớn tiếng phản bác).'
            
            if '\。' in row[10] or '\。' in row[11] or '\。' in row[4]:
                row[4] = row[4].replace('\。', '。')
                row[10] = row[10].replace('\。', '。')
                row[11] = row[11].replace('\。', '。')
            if 'Layout' in row[4]:
                row[4] = row[4].replace('予測にLayoutによると', '予測によると').replace('予測にLayoutによると、', '予測によると、')
                row[7] = 'よると、'
                row[9] = '回復するとのことです'
                row[10] = '。'
                row[11] = row[11].replace('Layout', '')

    with open(file_path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(rows)

    # part_77.csv
    file_path = 'mondai2_ordering/csv_filled/set_3_academic/part_77.csv'
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        rows = list(reader)
    for row in rows:
        if len(row) > 11:
            row[11] = row[11].replace('『', '「').replace('』', '」')
    with open(file_path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(rows)

    # part_78.csv
    file_path = 'mondai2_ordering/csv_filled/set_3_academic/part_78.csv'
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        rows = list(reader)
    for row in rows:
        if len(row) > 11:
            if 'Đây là một cấu trúc ngữ pháp quan trọng' in row[11]:
                if row[1] == '～の＜確認＞':
                    row[4] = 'A：お疲れ様。あれ、まだ残業しているの？ B：ええ、明日のプレゼン資料を直しているんです。'
                    row[5] = 'A：お疲れ様。あれ、'
                    row[6] = 'まだ'
                    row[7] = '残業して'
                    row[8] = 'いる'
                    row[9] = 'の'
                    row[10] = '？ B：ええ、明日のプレゼン資料を直しているんです。'
                    row[11] = '「の」 đặt ở cuối câu dùng để xác nhận một sự thật đang diễn ra trước mắt một cách thân mật. Trong giao tiếp công sở giữa các đồng nghiệp thân thiết, người A hỏi xác nhận hành động 「残業している」 (đang làm thêm giờ) của B.'
                elif row[1] == '～の＜軽い命令＞　V－る／V－ないの':
                    row[4] = '明日は重要な商談があるんだから、今日はもう早く帰るの。'
                    row[5] = '明日は重要な商談があるんだから、'
                    row[6] = '今日は'
                    row[7] = 'もう早く'
                    row[8] = '帰る'
                    row[9] = 'の'
                    row[10] = '。'
                    row[11] = '「V-るの」 dùng để đưa ra lời chỉ thị nhẹ nhàng, khuyên bảo (thường từ cấp trên với cấp dưới hoặc người đi trước). Trạng từ 「早く」 bổ nghĩa cho động từ 「帰る」 (về sớm) kết hợp với 「の」 để nhắc nhở cấp dưới nghỉ ngơi chuẩn bị cho ngày mai.'
                elif row[1] == 'なのだったら　A／V　のだったら':
                    row[4] = '明日の会議に出席できないのだったら、事前に資料に目を通しておいてください。'
                    row[5] = '明日の会議に出席できない'
                    row[6] = 'の'
                    row[7] = 'だったら、'
                    row[8] = '事前に資料に'
                    row[9] = '目を通しておいて'
                    row[10] = 'ください。'
                    row[11] = '「のだったら」 được dùng để đưa ra điều kiện dựa trên một sự thật đã biết. Mệnh đề 「会議に出席できない」 (không thể tham gia cuộc họp) đi kèm 「のだったら」 (nếu mà như vậy). Vế sau đưa ra chỉ thị thay thế là 「事前に資料に目を通しておいてください」 (hãy đọc trước tài liệu).'
    with open(file_path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(rows)

    # part_79.csv
    file_path = 'mondai2_ordering/csv_filled/set_3_academic/part_79.csv'
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        rows = list(reader)
    for row in rows:
        if len(row) > 11:
            row[11] = row[11].replace('\"""', '').replace('"""', '').replace('"', '')
            if 'Đây là một cấu trúc ngữ pháp quan trọng' in row[11]:
                if row[1] == 'つまり～のです':
                    row[4] = '今回のプロジェクトは予算を大幅に超過しています。つまり、計画を一から見直す必要があるのです。'
                    row[5] = '今回のプロジェクトは予算を大幅に超過しています。つまり、'
                    row[6] = '計画を一から'
                    row[7] = '見直す'
                    row[8] = '必要が'
                    row[9] = 'ある'
                    row[10] = 'のです。'
                    row[11] = 'Từ nối 「つまり」 (tóm lại/có nghĩa là) được dùng để đúc kết vấn đề. Động từ 「見直す」 (xem xét lại) đi với 「必要がある」 (cần thiết phải), kết hợp đuôi 「のです」 để giải thích và nhấn mạnh mức độ nghiêm trọng của tình hình.'
                elif row[1] == 'だから～のだ':
                    row[4] = '彼はいつも締め切りを守りません。だから、今回の重要なタスクは彼に任せられなかったのです。'
                    row[5] = '彼はいつも締め切りを守りません。だから、'
                    row[6] = '今回の'
                    row[7] = '重要なタスクは'
                    row[8] = '彼に'
                    row[9] = '任せられなかった'
                    row[10] = 'のです。'
                    row[11] = 'Từ nối 「だから」 (vì thế) dẫn ra kết quả của sự việc vế trước. Động từ khả năng phủ định quá khứ 「任せられなかった」 (đã không thể giao phó) kết hợp với 「のです」 để thuyết minh và giải thích lý do cho một quyết định phân công nhân sự.'
                elif row[1] == '～のですから':
                    row[4] = '社長のご意向なのですから、この方針に従って進めるしかありません。'
                    row[5] = '社長の'
                    row[6] = 'ご意向'
                    row[7] = 'な'
                    row[8] = 'のです'
                    row[9] = 'から、'
                    row[10] = 'この方針に従って進めるしかありません。'
                    row[11] = 'Cấu trúc 「なのですから」 (vì là... nên đương nhiên) dùng để đưa ra một lý do hiển nhiên. Danh từ 「ご意向」 (ý hướng/quyết định) đi với 「な」. Vế sau 「進めるしかありません」 (chỉ còn cách tiến hành) thể hiện sự tuân thủ bắt buộc trong công việc.'
    with open(file_path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(rows)

if __name__ == "__main__":
    fix()
    print("Fixed batch 16 manually")
