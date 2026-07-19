import csv

files = [
    'mondai2_ordering/csv_filled/set_1_daily/part_4.csv',
    'mondai2_ordering/csv_filled/set_1_daily/part_6.csv',
    'mondai2_ordering/csv_filled/set_1_daily/part_7.csv',
    'mondai2_ordering/csv_filled/set_1_daily/part_8.csv',
    'mondai2_ordering/csv_filled/set_1_daily/part_9.csv'
]

def check_csv(file_path):
    issues = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            header = next(reader)
            for row_idx, row in enumerate(reader, start=2):
                if len(row) != 12:
                    issues.append(f"Row {row_idx}: wrong number of columns ({len(row)} instead of 12)")
                    continue
                
                orig_example = row[4]
                chunk1 = row[6]
                explanation = row[11]
                
                # Check for （なし）
                for i, col in enumerate(row):
                    if "（なし）" in col or "(なし)" in col:
                        issues.append(f"Row {row_idx}: Contains (なし) in col {header[i]}")
                        
                # Check for prompt leakage
                lower_exp = explanation.lower()
                bad_phrases = ["dưới đây là", "here is", "sure", "câu ví dụ", "ví dụ trên", "tuy nhiên", "hy vọng", "cấu trúc"]
                for p in bad_phrases:
                    if p in lower_exp and "cấu trúc ngữ pháp cơ bản" in lower_exp:
                        issues.append(f"Row {row_idx}: Possible prompt leak '{p}' in explanation: {explanation[:30]}...")

                if "\n" in explanation:
                    issues.append(f"Row {row_idx}: Newline in explanation.")
                
                if "meas" in explanation or "..." in explanation:
                    issues.append(f"Row {row_idx}: Suspicious string in explanation.")
                
                # Missing closing quotes in Explanation
                if explanation.count('「') != explanation.count('」'):
                    issues.append(f"Row {row_idx}: Mismatched quotes in explanation: {explanation.count('「')} open vs {explanation.count('」')} close.")

                clean_chunk = chunk1.replace("、", "").replace("。", "").replace("「", "").replace("」", "").replace("？", "")
                clean_orig = orig_example.replace("、", "").replace("。", "").replace("「", "").replace("」", "").replace("？", "")
                if clean_chunk and clean_chunk not in clean_orig:
                    issues.append(f"Row {row_idx}: Chunk1 '{chunk1}' not in original example '{orig_example}'")
                    
    except Exception as e:
        issues.append(f"Error parsing {file_path}: {e}")
        
    if issues:
        print(f"--- Issues in {file_path} ---")
        for i in issues:
            print(i)
        print()
    else:
        print(f"{file_path} looks clean.")

for f in files:
    check_csv(f)
