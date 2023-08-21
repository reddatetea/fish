# _*_ conding:utf-8 _*_
import re

fname = r'4.1流水账.XLs'
pattern = '\w+(\.[X|x][l|L][Ss]$)'
rep = re.compile(pattern)
mat = rep.search(fname)
print(mat)
print(mat.group(1))

