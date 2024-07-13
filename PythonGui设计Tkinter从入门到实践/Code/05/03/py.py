#  _*_ coding:utf-8 _*_
# 开发团队：明日科技
# 开发人员：Administrator
# 文件名称：py.py
# 开发工具：PyCharm

from tkinter import *

win=Tk()
win.configure(bg="#EFE5D2")    #设置窗口的背景颜色
user=PhotoImage(file="user.png")     #用户名图标
psw=PhotoImage(file="psw.png")       #密码图标
Label(win,image=user,bg="#fff").grid(row=0)    #显示用户名图标
Entry(win).grid(row=0,column=1,padx=10,pady=10)  #用户名文本框
Label(win,image=psw,bg="#fff").grid(row=1)       #显示密码图标
Entry(win,show="*").grid(row=1,column=1,padx=10,pady=10)    #密码文本框，输入的内容显示为“*”
Label(win,text="确定",relief="groove").grid(row=2,columnspan=2,pady=10)
win.mainloop()