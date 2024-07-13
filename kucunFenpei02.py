'''
根据原材料库盘存表和流水账，统计出库存商品分别是从哪些供应商采购回的，以及采购数量、金额
2024-4-5加一列'计量单位’
'''
import pandas as pd
import numpy as np
import easygui
import os


def getKucun(caigous,pinmings,early_riqi):
    datas = []
    fname1 = r"F:\a00nutstore\006\zw\2024\202401\2024-1盘存表002.xlsx"
    kucun = pd.read_excel(fname1,'UFPrn20240127154825' ,usecols=[0, 1,2, 6])
    kucun_cailiao = kucun[kucun['期末结存数量']!=0]
    kucun_cailiao = kucun_cailiao.dropna(subset=['品名'])
    # kucun_cailiao = kucun_cailiao.dropna(subset=['计量单位'])
    cailiaos = kucun_cailiao['品名'].to_list()
    for cailiao in cailiaos:
        kucun = kucun_cailiao[kucun_cailiao['品名']==cailiao]
        kucun_shuliang = kucun.iloc[-1][-1]  # 提取库存数
        caigou = getCaigou(caigous,pinmings,cailiao,kucun_shuliang)
        df11 = lianjie(kucun,kucun_shuliang,caigou,early_riqi)
        datas.append(df11)
    return datas


def caigouLiushuizhang():
    fname = r'F:\a00nutstore\006\zw\原材料实时流水账\原材料实时流水账.xlsx'
    caigous = pd.read_excel(fname, '流水账',usecols=[0, 1, 2, 3, 5, 6, 7, 8, 9], index_col=0,dtype = {'单据号':str})
    caigous = caigous.sort_index(ascending=False)
    early_riqi = caigous.index.to_list()[-1]
    caigous = caigous.reset_index()
    pinmings = list(caigous['品名'].unique())
    return caigous,pinmings,early_riqi

def getCaigou(caigous,pinmings,cailiao,kucun_shuliang):
    if cailiao in pinmings:
        caigou = caigous[caigous['品名'] == cailiao]
    else:
        caigou = caigous.iloc[-1:]
        caigou.iloc[-1, 2] = '待查'
        caigou.iloc[-1, 3] = cailiao
        caigou.iloc[-1, -5] = kucun_shuliang
        caigou.iloc[-1, -4] = 0
        caigou.iloc[-1, -3] = 0
        caigou.iloc[-1, -2] = None
        caigou.iloc[-1, -1] = None
    return caigou

def lianjie(kucun,kucun_shuliang,caigou,early_riqi):
    df8 = pd.merge(kucun, caigou, on='品名', how='left')
    df9 = df8
    df9['累加数量'] = df9['入库数量'].cumsum()  # 累加求和
    df9['剩余数量'] = df9['期末结存数量'] - df9['累加数量']  # 累加求和
    leiji_ruku = df9['入库数量'].sum()          #对应于期末结存数量的累计入库数量
    shuliangs = df9['剩余数量'].to_list()

    if leiji_ruku >= kucun_shuliang:
        shuliangs = df9['剩余数量'].to_list()
        for j in range(len(shuliangs)):
            if shuliangs[j] < 0:
                row = j
                break
            else:
                row = len(shuliangs)
                continue
        row = row +1
        df10 = df9.iloc[:row,:]
        df11 = df10
        shengyu = df11.iloc[-1, -1]
        danjia = df11.iloc[-1, -6]
        last_ruku = df11.iloc[-1, -7]
        leiji = df11.iloc[-1, -2]
        df11.iloc[-1, -7] = last_ruku + shengyu
        df11.iloc[-1, -5] = round((last_ruku + shengyu) * danjia, 2)  # 调整金额，按调整后的数量和单价计算
        df11.iloc[-1, -2] = leiji + shengyu
        df11.iloc[-1, -1] = 0
    else:
        df11 = df9
        last_col_ser = df9.iloc[-1]
        df11 = df11._append(last_col_ser)
        df11.iloc[-1,4] = early_riqi    #加‘计量单位’这一列后，df11.iloc[-1,3]变为df11.iloc[-1,4]
        df11.iloc[-1, 6] = '待查'       #加‘计量单位’这一列后，df11.iloc[-1,5]变为df11.iloc[-1,6]
        df11.iloc[-1, -7] = kucun_shuliang - leiji_ruku
        danjia = df9.iloc[-1,-6]
        df11.iloc[-1, -5] = round((kucun_shuliang - leiji_ruku) * danjia, 2)  # 调整金额，按调整后的数量和单价计算
        df11.iloc[-1, -2] = kucun_shuliang
        df11.iloc[-1, -1] = 0
    # grouped = df11.groupby(['供货单位','品名','本日数量'])
    return df11


def main():
    caigous,pinmings,early_riqi =caigouLiushuizhang()
    path = r'F:\a00nutstore\008\zw08\原材料实时流水账'
    os.chdir(path)
    filename = '库存商品分配.xlsx'
    sheet_name = '库存分配'
    datas = getKucun(caigous,pinmings,early_riqi)
    df = pd.concat(datas)
    df = df[df['入库数量']!=0]
    grouped = df.groupby(['供货单位', '品名', '期末结存数量'])
    for key, value in grouped:
        print(value[['日期', '供货单位', '入库数量', '入库金额']])
    print(grouped[['入库数量', '入库金额']].sum())
    df.to_excel(filename,sheet_name,index=False)
    os.startfile(filename)

if __name__ == '__main__':
    main()

