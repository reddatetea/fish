'''
已知令价lingjia0算吨价dunjia
已知吨价dunjia0算令价lingjia
已知令数ling0算吨数dun
已知吨数dun0算令数ling
本版删掉global,改由参数传递
正则表达有个地方稍改！rep = r'(\d+\.?\d*)(元/令|元/吨|令|吨)',原来是\d+
'''
import pyperclip
import sys
import os
import re
import singleCailiaReoname


#已知令价计算吨价
def lingjiaTodunjia(cailiaoname,lingjia0,ke,chang,kuan):
    dunjia = round(lingjia0/(ke/1000/1000*chang/1000*kuan/1000*500),2)
    print('%s的吨价为：'%cailiaoname, '%s元/吨'%dunjia)
    return dunjia

#已知吨价计算令价
def dunjiaTolingjia(cailiaoname,dunjia0,ke,chang,kuan):
    lingjia = round(dunjia0*(ke/1000/1000*chang/1000*kuan/1000*500),2)
    print('%s的令价为：'%cailiaoname, '%s元/令'%lingjia)
    return lingjia

#已知令数计算吨数
def lingshuTodunshu(cailiaoname,lingshu0,ke,chang,kuan):
    lingshu = float(lingshu0)
    dunshu = round(ke/1000/1000*chang/1000*kuan/1000*500*lingshu,2)
    print('%s令  %s的吨数为：'%(lingshu0,cailiaoname), '%s吨'%dunshu)
    return dunshu

#已知吨数计算令数
def dunshuTolingshu(cailiaoname,dunshu0,ke,chang,kuan):
    dunshu = float(dunshu0)
    lingshu = round(dunshu/(ke/1000/1000*chang/1000*kuan/1000*500),2)
    print('%s吨  %s令数为：'%(dunshu0,cailiaoname), '%s令'%lingshu)
    return lingshu

def main():

    if len(sys.argv) > 1:
        #spring = ' '.join(sys.argv[1:])
        cailiaoname = sys.argv[1]
        temp = sys.argv[2]


    else:
        spring = pyperclip.paste()
        a = spring.split()
        #print(a)

        cailiaoname = a[0]
        temp = a[1]

    cw_name, price_name, ke, chang, kuan = singleCailiaoRename.singlecailiaoName(cailiaoname)
    ke = float(ke)
    chang = float(chang)
    kuan = float(kuan)

    #print(cailiaoname, temp)
    rep = r'(\d+\.?\d*)(元/令|元/吨|令|吨)'
    pattern = re.compile(rep)
    mat = pattern.search(temp)

    if mat != None:
        if mat.group(2) == '元/令':
            lingjia0 = float(mat.group(1))
            #print(lingjia0)
            lingjiaTodunjia(cailiaoname, lingjia0,ke,chang,kuan)

        elif mat.group(2) == '元/吨':
            dunjia0 = float(mat.group(1))
            #print(dunjia0)
            dunjiaTolingjia(cailiaoname, dunjia0,ke,chang,kuan)

        elif mat.group(2) == '令':
            lingshu0 = mat.group(1)
            #print(lingshu0)
            lingshuTodunshu(cailiaoname,lingshu0,ke,chang,kuan)

        elif mat.group(2) == '吨':
            dunshu0 = mat.group(1)
            #rint(dunshu0)
            dunshuTolingshu(cailiaoname,dunshu0,ke,chang,kuan)

        else:
            print('输入有误，请重新输入')

    else:
        print('输入有误，请重新输入')

    print('财务命名为：%s'%cw_name)

if __name__=="__main__" :
    main()
















