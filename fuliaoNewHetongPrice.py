import os
import pandas as pd
import excelfastsetings
import chinesetopinyin

def lastprice():
    fname = r'F:\a00nutstore\006\zw\price\辅料合同价格.xlsx'
    path, filename = os.path.split(fname)
    os.chdir(path)
    fname2 = os.path.join(path, '辅料最新合同价格.xlsx')
    ws_name = '辅料最新价格'
    df = pd.read_excel(fname)
    gys_pinmings = list(zip(df['供货单位'].tolist(), df['品名'].tolist()))
    dw_htdj_bzs = list(zip(df['单位'].tolist(), df['合同单价'].tolist(), df['备注'].tolist()))
    price_dic = dict(zip(gys_pinmings, dw_htdj_bzs))
    data = []
    for gys_pinming, dw_htdj_bzs in price_dic.items():
        data.append([gys_pinming[0], gys_pinming[1], dw_htdj_bzs[0], dw_htdj_bzs[1], dw_htdj_bzs[2]])
        print(gys_pinming, dw_htdj_bzs)
    data.sort(key=lambda x: chinesetopinyin.getpinyin(x[1]))  # 先进行优先级较低的排序，对品名进行排序
    data.sort(key=lambda x: chinesetopinyin.getpinyin(x[0]))  # 先进行优先级较高的排序，中文排序供应商

    df0 = pd.DataFrame(data, columns=['供应单位', '品名', '单位', '合同单价', '备注'])
    df0.to_excel(fname2, ws_name, index=False)
    excelfastsetings.fastseting(fname2, ws_name)
    os.startfile(fname2)

def main():
    lastprice()


if __name__ == '__main__':
    main()



