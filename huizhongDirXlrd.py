'''
选定目录,对目录下的工作簿xls,下面的工作表进行汇总合并,指定AB列名
'''
import os, xlrd, xlwt  # 导入操作系统接口模块，xls读取与写入库。
from xlutils.copy import copy  # 导入复制函数
import easygui


nwb = xlwt.Workbook('utf-8');
nws = nwb.add_sheet('合并结果')  # 新建工作簿和工作表。
msg = '请点选要汇总的文件夹'
path = easygui.diropenbox(msg)
files = os.listdir(path)  # 获取销售表文件夹下的所有工作簿名称。
lst = []
for file in files:  # 循环工作簿名称。
    wb = xlrd.open_workbook(os.path.join(path,file))  # 根据工作簿名称读取工作簿对象。
    for ws in wb.sheets():  # 循环工作簿下所有工作表。
        for row in ws.get_rows():  # 循环工作表下所有行记录
            old_title = [j.value for j in row]
            break
    for ws in wb.sheets():  # 循环工作簿下所有工作表。
        n = 0
        for row in ws.get_rows():  # 循环工作表下所有行记录
            if n==0 :
                n = n +1
                continue
            else :
                hang = []
                for j in row:
                    hang.append(j.value)
                    shuju = [file.split('.')[0], ws.name] + hang  # 准备好要写入新工作表的数据。
                lst.append(shuju)

daidin1 = input('请输入合并结果报表中表头第一项，类似每个工作簿的名字')
daidin2 = input('请输入合并结果报表中表头第一项，类似每个工作表的名字')
new_title = [daidin1, daidin2] + old_title
row_num = 0
[nws.write(row_num, n, v) for n, v in zip(list(range(len(new_title))), new_title)]  # 在新工作表写入表头。
filename = r'合并结果.xls'
fname = os.path.join(path, filename)
print(lst)
num = 1
print(len(lst))
for n, v in zip(range(len(lst)), lst):
    print(n)
    print(v)
    for j in range(len(v)):
        nws.write(num, j, v[j])
    num += 1

nwb.save(fname)  # 保存新建的工作簿。








