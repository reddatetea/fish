#  _*_ coding:utf-8 _*_
# 开发团队：明日科技
# 开发人员：Administrator
# 文件名称：demo1.py
# 开发工具：PyCharm


# Button：按钮控件

def show():
    #创建Label标签，在该标签中显示图片
    Label(win, image=img).pack()
from tkinter import *
win = Tk()
img = PhotoImage(file="laugth.png")    #创建图片对象
but1 = Button(win, text="添加图片", command=show).pack()   #添加按钮
win.mainloop()
