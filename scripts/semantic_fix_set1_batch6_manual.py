import csv
import os

dir_path = r'd:\pj\xx\ai-gen-quiz\mondai2_ordering\csv_filled\set_1_daily'

fixes = {
    "part_26.csv-18": "「宿題を」 là tân ngữ của 「忘れた」. 「忘れたのを」 cụm danh từ hóa việc quên bài tập làm đối tượng bị tác động. 「いつも」 là trạng từ tần suất. Cấu trúc 「Nのせいにする」 mang nghĩa đổ lỗi cho ai đó, ở đây là người anh/em trai đổ lỗi cho em gái trong cuộc sống gia đình thường nhật.",
    "part_28.csv-4": "Thể hiện hệ quả hợp lý từ lời nói của đối phương. Từ hành động đi mua sắm bây giờ, người B dùng 'そうすると' để chỉ ra kết quả muộn giờ cơm.",
    "part_29.csv-7": "Liên từ biểu thị trình tự hành động trước sau 'それから' (Sau đó) đứng đầu câu thứ hai. Vế sau lần lượt là trạng từ chỉ địa điểm 'スーパーで', danh từ bổ nghĩa '夕食の' đi kèm tân ngữ '買い物を' và kết thúc bằng động từ hành động 'した'.",
    "part_30.csv-17": "'それゆえ' (do đó) chỉ nguyên nhân và kết quả một cách hợp lý. Định ngữ '子育て世代の' bổ nghĩa cho danh từ '家族に' (đối tượng hướng tới). Phó từ 'とても' bổ nghĩa cho cụm từ chỉ trạng thái '人気があります'."
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
