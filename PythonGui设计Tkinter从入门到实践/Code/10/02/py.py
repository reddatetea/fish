#  _*_ coding:utf-8 _*_
# 开发团队：明日科技
# 开发人员：Administrator
# 文件名称：demo1.py
# 开发工具：PyCharm
#Menu菜单的使用   为菜单绑定事件





i = 84
# 提示
def help():
    showwarning("提醒", "第4行")
# 暂停与重新开始游戏
def game():
    boo = askyesnocancel("暂停", "是否停止本游戏，点击是，重新开始游戏，点击否暂停游戏")
    if boo == True:
        i = 0
        label.config(text=i)
    elif boo==False:
        i=84
        label.config(text=i)

#每点击错误一次，得分就减1
def wrong():
    global i
    i -= 1
    label.config(text=i)
# 找到与众不同的汉字
def suc():
    top = Toplevel(win)
    Label(top, text="恭喜，找到了\n，得分为"+str(i), fg="red").grid(row=0, column=0, padx=10, pady=10)

from tkinter import *
from tkinter.messagebox import *
win = Tk()
win.title("为游戏窗口添加菜单")
menu1 = Menu(win)  # 创建顶级菜单
# 添加工具栏
menu1.add_command(label="游戏", command=game)
menu1.add_command(label="帮助", command=help)
menu1.add_command(label="退出", command=win.quit)
win.config(menu=menu1)  # 显示菜单

for c in range(6):
    for j in range(14):
        Button(win, text="大", width=1,command=wrong).grid(row=c, column=j)
Button(win, text="女", width=1, command=suc).grid(row=3, column=3)
label = Label(win, font=14, fg="red", text=84)
label.grid(row=8, column=0, columnspan=14)
win.mainloop()
