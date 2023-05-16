'''
按期间选择供应商分类汇总后,实现批量打印
'''

import pandas as pandas
import easygui
import os
import openpyxl
import xlwings as xw


def toushiBiao(fname1,fname, ws_name, gongyingshangs,zhiziduan,hangziduan,jisuanfangsi,saixuanliezhi):
    # fname1 = r'材料入库单.xlsx'
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
            (values[u'期间'] == '{}'.format(saixuanliezhi)) & (values[u'供货单位'] == '{}'.format(gongyingshang))]
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
        nws.range('D1').value = '不含税金额'
        value1s = nws.range('A1').expand('table').options(pd.DataFrame).value
        max_row = value1s.shape[0] + 1
        for j in range(2, max_row):
            nws.range('D{}'.format(j)).formula = '=ROUND(C{}/1.13,2)'.format(j)
        last_row = max_row - 1
        nws.range('D{}'.format(max_row)).formula = '=SUM(D2:D{})'.format(last_row)
        nws.range('D{}'.format(j)).formula ='=round(C{}/1.13,2)'.format(j)
        nws.range('B1').expand('down').number_format = '#,##0.00'
        nws.range('D1').expand('down').number_format = '#,##0.00'
        nws.range('C1').expand('down').number_format = '#,##0.00'
        nws.autofit()
    wb.close()
    nwb.save(fname1)
    nwb.close()
    app.quit()
    return fname1

def  choiceJPrintGongyingshangs(fname, ws_name,saixuanliezhi):
    df = pd.read_excel(fname,sheet_name=ws_name)
    df = df[df['期间']==saixuanliezhi]
    gongyingshangs = df['供货单位'].unique()
    gongyingshangs = sortbypinyin.pinyinSort(gongyingshangs)     #供应商按拼音排序
    msg = '请选择供应商'
    gongyingshangs = easygui.multchoicebox(msg, title=msg, choices=gongyingshangs)
    return gongyingshangs

def main():
    fname = r'F:\a00nutstore\006\zw\原材料实时流水账\原材料实时流水账.xlsx'
    ws_name = '流水账'
    zhiziduan = ['入库数量', '入库金额']
    hangziduan = 'cwName'
    jisuanfangsi = 'sum'
    saixuanliezhi = easygui.enterbox('请输入期间（如2022-01)')
    gongyingshangs = choiceJPrintGongyingshangs(fname,ws_name,saixuanliezhi)
    fname1 = r'F:\a00nutstore\fishc\材料入库单.xlsx'
    fname1 = toushiBiao(fname1,fname, ws_name, gongyingshangs, zhiziduan, hangziduan, jisuanfangsi, saixuanliezhi)
    excelfastsetings.fastseting(fname1,gongyingshangs)
    excelprint.wsPrints(fname1,gongyingshangs)

if __name__ == '__main__':
    main()



