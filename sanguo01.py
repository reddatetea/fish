# *_* cording:utf-8 *_*
import os
fname = r'F:\a00nutstore\fishc\sanguo02.txt'
namedic = {}
count = 0
total = 0
names =['玄德','曹操','呂布','張飛','孔明','雲長','趙雲','馬超','許褚','子龍','諸葛亮','劉備','張遼','甘寧','黃忠','典韋']
with open(fname,'r',encoding = 'utf-8') as f:
    flist =list(f)
    print(type(flist))
    print(len(flist))
    for j in flist:
        count = j.count('玄德')
        total = total + count
        #print('%s\n'%j)
print('玄德出现的次数:%s '%total)