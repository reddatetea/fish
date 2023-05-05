'''
复制通过指定起止日期和供应商查询到的流水账数据，通过pandas的clipboard 生成材料入库单，快速设置，并打开excel文件
'''
import excelseting
import os
import pandas as pd
import xlwings as xw

def rukuRange(fname,ws_name):
    df = pd.read_clipboard()
    gys = df['供货单位'].to_list()[0]
    df1 = df.groupby('cwName').sum()
    df1 = df1.iloc[:, [0, 2]]
    df1['不含税金额'] = round(df1['入库金额'] / 1.13, 2)
    df1.at['合计', '入库数量'] = df1['入库数量'].sum()
    df1.at['合计', '入库金额'] = df1['入库金额'].sum()
    df1.at['合计', '不含税金额'] = df1['不含税金额'].sum()
    df1 = df1.rename_axis('品名')
    return df1,gys

def rukudan(df,fname,ws_name):
    app = xw.App(visible=False,add_book=False)
    wb=app.books.open(fname)
    ws = wb.sheets[ws_name]
    ws.clear()
    ws.range('a1').options(pd.DataFrame).value = df
    ws.autofit()
    wb.save(fname)
    app.quit()

def main():
    fname = r'F:\a00nutstore\fishc\材料入库单.xlsx'
    ws_name = '入库'
    df,gys= rukuRange(fname, ws_name)
    print('gys',gys)
    rukudan(df,fname,ws_name)
    excelseting.fastseting(fname,ws_name,gys)
    os.startfile(fname)
    # # os.startfile(fname, 'print')                         #打开excel并打印
    # excelprint.wsPrint(fname,ws_name)

if  __name__ == '__main__':
    main()
