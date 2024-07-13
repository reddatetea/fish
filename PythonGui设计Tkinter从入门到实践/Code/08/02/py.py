#  _*_ coding:utf-8 _*_
# 开发团队：明日科技
# 开发人员：Administrator
# 文件名称：demo1.py
# 开发工具：PyCharm

# frame组件

from tkinter import *
from tkinter.ttk import *        #因为使用了ttk中的Separate分割线，所以引入ttk模块
win=Tk()
win.title("长春市轨道交通1号线")
win.configure(background="#AFEBE5")
sty1=Style()  #左侧部分的样式
sty1.configure("BW.TLabel", foreground="#fff", background="red")
sty2=Style()   #右侧部分的样式
sty2.configure("BW.TFrame", background="#AFEBE5")
win.geometry("250x200")
win.configure(bg="#AFEBE5")
# 左侧容器，显示时间以及当次车辆信息
left=Frame(win,style="BW.TLabel",width=260)
left.pack(side=LEFT)
# 左侧第一部分显示当前月份、日期和时间信息
Label(left,text="2020-03-08",background="red",foreground="#fff").pack()
Label(left,text="06:49",background="red",foreground="#fff").pack()
Label(left,text="星期一 Sun",background="red",foreground="#fff").pack()
Separator(left,orient=HORIZONTAL).pack(side=TOP,fill=X)
#左侧第二部分显示当前站的站名
Label(left,text="本站",background="red",foreground="#fff").pack(ipady=5)
Label(left,text="解放大路",background="red",foreground="#fff").pack(ipady=5)
Separator(left,orient=HORIZONTAL).pack(side=TOP,fill=X)
#左侧第三部分，显示当前车次的前进方向
Label(left,text="前进方向",background="red",foreground="#fff").pack(ipady=5)
Label(left,text="东环城路",background="red",foreground="#fff").pack(ipady=5)
#右侧容器，提醒注意安全等
right=Frame(win,width=260,style="BW.TFrame")
right.pack(side=LEFT)
Label(right,text="请排队上下车先下后上",background="#AFEBE5",justify="center",wraplength=100,font=16).pack(padx=40)
win.mainloop()
