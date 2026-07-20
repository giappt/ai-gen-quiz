import csv, os

dir_path = r'd:\pj\xx\ai-gen-quiz\mondai2_ordering\csv_filled\set_2_business'

fixes = {
    "Thứ tự đúng là 1-2-3-4.": "Mạch câu vì thế được liên kết liền mạch.",
    "Thứ tự chuẩn là 1-2-3-4.": "Mạch câu vì thế được liên kết liền mạch.",
    "Thứ tự logic là 1-2-3-4.": "Mạch câu vì thế được liên kết liền mạch.",
    "Thứ tự tự nhiên là 1-2-3-4.": "Mạch câu vì thế được liên kết liền mạch.",
    "Thứ tự sắp xếp là 1-2-3-4.": "Mạch câu vì thế được liên kết liền mạch.",
    "Do đó thứ tự tự nhiên là Chunks 1-2-3-4.": "Do đó mạch câu được liên kết liền mạch.",
    "Thứ tự là 1-2-3-4.": "Mạch câu vì thế được liên kết liền mạch.",
    "Thứ tự hợp lý là 1-2-3-4.": "Mạch câu vì thế được liên kết liền mạch.",
    
    "Thứ tự cú pháp tự nhiên:": "Mạch câu diễn tiến tự nhiên:",
    "Thứ tự sắp xếp tự nhiên tuân theo quy tắc:": "Mạch câu diễn tiến tự nhiên:",
    "Thứ tự từ bắt buộc phải là": "Mạch câu đi từ",
    "Thứ tự câu chúc tụng chuẩn công sở:": "Mạch câu chúc tụng chuẩn công sở:",
    "Thứ tự cấu trúc câu:": "Cấu trúc câu:",
    "Thứ tự tự nhiên:": "Mạch câu diễn tiến tự nhiên:",
    "Thứ tự cấu trúc:": "Cấu trúc câu:",
    "Thứ tự sắp xếp logic:": "Mạch câu diễn tiến hợp lý:",
    "Thứ tự liên kết cú pháp:": "Các phần liên kết chặt chẽ:",
    "Thứ tự từ:": "Mạch câu diễn tiến:",
    "Thứ tự sắp xếp chuẩn cú pháp:": "Các phần liên kết chặt chẽ:",
    "Thứ tự tự nhiên sắp xếp các thành phần trạng ngữ và động từ trong tiếng Nhật:": "Mạch câu diễn tiến tự nhiên:",
    
    "được sắp xếp một cách tự nhiên theo thứ tự logic trước hành động chính.": "được liên kết một cách tự nhiên trước hành động chính.",
    "Thứ tự lập luận tự nhiên:": "Mạch lập luận diễn tiến tự nhiên:",
    "Thứ tự từ bổ nghĩa đến danh từ trung tâm hoàn toàn tự nhiên.": "Sự bổ nghĩa diễn tiến đến danh từ trung tâm hoàn toàn tự nhiên.",
    "Thứ tự được hình thành theo nguyên tắc bổ nghĩa liên tiếp:": "Mạch câu được hình thành theo nguyên tắc bổ nghĩa liên tiếp:",
    "Sắp xếp theo logic mục đích - hành động:": "Cấu trúc được liên kết theo logic mục đích - hành động:",
    "Sắp xếp theo cấu trúc định nghĩa lại bản chất sự việc:": "Mạch câu được hình thành theo cấu trúc định nghĩa lại bản chất sự việc:",
    "Trật tự từ bổ nghĩa cho hành động cấm đoán:": "Mạch câu bổ nghĩa cho hành động cấm đoán:",
    "Sắp xếp theo lập luận phán đoán:": "Mạch lập luận phán đoán:",
    "Trật tự câu đánh giá tính khả thi của kế hoạch:": "Mạch câu đánh giá tính khả thi của kế hoạch:",
    "Sắp xếp theo cấu trúc miêu tả tính chất và hệ quả trạng thái:": "Mạch câu miêu tả tính chất và hệ quả trạng thái:",
    "Sắp xếp theo quy tắc phó từ phủ định tần suất:": "Mạch câu diễn tiến theo quy tắc phó từ phủ định tần suất:",
    "Sắp xếp theo cấu trúc khẳng định tính nghiêm trọng, khó thay đổi:": "Mạch câu khẳng định tính nghiêm trọng, khó thay đổi:",
    "Thứ tự kết hợp:": "Sự kết hợp các phần:"
}

leakage_str1 = " Cấu trúc ngữ pháp cơ bản. Câu được chia thành các phần tương ứng để kiểm tra khả năng sắp xếp trật tự từ ngữ pháp trong tiếng Nhật một cách chính xác nhất."
leakage_str2 = "Câu được chia thành các phần tương ứng để kiểm tra khả năng sắp xếp trật tự từ ngữ pháp trong tiếng Nhật một cách chính xác nhất."
leakage_str3 = " 今回の国家規模の Câu được chia thành các phần tương ứng để kiểm tra khả năng sắp xếp trật tự từ ngữ pháp trong tiếng Nhật một cách chính xác nhất."

for i in range(81, 96):
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
        
        new_exp = exp.replace(leakage_str3, "").replace(leakage_str1, "").replace(leakage_str2, "")
        
        for old, new in fixes.items():
            if old in new_exp:
                new_exp = new_exp.replace(old, new)
                
        if exp != new_exp:
            row[exp_idx] = new_exp
            changed = True
            
    if changed:
        with open(path, 'w', encoding='utf-8-sig', newline='') as f:
            csv.writer(f).writerows(r)

print("Batches 17, 18, 19 fixed successfully!")
