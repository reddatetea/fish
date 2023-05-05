'''
将转换后的电子书复制到指定路径下
'''
import os
import easygui
import shutil

def searchfile_path(ebooks,start_dir, target):
    os.chdir(start_dir)
    for each_file in os.listdir(os.curdir):      #获取当前工作目录os.curdir下的文件列表！
        ext = os.path.splitext(each_file)[1].lower()     #文件列表每个文件，os.path.splitext分割为路径和文件名
        if ext in target :
            ebooks.add((os.getcwd() + os.sep + each_file))  # 使用os.sep是程序更标准
        if os.path.isdir(each_file):
            searchfile_path(ebooks,each_file, target)  # 递归调用
            os.chdir(os.pardir)  # 递归调用后切记返回上一层目录

def copysFiles(ebooks,target_dir,txt_path = r'F:\a00nutstore\dianzhishu'):
    for each_file in ebooks:
        ext = os.path.splitext(each_file)[1]
        qian,hou = os.path.split(each_file)
        if ext == '.txt':
            shutil.copy(each_file,os.path.join(txt_path,hou))
        else :
            shutil.copy(each_file, os.path.join(target_dir, hou))

def main():
    start_dir = easygui.diropenbox('请点选源目录')
    target = ['.mobi', '.azw3', '.epub', '.txt','.pdf']
    ebooks = set()
    searchfile_path(ebooks,start_dir, target)
    target_dir = easygui.diropenbox('请点选目标目录')
    copysFiles(ebooks,target_dir,txt_path = r'F:\a00nutstore\dianzhishu')
    # 复制后,删除源目录下所有文件夹及文件
    for each_dir in os.listdir(start_dir):
        shutil.rmtree(each_dir)

if __name__ == '__main__':
    main()

