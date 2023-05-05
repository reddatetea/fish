'''
已知令价lingjia0算吨价dunjia
已知吨价dunjia0算令价lingjia
已知令数ling0算吨数dun
已知吨数dun0算令数ling
'''
import os
import singleCailiaoRename

spring = '55g双胶787*1092'

lingjia0 = 559.44
dunjia0 =  6000
ling0 = 1000
dun0 = 100

cw_name,price_name,ke,chang,kuan = singleCailiaoRename.singlecailiaoName(spring)
ke = float(ke)
chang =float(chang)
kuan = float(kuan)

dunjia = round(lingjia0/(ke/1000/1000*chang/1000*kuan/1000*500),2)
lingjia = round(dunjia0*(ke/1000/1000*chang/1000*kuan/1000*500),2)
dun = round(ke/1000/1000*chang/1000*kuan/1000*500*ling0,2)
ling = round(dun0/(ke/1000/1000*chang/1000*kuan/1000*500),2)

print('该材料的标准财务名为：',cw_name)
print('该材料的克重为：',ke)
print('该材料的长为：',chang)
print('该材料的宽为：',kuan)
print('该材料的吨价为：',dunjia)
print('该材料的令价为：',lingjia)
print('该材料的吨数为：',dun)
print('该材料的令数为：',ling)




