'''
本模块以供应商的简称将仓库供应商和财务供应商进行连接，将仓库供应商和财务财务商构建为一个字典
'''
# _*_conding:utf:8 _*_
import openpyxl
import cangkuGongyingshangs
import chaiwuGongyingshangs
import jianchenGongyingshangs

cangkuGongyingshangs = cangkuGongyingshangs.cangku
chaiwuGongyingshangs = chaiwuGongyingshangs.chaiwu
jianchenGongyingshangs = jianchenGongyingshangs.jianchen

#仓库供应商简称
print('仓库供应商简称')
print(jianchenGongyingshangs)
print('*'*30)

#仓库供应商
print('仓库供应商')
print(cangkuGongyingshangs)
print('*'*30)

#财务供应商
print('财务供应商')
print(chaiwuGongyingshangs)
print('*'*30)


gongyingshangduizhaobiao={}
for k,v in jianchenGongyingshangs.items():
    for chaiwuGongyingshang in chaiwuGongyingshangs:
        if v in chaiwuGongyingshang:
            gongyingshangduizhaobiao[k]=chaiwuGongyingshang

for k,v in gongyingshangduizhaobiao.items():
    print(k,'-------',v)



