'''
本模块实现文件名的批量更名
文件夹一层结构
使用essygui,等待用户输入文件起始name，方式，选择当前日期还是照片创建日期
运行时出现这个提示'FileNotFoundError: [WinError 2] 系统找不到指定的文件',但不影响运行！
'''
# _*_ conding:utf-8 _*_

import os
import easygui
import time
import datetime
#
# msg = '请点选想要批量更名的完整路径'
# title = '文件夹所在路径'
# easygui.msgbox(msg=msg,title=title)
# filePath = easygui.diropenbox(msg = msg,title = title)
# os.chdir(filePath)
#
# #当前日期
# dqrq = datetime.date.today().strftime('%Y%m%d')
#
#
# msg = "请填写文件更名信息"
# title = "文件更名"
# renameList = ["文件名前缀",'地点',"方式"]
#
# fieldValues = easygui.multenterbox(msg,title,renameList)
#
# name = fieldValues[0]
# place =fieldValues[1]
# way = fieldValues[2]
#
# #序列号
# xlh = ''
#
# def totalRename(filePath):
#     sortFile(filePath)
#     renameFile(filePath)
#
# def sortFile(filePath):
#     dir_list = os.listdir(filePath)
#     fileList = sorted(dir_list, key=lambda x: os.path.getmtime(os.path.join(filePath, x)))   #按gettime排序，lambda的用法？这是x?
#     return fileList
#
# def renameFile(filePath):
#     os.chdir(filePath)
#     fileList = sortFile(filePath)
#     print(fileList)
#     #print(fileList)
#     for filename in fileList:
#         for i in range(len(fileList)):
#             xlh = '%02d'%(i+27)
#             print(xlh)
#             filename = fileList[i]
#             print(filename)
#             oldname = os.path.join(filePath,fileList[i])
#
#             #statinfo=os.stat(os.path.join(filePath,filename))
#             #statinfo=os.stat(os.path.join(filePath,fileList[i]))
#             #createTimeStrimng = time.strftime('%Y%m%d%H%M%S',time.localtime(statinfo.st_mtime))
#
#             abc = name+place+xlh+' '+way+os.path.splitext(filename)[-1]
#             #print(abc)
#             newname = os.path.join(filePath,abc)
#
#             os.rename(oldname,newname)
#
#
# totalRename(filePath)

dqrq = datetime.date.today().strftime('%Y%m%d')
print(dqrq)

