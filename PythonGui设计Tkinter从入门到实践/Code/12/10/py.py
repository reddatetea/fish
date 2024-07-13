#  _*_ coding:utf-8 _*_
# 开发团队：明日科技
# 开发人员：Administrator
# 文件名称：demo11.py
# 开发工具：PyCharm


#拖动鼠标绘制图形

def draw(event):
    global text1
    # 鼠标绘制图形
    text1=canvas.create_oval(event.x,event.y,event.x+10,event.y+10,fill="green",outline="")
def delete1():
    canvas.delete("all")       # 删除画布上所有元素
    can()                      # 初始化画布
from tkinter import *
win=Tk()
win.title("书法秀")
win.geometry("420x420")
canvas = Canvas(win, width=400, height=400, bg="#F1E9D0", relief="solid")
def can():
    rect=canvas.create_rectangle(4,4,400,385,outline="red",width=2)
    line1=canvas.create_line(2,198,400,198,dash=(2,2),fill="red")
    line2=canvas.create_line(198,2,198,400,dash=(2,2),fill="red")
    line3=canvas.create_line(0,0,400,400,dash=(2,2),fill="red")
    line4=canvas.create_line(0,400,400,0,dash=(2,2),fill="red")
    canvas.pack(side="bottom")
    canvas.bind("<B1-Motion>",draw)
Button(win,text="清屏",command=delete1).pack(side="bottom")
can()
win.mainloop()
