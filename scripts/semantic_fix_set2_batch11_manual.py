import csv, os

dir_path = r'd:\pj\xx\ai-gen-quiz\mondai2_ordering\csv_filled\set_2_business'

fixes_part54 = {
    "Thứ tự kết hợp từ trái sang phải hoàn toàn tuân theo dòng chảy tự nhiên của nguồn tin và nội dung thông báo:": "Các thành phần liên kết tự nhiên theo trình tự nguồn tin và thông báo:",
    "Thứ tự thành phần câu đi thẳng từ chủ ngữ và hành động bổ nghĩa đến danh từ trung tâm:": "Mạch câu đi từ chủ ngữ và hành động bổ nghĩa thẳng đến danh từ trung tâm:",
    "Thứ tự sắp xếp tạo nên cấu trúc lặp đối xứng logic:": "Cấu trúc câu tạo nên sự lặp lại đối xứng:",
    "Thứ tự cú pháp đi từ căn cứ nhìn thấy đến nội dung suy đoán:": "Mạch câu đi từ căn cứ quan sát được đến nội dung suy đoán:",
    "Thứ tự logic theo trục thời gian:": "Các sự kiện diễn tiến theo thời gian:",
    "Thứ tự thành phần chuyển động từ hành động đề xuất sang phản ứng tiêu cực:": "Mạch câu chuyển từ hành động đề xuất sang phản ứng tiêu cực:",
    "Thứ tự sắp xếp từ vựng:": "Các thành phần liên kết chặt chẽ:",
    "Thứ tự cú pháp đi từ đối tượng lớn đến đối tượng nhỏ bị ảnh hưởng:": "Sự việc được diễn đạt đi từ đối tượng lớn đến đối tượng nhỏ bị ảnh hưởng:",
    "Thứ tự liên kết:": "Sự liên kết các thành phần:",
    "Thứ tự từ bổ nghĩa đến danh từ chính được sắp xếp theo đúng ngữ pháp:": "Từ bổ nghĩa đến danh từ chính được sắp xếp liền mạch:",
    "Thứ tự tiếp diễn tự nhiên theo dòng sự kiện:": "Các sự kiện tiếp diễn tự nhiên:",
    "Thứ tự kết hợp cấu trúc từ vựng tạo tân ngữ ghép và hành động diễn tiến:": "Việc kết hợp từ vựng tạo thành tân ngữ ghép và hành động diễn tiến:",
    "Thứ tự phân rã động từ thể 「～ていた」 kết hợp với danh từ chỉ thời điểm 「ところ」:": "Động từ thể 「～ていた」 kết hợp tự nhiên với danh từ chỉ thời điểm 「ところ」:",
    "Thứ tự liên kết:": "Các thành phần nối tiếp:",
    "Thứ tự logic:": "Mạch câu diễn tiến:",
    "Thứ tự sắp xếp bổ ngữ cấu thành hành động sai sót trước cấu trúc kết câu:": "Các bổ ngữ làm rõ hành động sai sót kết hợp chặt chẽ trước cấu trúc kết câu:",
    "Thứ tự kết hợp:": "Sự kết hợp các phần:",
    "Thứ tự phân cấp thông tin đi từ từ chuyển hướng đến tôn kính ngữ kết câu:": "Thông tin được dẫn dắt từ từ chuyển hướng cho đến tôn kính ngữ kết câu:"
}

# Fix part 54
file_54 = os.path.join(dir_path, 'part_54.csv')
if os.path.exists(file_54):
    with open(file_54, encoding='utf-8-sig') as f:
        r = list(csv.reader(f))
    headers = r[0]
    exp_idx = headers.index('Explanation') if 'Explanation' in headers else len(headers)-1
    changed = False
    for i, row in enumerate(r):
        if i == 0 or len(row) <= exp_idx: continue
        exp = row[exp_idx]
        for old, new in fixes_part54.items():
            if old in exp:
                exp = exp.replace(old, new)
                changed = True
        row[exp_idx] = exp
    if changed:
        with open(file_54, 'w', encoding='utf-8-sig', newline='') as f:
            csv.writer(f).writerows(r)

# Fix part 55
file_55 = os.path.join(dir_path, 'part_55.csv')
if os.path.exists(file_55):
    with open(file_55, encoding='utf-8-sig') as f:
        r = list(csv.reader(f))
    headers = r[0]
    exp_idx = headers.index('Explanation') if 'Explanation' in headers else len(headers)-1
    changed = False
    for i, row in enumerate(r):
        if i == 0 or len(row) <= exp_idx: continue
        exp = row[exp_idx]
        if "Thứ tự: (1)" in exp:
            row[exp_idx] = exp.replace("Thứ tự: (1)", "Mạch câu đi qua các bước: (1)")
            changed = True
    if changed:
        with open(file_55, 'w', encoding='utf-8-sig', newline='') as f:
            csv.writer(f).writerows(r)

print("Batch 11 fixes applied successfully!")
