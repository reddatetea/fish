import qijianchuli
import baiyunqijian
import re
import singleCailiaoRename

pinming = '55g白云卷筒815'

#qijian(riqi)
singleCailiaoRename.singlecailiaoName(pinming)

#元组解包
a,b,c,d,e =singleCailiaoRename.singlecailiaoName(pinming)
print('a',a)
print('b',b)
print('c',c)
print('d',d)
print('e',e)





