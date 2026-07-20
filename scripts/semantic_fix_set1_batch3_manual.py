import csv
import os

dir_path = r'd:\pj\xx\ai-gen-quiz\mondai2_ordering\csv_filled\set_1_daily'

fixes = {
    "part_11.csv-4": "Cụm định ngữ '一人で暮らしている' bổ nghĩa trực tiếp cho danh từ '祖母'. Cấu trúc 'Nのことを思う' (nghĩ về ai đó) đi liền với trợ từ 'と' để thiết lập mối quan hệ hệ quả tự nhiên (hễ nghĩ về... là liền có cảm xúc ở vế sau).",
    "part_11.csv-8": "Cụm hành động trạng thái '晴れていた' kết hợp với mẫu 'と思ったら' tạo thành cấu trúc chỉ sự thay đổi đột ngột (vừa mới thấy... thì đã). Vế sau bắt đầu bằng phó từ '急に' bổ nghĩa cho cụm chủ vị '大雨が降り出してくる' để mô tả sự biến đổi bất ngờ của thời tiết.",
    "part_12.csv-5": "Cấu trúc 'NがNだけに' nhấn mạnh tính chất đặc trưng đặc biệt của danh từ (chính vì là ngày cuối tuần), làm lý do chính đáng cho trạng thái đông đúc của trung tâm thương mại.",
    "part_12.csv-19": "'お小遣いには限りがある' đưa ra một sự thật khách quan về giới hạn tiền bạc, liên từ 'から' nối mệnh đề này với lời khuyên mang tính tự nhiên ở mệnh đề sau.",
    "part_15.csv-15": "Mệnh đề chứa lý do cốt lõi '家族が応援してくれるからこそ' (chính vì được gia đình ủng hộ) được đưa lên đầu câu để nhấn mạnh. Vế sau diễn tiến tự nhiên: Trạng ngữ chủ ngữ '私は毎日' (tôi mỗi ngày) đi với cụm tân ngữ - động từ khả năng '仕事を頑張れる' (có thể cố gắng trong công việc)."
}

for file_id, fix_text in fixes.items():
    file_name, row_str = file_id.split('-')
    row_idx = int(row_str) - 1
    full_path = os.path.join(dir_path, file_name)
    
    with open(full_path, 'r', encoding='utf-8-sig') as f:
        reader = list(csv.DictReader(f))
        fieldnames = reader[0].keys()
        
    reader[row_idx]["Explanation"] = fix_text
    
    with open(full_path, 'w', encoding='utf-8-sig', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(reader)

print(f"Hoàn tất sửa {len(fixes)} câu giải thích cho Batch 3.")
