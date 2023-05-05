'''
本模块实现文件安全批量删除

'''
# _*_ conding:utf-8 _*_
import os
import easygui
import datetime
import shutil

def choicePath():                  #点选要删除文件所在的文件夹
    msg = '请点选想要批量删除的完整路径'
    title = '文件夹所在路径'
    easygui.msgbox(msg=msg,title=title)
    path = easygui.diropenbox(msg = msg,title = title)
    return path

def shangPath(path):
    os.chdir(path)
    # 上一级目录
    shang_dir = os.path.abspath(os.path.join(os.getcwd(), ".."))
    return shang_dir

def getnames(dirnames,filenames,path):
    os.chdir(path)
    for eachfile in os.listdir(os.curdir):
        if os.path.isdir(eachfile):
            dirnames.append(os.path.join(os.getcwd(), eachfile))
            dirnames,filenames = getnames(dirnames,filenames,eachfile)
            try:
                os.chdir(os.pardir)  # 递归调用后切记返回上一层目录
            except:
                print('已搜索到电脑的根目录')
        else:
            filenames.append(os.path.join(os.getcwd(), eachfile))
    return dirnames,filenames

def creatTempPath(shang_dir):
    os.chdir(shang_dir)
    # 在当前工作目录的上一级建立新的临时文件夹，即与当前工作目录平级
    dqrq = datetime.date.today().strftime('%Y%m%d')
    # 新建两个文件夹名字
    temp_file_name01 = dqrq + '_' + 'dir' + '_' + 'temp01'  # 用于存放移动过的文件夹
    temp_file_name02 = dqrq + '_' + 'dir' + '_' + 'temp02'  # 用于存放生成新的空文件夹
    try :
        os.mkdir(temp_file_name01)
        os.mkdir(temp_file_name02)
        file_path01 = os.path.join(shang_dir, temp_file_name01)
        file_path02 = os.path.join(shang_dir, temp_file_name02)
    except :
        file_path01 = os.path.join(shang_dir,temp_file_name01)
        file_path02 = os.path.join(shang_dir, temp_file_name02)
    return  file_path01,file_path02

def creatTxts(file_path02, file_geshu):
    os.chdir(file_path02)
    # 按原文件夹下面文件个数生成许多空的txt文件
    for i in range(1,file_geshu + 1):
        geshu_xh = '%09d' % i
        newfile_name = '%s.txt' % geshu_xh
        outfile = open(newfile_name, 'w')
        outfile.close()

def renameMoveOldfile(filenames,file_path01):
    i = 1
    newnames = []
    for filename in filenames:
        xh = '%09d' % i
        path1, name = os.path.split(filename)
        newname = xh + '.txt'
        newfname = os.path.join(path1, newname)
        os.rename(filename, newfname)
        newnames.append(newname)
        shutil.move(newfname, os.path.join(file_path01, newname))
        i = i + 1
    return newnames

def delKongDir(dirnames):
    # 删除空文件夹
    i = 1
    for dirname in dirnames:
        xh = '%09d' % i
        path1, name = os.path.split(dirname)
        newname = os.path.join(path1, xh)
        os.rename(dirname, newname)
        os.rmdir(newname)
        i = i + 1

def main():
    path = choicePath()
    shang_dir = shangPath(path)
    file_path01, file_path02 = creatTempPath(shang_dir)
    dirnames = []
    filenames = []
    dirnames,filenames=getnames(dirnames,filenames,path)
    dirnames = dirnames[::-1]
    creatTxts(file_path02, len(filenames))
    newnames = renameMoveOldfile(filenames, file_path01)
    os.chdir(path)
    for j in newnames:
        shutil.copyfile(os.path.join(file_path02, j),os.path.join(file_path01, j))
    for j in newnames:
        os.remove(os.path.join(file_path01, j))
    for j in newnames:
        os.remove(os.path.join(file_path02, j))
    delKongDir(dirnames)
    os.chdir(shang_dir)
    os.rmdir(file_path01)
    os.rmdir(file_path02)
    os.rmdir(path)


if __name__ == '__main__':
    main()












