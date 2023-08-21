#本版实现供应商多选
import os
import xlwings as xw
import pandas as pd
import openpyxl
import easygui
from openpyxl.utils import  get_column_letter,column_index_from_string
import excelprint
import datetime
import sortbypinyin
import excelfastsetings

def toushiBiao(fname, ws_name, gongyingshangs,zhiziduan,hangziduan,jisuanfangsi,saixuanliezhi):
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
    max_row = values.shape[0] + 1

    for gongyingshang in gongyingshangs:
        filtered = values[
            (values[u'记账'] == '{}'.format(saixuanliezhi)) & (values[u'供应商'] == '{}'.format(gongyingshang))]
        # print(fname, ws_name, zhiziduan,hangziduan, jisuanfangsi,saixuanliezhi)
        pivottable = pd.pivot_table(filtered, values=zhiziduan, index=hangziduan, columns=None, aggfunc=jisuanfangsi,
                                    fill_value=0, margins=True, margins_name='合计')
        order = zhiziduan
        pivottable = pivottable[order]
        nws = ws_ruku.copy(before=ws_ruku)
        nws.name = gongyingshang
        nws.clear()
        nws.range('A1').value = pivottable
        nws.range('A1').value = '品名'
        nws.range('B1').value = '入库(令)'
        nws.range('B1').expand('down').number_format = '#,##0.00'
        nws.range('C1').expand('down').number_format = '#,##0.000'
        nws.range('D1').expand('down').number_format = '#,##0.00'
        nws.range('E1').expand('down').number_format = '#,##0.00'
        nws.autofit()
    wb.close()
    nwb.save(fname1)
    nwb.close()
    app.quit()
    return fname1

def main():
    fname = r'F:\a00nutstore\006\zw\else\2020入库.xlsx'
    ws_name = '入库'
    zhiziduan = ['入库', '入库(吨)', '送货单金额', '不含税价']
    hangziduan = 'jd'
    jisuanfangsi = 'sum'
    df = pd.read_excel(fname,sheet_name=ws_name)
    df = df[df['记账'] !=None]
    saixuanliezhis = list(df['记账'].unique())[-20:]      #最后20个记账日期！
    # saixuanliezhis.sort(reverse=True)       #reverse=True是降序，reverse=False或不写是升序,为什么排序失败？
    msg = '请选择记账日期'
    saixuanliezhi = easygui.choicebox(msg, title=msg, choices=saixuanliezhis)
    print(saixuanliezhi)
    df = df[df['记账'] == saixuanliezhi]
    gongyingshangs = list(df['供应商'].unique())
    gongyingshangs = sortbypinyin.pinyinSort(gongyingshangs)  # 供应商按拼音排序
    msg = '请选择供应商'
    gongyingshangs = easygui.multchoicebox(msg, title=msg, choices=gongyingshangs)
    fname1 = toushiBiao(fname, ws_name, gongyingshangs, zhiziduan, hangziduan, jisuanfangsi, saixuanliezhi)
    excelfastsetings.fastseting(fname1, gongyingshangs)
    excelprint.wsPrints(fname1, gongyingshangs)

if __name__ == '__main__':
    main()