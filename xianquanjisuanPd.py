'''
线圈的匹配，提取规格、齿数、计算合同单价
'''
import re

def chicun(temp):
    string = temp.strip()
    if 'mm'  in string.lower() :
        pattern = r'(?P<qian>\d{1})\.?(?P<hou>\d{0,2})MM'
        regexp = re.compile(pattern, flags=re.I)
        a = regexp.search(string)
        qian = a.group('qian')
        hou = a.group('hou')
        if hou == "":
            hou = '00'
        elif hou == '9':
            hou = '90'
        else :
            hou = hou
        guige = qian + hou
    elif '*' not in string:
        pattern = r'(?P<guige>Q?(\d/)?\d{1,2})'
        regexp = re.compile(pattern)
        a = regexp.search(string)
        guige = a.group('guige')  # 规格

    else :
        pattern = r'(?P<guige>Q?(\d/)?\d{1,2})\*(?P<cishu>\d{1,2})'
        regexp = re.compile(pattern)
        a = regexp.search(string)
        guige = a.group('guige')  # 规格


    if a == None:
        cishu = 0
        guige = 0

    else:
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
    temp = '1*19黑色双线环'     #0.95mm黑线环
    guige,color,cishu = chicun(temp)
    print(guige,color,cishu)

if __name__ == '__main__':
    main()










