from xpinyin import Pinyin

def pinyinSort(wordlist):
    pin = Pinyin()
    temp = []
    for item in wordlist:
        temp.append((pin.get_pinyin(item),item))

    temp.sort()
    result = []
    for j in range(len(temp)):
        result.append((temp[j][1]))
    #print(result)
    return result

def zhongwenZhuanPinyin(zhongwen):
    pin = Pinyin()
    zhongwen_pinyin = pin.get_pinyin(zhongwen)
    #print(zhongwen_pinyin)
    return zhongwen_pinyin

def main():
    wordlist =['华为','苹果','小米','三星']
    print(pinyinSort(wordlist))
    zhongwen = '张博瑞'
    print(zhongwenZhuanPinyin(zhongwen))

if __name__=='__main__':
    main()

