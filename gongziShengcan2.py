'''
汇总生产人员工资

'''

import pandas as pd
import os
import openpyxl
import re
import easygui
import win32com.client as win32


def chuliName(df,chejian):

    df['卡号'] = df['卡号'].fillna('发现金')
    df = df.loc[~df['姓名'].isnull()]

    df['姓名'] = df['姓名'].astype('str')
    df = df.loc[~df['姓名'].str.contains('0|姓名|表|会计：|会计')]
    df['车间'] = chejian
    return df

def xlsXlsx(fname):
    print('正将excel低版本xls转化为高版本xlsx，请稍等:')
    excel = win32.DispatchEx('Excel.Application')
    excel.Visible = 0
    excel.DisplayAlerts = 0
    newname = fname + 'x'
    wb = excel.Workbooks.Open(fname)
    wb.SaveAs(newname, FileFormat = 51)
    wb.Close()
    excel.Application.Quit()
    return newname

# 柔印
def rouyin(fname, chejian,sheet_name):
    names = ['车间',
             '卡号',
             '姓名',
             '工资',
             '考评',
             '补贴',
             '生活补贴',
             '保底',
             '工龄',
             '奖励',
             '节约',
             '水电费',
             '罚款',
             '物耗',
             '代扣社保',
             '扣税',
             '补扣税',
             '实发数',
             '领款人签名',
             '保底人员金额']
    usecols = 'A:K,M:R,T,U,W'
    df = pd.read_excel(fname, sheet_name=sheet_name, names=names, usecols=usecols, skiprows=3)  # dtype={'卡号': "str"}
    df.insert(16,'借支',0)

    df = chuliName(df, chejian)
    index = df.columns.to_list().index('实发数')
    df1 = df.iloc[:, :17]

    df2 = df.iloc[:, 17:]
    df = pd.concat([df1, df2], axis=1)

    return df

#简装
def jianzhuang(fname,chejian,sheet_name):
    names = ['车间',
 '卡号',
 '姓名',
 '工资',
 '考评',
 '补贴',
 '生活补贴',
 '保底',
 '工龄',
 '奖励',
 '节约',
 '水电费',
 '罚款',
 '物耗',
         '借支0',
  '代扣社保',
 '扣税',
 '补扣税',
 '实发数',
 '领款人签名',
 '保底人员金额']
    usecols = 'A:C,F:Q,S:X'
    df = pd.read_excel(fname, sheet_name=sheet_name,names = names,usecols = usecols,skiprows =3)     #dtype={'卡号': "str"}
    df.insert(16,'借支',0)
    df['借支'] = df['借支0']
    df.drop('借支0', axis=1, inplace=True)
    df = chuliName(df,chejian)


    return df


# 胶印
def jiaoyin(fname, chejian,sheet_name):
    names = ['车间',
             '卡号',
             '姓名',
             '工资',
             '考评',
             '补贴',
             '生活补贴',
             '保底',
             '工龄',
             '奖励',
             '节约',
             '水电费',
             '罚款',
             '物耗',
             '代扣社保',
             '扣税',
             '补扣税',
             '实发数',
             '领款人签名',
             '保底人员金额'
             ]
    usecols = 'A:Q,S,T,U'
    df = pd.read_excel(fname, sheet_name=sheet_name, names=names, usecols=usecols, skiprows=3)
    df.insert(16,'借支',0)
    df = chuliName(df, chejian)

    return df


# 成品
def chengpin(fname, chejian,sheet_name):
    names = ['车间',
             '卡号',
             '姓名',
             '工资',
             '考评',
             '补贴',
             '生活补贴',
             '保底',
             '工龄',
             '奖励',
             '节约',
             '水电费',
             '罚款',
             '物耗',
             '代扣社保',
             '扣税',
             '补扣税',
             '实发数',
             '领款人签名',
             '保底人员金额'
             ]

    usecols = 'A:T'
    df = pd.read_excel(fname, sheet_name=sheet_name, names=names, usecols=usecols, skiprows=3)  # dtype={'卡号': "str"}
    df.insert(16,'借支',0)
    df = chuliName(df, chejian)
    return df


