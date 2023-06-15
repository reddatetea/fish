'''
核对胶套价格
'''
# _*_ coding:utf-8 _*_
import pandas as pd
import os
import datetime
import jiaotaojisuanPd
import NewGongyinshang
import easygui

def Dangyue(start_riqi,end_riqi):
    dtrq = datetime.date.today().strftime('%Y%m%d')    #当天日期
    path = r'F:\a00nutstore\006\zw\duizhang'
    os.chdir(path)
    filename = '胶套当月入库%s.xlsx'%dtrq
    fname = os.path.join(path, filename)
    fname_gy = r'F:\a00nutstore\006\zw\price\胶套供应商.xlsx'
    jianchen = NewGongyinshang.Gongyingshang(fname_gy)
    # jianchen = {'浙江海悦':'海悦',
    #             '钟祥市鑫众包装有限公司':'钟祥'
    #             }
    fname2 = r'F:\a00nutstore\006\zw\原材料实时流水账\原材料实时流水账.xlsx'
    df = pd.read_excel(fname2, sheet_name='流水账', usecols=[0, 1, 2, 3, 5, 6, 7, 9, 10],index_col=0,dtype = {'单据号':str})  # usecols直接取所取的行
    df.sort_index(inplace=True)  # 对索引排序
    df = df.truncate(before=start_riqi, after=end_riqi)
    df = df.loc[df['供货单位'].isin(jianchen)]  # isin非常实用
    for j in ['leibie', 'kaibie', 'yeshu','chang','kuan']:
        df[j] = None
    for j in ['合同单价','合同金额', '多计', '多计金额']:
        df[j] = 0.0                             #0.0是flaost64,0是ind64
    df [ '备注'] = None
    df = df.assign(leibie=df['品名'].map(lambda  x: jiaotaojisuanPd.jiaotaochicun(x)[0]))
    df = df.assign(kaibie=df['品名'].map(lambda x: jiaotaojisuanPd.jiaotaochicun(x)[1]))
    df = df.assign(yeshu=df['品名'].map(lambda x: jiaotaojisuanPd.jiaotaochicun(x)[2]))
    df = df.assign(chang=df['品名'].map(lambda x: jiaotaojisuanPd.jiaotaochicun(x)[3]))
    df = df.assign(kuan=df['品名'].map(lambda x: jiaotaojisuanPd.jiaotaochicun(x)[4]))
    df = df.reset_index()
    return fname,jianchen,df

def Hetong(end_riqi):
    fname = r'F:\a00nutstore\006\zw\price\胶套合同价格.xlsx'
    sheet_name = '合同单价'
    df = pd.read_excel(fname, sheet_name, index_col=0)
    grouped = df.groupby('供货单位')
    all_values = []
    for gys, values in grouped:
        grouped2 = values.groupby(['leibie','kaibie','yeshu','chang','kuan'])
        for riqi_leibie,values1 in grouped2:
            last_day = end_riqi
            values1.loc[last_day, '供货单位'] = gys
            values1 = values1.resample('D').ffill()
            values1.fillna(method='ffill', inplace=True)
            all_values.append(values1)
    df2 = pd.concat(all_values, axis=0)
    df2 = df2.reset_index()
    # df2.drop_duplicates(subset=['日期','leibie','kaibie','yeshu','chang','kuan'],keep='last',inplace=True)
    return df2

def dfMerge(df1, df2):
    df8 = pd.merge(df1, df2, on=['日期', '供货单位','leibie','kaibie','yeshu','chang','kuan'], how='left')  # 连接！从python的传统字典到pandas的连接！量变到质变的飞跃！
    return df8

def huizhong(jianchen,fname,df8):
    df8['合同单价'] = df8['danjia']
    df8['合同金额'] = round(df8['合同单价'] * df8['入库数量'], 2)
    df8['多计'] = df8['入库单价'] - df8['合同单价']
    df8['多计金额'] = df8['入库金额'] - df8['合同金额']
    beizhu_where = df8.columns.tolist().index('备注')+1
    df9 = df8.iloc[:, :beizhu_where]
    grouped = df9.groupby('供货单位')
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
            values1.to_excel(writer, sheet_name='{}'.format(gys), index=False)

def main():
    start_riqi = pd.Timestamp(easygui.enterbox('请输入入库起始日期期间：格式为2021-11-4：'))
    end_riqi = pd.Timestamp(easygui.enterbox('请输入入库结束日期期间：格式为2021-11-4：'))
    fname,jianchen,df1  = Dangyue(start_riqi,end_riqi)
    df2 = Hetong(end_riqi)
    df8 = dfMerge(df1, df2)
    huizhong(jianchen, fname, df8)
    os.startfile(fname)

if __name__ == '__main__':
    main()














