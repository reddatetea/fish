'''
计算背条面积，根据单价，计算金额
'''
# _*_ conding:utf-8 _*_

import re

def beitiaoJisuan(beitiaoName,im_gongyingshang):
    pattern = r'(?P<kuan>\d{2})MM.*背条'
    regex = re.compile(pattern)
    pipei = regex.search(beitiaoName)
    if pipei == None :
        pass
    else :
        kuan = float(pipei.group('kuan'))/1000
        print(kuan)
    if im_gongyingshang == '苏州市三鑫' :
        if '牛皮' in beitiaoName:
            # beitiao_price = 1.25  # 牛皮背条单价1.25
            beitiao_price = 1.1  # 牛皮背条单价1.25    #8月1日起新合同（胶套本裹背条1.1，学生本裹背条1.9）
        else:
            # beitiao_price = 2.4
            beitiao_price = 2.3  # 8月1日起新合同（办公本裹背条）
    elif  im_gongyingshang == '昆山楚宏' :
        if '牛皮' in beitiaoName:
            # beitiao_price = 1.25  # 牛皮背条单价1.25
            beitiao_price = 1.1  # 牛皮背条单价1.25    #8月1日起新合同（胶套本裹背条1.1，学生本裹背条1.9）
        else:
            if kuan - 0.025 <= 0.0001:
                # beitiao_price = 2.4
                beitiao_price = 2.25  # 8月1日起新合同（办公本裹背条）
            elif kuan -0.03 <= 0.0001:
                beitiao_price = 2.3  # 8月1日起新合同（办公本裹背条）
            else :
                beitiao_price = 2.25  # 8月1日起新合同（办公本裹背条）




    print('kuan',kuan)
    print('beitiao_price',beitiao_price)
    return kuan,beitiao_price

def main():
    beitiao = '30MM80克022紫背条'
    im_gongyingshang = '昆山楚宏'

    beitiaoJisuan(beitiao,im_gongyingshang)

if __name__ == '__main__':
    main()