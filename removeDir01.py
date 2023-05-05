'''
将特定后缀的文件，连同它上面的文件夹一起移动到新的指定文件夹
'''
import os
import easygui
import shutil

def moveDir(start_dir,file_suffixs,newdir):
    path, filename = os.path.split(start_dir)
    os.chdir(start_dir)

    for each_file in os.listdir(start_dir):  # 获取当前工作目录os.curdir下的文件列表！
        print(each_file)
        if os.path.isfile(each_file):
            if os.path.splitext(each_file)[-1] in file_suffixs:
                print(each_file)
                oldname = os.getcwd() + os.sep + each_file
                print(oldname)
                newname = os.path.join(newdir, each_file)
                print(newname)
                shutil.move(oldname, os.path.join(newdir, each_file))
            else :
                continue

        else:
            print('ffff', each_file)
            moveDir(os.getcwd() + os.sep + each_file, file_suffixs, newdir)  # 递归调用
            try:
                os.chdir(os.pardir)  # 递归调用后切记返回上一层目录
            except:
                print('已搜索到电脑的根目录')
            continue



def main():
    msg = '请点选开始文件夹'
    print(msg)
    start_dir = easygui.diropenbox(msg)
    suffix = set()
    for root, dirs, files in os.walk(start_dir):
        for file in files:
            print(os.path.join(root, file))
            suffix.add( os.path.splitext(file)[-1])
    suffixs = list(suffix)
    suffixs.sort()
    print(suffixs)
    msg = '请点选要处理的后缀'
    file_suffixs = easygui.multchoicebox(msg,choices=suffixs)
    print(file_suffixs)
    msg = '请点选目标文件夹'
    print(msg)
    newdir = easygui.diropenbox(msg)
    print(newdir)
    moveDir(start_dir,file_suffixs, newdir)
if __name__ == '__main__':
    main()