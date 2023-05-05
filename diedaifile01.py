'''
迭代查找文件
'''
# _*_ conding:utf-8 *_*

import os
import easygui

def pathchoice():
    msg = '请点选想要批量更名的完整路径'
    title = '文件夹所在路径'
    easygui.msgbox(msg=msg, title=title)
    filePath = easygui.diropenbox(msg=msg, title=title)
    os.chdir(filePath)
    return filePath

def panduanleixing(filePath):




