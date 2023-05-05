import os
import time
import datetime

fname = r'F:\a00nutstore\fishc\addqita.py'
path,filename = os.path.split(fname)


os.chdir(path)
#最近访问时间
zjfwsj = os.path.getatime(fname)
print('最近访问时间',zjfwsj)

print('最近访问时间',datetime.datetime.strptime(zjfwsj,'%Y-%m-%d'))   #输出最近访问时间1318921018.0
print('文件创建时间',os.path.getctime(fname))   #输出文件创建时间
print('最近修改时间',os.path.getmtime(fname) )  #输出最近修改时间
print('以struct_time形式输出最近修改时间',time.gmtime(os.path.getmtime(fname)))   #以struct_time形式输出最近修改时间
print('文件大小',os.path.getsize(fname) )   #输出文件大小（字节为单位）
print('绝对路径',os.path.abspath(fname))    #输出绝对路径'/Volumes/Leopard/Users/Caroline/Desktop/1.mp4'
print('标准格式',os.path.normpath(fname))   #输出'/Volumes/Leopard/Users/Caroline/Desktop/1.mp4'