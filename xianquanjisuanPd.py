'''
线圈的匹配，提取规格、齿数、计算合同单价
'''
import re

def chicun(temp):
    string = temp.strip()
    if '*' not in string:
        pattern = r'(?P<guige>Q?(\d/)?\d{1,2})'
        regexp = re.compile(pattern)
        a = regexp.search(string)
    else :
        pattern = r'(?P<guige>Q?(\d/)?\d{1,2})\*(?P<cishu>\d{1,2})'
        regexp = re.compile(pattern)
        a = regexp.search(string)

    if a == None:
        print('没有匹配')
        guige = 0
        cishu = 0
    else:
        guige = a.group('guige')  # 规格
        try :
            cishu = float(a.group('cishu'))  # 齿数
        except:
            cishu = 0

    if ('黑' in temp) or ('白' in temp):
        color = 'pure'
    elif ('金' in temp) or ('银' in temp) or ('铜' in temp):
        color = 'gold_silver'
    else:
        color = 'multi'
    return guige,color,cishu

def main():
    temp = '1.00mm黑线环'
    guige,color,cishu = chicun(temp)
    print(guige,color,cishu)

if __name__ == '__main__':
    main()










