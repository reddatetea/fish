# _*_ conding:utf-8 _*_

'''
编写一个程序，用户输入开始搜索的路径，查找该路径下（包含子文件夹内）所有的视频格式文件
（要求查找mp4 rmvb, avi的格式即可），并把创建一个文件（vedioList.txt）
存放所有找到的文件的路径，程序实现如图
'''

import os
import easygui


def search_file(start_dir, target):
    os.chdir(start_dir)

    for each_file in os.listdir(os.curdir):      #获取当前工作目录os.curdir下的文件列表！
        ext = os.path.splitext(each_file)[1]     #文件列表每个文件，os.path.splitext分割为路径和文件名
        if ext in target :
            vedio_list.append(os.getcwd() + os.sep + each_file + os.linesep)  # 使用os.sep是程序更标准

             #vedio_list.append(os.getcwd() + os.sep + each_file )
        if os.path.isdir(each_file):
            search_file(each_file, target)  # 递归调用
            os.chdir(os.pardir)  # 递归调用后切记返回上一层目录

msg = '请点选要待查找的初始目录'
print(msg)
start_dir = easygui.diropenbox(msg)

program_dir = os.getcwd()

target = ['.mp4', '.avi', '.rmvb']
vedio_list = []

search_file(start_dir, target)

#f = open(program_dir + os.sep + 'vedioList.txt', 'w')
#f = open(program_dir + os.sep + 'vedioList.txt', 'w',encoding = 'utf-8')
fname = program_dir + os.sep + 'vedioList.txt'
f = open(fname, 'w',encoding = 'utf-8')

f.writelines(vedio_list)
f.close()
os.system(fname)
