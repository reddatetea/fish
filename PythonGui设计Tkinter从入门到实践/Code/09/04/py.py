#  _*_ coding:utf-8 _*_
# 开发团队：明日科技
# 开发人员：Administrator
# 文件名称：demo1.py
# 开发工具：PyChar


# showinfo()

def mess():
    # 创建showinfo()会话框
    showwarning("警告","您正在退出游戏，退出后，将会失去本轮游戏所有得分")
from tkinter import *
from tkinter.messagebox import *
win=Tk()
win.title("警告会话框")
#创建一个按钮，单击按钮时，弹出会话框
Button(win,text="退出游戏",command=mess).pack(padx=20,pady=20)
win.mainloop()


