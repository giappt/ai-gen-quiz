import csv

input_file = 'mondai2_ordering/csv_filled/set_1_daily/part_63.csv'
with open(input_file, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# We will just rewrite the file correctly.
# I will output the exact text to replace.
