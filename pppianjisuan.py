'''
柔板的匹配，提取厚度、长度、宽度，计算合同单价
'''
import re

def pppianchicun(temp):
    string = temp.strip()

    pattern = r'(?P<hou>0\.\d{1,2})(?:.*(PP片|封面PP片|PP片封面))(?P<chang>\d{2,4})(\*|-)(?P<kuan>\d{2,4})'
    regexp = re.compile(pattern)
    a = regexp.search(string)

    if a == None:
        print('没有匹配')

        chang = 0
        kuan = 0
        hou = 0
        return chang,kuan,hou

    else:
        # 长
        chang = float(a.group('chang'))
        # 宽
        kuan = float(a.group('kuan'))
        hou = a.group('hou')

        return chang,kuan,hou

def jisuanDanjia(chang,kuan,hou):
    #目前信华的吨价 0.16
    sisuanjiner1 = 0.98/889/356
    sisuanjiner2 = 0.98 / 889 / 356/25*30
    sisuanjiner3 = 0.73 /227 / 373/65*60

    dunjia = {'0.25':sisuanjiner1,'0.3':sisuanjiner2,'0.6':sisuanjiner3}
    changshu = chang*kuan
    hetong_danjia = round(dunjia[hou] * changshu, 2)
    return hetong_danjia

def main():
    temp = '0.6挪威A5磨砂PP片封面161*215'
    chang,kuan,hou = pppianchicun(temp)
    print(chang,kuan,hou)
    hetong_danjia = jisuanDanjia(chang,kuan,hou)
    print('hetongdanjia', hetong_danjia)

if __name__ == '__main__':
    main()










