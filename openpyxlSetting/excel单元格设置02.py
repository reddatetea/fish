import os
import openpyxl
from openpyxl.worksheet.header_footer import _HeaderFooterPart

fname = r'D:\a00nutstore\fishc\原材料实时流水账 - 副本.xlsx'
wb = openpyxl.load_workbook(fname)
ws = wb['流水账']

# 设置首页与其他页不同
ws.HeaderFooter.differentFirst = True

# 设置奇偶页不同
ws.HeaderFooter.differentOddEven = True

# 设置首页页眉页脚
#ws.firstHeader.left = _HeaderFooterPart('第一页左页眉',size = 24 ,color = 'FF0000')
ws.firstHeader.center = _HeaderFooterPart('原材料实时流水账',size = 28 ,color = 'FF0000')

# 设置奇偶页页眉页脚
#ws.oddHeader.right = _HeaderFooterPart('奇数页右页眉')
ws.oddFooter.center = _HeaderFooterPart('&[日期]')
#ws.evenHeader.left = _HeaderFooterPart('偶数页左页眉')
ws.evenFooter.center = _HeaderFooterPart('&[日期]')
ws.evenFooter.right.text = '2020/06/06  &[时间]'

wb.save(fname)




