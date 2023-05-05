'''
对流水账进行操作
'''
# _*_ coding = uft-8 _*_
import os
import excelmessage
import liushuizhang02
import liushuizhang03

fname = excelmessage.wenjian()
excelmessage.excelMessage(fname)
dirname, fname = os.path.split(fname)
os.chdir(dirname)

if fname[-3:]=='xls':
    fname = fname + 'x'
#获取文件名
dirname, fname = os.path.split(fname)
os.chdir(dirname)

liushuizhang02.liushuiZhang02(fname)

#标准的模块间参数传递
fname = liushuizhang02.liushuiZhang02(fname)
print(fname)

liushuizhang03.liushuiZhang03(fname)
fname = liushuizhang03.liushuiZhang03(fname)
print(fname)

adddangtian02.addDangtian(fname)
print(fname)