# 夹子
def jiazi(fname, chejian,sheet_name):
    names = ['车间',
             '卡号',
             '姓名',
             '工资',
             '考评',
             '补贴',
             '生活补贴',
             '保底',
             '工龄',
             '奖励',
             '节约',
             '水电费',
             '罚款',
             '物耗',
             '代扣社保',
             '扣税',
             '补扣税',

             '实发数',
             '领款人签名',
             '保底人员金额'
             ]

    usecols = 'A:T'
    df = pd.read_excel(fname, sheet_name=sheet_name, names=names, usecols=usecols, skiprows=3)
    df.insert(15, '借支', 0)
    df = chuliName(df, chejian)
    return df


# 书芯
def shuxin(fname, chejian,sheet_name):
    names = ['车间',
             '卡号',
             '姓名',
             '工资',
             '考评',
             '补贴',
             '生活补贴',
             '保底',
             '工龄',
             '奖励',
             '节约',
             '水电费',
             '罚款',
             '物耗',
             '代扣社保',
             '扣税',
             '补扣税',
             '实发数',
             '领款人签名',
             '保底人员金额'
             ]

    usecols = 'A:Q,R,S,U'
    df = pd.read_excel(fname, sheet_name=sheet_name, names=names, usecols=usecols, skiprows=3)
    df.insert(16,'借支',0)
    df = chuliName(df, chejian)
    index = df.columns.to_list().index('实发数')
    df1 = df.iloc[:, :17]

    df2 = df.iloc[:, 17:]
    df = pd.concat([df1, df2], axis=1)
    return df


def main():
    fname_gongzi = r'F:\a00nutstore\008\zw08\gongzi\生产人员工资.xlsx'
    sheet_name_gz = '工资'
    path = easygui.diropenbox(msg='请点选“生产人员工资表所在路径”')
    os.chdir(path)
    filelist = os.listdir(path)
    sheet_name = r'工资表'
    for file in filelist:
        if '柔印工资表' in file:
            chejian = '柔印'
            df_rouyin = rouyin(file, chejian,sheet_name)
        elif '简装工资表' in file:
            chejian = '简装'
            df_jianzhuang = jianzhuang(file, chejian,sheet_name)
        elif '胶印工资表' in file:
            chejian = '胶印'
            df_jiaoyin = jiaoyin(file, chejian,sheet_name)
        elif '成品工资表' in file:
            chejian = '成品'
            df_chengpin = chengpin(file, chejian,sheet_name)
        elif '夹子工资表' in file:
            chejian = '夹子'
            df_jiazi = jiazi(file, chejian,sheet_name)
        elif '书芯工资表' in file:
            fname = os.path.join(path, file)
            # fname = xlsXlsx(fname)
            if os.path.splitext(fname)[-1].lower() == '.xls':
                fname = xlsXlsx(fname)

            elif len(os.path.splitext(fname)[-1]) >=6:
                continue

            else:
                fname = fname


            chejian = '书芯'
            df_shuxin = shuxin(fname, chejian,sheet_name)
        else:
            continue
    df = pd.concat([df_rouyin, df_shuxin, df_jiaoyin, df_jianzhuang, df_chengpin, df_jiazi])
    # df.to_excel(fname_gongzi,sheet_name = sheet_name_gz,index = False)
    # with pd.ExcelWriter(fname_gongzi, engine='openpyxl', date_format='yyyy-m-d', mode='a',
    #                     if_sheet_exists='replace') as writer:                       #replace,overlay
    #     df.to_excel(writer, sheet_name_gz, index=False)             #replace,overlay
    with pd.ExcelWriter(fname_gongzi, engine='openpyxl', date_format='yyyy-m-d', mode='a',
                        if_sheet_exists='replace') as writer:
        df.to_excel(writer, sheet_name_gz, index=False)             #replace,overlay
    os.startfile(fname_gongzi)


if __name__ == '__main__':
    main()











