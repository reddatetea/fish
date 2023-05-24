# -*- coding:utf-8 -*-
import re

#正则表达式imput_re
imput_re1 = r'^[\u4e00-\u9fa5]{2,3}'

#编绎正则表达式 re.compile(compile模式)
pattern1 = re.compile(imput_re1)

#字符串imput_str
#imput_str = '胡国华    420902198108287215  孝感市毛陈镇南大街韾都明珠四栋三单元  13797168672'

with open('abc.txt','r',encoding = 'utf-8') as f :
    for impput_str in f.readlines :
        #去除字符串中间的空格
        temp = imput_str.split()
        imput_str = ''.join(temp)

        #用编绎后的正则表达式进行匹配
res1 = re.search(pattern1,imput_str)
name = res1.group()
print(name)

imput_re2 = r'(\d{6})(\d{4})(\d{2})(\d{2})(\d{3})([0-9]|X)'
pattern2 = re.compile(imput_re2)
res2 = re.search(pattern2,imput_str)
idcard = res2.group()
print(idcard)

imput_re3 = r'[\u4e00-\u9fa5]{4,30}'
pattern3 = re.compile(imput_re3)
res3 = re.search(pattern3,imput_str)
address = res3.group()
print(address)

imput_re4 = r'1[0-9]{10}$'
pattern4 = re.compile(imput_re4)
res4 = re.search(pattern4,imput_str)
phonenumber = res4.group()
print(phonenumber)

imput_re5 = r'^[\u4e00-\u9fa5]{2,3}\s*(\d{6})(\d{4})(\d{2})(\d{2})(\d{3})([0-9]|X)\s*[\u4e00-\u9fa5]{4,30}\s*(1[0-9]{10}$)'
pattern5 = re.compile(imput_re5)
res5 = re.search(pattern5,imput_str)
print(res5)





