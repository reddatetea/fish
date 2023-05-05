import xlwings as xw
import pandas as pd
import os
import shutil
import easygui


def fileCopy(fname):
    qian, filehouzui = os.path.splitext(fname)
    msg = '请点选要欲往路径'
    print(msg)
    newpath = easygui.diropenbox(msg, title='请选文件夹')
    msg = '请输入文件新名字'
    print(msg)
    newname = easygui.enterbox(msg, title='不用输后缀')
    newfilename = newname + filehouzui
    newfname = os.path.join(newpath, newfilename)
    shutil.copyfile(fname, newfname)
    return newfname


def main():
    msg = '请点选源文件'
    print(msg)
    fname = easygui.fileopenbox(msg, title=msg)
    fileCopy(fname)


if __name__ == '__main__':
    main()

