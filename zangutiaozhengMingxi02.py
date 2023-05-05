#纸张和白云及其它辅料暂估调整,复制原来的透视表和调整后的透视表的整个区域,然后运行此程序,从品名开始复制!调整后的透视表包括供应商!程序运行过程中会将供应商作为分界,分成两个DF进行处理!透视表里不能有千分符和-（0）
import pandas as pd
import xlwings as xw
import excelseting
import addshuziqianfenfu
import excelprint
import os


def getShuju():
    #dfe = pd.read_clipboard(sep='\\s+',error_bad_lines = False)
    dfe = pd.read_clipboard(sep='\\s+')
    dfe = dfe.apply(lambda x: x.str.strip())  #去除空格
    dfe.columns = [i.strip() for i in dfe.columns]   #列名去除空格
    dfe.set_index('品名', inplace=True)
    dfe = dfe.loc[~dfe.index.isnull()]  # 删除索引为空的记录
    # dfe.drop(labels=['品名','值','期间','记账','总计'], inplace=True, axis=0)
    dfe = dfe[~dfe.index.isin(['品名','值','期间','记账','"白云','期间"'])]
    dfe = dfe.apply(lambda x: x.str.replace(',', ''))
    fen = dfe.loc[dfe.isnull().sum(1) > 1].index
    gys = list(fen)[0]
    dfe = dfe.replace('-', '0.00')
    # cols = dfe.columns.to_list()
    # for j in cols:
    #     dfe[j] = dfe[j].str.replace(',', '')

    gongyingshang = dfe.at[fen[0], dfe.columns[0]]
    df1 = dfe.loc[:gys, :]
    df1 = df1.drop(gys, axis=0)
    df1 = df1.astype('float64')
    df11 = df1 * (-1)
    df2 = dfe.loc[gys:, :]
    df22 = df2.drop(gys, axis=0)
    df22 = df22.fillna(0)
    df22 = df22.astype('float64')
    df1_df2 = pd.concat([df11, df22])
    order = df1_df2.columns
    filter_str = '返利|价差|折扣|冲减|多计'
    youzekou = df22.index.str.contains(filter_str)
    pivot = pd.pivot_table(df1_df2, index='品名', values=order,
                           aggfunc='sum')
    pivot = pivot[order]
    return pivot,gongyingshang,youzekou,df11,df22

def zangutiaozheng(pivot,fname,ws_name):
    app = xw.App(visible=False, add_book=False)
    wb = app.books.open(fname)
    ws = wb.sheets[ws_name]
    ws.clear()
    ws.range('A1').value = pivot
    ws.autofit()
    wb.save(fname)
    wb.close()
    app.quit()
    return fname,ws_name

def  zekoufenpei(youzekou,df11,df22):
    df3 = df22[youzekou][df22.columns[-2:]]
    zekou_jiner = df3[df3.columns[-2]].sum()   #折扣金额合计
    buhansui = df3[df3.columns[-1]].sum()
    df4 = df22.drop(df22[youzekou].index)  # 删除折扣\价差行
    zhongdushu = df4.at['总计', df4.columns[-3]]   #总吨数
    df4[df4.columns[-2]]=round(df4[df4.columns[-3]]/zhongdushu*zekou_jiner,2)
    df4[df4.columns[-1]] = round(df4[df4.columns[-3]] / zhongdushu * buhansui,2)
    df4.at['总计', df4.columns[-2]] = zekou_jiner   #最后一行写入折扣金额
    df4.at['总计', df4.columns[-1]] = buhansui
    yun_jiner = df4.iloc[-2,-2]
    yun_buhansui = df4.iloc[-2,-1]
    df4.iloc[-2,-2] = 2*zekou_jiner-df4[df4.columns[-2]].sum()+yun_jiner    #倒数第二行金额微调
    df4.iloc[-2,-1] = 2 * buhansui - df4[df4.columns[-1]].sum() + yun_buhansui
    return df4

def main():
    path = r'F:\a00nutstore\fishc'
    os.chdir(path)
    filename = r'纸暂估调整.xlsx'
    fname = os.path.join(path,filename)
    ws_name = r'暂估调整'
    #getShuju()
    pivot, gongyingshang, youzekou, df11, df22 = getShuju()
    #print(pivot, gongyingshang, youzekou, df11, df22)
    print(df22)
    fname, ws_name = zangutiaozheng(pivot,fname,ws_name)
    title = '暂估调整--{}'.format(gongyingshang)
    addshuziqianfenfu.addShuziStyle(fname, ws_name, min_row=2, min_col=2)
    excelseting.fastseting(fname, ws_name, title)
    # excelprint.wsPrint(fname, gongyingshang)
    if youzekou.any() == True:
        df4 = zekoufenpei(youzekou,df11,df22)
        ws_name1 = '折扣分配'
        zangutiaozheng(df4,fname,ws_name1)
        addshuziqianfenfu.addShuziStyle(fname,ws_name1, min_row=2, min_col=2)
        title = '折扣分配--{}'.format(gongyingshang)
        excelseting.fastseting(fname,ws_name1,title)
        # excelprint.wsPrint(fname, gongyingshang)
    else:
        pass
    os.startfile(fname)

if __name__== '__main__':
    main()








