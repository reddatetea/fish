'''
对T+CLOUD上的收发存汇总表进行二次开发，与公司以前的格式一致
此版本加零结存，将抄本中的小学生按原顺序排列
此版本增加一个按销售订单生成昨日出库的选项
计算两者的差异
'''
import os
import datetime
import easygui
import numpy as np
import pandas as pd
import openpyxl
from openpyxl.styles import Font, Border, Side, Fill, Alignment
import formatPainter

lst = ['仓库编码',
       '仓库',
       '存货分类 (1级)',
       '存货分类 (2级)',
       '存货分类 (3级)',
       '存货分类 (4级)',
       '存货分类 (5级)',
       '存货编码',
       '存货',
       '存货代码',
       '数量(主单位)',
       '平均单价',
       '金额',
       '数量(辅单位)',
       '计量单位组合',
       '数量(主单位).1',
       '平均单价.1',
       '金额.1',
       '数量(辅单位).1',
       '计量单位组合.1',
       '数量(主单位).2',
       '平均单价.2',
       '金额.2',
       '数量(辅单位).2',
       '计量单位组合.2',
       '数量(主单位).3',
       '平均单价.3',
       '金额.3',
       '辅数量',
       '计量单位组合.3']
lst2 = [
    'store',
    'num',
    'class01',
    'class02',
    'class03',
    'class04',
    'class05',
    'code',
    'stock',
    'content',
    'begin_ben',
    '平均单价',
    '金额',
    'begin_jian',
    '计量单位组合',
    'ruku_ben',
    '平均单价.1',
    '金额.1',
    'ruku_jian',
    '计量单位组合.1',
    'chuku_ben',
    '平均单价.2',
    '金额.2',
    'chuku_jian',
    '计量单位组合.2',
    'end_ben',
    '平均单价.3',
    '金额.3',
    'end_jian',
    '计量单位组合.3']

lst3 = [
    'class02',
    'class05',
    'code',
    'stock',
    'content',
    'begin_ben',
    'begin_jian',
    'ruku_ben',
    'ruku_jian',
    'chuku_ben',
    'chuku_jian',
    'end_ben',
    'end_jian',
]

lst_yeterday_ruku = ['class02',
                     'class05',
                     'code',
                     'stock',
                     'begin_ben',
                     'begin_jian',
                     'ruku_ben',
                     'ruku_jian',
                     ]
lst_yeterday_ruku1 = ['class02',
                      'class05',
                      'code',
                      'stock',
                      'yesterday_ben',
                      'yesterday_jian',
                      'yesterday_ruku_ben',
                      'yesterday_ruku_jian',
                      ]

lst01_yesterday = [
    'class02',
    'class05',
    'code',
    'stock',
    'begin_ben',
    'begin_jian',
    'ruku_ben',
    'ruku_jian',
    'chuku_ben',
    'chuku_jian',
]
lst02_yesterday = [
    'class02',
    'class05',
    'code',
    'stock',
    'yesterday_ben',
    'yesterday_jian',
    'yesterday_ruku_ben',
    'yesterday_ruku_jian',
    'yesterday_chuku_ben',
    'yesterday_chuku_jian',

]
lst_merge0 = ['class02',
              'class05',
              'code',
              'stock',
              'content',
              'begin_ben',
              'begin_jian',
              'ruku_ben',
              'ruku_jian',
              'chuku_ben',
              'chuku_jian',
              'end_ben',
              'end_jian',
              'yesterday_ben',
              'yesterday_jian',
              'yesterday_ruku_ben',
              'yesterday_ruku_jian',
              'yesterday_chuku_ben',
              'yesterday_chuku_jian']

lst_merge = ['class02', 'class05', 'code', 'stock',
             'content',
             'begin_jian', 'yesterday_jian',
             'yesterday_ruku_jian', 'ruku_jian',
             'yesterday_chuku_jian', 'chuku_jian',
             'end_jian']

lst_result0 = ['class05', 'code', 'stock',
               'content',
               'begin_jian', 'yesterday_jian',
               'yesterday_ruku_jian', 'ruku_jian',
               'yesterday_chuku_jian', 'chuku_jian',
               'end_jian']

lst_result = ['类别', '货号', '品名',
              '含量',
              '月初', '上日',
              '本日入库', '入库累计',
              '本日出库', '出库累计',
              '结余']


def chuli(fname, store_num):
    df = pd.read_excel(fname, skiprows=7)
    df = df.iloc[:, 1:]
    df.columns = lst
    df.columns = lst2
    if store_num == '001库':
        df = df.loc[df.store == '001']
    elif store_num == '002电商库':
        df = df.loc[df.store == '002']
    else:
        df = df.loc[(df.store == '001') | (df.store == '002')]

    df['content'] = df['end_ben'] / df['end_jian']
    df = df[df['store'] != '制表人:']
    df = df[df['store'] != '合计：']
    df = df[df['store'].notnull()]
    df = df.iloc[:, 2:]
    df = df[lst3]
    return df


