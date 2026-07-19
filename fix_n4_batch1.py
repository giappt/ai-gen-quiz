import csv

def fix_csv(filename, fix_map, replace=False):
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    for idx, data in fix_map.items():
        if idx < len(lines):
            if replace:
                lines[idx] = lines[idx].replace(data[0], data[1])
            else:
                lines[idx] = data + '\n'
            
    with open(filename, 'w', encoding='utf-8') as f:
        f.writelines(lines)

# Fix part_33.csv
fix_csv('mondai2_ordering/csv_filled/set_1_daily/part_33.csv', {
    6: ('路だけど、', 'だけど、')
}, replace=True)

