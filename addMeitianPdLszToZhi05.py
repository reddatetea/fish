'''
每天将D:\ribaobiao下的流水账和零配件入库统计或退货统计分别写入原材料实时流水账和零配件实时流水账，
去除重复数据，再从原材料流水账中，
将上月26日至昨天的白云纸张入库和其它供应商的纸张入库
分别写入白云入库和2020入库！
后者按期间、供应商、时间、单号、品名排序！
命令行快捷按键是:meitian
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
from datetime import datetime, date, timedelta
import addbaiyunRukuPd
from addbaiyunRukuPd import liushuizhang
from addbaiyunRukuPd import chuli
from addbaiyunRukuPd import liushuizhang
from addbaiyunRukuPd import  qushu
from addbaiyunRukuPd import  jiagongsi
from addbaiyunRukuPd import  delchongfu
import addzhiRukuPd
from easygui import buttonbox
import zhiNewGongyingshang
import easygui

def yuancailiaoLiushuizhang(files):
    datas = []
    for filename in files:
        data = pd.read_excel(filename,dtype = {'单据号':str})
        data = data[['日期', '单据号', '供货单位', '存货名称', '计量单位',  '入库数量','入库单价', '入库金额']]
        # data = data.rename(columns={'存货名称': '品名', '计量单位': '单价'})
        data.dropna(subset=['供货单位'], inplace=True)  # 删除供货单位列中的有空值的行
        datas.append(data)

    ysl = pd.concat(datas)  # 多个原材料流水账账汇总

    ysl.rename({'存货名称':'品名','计量单位':'单位'},axis=1,inplace=True)   #042新账套引出的流水账，列名有变，需调整
    # a = ysl.pop('入库数量')  # 移动列
    # ysl.insert(5, '入库数量', a)
    # print(ysl)

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
    qijian = str(y)+'-'+str(m).zfill(2)
    return qijian

def lingpeijianLiushuizhang(files):
    datas = []
    for filename in files:
        data = pd.read_excel(filename)

        if data.columns[0]=='退货单号':
            data.rename(columns={'退货单号':'入库单号','退货日期': '入库日期','退货数量':'入库数量'},inplace=True)
            data['入库数量'] = data['入库数量'] * -1
            data['金额'] = data['金额'] * -1
        else :
            pass
        data.dropna(subset=['入库单号'], inplace=True)  # 删除入库单号列中的有空值的行

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
    olddata = pd.DataFrame(pd.read_excel(fname, sheetname,dtype = {'单据号':str}))
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


def startriqiEndriqi(today):
    yesterday = today + timedelta(days=-1)  # 昨天日期
    year = yesterday.year
    month = yesterday.month
    day = yesterday.day
    if day <= 25 and month == 1:
        last_year = year - 1
        last_month = 12
        last_day = 26
    elif day <= 25 and month != 1:
        last_year = year
        last_month = month - 1
        last_day = 26
    else:
        last_year = year
        last_month = month
        last_day = 26
    start_riqi = str(last_year) + '-' + str(last_month) + '-' + str(last_day)
    end_riqi = str(year) + '-' + str(month) + '-' + str(day)
    start_riqi = pd.Timestamp(start_riqi)
    end_riqi = pd.Timestamp(end_riqi)
    return start_riqi, end_riqi

def lszTobaiyun(start_riqi, end_riqi,piaojuhao):
    df = liushuizhang()  # 流水账df
    df1 = qushu(df, start_riqi, end_riqi, piaojuhao)
    fname_ruku = chuli(df1)
    df = pd.read_excel(fname_ruku, '2020',dtype = {'单号':str})
    in_subject = ['开票日期', '入库单号', '品名', '数量(令)', '计算重量', '仓库材料']
    sort_cols = ['开票日期', '入库单号', '品名']
    # sort_cols = ['入库单号', '品名']
    delchongfu(fname_ruku, '2020', in_subject,sort_cols)
    jiagongsi(fname_ruku)

def lszTozhi(start_riqi, end_riqi,piaojuhao):
    df = addzhiRukuPd.liushuizhang()  # 流水账df
    jianchen = zhiNewGongyingshang.zhiGongyingshang()
    df1 = addzhiRukuPd.qushu(df, start_riqi, end_riqi, piaojuhao,jianchen)
    fname_ruku = addzhiRukuPd.chuli(df1)
    df = pd.read_excel(fname_ruku, '入库',dtype = {'单号':str})
    in_subject = ['单位', '供应商', '时间', '单号', '材料', '入库', '入库（kg）']
    sort_cols = ['期间','供应商','时间', '单号','材料']
    addzhiRukuPd.delchongfu(fname_ruku, '入库', in_subject,sort_cols)
    addzhiRukuPd.jiagongsi(fname_ruku)

def addmeitianLiushuizhang():
    desktopPath = r'D:\ribaobiao'
    os.chdir(desktopPath)
    filenames = os.listdir(desktopPath)
    lsz_files = [i for i in filenames if fnmatch(i, '*流水*.xls*')]
    lpj_files = [i for i in filenames if fnmatch(i, '*统计*.xls*')]
    # 原材料
    try:
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
    except:
        pass

    # 零配件
    try:
        if len(lpj_files) >= 1:
            lpj_subject = ['入库单号', '入库日期', '相关单位', '单据附注', '货品编码', '货品名称', '规格', '所属类别', '单位', '入库数量', '单价', '金额', '备注',
                           '期间', '标准日期']
            lpj = lingpeijianLiushuizhang(lpj_files)
            lpj_fname = r'F:\a00nutstore\006\zw\lingpeijian\零配件实时入库2020.xlsx'
            beifen(lpj_fname)
            index_col = ['入库日期', '入库单号', '相关单位']
            concatAndQuchong(lpj_fname, 'ssrk', lpj, lpj_subject, index_col)
            quchong.delchongfu(lpj_fname, 'ssrk', lpj_subject,
                               index_col=['入库日期', '入库单号', '相关单位'])  # 零配件两次去重才行，不知原因20211207
        else:
            pass
    except:
        pass

def tozhi(start_riqi, end_riqi, piaojuhao):
    lszTozhi(start_riqi, end_riqi, piaojuhao)

def tobaiyun(start_riqi, end_riqi, piaojuhao):
    lszTobaiyun(start_riqi, end_riqi, piaojuhao)

def main():
    addmeitianLiushuizhang()

    piaojuhao = 0
    msg = '请选择日期输入的方式：'
    print(msg)
    choice = buttonbox(msg, choices=['自动', '手动','singleZhi','singleBaiyun'])
    if choice == '自动':
        today = date.today()
        start_riqi, end_riqi = startriqiEndriqi(today)
        try :
            tobaiyun(start_riqi, end_riqi, piaojuhao)
        except:
            print('本月没有白云入库')
        try :
            tozhi(start_riqi, end_riqi, piaojuhao)
        except:
            print('本月没有纸入库')

    elif choice == '手动':
        today = pd.Timestamp(easygui.enterbox('请输入要查询期间的后一天"2021-12-27"\n'))
        start_riqi, end_riqi = startriqiEndriqi(today)
        try :
            tobaiyun(start_riqi, end_riqi, piaojuhao)
        except:
            print('本月没有白云入库')
        try :
            tozhi(start_riqi, end_riqi, piaojuhao)
        except:
            print('本月没有纸入库')
    elif choice == 'singleZhi':
        try :
            addzhiRukuPd.main()
        except:
            print('本月没有纸入库')
    else :
        try:
            addbaiyunRukuPd.main()
        except:
            print('本月没有白云入库')


    easygui.msgbox('程序结束')




if __name__ == '__main__':
    main()







