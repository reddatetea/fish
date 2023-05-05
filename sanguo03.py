# *_* cording:utf-8 *_*
import os

names =['玄德','劉備','曹操','孟德','孔明','諸葛亮','呂布','張飛','翼德','雲長','關羽','趙雲','子龍','馬超','許褚','張遼','甘寧','黃忠','典韋']

fname = r'F:\a00nutstore\fishc\sanguo01.txt'
path,filename = os.path.split(fname)
os.chdir(path)

fname2 = 'sanguotongji.txt'
with open(fname2,'w',encoding='utf-8') as  tongji :
    for name in names:
        count = 0
        total = 0
        with open(fname, 'r', encoding='utf-8') as f:
            flist = list(f)
            for j in flist:
                count = j.count(name)
                total = total + count
                # print('%s\n'%j)

            message = '{}出现的次数:{} '.format(name, total) + os.linesep
            print(message)
            tongji.write(message)

os.system(fname2)



