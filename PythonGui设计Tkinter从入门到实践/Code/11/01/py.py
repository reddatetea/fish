# _*_coding:UTF-8 _*_
# 开发团队：明日科技
# 开发人员：pc
# 开发时间：2020/4/8  20:33
# 文件名称：demo1.PY
# 开发工具：PyCharm
# progressbar的相关方法
# 吃了几分饱

from tkinter import *
from tkinter.ttk import *

val = 0
def add1(c):
    global val
    val += c
    # 判断进度条的当前值是否到达最大值
    if val > pro["max"]:
        label.config(text="我吃饱了")
    else:
        vari.set(val)
win = Tk()
win.geometry("220x190")
Label(win, text="投食：").grid(row=0, column=0, columnspan=1)
# 选择投食大鱼或者小鱼，大鱼增加2点，小鱼增加1点
Button(win, text="大鱼", command=lambda: add1(1)).grid(row=0, column=1,  pady=10)
Button(win, text="小鱼", command=lambda: add1(2)).grid(row=0, column=2, pady=10)
img=PhotoImage(file="cat.png")          #  小猫
label=Label(win,image=img,compound=TOP,foreground="red")
label.grid(row=1, column=0, columnspan=4)
vari=IntVar()  #绑定到进度条的当前值
vari.set(0)
# 进度条显示小猫饱腹程度
pro = Progressbar(win, mode="determinate", variable=vari, max=50, length=200)
pro.grid(row=2, column=0, columnspan=4, pady=5)
win.mainloop()
