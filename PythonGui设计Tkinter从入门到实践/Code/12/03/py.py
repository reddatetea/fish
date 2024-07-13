#  _*_ coding:utf-8 _*_
# 开发团队：明日科技
# 开发人员：Administrator
# 文件名称：demo1.py
# 开发工具：PyCharm
# canvas绘制矩形


def up1(event):
    # move方法实现rect向上移动两个单位
    canvas.move(rect, 0, -2)


def down1(event):
    # move方法实现rect向下移动两个单位
    canvas.move(rect, 0, 2)


def left1(event):
    # move方法实现rect向左移动两个单位
    canvas.move(rect, -2,0 )


def right1(event):
    # move方法实现rect向右移动两个单位
    canvas.move(rect, 2,0 )


from tkinter import *

win = Tk()
win.title("键盘控制矩形移动")
win.geometry("300x200")
canvas = Canvas(win, width=200, height=200, relief="solid")  # 创建画布
rect = canvas.create_rectangle(10, 10, 50, 50, fill="#C8F7F2") # 绘制矩形
canvas.pack()

win.bind("<Up>", up1)      # 绑定键盘事件
win.bind("<Down>", down1)
win.bind("<Left>", left1)
win.bind("<Right>", right1)
win.mainloop()
