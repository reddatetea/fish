'''
将每天的原材料流水账和零配件流水账账加到流水账大库中，并去重
'''
# _*_ coding:utf-8 _*_
import os
import numpy as np
import pandas as pd
from singleCailiaoRename import singlecailiaoName
from qijianchuli import qijian
from baiyunqijian import  baiyunQijian
from fnmatch import fnmatch
import xlwings as xw
from beifenFile import beifen
import datetime
import quchong


def yuancailiaoLiushuizhang(files):
    datas = []
    for filename in files:
        data = pd.read_excel(filename)
        data = data[['日期', '单据号', '供货单位', '存货名称', '计量单位', '入库单价', '入库金额', '入库数量']]
        data = data.rename(columns={'存货名称': '品名', '计量单位': '单价'})
        data.dropna(subset=['供货单位'], inplace=True)  # 删除供货单位列中的有空值的行
        datas.append(data)

    ysl = pd.concat(datas)  # 多个原材料流水账账汇总
    a = ysl.pop('入库数量')  # 移动列
    ysl.insert(5, '入库数量', a)

    for j in ['cwName', 'priceName', '期间', '送货日期', '白云期间', '令数', '吨数', '令价', '吨价', '吨价0', '记账']:
        ysl[j] = None
    ysl = ysl.assign(cwName=ysl['品名'].map(lambda x: singlecailiaoName(x)[0]))
    ysl = ysl.assign(priceName=ysl['品名'].map(lambda x: singlecailiaoName(x)[1]))
    ysl = ysl.assign(期间=ysl['日期'].map(lambda x: qijian(x)))
    ysl = ysl.assign(白云期间=ysl['日期'].map(lambda x: baiyunQijian(x)[0]))
    ysl = ysl.assign(送货日期=ysl['日期'].map(lambda x: baiyunQijian(x)[1]))
    ysl = ysl.assign(令数=ysl.apply(lambda x: lingDun(x)[0], axis=1))
    ysl = ysl.assign(吨数=ysl.apply(lambda x: lingDun(x)[1], axis=1))
    ysl = ysl.assign(令价=ysl.apply(lambda x: lingDun(x)[2], axis=1))
    ysl = ysl.assign(吨价=ysl.apply(lambda x: lingDun(x)[3], axis=1))
    ysl['日期'] = ysl['日期'].astype('datetime64[ns]')
    ysl['送货日期'] = ysl['送货日期'].astype('datetime64[ns]')
    ysl['单据号'] = ysl['单据号'].astype('int64')
    ysl = ysl.assign(cwName=np.where((ysl.cwName == '线圈') & (ysl['单位'] == '卷'), '线圈（卷）', ysl.cwName))
    ysl = ysl.assign(priceName=np.where((ysl.priceName == '线圈') & (ysl['单位'] == '卷'), '线圈（卷）', ysl.priceName))
    ysl = ysl.assign(cwName=np.where((ysl.cwName == '线圈') & (ysl['单位'] == '公斤'), '线圈（公斤）', ysl.cwName))
    ysl = ysl.assign(priceName=np.where((ysl.priceName == '线圈') & (ysl['单位'] == '公斤'), '线圈（公斤）', ysl.priceName))

    return ysl

def qijianJisuan(string):
    y = int(string.split('-')[0])
    m = int(string.split('-')[1])
    d = int(string.split('-')[2])
    if d > 25 and m < 12:
        m = m + 1
    elif d > 25 and m == 12 :
        m = 1
        y = y + 1
    else :
        pass
    qijian = str(y)+'-'+str(m)
    return qijian

def lingpeijianLiushuizhang(files):
    datas = []
    for filename in files:
        data = pd.read_excel(filename)
        data.dropna(subset=['入库单号'], inplace=True)  # 删除入库单号列中的有空值的行
        if data.columns[0]=='退货单号':
            data.rename(columns={'退货单号':'入库单号','退货日期': '入库日期','退货数量':'入库数量'},inplace=True)
            data['入库数量'] = data['入库数量'] * -1
            data['金额'] = data['金额'] * -1
        else :
            pass

        datas.append(data)
    lpj = pd.concat(datas)
    for j in ['期间','标准日期']:
        lpj[j] = lpj['入库日期']
    lpj['标准日期'] = lpj['标准日期'].astype('datetime64[ns]')
    lpj = lpj.assign(期间=lpj['入库日期'].map(lambda x: qijianJisuan(x)))
    lpj['入库日期'] = lpj['入库日期'].astype('datetime64[ns]')
    return lpj

