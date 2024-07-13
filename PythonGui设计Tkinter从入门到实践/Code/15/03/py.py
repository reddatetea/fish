#  _*_ coding:utf-8 _*_
# 开发团队：明日科技
# 开发人员：Administrator
# 文件名称：py.py
# 开发工具：PyCharm
# python文件夹操作

from tkinter import *
import os,time
def show1():
    a=os.stat("test.txt")
    text.insert(INSERT,"文件大小:"+str(a.st_size)+"字节")
    text.insert(INSERT, "\n\n文件路径:" + os.path.abspath("test.txt"))
    text.insert(INSERT, "\n\n最后访问时间:" + time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(a.st_atime)))
    text.insert(INSERT, "\n\n最后修改:" + time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(a.st_mtime)))
win=Tk()
Button(win,text="显示信息",command=show1).pack(pady=10)
text=Text(win,font=14,width=60,height=8)
text.pack(padx=10)
win.mainloop()
