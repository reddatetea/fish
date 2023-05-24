from openpyxl import load_workbook
fname = r'F:\a00nutstore\fishc\test.xlsx'
wb = load_workbook(fname)
ws = wb.active
ws.row_dimensions[1].height = 50
ws.column_dimensions['B'].width = 20

wb.save(fname)