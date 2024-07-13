#  _*_ coding:utf-8 _*_
# 开发团队：明日科技
# 开发人员：Administrator
# 文件名称：demo3.py
# 开发工具：PyCharm
# 绑定多个事件from tkinter import *
# 实现多个按钮一键添加颜色效果


from tkinter import *
import random

# 随机生成颜色
def col():
    arr=["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
    #为保证颜色相近，color1+color2多数方块的颜色     color1+color3为与众不同的方块的颜色
    color1="#"
    for i in range(6):
        color1+=arr[random.randint(0,15)]
    return color1
# 第一部分Label组件添加颜色
def go1():
    a=col()
    for i in box1:
        i.config(bg=a)
# 第二部分Label组件添加颜色
def go2(event):
    a=col()
    for i in box2:
        i.config(bg=a)


win=Tk()
win.geometry("330x200")
box1=[]
box2=[]
# 通过循环定义多个Label组件
for i in range(8):
    for j in range(2):
        label=Label(win,width=5,height=1,relief="groove")
        label.grid(row=j,column=i)
        if (i+j)%2==0:
            box1.append(label)
        else:
            box2.append(label)
btn=Button(win,text="一键着色",command=go1)
btn.grid(row=9,column=0,columnspan=8)
btn.bind("<Button-1>",go2,add="+")    #绑定第二个事件
win.mainloop()
