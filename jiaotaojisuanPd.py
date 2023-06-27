'''
柔板的匹配，提取厚度、长度、宽度，计算合同单价
'''
'''
柔板的匹配，提取厚度、长度、宽度，计算合同单价
'''
import re
import pandas as pd

def jiaotaochicun(temp):
    string = temp.strip()
    pattern1 = r'(?P<leibie>XR|夏天|冬天|EVA|EJL|EVA\s+|EJL\s|勤问|EVA\s+DJL)(?P<kaibie>16|32|48|64|80|100)K(?P<yeshu>\d{2,3})胶套'
    pattern2 = r'胶套\w*(?P<chang>\d{3,4})\*(?P<kuan>\d{3,4})'
    regexp1 = re.compile(pattern1)
    pipei1 = regexp1.search(string)
    regexp2 = re.compile(pattern2)
    pipei2 = regexp2.search(string)
    if pipei1 == None:
        # print('没有匹配')
        leibie = 'putong'
        kaibie = 0
        yeshu = 0
    else:
        leibie = pipei1.group('leibie')
        kaibie = float(pipei1.group('kaibie'))
        yeshu = float(pipei1.group('yeshu'))
        if 'EVA' in leibie or '勤问' in leibie or 'EJL' in leibie:
            leibie = 'gaoji'
        else :
            leibie = 'putong'

    if pipei2 == None:
        # print('没有匹配')
        chang = 0
        kuan = 0
    else:
        chang = float(pipei2.group('chang'))
        kuan = float(pipei2.group('kuan'))
    return leibie,kaibie,yeshu,chang,kuan


def main():
    temp = '勤问32K80胶套291*201'
    leibie,kaibie,yeshu,chang,kuan = jiaotaochicun(temp)
    print(leibie,kaibie,yeshu,chang,kuan)

if __name__ == '__main__':
    main()










