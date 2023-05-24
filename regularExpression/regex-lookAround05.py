'''
去除中英文混排字符串中的空格
'''
# -*- coding = utf-8 -*-_
import re
string = '''
    寸阴虚度    
了成何事
happy   birthday 
抱竖琴独向
银蟾  影里，
此怀   难    寄                   
'''
rep = r'(?m)(?<![a-zA-Z])\s(?![a-zA-Z])'
pattern = re.compile(rep)
a = pattern.sub('',string)
print(a)

