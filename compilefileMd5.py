import os
import  sys
import  hashlib
import  easygui

def fileMd5(file):
    f = open(file,'rb')
    new_md5 = hashlib.md5()
    new_md5.update(f.read().encode(encoding='utf-8'))
    file_md5 = new_md5.hexdigest()
    f.close()
    print(file_md5)
    return file_md5

def cmp_file(f1_md5, f2_md5):

    if f1_md5==f2_md5 :
        print('f1和f2两个文件有一样的md5')
    else :
        print('f1和f2两个文件不同')


def  main():
    # msg = '请点选要比较的文件1'
    # print(msg)
    # f1 = easygui.fileopenbox(msg,title = 'f1')
    # msg = '请点选要比较的文件2'
    # print(msg)
    # f2 = easygui.fileopenbox(msg, title='f2')
    f1 = r'D:\a00nutstore\fishc\豆瓣 - 副本 (2).csv'
    f2 = r'D:\a00nutstore\fishc\豆瓣 - 副本.csv'
    f1_md5 = fileMd5(f1)
    f2_md5 = fileMd5(f2)
    cmp_file(f1_md5, f2_md5)

if  __name__ == '__main__' :
    main()

