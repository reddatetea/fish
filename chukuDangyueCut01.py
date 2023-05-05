'''
在chukuDangyuePd的基础上，使用分箱的方法生成材料大类
'''
import os
import openpyxl
import easygui
import re
import pandas as pd
import excelseting
import numpy as np

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
    lei = ['纸', '灰板', '辅料', '包装物']
    fenlei = pd.cut(df.科目编码, bins=[0, 1403002001, 1403003001, 1403006001, 1403007001], labels=lei)
    df = df.assign(leibie=fenlei)
    table = pd.pivot_table(df, index=['leibie', '科目编码', '科目名称'], aggfunc='sum')
    # df2 = df1.set_index(['lei', '科目编码', '科目名称'])   #不分类汇总，索引也可以
    datas = []
    gp = table.groupby('leibie')
    for k, d in gp:
        j = d.append(d.sum().rename(("","  " + k + "  " + '小计',"")))
        datas.append(j)
    df_total = pd.concat(datas)
    out = df_total.append(table.sum().rename(('005原材料', '', '合计')))
    # out.index = pd.MultiIndex.from_tuples(out.index)
    out = out.reset_index()
    # out1 = out.assign(科目编码=out.apply(lambda x: xiaoji(x), axis=1))  #axis很重要
    out2 = out.iloc[:, 1:]
    out3 = out2.iloc[:, [0, 1, 2, 3, -1]]
    out3 = out3[out3.金额 != 0]
    out3['科目编码'] = out3['科目编码'].astype('str')    #强行转换格式
    out3.iloc[-1,0] = '原材料'
    out3 = out3.set_index('科目编码')
    out3.出库 = np.where(out3.index.str.contains('计|原材料'), None, out3.出库)
    out3.单价 = np.where(out3.index.str.contains('计|原材料'), None, out3.单价)
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
