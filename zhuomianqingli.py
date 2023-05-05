'''
将桌面所有文件先复制到G:\backPath',然后全部删除！
'''
# _*_ conding:utf-8 _*_
import shutil
import os
import send2trash


path = r'C:\Users\Administrator\Desktop'
newpath = r'G:\backPath'

filenames = os.listdir(path)

#备份文件
for filename in filenames :
    oldfname = os.path.join(path, filename)
    newfname = os.path.join(newpath, filename)
    shutil.copyfile(oldfname,newfname)

#删除文件
for filename in filenames:
    oldfname = os.path.join(path, filename)
    send2trash.send2trash(oldfname)





