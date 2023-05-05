'''
program name :shishiliushuzhang08gs.py
本模块增加专入价格更新,20200523增加easygui
'''
# _*_ coding: uft-8 _*_
import os
import excelmessage
import liushuizhang02
import liushuizhang03
import shujuquchong
import quchong
import openpyxl
import shutil
#如不想用excelmessage点选 ‘原材料实时流水账，则可在adddangtian中直接指定
import adddangtian
import daoruprice
import dataonly
import easygui
import allyueprice
from beifenFile import beifen

def liushuizhangMeitian(oldname,fname):
    beifen(oldname)
    print('请点选要添加的当天原材料流水账')

    #fname = excelmessage.excelMessage()
    dirname, filename = os.path.split(fname)
    os.chdir(dirname)


    #liushuizhang02.liushuiZhang02(fname)

    #仅取流水账中有采购事项的业务,标准的模块间参数传递
    fname = liushuizhang02.liushuiZhang02(fname)
    #期间、财务名称、价格名称、令数、吨数等
    #liushuizhang03.liushuiZhang03(fname)
    fname = liushuizhang03.liushuiZhang03(fname)
    #将上月底至当天的流水账添加到实时流水账中
    fname = adddangtian.addDangtian(oldname,fname)

    #dataonly.dataOnly(fname)
    #下面是数据去重操作
    in_subject=['日期', '单据号', '供货单位', '品名', '单位', '入库数量', '入库单价', '入库金额', 'cwName', 'priceName', '期间', '送货日期', '白云期间',
                    '令数', '吨数', '令价', '吨价']

    path,excelname = os.path.split(fname)
    os.chdir(path)
    sheetname = '流水账'
    wb = openpyxl.load_workbook(fname)
    ws = wb[sheetname]         #以前版本是ws=wb.active,导致汇总工作表被挤占
    wb.close()
    #数据去重
    # duplicated_name = shujuquchong.delchongfu(fname,excelname,sheetname,in_subject)

    # #将去重后的数据重新引入
    # pandas09.shujuqingli(duplicated_name, fname)
    quchong.delchongfu(fname,sheetname,in_subject)

    #引入价格
    #allyueprice.main()
    #daoruprice.daoruPrice(fname)

def main():
    oldname = r'd:\a00nutstore\006\zw\原材料实时流水账\原材料实时流水账.xlsx'
    print('请点选要添加的当天原材料流水账')

    fname = excelmessage.wenjian()
    fname = excelmessage.excelMessage(fname)

    liushuizhangMeitian(oldname,fname)

if __name__ == '__main__':
    main()




















