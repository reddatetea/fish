'''
计算背条面积，根据单价，计算金额
'''
# _*_ conding:utf-8 _*_

import re

def beitiaoJisuan(beitiaoName):
    pattern = r'(?P<kuan>\d{2})MM.*背条'
    regex = re.compile(pattern)
    pipei = regex.search(beitiaoName)
    if pipei == None :
        pass
    else :
        kuan = float(pipei.group('kuan'))
        print(kuan)
    if '牛皮' in beitiaoName:
        leibie = 'niupi'
    else:
        leibie = 'putong'
    return leibie,kuan

def main():
    beitiao = '26MM504灰背条'
    leibie,kuan=beitiaoJisuan(beitiao)
    print(leibie,kuan)
    print(type(kuan))

if __name__ == '__main__':
    main()