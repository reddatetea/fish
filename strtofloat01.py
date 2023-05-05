import re

def strtoFloat(string):


    if string in ['',None]:
        newshu = 0
    else :
        liang = string.split('.')
        zhengshu = liang[0]
        xiaoshu = liang[1]

        # 处理整数部分
        zhengshu1 = zhengshu.replace(',', '')
        zhengshu2 = float(zhengshu1)

        # 处理小数部分
        xiaoshu1 = '0.' + xiaoshu
        xiaoshu2 = float(xiaoshu1)

        # 重新组合为float
        newshu = zhengshu2 + xiaoshu2
        return  newshu

def main():
    string = ''
    newshu = strtoFloat(string)
    print(newshu)

if __name__ == '__main__':
    main()







