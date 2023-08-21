import openpyxl
from openpyxl.worksheet.header_footer import _HeaderFooterPart
fname = r'D:\a00nutstore\fishc\test.xlsx'
wb = openpyxl.load_workbook(fname)
ws = wb.active
ws.print_options.horizontalCentered = True
ws.print_options.verticalCentered = True
ws.HeaderFooter.differentFirst = True

# 设置奇偶页不同

ws.HeaderFooter.differentOddEven = True

# 设置首页页眉页脚

ws.firstHeader.left = _HeaderFooterPart('第一页左页眉', size=24, color='FF0000')

ws.firstFooter.center = _HeaderFooterPart('第一页中页脚', size=24, color='00FF00')

# 设置奇偶页页眉页脚
ws.oddHeader.right = _HeaderFooterPart('奇数页右页眉')

ws.oddFooter.center = _HeaderFooterPart('奇数页中页脚')

ws.evenHeader.left = _HeaderFooterPart('偶数页左页眉')

ws.evenFooter.center = _HeaderFooterPart('偶数页中页脚')


wb.save(fname)
