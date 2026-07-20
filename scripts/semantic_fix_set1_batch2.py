import csv
import os
import re

dir_path = r'd:\pj\xx\ai-gen-quiz\mondai2_ordering\csv_filled\set_1_daily'
files_to_clean = ['part_6.csv', 'part_8.csv', 'part_9.csv', 'part_10.csv']
part7_file = 'part_7.csv'

# Data for part 7 regeneration
part7_data = [
    {
        "Original Example": "娘が希望の大学に合格し、親として喜びの至りです。",
        "Prefix": "娘が希望の大学に合格し、",
        "Chunk1": "親として",
        "Chunk2": "喜びの",
        "Chunk3": "至り",
        "Chunk4": "です。",
        "Suffix": "",
        "Explanation": "Cấu trúc 'Nの至り' (vô cùng, cực kỳ) đi liền với danh từ cảm xúc '喜び' để diễn tả niềm vui tột độ của bậc làm cha mẹ."
    },
    {
        "Original Example": "有機野菜が安全だと、一概には言えません。",
        "Prefix": "有機野菜が安全だと、",
        "Chunk1": "一概",
        "Chunk2": "には",
        "Chunk3": "言え",
        "Chunk4": "ません。",
        "Suffix": "",
        "Explanation": "Phó từ '一概には' (không thể đánh đồng/không thể nói tuyệt đối là) luôn đi kèm với thể phủ định '言えません' ở cuối câu."
    },
    {
        "Original Example": "あの店のラーメンは、一度食べたら病みつきになるよ。",
        "Prefix": "あの店のラーメンは、",
        "Chunk1": "一度",
        "Chunk2": "食べたら",
        "Chunk3": "病みつきに",
        "Chunk4": "なるよ。",
        "Suffix": "",
        "Explanation": "Phó từ '一度' (một khi đã) kết hợp với động từ thể điều kiện '食べたら' diễn tả việc nếu thử một lần thì sẽ dẫn đến kết quả ở vế sau."
    },
    {
        "Original Example": "こんなつまらない映画は、一度見れば十分だ。",
        "Prefix": "こんなつまらない映画は、",
        "Chunk1": "一度",
        "Chunk2": "見れば",
        "Chunk3": "十分",
        "Chunk4": "だ。",
        "Suffix": "",
        "Explanation": "'一度' kết hợp với động từ thể điều kiện '見れば' mang nghĩa 'chỉ cần xem một lần là đủ'."
    },
    {
        "Original Example": "テレビを見ている間に、いつか眠ってしまった。",
        "Prefix": "テレビを",
        "Chunk1": "見ている",
        "Chunk2": "間に、",
        "Chunk3": "いつか眠って",
        "Chunk4": "しまった。",
        "Suffix": "",
        "Explanation": "Phó từ 'いつか' (lúc nào không hay) bổ nghĩa cho hành động '眠ってしまった' diễn ra trong khoảng thời gian đang xem tivi."
    },
    {
        "Original Example": "この歌は、いつか聞いたことがある懐かしいメロディーだ。",
        "Prefix": "この歌は、",
        "Chunk1": "いつか",
        "Chunk2": "聞いた",
        "Chunk3": "ことが",
        "Chunk4": "ある",
        "Suffix": "懐かしいメロディーだ。",
        "Explanation": "'いつか' (trước đây, lúc nào đó trong quá khứ) kết hợp với động từ quá khứ '聞いた' để nhắc lại một trải nghiệm chưa rõ thời điểm."
    },
    {
        "Original Example": "いつかは自分の家を持ちたいと思っています。",
        "Prefix": "",
        "Chunk1": "いつか",
        "Chunk2": "は自分の家を",
        "Chunk3": "持ちたいと",
        "Chunk4": "思っています。",
        "Suffix": "",
        "Explanation": "'いつかは' (một ngày nào đó trong tương lai) thể hiện niềm hy vọng hay mơ ước, đi liền với động từ thể nguyện vọng '持ちたい'."
    },
    {
        "Original Example": "昨日、いつかのレストランで偶然彼に会った。",
        "Prefix": "昨日、",
        "Chunk1": "いつかの",
        "Chunk2": "レストランで",
        "Chunk3": "偶然彼に",
        "Chunk4": "会った。",
        "Suffix": "",
        "Explanation": "'いつかの' (của một ngày nào đó) đóng vai trò bổ nghĩa cho danh từ 'レストラン' để chỉ một địa điểm đã từng đến trong quá khứ."
    },
    {
        "Original Example": "薬を飲んだのに、一向に熱が下がらない。",
        "Prefix": "薬を飲んだのに、",
        "Chunk1": "一向に",
        "Chunk2": "熱が",
        "Chunk3": "下がら",
        "Chunk4": "ない。",
        "Suffix": "",
        "Explanation": "Phó từ '一向に' (hoàn toàn không) luôn đi kèm với thể phủ định '下がらない' để nhấn mạnh tình trạng không hề tiến triển dù đã uống thuốc."
    },
    {
        "Original Example": "私はその事件と一切関係がありません。",
        "Prefix": "私は",
        "Chunk1": "その事件と",
        "Chunk2": "一切",
        "Chunk3": "関係が",
        "Chunk4": "ありません。",
        "Suffix": "",
        "Explanation": "Phó từ '一切' (hoàn toàn không) kết hợp trực tiếp với thể phủ định 'ありません' nhằm phủ nhận hoàn toàn sự liên quan."
    },
    {
        "Original Example": "気がつくと、いつしか外は真っ暗になっていた。",
        "Prefix": "気がつくと、",
        "Chunk1": "いつしか",
        "Chunk2": "外は",
        "Chunk3": "真っ暗に",
        "Chunk4": "なっていた。",
        "Suffix": "",
        "Explanation": "Phó từ 'いつしか' (lúc nào không hay) thường dùng trong văn viết, miêu tả sự thay đổi trạng thái '真っ暗に' diễn ra một cách vô thức."
    },
    {
        "Original Example": "毎日満員電車に乗るくらいなら、いっそ会社の近くに引っ越したい。",
        "Prefix": "毎日満員電車に乗るくらいなら、",
        "Chunk1": "いっそ",
        "Chunk2": "会社の近くに",
        "Chunk3": "引っ越し",
        "Chunk4": "たい。",
        "Suffix": "",
        "Explanation": "'いっそ' (thà rằng) được dùng khi đưa ra một quyết định táo bạo thay cho tình trạng tồi tệ hiện tại, kết hợp với thể nguyện vọng '引っ越したい'."
    },
    {
        "Original Example": "迷っているなら、よりいっそのこと両方買ってみたらどう？",
        "Prefix": "迷っているなら、",
        "Chunk1": "より",
        "Chunk2": "いっそのこと",
        "Chunk3": "両方買って",
        "Chunk4": "みたらどう？",
        "Suffix": "",
        "Explanation": "'よりいっそのこと' nhấn mạnh hơn vào sự lựa chọn dứt khoát, đi kèm với lời khuyên '買ってみたらどう' ở cuối câu."
    },
    {
        "Original Example": "こんな夜中に、いったい誰がドアを叩いているのだろう。",
        "Prefix": "こんな夜中に、",
        "Chunk1": "いったい",
        "Chunk2": "誰が",
        "Chunk3": "ドアを叩いているの",
        "Chunk4": "だろう。",
        "Suffix": "",
        "Explanation": "Phó từ 'いったい' (rốt cuộc là) luôn đi với từ để hỏi '誰が' nhằm nhấn mạnh sự thắc mắc, tò mò cực độ của người nói."
    },
    {
        "Original Example": "彼女は、一旦怒り出すと誰にも止められない。",
        "Prefix": "彼女は、",
        "Chunk1": "一旦",
        "Chunk2": "怒り出すと",
        "Chunk3": "誰にも",
        "Chunk4": "止められない。",
        "Suffix": "",
        "Explanation": "Phó từ '一旦' kết hợp với động từ thể điều kiện '怒り出すと' mang nghĩa 'một khi đã... thì', diễn tả kết quả tất yếu khó tránh khỏi ở vế sau."
    },
    {
        "Original Example": "日本の人口は減る一方で、高齢者は増え続けている。",
        "Prefix": "日本の人口は",
        "Chunk1": "減る",
        "Chunk2": "一方で、",
        "Chunk3": "高齢者は",
        "Chunk4": "増え続けている。",
        "Suffix": "",
        "Explanation": "Cấu trúc 'V-る + 一方で' (mặt khác thì) thể hiện hai xu hướng trái ngược nhau đang diễn ra song song (giảm đi và tăng lên)."
    },
    {
        "Original Example": "彼は会社員として働く一方、夜は小説を書いている。",
        "Prefix": "彼は会社員として",
        "Chunk1": "働く",
        "Chunk2": "一方、",
        "Chunk3": "夜は小説を",
        "Chunk4": "書いている。",
        "Suffix": "",
        "Explanation": "'一方' (mặt khác) được dùng để nối hai mệnh đề, thể hiện một người đang song song thực hiện hai vai trò hoặc hành động cùng lúc."
    }
]

