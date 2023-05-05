'''
计算纸箱各供应商纸箱合同单价
'''
# _*_ conding:utf-8 _*_

import openpyxl
import os
import re
from openpyxl.utils import column_index_from_string
import zhixiangtodic

def zhixiangLeibian(pinming):
    leixiangs = ['内箱']
    # 质量好一点的纸箱
    haoxiangs = ['C7箱', 'C8箱', 'C9箱', 'F10箱', 'F11箱', 'F12箱', 'F13箱', 'F14箱', 'F15箱', 'F16箱']
    ruiyixiangs = ['锐意箱', '锐意外箱']
    xinruixiangs = ['新锐']
    # 外贸箱
    waimaoxiangs = ['外贸箱', '外贸外箱']

    zhixiangs = leixiangs + haoxiangs + ruiyixiangs + xinruixiangs + waimaoxiangs

    for zhixiang in zhixiangs:
        r = r'.*(?P<xiaolei>%s).*' % zhixiang
        pattern = re.compile(r)
        pipei = re.search(pattern, pinming)

        if pipei is not None:
            zhixiang_xiaolei = pipei.group('xiaolei')
            if zhixiang_xiaolei in leixiangs :
                zhixiang_leibie = 'leixiang'
                return zhixiang_leibie
            elif zhixiang_xiaolei in haoxiangs :
                zhixiang_leibie = 'haoxiang'
                return zhixiang_leibie
            elif zhixiang_xiaolei in xinruixiangs :
                zhixiang_leibie = 'xinruixiang'
                return zhixiang_leibie
            elif zhixiang_xiaolei in ruiyixiangs :
                zhixiang_leibie = 'ruiyixiang'
                return zhixiang_leibie
            elif zhixiang_xiaolei in waimaoxiangs :
                zhixiang_leibie = 'waimaoxiang'
                return zhixiang_leibie

            else :
                zhixiang_leibie = 'leimaoxiang'
                return zhixiang_leibie

        else:
            continue

    zhixiang_leibie = 'leimaoxiang'
    return zhixiang_leibie


def hengrong(zhixiang_leibie,chang,kuan,gao):
    dange_mianji = (chang+kuan+80)/1000*(kuan+gao+50)/1000*2
    if zhixiang_leibie == 'leixiang':
        zx_singlePrice = 2.43
    elif zhixiang_leibie == 'haoxiang':
        zx_singlePrice = 4.2
    elif zhixiang_leibie == 'ruiyixiang':
        zx_singlePrice = 4.2
    elif zhixiang_leibie == 'xinruixiang':
        zx_singlePrice = 3.78
    elif zhixiang_leibie == 'waimaoxiang':
        zx_singlePrice = 4.5
    else :
        zx_singlePrice = 3.78

    hetong_danjia = round(dange_mianji*zx_singlePrice,2)
    print(hetong_danjia)

    return dange_mianji,hetong_danjia


def jiuanyuan(zhixiang_leibie,chang,kuan,gao):
    dange_mianji = (chang+kuan+80)/1000*(kuan+gao+50)/1000*2
    if zhixiang_leibie == 'leixiang':
        zx_singlePrice = 2.16
    elif zhixiang_leibie == 'haoxiang':
        zx_singlePrice = 3.82
    elif zhixiang_leibie == 'ruiyixiang':
        zx_singlePrice = 3.82
    elif zhixiang_leibie == 'xinruixiang':
        zx_singlePrice = 3.26
    elif zhixiang_leibie == 'waimaoxiang':
        zx_singlePrice = 3.82
    else :
        zx_singlePrice = 3.42

    hetong_danjia = round(dange_mianji*zx_singlePrice,2)
    print(hetong_danjia)
    return dange_mianji, hetong_danjia

def xinlongxin(zhixiang_leibie,chang,kuan,gao):    #鑫龙鑫
    dange_mianji = (chang+kuan+80)/1000*(kuan+gao+50)/1000*2
    if zhixiang_leibie == 'leixiang':
        zx_singlePrice = 2.16
    elif zhixiang_leibie == 'haoxiang':
        zx_singlePrice = 3.82
    elif zhixiang_leibie == 'ruiyixiang':
        zx_singlePrice = 3.82
    elif zhixiang_leibie == 'xinruixiang':
        zx_singlePrice = 3.26
    elif zhixiang_leibie == 'waimaoxiang':
        zx_singlePrice = 4.9

    else :
        zx_singlePrice = 3.42

    hetong_danjia = round(dange_mianji*zx_singlePrice,2)
    print(hetong_danjia)
    return dange_mianji, hetong_danjia

def luhezi(zhixiang_leibie,chang,kuan,gao):    #绿盒子
    dange_mianji = (chang+kuan+80)/1000*(kuan+gao+50)/1000*2

    if zhixiang_leibie == 'waimaoxiang':
        zx_singlePrice = 4.32

    else :
        zx_singlePrice = 3.5

    hetong_danjia = round(dange_mianji*zx_singlePrice,2)
    print(hetong_danjia)
    return dange_mianji, hetong_danjia

