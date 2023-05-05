# conding = utf-8
#将excel老版本xls文件升级为xlsx文件，以便在openpyxl中操作
import win32com.client as win32
import os
import time
from openpyxl import Workbook,load_workbook

def xlsXlsx(fname):
    print('正将excel低版本xls转化为高版本xlsx，请稍等:')
    #excel = win32.gencache.EnsureDispatch('Excel.Application')
    excel = win32.DispatchEx('Excel.Application')
    # 更换工作目录为当前文件所在文件夹
    # path,filename = os.path.split(fname)    #20210703
    # os.chdir(path)                         #20210703
    #path = os.getcwd()
    newname = fname + 'x'
    wb = excel.Workbooks.Open(fname)
    #time.sleep(3)
    wb.SaveAs(newname, FileFormat = 51)
    time.sleep(3)
    wb.Close()
    excel.Application.Quit()
    return newname

def main():
    path=input('请输入文件路径:')
    filename = input('请输入带后缀的文件名:')
    fname = os.path.join(path,filename)
    fname = os.path.normpath(fname)
    print(fname)
    xlsXlsx(fname)

if __name__=='__main__':
    main()