def chuli(fname, store_num):
    df = pd.read_excel(fname, skiprows=7)
    df = df.iloc[:, 1:]
    df.columns = lst
    df.columns = lst2
    if store_num == '001库':
        df = df.loc[df.store == '001']
    elif store_num == '002电商库':
        df = df.loc[df.store == '002']
    else:
        df = df.loc[(df.store == '001') | (df.store == '002')]

    df['content'] = df['end_ben'] / df['end_jian']
    df = df[df['store'] != '制表人:']
    df = df[df['store'] != '合计：']
    df = df[df['store'].notnull()]
    df = df.iloc[:, 2:]
    df = df[lst3]
    return df


# first,choice仓库编号
msg = '请点选仓库'
nums = ['001库', '002电商库', '总库']
num = easygui.buttonbox(msg, choices=nums)
msg = '请点选产成品"当日"工作表'
fname = easygui.fileopenbox(msg, title='AAA')
path, filename = os.path.split(fname)
os.chdir(path)
df1 = chuli(fname, num)
df11 = df1.copy()
msg = '请点选产成品"累计"工作表'
fname2 = easygui.fileopenbox(msg, title='BBB')
df2 = chuli(fname2, num)
df22 = df2.copy()

today_date = datetime.date.today()
yesterday_date = (today_date + datetime.timedelta(days=-1)).strftime("%Y-%m-%d")
msg = '报表日期是{}?'.format(yesterday_date)
choice = easygui.ccbox(msg, title='请选择"是"或"否"', choices=('是', '否'))
if choice:
    riqi = yesterday_date
else:
    msg = '请输入报表日期'
    riqi = easygui.enterbox(msg, title=" 昨天日期")
fname_canchengpin = '产成品报表差异{}.xlsx'.format(riqi)
wb = openpyxl.Workbook()
wb.save(fname_canchengpin)


#销售订单生成昨日出库
# 当日汇总表仅取入库数
df11 = df11[lst_yeterday_ruku]
df11.columns = lst_yeterday_ruku1
df22_df11 = pd.merge(df22, df11, how='left', on=['class02', 'class05', 'code', 'stock'], sort=False)
msg = '请点选工厂昨天的销售订单'
fname_dingdan = easygui.fileopenbox(msg, title='工厂昨天的销售订单工作表')
df_dingdan = pd.read_excel(fname_dingdan)
df_dingdan = df_dingdan[df_dingdan['单据执行状态'] != '合计']
df_dingdan = df_dingdan[['存货编码', '存货名称', '存货分类', '数量(本）', '数量2（件）']]
df_dingdan.columns = ['code', 'stock', 'class05', 'yesterday_chuku_ben', 'yesterday_chuku_jian']
# 汇总销售订单
gp_dingdan = df_dingdan.groupby(['class05', 'code', 'stock'])
yesterday_chuku_ben = gp_dingdan['yesterday_chuku_ben'].sum()
yesterday_chuku_jian = gp_dingdan['yesterday_chuku_jian'].sum()
df_dingdan_total = pd.DataFrame(
    {'yesterday_chuku_ben': yesterday_chuku_ben, 'yesterday_chuku_jian': yesterday_chuku_jian}).reset_index()
# 再连接销售订单
merge22 = pd.merge(df22_df11, df_dingdan_total, how='outer', on=['class05', 'code', 'stock'], \
                 sort=False)
merge22.class02 = merge22.class02.fillna(method='ffill')
merge22 = merge22.fillna(0)
merge22.content = (merge22.begin_ben + merge22.ruku_ben) / (merge22.begin_jian + merge22.ruku_jian)
merge22.chuku_jian = merge22.chuku_jian + merge22.yesterday_chuku_jian
merge22.end_jian = merge22.end_jian - merge22.yesterday_chuku_jian

# def chuliMerge(merge):
#     merge = merge[lst_merge]
#     merge = merge.iloc[:, 1:]
#     merge.columns = lst_result0
#     merge = merge[lst_result]
#     return merge
merge22 = merge22[lst_merge]
merge22  = merge22.iloc[:,1:]
merge22.columns = lst_result


#收发存汇总表直接生成
df1 = df1[lst01_yesterday]
df1.columns = lst02_yesterday
merge = pd.merge(df2, df1, how='left', on=['class02', 'class05', 'code', 'stock'], sort=False)  # merge
merge = merge.fillna(0)
merge.content = (merge.begin_ben + merge.ruku_ben) / (merge.begin_jian + merge.ruku_jian)
merge = merge[lst_merge]
merge  = merge.iloc[:,1:]
merge.columns = lst_result

for i in ['含量',
              '月初', '上日',
              '本日入库', '入库累计',
              '本日出库', '出库累计',
              '结余']:
    merge[i] = merge[i] * -1

result = pd.concat([merge22,merge],axis = 0)
gp = result.groupby('货号')
content = gp['含量'].mean()
yuechu = gp['月初'].sum()
shangri = gp['上日'].sum()
benriruku = gp['本日入库'].sum()
rukuleiji = gp['入库累计'].sum()
benrichuku = gp['本日出库'].sum()
chukuleiji = gp['出库累计'].sum()
jieyu = gp['结余'].sum()
dic = dict(zip( ['含量',
              '月初', '上日',
              '本日入库', '入库累计',
              '本日出库', '出库累计',
              '结余'],[content,yuechu,shangri,benriruku,rukuleiji,benrichuku,chukuleiji,jieyu]))
result1 = pd.DataFrame(dic)
result1.to_excel(fname_canchengpin)
os.startfile(fname_canchengpin)














