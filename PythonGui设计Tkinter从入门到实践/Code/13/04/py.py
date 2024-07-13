#  _*_ coding:utf-8 _*_
# 开发团队：明日科技
# 开发人员：Administrator
# 文件名称：demo3.py
# 开发工具：PyCharm
# 取消绑定事件
# 单击上键，鼠标向上移动

step = 5


def up1(event):
    # 如果组件贴近窗口的上边缘，则取消绑定键盘事件
    if (yy(frame) <= 0):
        win.unbind("<Up>")
    else:
        frame.place(x=xx(frame), y=yy(frame) - step)


#  单击下键，鼠标向下移动
def down1(event):
    # 如果组件贴近窗口的下边缘，则取消绑定键盘事件
    if (yy(frame) >= 160):
        win.unbind("<Down>")
    else:
        frame.place(x=xx(frame), y=yy(frame) + step)


def left1(event):  # 单击左键，鼠标向左移动
    if xx(frame) <= 0:
        win.unbind("<Left>")
    else:
        frame.place(x=xx(frame) - step, y=yy(frame))


def right1(event):  # 单击右键，鼠标向右移动
    if xx(frame) >= 260:
        win.unbind("<Right>")
    else:
        frame.place(x=xx(frame) + step, y=yy(frame))


# 避免重复代码，通过一个xx(moudle)，和yy(moudle)方法获取指定组件的当前位置
def xx(module):
    return int(module.winfo_geometry().split("+")[1])


def yy(module):
    return int(module.winfo_geometry().split("+")[2])


from tkinter import *

win = Tk()
win.geometry("300x200")
win.resizable(0, 0)

frame = Frame(width=40, height=40, bg="#E2ABE5")
frame.place(x=0, y=0)

win.bind("<Up>", up1)  # 绑定事件
win.bind("<Down>", down1)
win.bind("<Left>", left1)
win.bind("<Right>", right1)

win.mainloop()
