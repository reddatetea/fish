'''
灰板的匹配，提取厚度、长度、宽度，计算合同单价
'''
import re


def huibanchicun(temp):
    string = temp.strip()
    pattern = r'(?P<hou>\d\.?\d?\d?)MM(?:.*)(?P<leixing>[灰板|双灰]\w+)(?P<chang>\d{3,4})\*(?P<kuan>\d{3,4})'
    regexp = re.compile(pattern)
    a = regexp.search(string)
    #midu =0.575  # 密度,1立方米的重量为1150克，厚度2mm的重量为1150克，1mm为575,厚度每米为0.575g

    if 'A级' in temp and 'FH' in temp:
        leibie = 'AFH'  # A级，质量好的！对灰板而言是复合板
        midu = 1160 / 2
    elif 'B级' in temp and 'FH' in temp:
        leibie = 'BFH'  # B级，质量次好的！对灰板而言是复合板
        midu = 1160 / 2
    else:
        if  'FH' in temp:
            leibie = 'BFH'  # B级，质量次好的！对灰板而言是复合板
            midu = 1160/2
        else :
            leibie = 'putong'  # 普通，一次成型板
            midu = 1160/2

    if a == None:
        print('没有匹配')
        hou = 0
        chang = 0
        kuan = 0

    else:
        # 克重
        hou = float(a.group('hou'))
        # 类型
        leixing = a.group('leixing')
        # 长
        chang = float(a.group('chang'))
        # 宽
        kuan = float(a.group('kuan'))

    dun_meizhang = hou * chang * kuan * midu / 1000 / 1000 / 1000/1000
    return dun_meizhang, leibie


def main():
    temp = '2.0MM富业灰板A级FH800*1100'
    dun_meizhang, leibie = huibanchicun(temp)

    print(dun_meizhang, leibie)


if __name__ == '__main__':
    main()










