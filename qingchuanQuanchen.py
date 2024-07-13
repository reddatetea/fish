'''
根据给定的简称和全称对照表，根据摘要中包含的简称，将其对应的全称写入“供应商名称”列
'''

import os
import pandas as pd
import easygui
import os
import openpyxl

def choiceSheetname(df,msg):
    sheet_names = [key for key in df.keys() ]
    if len(sheet_names) == 1:
        sheet_name = sheet_names[0]
    else :
        sheet_name = easygui.choicebox(msg = msg,choices = sheet_names)
    return sheet_name

def quan(ser,dic):
    for key, value in dic.items():
        if key in ser:
            ser = value
            ser1 = ser
            break
        else:
            ser1 = ''
            continue
    return ser1

def main():
    fname = easygui.fileopenbox('请点选“付款”工作薄')
    df0 = pd.read_excel(fname, sheet_name=None)
    sheet_name = choiceSheetname(df0, '请点选"Transaction Reference"')
    skiprows = int(str(easygui.enterbox('数据是从第几天开始'))) - 1
    df = pd.read_excel(fname, sheet_name=sheet_name, skiprows=skiprows)
    df = df.loc[df['Description'].notnull()]
    sheet_name0 = choiceSheetname(df0, '请点选"供应商简称全称对照"工作表')
    df_jiancen = pd.read_excel(fname, sheet_name=sheet_name0)
    df_jiancen = df_jiancen.loc[df_jiancen['简称'].notnull()]
    dic = dict(zip(df_jiancen['简称'], df_jiancen['销售单位名称']))
    df1 = df.assign(quan=df['Description'].apply(lambda x: quan(x,dic)))
    quans = df1.quan.to_list()
    maxrow = skiprows + 1 + len(df1)
    wb = openpyxl.load_workbook(fname)
    ws = wb[sheet_name]
    for i in range(skiprows + 2, maxrow + 1):
        ws[f'I{i}'].value = quans[i - 8]
    wb.save(fname)
    os.startfile(fname)

if __name__ == '__main__':
    main()
