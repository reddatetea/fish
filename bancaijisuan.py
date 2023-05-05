'''
版材的匹配，提取厚度、长度、宽度，计算合同单价
'''
import re

def chicun(temp):
    string = temp.strip()
    pattern = r'[CTP|PS版]\w*版材*(?P<chang>\d{3,4})(\*|-|X|x)(?P<kuan>\d{3,4})$'
    regexp = re.compile(pattern)
    a = regexp.search(string)

    if a == None:
        print('没有匹配')

        chang = 0
        kuan = 0


    else:
        # 长
        chang = float(a.group('chang'))
        # 宽
        kuan = float(a.group('kuan'))

    mianji = chang *kuan/1000/1000

    return mianji

def main():
    temp = 'PS版920*760'
    mianji = chicun(temp)
    print(mianji)

if __name__ == '__main__':
    main()










