'''
原材料品名按标准格式命名，将不规范的命名通过正则表达式改为标准命名
涉及正则表达式的命名(?P<>...)
'''

import re

int_string = '55宁振双胶787*1092'

pattern = r'(?P<ke>\d{2,3})[\u4e00-\u9fa5]*(?P<leixing>双胶)(?P<cicun>(\d{3}\*\d{4})|(\d{4}\*\d{3}))'
regexp = re.compile(pattern)
'''
def rename(match_obj):
    ke = match_obj(group('ke'))+'g'
    leixing = match_obj(group('leixing'))
    cicun = match_obj(group('cicun'))
    return
'''
a = regexp.search(int_string)
print(a)
print(a.group('ke'))
print(a.group('leixing'))
print(a.group('cicun'))

newKe = a.group('ke') + 'g'
newLeixing = a.group('leixing')
newCicun = a.group('cicun')

newPinming = newKe + newLeixing + newCicun
print(newPinming)



'''
result:
<re.Match object; span=(0, 14), match='55宁振双胶787*1092'>
55
双胶
787*1092
55g双胶787*1092

'''