import xlwings as xw
import os

fname = r'D:\a00nutstore\006\zw\2020\202009\2020入库.xlsx'
path,filename = os.path.split(fname)
app = xw.App(visible = False,add_book = False)
wb = app.books.open(fname)
ws = wb.sheets['入库']
ws.range('D2:D372').api.NumberFormat = "mm/dd"
#ws.range('V1').expand('down').number_format = 'm/d'

#ws.range('D2:D372').number_format = 'm/d'

wb.save(fname)
wb.close()
app.quit()
