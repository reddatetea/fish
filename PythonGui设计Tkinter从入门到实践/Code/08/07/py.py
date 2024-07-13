#  _*_ coding:utf-8 _*_
# 开发团队：明日科技
# 开发人员：Administrator
# 文件名称：py.py
# 开发工具：PyCharm

# Notebook选项卡组件

from tkinter import *
from tkinter.ttk import *
win = Tk()
win.title("日期和时间")
note = Notebook(win, width=250, height=150)   #添加选项卡容器
pane1 = Frame()                               #子选项卡的容器
Button(pane1,text="更改日期时间").pack(pady=20)           #第一个选项卡的内容
pane2 = LabelFrame()
Checkbutton(pane2,text="显示此时钟",variable=StringVar()).pack(pady=20)
pane3 = Frame()
Button(pane3,text="更改设置").pack(pady=20)

note.add(pane1, text="日期和时间")     #添加第一个选项卡
note.add(pane2, text="附加时钟")           #添加第二个选项卡
note.add(pane3, text="Internet时间")   #添加第三个选项卡
note.pack()
win.mainloop()
