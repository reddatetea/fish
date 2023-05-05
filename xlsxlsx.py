# conding = utf-8
#将excel老版本xls文件升级为xlsx文件，以便在openpyxl中操作
import win32com.client as win32
import os
import time
from openpyxl import Workbook,load_workbook

def xlsXlsx(fname):
    print('正将excel低版本xls转化为高版本xlsx，请稍等:')
    excel = win32.DispatchEx('Excel.Application')
    excel.Visible = 0
    excel.DisplayAlerts = 0
    newname = fname + 'x'
    wb = excel.Workbooks.Open(fname)
    wb.SaveAs(newname, FileFormat = 51)
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