def concatAndQuchong(fname,sheetname,newdata,in_subject,index_col=['日期','单据号', '供货单位'] ):
    app = xw.App(visible=False, add_book=False)
    wb = app.books.open(fname)
    ws = wb.sheets[sheetname]
    olddata = pd.DataFrame(pd.read_excel(fname, sheetname))
    data = pd.concat([olddata, newdata])
    col_names = data.columns.to_list()
    data.drop_duplicates(subset=in_subject, keep='first', inplace=True)
    data = data.set_index(index_col)                   #按日期索引
    data = data.sort_values(by=index_col)
    data = data.reset_index()                               #取消索引
    data = data[col_names]                               #按原来列顺序
    # first_col = data.columns[0]                   #取第一列
    # data = data.set_index(first_col)      #按首列索引
    ws.clear()
    ws.range('A1').options(pd.DataFrame, index=False).value = data
    wb.save()
    wb.close()
    app.quit()
    return fname

def lingDun(x):
    ling = 0
    lingjia = 0
    dunshu = 0
    dunjia = 0
    if x['单位']=='kg' or x['单位']=='公斤':
        dunshu = x['入库数量']/1000
        dunjia = x['入库单价']*1000
    elif x['单位']=='令':
        ling = x['入库数量']
        lingjia = round(x['入库单价'],2)
        ke = float(singlecailiaoName(x['品名'])[2])
        chang = float(singlecailiaoName(x['品名'])[3])
        kuan = float(singlecailiaoName(x['品名'])[4])
        dunshu = round(ke/1000/1000*chang/1000*kuan/1000*500*x['入库数量'],3)
        try :
            dunjia = round(x['入库金额']/dunshu,0)
        except:
            dunjia = 0
    else :
        pass
    return ling,dunshu,lingjia,dunjia

def main():
    desktopPath = r'D:\ribaobiao'
    os.chdir(desktopPath)
    filenames = os.listdir(desktopPath)
    lsz_files = [i for i in filenames if  fnmatch(i,'*流水*.xls*')]
    lpj_files = [i for i in filenames if fnmatch(i, '*统计*.xls*')]
    #原材料
    try :
        if len(lsz_files) >= 1:
            ysl_subject = ['日期', '单据号', '供货单位', '品名', '单位', '入库数量', '入库单价', '入库金额', 'cwName', 'priceName', '期间', '送货日期',
                           '白云期间', '令数', '吨数', '令价', '吨价']
            ysl = yuancailiaoLiushuizhang(lsz_files)

            ysl_fname = r'F:\a00nutstore\006\zw\原材料实时流水账\原材料实时流水账.xlsx'
            beifen(ysl_fname)
            concatAndQuchong(ysl_fname, '流水账', ysl, ysl_subject)
            # quchong.delchongfu(ysl_fname,  '流水账',ysl_subject)   #20211217两次去重才行
        else:
            pass
    except :
        pass

    #零配件
    try :
        if len(lpj_files) >= 1:
            lpj_subject = ['入库单号', '入库日期', '相关单位', '单据附注', '货品编码', '货品名称', '规格', '所属类别', '单位', '入库数量', '单价', '金额', '备注', '期间', '标准日期']
            lpj = lingpeijianLiushuizhang(lpj_files)
            lpj_fname = r'F:\a00nutstore\006\zw\lingpeijian\零配件实时入库2020.xlsx'
            beifen(lpj_fname)
            index_col = ['入库日期','入库单号', '相关单位']
            concatAndQuchong(lpj_fname, 'ssrk', lpj, lpj_subject,index_col)
            quchong.delchongfu(lpj_fname, 'ssrk', lpj_subject,index_col = ['入库日期','入库单号', '相关单位'])  # 零配件两次去重才行，不知原因20211207
        else:
            pass
    except :
        pass

if __name__ == '__main__':
    main()







