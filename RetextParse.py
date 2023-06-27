#!/usr/bin/env python
# coding: utf-8

# In[23]:


'''以正则表达式对字符串进行清洗'''
import re

def textParse(str_doc):
    #通过正则表达式过滤掉特殊符号、标点、英文、数字等
    r1 = '[a-zA-Z0-9’!"#$%&\'()*+,-./:;<=>?@，。?★、…【】《》？“”‘’！[\\]^_`{|}~]+'
    str_doc = re.sub(rl,'',str_doc)
    #去掉字符
    str_doc = re.sub('\u3000','',str_doc)
    #去除空格
    str_doc = re.sub('\s+','',str_doc)
    #去除换行符
    str_doc = str_doc.replace('\n',' ')
    return str_doc

main():
    textParse(str_doc)
   
if __name__ == '__main__':
    x = '1我爱你1'
    print(re.sub(r1, '', x))


