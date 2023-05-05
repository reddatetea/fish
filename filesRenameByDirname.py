'''
将一个文件夹下子文件夹的所有文件前加子文件夹名的前缀
'''
import os
import easygui


def renameFiles(start_dir):
    dir_list = os.listdir(start_dir)
    print(dir_list)
    path,filename = os.path.split(start_dir)
    print('path', path)
    print('filename',filename)
    os.chdir(start_dir)
    for each_file in dir_list:      #获取当前工作目录os.curdir下的文件列表！
        print(each_file)
        if  os.path.isfile(each_file):
            # file_list = []
            oldfilename = os.getcwd() + os.sep + each_file
            print('oldfilename',oldfilename)
            newname = os.getcwd() + os.sep + filename + '_' + each_file
            print('newname',newname)
            os.rename(oldfilename,newname)

        else:
            renameFiles(each_file)  # 递归调用
            try :
                os.chdir(os.pardir)  # 递归调用后切记返回上一层目录
            except:
                print('已搜索到电脑的根目录')


def main():
    msg = '请点选文件夹'
    start_dir = easygui.diropenbox(msg,title='请点选文件夹 ')
    # keyname = input('请输入文件名\n')
    # fname =  '%s.txt' % keyname
    renameFiles(start_dir)


if __name__ == '__main__':
    main()