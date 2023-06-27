import re

int_string = 'RL-1680-卡面'

pattern = r'(-卡面)$'

regexp = re.compile(pattern)
mat = regexp.search(int_string)
print(mat)
print(mat.group(1))

a = re.sub(mat.group(1),'卡面',int_string)
print(a)


