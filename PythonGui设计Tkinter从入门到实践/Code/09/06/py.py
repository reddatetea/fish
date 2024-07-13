#  _*_ coding:utf-8 _*_
# 开发团队：明日科技
# 开发人员：Administrator
# 文件名称：demo1.py
# 开发工具：PyChar


# showinfo()

def mess():
    # 创建askokcancel()会话框
    boo=askokcancel("关闭提醒","您正在关闭主窗口，点击确定即可关闭主窗口")
    if boo==True:
        win.quit()
from tkinter import *
from tkinter.messagebox import *
win=Tk()
win.title("关闭会话框")
#创建一个按钮，单击按钮时，弹出会话框
Button(win,text="关闭窗口",command=mess).pack(padx=20,pady=20)
win.mainloop()


