# _*_coding:UTF-8 _*_
# 开发团队：明日科技
# 开发人员：pc
# 开发时间：2020/4/8  20:33
# 文件名称：demo1.PY
# 开发工具：PyCharm
# progressbar的相关方法


from tkinter import *
from tkinter.ttk import *
win = Tk()
win.title("灵魂画师")
win.geometry("250x230")
# 添加游戏名称并应用样式
img = PhotoImage(file="game.png")
Label(win,image=img,text="灵魂画师",foreground="red",font=("华文新魏", 18),compound=BOTTOM).pack(pady=5)
pro = Progressbar(win, mode="indeterminate", value=0, max=100, length=200)
pro.pack(pady=10)
Button(win, text="进入游戏", command=pro.start(40), width=7).pack()
win.mainloop()
