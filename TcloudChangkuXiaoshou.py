'''
将产成品仓库的存货编码转为销售部的存货编码
'''

import pandas as pd
import numpy as np
import re
import openpyxl
import easygui
import os

#仓库销售编码字典
fname0 =  r"F:\a00nutstore\008\zw08\用友报价\仓库销售编码字典.xlsx"
df0 = pd.read_excel(fname0)
dic_ck_xs = dict(zip(df0['仓库货号'],df0['销售货号']))
dic_xs_ck = {v:k for k,v in dic_ck_xs.items()}

#产成品仓库库存
def chuliChangku(fname,sheet_name):
    df = pd.read_excel(fname,sheet_name = sheet_name)
    #删除第一列的空行
    df = df[~df['类别'].isna()]
    df = df[~df['类别'].str.contains('小计|累计|合   计')]
    df = df[~(abs(df['本日数量'] - 0) < 0.00001)]
    return df



fname = r"F:\a00nutstore\008\zw08\用友报价\产成品库存\成品仓库数据7.21.xls"

sheet_name  =  0
df = chuliChangku(fname,sheet_name)

def addXiaoshouhuohao(df,dic_ck_xs):
    df_ck = df.assign(销售货号 = df['货号'].map(dic_ck_xs))
    gp = df_ck.groupby('货号')
    df_ck = pd.DataFrame(gp.sum())
    df_ck = df_ck[['销售货号','本日数量']]
    df_ck = df_ck.reset_index()
    return df_ck
df_ck = addXiaoshouhuohao(df,dic_ck_xs)
df_ck = df_ck[['本日数量','销售货号','货号']]
df_ck = df_ck.rename(columns = {'货号':'仓库货号'})
df_ck.to_excel('仓库库存.xlsx',index = False)

# 销售编码
def xiaoshou(fname_xs):
    df_xs = pd.read_excel(fname_xs)
    df_xs = df_xs[~df_xs['类别'].isna()]
    return df_xs


fname_xs = r"F:\a00nutstore\008\zw08\用友报价\销售仓库价格库存1.xlsx"
df_xs = xiaoshou(fname_xs)
xs_lst = [
    '类别',
    '货号',
    '品名',
    '销售部存货大类编码',
    '含量',
    '汉办',
    '汉口北电商',
    '外地',
]
df_xs = df_xs[xs_lst]


def weiyihuXiaoshouhuohao(df_xs, df_ck, dic_xs_ck):
    merge = pd.merge(df_xs, df_ck, left_on='货号', right_on='销售货号', how='right')
    merge['本日数量本'] = merge['本日数量']
    merge['本日数量件'] = merge['本日数量'] / merge['含量']
    del merge['本日数量']
    del merge['销售货号']
    gp = merge.groupby('货号')
    dic_agg = {'含量': 'mean', '汉办': 'mean', '汉口北电商': 'mean', '外地': 'mean', '本日数量本': 'sum'}
    right = gp.agg(dic_agg)
    right = right.reset_index()
    left = df_xs[[
        '类别',
        '货号',
        '品名',
        '销售部存货大类编码'
    ]]
    mg = pd.merge(left, right, left_on='货号', right_on='货号',how = 'right')
    mg['本日数量件'] = mg['本日数量本'] / mg['含量']
    mg = mg.assign(仓库货号=mg['货号'].map(dic_xs_ck))
    return mg


result = weiyihuXiaoshouhuohao(df_xs, df_ck, dic_xs_ck)
result.to_excel('销售仓库价格库存0722.xlsx',index = False)



