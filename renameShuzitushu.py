#批量更名从数字图书馆下载的图书，将'(z-lib.org)'替抽抽换为空
import os
import easygui

def renameZlibrary(path,str0):
    os.chdir(path)
    filelists = [i for i in os.listdir(path) if os.path.isfile(i)]
    for i in filelists:
        if str0 in i:
            j = i.replace(str0, '')
            src = os.path.join(path, i)
            dsc = os.path.join(path, j)
            os.rename(src, dsc)
        else:
            continue


def main():
    str0 = r'(z-lib.org)'
    path = easygui.diropenbox('请打开要更改文件名的文件所在文件夹')
    renameZlibrary(path,str0)

if __name__== '__main__':
    main()


