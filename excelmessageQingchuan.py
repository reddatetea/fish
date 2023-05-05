# _*_ conding = utf-8 _*_
'''
查看excel文件基本信息，如果是低版的xls文件，则自动将其转化为高版本的xlsx
需输入完整路路径和带后缀的文件名
本版解决后缀xls大小写混写
'''
from xlsxlsx import xlsXlsx
from openpyxl import Workbook,load_workbook
import os
import re
import easygui


def wenjian(msg='请点选要处理的excel文件'):
    fname = easygui.fileopenbox(msg,title='file')
    return fname

def excelMessage(fname):
    pattern = '\w+(\.[X|x][l|L][Ss]$)'
    rep = re.compile(pattern)
    mat = rep.search(fname)
    if mat != None :
        xlsXlsx(fname)
        fname = fname + 'x'

    else:
        fname = fname
    print(fname)
    return fname

def main():
    msg = '"请点选产成品当日和累计"excel文件'
    #fname =wenjian(msg)
    # print(fname)
    # excelMessage(fname)
    fname = r'C:\Users\asus\Desktop\新建文件夹 (2)\itemize_sales_analysis.xls'
    excelMessage(fname)

if __name__=='__main__':
    main()






