import csv, os

dir_path = r'd:\pj\xx\ai-gen-quiz\mondai2_ordering\csv_filled\set_2_business'

fixes = {
    "part_33.csv-1": "Cấu trúc 'Vだけましだ' thể hiện ý nghĩa vẫn còn may mắn hoặc tốt chán so với tình huống tồi tệ hơn. Ở đây việc 'được lọt vào vòng tuyển chọn cuối cùng' (最終選考まで残った) đi kèm 'だけましだ' tạo thành cụm bổ nghĩa bổ sung cho kết quả thất bại trước đối thủ ở phần Prefix. Câu được hình thành bằng cách đi từ chủ ngữ '我が社の提案が' đến giới hạn '最終選考まで' và khép lại với vị ngữ ngữ pháp '残っただけましだ'.",
    "part_34.csv-7": "Mẫu ngữ pháp 'だなんて' đứng sau một mệnh đề thể hiện sự ngạc nhiên hoặc phủ định mạnh mẽ. Mạch câu đi từ Chủ ngữ '機密情報が', Trạng ngữ chỉ nơi chốn '外部に', Động từ thể hiện kết quả '漏れてしまった' và 'だなんて', dẫn tới vế sau thể hiện sự không thể tin nổi.",
    "part_34.csv-9": "Cấu trúc liệt kê song song 'AだのBだの' (nào là A nào là B, mang sắc thái than phiền). Mệnh đề thứ nhất '価格が高いだの' kết hợp với mệnh đề thứ hai '納期が遅いだのと言って' để làm rõ nội dung than phiền trước khi đi đến kết quả ở phần Suffix.",
    "part_34.csv-12": "Câu diễn tả áp lực công việc một cách tự nhiên: trạng từ chỉ tần suất '毎日のように' kết hợp trạng ngữ chỉ thời gian giới hạn '終電まで', bổ nghĩa cho cụm danh từ hóa hành động '残業するのは'. Phó từ nhấn mạnh '本当に' đi kèm tính từ 'たまらない' (không thể chịu nổi) ở phần kết thúc.",
    "part_34.csv-13": "Cấu trúc '～てたまらない' thể hiện cảm xúc/tâm trạng cực kỳ mãnh liệt không kìm nén được. Về mặt bổ nghĩa: Định ngữ '大手クライアントとの' bổ nghĩa cho '商談が', tiếp theo là mệnh đề nghi vấn lựa chọn '上手くいくか' làm nội dung cho trạng thái lo lắng '心配で', kết hợp trực tiếp với cấu trúc 'たまらない'.",
    "part_34.csv-14": "Cấu trúc N4 diễn tả mục đích/lợi ích 'Nのために'. Chuỗi danh từ sở hữu '新入社員の' -> '皆さんの' -> '成長の' kết nối chặt chẽ bằng trợ từ 'の', sau đó đi với cụm từ chỉ mục đích 'ために' để bổ nghĩa cho động từ bị động ở đuôi câu '企画されました'.",
    "part_34.csv-16": "Mẫu ngữ pháp cổ/trang trọng N1 '～んがため' (để/nhằm mục đích...). Các thành phần kết nối chặt chẽ: Cụm từ chỉ môi trường cạnh tranh '市場競争に' bổ nghĩa cho động từ thể cổ '生き残らん' (từ 生き残る), đi liền với 'がため' tạo thành vế chỉ mục đích, theo sau là tính từ bổ nghĩa '大規模な' bổ nghĩa cho cụm danh từ hành động ở Suffix."
}

leakage_str1 = " Câu được chia thành các phần tương ứng để kiểm tra khả năng sắp xếp trật tự từ ngữ pháp trong tiếng Nhật một cách chính xác nhất."
leakage_str2 = "Câu được chia thành các phần tương ứng để kiểm tra khả năng sắp xếp trật tự từ ngữ pháp trong tiếng Nhật một cách chính xác nhất."

files = ['part_31.csv', 'part_32.csv', 'part_33.csv', 'part_34.csv', 'part_35.csv']

for file in files:
    path = os.path.join(dir_path, file)
    with open(path, encoding='utf-8-sig') as f:
        r = list(csv.reader(f))
    
    headers = r[0]
    exp_idx = headers.index('Explanation') if 'Explanation' in headers else -1
    if exp_idx == -1: exp_idx = len(headers) - 1
    
    changed = False
    for i, row in enumerate(r):
        if i == 0: continue
        key = f"{file}-{i}"
        
        # Remove leakages globally
        if len(row) > exp_idx:
            orig = row[exp_idx]
            new = orig.replace(leakage_str1, "").replace(leakage_str2, "")
            if orig != new:
                row[exp_idx] = new
                changed = True
        
        # Specific fixes
        if key in fixes:
            new_exp = fixes[key]
            del row[exp_idx:]
            row.append(new_exp)
            changed = True
            
    if changed:
        with open(path, 'w', encoding='utf-8-sig', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(r)

print("Batch 7 of set 2 updated safely!")
