#通过复制记本本上的内容（一排排书名）批量更名一个文件夹下的所有文件
import os
import re
import pyperclip
import easygui
import openpyxl


def  azw3ChineseName():
    choice = True
    msg = '请复制记本事上所有书名'
    choice = easygui.ccbox(msg, title='Yes or No', choices=('Yes', 'No'))
    if choice == True:
        string = pyperclip.paste()
        name = string.split('\r\n')
        names = [j.strip() for j in name if j != '']
        print(names)
    return names

def   renameAzwdir(azw3path,names):
    os.chdir(azw3path)
    azw3files = [ x for x in  os.listdir(azw3path) if x.split('.')[-1]=='azw3']
    sizes = [os.path.getsize(file) for file in azw3files ]
    size_file = dict(zip(sizes,azw3files))
    sizes.sort()
    oldnames = [size_file[size] for size in sizes ]

    if len(oldnames)==len(names):
        old_new = dict(zip(oldnames,names))
        for key,value in old_new.items():
            oldname = key
            newname = value + '.' +key.split('.')[-1]
            os.rename(oldname,newname)

    else :
        print(len(azw3files))
        print(len(names))
        print('数量不匹配，无法批量更名')


def main():
    msg = '请点选已破解azw文件夹'
    print(msg)
    azw3path = easygui.diropenbox(msg)
    names = azw3ChineseName()
    renameAzwdir(azw3path, names)


if __name__ == '__main__':
    main()




