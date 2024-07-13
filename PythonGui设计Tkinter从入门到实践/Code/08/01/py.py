#  _*_ coding:utf-8 _*_
# 开发团队：明日科技
# 开发人员：Administrator
# 文件名称：demo1.py
# 开发工具：PyCharm
from tkinter import *

win = Tk()
win.geometry("360x180")
for i in range(6):
    if i % 2 == 0:
        # 第偶数个Frame的背景颜色为#b1ffbb，鼠标悬停时形状为cross
        Frame(win, bg="#B1FFBB", width=60, height=40, relief=SOLID, cursor="cross").grid(row=0, column=i,pady=10)
    else:
        # 第奇数个Frame的背景颜色为#ffd9c5，鼠标悬停时形状为plus
        Frame(win, bg="#FFD9C5", width=60, height=40, cursor="plus").grid(row=0, column=i,pady=20)
win.mainloop()


win.mainloop()