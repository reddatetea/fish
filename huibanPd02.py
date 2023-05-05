'''
灰板核对，pandas写的
'''
# _*_ coding:utf-8 _*_
import pandas as pd
import os
import datetime
import huibanjisuan02

def  Dangyue(start_riqi,end_riqi):
    dtrq = datetime.date.today().strftime('%Y%m%d')    #当天日期
    path = r'F:\a00nutstore\006\zw\duizhang'
    os.chdir(path)
    filename = '灰板当月入库%s.xlsx'%dtrq
    fname = os.path.join(path, filename)
    jianchen = {'武汉富业纸业有限公司':'富业',
                '舞钢市环能科技有限公司':'舞钢'
                }

    fname2 = r'F:\a00nutstore\006\zw\原材料实时流水账\原材料实时流水账.xlsx'
    df = pd.read_excel(fname2, sheet_name='流水账',usecols=[0,1,2,3,5,6,7,9,10],index_col=0)    #usecols直接取所取的行
    df.sort_index(inplace=True)  # 对索引排序
    df = df.truncate(before=start_riqi, after=end_riqi)
    df = df.loc[df['供货单位'].isin (jianchen)] #isin非常实用
    for j in ['单张吨数','吨数','合同单价', '合同金额', '多计', '多计金额']:
        df[j] = 0.0                             #0.0是flaost64,0是ind64
    df [ '备注'] = None

    df = df.assign(单张吨数=df['品名'].map(lambda x: huibanjisuan02.huibanchicun(x)[0]))
    df['类别'] = df['品名'].map(lambda x: huibanjisuan02.huibanchicun(x)[-1])
    df['吨数'] = df['入库数量']* df['单张吨数']
    df = df.reset_index()
    return fname,jianchen,df

def Hetong(end_riqi):
    fname = r'F:\a00nutstore\006\zw\price\灰板合同价格.xlsx'
    sheet_name = '合同单价'
    df = pd.read_excel(fname, sheet_name, index_col=0)
    grouped = df.groupby('供货单位')
    all_values = []
    for gys, values in grouped:
        print('gys', gys)
        print('values', values)
        last_day =end_riqi
        values.loc[last_day, '供货单位'] = gys
        values = values.resample('D').ffill()
        values.fillna(method='ffill', inplace=True)
        all_values.append(values)
    df2 = pd.concat(all_values, axis=0)
    return df2

def dfMerge(df1,df2):
    df2 = df2.reset_index()
    df8 = pd.merge(df1, df2, on=['日期', '供货单位'], how='left')  #连接！从python的传统字典到pandas的连接！量变到质变的飞跃！
    return df8

def huizhong(jianchen,fname,df8):
    df8 = df8.assign(singlePrice=df8.apply(lambda x: x[x.类别], axis=1))    #根据类别，确定sinlePrice的值,横竖交叉定位！非常实用！
    df8['合同单价'] = round(df8['单张吨数'] * df8['singlePrice'], 2)
    df8['合同金额'] = round(df8['合同单价'] * df8['入库数量'], 2)
    df8['多计'] = df8['入库单价'] - df8['合同单价']
    df8['多计金额'] = df8['入库金额'] - df8['合同金额']
    df9  = df8.iloc[:,:-5]
    grouped = df9.groupby('供货单位')
    with pd.ExcelWriter(fname)  as writer:
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
    start_riqi = pd.Timestamp(input('请输入入库起始日期期间：格式为2021-11-4：\n'))
    end_riqi = pd.Timestamp(input('请输入入库结束日期期间：格式为2021-11-4：\n'))
    fname,jianchen,df1  = Dangyue(start_riqi,end_riqi)
    print(df1)
    df2 = Hetong(end_riqi)
    df8 = dfMerge(df1, df2)
    huizhong(jianchen, fname, df8)
    os.startfile(fname)

if __name__ == '__main__':
    main()



















