'''
输入生产人员的姓名，生成其工资条
'''
import os
import pandas as pd
import easygui


fname =r"F:\a00nutstore\008\zw08\gongzi\生产人员工资.xlsx"
os.chdir(r'F:\a00nutstore\008\zw08\gongzi')
filter = easygui.enterbox('请输入员工姓名')
df = pd.read_excel(fname,sheet_name = '工资')
df = df.loc[df['姓名']==filter]
df = df.dropna(axis = 1)   #删除空格或完全没有数据的列
df = df.drop(df.columns[df.isin([0]).any()], axis=1)
df = df.loc[:,'姓名':"实发数"]
df.to_excel('工资条.xlsx',sheet_name = '工资',index = False)
os.startfile('工资条.xlsx')