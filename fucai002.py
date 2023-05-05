import pandas as pd
from itertools import combinations
import xlwings as xw
import numpy as np

columns= ['开奖期号','开奖日期','开','奖','号','试','机','号1','机1','球','投注总额','单选注数','单选金额','组三注数','组三金额','组六注数','组六金额']
df = pd.read_csv(r'http://www.17500.cn/getData/3d.TXT',sep=' ',header=None,names=columns)

df =df.iloc[:,:8]
old_columns =  ['qihao','riqi','bai','shi','ge','sbai','sshi','sge']
df.columns = old_columns
nums = ['0123456789']
items= map(str,*nums)
wumas= ["".join(i) for i in combinations(items,5)]
df = df.assign(和值=df.apply(lambda x:x['bai'] + x['shi'] + x['ge'] ,axis=1))
old_columns =  ['qihao','riqi','bai','shi','ge','sbai','sshi','sge']
old_columns.append('和值')
dic = dict(zip(old_columns,['str']*len(old_columns)))
df = df.astype(dic)

df1 = df.loc[:'bai','shi','ge']
data = []
def func(ser):
    data0 =  []
    for i,j in zip(lst,ser):
        if i in ser.name:
            data0.append(1)
        else :
            data0.append(0)
    return data0
for i in df:
    m = func(df[i])
    data.append(m)
dic = dict(zip(lst,data))
result = pd.DataFrame(dic,index=['a','b','c'])
data = np.array([np.nan]*df.shape[0]*len(wumas)).reshape(len(df.qihao),len(wumas))
df_tmp = pd.DataFrame(data,index=range(df.shape[0]),columns=wumas)
df1 = pd.concat([df,df_tmp],axis=1)
df1 = df1.set_index(old_columns)
lst = df1.index
for label,ser in df1.items():
    for index,i in enumerate((zip(lst,ser))):
        if (i[0][2] in label) or (i[0][3] in label) or (i[0][4] in label):
             ser.iloc[index] = 1
        else :
             continue
print(df1)

