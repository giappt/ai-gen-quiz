import csv

def fix_csv(filename, fix_map):
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    for idx, (old, new) in fix_map.items():
        if idx < len(lines):
            lines[idx] = lines[idx].replace(old, new)
            
    with open(filename, 'w', encoding='utf-8') as f:
        f.writelines(lines)

# Fix part_48.csv
fix_csv('mondai2_ordering/csv_filled/set_1_daily/part_48.csv', {
    2: ('お母さんは」', '「お母さんは」'),
    5: ('友達から」', '「友達から」'),
    6: ('彼の話し方は」', '「彼の話し方は」'),
    7: ('息子の部屋は」', '「息子の部屋は」'),
    8: ('私は」', '「私は」'),
    17: ('母が「好きにしなさいというのは', '母が「好きにしなさい」というのは')
})

# Fix part_77.csv
fix_csv('mondai2_ordering/csv_filled/set_1_daily/part_77.csv', {
    1: ('新しい家を」', '「新しい家を」'),
    4: ('スープが」', '「スープが」'),
    5: ('ケーキを一口くれと', '「ケーキを一口くれ」と'),
    7: ('私が」', '「私が」')
})
