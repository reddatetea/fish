# _*_coding:UTF-8 _*_
# 开发团队：明日科技
# 开发人员：pc
# 开发时间：2020/4/8  20:33
# 文件名称：demo1.PY
# 开发工具：PyCharm
# progressbar的相关方法

def rego():
    pro.stop()   #停止原进度条动画
    pro.step(5)  #设置步进值
    pro.start()  #开始加载动画

from tkinter import *
from tkinter.ttk import *

win = Tk()
win.title("灵魂画师")
# 游戏图标与名称
img = PhotoImage(file="game.png")
label=Label(win, image=img,text="灵魂画师", foreground="red", font=("华文新魏", 18),compound=BOTTOM)
label.grid(row=1, column=0, columnspan=3)
pro = Progressbar(win, mode="indeterminate", value=0, max=100, length=100)
pro.grid(row=2, column=0, columnspan=3,pady=10)
# 单击时，开始进度条动画
Button(win, text="进入游戏", command=pro.start, width=7).grid(row=4, column=0, padx=5)
#设置进度条每次递增的值，并进行加载动画
Button(win, text="游戏加速", command=rego, width=7).grid(row=4, column=1, padx=5)
# 停止进度条动画
Button(win, text="停止加载", command=pro.stop, width=7).grid(row=4, column=2, padx=5)

win.mainloop()