modifications = []

# 1. Regenerate part_7.csv
part7_path = os.path.join(dir_path, part7_file)
with open(part7_path, 'r', encoding='utf-8-sig') as f:
    reader = list(csv.DictReader(f))
    fieldnames = reader[0].keys() if len(reader) > 0 else []

for i, row in enumerate(reader):
    if i < len(part7_data):
        new_data = part7_data[i]
        for key in new_data:
            row[key] = new_data[key]
        modifications.append({
            "id": f"part_7.csv-{i+1}",
            "old": "(Empty Data)",
            "new": "Regenerated Quiz and Explanation"
        })

with open(part7_path, 'w', encoding='utf-8-sig', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(reader)


# 2. Clean up other files
def clean_explanation(text):
    original_text = text
    text = text.replace("N của あいだ", "Nのあいだ")
    text = text.replace("N của 後で", "Nのあとで")
    text = text.replace("N của ことを", "Nのことを")
    text = text.replace("N của こと", "Nのこと")

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
    
    text = re.sub(r'\s+([A-Z][a-z]+.*?\.)\s*$', r' \1', text).strip()
    return text

for file in files_to_clean:
    full_path = os.path.join(dir_path, file)
    with open(full_path, 'r', encoding='utf-8-sig') as f:
        reader = list(csv.DictReader(f))
        fieldnames = reader[0].keys() if len(reader) > 0 else []
        
    for index, row in enumerate(reader):
        file_id = f"{file}-{index + 1}"
        old_exp = row.get("Explanation", "")
        new_exp = clean_explanation(old_exp)
        
        if old_exp != new_exp:
            row["Explanation"] = new_exp
            modifications.append({
                "id": file_id,
                "old": old_exp,
                "new": new_exp
            })
            
    with open(full_path, 'w', encoding='utf-8-sig', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(reader)

# Write report
report_lines = ["# Semantic Review Report - Set 1 Batch 2\n"]
report_lines.append(f"Tổng số mục đã can thiệp: {len(modifications)}\n\n")

for mod in modifications:
    report_lines.append(f"### ID: {mod['id']}")
    report_lines.append(f"- **Cũ**: {mod['old']}")
    report_lines.append(f"- **Mới**: {mod['new']}\n")

with open(r'd:\pj\xx\ai-gen-quiz\review\set1_batch2_report.md', 'w', encoding='utf-8') as f:
    f.write('\n'.join(report_lines))

print(f"Done processing Set 1 Batch 2. Modified {len(modifications)} items.")
