'''
柔板的匹配，提取厚度、长度、宽度，计算合同单价
'''
import re

def roubanchicun(temp):
    string = temp.strip()
    pattern = r'(?:.*)(?P<chang>\d{3,4})(\*|-|X|x)(?P<kuan>\d{3,4})'
    regexp = re.compile(pattern)
    a = regexp.search(string)

    if a == None:
        print('没有匹配')

        chang = 0
        kuan = 0
        return chang,kuan

    else:
        # 长
        chang = float(a.group('chang'))
        # 宽
        kuan = float(a.group('kuan'))

        return chang,kuan

def jisuanDanjia(im_gongyingshang,chang,kuan,temp):
    if im_gongyingshang=='信华'  or im_gongyingshang=='辉盈':
        if 'HH' not in  temp :
            #目前信华的吨价 0.16
            dunjia = 0.13
        else :
            dunjia = 0.15
        changshu = (chang + 10) * (kuan + 10) / 10 / 10
    else :
        dunjia = 0.15
        changshu = (chang ) * (kuan ) / 10 / 10
    hetong_danjia = round(dunjia * changshu, 0)
    return hetong_danjia

def main():
    temp = 'N0871语文-内芯760*520'
    chang,kuan = roubanchicun(temp)
    print(chang,kuan)
    im_gongyingshangs = ['信华','博质']
    for im_gongyingshang in im_gongyingshangs:
        hetong_danjia = jisuanDanjia(im_gongyingshang,chang,kuan,temp)
        print('hetongdanjia', hetong_danjia)

if __name__ == '__main__':
    main()










