# _*_ conding:utf-8 _*_

'''
编写一个程序，用户输入开始搜索的路径，查找该路径下（包含子文件夹内）所有的指定格式文件target
，归集到一个列表中，然后将这些全部移动到一个临时文件夹中
然后将其它未找到文件全部归集到另一个临时文件夹中！
运行后，原输入的路径下只剩空文件夹
'''

import os
import datetime
import easygui
import shutil

def TempPathName():       #创建一个新的临时文件夹名称
    #当前日期
    dqrq = datetime.date.today().strftime('%Y%m%d')

    #新建文件夹名字
    temp_dir_name = dqrq + '_' + 'temp'
    no_temp_dir_name = 'no_' + dqrq + '_' + 'temp'
    return temp_dir_name,no_temp_dir_name


def search_file(path, target):
    os.chdir(path)

    for each_file in os.listdir(os.curdir):      #获取当前工作目录os.curdir下的文件列表！
        print(each_file)
        ext = os.path.splitext(each_file)[1]
        #文件列表每个文件，os.path.splitext分割为路径和文件名

        print(ext)
        if ext in target :
            #vedio_list.append(os.getcwd() + os.sep + each_file + os.linesep)  # 使用os.sep是程序更标准
            print('ok',each_file)
            xiazai_list.append(os.getcwd() + os.sep + each_file)


        if os.path.isdir(each_file):
            search_file(each_file, target)  # 递归调用
            os.chdir(os.pardir)  # 递归调用后切记返回上一层目录


def no_search_file(path, target):
    os.chdir(path)

    for each_file in os.listdir(os.curdir):      #获取当前工作目录os.curdir下的文件列表！

        if os.path.isdir(each_file):
            no_search_file(each_file, target)  # 递归调用
            os.chdir(os.pardir)  # 递归调用后切记返回上一层目录
        else :
            ext = os.path.splitext(each_file)[1]
            if ext not in target:
                # vedio_list.append(os.getcwd() + os.sep + each_file + os.linesep)  # 使用os.sep是程序更标准
                no_xiazai_list.append(os.getcwd() + os.sep + each_file)


def shangPath(path):
    os.chdir(path)
    # 上一级目录
    shang_dir = os.path.abspath(os.path.join(os.getcwd(), ".."))
    print(shang_dir)
    return shang_dir

def creatTempPath(shang_dir,temp_dir_name,no_temp_dir_name):
    os.chdir(shang_dir)
    #建临时文件夹，以存放搜索到的指定文件
    try :
        os.mkdir(temp_dir_name)
        print(temp_dir_name)

    except :
        pass

    #建临时文件夹，以存放未搜索到的指定文件
    try:
        os.mkdir(no_temp_dir_name)
        print(no_temp_dir_name)

    except:
        pass

    newpath = os.path.join(shang_dir, temp_dir_name)
    no_newpath = os.path.join(shang_dir, no_temp_dir_name)

    return  newpath,no_newpath


temp_dir_name,no_temp_dir_name= TempPathName()
msg = '请输入下载目录：'
title = '文件夹所在路径'
easygui.msgbox(msg=msg, title=title)
path = easygui.diropenbox(msg=msg, title=title)

shang_dir = shangPath(path)

newpath,no_newpath = creatTempPath(shang_dir,temp_dir_name,no_temp_dir_name)

target = ['.mp4', '.avi', '.rmvb','.mkv','mov']

xiazai_list = []
search_file(path, target)
for oldname in xiazai_list:
    dirname,filename = os.path.split(oldname)
    newname = os.path.join(newpath,filename)
    shutil.move(oldname,newname)

no_xiazai_list = []
no_search_file(path, target)
for no_oldname in no_xiazai_list:
    dirname,filename = os.path.split(no_oldname)
    newname = os.path.join(no_newpath,filename)
    shutil.move(no_oldname,newname)



