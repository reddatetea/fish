import openpyxl
fname = r'D:\a00nutstore\fishc\test.xlsx'
wb = openpyxl.load_workbook(fname)
ws = wb.active
# ws.print_options.horizontalCentered = True
# ws.print_options.verticalCentered = True

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
