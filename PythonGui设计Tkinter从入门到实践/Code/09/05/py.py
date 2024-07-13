#  _*_ coding:utf-8 _*_
# 开发团队：明日科技
# 开发人员：Administrator
# 文件名称：demo1.py
# 开发工具：PyChar


# showinfo()

def mess():
    # 创建showerror()会话框
    showerror("错误提醒","XX游戏请求开启摄像头权限，\n您拒绝了此项请求，导致游戏无法正常进行")
from tkinter import *
from tkinter.messagebox import *
win=Tk()
win.title("错误会话框")
#创建一个按钮，单击按钮时，弹出会话框
Button(win,text="进入游戏",command=mess).pack(padx=20,pady=20)
win.mainloop()


