'''
按原材料流水账，计算指定查询开始日期之前的最近价格
'''
import os
import pandas as pd


def lastprice(start_riqi,end_riqi,gys_jianchen):
    fname = r'F:\a00nutstore\006\zw\原材料实时流水账\原材料实时流水账.xlsx'
    df = pd.read_excel(fname,'流水账',index_col=0)
    df.sort_index(inplace=True)  # 对索引排序
    df = df.truncate(before=start_riqi, after=end_riqi)
    df = df[df['供货单位'].str.contains(gys_jianchen)]
    gys_pinmings_danwei = list(zip(df['供货单位'].tolist(), df['品名'].tolist(),df['单位'].tolist()))
    prices = df['入库单价'].tolist()
    dic = dict(zip(gys_pinmings_danwei,prices))
    return dic

def main():
    start_riqi = '2021-10-26'
    end_riqi = '2021-11-9'
    gys_jianchen = '长利'
    dic = lastprice('2021-1-1', start_riqi, gys_jianchen)
    print(dic)


if __name__ == '__main__':
    main()



