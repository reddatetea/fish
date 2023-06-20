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
import xlsxlsx
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
import datetime


def xlsToXlsx(fname):
    if os.path.splitext(fname)[-1].lower()=='.xls':
        newname = xlsxlsx.xlsXlsx(fname)
    else:
        newname = fname
    return newname

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
        xlsxname = xlsToXlsx(filename)
        data = pd.read_excel(xlsxname)

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
    olddata = pd.read_excel(fname, sheetname,dtype = {'单据号':str})
    data = pd.concat([olddata, newdata])
    col_names = data.columns.to_list()
    data.drop_duplicates(subset=in_subject, keep='first', inplace=True)
    data = data.set_index(index_col)                   #按日期索引
    data = data.sort_values(by=index_col)
    data = data.reset_index()                               #取消索引
    data = data[col_names]                               #按原来列顺序
    # first_col = data.columns[0]                   #取第一列
    # data = data.set_index(first_col)      #按首列索引

    # df_temp = data.applymap(lambda x: str(x) if isinstance(x, datetime.time) else x)
    # ws.range('A1').options(pd.DataFrame, index=False).value = df_temp
    df_temp = data.applymap(lambda x: str(x) if pd.api.types.is_datetime64_dtype else x)   #可行
    data1 = data.astype(data.dtypes.replace({'datetime64[ns]': str}))    #可行

    app = xw.App(visible=False, add_book=False)
    wb = app.books.open(fname)
    ws = wb.sheets[sheetname]
    ws.clear_contents()
    wb.save()
    wb.close()
    app.quit()
    with pd.ExcelWriter(fname, engine='openpyxl', datetime_format='yyyy-m-d', mode='a',
                        if_sheet_exists='overlay') as writer:
        data1.to_excel(writer, sheetname, index=False)

    return fname


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



def addmeitianLiushuizhang():
    desktopPath = r'D:\ribaobiao'
    os.chdir(desktopPath)
    filenames = os.listdir(desktopPath)
    lsz_files = [os.path.join(desktopPath,i) for i in filenames if fnmatch(i, '*流水*.xls*')]
    lpj_files = [os.path.join(desktopPath,i) for i in filenames if fnmatch(i, '*统计*.xls*')]

    # 零配件

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


def main():
    addmeitianLiushuizhang()







if __name__ == '__main__':
    main()







