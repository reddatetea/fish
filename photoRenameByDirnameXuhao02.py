'''
将一个文件夹下子文件夹的所有照片前加子文件夹名的前缀,文件名中间是照片创建日期，文件名尾自动加序号
'''
import os
import easygui
import time
import datetime
import photoTime


def renameFiles(start_dir):
    fileList = sortFile(start_dir)
    path,filename = os.path.split(start_dir)
    os.chdir(start_dir)
    xlh = ''
    i = 0
    for each_file in fileList :      #获取当前工作目录os.curdir下的文件列表！
        print(each_file)
        i = i +1
        if  os.path.isfile(each_file):
            xlh = '%03d'%(i)
            #dqrq = datetime.date.today().strftime('%Y%m%d')                             #当前日期
            # statinfo = os.stat(each_file)
            # createTimeStrimng = time.strftime('%Y%m%d%H%M%S', time.localtime(statinfo.st_mtime))
            paishe_time = photoTime.getExif(each_file)
            oldfilename = os.getcwd() + os.sep + each_file
            print('oldfilename',oldfilename)
            newname = os.getcwd() + os.sep + filename + '_' + paishe_time + '_'  + xlh + os.path.splitext(each_file)[-1]
            # newname = os.getcwd() + os.sep + filename + '_' + createTimeStrimng + '_' + xlh + os.path.splitext(each_file)[-1]
            print('newname',newname)
            os.rename(oldfilename,newname)

        else:
            renameFiles(each_file)  # 递归调用
            try :
                os.chdir(os.pardir)  # 递归调用后切记返回上一层目录
            except:
                print('已搜索到电脑的根目录')

def sortFile(filePath):
    # dir_list = []
    # for file in os.listdir(filePath):
    #     if  os.path.isfile(file):
    #         dir_list.append(file)
    #     else :
    #         continue
    dir_list = os.listdir(filePath)
    # paishe_time = photoTime.getExif(each_file)      #照片的拍摄时间
    # fileList = sorted(dir_list, key=lambda x: os.path.getmtime(os.path.join(filePath, x)))   #按gettime排序，lambda的用法？这是x?
    fileList = sorted(dir_list, key=lambda x: photoTime.getExif(os.path.join(filePath, x)))  # 按拍摄时间排序，速度较慢
    return fileList


def main():
    msg = '请点选文件夹'
    start_dir = easygui.diropenbox(msg,title='请点选文件夹 ')
    # keyname = input('请输入文件名\n')
    # fname =  '%s.txt' % keyname
    renameFiles(start_dir)


if __name__ == '__main__':
    main()