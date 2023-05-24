'''
原材料品名按标准格式命名，将不规范的命名通过正则表达式改为标准命名
涉及正则表达式的命名(?P<>...)
?:...非捕获组
匹配到长宽后第二次用正则匹配到长宽
'''

import re

int_string = '98g白云全木浆双胶889*1200'

pattern = r'(?P<ke>\d{2,3})g?(?:[\u4e00-\u9fa5]*)(?P<leixing>双胶|白卡|牛|铜|涂布|无碳)(?:[\u4e00-\u9fa5]*)(?P<changKuan>(\d{3}\*\d{4})|(\d{4}\*\d{3}))'
regexp = re.compile(pattern)
a = regexp.search(int_string)

#克重
ke = a.group('ke')

#类型
leixing = a.group('leixing')

#长和宽
changKuan = a.group('changKuan')

if  '牛' in leixing or  '牛卡' in leixing  or '牛皮'in leixing :
    leixing = '牛卡'
elif  '铜' in  leixing or '铜版' in leixing :
    leixing = '铜版'

elif  '无碳' in  leixing  or  '无碳复写' in  leixing  or '无碳复写纸' in  leixing :
    leixing = '无碳复写纸'

else :
    leixing = leixing

#标准命名
pinming = ke +'g'+ leixing + changKuan
print(pinming)

#长宽
chang = re.compile('(?P<chang>\d{3,4})\*(?P<kuan>\d{3,4})').search(changKuan).group('chang')
kuan = re.compile('(?P<chang>\d{3,4})\*(?P<kuan>\d{3,4})').search(changKuan).group('kuan')
print(chang)
print(kuan)


'''
if danwei = kg :
   zhongLiang = rukushuliang
else :
   zhongLiang = ke/1000*chang*kuang *500 *rukushuliang
   
卷筒纸的命名法有点不同

'''




