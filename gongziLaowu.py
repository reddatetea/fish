'''
根据统计质检部的“劳务工工资表.excel”,制作比较标准的“劳务工资”excel文件
'''

import os
import pandas as pd
import easygui
import os

fname = easygui.fileopenbox('请点选统计质检部的"劳务工工资表"excel文件')
path,_ = os.path.split(fname)
os.chdir(path)
sheet_name = r'工资表'
df= pd.read_excel(fname,sheet_name,skiprows=3)
columns = ['部门',
 '账号',
 '姓名',
 '工资',
 '考评',
 '补贴',
 '生活补贴',
 '保底',
 '工龄',
 '奖励',
 '节约',
 'Unnamed: 11',
 '扣电费',
 '罚款',
 '物耗',
 '代扣社保',
 '扣税',
 'Unnamed: 17',
 'Unnamed: 18',
 '实发工资',
  '领款人签名',
   '保底人员金额',
    'Unnamed: 22'
]
df.columns = columns
index = df['姓名'].to_list().index(0)     #定位
df = df.iloc[:index,]
df = df.loc[:,['部门',
 '账号',
 '姓名',
 '工资',
 '考评',
 '补贴',
 '生活补贴',
 '保底',
 '工龄',
 '奖励',
 '节约',
 '扣电费',
 '罚款',
 '物耗',
 '代扣社保',
 '扣税',
 '实发工资',
 '领款人签名',
 '保底人员金额'
 ]]

df['部门'] = '劳务'
df['账号'] = ''
qijian = easygui.enterbox('请输入期间"2024-03"')
fname = f'劳务工资{qijian}.xlsx'
sheet_name = '工资'
df.to_excel(f'劳务工资{qijian}.xlsx',sheet_name = sheet_name,index = False)
os.startfile(fname)


