'''
2022-8-15用pandas重写线圈小脚本，单位为卷的线圈也可以计算了
'''
# _*_ coding:utf-8 _*_

import pandas as pd
import easygui
import os
import datetime
import xianquanjisuanPd
import NewGongyinshang

def Dangyue(start_riqi,end_riqi):
    dtrq = datetime.date.today().strftime('%Y%m%d')    #当天日期
    path = r'F:\a00nutstore\006\zw\duizhang'
    os.chdir(path)
    filename = '线圈当月入库%s.xlsx'%dtrq
    fname = os.path.join(path, filename)
    fname_gy = r'F:\a00nutstore\006\zw\price\线圈供应商.xlsx'
    jianchen = NewGongyinshang.Gongyingshang(fname_gy)
    fname2 = r'F:\a00nutstore\006\zw\原材料实时流水账\原材料实时流水账.xlsx'
    df = pd.read_excel(fname2, sheet_name='流水账', usecols=[0, 1, 2, 3,4, 5, 6, 7, 9, 10], index_col=0,dtype = {'单据号':str})  # usecols直接取所取的行
    df.sort_index(inplace=True)  # 对索引排序
    df = df.truncate(before=start_riqi, after=end_riqi)
    df = df.loc[df['供货单位'].isin(jianchen)]  # isin非常实用
    for j in ['规格','color' ,'齿数', '单价（元/齿）', '单价（元/条)', '合同金额', '多计金额']:
        df[j] = 0.0  # 0.0是flaost64,0是ind64
    df['备注'] = None
    df = df.assign(规格=df['品名'].map(lambda x: xianquanjisuanPd.chicun(x)[0]))
    df = df.assign(color=df['品名'].map(lambda x: xianquanjisuanPd.chicun(x)[1]))
    df = df.assign(齿数=df['品名'].map(lambda x: xianquanjisuanPd.chicun(x)[2]))
    df = df.reset_index()
    return fname, jianchen, df

def Hetong(end_riqi):
    fname = r'F:\a00nutstore\006\zw\price\线圈合同价格.xlsx'
    sheet_name = '合同单价'
    df = pd.read_excel(fname, sheet_name, index_col=0)
    grouped = df.groupby('供货单位')
    all_values = []
    for gys, values in grouped:
        last_day = pd.Timestamp(end_riqi)
        values.loc[last_day, '供货单位'] = gys     #添加最后一行
        values = values.resample('D').ffill()     #resample之前，字段必须是时间格式，且已索引
        values.fillna(method='ffill', inplace=True) #填充最后一行NA
        all_values.append(values)
    df2 = pd.concat(all_values, axis=0)
    return df2

def dfMerge(df1,df2):
    df2 = df2.reset_index()
    df8 = pd.merge(df1, df2, on=['日期', '供货单位'], how='left')  #连接！从python的传统字典到pandas的连接！量变到质变的飞跃！
    return df8

def huizhong(jianchen,fname,df8):
    df8 = df8.assign(newguige=('tiao' + df8['规格']).where(df8['单位'] == '条', 'kun' + df8['规格']))
    df8 = df8.assign(xishu=(df8.color.map({'pure': 1.0, 'multi': 1.1, 'gold_silver': 1.2})).where(df8['单位'] == '条', 1))
    df8['单价（元/齿）'] = df8.apply(lambda x: x[x.newguige], axis=1) * df8.xishu
    df8['单价（元/条)'] = round((df8['单价（元/齿）'] * df8['齿数']).where(df8['单位'] == '条', df8['单价（元/齿）']),4)
    df8['合同金额'] = round(df8['单价（元/条)'] * df8['入库数量'],2)
    df8['多计金额'] = round(df8['入库金额'] - df8['合同金额'],2)
    df8  = df8.iloc[:,:18]
    grouped = df8.groupby('供货单位')
    with pd.ExcelWriter(fname,datetime_format='yyyy-m-d')  as writer:
        df8 = df8.append(df8.sum(numeric_only=True), ignore_index=True)
        df8.to_excel(writer, '当月正', index=False)
        for gys, values in grouped:
            gys = jianchen[gys]
            values1 = values.copy()
            values1.loc['合计', '日期'] = '合计'
            values1.at['合计', '入库数量'] = sum(values['入库数量'])
            values1.at['合计', '入库金额'] = sum(values['入库金额'])
            values1.at['合计', '合同金额'] = sum(values['合同金额'])
            values1.at['合计', '多计金额'] = sum(values['多计金额'])
            values1.to_excel(writer, sheet_name='{}'.format(gys) ,index=False)

def main():
    start_riqi = pd.Timestamp(easygui.enterbox('请输入入库起始日期期间：格式为2021-5-26:'))
    end_riqi = pd.Timestamp(easygui.enterbox('请输入入库结束日期期间：格式为2022-8-4：'))
    fname, jianchen, df1 = Dangyue(start_riqi, end_riqi)
    df2 = Hetong(end_riqi)
    df8 = dfMerge(df1, df2)
    huizhong(jianchen, fname, df8)
    os.startfile(fname)

if __name__ == '__main__':
    main()



















