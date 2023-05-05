'''
灰板的匹配，提取厚度、长度、宽度，计算合同单价
'''
import re

def huibanchicun(temp):
    string = temp.strip()
    pattern = r'(?P<hou>\d\.?\d?\d?)MM(?:.*)(?P<leixing>灰板|双灰)(?P<chang>\d{3,4})\*(?P<kuan>\d{3,4})'
    regexp = re.compile(pattern)
    a = regexp.search(string)

    if a == None:
        print('没有匹配')
        hou = 0
        chang = 0
        kuan = 0
        return hou,chang,kuan



    else:
        # 克重
        hou = float(a.group('hou'))
        # 类型
        leixing = a.group('leixing')
        # 长
        chang = float(a.group('chang'))
        # 宽
        kuan = float(a.group('kuan'))

        return hou,chang,kuan


def jisuanDanjia(im_gongyingshang,hou,chang,kuan):
    if im_gongyingshang=='舞钢':
        # 目前舞钢的吨价 3085元/吨
        dunjia = 3435  # 2021-04-06起
        changshu = 2 * 870 * 800 * 1100
    else :
        # 目前富业的吨价暂估为 3178元/吨
        dunjia = 3178  # 2021-04-06起
        changshu = 2 * 870 * 800 * 1100


    if hou == 0:
        hetong_danjia = 0
    else :
        zhangshu = changshu / hou / chang / kuan
        hetong_danjia = round(dunjia / zhangshu, 2)



    return hetong_danjia

def main():
    temp = '2MM灰板780*1280'
    hou,chang,kuan = huibanchicun(temp)
    hetong_danjia = jisuanDanjia(im_gongyingshang,hou,chang,kuan)
    print('hetongdanjia', hetong_danjia)

if __name__ == '__main__':
    main()










