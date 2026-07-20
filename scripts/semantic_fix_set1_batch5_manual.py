import csv
import os

dir_path = r'd:\pj\xx\ai-gen-quiz\mondai2_ordering\csv_filled\set_1_daily'

fixes = {
    "part_21.csv-2": "'これでは' nhấn mạnh hoàn cảnh bất lợi hiện tại (mưa to) dẫn đến hệ quả tiêu cực. Vế sau lần lượt đưa ra các thành phần bổ trợ: thời gian '今日の', mục đích '買い物に' và kết thúc bằng cụm trạng thái khả năng phủ định '行けそうにない'.",
    "part_21.csv-5": "Cấu trúc 'Nの際(は)' diễn tả thời điểm (khi làm gì đó). Trật tự câu bắt đầu từ địa điểm xảy ra 'デパートで', danh từ hành động '買い物の' kết hợp cấu trúc '際は', tiếp đến cụm định ngữ chỉ định danh từ tân ngữ 'こちらのポイントカードを' và kết thúc bằng động từ kính ngữ chỉ yêu cầu 'ご提示ください'.",
    "part_21.csv-11": "'さすがに' biểu thị một trạng thái tất yếu, không thể tránh khỏi do nguyên nhân rõ ràng từ vế trước mang lại. Vế sau được sắp xếp hợp lý: trạng từ thời gian đối chiếu '今日は' dẫn nhập cho chủ ngữ phụ của trạng thái '体力が', đi kèm danh từ kết luận '限界' và hệ từ 'だ'.",
    "part_22.csv-16": "Cấu trúc kết hợp liệt kê lý do khách quan '雨が降っているし' và lý do chủ quan từ phía bản thân '私は風邪気味だから'. Việc đưa hai lý do liên tiếp bằng 'し' và 'から' tạo ra căn cứ tự nhiên và vững chắc cho quyết định trì hoãn hành động ở vế cuối câu.",
    "part_23.csv-12": "'したがって' là liên từ biểu thị kết quả hợp lý mang tính khách quan (do đó). Câu trước nêu rõ quy định/nguyên nhân 'ペット禁止' dẫn đến kết quả tất yếu ở câu sau."
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
