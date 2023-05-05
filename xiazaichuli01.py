# _*_ conding:utf-8 _*_

'''
编写一个程序，用户输入开始搜索的路径，查找该路径下（包含子文件夹内）所有的视频格式文件
（要求查找mp4 rmvb, avi的格式即可），归集到一个列表中，然后将这些视频文件全部移动到一个临时文件夹中

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
    return temp_dir_name


def search_file(path, target):
    os.chdir(path)
    #global xiazai_list

    for each_file in os.listdir(os.curdir):      #获取当前工作目录os.curdir下的文件列表！
        print(each_file)
        ext = os.path.splitext(each_file)[1]     #文件列表每个文件，os.path.splitext分割为路径和文件名
        print(ext)
        if ext in target :
            #vedio_list.append(os.getcwd() + os.sep + each_file + os.linesep)  # 使用os.sep是程序更标准
            print('ok',each_file)
            xiazai_list.append(os.getcwd() + os.sep + each_file)

            #vedio_list.append(os.getcwd() + os.sep + each_file )
        if os.path.isdir(each_file):
            search_file(each_file, target)  # 递归调用
            os.chdir(os.pardir)  # 递归调用后切记返回上一层目录


def shangPath(path):
    os.chdir(path)
    # 上一级目录
    shang_dir = os.path.abspath(os.path.join(os.getcwd(), ".."))
    print(shang_dir)
    return shang_dir

def creatTempPath(shang_dir,temp_dir_name):
    os.chdir(shang_dir)
    # 在当前工作目录的上一级建立新的临时文件夹，即与当前工作目录平级
    try :
        os.mkdir(temp_dir_name)
        print(temp_dir_name)
    except :
        pass
    newpath = os.path.join(shang_dir, temp_dir_name)
    print(newpath)
    os.chdir(newpath)
    return newpath


def main():
    global xiazai_list    #main里的变量不属于全局变量！
    temp_dir_name = TempPathName()
    msg = '请输入下载目录：'
    title = '文件夹所在路径'
    easygui.msgbox(msg=msg, title=title)
    path = easygui.diropenbox(msg=msg, title=title)

    shang_dir = shangPath(path)

    newpath = creatTempPath(shang_dir,temp_dir_name)

    target = ['.mp4', '.avi', '.rmvb','.mkv']

    xiazai_list = []

    search_file(path, target)


    for oldname in xiazai_list:
        dirname,filename = os.path.split(oldname)
        newname = os.path.join(newpath,filename)
        shutil.move(oldname,newname)

if __name__ == '__main__':
    main()





