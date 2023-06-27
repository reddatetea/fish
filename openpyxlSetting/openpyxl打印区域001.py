import openpyxl
fname = r'D:\a00nutstore\fishc\test.xlsx'
wb = openpyxl.load_workbook(fname)
ws = wb.active

max_row = ws.max_row
print(max_row)

wb.close()