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

def diedai_qushang_qijian(byprices,pinming,qi_jian):
    while qi_jian != '2020-01' :
        qi_jian = shangQijian(qi_jian)
        byprices[qi_jian].setdefault(pinming, {0: 0})
        danjias = byprices[qi_jian][pinming].keys()
        danjia = max(danjias)
        if danjia != 0 :
            break
        else :
            continue
    print(danjia)


def main():
    byprices = {'2020-01': {'78g双胶': {6496: {'lingshu': 638, 'dunshu': 21.373, 'jiner': 138839.01}},
                            '63g卷筒纸': {6246: {'lingshu': 0, 'dunshu': 116.45, 'jiner': 727346.69}},
                            '55g卷筒纸': {6296: {'lingshu': 0, 'dunshu': 132.308, 'jiner': 833011.16}},
                            '2019年第3季返利': {6296: {'lingshu': 0, 'dunshu': 0, 'jiner': 0}},
                            '60g卷筒纸': {6146: {'lingshu': 0, 'dunshu': 97.626, 'jiner': 600009.4}},
                            '2019年12月返利': {6146: {'lingshu': 0, 'dunshu': 0, 'jiner': 0}},
                            '70g卷筒纸': {6296: {'lingshu': 0, 'dunshu': 122.683, 'jiner': 772412.1699999999}}, '55g双胶': {
            6396: {'lingshu': 870, 'dunshu': 24.401999999999997, 'jiner': 156075.19000000003}},
                            '70g道林双胶': {6396: {'lingshu': 805, 'dunshu': 27.002000000000002, 'jiner': 172704.79}},
                            '70g双胶': {6396: {'lingshu': 437, 'dunshu': 13.148, 'jiner': 84094.61}},
                            '98g双胶': {6396: {'lingshu': 540, 'dunshu': 25.637999999999998, 'jiner': 163980.65}},
                            '75g双胶': {6046: {'lingshu': 990, 'dunshu': 31.905, 'jiner': 192897.63}},
                            '12月返利': {6046: {'lingshu': 0, 'dunshu': 0, 'jiner': 0}},
                            '1月返利': {6046: {'lingshu': 0, 'dunshu': 0, 'jiner': 0}},
                            '1月多计': {6046: {'lingshu': 0, 'dunshu': 0, 'jiner': 0}}},
                '2020-03': {'55g卷筒纸': {6296: {'lingshu': 0, 'dunshu': 150.672, 'jiner': 948630.8999999999}},
                            '55g双胶': {6396: {'lingshu': 1920, 'dunshu': 45.376000000000005, 'jiner': 290224.89}},
                            '90g双胶': {6046: {'lingshu': 323, 'dunshu': 14.049000000000001, 'jiner': 84940.25}},
                            '65g卷筒纸': {6046: {'lingshu': 0, 'dunshu': 16.182, 'jiner': 97836.37}}}, '2020-04': {
            '55g卷筒纸': {6296: {'lingshu': 0, 'dunshu': 252.262, 'jiner': 1588241.5599999998},
                       6300: {'lingshu': 0, 'dunshu': 178.56500000000003, 'jiner': 1124959.5100000002}},
            '65g卷筒纸': {6046: {'lingshu': 0, 'dunshu': 57.82299999999999, 'jiner': 349597.87000000005}},
            '2月返利': {6046: {'lingshu': 0, 'dunshu': 0, 'jiner': 0}},
            '价差': {6046: {'lingshu': 0, 'dunshu': 0, 'jiner': 0}, 6296: {'lingshu': 0, 'dunshu': 0, 'jiner': 0},
                   6300: {'lingshu': 0, 'dunshu': 0, 'jiner': 0}},
            '63g卷筒纸': {6246: {'lingshu': 0, 'dunshu': 19.57, 'jiner': 122234.22}},
            '55g双胶': {6396: {'lingshu': 1290, 'dunshu': 32.491, 'jiner': 207812.43}},
            '70g卷筒纸': {6296: {'lingshu': 0, 'dunshu': 5.159, 'jiner': 32481.06}},
            '75g双胶': {6046: {'lingshu': 330, 'dunshu': 11.469999999999999, 'jiner': 69347.62},
                      6050: {'lingshu': 264, 'dunshu': 8.508, 'jiner': 51473.4}},
            '2019年第4季度返利': {6296: {'lingshu': 0, 'dunshu': 0, 'jiner': 0}},
            '60g卷筒纸': {6146: {'lingshu': 0, 'dunshu': 10.11, 'jiner': 62136.06}},
            '2019年第1季度返利': {6296: {'lingshu': 0, 'dunshu': 0, 'jiner': 0}},
            '2020年3月返利': {6296: {'lingshu': 0, 'dunshu': 0, 'jiner': 0}},
            '68g双胶': {6150: {'lingshu': 72, 'dunshu': 2.598, 'jiner': 15977.7}},
            '2019年返利': {6301: {'lingshu': 0, 'dunshu': 0, 'jiner': 0}, 6300: {'lingshu': 0, 'dunshu': 0, 'jiner': 0}},
            '78g双胶': {6500: {'lingshu': 748, 'dunshu': 25.58, 'jiner': 166270.0}},
            '98g双胶': {6500: {'lingshu': 144, 'dunshu': 6.064, 'jiner': 39416}},
            '90g双胶': {6050: {'lingshu': 114, 'dunshu': 5.55, 'jiner': 33577.5}}}, '2020-05': {
            '55g双胶': {5750: {'lingshu': 990, 'dunshu': 24.733, 'jiner': 142214.75},
                      5550: {'lingshu': 5100, 'dunshu': 108.68999999999998, 'jiner': 603229.4999999999}},
            '价差': {5550: {'lingshu': 0, 'dunshu': 0, 'jiner': 0}, 5700: {'lingshu': 0, 'dunshu': 0, 'jiner': 0},
                   5650: {'lingshu': 0, 'dunshu': 0, 'jiner': 0}, 5600: {'lingshu': 0, 'dunshu': 0, 'jiner': -50000},
                   5450: {'lingshu': 0, 'dunshu': 0, 'jiner': 0}, 5400: {'lingshu': 0, 'dunshu': 0, 'jiner': 0}},
            '55g卷筒纸': {5650: {'lingshu': 0, 'dunshu': 36.632999999999996, 'jiner': 206976.45},
                       5450: {'lingshu': 0, 'dunshu': 385.532, 'jiner': 2101149.3699999996}},
            '60g卷筒纸': {5550: {'lingshu': 0, 'dunshu': 29.680999999999997, 'jiner': 164729.55},
                       5350: {'lingshu': 0, 'dunshu': 67.027, 'jiner': 358594.45}},
            '90g双胶': {5450: {'lingshu': 190, 'dunshu': 8.17, 'jiner': 44526.5},
                      5250: {'lingshu': 95, 'dunshu': 4.625, 'jiner': 24281.25}},
            '70g卷筒纸': {5700: {'lingshu': 0, 'dunshu': 10.248, 'jiner': 58413.6},
                       5250: {'lingshu': 0, 'dunshu': 20.224, 'jiner': 106176.0}},
            '78g双胶': {5900: {'lingshu': 220, 'dunshu': 7.37, 'jiner': 43483},
                      5700: {'lingshu': 1342, 'dunshu': 46.492999999999995, 'jiner': 265010.1}},
            '98g双胶': {5900: {'lingshu': 180, 'dunshu': 7.58, 'jiner': 44722},
                      5700: {'lingshu': 90, 'dunshu': 3.79, 'jiner': 21603}},
            '63g卷筒纸': {5450: {'lingshu': 0, 'dunshu': 49.589000000000006, 'jiner': 270260.05000000005},
                       None: {'lingshu': 0, 'dunshu': 0, 'jiner': 0}},
            '98g卷筒纸': {5600: {'lingshu': 0, 'dunshu': 3.692, 'jiner': 20675.2},
                       5400: {'lingshu': 0, 'dunshu': 3.783, 'jiner': 20428.2}},
            '75g双胶': {5250: {'lingshu': 220, 'dunshu': 7.09, 'jiner': 37222.5}},
            '65g卷筒纸': {5250: {'lingshu': 0, 'dunshu': 15.017999999999999, 'jiner': 78844.5}},
            '65g双胶': {5350: {'lingshu': 150, 'dunshu': 5.274, 'jiner': 28215.9}},
            '70g双胶': {5350: {'lingshu': 391, 'dunshu': 12.25, 'jiner': 65537.5}},
            '100g双胶': {5600: {'lingshu': 323, 'dunshu': 13.928, 'jiner': 77996.8}},
            '78g卷筒纸': {5550: {'lingshu': 0, 'dunshu': 9.506, 'jiner': 52758.3}},
            '202005返利': {5450: {'lingshu': 0, 'dunshu': 0, 'jiner': 0}},
            '68g卷筒纸': {5650: {'lingshu': 0, 'dunshu': 12.5, 'jiner': 70625},
                       5550: {'lingshu': 0, 'dunshu': 11.77, 'jiner': 65323.5}}},
                '2020-06': {'55g卷筒纸': {5450: {'lingshu': 0, 'dunshu': 318.1309999999999, 'jiner': 1733813.9499999995}},
                            '75g双胶': {5250: {'lingshu': 374, 'dunshu': 12.053, 'jiner': 63278.25}},
                            '65g卷筒纸': {5250: {'lingshu': 0, 'dunshu': 20.277, 'jiner': 106454.25}},
                            '55g双胶': {5550: {'lingshu': 1920, 'dunshu': 47.046, 'jiner': 261105.30000000002}},
                            '63g卷筒纸': {5450: {'lingshu': 0, 'dunshu': 131.299, 'jiner': 715579.5499999999}},
                            '价差': {5450: {'lingshu': 0, 'dunshu': 0, 'jiner': 0}},
                            '60g卷筒纸': {5350: {'lingshu': 0, 'dunshu': 129.364, 'jiner': 692097.4}},
                            '70g卷筒纸': {5500: {'lingshu': 0, 'dunshu': 27.076999999999998, 'jiner': 148923.5},
                                       5600: {'lingshu': 0, 'dunshu': 27.841, 'jiner': 155909.6}},
                            '6月返利': {5450: {'lingshu': 0, 'dunshu': 0, 'jiner': 0}},
                            '98g双胶': {5700: {'lingshu': 90, 'dunshu': 4.324, 'jiner': 24646.800000000003}},
                            None: {5450: {'lingshu': 0, 'dunshu': 0, 'jiner': 0}},
                            '70g双胶': {5700: {'lingshu': 851, 'dunshu': 27.958, 'jiner': 159360.6}}},
                '2020-07': {'63g卷筒纸': {5450: {'lingshu': 0, 'dunshu': 31.679, 'jiner': 172650.55}},
                            '55g卷筒纸': {5450: {'lingshu': 0, 'dunshu': 50.568, 'jiner': 275595.6},
                                       5350: {'lingshu': 0, 'dunshu': 32.246, 'jiner': 172516.1}},
                            '70g卷筒纸': {5600: {'lingshu': 0, 'dunshu': 34.723, 'jiner': 194448.8}},
                            '7月返利': {5450: {'lingshu': 0, 'dunshu': 0, 'jiner': 0}},
                            '55g双胶': {5550: {'lingshu': 510, 'dunshu': 12.053, 'jiner': 66894.15},
                                      0: {'lingshu': 0, 'dunshu': 0, 'jiner': 0}},
                            '60g卷筒纸': {5350: {'lingshu': 0, 'dunshu': 0, 'jiner': 0}},
                            '78g双胶': {0: {'lingshu': 0, 'dunshu': 0, 'jiner': 0}},
                            '98g卷筒纸': {5600: {'lingshu': 0, 'dunshu': 0, 'jiner': 0}},
                            '70g双胶': {0: {'lingshu': 0, 'dunshu': 0, 'jiner': 0}},
                            '98g双胶': {0: {'lingshu': 0, 'dunshu': 0, 'jiner': 0}}}}
    # qi_jian = '2020-07'
    riqi = '2020-07-26'
    qi_jian = qijian(riqi)
    pinming = '98g卷筒纸'

    #shang_qijian = shangQijian(qi_jian)
    diedai_qushang_qijian(byprices,pinming,qi_jian)



if __name__=='__main__':

    main()


