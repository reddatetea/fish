import openpyxl
fname = r'D:\a00nutstore\fishc\test.xlsx'
wb = openpyxl.load_workbook(fname)
ws = wb.active
ws.print_options.horizontalCentered = True
ws.print_options.verticalCentered = True
ws.oddHeader.left.text = "Page &[Page] of &N"
ws.oddHeader.left.size = 14
ws.oddHeader.left.font = "Tahoma,Bold"
ws.oddHeader.left.color = "CC3366"


wb.save(fname)
