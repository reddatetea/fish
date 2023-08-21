import openpyxl
from openpyxl.utils import get_column_letter, column_index_from_string


fname = r'D:\a00nutstore\fishc\test.xlsx'
wb = openpyxl.load_workbook(fname)
ws = wb.active
# ws.print_options.horizontalCentered = True
# ws.print_options.verticalCentered = True

title = input('请输入打印标题：\n')

#冻结单元格
ws.freeze_panes = 'B2'

#打印标题
ws.print_title_cols = 'A:B' # the first two cols   #左端标题列（即从左侧重复的列数）
ws.print_title_rows = '1:1' # the first row     #顶端标题行（即从上端重复的行数）

#页眉设置
ws.oddHeader.center.text =  '%s'%title    #1/n      页眉中文字
ws.oddHeader.center.size = 18                   # 页眉中字体大小
# ws.oddHeader.center.font = '宋体,Italic'         # 页眉中字体,宋体、倾斜
# ws.oddHeader.center.font = '宋体,Bold'         # 页眉中字体,宋体、加粗
ws.oddHeader.center.font = '宋体,Bold Italic'     # 页眉中字体,宋体、加粗、倾斜

ws.oddHeader.center.color = "000000"            # 页眉中字体颜色

#页脚设置
ws.oddFooter.center.text =  " &[Page] / &N"     #1/n      页脚中文字
ws.oddFooter.center.size = 12                   # 页脚中字体大小
ws.oddFooter.center.font = "Tahoma"             # 页脚中字体
ws.oddFooter.center.color = "000000"            # 页脚中字体颜色

ws.oddFooter.right.text =  "张文伟 &[Date]"     #页脚右 文字
ws.oddFooter.right.size = 12                    #页脚右 字体大小
ws.oddFooter.right.font = "书体坊米芾体"        #页脚右 字体
ws.oddFooter.right.color = "000000"             #页脚右 字体颜色




wb.save(fname)
