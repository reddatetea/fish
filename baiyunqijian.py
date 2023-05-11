'''
本模块计算白云期间，将入库单日期减1作为送货单日期，以送货单的自然月份作为白云期间，自2021年1月1日起执行
'''
import re
import datetime

def baiyunQijian(riqi):
    ruku_date = datetime.datetime.strptime(riqi,'%Y-%m-%d')                   # 将日期的字符串格式转为标准日期格式
    songhuo_date = ruku_date - datetime.timedelta(days=1)       # 送货单日期 = 入库日期 - 1天
    songhuoriqi = datetime.datetime.strftime(songhuo_date, "%Y-%m-%d")       # 将送货单日期格式转字符串
    r = '(?P<year>\d{4})-(?P<month>0[1-9]|1[012])-(?P<day>0[1-9]|[12]\d|3[01])'
    pattern = re.compile(r)
    mat = pattern.match(songhuoriqi)
    year = int(mat.group('year'))
    month = int(mat.group('month'))
    day = int(mat.group('day'))
    # print(year,month,day)
    #计算白云期间
    songhuoday = '%02d' % day
    songhuomonth = '%02d' % month
    songhuoyear = '%02d' % year
    songhuoriqi = str(year) + '-' + str(month)+ '-' + str(day)
    baiyun_qijian = str(songhuoyear)+'-'+ str( songhuomonth)
    #print('白云日期',baiyunyear,baiyunyue,songhuoday)
    return baiyun_qijian,songhuoriqi

def main():
    riqi = '2021-1-26'
    baiyun_qijian,songhuoriqi = baiyunQijian(riqi)
    print(baiyun_qijian,songhuoriqi)

if __name__=='__main__':
    main()



