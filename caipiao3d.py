import pandas as pd
from itertools import combinations
import xlwings as xw

columns= ['开奖期号','开奖日期','开','奖','号','试','机','号1','机1','球','投注总额','单选注数','单选金额','组三注数','组三金额','组六注数','组六金额']
df = pd.read_csv(r'http://www.17500.cn/getData/3d.TXT',sep=' ',header=None,names=columns)
df =df.iloc[:,:8]
df.columns = ['qihao','riqi','bai','shi','ge','sbai','sshi','sge']
dic = {'bai':str,'shi':str,'ge':str,'sbai':str,'sshi':str,'sge':str}
df = df.astype(dic)
nums = ['0123456789']
items=list(map(str,*nums))
wumas= []
for i in combinations(items,5):
    j = "".join(i)
    wumas.append(j)
df1 = df.copy()
df2 = df1.iloc[:,:5]
df3 = df1.iloc[:,[0,-3,-2,-1]]
df2['3d'] = df2['bai'] +df2['shi'] +df2['ge']

for i in wumas:
    df2[i] =0
df2 = df2.set_index(['qihao','riqi','bai','shi','ge'])
df2 = df2.sort_index()
for i in wumas:
    for j in df2.index:
        if (j[2] in i) or (j[3] in i) or (j[4] in i):
            df2.loc[j,i] =1
        else:
            continue
print(df2)
