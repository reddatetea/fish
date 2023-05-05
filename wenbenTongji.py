'''
对指定文本文件里的字出现次数进行统计
用于临帖时,可以优先临写出现频率最多的字!
'''
import openpyxl
import re
import easygui


def wenbenString(fname):
    wenben_string = ''
    with open(fname, 'r', encoding='utf-8') as file:
        for line in file.readlines():
            line = line.strip()
            wenben_string = wenben_string + line
    print(wenben_string)
    return wenben_string

def delzhiding(wenben_string,zhidings):
    lst = []
    for j in wenben_string:
        if j not in zhidings:
            lst.append(j)
    print(lst)
    return lst

def wenbenTongji(lst):
    dic = {}
    for j in lst:
        if j not in dic.keys():
            dic[j] = 1
        else:
            dic[j] += 1
    print(dic)
    dic_order = sorted(dic.items(), key=lambda x: x[1], reverse=True)   #元组
    print(dic_order)
    for key, value in dic_order:
        print(key, value)
    wenben_zishu = sum([j for i, j in dic_order])
    print('文本总字数:', wenben_zishu)
    print('文本中不同的字共有:', len(dic_order))

def main():
    msg = '请点选要统计字数出现频率的txt文本文件'
    fname = easygui.fileopenbox(msg)
    # filename = r'灵飞经墨迹文字.txt'
    wenben_string = wenbenString(fname)
    msg = '请输入字符串中不需要的指定字符'
    zhiding = easygui.multenterbox(msg, title='指定字符串',
                                   fields=['指定字符1', '指定字符2', '指定字符3', '指定字符4', '指定字符5', '指定字符6', '指定字符7', '指定字符',
                                           '指定字符9', '指定字符10'])

    zhiding = [j for j in zhiding if j not in ['',None]]
    print(zhiding)
    zhidings = {'：', '、', '。', '？', '〔五〕', '【', ')', '《', '（', '”', ') ', '〔一〕', '】', '》', '(', '〔三〕', '，', '〔四〕', '〔六〕', '）', '“', '〔二〕', '！', '；', '( '}
    if len(zhiding) ==0 :
        zhidings = zhidings
    else :
        for j in zhiding:
            if j not in ['',None]:
                zhidings.add(j)
            else :
                zhidings = zhidings
    zhidings = list(zhidings)
    print(zhidings)
    lst = delzhiding(wenben_string,zhidings)
    wenbenTongji(lst)


if __name__ == '__main__':
    main()







