import openpyxl
from openpyxl.styles import Font,Border,Side,Alignment,Fill,Protection

fname = r'D:\a00nutstore\fishc\qingchuan\2020.11Mothly Wedding Report.xlsx'
wb = openpyxl.load_workbook(fname)
ws = wb['Sheet1']
sjqy2 = ws['A1:AA1']
fts = []
bds = []
alis = []
for row in sjqy2:
    ft_row = []
    bd_row = []
    ali_row = []
    for cell in row:
        print(cell.font)
        #print(cell.border)
        #print(cell.alignment)

        ft_row.append(cell.font)
        bd_row.append(cell.border)
        ali_row.append(cell.alignment)
    fts.append(ft_row)
    bds.append(bd_row)
    alis.append(ali_row)

# for ft_row in fts:
#     print(ft_row)



# for bd in bds:
#     print(bds)
#
# for ali in alis:
#     print(alis)
#
# print(len(fts))

# fts_with_index = list(enumerate(fts))
#
# for index,ft0 in fts_with_index:
#     print(index,ft0)
ft = Font(name=u'微软雅黑',size=11)        #字体

bd = Border(left=Side(border_style="thin",
                  color='0000FF'),
        right=Side(border_style="thin",
                  color='0000FF'),
        top=Side(border_style="thin",
                  color='0000FF'),
        bottom=Side(border_style="thin",
                  color='0000FF')
                    )

alignment=Alignment(horizontal='center',vertical='center',shrink_to_fit=True)

wb.save(fname)