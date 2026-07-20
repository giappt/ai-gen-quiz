import csv
import os
import re

dir_path = r'd:\pj\xx\ai-gen-quiz\mondai2_ordering\csv_filled\set_1_daily'
files = ['part_1.csv', 'part_2.csv', 'part_3.csv', 'part_4.csv', 'part_5.csv']

hardcoded_fixes = {
    # Replace entire explanations that are too robotic or don't use colons
    'part_2.csv-3': "Mẫu 'V-たあとから' diễn tả sự việc xảy ra muộn màng ngay sau khi một quyết định đã được ấn định. Trong câu, hành động gốc '決めた' (đã quyết định) nối với 'あとから', tiếp đến là vế sau diễn tả sự phiền toái '時間を変更したいと言われても困るよ' (dù có bị nói là muốn đổi giờ thì cũng kẹt lắm).",
    'part_2.csv-6': "Mẫu 'あとから' đóng vai trò là trạng từ chỉ thời gian, mang ý nghĩa thực hiện hành động muộn hơn người khác (theo sau). Câu ví dụ được cấu trúc tự nhiên: Chủ ngữ '私は' đi kèm trạng từ 'あとから', 'すぐに' (ngay lập tức) và kết thúc bằng động từ chính '追いかける' (đuổi theo).",
    'part_2.csv-7': "Trạng từ 'あとで' chỉ một thời điểm trong tương lai gần (lát nữa, sau). Trong câu, chủ đề '宿題は' (bài tập thì) được đưa lên đầu, kết hợp với trạng từ thời gian 'あとで', trạng từ cách thức 'まとめて' (làm gộp lại) và động từ 'やる' (làm) đi kèm cấu trúc dự định 'つもりだ'.",
    'part_2.csv-12': "'あんまりにも' đi kèm và bổ nghĩa cho cụm trạng từ thời gian '夜遅く' và động từ điều kiện '寝ると' (nếu ngủ quá muộn). Vế sau thể hiện hệ quả tất yếu đối với chủ ngữ '次の日の朝が' đi với tính từ '辛いよ' (sáng hôm sau sẽ rất vất vả).",
    'part_4.csv-2': "'言うまでもないことだが' đứng đầu câu đóng vai trò là cụm từ dẫn dắt một sự thật hiển nhiên (không cần phải nói cũng biết). Phía sau là cấu trúc so sánh hơn '買うほうが' làm chủ ngữ, kết thúc bằng tính từ '安い' (việc mua ở siêu thị này thì rẻ hơn).",
}

def clean_explanation(file_id, text):
    if file_id in hardcoded_fixes:
        return hardcoded_fixes[file_id]

    original_text = text
    
    # 1. Replace "N của ..."
    text = text.replace("N của あいだ", "Nのあいだ")
    text = text.replace("N của 後で", "Nのあとで")
    text = text.replace("N của ことを", "Nのことを")
    text = text.replace("N của こと", "Nのこと")

    # 2. Remove robotic sequence descriptions
    # Patterns to match sentences starting with "Thứ tự", "Câu cấu trúc theo", "Cú pháp chia tách"
    # and stopping at the end of the text. 
    # Usually these are the last sentence in the explanation.
    patterns = [
        r"(?:Thứ tự|Cú pháp chia tách|Câu cấu trúc theo).*?(?:[:+->]).*$",
        r"Thứ tự logic:.*$",
        r"Thứ tự cấu trúc:.*$",
        r"Thứ tự kết hợp tự nhiên:.*$",
        r"Thứ tự bổ nghĩa bắt buộc:.*$",
        r"Thứ tự tự nhiên:.*$",
        r"Thứ tự:.*$",
    ]
    
    for p in patterns:
        text = re.sub(p, "", text, flags=re.IGNORECASE).strip()
    
    # Remove any trailing empty sentences if they exist
    text = re.sub(r'\s+([A-Z][a-z]+.*?\.)\s*$', r' \1', text).strip()
    
    return text

modifications = []

for file in files:
    full_path = os.path.join(dir_path, file)
    
    with open(full_path, 'r', encoding='utf-8') as f:
        reader = list(csv.DictReader(f))
        fieldnames = reader[0].keys() if len(reader) > 0 else []
        
    for index, row in enumerate(reader):
        file_id = f"{file}-{index + 1}"
        old_exp = row.get("Explanation", "")
        new_exp = clean_explanation(file_id, old_exp)
        
        if old_exp != new_exp:
            row["Explanation"] = new_exp
            modifications.append({
                "id": file_id,
                "old": old_exp,
                "new": new_exp
            })
            
    # Write back
    with open(full_path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(reader)

# Write report
report_lines = ["# Semantic Review Report - Set 1 Batch 1\n"]
report_lines.append(f"Tổng số câu đã sửa: {len(modifications)}\n\n")

for mod in modifications:
    report_lines.append(f"### ID: {mod['id']}")
    report_lines.append(f"- **Nguyên nhân sửa**: Lỗi diễn đạt máy móc (liệt kê thứ tự) hoặc lỗi gọi sai tên ngữ pháp ('N của...').")
    report_lines.append(f"- **Cũ**: {mod['old']}")
    report_lines.append(f"- **Mới**: {mod['new']}\n")

with open(r'd:\pj\xx\ai-gen-quiz\review\set1_batch1_report.md', 'w', encoding='utf-8') as f:
    f.write('\n'.join(report_lines))

print(f"Done processing Set 1 Batch 1. Modified {len(modifications)} items.")
