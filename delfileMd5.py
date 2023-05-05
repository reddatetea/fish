# -*- coding:utf-8 -*-
import os
import hashlib
import time
import sys
import  easygui
import  send2trash


# 搞到文件的MD5
def get_ms5(filename):
    m = hashlib.md5()
    mfile = open(filename, "rb")
    m.update(mfile.read())
    mfile.close()
    md5_value = m.hexdigest()
    return md5_value

# 搞到文件的列表
def get_recursion_file(path):
    recursion_list = []
    for dirpath, dirnames, filenames in os.walk(path):
        for filename in filenames:
            recursion_list.append(os.path.join(dirpath, filename))
            print(os.path.join(dirpath, filename))
    return recursion_list

def get_urllist():
    msg = '请点选欲删除重复文件的路径'
    base = easygui.diropenbox(msg,title ='路径')
    #base = r'F:\img\\'
    list = get_recursion_file(base)
    return list
# 主函数
if __name__ == '__main__':
    md5list = []
    urllist = get_urllist()
    print("test1")
    with open('delfilelist.txt','w',encoding='utf-8') as f:

        for a in urllist:
            md5 = get_ms5(a)
            if (md5 in md5list):
                #os.remove(a)                                         #直接删除！慎用！
                send2trash.send2trash(a)                     #先删除到回收站，比较安全！
                f.write(a+os.linesep)
                print("重复：%s" % a)
            else:
                md5list.append(md5)

    os.system('delfilelist.txt')                              #打开已删除文件的列表，查看删除了多少文件