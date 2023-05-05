'''
通过指定的起止日期，及供应商简称，查询流水账，并自动在excel中显示出来
'''
import pandas as pd
import numpy as np
import os
import xlwings as xw
import fuliaoLastPrice
import easygui
import chinesetopinyin

def query():
    fname0 = r'F:\a00nutstore\006\zw\原材料实时流水账\原材料实时流水账.xlsx'
    ws_name0 = '流水账'
    df = pd.read_excel(fname0, ws_name0, index_col=0)
    df.sort_index(inplace=True)  # 对索引排序
    gys = list(df['供货单位'].unique())
    gys.sort(key=lambda x: chinesetopinyin.getpinyin(x))
    start_riqi = pd.Timestamp(input('请输入入库起始日期期间：格式为2021-11-4：\n'))
    end_riqi = pd.Timestamp(input('请输入入库结束日期期间：格式为2021-11-4：\n'))
    piaojuhao = int(input('请输入票据号90031065：\n'))
    # 单个还是多个供应商查询
    msg = '请选择单个还是多个供应商查询'
    print(msg)
    choice = easygui.buttonbox(msg, title='打印excel工作表', choices=['单个查询', '多个查询'])
    if choice == '单个查询':
        gys = input('请输入要查询的供应商简称：\n')
        df = df[df['供货单位'].str.contains(gys)]
        gys = [gys]
    else:
        gys = easygui.multchoicebox('请选择要查询的多个供应商', choices=gys)
        df = df[df['供货单位'].isin(gys)]
    df = df.truncate(before=start_riqi, after=end_riqi)
    df = df.loc[df['单据号'] >= piaojuhao]
    return gys,start_riqi,end_riqi,df

def Hetong(end_riqi ):
    fname = r'F:\a00nutstore\006\zw\price\辅料合同价格.xlsx'
    sheet_name = '合同单价'
    df = pd.read_excel(fname, sheet_name, index_col=0)
    grouped = df.groupby('供货单位')
    all_values = []
    for gys, values in grouped:
        grouped2 = values.groupby(['品名', '单位'])
        for riqi_leibie, values1 in grouped2:
            last_day = pd.Timestamp(end_riqi )
            values1.at[last_day, '供货单位'] = gys
            values1 = values1.resample('D').ffill()
            values1.fillna(method='ffill', inplace=True)
            all_values.append(values1)
    df2 = pd.concat(all_values, axis=0)
    df2 = df2.reset_index()
    return df2

def dfMerge(df, df2):
    df8 = pd.merge(df, df2, on=['日期', '供货单位','品名','单位'], how='left')  # 连接！从python的传统字典到pandas的连接！量变到质变的飞跃！
    return df8

def gjyJianchen():
    fname = r'F:\a00nutstore\006\zw\query\gongyingshang.xlsx'
    df = pd.read_excel(fname)
    dic = dict(zip(df.changku.to_list(),df.jianchen.to_list()))
    print(dic)
    return dic

def main():
    gys,start_riqi,end_riqi,df = query()
    df = df.iloc[:,:9]
    df2 = Hetong(end_riqi)
    df2 = df2.iloc[:,:-1]
    end_riqi1 = start_riqi - pd.Timedelta(days=1)  #原开始时间的前一天为查询最近价格的结束时间
    path = r'F:\a00nutstore\006\zw\query'
    jianchen_dic = gjyJianchen()
    fname_query = os.path.join(path, "流水账查询.xlsx")
    app = xw.App(visible=False, add_book=False)
    wb = app.books.add()
    grouped = df.groupby('供货单位')
    for gys,values in grouped:
        dic = fuliaoLastPrice.lastprice('2018-12-25', end_riqi1, gys)  # 指定开始时间为2021-1-1
        df8 = dfMerge(values, df2)
        df8 = df8.assign(最后单价=df8.apply(lambda x: dic.get((x.供货单位, x.品名, x.单位), 0), axis=1))
        df8['合同金额'] =round(df8['合同单价']*df8['入库数量'],2)
        df8['最近金额'] = round(df8['最后单价'] * df8['入库数量'], 2)
        df8.at['合计','入库数量']=df8['入库数量'].sum()
        df8.at['合计', '入库金额'] = df8['入库金额'].sum()
        df8.at['合计', '合同金额'] = df8['合同金额'].sum()
        df8.at['合计', '最近金额'] = df8['最近金额'].sum()
        ws_name = jianchen_dic.get(gys,gys)
        ws = wb.sheets.add(ws_name)
        ws.range('a1').options(pd.DataFrame, index=False).value = df8
        ws.autofit()
    wb.save(fname_query)
    app.quit()
    os.startfile(fname_query)

if __name__=='__main__':
    main()

