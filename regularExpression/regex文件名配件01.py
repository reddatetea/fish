# _*_ conding:utf-8 _*_
import re

def pipeifile(guanjianzi):

    #regax = r'.*%s.*\.[x|X][l|L][s|S][x|X]?'%guanjianzi
    regax = r'.*(?P<guanjian>%s).*\.[x|X][l|L][s|S][x|X]?' % guanjianzi


    string = r'6.2.xls'

    pattern = re.compile(regax)
    mat = pattern.search(string)
    print(mat.group('guanjian'))

guanjianzi = '流水'
pipeifile(guanjianzi)

