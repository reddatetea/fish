# _*_ conding:utf-8 _*_
import re


def pipeifile(guanjianzi):
    regax = r'.*(?P<guanjian>%s).*\.[x|X][l|L][s|S][x|X]?' % guanjianzi

    string = r'%s.xls' % guanjianzi

    pattern = re.compile(regax)
    mat = pattern.search(string)
    return mat


guanjianzi = '入库'
mat = pipeifile(guanjianzi)

if mat:
    print(mat.group('guanjian'))

