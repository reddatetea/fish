import numpy as np
import pandas as pd
import datetime
import time
import easygui
import os


def judgePeriod(x,timeStr):
    today = x[:10]
    weekday = datetime.date.weekday(datetime.datetime.strptime(today,'%Y-%m-%d'))
    if 'nan' in x :
        
        if weekday not in [4,5,6]  :
            return '待提交'
        else :
            if weekday == 7 :
                return '待提交'
            else :
                return "weekend"  
    elif '待提交'  in x :
             return  '待提交'
    else :
        if today == timeStr:
            if f'{today} 00:00' <= x < f'{today} 22:00':
                return '22:00以前'
            elif f'{today} 22:00' <= x < f'{today} 23:00':
                return '22:00-23:00'
            elif f'{today} 23:00' <= x < f'{today} 24:00':
                return '23:00-24:00'
        else :
            return '24:00以后'
    return x


def getEndtime(timeStr):
    today = datetime.datetime.strptime(timeStr,'%Y-%m-%d')
    tomorrow = today + datetime.timedelta(days = 1)
    tomorrow_str = datetime.datetime.strftime(tomorrow,'%Y-%m-%d')
    return tomorrow_str

def getEachEndtime(df,columns):
    start = columns.index('学生姓名')
    nums = [i for i in columns[start+1:]]
    news = []
    for num in nums:
        # 格式化为时间元组
        timeArray = time.localtime((num-25569) * 86400.0)
        # 将时间元组转换为时间字符串
        timeStr = time.strftime('%Y-%m-%d',timeArray)
        news.append(timeStr)
    columns = ['学生姓名'] + news
    df.columns = columns
    for timeStr in news:
        tomorrow_str = getEndtime(timeStr)
        df[f'{timeStr}'] = df[f'{timeStr}'].astype('str').str[:5]
        df[f'{timeStr}'] = np.where(df[f'{timeStr}'].str[:2].isin(['00','01','02','03','04','05','06']),tomorrow_str + ' '+ df[f'{timeStr}']  ,timeStr + ' '+ df[f'{timeStr}'])
    return news,df

def getNat(x):
    if 'nan' in x:
        return pd.NaT
    else:
        return x

def hourMinute(x):
    x = x[-5:]
    hour, minute = x.split(':')
    if hour in ['00', '01', '02', '03', '04', '05', '06', '07']:
        hour = int(hour) + 24
    return hour, int(minute)

def strfill(x):
    x = str(int(x)).zfill(2)
    return x


fname = easygui.fileopenbox(msg = '请点选作业完成时间统计表.xlsx')
path,fname = os.path.split(fname)
os.chdir(path)
fname1 = easygui.fileopenbox(msg = '请点选七8班名单.xlsx')
df_name = pd.read_excel(fname1)
dfs = pd.read_excel(fname,sheet_name=None)
dfs_period = []
dfs_names = []
for sheet_name,df in dfs.items():
    if sheet_name == '汇总' :
        continue
    else :
        columns = df.columns.to_list()
        for j in columns:
            if j in ['学号','备注']:
                columns.remove(j)
        df = df[columns]
        news,df = getEachEndtime(df,columns)
        dfs_names.append(df)
        for timeStr in news:
            df2 = df.assign(period = df[f'{timeStr}'].map(lambda x:judgePeriod(x,timeStr)))
            gp = df2.groupby('period',sort = False).count()
            gp = pd.DataFrame(gp.loc[:,f'{timeStr}'])
            gp = gp.loc[gp.index != 'weekend']
            gp.at['合计',f'{timeStr}'] = gp[f'{timeStr}'].sum()
            dfs_period.append(gp)

df_period_total = pd.concat(dfs_period,axis = 1)
df_period_total = df_period_total.reindex(['22:00以前','22:00-23:00','23:00-24:00','24:00以后','待提交','合计'])
df_period_total.index.name = '完成作业时间段'

for index,df0 in enumerate(dfs_names):
    if index == 0:
        df = df0
    else :
        df = pd.merge(df,df0,left_on = '学生姓名',right_on = '学生姓名')

df2 = df.copy()
df2 = df2.set_index('学生姓名')
df2 = df2.applymap(lambda x:x[11:])
df2 = df2.applymap(getNat)
df_name = df_name.iloc[:,1:]
df_nameLst = pd.merge(df_name,df2,how = 'inner',on = '学生姓名')

df = df.set_index('学生姓名')
dels = []
columns = df.columns.to_list()
for i in columns:
    today = datetime.datetime.strptime(i,'%Y-%m-%d')
    weekday = datetime.date.weekday(today)
    if weekday in [4,5,6]:
        dels.append(i)
    else:
        continue
for i in dels:
    columns.remove(i)

columns = sorted(columns)
end_date = columns[-1]
result_fname = f'七8班作业速度排名{end_date}.xlsx'
df_time = df[columns]
df_time = df_time.applymap(getNat)
df1 = df_time.copy()
df1 = df1.dropna()
for i in columns:
    a = df1[f'{i}'].max()
    df_time[f'{i}'].fillna(a,inplace = True)
df_hour = df_time.applymap(lambda  x :hourMinute(x)[0])
df_hour['mean'] = df_hour.astype(int).mean(1)
df_hour['hour0'] = df_hour['mean'].apply(lambda x:int(x))
df_hour['minute'] =60*(df_hour['mean']-df_hour['hour0'])
df_hour = df_hour[['hour0','minute']]
df_minute = df_time.applymap(lambda  x :hourMinute(x)[1])
df_minute['minute'] = df_minute.astype(int).mean(1)
df_minute = df_minute[['minute']]
df_hf = pd.merge(df_hour,df_minute,how = 'inner',on = '学生姓名')
df_hf['minute_xy'] = round(df_hf['minute_x'] + df_hf['minute_y'],0)
df_hf['hour1'] = np.where(df_hf.minute_xy >= 60,1,0)
df_hf['hour'] = df_hf['hour0'] + df_hf['hour1']
df_hf['minute'] = np.where(df_hf.minute_xy < 60,df_hf.minute_xy,df_hf.minute_xy -60)
df_hf = df_hf[['hour','minute']]
df_hf = df_hf.applymap(strfill)
df_hf['end_time'] = df_hf['hour'] + ':' + df_hf['minute']
df_hf = df_hf[['end_time']]
df_hf = df_hf.reset_index()
df_total = pd.merge(df_name,df_hf,how = 'inner',on = '学生姓名')
df_total= df_total.sort_values('end_time')
df_total.index = range(1,len(df_hf)+1)
df_total.index.name = '排名'
df_total.columns = ['学号','学生姓名','平均完成作业时间']

with pd.ExcelWriter(result_fname, engine='openpyxl')  as writer:
    df_period_total.to_excel(writer,sheet_name = '时间段')
    df_nameLst.to_excel(writer, sheet_name= '同学',index = False)
    df_total.to_excel(writer,sheet_name = '排名')

os.startfile(result_fname)








