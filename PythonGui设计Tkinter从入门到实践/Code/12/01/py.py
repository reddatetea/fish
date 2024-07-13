#  _*_ coding:utf-8 _*_
# 开发团队：明日科技
# 开发人员：Administrator
# 文件名称：demo1.py
# 开发工具：PyCharm
# canvas

from tkinter import *
win=Tk()
win.title("创建canvas画布")
win.geometry("300x200")
canvas=Canvas(win,width=200,height=200,bg="#EFEFA3").pack()   # 创建画布
win.mainloop()