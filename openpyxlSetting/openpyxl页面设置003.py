import openpyxl
fname = r'D:\a00nutstore\fishc\test.xlsx'
wb = openpyxl.load_workbook(fname)
ws = wb.active
# ws.print_options.horizontalCentered = True
# ws.print_options.verticalCentered = True
ws.oddFooter.center.text =  " &[Page] / &N"     #1/n
ws.oddFooter.center.size = 12
#ws.oddFooter.center.font = "Tahoma,Bold"
ws.oddFooter.center.font = "Tahoma"
ws.oddFooter.center.color = "000000"

ws.oddFooter.right.text =  "张文伟"
ws.oddFooter.right.size = 12
ws.oddFooter.right.font = "书体坊米芾体"
ws.oddFooter.right.color = "000000"




wb.save(fname)
