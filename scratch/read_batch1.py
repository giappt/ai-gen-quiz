import csv
import os

dir_path = r'd:\pj\xx\ai-gen-quiz\mondai2_ordering\csv_filled\set_1_daily'
files = ['part_16.csv', 'part_17.csv', 'part_18.csv', 'part_19.csv', 'part_20.csv']

output = ''
output_file = 'batch4_review.md'

for file in files:
    full_path = os.path.join(dir_path, file)
    with open(full_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        output += f'# File: {file}\n\n'
        for index, row in enumerate(reader):
            output += f'## ID: {file}-{index + 1}\n'
            output += f'- **Grammar**: {row.get("Grammar", "")}\n'
            output += f'- **Original Example**: {row.get("Original Example", "")}\n'
            output += f'- **Explanation**: {row.get("Explanation", "")}\n\n'

with open(rf'd:\pj\xx\ai-gen-quiz\scratch\{output_file}', 'w', encoding='utf-8') as f:
    f.write(output)

print(f'Done reading to {output_file}')
