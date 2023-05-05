'''
删除重复数据，但保留已记账的数据！
'''
import pandas as pd
import xlwings as xw


def quchong(df,subset,keep_way = 'first'):

    # subset = df.columns.to_list()
    # print(subset)
    # subset.remove('记账')
    df_dels = df[df.duplicated(subset, keep=keep_way )]  # 删除的记录
    df0 = df.drop_duplicates(subset=subset,keep = keep_way)  # 删除后保贸的记录
    df8 = pd.merge(df0, df_dels, on=subset, how='left')
    df9 = df8.copy()
    df9['记账_x'] = df9['记账_x'].fillna('1899-1-1')
    df9['记账_y'] = df9['记账_y'].fillna('1899-1-1')

    def jizhang(x):
        if x.记账_x == 0:
            ji = x.记账_y
        else:
            ji = x.记账_x
        return ji

    df10 = df9.assign(记账_x=df9.apply(lambda x: jizhang(x), axis=1))
    df10 = df10.iloc[:, :-1]
    df11 = df10.rename({'记账_x': '记账'}, axis=1)
    df11['记账'] = df11['记账'].replace('1899-1-1','')
    return df11

def dataToExcel(df,fname,sheet_name=0,index_col=['日期','单据号', '供货单位']):
    app = xw.App(visible=False, add_book=False)
    wb = app.books.open(fname)
    ws = wb.sheets['%s' % sheet_name]
    col_names = df.columns.to_list()
    df = df.set_index(index_col)
    df = df.sort_values(by=index_col)
    df = df.reset_index()  # 取消索引
    df = df[col_names]  # 按原来列顺序
    ws.clear()
    ws.range('A1').options(pd.DataFrame, index=False).value = df
    wb.save()
    wb.close()
    app.quit()

def main():
    fname = r'F:\a00nutstore\006\zw\lingpeijian\重复数据.xlsx'
    sheet_name = '无法去重的数据行'
    df = pd.read_excel(fname,sheet_name)
    df['记账'] = df['记账'].astype('datetime64[ns]')
    subset = ['入库单号', '入库日期', '相关单位', '单据附注', '货品编码', '货品名称', '规格', '所属类别', '单位', '入库数量', '单价', '金额', '备注',  '期间', '标准日期']
    df11 = quchong(df,subset,keep_way='last')
    dataToExcel(df11, fname, sheet_name, index_col=['入库日期', '入库单号', '相关单位'])


if __name__ == '__main__':
    main()
