#  _*_ coding:utf-8 _*_
# 开发团队：明日科技
# 开发人员：Administrator
# 文件名称：demo1.py
# 开发工具：PyChar


# showinfo()

def mess():
    # 创建showinfo()会话框
    showinfo("welcome！","好久不见，欢迎回归")
from tkinter import *
from tkinter.messagebox import *
win=Tk()
win.title("会话框")
#创建一个按钮，单击按钮时，弹出会话框
Button(win,text="进入游戏",command=mess).pack(padx=20,pady=20)
win.mainloop()


