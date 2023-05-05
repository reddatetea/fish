'''
线圈的匹配，提取规格、齿数、计算合同单价
'''
import re

def xianquan_chicun(temp):
    string = temp.strip()
    pattern = r'(?P<guige>.*\d{1})\*(?P<cishu>\d{1,2})'
    regexp = re.compile(pattern)
    a = regexp.search(string)

    if a == None:
        print('没有匹配')
        guige = 0
        cishu = 0
        return guige,cishu

    else:
        # 规格
        guige = a.group('guige')
        #齿数
        cishu = float(a.group('cishu'))

        return guige,cishu

def jisuanDanjia(guige,cishu):
    pass
    #目前信华的吨价 0.16
    #hetong_danjia =
    # changshu = (chang+10)*(kuan+10)/10/10
    # hetong_danjia = round(dunjia * changshu, 0)
    # return hetong_danjia

def main():
    temp = 'Q12*40单线环黑'
    guige,cishu = xianquan_chicun(temp)
    #hetong_danjia = jisuanDanjia(chang,kuan)
    #print('hetongdanjia', hetong_danjia)
    print(guige,cishu)

if __name__ == '__main__':
    main()










