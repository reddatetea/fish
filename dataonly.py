'''
dataonly后直接复盖原文件
'''
import win32com.client as win32
import os
import time
import openpyxl

def dataOnly(fname):
    #wb = openpyxl.load_workbook(fname)
    #ws = wb['2020']
    #ws = wb.active
    #wb.save(fname)

    excel = win32.DispatchEx('Excel.Application')

    qian,hou = os.path.splitext(fname)
    newname = qian+'正'+hou

    wb = excel.Workbooks.Open(fname)

    #time.sleep(3)
    wb.SaveAs(fname, FileFormat = 51)
    time.sleep(3)
    wb.Close()
    excel.Application.Quit()

    return newname

def main():
    path = r'F:\a00nutstore\006\zw\baiyun'
    os.chdir(path)
    filename = r'2020白云入库 - 副本 (4).xlsx'
    fname = os.path.join(path, filename)
    dataOnly(fname)

if __name__ == '__main__':
    main()