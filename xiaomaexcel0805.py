import xlwings as xw
import os
# 打开excel
app = xw.App(visible=False, add_book=False)
# 为了提高运行速度，关闭警告信息，比如 关闭前提示保存、删除前提示确认等，默认是打开的。
app.display_alerts = False
fname = r'D:\a00nutstore\PythonExceWordPPT一本通\003_Excel篇源代码\第8章\8.5\1组.xlsx'
destWorkbook = app.books.open(fname)

# 设置第一个工作表为活跃工作表
destSheet = destWorkbook.sheets[0]

# 设置除表头之外的字体名称为微软雅黑
print('设置除表头之外的字体样式')
print('设置字体名称为书体坊米芾体')
destSheet.range('A2').expand('table').api.Font.Name = '书体坊米芾体'
print('设置字体大小为16')
# destSheet.range('A2').expand('table').api.Font.size = 16
print('设置字体加粗')
# destSheet.range('A2').expand('table').api.Font.Bold = True
print('设置字体颜色')
# destSheet.range('A2').expand('table').api.Font.color = xw.utils.rgb_to_int((1, 1, 255))

# 保存文件
destWorkbook.save(fname)
destWorkbook.close()
# 退出
app.quit()
# os.startfile(fname)
