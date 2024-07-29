'''
处理Tcloud中的进货单、销货单等
'''

import pandas as pd
import numpy as ny
import re
import os
import easygui
import glob
import openpyxl


def danjuChuli(df):
    df = df.dropna(how='all', axis=0)
    cols = [i for i in df.columns.to_list() if 'Unnamed' not in i]
    df = df[cols]
    # get maxrows
    for label, ser in df.items():
        for num, x in enumerate(ser):
            if isinstance(x, str):
                if '合计' in x:
                    index = num
                    print(index)
                    break
    df = df.iloc[:index]
    df = df.dropna(how='all', axis=1)
    return df


def main():
    fname = r"F:\a00nutstore\008\zw08\用友报价\单据格式\莱新销货单SaleDelivery.xlsx"
    df = pd.read_excel(fname, skiprows=7)  # 销售单 skiprows = 7
    df = danjuChuli(df)
    df1 = pd.read_excel(fname, skiprows=4)  # 进货单 skiprows = 4
    df1 = danjuChuli(df1)

if __name__ == '__main__':
    main()



