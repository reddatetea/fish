import os
import openpyxl
import easygui
import re
import pandas as pd
import excelseting


def leibie(x):                      #加类别！以便汇总！
    if x >= 1403001001 and x < 1403002001:
        lei = '001纸'                        #加001等是为了排序方便！最后去掉即可！
    elif x >= 1403002001 and x < 1403003001:
        lei = '002灰板'
    elif x >= 1403003001 and x < 1403006001:
        lei = '003辅料'
    else:
        lei = '004包装物'
    return lei


def xiaoji(x):
    if x['科目编码'] in [None, '']:
        ji = '  ' + x['leibie'][3:] + '  ' + '小计'    #加空格使之美观！不过也增加后面处理难度
    else:
        ji = x['科目编码']
    return ji

def getChuname(fname):
    path, filename = os.path.split(fname)
    os.chdir(path)
    regax = r'(?:原材料出库)(\d{4}-\d{2})'
    pattern = re.compile(regax)
    mat = pattern.search(filename)
    if mat:
        qijian_string = mat.group(1)   #匹配上则自动输入
        chuku_name = qijian_string[-2:]
    else:
        qijian_string = easygui.msgbox('请输入当月材料出库名字"2021-11"')  #匹配不上则手动输入
        chuku_name = qijian_string[-2:]
    yemei_title = '原材料出库y明细' + qijian_string
    new_name = '原材料出库y' + qijian_string + '.xlsx'
    fname1 = os.path.join(path, new_name)
    yeimei_yanfa = qijian_string + '研发材料出库明细表'
    yanfa_name = qijian_string + '研发材料出库明细表' + '.xlsx'
    fname_yanfa = os.path.join(path,yanfa_name)
    return fname1,chuku_name,yemei_title,fname_yanfa,yeimei_yanfa

def chukuDangyue(df5,fname1,chuku_name):
    df6 = df5.reset_index()
    df6 = df6.astype({'科目编码': 'int'})
    df6.insert(0, 'leibie', df6['科目名称'])  # 后面插入None不行！
    df6.leibie = df6['科目编码'].map(leibie)
    table = pd.pivot_table(df6, index=['leibie', '科目编码', '科目名称'], aggfunc='sum')
    datas = []
    grouped = table.groupby('leibie')
    for k, d in grouped:
        j = d._append(d.sum().rename((k, '', '')))  # 关键操作，从百度上照搬！
        datas.append(j)
    df_total = pd.concat(datas)
    out = df_total._append(table.sum().rename(('005原材料', '', '合计')))
    # out.index = pd.MultiIndex.from_tuples(out.index)
    out = out.reset_index()
    out = out.assign(科目编码=out.apply(lambda x: xiaoji(x), axis=1))  # axis很重要
    out = out.iloc[:, 1:]
    out = out.iloc[:, [0, 1, 2, 3, -1]]
    out = out[out.金额 != 0]
    out['科目编码'] = out['科目编码'].astype('str')  # 强行转换格式
    out.iloc[-1, 0] = '原材料'
    out = out.set_index('科目编码')
    for j in ['  纸  小计', '  灰板  小计', '  辅料  小计', '  包装物  小计', '原材料']:
        for i in ['出库', '单价']:
            out.at[j, i] = None  # =''不行!将出库、单价的合计数，更改为空！
    out = out.reset_index()
    out.to_excel(fname1, chuku_name, index=False)
    return fname1


def main():
    msg = '请点选本月出库文件"原材料出库2022-03.xlsx"！'
    fname = easygui.fileopenbox(msg, title=msg)
    fname1,chuku_name,yemei_title,fname_yanfa,yeimei_yanfa = getChuname(fname)
    df = pd.read_excel(fname)
    df1 = df.astype({'科目名称': 'object'})
    df1 = df1[df1['科目名称'].str.contains('计') == False]
    df1 = df1[df1['科目编码'].str.contains('计') == False]
    #研发明细
    choice = True
    while choice:
        titleYN = easygui.ccbox(msg, title='是否已复制研发明细', choices=('yes', 'no'), image=None)
        if titleYN == True:
            df2 = pd.read_clipboard()
            choice = False
        else:
            continue

    df2 = df2[~df2['科目名称'].str.contains('计')]
    df3 = df1.loc[:, ['科目名称', '科目编码', '单价']]
    #df2,df1合并，df2取df1的单价和科目名称
    df2_df1 = pd.merge(df2, df3, how='left', on='科目名称')
    df2_df1['出库'] = round(df2_df1['金额']/df2_df1['单价'],0)   #计算整数数量
    df2_df1['金额'] = round(df2_df1['出库'] * df2_df1['单价'], 2)  #根据整数数量，重新计算金额
    df2_df1 = df2_df1.loc[:, ['科目编码', '科目名称', '出库', '单价', '金额']]  #重新排列,研发明细
    total = sum(df2_df1['金额'])
    df_yanfa = df2_df1._append({'科目编码': '合计', '金额': total}, ignore_index=True)
    df2_df1_1 = df2_df1.set_index(['科目编码', '科目名称'])
    df2_df1_1 = df2_df1_1 * (-1)
    df2_df1_1['单价'] = 0
    df2_df1_1 = df2_df1_1.reset_index()
    df5 = pd.concat([df1,df2_df1_1])
    df5 = df5.groupby(['科目编码', '科目名称']).sum()
    fname1 = chukuDangyue(df5,fname1,chuku_name)
    excelseting.fastseting(fname1, chuku_name, yemei_title)
    os.startfile(fname1)
    df_yanfa.to_excel(fname_yanfa,chuku_name, index=False)
    excelseting.fastseting(fname_yanfa,chuku_name,yeimei_yanfa)
    os.startfile(fname_yanfa)


if __name__ == '__main__':
    main()
