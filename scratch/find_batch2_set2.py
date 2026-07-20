import csv, os
dir_path = r'd:\pj\xx\ai-gen-quiz\mondai2_ordering\csv_filled\set_2_business'
files = ['part_6.csv', 'part_7.csv', 'part_8.csv', 'part_9.csv', 'part_10.csv']
out = []
for file in files:
    with open(os.path.join(dir_path, file), encoding='utf-8-sig') as f:
        r = list(csv.reader(f))
        headers = r[0]
        exp_idx = headers.index('Explanation') if 'Explanation' in headers else -1
        if exp_idx == -1: exp_idx = len(headers) - 1
        
        for i, row in enumerate(r):
            if i == 0: continue
            if len(row) > exp_idx:
                exp = ','.join(row[exp_idx:]) 
                exp_clean = exp.replace('"', '')
                if 'thứ tự' in exp_clean.lower() or 'cú pháp' in exp_clean.lower() or 'logic' in exp_clean.lower() or 'n của ' in exp_clean.lower():
                    out.append(f'{file}-{i}: {exp}')
open(r'd:\pj\xx\ai-gen-quiz\scratch\batch2_set2_issues.txt', 'w', encoding='utf-8').write('\n'.join(out))
