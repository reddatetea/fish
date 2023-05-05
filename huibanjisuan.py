'''
灰板的匹配，提取厚度、长度、宽度，计算合同单价
'''
import re


def huibanchicun(temp):
    string = temp.strip()
    pattern = r'(?P<hou>\d\.?\d?\d?)MM?(?P<leixing>.*?[(灰板)|(双灰)]\w+)(?P<chang>\d{3,4})\*(?P<kuan>\d{3,4})'
    regexp = re.compile(pattern)
    mat = regexp.search(string)
    #midu =0.575  # 密度,1立方米的重量为1150克，厚度2mm的重量为1150克，1mm为575,厚度每米为0.575g

    ke = 1200
    if 'A级' in temp and 'FH' in temp:
        leibie = 'AFH'  # A级，质量好的！对灰板而言是复合板

    elif 'B级' in temp and 'FH' in temp:
        leibie = 'BFH'  # B级，质量次好的！对灰板而言是复合板

    else:
        if  'FH' in temp:
            leibie = 'BFH'  # B级，质量次好的！对灰板而言是复合板

        else :
            leibie = 'putong'  # 普通，一次成型板


    if mat == None:
        print('没有匹配')
        hou = 0
        chang = 0
        kuan = 0

    else:

        # 克重
        hou = float(mat.group('hou'))
        # 类型
        leixing = mat.group('leixing')
        # 长
        chang = float(mat.group('chang'))
        # 宽
        kuan = float(mat.group('kuan'))
        pattern2 = r'(?P<ke>\d{3,4})g'
        regexp2 = re.compile(pattern2)
        mat2 = regexp2.search(leixing)
        if mat2:
            ke = float(mat2.group('ke'))
        else :
            ke = 1200
    dun_meizhang = hou * chang * kuan * ke/hou / 1000 / 1000 / 1000/1000
    return dun_meizhang,hou,ke, leibie,chang,kuan


def main():
    temp = '1.8MM1050g四川联益B级灰板FH860*1070'
    dun_meizhang,hou,ke,leibie,chang,kuan = huibanchicun(temp)

    print(dun_meizhang,hou,ke,leibie,chang,kuan)


if __name__ == '__main__':
    main()










