#  _*_ coding:utf-8 _*_
# 开发团队：明日科技
# 开发人员：Administrator
# 文件名称：demo2.py
# 开发工具：PyCharm

w=10          # 蛇体由小正方形组成，w为正方形的边长
x1 = 0        # 蛇头的初始位置
y1 = 10
num=5        #初始状态的蛇右5个方块组成
step=10        #蛇移动的单元距离





# 单击上键，鼠标向上移动
def up1(event):
    for index,ch in enumerate(snake):
        ind=len(snake)-index-1
        if ind==0:    #蛇头的移动
            snake[ind].place(x=xx(snake[ind]),y=yy(snake[ind])- step)
        else:      #蛇身体的移动
            snake[ind].place(x=xx(snake[ind - 1]),y=yy(snake[ind - 1]))
# 单击下键，鼠标向下移动
def down1(event):
    for index,ch in enumerate(snake):
        ind=len(snake)-index-1
        if ind==0:
            snake[ind].place(x=xx(snake[ind]),y=yy(snake[ind])+ step)
        else:
            snake[ind].place(x=xx(snake[ind - 1]),y=yy(snake[ind - 1]))
def left1(event):     # 单击左键，鼠标向左移动
    for index,ch in enumerate(snake):
        ind=len(snake)-index-1
        if ind==0:
            snake[ind].place(x=xx(snake[ind]) - step, y=yy(snake[ind]))
        else:
            snake[ind].place(x=xx(snake[ind - 1]),y=yy(snake[ind - 1]))
def right1(event)    :# 单击右键，鼠标向右移动
    for index,ch in enumerate(snake):
        ind=len(snake)-index-1
        if ind==0:
            snake[ind].place(x=xx(snake[ind])+ step,y=yy(snake[ind]))
        else:
            snake[ind].place(x=xx(snake[ind - 1]),y=yy(snake[ind - 1]))
# 避免重复代码，通过一个xx(moudle)，和yy(moudle)方法获取指定组件的当前位置
def xx(module):
    return int(module.winfo_geometry().split("+")[1])
def yy(module):
    return int(module.winfo_geometry().split("+")[2])

# 键盘事件
from tkinter import *
win = Tk()
# 贪吃蛇
snake=[]
for i in range(num):
    item1 = Frame(width=10, height=10, bg="#86E7DD")
    snake.append(item1)
    item1.place(x=x1, y=y1+i*w)
snake[0].config(bg="#E7869D")
win.bind("<Up>",up1)    #绑定事件
win.bind("<Down>",down1)
win.bind("<Left>",left1)
win.bind("<Right>",right1)
win.mainloop()
