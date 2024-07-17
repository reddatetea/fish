'''
荡总行管人员工资

'''
import easygui
import pandas as pd
import numpy as np
import re
import os


def gongzi(fname, sheet_name):
    df = pd.read_excel(fname, sheet_name=sheet_name)
    skiprows = df.iloc[:, 2].to_list().index('姓名') + 1
    df = pd.read_excel(fname, sheet_name=sheet_name,skiprows = skiprows)
    df = df.loc[~df['姓名'].isnull()]
    df = df.drop(['序号'], axis=1)
    for i in ['公司', '部门'][::-1]:
        df.insert(0, i, '')
    if '双佳' in fname:
        df['公司'] = '双佳'
    else:
        df['公司'] = '莱特'
    df['账      号'] = df['账      号'].fillna('现金')
    df['部门'] = df['账      号']
    df = df[df['账      号'].str.contains('账      号|合计|本页') == False]
    lst = [np.nan if '计' not in i else i for i in df['账      号']]
    df = df.assign(部门=lst)
    df['部门'].fillna(method="bfill", axis=0, inplace=True)
    df = df[df['账      号'].str.contains('计') == False]
    pattern = r'(?P<bumen>\w+)小计(?:.*)'
    regexp = re.compile(pattern)
    repl = lambda m: m.group('bumen')
    df['部门'] = df['部门'].str.replace(regexp, repl, regex=True)
    index = df.columns.to_list().index('考勤')
    return df


def main():
    fname_gongzi = r"F:\a00nutstore\008\zw08\gongzi\行管工资.xlsx"
    sheet_name_gz = '工资'
    columns_name = ['公司',
                    '部门',
                    '账号',
                    '姓名',
                    '基本工资',
                    '团体奖金',
                    '效益奖金',
                    '话费职补高温',
                    '考勤奖',
                    '加班工资',
                    '考核分数',
                    '考评基数',
                    '消防分数',
                    '消防基数',
                    '计件/考核',
                    '绩效',
                    '安全分',
                    '安全责任基数',
                    '安全奖',
                    '考勤',
                    '奖罚',
                    '其他',
                    '社保',
                    '应发数',
                    '个税',
                    '实发数',
                    '备注',
                    '签名']

    def getDf(msg):
        fname = easygui.fileopenbox(msg=f'请点选{msg}工资表.xlsx')
        df = pd.read_excel(fname, sheet_name=None)
        sheetnames = list(df)
        sheet_name = easygui.choicebox(title='请点选工作表', choices=sheetnames)
        return fname,df,sheet_name
    def getDicJibie():
        fname1 = r"F:\a00nutstore\008\zw08\gongzi\工资级别.xlsx"
        sheet_name1 = r'级别'
        df_jibie = pd.read_excel(fname1, sheet_name1, dtype={'账号': "str"})
        dic_gongzi = dict(zip(df_jibie['账号'], zip(df_jibie['基本工资0'], df_jibie['考评基数0'], df_jibie['效益奖金0'])))
        return dic_gongzi

    for i in ['双佳','莱特']:
        if i == '双佳':
            fname,df,sheetname = getDf(i)
            path, file = os.path.split(fname)
            os.chdir(path)
            df_sj = gongzi(fname, sheetname)
            index = df_sj.columns.to_list().index('考勤')
            for i in ['绩效', '安全分', '安全责任基数', '安全奖'][::-1]:
                df_sj.insert(index, i, 0)
            df_sj.columns = columns_name
        else:
            fname,df,sheetname = getDf(i)
            df_laite = gongzi(fname, sheetname)
            df_laite.columns = columns_name

    df = pd.concat([df_sj, df_laite])
    df.index = range(df.shape[0])
    index = df['账号'].to_list().index('6230290032789725')
    df['公司'] = np.where(df.index < index, df['公司'], '物业')
    dic_jibie = getDicJibie()
    df['基本工资0'] = df['账号'].map(lambda x:dic_jibie.get(x,(0,0,0))[0])
    df['考评基数0'] = df['账号'].map(lambda x: dic_jibie.get(x, (0, 0, 0))[1])
    df['效益奖金0'] = df['账号'].map(lambda x: dic_jibie.get(x, (0, 0, 0))[2])
    # df['团休奖金0'] = round(df['考评基数0']*df['考核分数'],2)
    df['基本工资测试'] = df['基本工资0'] - df['基本工资']
    df['考评基数测试'] = df['考评基数0'] - df['考评基数']
    df['效益奖金测试'] = df['效益奖金0'] - df['效益奖金']
    df['考评基数0'] = df['考评基数0'].fillna(0)
    df['考核分数'] = df['考核分数'].fillna(0)
    df['团体奖金0'] = round(df['考评基数0']*df['考核分数'],0)
    df['团体奖金测试'] = df['团体奖金0'] -df['团体奖金']
    with pd.ExcelWriter(fname_gongzi, engine='openpyxl', date_format='yyyy-m-d', mode='a',
                        if_sheet_exists='replace') as writer:
        df.to_excel(writer, sheet_name_gz, index=False)             #replace,overlay
    os.startfile(fname_gongzi)


if __name__ == '__main__':
    main()











