'''
柔板的匹配，提取厚度、长度、宽度，计算合同单价
'''
import re

def jiaotaochicun(temp):
    string = temp.strip()
    # pattern =  r'(XR|夏天|冬天|EVA|EVA\s+)(?P<guige>16|32|48|64|80|100).*胶套.*'
    pattern = r'(XR|夏天|冬天|EVA|EVA\s+|EVA\s+DJL)(?P<guige>16|32|48|64|80|100).*胶套.*'
    regexp = re.compile(pattern)
    pipei = regexp.search(string)

    if pipei == None:
        print('没有匹配')

        guige = 0
        return guige

    else:
        guige = pipei.group('guige')

        return guige




def jisuanDanjia(im_gongyingshang,guige,temp):
    if im_gongyingshang =='钟祥市鑫众':
        dic = {16:0.68,32:0.46,48:0.34,64:0.27,80:0.21,100:0.19,0:0}
        guige = jiaotaochicun(temp)
        hehong_danjia = dic[int(guige)]
        return hehong_danjia

    elif im_gongyingshang =='浙江海悦':
        dic = {16: 0.95, 32: 0.62, 48: 0.59, 64: 0.41, 80: 0.34, 100: 0.29, 0: 0}
        dic =  {'EVA 16K150胶套': 0.92, 'EVA 16K200胶套': 0.95, 'EVA 16K80胶套': 0.91, 'EVA 32K80胶套': 0.61, 'EVA DJL100胶套': 0.29, 'EVA DJL32150胶套': 0.62, 'EVA DJL64胶套': 0.41, 'EVA DJL80胶套': 0.34}
        guige = jiaotaochicun(temp)
        hehong_danjia = dic.get(temp,0)
        # if im_gongyingshang=='钟祥市鑫众'  or im_gongyingshang=='浙江海悦':
        # hehong_danjia = dic[int(guige)]
        return  hehong_danjia
    else:                               #预留其它单位
        dic = {16: 0.68, 32: 0.46, 48: 0.34, 64: 0.27, 80: 0.21, 100: 0.19, 0: 0}
        guige = jiaotaochicun(temp)
        hehong_danjia = dic[int(guige)]
        return hehong_danjia

def main():
    temp = 'XR32K80胶套冬292*201'
    guige = jiaotaochicun(temp)
    print(guige)
    im_gongyingshangs = ['钟祥市鑫众','浙江海悦']
    for im_gongyingshang in im_gongyingshangs:
        hetong_danjia = jisuanDanjia(im_gongyingshang,guige,temp)
        print('hetongdanjia', hetong_danjia)

if __name__ == '__main__':
    main()










