#  _*_ coding:utf-8 _*_
# 开发团队：明日科技
# 开发人员：Administrator
# 文件名称：demo1.py
# 开发工具：PyChar




i=0                  # Message组件的行号
def mess():
    textLeft=enc.get()   #获取文本框的内容
    global i
    # 接收的消息 ，获取的文本框中的内容
    Message(box, text=textLeft, bg="#CBEDE9",width=140).grid(row=i,column=0,sticky=W)
    # 发送的消息
    Message(box,text="你说："+textLeft, bg="#EFE2B8",width=140).grid(row=(i+1),column=2)
    i += 2     #设置行号
from tkinter import *
win=Tk()
win.geometry("300x230")                      #设置窗口大小
box=Frame(width=300,height=200)              #第一个容器，放置聊天信息
box.place(x=0,y=0)
info=Frame(width=250,height=20)              #第二个容器，放置下方文本框和按钮
info.place(x=40,y=200)
enc=Entry(info)                            #添加文本框
enc.pack(side=LEFT,fill=BOTH)
btn=Button(info,text="发送" ,command=mess).pack(side=LEFT)  #发送按钮
win.mainloop()