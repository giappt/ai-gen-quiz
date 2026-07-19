import csv
import sys
import glob

files = [
    'mondai2_ordering/csv_filled/set_1_daily/part_18.csv',
    'mondai2_ordering/csv_filled/set_1_daily/part_98.csv',
    'mondai2_ordering/csv_filled/set_1_daily/part_97.csv',
    'mondai2_ordering/csv_filled/set_1_daily/part_25.csv',
    'mondai2_ordering/csv_filled/set_1_daily/part_31.csv'
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
                bad_phrases = ["dưới đây là", "here is", "sure", "câu ví dụ", "ví dụ trên", "tuy nhiên", "hy vọng"]
                for p in bad_phrases:
                    if p in lower_exp:
                        issues.append(f"Row {row_idx}: Possible prompt leak '{p}' in explanation: {explanation[:30]}...")

                # check if there's any newline in explanation (sometimes prompt leaks are multi-line)
                if "\n" in explanation:
                    issues.append(f"Row {row_idx}: Newline in explanation.")
                
                # Check missing quotes in explanation if it contains commas?
                # The csv module handles quotes, if there was an issue, it would be misaligned columns.
                
                # Check if chunks are in orig_example
                if chunk1 and chunk1 not in orig_example and chunk1.replace("、", "") not in orig_example:
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
