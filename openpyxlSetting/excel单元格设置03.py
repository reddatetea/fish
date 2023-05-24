import os
import openpyxl
from openpyxl.worksheet.header_footer import _HeaderFooterPart
import datetime
import time


fname = r'D:\a00nutstore\fishc\原材料实时流水账 - 副本.xlsx'
wb = openpyxl.load_workbook(fname)
ws = wb['流水账']

# 设置首页与其他页不同
ws.HeaderFooter.differentFirst = True

# 设置奇偶页不同
ws.HeaderFooter.differentOddEven = True

# 设置首页页眉页脚

ws.firstHeader.center = _HeaderFooterPart('原材料实时流水账',size = 28 ,color = '000000')

# 设置页眉页脚
ws.oddFooter.center.text ='&[页码]/&[总页数]'
ws.oddFooter.right.text = '制表：张文伟  &[日期]'
ws.evenFooter.center.text = '&[页码]/&[总页数]'
ws.evenFooter.right.text = '制表：张文伟  &[日期]'


wb.save(fname)




