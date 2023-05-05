# *_* cording:utf-8 *_*
import os

names =['玄德','刘备','曹操','孟德','孔明','诸葛亮','吕布','张飞','翼德','云长','关羽','赵云','子龙','马超','许褚','张辽','甘宁','黄忠','典韦']

fname = r'F:\a00nutstore\fishc\三国演义58.txt'
path,filename = os.path.split(fname)
os.chdir(path)

fname2 = 'sanguojiantitongji.txt'
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