def xiaoganxinrong(zhixiang_leibie,chang,kuan,gao):   #孝感鑫荣
    dange_mianji = (chang+kuan+80)/1000*(kuan+gao+50)/1000*2
    if zhixiang_leibie == 'leixiang':
        zx_singlePrice = 2.3
    elif zhixiang_leibie == 'haoxiang':
        zx_singlePrice = 4.05

    elif zhixiang_leibie == 'ruiyixiang':
        zx_singlePrice = 4.05
    elif zhixiang_leibie == 'xinruixiang':
        zx_singlePrice = 3.55
    elif zhixiang_leibie == 'waimaoxiang':
        zx_singlePrice = 4.4
    else :
        zx_singlePrice = 3.55

    hetong_danjia = round(dange_mianji*zx_singlePrice,2)
    print(hetong_danjia)
    return dange_mianji, hetong_danjia

def hubeileihe(zhixiang_leibie,chang,kuan,gao):
    dange_mianji = (chang+kuan+80)/1000*(kuan+gao+50)/1000*2
    if zhixiang_leibie == 'leixiang':
        zx_singlePrice = 2.4
    elif zhixiang_leibie == 'haoxiang':
        zx_singlePrice = 4.05
    elif zhixiang_leibie == 'ruiyixiang':
        zx_singlePrice = 4.05
    elif zhixiang_leibie == 'xinruixiang':
        zx_singlePrice = 3.45
    elif zhixiang_leibie == 'waimaoxiang':
        zx_singlePrice = 4.05
    else :
        zx_singlePrice = 3.45

    hetong_danjia = round(dange_mianji*zx_singlePrice,2)
    print(hetong_danjia)
    return dange_mianji, hetong_danjia

def priceDic():
    price_dic = {'恒龙包装': {'leixiang': 2.43,
                          'haoxiang': 4.2,
                          'ruiyixiang': 4.2,
                          'xinruixiang': 3.78,
                          'waimaoxiang': 4.5,
                          'leimaoxiang': 3.78},
                 '武汉市九安源纸业有限公司': {'leixiang': 2.16,
                                  'haoxiang': 3.82,
                                  'ruiyixiang': 3.82,
                                  'xinruixiang': 3.26,
                                  'waimaoxiang': 3.82,
                                  'leimaoxiang': 3.42},
                 '孝感鑫荣环保包装': {'leixiang': 2.3,
                              'haoxiang': 4.05,
                              'ruiyixiang': 4.05,
                              'xinruixiang': 3.55,
                              'waimaoxiang': 4.4,
                              'leimaoxiang': 3.55},
                 '湖北恒大包装': {'leixiang': 2.26,
                            'haoxiang': 3.92,
                            'ruiyixiang': 3.92,
                            'xinruixiang': 3.42,
                            'waimaoxiang': 4.34,
                            'leimaoxiang': 3.42},
                 '武汉绿盒子实业': {'leixiang': 2.3,
                             'haoxiang': 3.5,
                             'ruiyixiang': 3.5,
                             'xinruixiang': 3.5,
                             'waimaoxiang': 4.32,
                             'leimaoxiang': 3.5},
                 '鑫龙鑫': {'leixiang': 2.16,
                         'haoxiang': 3.82,
                         'ruiyixiang': 3.82,
                         'xinruixiang': 3.26,
                         'waimaoxiang': 4.9,
                         'leimaoxiang': 3.42},
                 "湖北雷合实业": {'leixiang': 2.4,
                            'haoxiang': 4.05,
                            'ruiyixiang': 4.05,
                            'xinruixiang': 3.45,
                            'waimaoxiang': 4.05,
                            'leimaoxiang': 3.45},
                 '湖北梓熠纸制器有限公司': {'leixiang': 2.3,
                                 'haoxiang': 4.05,
                                 'ruiyixiang': 4.05,
                                 'xinruixiang': 3.55,
                                 'waimaoxiang': 4.4,
                                 'leimaoxiang': 3.55}
                 }
    return price_dic


def hubeihangda(zhixiang_leibie,chang,kuan,gao):
    dange_mianji = (chang+kuan+80)/1000*(kuan+gao+50)/1000*2
    if zhixiang_leibie == 'leixiang':
        zx_singlePrice = 2.26
    elif zhixiang_leibie == 'haoxiang':
        zx_singlePrice = 3.92
    elif zhixiang_leibie == 'ruiyixiang':
        zx_singlePrice = 3.92
    elif zhixiang_leibie == 'xinruixiang':
        zx_singlePrice = 3.42
    elif zhixiang_leibie == 'waimaoxiang':
        zx_singlePrice = 4.34
    else :
        zx_singlePrice = 3.42

    hetong_danjia = round(dange_mianji*zx_singlePrice,2)
    print(hetong_danjia)
    return dange_mianji, hetong_danjia


def main():

    pinming = 'F10箱'
    zhixiang_dic = zhixiangtodic.zhixiangdic()
    chang = zhixiang_dic[pinming][0]
    kuan = zhixiang_dic[pinming][1]
    gao = zhixiang_dic[pinming][2]
    print(chang,kuan,gao)
    zhixiang_leibie = zhixiangLeibian(pinming)
    print(zhixiang_leibie)
    #hengrong(zhixiang_leibie, chang, kuan, gao)
    #jiuanyuan(zhixiang_leibie, chang, kuan, gao)
    xiaoganxinrong(zhixiang_leibie, chang, kuan, gao)



if __name__ == '__main__' :
    main()










