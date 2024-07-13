#  _*_ coding:utf-8 _*_
# 开发团队：明日科技
# 开发人员：Administrator
# 文件名称：py.py
# 开发工具：PyCharm

# Notebook选项卡组件

from tkinter import *
from tkinter.ttk import *

win = Tk()

note = Notebook(win, width=300, height=200)
pane1 = Frame()      #第一个游戏介绍内容
img1 = PhotoImage(file="pane1.png")
Label(pane1, image=img1).pack()  #第一个游戏图片
Label(pane1, text="脑洞大不大，一问便知").pack(pady=20)
Button(pane1, text="现在就玩", state="DISABLE").pack()
pane2 = Frame()                      #第二个游戏介绍内容
img2 = PhotoImage(file="pane2.png")  #第二个游戏图片
Label(pane2, image=img2).pack()
Label(pane2, text="抽象派还是形象派，你到底是哪一派").pack(pady=20)
Button(pane2, text="现在就玩", state="DISABLE").pack()

note.add(pane1, text="最强的大脑") #第一个游戏
note.add(pane2, text="水泼墨画")   #第二个游戏

note.pack()

win.mainloop()
