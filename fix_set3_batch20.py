import csv
import re

def fix():
    files = [
        'mondai2_ordering/csv_filled/set_3_academic/part_96.csv',
        'mondai2_ordering/csv_filled/set_3_academic/part_97.csv',
        'mondai2_ordering/csv_filled/set_3_academic/part_98.csv',
        'mondai2_ordering/csv_filled/set_3_academic/part_99.csv',
        'mondai2_ordering/csv_filled/set_3_academic/part_100.csv'
    ]

    for file_path in files:
        with open(file_path, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            rows = list(reader)

        for row in rows:
            for i in range(len(row)):
                row[i] = row[i].replace('AI của 活用', 'AIの活用')
                row[i] = row[i].replace('N của もとで', 'Nのもとで')
                row[i] = row[i].replace('N của もとに', 'Nのもとに')
                row[i] = row[i].replace('合否u', '合否')

            if len(row) > 11:
                exp = row[11]
                
                # Replace single quotes
                exp = re.sub(r"'([^']+)'", r'「\1」', exp)
                
                # Replace double quotes (which were escaped in CSV, so now they are standard double quotes)
                exp = re.sub(r'"([^"]+)"', r'「\1」', exp)
                
                # Fix missing opening quote at the very beginning of the explanation
                exp = re.sub(r'^([^「]+)」', r'「\1」', exp)
                
                row[11] = exp

            if len(row) > 11:
                if row[4] == '':
                    row[4] = "".join(row[5:11])

        with open(file_path, 'w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(rows)

if __name__ == "__main__":
    fix()
    print("Fixed batch 20 manually")
