'''
正则表达式反向引用
'''

import re
'''
int_string = 'aaa'
pattern = r'^([a-z])\1\1$'
regexp = re.compile(pattern)
a = re.search(regexp,int_string)
print(a)

int_string = 'ac'
pattern = r'^([a-z])\1$'
regexp = re.compile(pattern)
a = re.search(regexp,int_string)
print(a)
'''

int_string = '<bold>text</bold>'
pattern = r'<([a-zA-Z0-9]+)(\s[^>]+)?>[\s\S]*?</\1>'
regexp = re.compile(pattern)
a = re.search(regexp,int_string)
print(a)

