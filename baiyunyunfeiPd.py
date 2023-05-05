import pandas as pd
import os
import excelseting
import easygui

fname = r'F:\a00nutstore\006\zw\baiyun\2020白云入库.xlsx'
start = easygui.enterbox('请输入送货单开始日期"2021-06-03"')
end = easygui.enterbox('请输入送货单开始日期"2021-07-15"')
path,filename = os.path.split(fname)
os.chdir(path)
new_filename = r'白云运费{}.xlsx'.format(end)
new_fname = os.path.join(path,new_filename)
df = pd.read_excel(fname,sheet_name='2020')
df.set_index('送货单日期',inplace=True)    #索引
df.sort_index(inplace=True)                       #对索引排序
df1 = df.truncate(before=start,after=end)

pivot = df1.pivot_table(index = '品名',values=['数量(令)','计算重量','数量(吨)'],aggfunc='sum')                 #透视表
# pivot.rename_axis('品名',axis=0,inplace=True)                      #更改行索引名字！axis='index'也行
del_list = ['价差','返利','冲减']
for j in del_list:
    pivot=pivot[~pivot.index.str.contains(j)]  #删除带有'价差','返利','冲减'的行
pivot['运费'] = round(pivot['数量(吨)']*115,2)
pivot['不含税运费'] = round(pivot['运费'] /1.09,2)
result = pivot.reindex(index=list(pivot.index)+['合计'])      #添加一行！先添加一个索引
result.loc['合计'] = pivot.sum()                              #添加一行！在索引后添加数据

#writer = pd.ExcelWriter(new_fname,engine='openpyxl')          #非如此，不能将不同的df存入不同的工作表
with pd.ExcelWriter(new_fname)  as writer:
    df1.to_excel(writer,sheet_name= 'yf{}'.format(end[-5:]))
    result.to_excel(writer,'yfdy{}'.format(end[-5:]))                             #不要sheet_name=也可以

taitou = '白云运费{}至{}'.format(start,end)
excelseting.fastseting(new_fname,'yfdy{}'.format(end[-5:]),taitou)
os.startfile(new_fname)




