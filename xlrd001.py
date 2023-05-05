import xlrd
file = r'D:\a00nutstore\fishc\qingchuan\2020年月饼券销售明细表.xls'
data = xlrd.open_workbook(file)
table = data.sheets()[0]
value = table.cell_value(4,1)
print(value)