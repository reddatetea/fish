'''
选定目录,对目录下的工作簿xls,下面的工作表进行汇总合并,指定AB列名
'''
import os
import xlwings as xw
import easygui
import excelmessage

app = xw.App(visible=False, add_book=False)
nwb = app.books.add()
nws = nwb.sheets[0]
# nws.title = '合并结果'# 新建工作簿和工作表。
msg = '请点选要汇总的文件夹'
path = easygui.diropenbox(msg)
files = os.listdir(path)  # 获取销售表文件夹下的所有工作簿名称。
lst = []
fname = os.path.join(path,os.listdir(path)[0])
wb = app.books.open(fname)
ws = wb.sheets.active
ws.name = '合并结果'
old_title = [j.value for j in ws.range('A1').expand('right')]
wb.close()
daidin1 = input('请输入合并结果报表中表头第一项，类似每个工作簿的名字')
daidin2 = input('请输入合并结果报表中表头第一项，类似每个工作表的名字')
new_title = [daidin1, daidin2] + old_title
nws.range('A1').value = new_title
hz_filename = r'合并结果xlwings.xlsx'
hz_fname = os.path.join(path, hz_filename)
shuju = []
for file in files:  # 循环工作簿名称。
    fname = os.path.join(path,file)
    fname = excelmessage.excelMessage(fname)
    wb = app.books.open(fname)
    for ws in wb.sheets:  # 循环工作簿下所有工作表。
        old_shuju = ws.range('A1').expand('table').value[1:]
        for j in old_shuju:
            shuju.append([file.split('.')[0], ws.name]+j)
    wb.close()

nws.range('A2').expand('right').value = shuju
nwb.save(hz_fname)  # 保存新建的工作簿。
app.quit()
