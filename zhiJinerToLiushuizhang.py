'''
将已记账白云入库和纸张入库的金额写入原材料流水账
'''
import os
import pandas as pd
from beifenFile import beifen
import xlwings as xw
import easygui

def getBaiyun():
    fname_by = r'F:\a00nutstore\006\zw\baiyun\2020白云入库.xlsx'
    df_baiyun = pd.read_excel(fname_by,'2020')
    df_baiyun = df_baiyun.loc[df_baiyun['记账'].notnull()]
    df_baiyun = df_baiyun[['开票日期', '公司', '入库单号', '仓库材料', '金额']]
    df_baiyun['公司'] = '驻马店白云纸业有限公司'
    df_baiyun = df_baiyun.rename({'开票日期': '日期', '公司': '供货单位', '入库单号': '单据号', '仓库材料': '品名'}, axis=1)
    df_baiyun = df_baiyun.groupby(by=['日期', '供货单位', '单据号', '品名']).sum()
    return df_baiyun

def getZhi():
    fname_ruku = r'F:\a00nutstore\006\zw\else\2020入库.xlsx'
    df_ruku = pd.read_excel(fname_ruku,'入库')
    df_ruku = df_ruku.loc[df_ruku['记账'].notnull()]
    df_ruku = df_ruku[['时间', '供应商', '单号', '材料', '送货单金额']]
    df_ruku = df_ruku.rename({'时间': '日期', '供应商': '供货单位', '单号': '单据号', '材料': '品名', '送货单金额': '金额'}, axis=1)
    df_ruku = df_ruku.groupby(by=['日期', '供货单位', '单据号', '品名']).sum()
    return df_ruku

def getLiushuizhang(fname_lsz, sheet_name):
    df_lsz = pd.read_excel(fname_lsz, sheet_name)
    return df_lsz

def lianjie(df_lsz,df2):
    df_m = pd.merge(df_lsz, df2, on=['日期', '供货单位', '单据号', '品名'], how='left')
    df_m['金额'] = df_m['金额'].fillna(0)
    df_m = df_m.assign(入库金额=df_m.apply(lambda x: x['入库金额'] if x['金额'] == 0 else x['金额'], axis=1)
                                     )
    df_m = df_m.assign(入库单价=df_m.apply(lambda x: round(x['入库金额']/x['入库数量'],2) if x['入库数量'] != 0 else x['入库单价'], axis=1)
                       )
    df_m.drop('金额', axis=1, inplace=True)
    return df_m

def dataToLiushuizhang(fname,sheet_name,data):
    app = xw.App(visible=False, add_book=False)
    wb = app.books.open(fname)
    ws = wb.sheets[sheet_name]
    ws.clear()
    ws.range('A1').options(pd.DataFrame, index=False).value = data
    wb.save()
    wb.close()
    app.quit()
    return fname

def main():
    fname_lsz = r'F:\a00nutstore\006\zw\原材料实时流水账\原材料实时流水账.xlsx'
    sheet_name = '流水账'
    #合并流水账和白云
    df_lsz = getLiushuizhang(fname_lsz, sheet_name)
    df_baiyun = getBaiyun()
    df_m = lianjie(df_lsz,df_baiyun)
    beifen(fname_lsz)
    fname_lsz = dataToLiushuizhang(fname_lsz,sheet_name,df_m)
    #合并流水账和纸张
    df_lsz = getLiushuizhang(fname_lsz, sheet_name)
    df_zhi = getZhi()
    df_m = lianjie(df_lsz, df_zhi)
    beifen(fname_lsz)
    fname_lsz = dataToLiushuizhang(fname_lsz, sheet_name, df_m)
    easygui.msgbox('程序结束')

if __name__ == '__main__':
    main()