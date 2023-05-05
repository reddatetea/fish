'''
快查令吨互算
本版增加只传入两个参数，就只判断正度和大度
'''
import pyperclip
import sys
import re


#已知令价计算吨价
def lingjiaTodunjia(lingjia0,ke,chang,kuan):
    ke1 = float(ke)
    chang1 = float(chang)
    kuan1 = float(kuan)
    lingjia = float(lingjia0)

    dunjia = round(lingjia/(ke1/1000/1000*chang1/1000*kuan1/1000*500),2)
    print('令价为%s元/令 %s克%s*%s 吨价为：'%(lingjia0,ke,chang,kuan), '%s元/吨'%dunjia)
    return dunjia

#已知吨价计算令价
def dunjiaTolingjia(dunjia0,ke,chang,kuan):
    ke1 = float(ke)
    chang1 = float(chang)
    kuan1 = float(kuan)
    dunjia = float(dunjia0)
    lingjia = round(dunjia*(ke1/1000/1000*chang1/1000*kuan1/1000*500),2)
    print('吨价为%s元/吨 %s克%s*%s 令价为：'%(dunjia0,ke,chang,kuan), '%s元/令'%lingjia)
    return lingjia

#已知令数计算吨数
def lingshuTodunshu(lingshu0,ke,chang,kuan):
    ke1 = float(ke)
    chang1 = float(chang)
    kuan1 = float(kuan)
    lingshu = float(lingshu0)
    dunshu = round(ke1/1000/1000*chang1/1000*kuan1/1000*500*lingshu,2)
    print('%s令 %s克%s*%s 吨数为:'%(lingshu0,ke,chang,kuan), '%s吨'%dunshu)
    return dunshu

#已知吨数计算令数
def dunshuTolingshu(dunshu0,ke,chang,kuan):
    ke1 = float(ke)
    chang1 = float(chang)
    kuan1 = float(kuan)
    dunshu = float(dunshu0)
    lingshu = round(dunshu/(ke1/1000/1000*chang1/1000*kuan1/1000*500),2)
    print('%s吨 %s克%s*%s 令数为:' %(dunshu0,ke,chang,kuan), '%s令' % lingshu)
    return lingshu

def main():

    if len(sys.argv) > 1:
        if len(sys.argv) == 5:
            ke = sys.argv[1]
            chang = sys.argv[2]
            kuan = sys.argv[3]
            temp = sys.argv[4]
        elif len(sys.argv) == 3:
            chang = sys.argv[1]
            kuan = sys.argv[2]
            #如果只传入两个参数，则判断正度大度后退出程序！
            if float(chang) * float(kuan) >= 787 * 1092 * 1.05:
                print('该材料是： 大度')
                return
            else:
                print('该材料是： 正度')
                return

        else :
            print('输入有误 ，请重新输入')

    else:
        spring = pyperclip.paste()
        a = spring.split()

        ke = a[0]
        chang = a[1]
        kuan = a[2]
        temp = a[3]

    rep = r'(\d+\.?\d*)(yl|yd|l|d)'
    pattern = re.compile(rep)
    mat = pattern.search(temp)

    if mat != None:

        if mat.group(2) == 'yl':
            lingjia0 = mat.group(1)
            #print(lingjia0)
            lingjiaTodunjia(lingjia0,ke,chang,kuan)

        elif mat.group(2) == 'yd':
            dunjia0 = mat.group(1)
            #print(dunjia0)
            dunjiaTolingjia(dunjia0,ke,chang,kuan)

        elif mat.group(2) == 'l':
            lingshu0 = mat.group(1)
            #print(lingshu0)
            lingshuTodunshu(lingshu0,ke,chang,kuan)


        elif mat.group(2) == 'd':
            dunshu0 = mat.group(1)
            #rint(dunshu0)
            dunshuTolingshu(dunshu0,ke,chang,kuan)


        else:
            print('输入有误，请重新输入')

    else:
        print('输入有误，请重新输入')

if __name__=="__main__" :
    main()
















