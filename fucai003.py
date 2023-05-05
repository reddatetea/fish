import pandas as pd
from itertools import combinations
import xlwings as xw
import numpy as np
import os

def getDf0(fname,columns,columns_effect):
    df0 = pd.read_csv(fname, sep=' ', header=None, names=columns)
    df0 = df0.iloc[:, :len(columns_effect)]
    df0.columns = columns_effect
    df0 = df0.replace('-', np.nan)  # 有时试机号出来，而实际数并未出来，相关处理
    df0 = df0.dropna()
    dic = dict(zip(columns_effect, ['str'] * len(columns_effect)))
    df0 = df0.astype(dic)
    df0 = df0.assign(ddd=df0.apply(lambda x: x['bai'] + x['shi'] + x['ge'], axis=1))
    return df0

def getDfTmpDan(df0,num_lst):
    data = []
    for i in num_lst:
        data0 = []
        for x, y, z in zip(df0['bai'], df0['shi'], df0['ge']):
            a = set([x, y, z])
            if (x in i and y in i and z in i) and (len(a) == 3):
                data0.append(1)
            else:
                data0.append("")
        data.append(data0)
    dic = dict(zip(num_lst, data))
    df_tmp = pd.DataFrame(dic, index=range(df0.shape[0]), columns=num_lst)
    return df_tmp

def getDfTmpShuang(df0,num_lst):
    data = []
    for i in num_lst:
        data0 = []
        for x, y, z in zip(df0['bai'], df0['shi'], df0['ge']):
            a = set([x, y, z])
            if (x in i and y in i and z in i) and (len(a) < 3):
                data0.append(1)
            else:
                data0.append("")
        data.append(data0)
    dic = dict(zip(num_lst, data))
    df_tmp = pd.DataFrame(dic, index=range(df0.shape[0]), columns=num_lst)
    return df_tmp

def getDfTmpDanShuang(df0,num_lst):
    data = []
    for i in num_lst:
        data0 = []
        for x, y, z in zip(df0['bai'], df0['shi'], df0['ge']):
            a = set([x, y, z])
            if x in i and y in i and z in i:
                data0.append(1)
            else:
                data0.append("")
        data.append(data0)
    dic = dict(zip(num_lst, data))
    df_tmp = pd.DataFrame(dic, index=range(df0.shape[0]), columns=num_lst)
    return df_tmp

def combineDf(df0,df_tmp,num_lst,columns_effect):
    df_tmp = getDfTmpDan(df0, num_lst)
    df = pd.concat([df0, df_tmp], axis=1)
    df = df.astype({"bai": int, 'shi': int, 'ge': int})
    df1 = df.assign(he=df.apply(lambda x: x['bai'] + x['shi'] + x['ge'], axis=1))
    df1 = df1.astype({'he': str})
    df1 = df1.assign(hezhi=df1.he.str[-1])
    df1['hui'] = ''
    df1['xuhao'] = range(df1.shape[0])
    new_columns = columns_effect[:5] + ['ddd', 'hui'] + num_lst + ['he', 'hezhi', 'xuhao'] + columns_effect[-3:]
    df1 = df1.loc[:, new_columns]
    df1 = df1.astype({'he': int, 'hezhi': int})
    return df1

def main():
    fname_fucai = r'http://www.17500.cn/getData/3d.TXT'
    columns_fucai = ['开奖期号', '开奖日期', '开', '奖', '号', '试', '机', '号1', '机1', '球', '投注总额', '单选注数', '单选金额', '组三注数', '组三金额',
                     '组六注数', '组六金额']
    nums = ['0123456789']
    items = map(str, *nums)
    wumas = ["".join(i) for i in combinations(items,3)]
    columns_effect_fucai = ['qihao', 'riqi', 'bai', 'shi', 'ge', 'sbai', 'sshi', 'sge']
    columns_effect_ticai = columns_effect_fucai[:5]
    df0 = getDf0(fname_fucai, columns_fucai,columns_effect_fucai)
    df_tmp = getDfTmpDan(df0, wumas)
    df1 = combineDf(df0, df_tmp,wumas,columns_effect_fucai)
    df1.to_excel('sanmaxdan.xlsx', index=False)
    os.startfile('sanmaxdan.xlsx')

if __name__ == '__main__':
    main()


