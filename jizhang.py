'''
删除重复数据，但保留已记账的数据！
'''
import pandas as pd
import xlwings as xw


def quchong(fname,sheet_name=0):
    df = pd.read_excel(fname)
    df['记账'] = df['记账'].astype('datetime64[ns]')
    print(df.info())
    subset = df.columns.to_list()
    subset.remove('记账')
    print(subset)
    df_dels = df[df.duplicated(subset, keep='first')]  # 删除的记录
    print(df_dels)
    df0 = df.drop_duplicates(subset=subset, keep='first')  # 删除后保贸的记录
    print(df0)
    df8 = pd.merge(df0, df_dels, on=subset, how='left')
    print(df8)
    df9 = df8.copy()
    print(df9)
    df9['记账_x'] = df9['记账_x'].fillna('1899-1-1')
    df9['记账_y'] = df9['记账_y'].fillna('1899-1-1')
    print(df9)

    def jizhang(x):
        if x.记账_x == 0:
            ji = x.记账_y
        else:
            ji = x.记账_x
        return ji

    df10 = df9.assign(记账_x=df9.apply(lambda x: jizhang(x), axis=1))
    print(df10)

    df10 = df10.iloc[:, :-1]
    print(df10)

    df11 = df10.rename({'记账_x': '记账'}, axis=1)
    df11['记账'] = df11['记账'].replace('1899-1-1','')
    return df11



def main():
    fname = r'F:\a00nutstore\006\zw\lingpeijian\重复数据.xlsx'
    df11 = quchong(fname,sheet_name=0)
    df11.to_excel('删除未记账的重复数据.xlsx', index=False)

if __name__ == '__main__':
    main()
