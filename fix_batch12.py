import csv
import re
import os

base_dir = '/home/kakashi/sources/pj/ai-gen-quiz/mondai2_ordering/csv_filled/set_2_business/'

def fix_quotes(text):
    # Replace single quotes with Japanese brackets
    while "'" in text:
        text = text.replace("'", "「", 1)
        text = text.replace("'", "」", 1)
    
    # Fix missing opening quotes (like `先ほど」`)
    # If the text starts with some characters then 」 without a matching 「 before it
    # We will use regex to find sequences ending with 」 but missing 「
    # Actually, a simpler way: just check if the very first quote is 」
    if text.find("」") != -1:
        first_close = text.find("」")
        first_open = text.find("「")
        if first_open == -1 or first_close < first_open:
            # Missing opening quote, likely at the beginning of the string or word
            # Let's just use regex to fix: `word」` -> `「word」` where it's at the start of explanation
            text = re.sub(r'^([^「]+)」', r'「\1」', text)
    
    return text

def process_file(file_name):
    file_path = os.path.join(base_dir, file_name)
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        rows = list(reader)
    
    for i in range(1, len(rows)):
        row = rows[i]
        if len(row) < 12:
            continue
        
        # Specific fixes
        if file_name == 'part_56.csv':
            if "社外秘 of 書類は" in row[4]:
                row[4] = row[4].replace("社外秘 of 書類は", "社外秘の書類は")
                row[5] = row[5].replace("社外秘 of 書類は", "社外秘の書類は")
            if "120台u" in row[11]:
                row[11] = row[11].replace("120台u", "120台")
            if i == 9: # Row 10 (0-indexed 9)
                if row[0] == 'とすると' and 'だとすると' in row[1]:
                    # Manually fix line 10
                    row[4] = 'A「明日の午前中までに必要だそうです。」B「だとすると、今夜は残業しなければなりませんね。」'
                    row[5] = 'A「明日の午前中までに必要だそうです。」B「'
                    row[10] = 'なりませんね。」'
                    row[11] = 'Liên từ 「だとすると」 đứng đầu câu của người B đóng vai trò nối phản hồi lại thông tin của người A. Cụm 「今夜は残業」 kết hợp cấu trúc bắt buộc 「しなければなりません」 biểu thị việc phải tăng ca.'
        
        if file_name == 'part_58.csv':
            row[11] = row[11].replace("N của こととなると", "Nのこととなると")
        
        row[11] = fix_quotes(row[11])

    with open(file_path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(rows)
    print(f"Fixed {file_name}")

for i in range(56, 61):
    process_file(f'part_{i}.csv')
