'''
纸箱类别
'''
import re

def zhixiangLeibie(pinming):
    haoxiangs = ['C7箱','C8箱','C9箱','F10箱','F11箱','F12箱','F13箱','F14箱','F15箱','F16箱']
    ruiyixiangs = ['锐意箱','锐意外箱']
    xinruixiangs = ['新税']
    #外贸箱
    waimaoxiangs = ['外贸箱','外贸外箱']

    zhixiangs = haoxiangs + ruiyixiangs + xinruixiangs + waimaoxiangs

    for zhixiang in zhixiangs :
        r = r'.*(?P<xiaolei>%s).*' % zhixiang
        pattern = re.compile(r)
        pipei = re.search(pattern, pinming)
        if pipei is not None:
            print(pipei.group('xiaolei'))
        else:
            pass

def main():
    pinming = '乌克兰HCA5-80外贸外箱'
    zhixiangLeibie(pinming)

if __name__ == '__main__' :
    main()
