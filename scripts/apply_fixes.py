import json
import csv
import os

dir_path = r'd:\pj\xx\ai-gen-quiz\mondai2_ordering\csv_filled\set_1_daily'

with open(r'd:\pj\xx\ai-gen-quiz\scratch\fixes_1.json', 'r', encoding='utf-8') as f:
    fixes = json.load(f)

with open(r'd:\pj\xx\ai-gen-quiz\scratch\fixes_2.json', 'r', encoding='utf-8') as f:
    fixes.update(json.load(f))

# Map file names to the rows that need updating
files_to_update = {}
for fix_id, fix_data in fixes.items():
    file_name, row_str = fix_id.split('-')
    row_idx = int(row_str) - 1
    if file_name not in files_to_update:
        files_to_update[file_name] = {}
    files_to_update[file_name][row_idx] = fix_data

total_injected = 0

for file_name, updates in files_to_update.items():
    full_path = os.path.join(dir_path, file_name)
    with open(full_path, 'r', encoding='utf-8-sig') as f:
        reader = list(csv.DictReader(f))
        fieldnames = reader[0].keys()
        
    for row_idx, fix_data in updates.items():
        if row_idx >= len(reader):
            print(f"Error: row_idx {row_idx} >= len {len(reader)} in {file_name}")
            continue
        row = reader[row_idx]
        # Build original example
        orig = f"{fix_data['Prefix']}{fix_data['Chunk1']}{fix_data['Chunk2']}{fix_data['Chunk3']}{fix_data['Chunk4']}{fix_data['Suffix']}"
        row["Original Example"] = orig
        row["Prefix"] = fix_data["Prefix"]
        row["Chunk1"] = fix_data["Chunk1"]
        row["Chunk2"] = fix_data["Chunk2"]
        row["Chunk3"] = fix_data["Chunk3"]
        row["Chunk4"] = fix_data["Chunk4"]
        row["Suffix"] = fix_data["Suffix"]
        row["Explanation"] = fix_data["Explanation"]
        total_injected += 1
        
    with open(full_path, 'w', encoding='utf-8-sig', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(reader)

print(f"Successfully injected {total_injected} missing items across {len(files_to_update)} files.")
