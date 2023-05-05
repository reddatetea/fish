'''
pp片的匹配，提取厚度、长度、宽度，计算合同单价
'''
import re


def chicun(temp):
    string = temp.strip()
    pattern = r'(?P<hou>\d{1}\.{1}\d{1,2})\w+PP片(?P<chang>\d{2,4})\*(?P<kuan>\d{2,4})'
    regexp = re.compile(pattern)
    a = regexp.search(string)
    if a == None:
        print('没有匹配')
        hou = 0
        chang = 0
        kuan = 0
    else:
        # 克重
        hou = float(a.group('hou'))

        # 长
        chang = float(a.group('chang'))
        # 宽
        kuan = float(a.group('kuan'))
    return hou,chang*kuan/1000/1000

def main():
    temp = '0.25挪威A5磨砂封面PP片70*215'
    hou,mianji = chicun(temp)
    print(hou,mianji)

if __name__ == '__main__':
    main()










