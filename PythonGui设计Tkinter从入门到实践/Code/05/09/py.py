# _*_coding:UTF-8 _*_
# 开发团队：明日科技
# 开发人员：pc
# 开发时间：2020/3/9  9:09
# 文件名称：demo1.PY
# 开发工具：PyCharm

# scale()的使用
# Scale

from tkinter import *
# num=0   #设置初始值
# # 单击加号时，滑块向右移动一格，并且计算爱心暴击
def up1():
    if scale1.get() < 50:
        val = scale1.get() + 1
        scale1.set(val)
        num=val*5
        txt.config(text="爱心暴击 "+str(num))
# 单击减号时，滑块向左移动一格，并且计算爱心暴击
def down1():
    if scale1.get() > 0:
        val = scale1.get() - 1
        scale1.set(val)
        num = val * 5
        txt.config(text="爱心暴击 " + str(num))
#滑动滑块时，计算爱心暴击
def hit(widget):
    num=scale1.get()*5
    txt.config(text="爱心暴击 " + str(num))
win = Tk()
win.title("爱心暴击")
txt = Label(text="爱心暴击+0")
txt.pack(side=TOP)
btndown = Button(win, text="-", command=down1, width=2).pack(side="left")
# 设置滑块的取值范围为0-50，进步值为1,
scale1 = Scale(win, from_=0, to=50, resolution=1, orient=HORIZONTAL,showvalue=0,command=hit,troughcolor="#22EBBB")
scale1.pack(side="left")
num = Entry()
btnup = Button(win, text="+", command=up1, width=2).pack(side="left")
win.mainloop()
