import csv
import os

dir_path = r'd:\pj\xx\ai-gen-quiz\mondai2_ordering\csv_filled\set_1_daily'

fixes = {
    "part_37.csv-17": "Trạng từ chỉ thời gian「夕方」. Cấu trúc「Nのついでに」lấy danh từ hành động「散歩」làm chính để chỉ việc nhân tiện. Vế sau là hành động kết hợp phụ: trạng ngữ nơi chốn「ポストに」, tân ngữ「手紙を」và cụm động từ「出してきた」.",
    "part_40.csv-14": "Cấu trúc 「V-ている」 diễn tả hành động đang tiếp diễn tại thời điểm nói. Vế sau được sắp xếp từ chủ đề kèm trạng từ 「外はまだ」 (bên ngoài vẫn), danh từ 「雨が」 (trời mưa) đi với động từ thể て 「降って」 và kết thúc bằng đuôi tiếp diễn lịch sự 「います」.",
    "part_40.csv-15": "Cấu trúc 「V-ている」 diễn tả trạng thái kết quả của một hành động vẫn còn tồn tại. Trật tự câu bắt đầu bằng chủ đề 「その店のドアは」 (cửa của cửa hàng đó), tiếp đến phó từ 「もう」 (đã), động từ thể て 「開いて」 (mở) và kết thúc bằng đuôi trạng thái 「います」.",
    "part_40.csv-16": "Cấu trúc 「V-ている」 diễn tả hành động đang diễn ra. Câu bắt đầu từ địa điểm 「公園で」, lượng từ 「たくさんの」 bổ nghĩa cho 「子供が」 (trẻ em), tiếp đó là động từ thể て 「遊んで」 và phần đuôi tiếp diễn 「います」.",
    "part_40.csv-17": "Cấu trúc 「Nをしている」 dùng để nói về nghề nghiệp hoặc vai trò. Trật tự câu gồm chủ ngữ 「私の兄は」 (anh trai tôi), cụm danh từ nghề nghiệp 「中学校の先生を」 (giáo viên trung học) và đuôi hành động trạng thái 「しています」.",
    "part_40.csv-20": "Cấu trúc 「V-ていない」 diễn tả trạng thái chưa hoàn thành. Trật tự câu gồm chủ ngữ 「私は」 (tôi), cụm trạng từ thời gian 「まだ今日の」 (vẫn chưa... của ngày hôm nay), tân ngữ 「宿題を」 (bài tập) và động từ đuôi phủ định 「していません」."
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
