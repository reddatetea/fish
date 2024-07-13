#  _*_ coding:utf-8 _*_
# 开发团队：明日科技
# 开发人员：Administrator
# 文件名称：demo1.py
# 开发工具：PyCharm
# canvas拖动鼠标绘制图像  小猫钓鱼







from tkinter import *
from tkinter.messagebox import *
import time

x1=350   #小鱼的初始水平坐标
step=2
op=1   #控制鱼向左移动或者向右移动
bar=1  #当bar=0时，小鱼不再游动

def move1():
    global bar
    bar=1
    global  x1
    global fish
    global op
    if(x1>=350):       #如果鱼儿的坐标在最右侧，则设置鱼的移动方向为向左
        op=-1
        canvas.delete(fish)
        fish = canvas.create_image(x1, 50, image=fish1)
    if(x1<=0):        #如果鱼儿的坐标在最左侧，则鱼的移动方向为向右
        op=1
        canvas.delete(fish)
        fish = canvas.create_image(x1, 50, image=fish2)
    x1=x1+op*step
    canvas.coords(fish,(x1,50))


def move_fish():                                 #鱼儿持续游动
    while bar:
        move1()                                 #鱼儿游动
        time.sleep(0.1)                          #每隔0.1s移动一次
        win.update()                             #更新页面


def catch_fish():
    canvas.coords(cat, (150, 50))
    global bar
    bar = 0                                      #小鱼停止游动
    if abs(x1-50)<=160 and abs(x1-50)>=40:       #160和40为小猫与鱼之间的距离
        showinfo("成功钓鱼","恭喜 调到一只鱼")
    else:
        showinfo("钓鱼失败", "哇喔，钓鱼失败哦")

win = Tk()
win.title("绘制兔子")
win.geometry("400x400")
canvas = Canvas(win, width=400, height=320, relief="solid",bg="#E7D2BB")
cat1=PhotoImage(file="cat.png")
fish1=PhotoImage(file="fish.png")
fish2=PhotoImage(file="fish1.png")
fish=canvas.create_image(350,50,image=fish1)  # 绘制小鱼
cat=canvas.create_image(150,250,image=cat1)  # 绘制小猫
canvas.grid(row=0,column=0,columnspan=2)
btn=Button(win,text="开始",command=move_fish).grid(row=1,column=0)
Button(win,text="钓鱼",command=catch_fish).grid(row=1,column=1)

win.mainloop()
