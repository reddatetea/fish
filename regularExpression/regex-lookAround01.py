import re
string = 'fffff123456kkkj'
r = '(?<!\d)\d+(?!\d)'
pattern = re.compile(r)
a = pattern.search(string)
print(a)

