import csv
import os

dir_path = r'd:\pj\xx\ai-gen-quiz\mondai2_ordering\csv_filled\set_1_daily'

fixes = {
    "part_17.csv-5": "Lý do '結婚式に参加できて' (tham gia được lễ cưới) đẩy cảm xúc của chủ ngữ '私は今' lên mức cao nhất, kết hợp với danh từ '幸福の' đi cùng 'きわみです' (tột cùng của hạnh phúc).",
    "part_17.csv-18": "Đưa ra phán đoán hợp lý dựa trên một mức độ thực tế. Khả năng '日本語の本をスラスラ読める' (đọc trơn tru sách tiếng Nhật) kết hợp 'くらいだから' làm điểm tựa vững chắc để suy ra kết luận 'かなり勉強したのだろう'.",
    "part_20.csv-12": "Vế đầu đưa ra điều kiện giả định phủ định '作らないなら'. Danh từ '外食' đi với cấu trúc 'ということになる' nhằm đưa ra một kết luận hợp lý mang tính tất yếu phát sinh từ điều kiện đó trong bối cảnh giao tiếp gia đình.",
    "part_19.csv-17": "Tính từ đuôi -na '真面目な' bổ nghĩa cho danh từ '彼女'. Cấu trúc 'Nのことだから' đứng ở giữa câu để đưa ra cơ sở tính cách cho lời phán đoán phía sau. Vế sau dùng phó từ 'きっと' (chắc chắn) đi với trạng từ hành động '遅れずに' (không trễ) và động từ '来ます'."
}

for file_id, fix_text in fixes.items():
    file_name, row_str = file_id.split('-')
    row_idx = int(row_str)
    full_path = os.path.join(dir_path, file_name)
    
    with open(full_path, 'r', encoding='utf-8-sig') as f:
        reader = list(csv.DictReader(f))
        fieldnames = reader[0].keys()
        
    reader[row_idx]["Explanation"] = fix_text
    
    with open(full_path, 'w', encoding='utf-8-sig', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(reader)
