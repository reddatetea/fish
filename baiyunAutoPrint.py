#本版本实现多个记账日期查询
import os
import xlwings as xw
import pandas as pd
import openpyxl
import easygui
from openpyxl.utils import  get_column_letter,column_index_from_string
# import excelcellfillby
import excelseting
import excelprint
import excelfastsetings


def toushiBiao(fname, ws_name, zhiziduan,hangziduan,jisuanfangsi,saixuanliezhis):
    fname1 = r'F:\a00nutstore\fishc\材料入库单.xlsx'
    app = xw.App(visible = False,add_book = False)
    wb = app.books.open(fname)
    nwb = app.books.open(fname1)
    for nws in nwb.sheets:
        if nws.name == '入库':
            ws_ruku = nwb.sheets['入库']
            continue
        else:
            nws.delete()
    ws = wb.sheets[ws_name]
    values = ws.range('A1').expand('table').options(pd.DataFrame).value
    filter_js =[]
    for  saixuanliezhi in saixuanliezhis:
        filter_j= values[values['记账'] ==saixuanliezhi]
        filter_js.append(filter_j)
    filtered = pd.concat(filter_js)
    pivottable = pd.pivot_table(filtered, values=zhiziduan, index=hangziduan, columns=None, aggfunc=jisuanfangsi, fill_value =0,margins=True, margins_name='合计')
    order = zhiziduan
    pivottable = pivottable[order]
    nws = ws_ruku.copy(before=ws_ruku)
    nws.name = '白云'
    nws.clear()
    nws.range('A1').value = pivottable
    nws.range('B1').expand('down').number_format = '#,##0.00'
    nws.range('E1').expand('down').number_format = '#,##0.00'
    nws.range('F1').expand('down').number_format = '#,##0.00'
    nws.range('C1').expand('down').number_format = '#,##0.000'
    nws.range('D1').expand('down').number_format = '#,##0.000'
    nws.autofit()
    wb.close()
    nwb.save(fname1)
    nwb.close()
    app.quit()
    return fname1

def main():
    fname = r'F:\a00nutstore\006\zw\baiyun\2020白云入库.xlsx'
    ws_name = '2020'
    zhiziduan = ['数量(令)', '计算重量', '数量(吨)', '金额', '不含税金额']
    hangziduan = '品名'
    jisuanfangsi = 'sum'
    df = pd.read_excel(fname, sheet_name=ws_name)
    df = df[df['记账'] != None]
    saixuanliezhis = list(df['记账'].unique())[-20:]  # 最后20个记账日期！
    # saixuanliezhis.sort(reverse=True)       #reverse=True是降序，reverse=False或不写是升序,为什么排序失败？
    msg = '请选择记账日期'
    saixuanliezhis = easygui.multchoicebox(msg, title=msg, choices=saixuanliezhis)
    print(saixuanliezhis)
    fname1 = toushiBiao(fname, ws_name, zhiziduan,hangziduan,jisuanfangsi,saixuanliezhis)
    excelfastsetings.fastseting(fname1, ['白云'])
    excelprint.wsPrints(fname1, ['白云'])

if __name__ == '__main__':
    main()