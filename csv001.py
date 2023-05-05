import csv
file = r'D:\a00nutstore\fishc\6789.csv'
with open(file, 'r', encoding='utf-8-sig',newline = '') as f:  # utf-8不行 ,unicode_escape
    f_csv = csv.reader(f)
    for row in f_csv:
        hang = [j.strip() for j in row]
        if '卷筒纸' in hang:
            print(hang)
        else:
            continue