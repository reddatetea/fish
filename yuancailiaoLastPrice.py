'''
原材料每个品种最后价格，分白云和纸张
'''

# _*_ conding:utf-8 _*_
import os
import pandas as pd
import numpy as np
from xpinyin import Pinyin
import excelseting
import re

def BydunjiaDic():
    fname2 = r'f:\a00nutstore\006\zw\baiyun\2020白云入库.xlsx'
    df = pd.read_excel(fname2, sheet_name='2020')
    df = df.loc[~df['记账'].isnull()]            #删除记账为空的记录
    df1 = df[df['pricename'].str.contains('返利|价差|冲减|多计|折扣') == False]  # 品名中包含返利、价差、冲减等不计入字典
    df1 = df1.assign(gongsi='驻马店白云纸业有限公司')    #增加一列‘'驻马店白云纸业有限公司'
    gys_pinming = [(x, y) for x, y in zip(df1['gongsi'].tolist(), df1['pricename'].tolist())]
    dunjia_dic = dict(zip(gys_pinming,df1['单价'].tolist()))
    return dunjia_dic

def tichuNum(temp):
        pattern = r'卷筒(\d{3})$'
        regexp = re.compile(pattern)
        pipei = regexp.search(temp)
        if pipei == None:
            string = temp
        else:
            string = re.sub(pattern, '卷筒', temp)
        return string

def dunjiaDic():
    fname2 = r'F:\a00nutstore\006\zw\else\2020入库.xlsx'
    df = pd.read_excel(fname2, sheet_name='入库')
    df = df.loc[~df['记账'].isnull()]  # 删除记账为空的记录
    df = df[df['pricename'].str.contains('返利|价差|冲减|多计|折扣') == False]  # 品名中包含返利、价差、冲减等不计入字典
    # df = df.assign(cailiao=np.where(df['供应商'] == '河南省江河纸业有限公司',df['材料'].agg(tichuNum),df['材料'])) #新增一列，将江河卷筒纸后面的数字去掉
    df['pricename'] = np.where(df['供应商'] == '河南省江河纸业有限公司', df['材料'].agg(tichuNum), df['pricename'])    #江河的pricename名称按cailiao
    gys_pinming = [(x, y) for x, y in zip(df['供应商'].tolist(), df['pricename'].tolist())]       #将两个列表打包为元组列表
    dunjia_dic = dict(zip(gys_pinming,df['吨价'].tolist()))     #字典生成式
    return dunjia_dic

def allPrice(baiyun_price,zhi_price):
    all_price = []
    for key, value in baiyun_price.items():
        all_price.append([key[0],key[1],value])
    for key, value in zhi_price.items():
        all_price.append([key[0],key[1],value])
    return all_price

def getpinyin(chinese_str):
    p = Pinyin()
    pinyins = p.get_pinyin(chinese_str, '-')
    pinyin_str = ' '.join([i.capitalize() for i in pinyins.split('-')] )
    return pinyin_str

def main():
    path = r'f:\a00nutstore\006\zw\price'
    os.chdir(path)
    fname = r'纸张最新价格.xlsx'
    ws_name = 'price'
    baiyun_price = BydunjiaDic()
    zhi_price = dunjiaDic()
    all_price = allPrice(baiyun_price,zhi_price)
    print(all_price)
    df = pd.DataFrame(all_price,columns=['供应商','品名', '价格'])
    df = df.assign(gongyingshang=list(map(getpinyin,df['供应商'])))          #新增一列,将供应商转化为拼音，以便排序
    df.set_index('gongyingshang',inplace=True)                      #分别对供应商和品名排序
    df.index.names = ['gongyingshang']
    df = df.sort_values(by=['gongyingshang','品名'])
    df = df.reset_index()
    df = df.loc[:,['供应商','品名', '价格']]
    df.to_excel(fname,sheet_name = ws_name,index =False )
    excelseting.fastseting(fname,ws_name,'原材料最新价格')
    os.startfile(fname)

if __name__ == '__main__':
    main()