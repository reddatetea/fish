# _*_coding:UTF-8 _*_
# 开发团队：明日科技
# 开发人员：pc
# 开发时间：2020/3/9  9:09
# 文件名称：demo1.PY
# 开发工具：PyCharm

# Widget的公共属性以及公共方法

from tkinter import *
win=Tk()
win.title("充值成功")
win.geometry("300x240")
str="1、一级VIP30天\n\n2、每天额外赠送300金币7天\n\n3、全英雄限免30天\n"
text=Label(win,text="\n充值成功!",font="Times 18 bold").pack()
text1=Label(win,text="\n恭喜获得：\n",font="16").pack(anchor=W,padx=45)
text2=Label(win,text=str,font="18",fg="red",justify="left").pack()

win.mainloop()
