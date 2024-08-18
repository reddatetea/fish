'''
计算Tcloud中工厂与销售公司、各机构的存货档案中含量和价格的差异

'''

import pandas as pd
import numpy as np
import re
import easygui
import os
import openpyxl

def addBen(string):
    pattern = r'(?P<num>\d+)本/件'
    regexp1 = re.compile(pattern)
    mat = regexp1.search(string)
    if mat:
        content = int(mat.group('num'))
    else :
        content  = 0
    return content

def getContentCodeContenDic(fname):
    df_content = pd.read_excel(fname,dtype = {'存货编码' :str})
    df_content['content'] = df_content['计量单位'].map(addBen)
    codes = df_content['存货编码']
    contens = df_content['content']
    caigous = df_content['采购价']
    pifa01s = df_content['一级批发价']
    pifa02s = df_content['二级批发价']
    pifa03s = df_content['三级批发价']
    content_price = zip(contens,caigous,pifa01s,pifa02s,pifa03s)
    code_content = dict(zip(codes, content_price))
    return df_content,code_content

fname_gongchang = r"F:\a00nutstore\008\zw08\用友报价\产成品库存\存货档案20240818\存货-工厂.xlsx"
df_gongchang,code_contentPrice_gongchang = getContentCodeContenDic(fname_gongchang)

fname_rongjia = r"F:\a00nutstore\008\zw08\用友报价\产成品库存\存货档案20240818\存货-荣佳.xlsx"
df_rongjia,code_contentPrice_rongjia = getContentCodeContenDic(fname_rongjia)

fname_jiaguang = r"F:\a00nutstore\008\zw08\用友报价\产成品库存\存货档案20240818\存货-佳广.xlsx"
df_jiaguang,code_contentPrice_jiaguang = getContentCodeContenDic(fname_jiaguang)

fname_xiaoshou = r"F:\a00nutstore\008\zw08\用友报价\产成品库存\存货档案20240818\存货-销售公司.xlsx"
df_xiaoshou,code_contentPrice_xiaoshou = getContentCodeContenDic(fname_xiaoshou)

fname_laixin = r"F:\a00nutstore\008\zw08\用友报价\产成品库存\存货档案20240818\存货-莱新.xlsx"
df_laixin,code_contentPrice_laixin = getContentCodeContenDic(fname_laixin)


diff_gongchang_rongjia = pd.merge(df_gongchang,df_rongjia,on = '存货编码',how = 'outer')
diff_gongchang_rongjia.to_excel('存货差异-工厂-荣佳.xlsx',index = False)

diff_gongchang_laixin = pd.merge(df_gongchang,df_laixin,on = '存货编码',how = 'outer')
diff_gongchang_laixin.to_excel('存货差异-工厂-莱新.xlsx',index = False)

diff_gongchang_jiaguang = pd.merge(df_gongchang,df_jiaguang,on = '存货编码',how = 'outer')
diff_gongchang_jiaguang.to_excel('存货差异-工厂-佳广.xlsx',index = False)

diff_gongchang_xiaoshou = pd.merge(df_gongchang,df_xiaoshou,on = '存货编码',how = 'outer')
diff_gongchang_xiaoshou.to_excel('存货差异-工厂-销售公司.xlsx',index = False)


