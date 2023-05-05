'''
本程序用来计算各供应商送货期间，每月26号到次月25日为一个期间
'''
import re

def qijian(riqi):

    r = '(?P<year>\d{4})-(?P<month>0[1-9]|1[012])-(?P<day>0[1-9]|[12]\d|3[01])'
    pattern = re.compile(r)
    mat = pattern.match(riqi)
    if mat != None :

        #print(mat)
        #print(mat.group('year'))
        #print(mat.group('month'))
        #print(mat.group('day'))
        year = int(mat.group('year'))
        month = int(mat.group('month'))
        day = int(mat.group('day'))
        #print(year,month,day)

        #计算期间
        if day>25 :
            if month == 12 :
                yue = 1
                year = year +1

            else :
                yue = month +1

        else:
            yue = month
            year = year


        yue= '%02d'%yue
        qijian = str(year)+'-'+ str(yue)
        #print('日期',year,yue,day)
        #print('期间',qijian)
    else:
        print('日期有误，匹配失败')

    return qijian


def main():
    riqi = '2021-11-30'

    qijia= qijian(riqi)
    print(qijia)

if __name__=='__main__':

    main()


