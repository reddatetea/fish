'''
pd处理原材料出库
'''
# -*-coding : utf-8 -*-
import pandas as pd
import easygui
from singleCailiaoRename import singlecailiaoName
import openpyxl
from openpyxl.utils import get_column_letter, column_index_from_string
import os


def totalPancunbiao():
    print('请点选原材料盘存表文件')
    fname = easygui.fileopenbox('请点选原材料盘存表文件')
    path,filename = os.path.split(fname)
    sheet_name = pd.ExcelFile(fname).sheet_names[0]   #fisrt sheet
    df = pd.read_excel(fname,sheet_name)
    df = df.loc[~df.存货大类名称.str.contains('小计|合   计')]
    df = df.iloc[:, :-2]
    df = df.assign(cwName=df['品名'].map(lambda x: singlecailiaoName(x)[0]))
    df1 = pd.pivot_table(df, index='cwName', aggfunc='sum', fill_value=0,
                         margins=True, margins_name='合计')
    df1 = df1.reset_index()

    return df1,path


def totalShuliangjiner():
    print('请点选数量文件')
    fname = easygui.fileopenbox('请点选原材料数量文件')
    # fname = r'F:\a00nutstore\006\zw\2021\202111\1130数量金额.xls'
    df = pd.read_excel(fname)
    df = df.loc[~df.科目编码.str.contains('小计|合计')]
    df = df.assign(期初方向=df['期初方向'].map({'借': 1.0, '贷': -1.0, '平': 1.0}))
    df = df.assign(期末方向=df['期末方向'].map({'借': 1.0, '贷': -1.0, '平': 1.0}))
    df['期初数量'] = df['期初数量'] * df['期初方向']
    df['期初金额'] = df['期初金额'] * df['期初方向']
    df['期末数量'] = df['期末数量'] * df['期末方向']
    df['期末金额'] = df['期末金额'] * df['期末方向']
    df['科目名称'] = df['科目名称'].str.strip()
    df['会计期间'] = df['会计期间'].str[-7:]
    df['会计期间'] = df['会计期间'].str.replace('.', '-')
    qijian = df['会计期间'].to_list()[-1]
    for j in ['会计年度', '外币名称', '期初方向', '期末方向', '期末借方', '期末贷方']:
        del df[j]
    return df, qijian


def weida(qijian, xia_qijian, fname, sheet_name):
    df = pd.read_excel(fname, sheet_name)
    df.dropna(subset=['记账'], inplace=True)
    df = df[(df['期间'] == xia_qijian)]
    # df = df[(df['期间']==xia_qijian) & (df['记账']!=None)]   #连着一起写好象不行！？
    return df


def shuliang_baiyun(x):
    if x.品名 == '卷筒纸':
        shuliang = x['数量(吨)'] * 1000
    else:
        shuliang = x['数量(令)']
    return shuliang


def shuliang_zhi(x):
    if '卷筒纸' in x['jd']:
        shuliang = x['入库(吨)'] * 1000
    else:
        shuliang = x['入库']
    return shuliang


def main():
    df_cangku ,path = totalPancunbiao()
    os.chdir(path)
    df_caiwu, qijian = totalShuliangjiner()
    df1 = pd.merge(df_cangku, df_caiwu, left_on='cwName', right_on='科目名称', how='outer')
    df1 = df1.sort_values('科目编码')

    if int(qijian[-2:]) != 12:
        xia_qijian = qijian[:-2] + '%02d' % (int(qijian[-2:]) + 1)
    else:
        xia_qijian = str(int(qijian[:-3]) + 1) + '-01'  # 年底处理期间
    # 白云未达
    fname = r'F:\a00nutstore\006\zw\baiyun\2020白云入库.xlsx'
    sheet_name = r'2020'
    df = weida(qijian, xia_qijian, fname, sheet_name)
    df = df.assign(未达项=df.apply(lambda x: shuliang_baiyun(x), axis=1))
    df_baiyun = df[['品名', '未达项']]
    df_baiyun = df_baiyun.rename({'品名': 'cwName'}, axis=1)
    print(df_baiyun)

    # 纸未达
    fname = r'F:\a00nutstore\006\zw\else\2020入库.xlsx'
    sheet_name = r'入库'
    df = weida(qijian, xia_qijian, fname, sheet_name)
    df = df.assign(未达项=df.apply(lambda x: shuliang_zhi(x), axis=1))
    df_zhi = df[['jd', '未达项']]
    df_zhi = df_zhi.rename({'jd': 'cwName'}, axis=1)
    print(df_zhi)

    # 其它未达
    fname = r'F:\a00nutstore\006\zw\原材料实时流水账\原材料实时流水账.xlsx'
    sheet_name = r'流水账'
    df = weida(qijian, xia_qijian, fname, sheet_name)
    df_qita = df[['cwName', '入库数量']]
    df_qita = df_qita.rename({'入库数量': '未达项'}, axis=1)
    print(df_qita)

    # 未达字典
    weida_data = pd.concat([df_baiyun, df_zhi, df_qita])
    weida_pivot = pd.pivot_table(weida_data, index='cwName', aggfunc='sum')
    df2 = pd.merge(df1, weida_pivot, on='cwName', how='left')  # 原表
    df_cankao = df2
    df_cankao.dropna(subset=['科目编码'], inplace=True)
    chayi = []
    shijichayi = []  # pandas可以这样写公式01
    chuku = []
    jiner = []
    tiesi_num = df_cankao['cwName'].to_list().index('铁丝')
    for i in range(2, df_cankao.shape[0] + 2):
        if i-2  != tiesi_num :
            chayi.append('=B{}+C{}-J{}-L{}'.format(i, i, i, i))
            shijichayi.append('=R{}+S{}'.format(i, i))  # pandas可以这样写公式02
            chuku.append('=D{}'.format(i))
            jiner.append('=IF(J{}+L{}-U{}=0,K{}+M{},ROUND(U{}*V{},2))'.format(i, i, i, i, i, i, i))
        else :
            chayi.append('=2*B{}+2*C{}-J{}-L{}'.format(i, i, i, i))
            shijichayi.append('=2*R{}+S{}'.format(i, i))  # pandas可以这样写公式02
            chuku.append('=2*D{}'.format(i))
            jiner.append('=IF(J{}+L{}-U{}=0,K{}+M{},ROUND(U{}*V{},2))'.format(i, i, i, i, i, i, i))


    df_cankao['差异'] = chayi
    df_cankao['实际差异'] = shijichayi  # pandas可以这样写公式03
    df_cankao['出库'] = chuku

    try:
        df_cankao['单价'] = df_cankao['期末金额'] / df_cankao['期末数量']
    except:
        df_cankao['单价'] = 0
    df_cankao['金额'] = jiner

    msg = '请点选本月材料出库文件所在文件夹"202012"'
    print(msg)
    path = easygui.diropenbox(msg)
    filename = r'原材料{}出库参考.xlsx'.format(qijian)
    fname = os.path.join(path, filename)
    with pd.ExcelWriter(fname) as writer:
        df1.to_excel(writer, '原表', index=False)
        df_cankao.to_excel(writer, '出库参考', index=False)
        df_cankao.to_excel(writer, '出库参考 Copy', index=False)
    os.startfile(fname)


if __name__ == '__main__':
    main()