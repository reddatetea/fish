#  _*_ coding:utf-8 _*_
# 开发团队：明日科技
# 开发人员：Administrator
# 文件名称：demo1.py
# 开发工具：PyCharm
# canvas拖动鼠标帮小鸟回家

from tkinter import *
from tkinter.messagebox import *
# 拖动鼠标，移动小鸟
def draw(event):
    canvas.coords(bird, event.x, event.y)
#     判断小鸟是否回家
def panduan(event):
    canvas.coords(bird, event.x, event.y)
    x1=abs(event.x-340)
    y1=abs(event.y-70)
    if x1<70 and y1<75:
        showinfo("小鸟回家","谢谢你成功帮小鸟回家")
win = Tk()
win.title("帮助小鸟回家")
win.geometry("400x320")
canvas = Canvas(win, width=400, height=320, relief="solid", bg="#E7D2BB")
bird1 = PhotoImage(file="bird.png")
house1 = PhotoImage(file="house.png")
house = canvas.create_image(340, 70, image=house1)   #绘制房子
bird = canvas.create_image(150, 250, image=bird1)    #绘制小鸟
canvas.grid(row=0, column=0, columnspan=2)
canvas.bind("<B1-Motion>", draw)    #绑定鼠标按住左键移动事件
canvas.bind("<ButtonRelease-1>",panduan)   #绑定鼠标松开左键事件
win.mainloop()
