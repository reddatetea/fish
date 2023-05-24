'''
打开存储于文件中的变量
'''
# -*- conding = uft-8 -*-
import re
import  pickle
import datetime
import os

ff_phbs = pickle.load(open('C:\\Users\\asus\\dal\\扇贝编程\\ff_phb_sm.dat','rb'))
ff_prices = pickle.load(open('C:\\Users\\asus\\dal\\扇贝编程\\ff_phb_prices.dat','rb'))
ff_pics =pickle.load(open('C:\\Users\\asus\\dal\\扇贝编程\\ff_phb_pics.dat','rb'))

path = 'C:\\Users\\asus\\dal\\扇贝编程'
os.chdir(path)

ff_dic01 = {}
for i in range(100):
    ff_dic01[ff_phbs[i]]=ff_prices[i]

#print(ff_dic01)
''' 
for key,value in ff_dic01.items():
    print(key,value)
'''

ff_phbs_simple_dic = {}
for k in sorted(ff_dic01,key=ff_dic01.__getitem__):
    #print(k,ff_dic01[k])
    ff_phbs_simple_dic[k]=ff_dic01[k]
print(ff_phbs_simple_dic)


for key,value in ff_phbs_simple_dic.items():
    #print(key)
    if  '(' not in key and  '【' not in key and  '（'not in key :
        key  = key

    else :

        r = r'(?<=\().*(?=\))'
        pattern = re.compile(r)
        result0 = pattern.search(key)
        if result0 is not None:
            #print(result0)
            key = pattern.sub('', key)


        r = r'(?<=【).*(?=】)'
        pattern = re.compile(r)
        result0 = pattern.search(key)
        if result0 is not None:
            #print(result0)
            key = pattern.sub('', key)


        r = r'(?<=（).*(?!=）)'
        pattern = re.compile(r)
        result0 = pattern.search(key)
        if result0 is not None:
            #print(result0)
            key = pattern.sub('', key)

        key = key.replace('(','')
        key = key.replace('【','')
        key = key.replace('】', '')
        key = key.replace(')', '')
        key = key.replace('（','')
        key = key.replace('）','')


    print(key,value)





'''
dtrq =datetime.date.today().strftime('%Y%m%d')
f=open('付费电子书排行榜按价格排序%s.txt'%dtrq,'w',encoding='utf-8')

ff_phbs_simple_dic = {}
for k in sorted(ff_dic01,key=ff_dic01.__getitem__):
    print(k,ff_dic01[k])
    ff_phbs_simple_dic[k]=ff_dic01[k]
    f.write('{},{}\n'.format(k,ff_dic01[k]))

f.close()
print(ff_phbs_simple_dic )
'''



