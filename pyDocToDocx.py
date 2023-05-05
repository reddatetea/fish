# _*_ conding = utf-8 _*_
'''
查看word文件基本信息，如果是低版的doc文件，则自动将其转化为高版本的docx
需输入完整路路径和带后缀的文件名
本版解决后缀doc大小写混写
'''
import win32com.client as wc
import os
import re
import easygui

def wenjian():
    msg ='请点选文件:'
    print(msg)
    fname = easygui.fileopenbox(msg,title='file')
    return fname

def wordMessage(fname):
    pattern = '\w+(\.[D|d][O|o][Cc]$)'
    rep = re.compile(pattern)
    mat = rep.search(fname)
    if mat != None :
        fname = docToDocx(fname)
    else:
        fname = fname
    return fname

def docToDocx(fname):
    print('正将word低版本doc转化为高版本docx，请稍等:')
    # 更换工作目录为当前文件所在文件夹
    path, filename = os.path.split(fname)
    os.chdir(path)
    newname = fname + 'x'
    word = wc.Dispatch('Word.Application')
    doc = word.Documents.Open(fname)  # 目标路径下的文件
    doc.SaveAs(newname, 12, False, "", True, "", False, False, False, False)  # 转化后路径下的文件
    doc.Close()
    word.Quit()
    return newname

def main():
    fname =wenjian()
    print(fname)
    fname = wordMessage(fname)

if __name__=='__main__':
    main()

