import pandas as pd
from itertools import combinations
import xlwings as xw
import numpy as np
import os

columns= ['开奖期号','开奖日期','开','奖','号','试','机','号1','机1','球','投注总额','单选注数','单选金额','组三注数','组三金额','组六注数','组六金额']
df0 = pd.read_csv(r'http://www.17500.cn/getData/3d.TXT',sep=' ',header=None,names=columns)

df0 =df0.iloc[:,:8]
old_columns =  ['qihao','riqi','bai','shi','ge','sbai','sshi','sge']
df0.columns = old_columns
df0 = df0.replace('-',np.nan)   #有时试机号出来，而实际数并未出来，相关处理
df0 = df0.dropna()
old_columns =  ['qihao','riqi','bai','shi','ge','sbai','sshi','sge']
dic = dict(zip(old_columns,['str']*len(old_columns)))
df0 = df0.astype(dic)
df0 = df0.assign(ddd=df0.apply(lambda x:x['bai'] + x['shi'] + x['ge'] ,axis=1))
nums = ['0123456789']
items= map(str,*nums)
wumas= ["".join(i) for i in combinations(items,5)]

data = []
for i in wumas:
    data0 = []
    for x, y, z in zip(df0['bai'], df0['shi'], df0['ge']):
        if x in i and y in i and z in i:
            data0.append(1)
        else:
            data0.append("")
    data.append(data0)
dic = dict(zip(wumas,data))
df_tmp = pd.DataFrame(dic,index=range(df0.shape[0]),columns=wumas)

df = pd.concat([df0,df_tmp],axis=1)

df = df.astype({"bai":int,'shi':int,'ge':int})
df1 = df.assign(he=df.apply(lambda x:x['bai'] + x['shi'] + x['ge'] ,axis=1))
df1 = df1.astype({'he':str})
df1 = df1.assign(hezhi = df1.he.str[-1])
df1['hui'] = ''
df1['xuhao'] = range(df1.shape[0])
new_columns = old_columns[:5]+['ddd','hui']+ wumas + ['he','hezhi','xuhao'] + old_columns[-3:]
df1 = df1.loc[:,new_columns]
df1 = df1.astype({'he':int,'hezhi':int})
df1.to_excel('wumax.xlsx',index = False)
os.startfile('wumax.xlsx')
