'''
将吨价转化为令价
'''

import re
import pandas as pd

def getKeChangKuan(str):
    ke = 0
    chang = 0
    kuan = 0
    pattern = r'^(?P<ke>\d{1,3})g\w+(?P<chang>\d{3,4})\*(?P<kuan>\d{3,4})\w*'
    regex = re.compile(pattern,flags=re.I)
    a = regex.search(str)
    if a :
        ke = float(a.group('ke'))
        chang = float(a.group('chang'))
        kuan = float(a.group('kuan'))
    return ke,chang,kuan

def DunjiaToLingjia(str,dunjia=0):
    ke = 0
    chang = 0
    kuan = 0
    pattern = r'^(?P<ke>\d{1,3})g\w+(?P<chang>\d{3,4})\*(?P<kuan>\d{3,4})\w*'
    regex = re.compile(pattern,flags=re.I)
    a = regex.search(str)
    if a :
        ke = float(a.group('ke'))
        chang = float(a.group('chang'))
        kuan = float(a.group('kuan'))
    lingjia = round(ke/1000*chang*kuan/1000/1000*500*dunjia/1000,2)
    return lingjia

def main():
    lingjia = DunjiaToLingjia('46g无碳复写上白787*1092',dunjia = 9865)
    print(lingjia)
    # fname = r'F:\repos\fish\2020入库.xlsx'
    # df = pd.read_excel(fname, sheet_name='入库')
    # df1 = df.assign(令价=df.apply(lambda x: DunjiaToLingjia(x['材料'], dunjia=x['吨价']), axis=1))

if __name__ == '__main__':
    main()
