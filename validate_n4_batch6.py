import csv
import sys
import glob

files = [
    'mondai2_ordering/csv_filled/set_1_daily/part_80.csv',
    'mondai2_ordering/csv_filled/set_1_daily/part_52.csv',
    'mondai2_ordering/csv_filled/set_1_daily/part_84.csv',
    'mondai2_ordering/csv_filled/set_1_daily/part_63.csv',
    'mondai2_ordering/csv_filled/set_1_daily/part_46.csv'
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
                chunk2 = row[7]
                chunk3 = row[8]
                chunk4 = row[9]
                explanation = row[11]
                
                # Check for （なし）
                for i, col in enumerate(row):
                    if "（なし）" in col or "(なし)" in col:
                        issues.append(f"Row {row_idx}: Contains (なし) in col {header[i]}")
                        
                # Check for prompt leakage
                lower_exp = explanation.lower()
                bad_phrases = ["dưới đây là", "here is", "sure", "câu ví dụ", "ví dụ trên", "tuy nhiên", "hy vọng", "cấu trúc"]
                for p in bad_phrases:
                    # 'cấu trúc' is often used naturally, so we just flag if it's the beginning of a weird sentence
                    if p in lower_exp and "cấu trúc ngữ pháp cơ bản" in lower_exp:
                        issues.append(f"Row {row_idx}: Possible prompt leak '{p}' in explanation: {explanation[:30]}...")

                # check if there's any newline in explanation (sometimes prompt leaks are multi-line)
                if "\n" in explanation:
                    issues.append(f"Row {row_idx}: Newline in explanation.")
                
                # check for hallucinated english words
                if "meas" in explanation or "..." in explanation:
                    issues.append(f"Row {row_idx}: Suspicious string in explanation.")
                
                # Check if chunks are in orig_example
                if chunk1 and chunk1 not in orig_example and chunk1.replace("、", "") not in orig_example:
                    # Ignore punctuation differences
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
