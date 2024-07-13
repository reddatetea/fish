'''
根撱行管工资和生产工资计算部门平均工资和细分部门平均工资
'''

import pandas as pd
import os
import openpyxl
import re
import easygui
import win32com.client as win32

xifen_bumen = {'劳务': '生产部',
 '生产管理': '生产部',
 '统计质检': '统计质检部',
 '设备科': '生产部',
 '车间-书芯': '生产部',
 '车间-夹子': '生产部',
 '车间-成品': '生产部',
 '车间-柔印': '生产部',
 '车间-简装': '生产部',
 '车间-胶印': '生产部',
 '采购': '采购部',
 '外贸人员': '营销部',
 '销售': '营销部',
 '销售文员': '营销部',
 '保安': '行政部',
 '司机': '行政部',
 '后勤': '行政部',
 '总经理': '行政部',
 '行政文员': '行政部',
 '设计': '设计研发部',
 '财务部': '行政部',
 '食堂': '行政部',
 '仓库管理员': '财务部',
 '叉车搬运': '财务部',
 '财务': '财务部'}
path = r"F:\a00nutstore\008\zw08\gongzi"
os.chdir(path)
fname_xg = r"行管工资.xlsx"
sheet_name = r'工资'
df_xg = pd.read_excel(fname_xg,sheet_name)          #行管工资

df_xg.insert(2,'xifen','')
df_xg  = df_xg[['部门','xifen','姓名','实发数']]
fname_nameXifen = r"行管工资姓名部门对照表.xlsx"
df0 = pd.read_excel(fname_nameXifen)
name_xifen = dict(zip(df0['姓名'],df0['部门']))
df_xg = df_xg.assign(xifen = df_xg['姓名'].map(name_xifen) )
df_xg.部门 = df_xg.部门.replace({'行政、管理部':'行政部','仓库搬运':'财务部'})
df_xg.部门 = df_xg.xifen.replace(xifen_bumen)

fname_shengcan = r"F:\a00nutstore\008\zw08\gongzi\生产人员工资.xlsx"
sheet_name = '工资'
df_shengcan = pd.read_excel(fname_shengcan,sheet_name = sheet_name)
df_shengcan = df_shengcan[['车间','姓名','实发数']]
df_shengcan.insert(0,'部门','车间')
lst = df_shengcan['车间'].to_list()
lst = ['车间-' + i for i in lst]
df_shengcan['车间'] =  lst
df_shengcan = df_shengcan[['部门','车间','姓名','实发数']]         #生产工资
df_shengcan.columns = ['部门','xifen','姓名','实发数']

# fname_laowu = r"F:\a00nutstore\008\zw08\gongzi\2024年工资\202405\生产部劳务工资表-2024-5-25 的副本.xls"
# sheet_name = r'劳务派遣报酬'
def getDf(msg):
    fname = easygui.fileopenbox(msg=msg)
    df = pd.read_excel(fname, sheet_name=None)
    sheetnames = list(df)
    sheet_name = easygui.choicebox(title='请点选"劳务派遣报酬"', choices=sheetnames)
    return fname, df, sheet_name
fname_laowu,df,sheet_name = getDf('请点选劳务工资表')
df_laowu = pd.read_excel(fname_laowu,sheet_name = sheet_name,skiprows = 2)
df_laowu['姓名'] = df_laowu['姓名'].dropna()

def chuliName(df):
    df = df.loc[~df['姓名'].isnull()]
    df['姓名'] = df['姓名'].astype('str')
    df = df.loc[~df['姓名'].str.contains('0|姓名|表|会计：|会计')]
    return df

def median(data):
    data.sort()
    half = len(data) // 2
    return (data[half] + data[~half])/2

def huizhong(df):
    renshu =  df['人数'].sum()
    total = df['总工资'].sum()
    mean = round(total/renshu,2)
    return renshu,total,mean

def groupbyDf(df):
    gp = df.groupby(['部门','xifen'])
    renshu = gp['姓名'].count()
    total = gp['实发数'].sum()
    mean = gp['实发数'].mean()
    median = gp['实发数'].median()
    result = pd.concat([renshu,total,mean,median],axis = 1)
    result =result.reset_index()
    # result.columns = ['部门','部门细分','人数','总工资','平均工资','中位数工资']
    return result

def groupbyBumen(df):
    df = df[['部门', '姓名', '实发数']]
    gp = df.groupby('部门')
    renshu = gp['姓名'].count()
    total = gp['实发数'].sum()
    mean = gp['实发数'].mean()
    median = gp['实发数'].median()
    result = pd.concat([renshu, total, mean, median], axis=1)
    result = result.reset_index()
    # result.columns = ['部门','部门细分','人数','总工资','平均工资','中位数工资']
    return result

def addHeji(df,median):
    result_bumen._append(['' * 5])
    renshu, total, mean = huizhong(df)
    lst = ['合计', renshu, total, mean, median]
    df.iloc[-1] = lst
    return df

df_laowu= chuliName(df_laowu)
df_laowu = df_laowu[['行次','姓名','实发数']]
df_laowu.insert(0,'bumen','生产部')
df_laowu.columns = ['部门','xifen','姓名','实发数']
df_laowu.xifen = '车间-劳务'                                                                    #劳务工资

df_total = pd.concat([df_xg,df_shengcan,df_laowu],ignore_index = True)
df_total = df_total.sort_values(['部门','xifen'])
heji = df_total['实发数'].sum()
lst = ['合计','','',heji]
add = df_total.copy()
add = add.iloc[-2:,:]
add.iloc[-1,:] = lst
df_total1 = pd.concat([df_total,add],axis = 0)               #行管、生产、劳务工资汇总
df_up = df_total1.iloc[:-2,:]
df_down = df_total1.iloc[-1:,:]
df_total1 = pd.concat([df_up,df_down],axis = 0)
shifashu_lst = df_total1['实发数'].to_list()
median = median(shifashu_lst)
#计算中位数工资

fname_gongzi = r"工资汇总.xlsx"
sheet_name = '工资'
with pd.ExcelWriter(fname_gongzi,engine='openpyxl', date_format='yyyy-m-d', mode='a',
                    if_sheet_exists='replace') as writer:                       #replace,overlay
    df_total1.to_excel(writer, sheet_name, index=False)

result = groupbyDf(df_total)
result.columns = ['部门','部门细分','人数','总工资','平均工资','中位数工资']
result.sort_values(['部门','部门细分'])
result.to_excel('部门细分平均工资.xlsx',index = False)

result_bumen = groupbyBumen(df_total)
result_bumen.columns = ['部门','人数','总工资','平均工资','中位数工资']
result_bumen = addHeji(result_bumen,median)
result_bumen.to_excel('部门平均工资.xlsx',index = False)

os.startfile('部门细分平均工资.xlsx')
os.startfile('部门平均工资.xlsx')
os.startfile('工资汇总.xlsx')





