'''
本程序用来计算各供应商送货期间，每月26号到次月25日为一个期间
将2020-07这种格式计算其上一个期间,qi_jian = '2020-07',计算出上一个期间shang_qijian为2020-06
将2020-07-26 这种格式计算其上一个期间,riqi = '2020-07-26'，计算出上一个期间shang_qijian为2020-06
本版增加迭代取上一个期间
'''
import re

def qijian(riqi):
    r = '(?P<year>\d{4})-(?P<month>0[1-9]|1[012])-(?P<day>0[1-9]|[12]\d|3[01])'
    pattern = re.compile(r)
    mat = pattern.match(riqi)
    if mat != None :
        year = int(mat.group('year'))
        month = int(mat.group('month'))
        day = int(mat.group('day'))

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
        qi_jian = str(year)+'-'+ str(yue)

    else:
        print('日期有误，匹配失败')


    return qi_jian

def shangQijian(qi_jian):
    r = '(?P<year>\d{4})-(?P<month>0[1-9]|1[012])'
    pattern = re.compile(r)
    mat = pattern.match(qi_jian)
    if mat != None:
        year = int(mat.group('year'))
        month = int(mat.group('month'))
        # 计算期间

        if month == 1:
            yue = 12
            year = year - 1

        else:
            yue = month - 1

        yue = '%02d' % yue
        shang_qijian = str(year) + '-' + str(yue)

    else:
        print('日期有误，匹配失败')

    return shang_qijian

def diedai_qushang_qijian(qi_jian):
    while qi_jian != '2020-01' :
        qi_jian = shangQijian(qi_jian)
        print(qi_jian)


def main():
    riqi = '2099-07-26'
    qi_jian = qijian(riqi)

    #shang_qijian = shangQijian(qi_jian)
    shang_qijian = diedai_qushang_qijian(qi_jian)


if __name__=='__main__':

    main()


