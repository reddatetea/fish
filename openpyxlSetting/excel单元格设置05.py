import os
import openpyxl
from openpyxl.worksheet.header_footer import _HeaderFooterPart
import datetime
import time

def jiayemei(fname):

    wb = openpyxl.load_workbook(fname)
    ws = wb['流水账']

    #顶端标题行
    ws.print_title_rows = '1:1'

    # 设置首页与其他页不同
    ws.HeaderFooter.differentFirst = True

    # 设置奇偶页不同
    ws.HeaderFooter.differentOddEven = False

    # 设置首页页眉页脚

    ws.firstHeader.center = _HeaderFooterPart('原材料实时流水账',size = 28 ,font = '宋体',color = '000000')

    # 设置页眉页脚

    ws.oddFooter.left.text = '&[页码]/&[总页数]'
    ws.oddFooter.center.text = ' &[日期]'
    ws.oddFooter.right.text = '制表：张文伟'
    ws.oddFooter.right.font = '书体坊米芾体'
    ws.oddFooter.right.size = 14

    wb.save(fname)
    return fname

def main():
    fname = r'D:\a00nutstore\fishc\原材料实时流水账 - 副本.xlsx'
    jiayemei(fname)

if __name__ == '__main__':
    main()




