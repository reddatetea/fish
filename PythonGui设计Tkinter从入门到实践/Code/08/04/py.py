#  _*_ coding:utf-8 _*_
# 开发团队：明日科技
# 开发人员：Administrator
# 文件名称：demo1.py
# 开发工具：PyCharm

# Labelframe组件

def duihuan():
    txt=entry.get()
    #判断兑换码是否为空，若为空，则兑换码无效
    if len(txt)>0:
        re.config(text="兑换成功!")
    else:
        print("兑换码无效")
    re.grid(row=4,column=2)
from tkinter import *
win=Tk()
win.geometry("270x220")
#添加标签容器，并且设置标题为礼品兑换
labelframe=LabelFrame(win,text="礼品兑换",bg="#FFF5D7",padx=20,pady=10,font=14)
labelframe.grid(row=0,ipadx=10,ipady=10,column=1)
img=PhotoImage(file="cat.png")
# 添加游戏图标
Label(labelframe,image=img,bg="#FFF5D7").grid(row=1,column=2)
Label(labelframe,text="兑换码：",bg="#FFF5D7").grid(row=2,column=1,pady=10)
entry=Entry(labelframe)     #添加兑换码文本输入框
entry.grid(row=2,column=2,pady=10)
Button(labelframe,text="确认兑换",borderwidth=1,bg="#4EB1FF",command=duihuan).grid(row=3,column=2)
re=Label(labelframe,bg="#FFF5D7",font=16,fg="red")
win.mainloop()
