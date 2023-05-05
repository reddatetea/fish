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
    regax = r'(?:原材料)(\d{4}-\d{2})(?:出库参考)'
    pattern = re.compile(regax)
    mat = pattern.search(filename)
    if mat:
        qijian_string = mat.group(1)   #匹配上则自动输入
        chuku_name = qijian_string[-2:]
    else:
        qijian_string = input('请输入当月材料出库名字2021-11\n')  #匹配不上则手动输入
        chuku_name = qijian_string[-2:]
    yemei_title = '原材料出库明细' + qijian_string
    new_name = '原材料出库' + qijian_string + '.xlsx'
    fname1 = os.path.join(path, new_name)
    return fname1,chuku_name,yemei_title

def chukuDangyue(fname,fname1,chuku_name):
    df_cankao = pd.read_excel(fname, '出库参考 Copy')
    lst = df_cankao.columns.to_list()
    new_lst = lst[7:17] + lst[20:]
    df = df_cankao.loc[:, new_lst]
    df.insert(0, 'leibie', df['科目名称'])   #后面插入None不行！
    df.leibie = df['科目编码'].map(leibie)
    table = pd.pivot_table(df, index=['leibie', '科目编码', '科目名称'], aggfunc='sum')
    datas = []
    grouped = table.groupby('leibie')
    for k, d in grouped:
        j = d.append(d.sum().rename((k, '', '')))    #关键操作，从百度上照搬！
        datas.append(j)
    df_total = pd.concat(datas)
    out = df_total.append(table.sum().rename(('005原材料', '', '合计')))
    # out.index = pd.MultiIndex.from_tuples(out.index)
    out = out.reset_index()
    out1 = out.assign(科目编码=out.apply(lambda x: xiaoji(x), axis=1))  #axis很重要
    out2 = out1.iloc[:, 1:]
    out3 = out2.iloc[:, [0, 1, 2, 3, -1]]
    out3 = out3[out3.金额 != 0]
    out3['科目编码'] = out3['科目编码'].astype('str')    #强行转换格式
    out3.iloc[-1,0] = '原材料'
    out3 = out3.set_index('科目编码')
    for j in ['  纸  小计','  灰板  小计','  辅料  小计','  包装物  小计','原材料']:
        for i in ['出库','单价']:
            out3.at[j, i] = None    # =''不行!将出库、单价的合计数，更改为空！
    out3 = out3.reset_index()
    out3.to_excel(fname1, chuku_name, index=False)
    return fname1

def main():
    msg = '请对“出库参考 Copy"稍作变动并保存后，再点选它！'
    fname = easygui.fileopenbox(msg, title=msg)
    fname1, chuku_name, yemei_title = getChuname(fname)
    fname1 = chukuDangyue(fname,fname1,chuku_name)
    excelseting.fastseting(fname1, chuku_name, yemei_title)
    os.startfile(fname1)

if __name__ == '__main__':
    main()
