'''
类的使用
'''
# _*_ conding:utf-8 _*_
import zhixiangTodic
import openpyxl
import re

class Zhixiang():
    def __init__(self,pinming):
        self.pinming = pinming
        chang = zhixiangTodic.zhixiangdic()[pinming][0]
        kuan = zhixiangTodic.zhixiangdic()[pinming][1]
        gao = zhixiangTodic.zhixiangdic()[pinming][2]

        self.chang = chang
        self.kuan = kuan
        self.gao = gao
        dange_mianji = round((self.chang + self.kuan + 80) / 1000 * (self.kuan + self.gao + 50) / 1000 * 2,2)
        self.dange_mianji = dange_mianji

    def zhixiangmessage(self):
        #print(self.pinming,self.chang,self.kuan,self.gao,self.dange_mianji)
        return self.pinming,self.chang,self.kuan,self.gao,self.dange_mianji

class Leixiang(Zhixiang):
    def  __init__(self,pinming):
        super().__init__(pinming)
    def singleprice(self,gongyingshang):
        singlePrice = 2.06
        return singlePrice

class Haoxiang(Zhixiang):
    def  __init__(self,pinming):
        super().__init__(pinming)
    def singleprice(self,gongyingshang):
        if gongyingshang == '恒龙包装':
            singlePrice = 3.55
        elif gongyingshang == '武汉市九安源纸业有限公司':
            singlePrice = 3.64
        elif gongyingshang == '孝感鑫荣环保包装':
            singlePrice = 3.6
        return singlePrice


class Ruiyixiang(Zhixiang):
    def  __init__(self,pinming):
        super().__init__(pinming)
    def singleprice(self,gongyingshang):
        if gongyingshang == '恒龙包装':
            singlePrice = 3.55
        elif gongyingshang == '武汉市九安源纸业有限公司':
            singlePrice = 3.64
        elif gongyingshang == '孝感鑫荣环保包装':
            singlePrice = 3.6
        return singlePrice

class Xinruixiang(Zhixiang):
    def  __init__(self,pinming):
        super().__init__(pinming)
    def singleprice(self,gongyingshang):
        if gongyingshang == '恒龙包装':
            singlePrice = 3.2
        elif gongyingshang == '武汉市九安源纸业有限公司':
            singlePrice = 3.1
        elif gongyingshang == '孝感鑫荣环保包装':
            singlePrice = 3.33

        return singlePrice

class Waimaoxiang(Zhixiang):
    def  __init__(self,pinming):
        super().__init__(pinming)
    def singleprice(self,gongyingshang):
        if gongyingshang == '恒龙包装':
            singlePrice = 3.7
        elif gongyingshang == '武汉市九安源纸业有限公司':
            singlePrice = 3.64
        elif gongyingshang == '孝感鑫荣环保包装':
            singlePrice = 3.6
        return singlePrice

class Leimaoxiang(Zhixiang):
    def  __init__(self,pinming):
        super().__init__(pinming)

    def singleprice(self, gongyingshang):
        if gongyingshang == '恒龙包装':
            singlePrice = 3.2
        elif gongyingshang == '武汉市九安源纸业有限公司':
            singlePrice = 3.26
        elif gongyingshang == '孝感鑫荣环保包装':
            singlePrice = 3.33
        return singlePrice


def zhixiangLeibian(pinming):
    leixiangs = ['内箱']
    # 质量好一点的纸箱
    haoxiangs = ['C7箱', 'C8箱', 'C9箱', 'F10箱', 'F11箱', 'F12箱', 'F13箱', 'F14箱', 'F15箱', 'F16箱']
    ruiyixiangs = ['锐意箱', '锐意外箱']
    xinruixiangs = ['新锐']
    # 外贸箱
    waimaoxiangs = ['外贸箱', '外贸外箱']
    zhixiangs = leixiangs + haoxiangs + ruiyixiangs + xinruixiangs + waimaoxiangs

    for zhixiang in zhixiangs:
        r = r'.*(?P<xiaolei>%s).*' % zhixiang
        pattern = re.compile(r)
        pipei = re.search(pattern, pinming)

        if pipei is not None:
            zhixiang_xiaolei = pipei.group('xiaolei')
            if zhixiang_xiaolei in leixiangs :
                leibie = Leixiang(pinming)
                return leibie
            elif zhixiang_xiaolei in haoxiangs :
                leibie = Haoxiang(pinming)
                return leibie
            elif zhixiang_xiaolei in xinruixiangs :
                leibie = Xinruixiang(pinming)
                return leibie
            elif zhixiang_xiaolei in ruiyixiangs :
                leibie = Ruiyixiang(pinming)
                return leibie
            elif zhixiang_xiaolei in waimaoxiangs :
                leibie = Waimaoxiang(pinming)
                return leibie

            else :
                leibie = Leimaoxiang(pinming)
                return leibie

        else:
            continue

    leibie = Leimaoxiang(pinming)
    return leibie

def main():
    pinming = r'DJL3260锐意外箱'
    gongyingshang = '恒龙包装'
    leibie =zhixiangLeibian(pinming)
    pinmin,chang,kuan,gao,dange_mianji = leibie.zhixiangmessage()
    singlePrice = leibie.singleprice(gongyingshang)
    print(singlePrice)
    hetongPrice = round(dange_mianji*singlePrice,2)
    print(hetongPrice)

if __name__ == '__main__' :
    main()





