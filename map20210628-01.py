import os
from xpinyin import Pinyin

def getpinyin(chinese_str):
    p = Pinyin()
    pinyins = p.get_pinyin(chinese_str, '-')
    pinyin_str = ' '.join([i.capitalize() for i in pinyins.split('-')] )
    return pinyin_str

def main():
    chinese_str = input('请输入需要转为拼音的中文字符串\n')
    pinyin_str = getpinyin(chinese_str)
    gongyings = ['波士胶（上海）管理有限公司', '驻马店市白云纸业有限公司', '东莞市合裕粘贴制品有限公司', '东莞市双吉装订器材有限公司', '广州宝勒商贸有限公司']
    gonyings_pin=list(map(getpinyin,gongyings))
    print(gonyings_pin)

if __name__ == '__main__':
    main()