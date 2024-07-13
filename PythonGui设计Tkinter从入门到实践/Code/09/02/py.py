#  _*_ coding:utf-8 _*_
# 开发团队：明日科技
# 开发人员：Administrator
# 文件名称：demo1.py
# 开发工具：PyChar




# 0：敬业福，1：友善福，2：爱国福，3：富强福，4：友善福
def coll():
    a=randint(0,6)
    mess.config(fg="#f00")   #若得到福卡，则文字为红色
    if a==0:
       text="恭喜获得敬业福一张"
    elif a == 1:
       text = "恭喜获得友善福一张"
    elif a == 2:
       text = "恭喜获得爱国福一张"
    elif a == 3:
       text = "恭喜获得富强福一张"
    elif a==4:
       text = "恭喜获得有善福一张"
    else:
        text="很遗憾，什么也没得到"   #若没得到福卡，则文字为黑色
        mess.config(fg="#000")
    val.set("\n"+text+"\n")
    mess.pack()
from tkinter import *
from random import *
win=Tk()
win.geometry("300x230")
win.title("集福卡")
val=StringVar()
mess=Message(win,textvariable=val,font=14,aspect=350,fg="red")   #在message中显示得到的福卡
Button(win,text="集福卡",command=coll).pack(side=TOP)
win.mainloop()