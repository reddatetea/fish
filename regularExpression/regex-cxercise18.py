'''
原材料品名按标准格式命名，将不规范的命名通过正则表达式改为标准命名
涉及正则表达式的命名(?P<>...)
?:...非捕获组
'''

import re

int_string = '190宁振铜版合合合1092*787'

pattern = r'(?P<ke>\d{2,3})(?:[\u4e00-\u9fa5]*)(?P<leixing>双胶|白卡|牛卡|铜版|涂布)(?:[\u4e00-\u9fa5]*)(?P<cicun>(\d{3}\*\d{4})|(\d{4}\*\d{3}))'
regexp = re.compile(pattern)
'''
def rename(match_obj):
    ke = match_obj(group('ke'))
    leixing = match_obj(group('leixing'))
    cicun = match_obj(group('cicun'))
    return
'''
a = regexp.search(int_string)
print(a)
print(a.group('ke'))
print(a.group('leixing'))
print(a.group('cicun'))

ke = a.group('ke')
leixing = a.group('leixing')
cicun = a.group('cicun')

pinming = ke +'g'+ leixing + cicun
print(pinming)

chang = re.compile('(?P<chang>\d{3,4})\*(?P<kuan>\d{3,4})').search(cicun).group('chang')
kuan = re.compile('(?P<chang>\d{3,4})\*(?P<kuan>\d{3,4})').search(cicun).group('kuan')
print(chang)
print(kuan)

print(type(ke))
print(type(chang))
print(type(kuan))



