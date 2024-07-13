#  _*_ coding:utf-8 _*_
# 开发团队：明日科技
# 开发人员：Administrator
# 文件名称：demo1.py
# 开发工具：PyChar


# showinfo()

def mess():
    # 创建showinfoerror()会话框
    boo=askyesnocancel("退出提醒","您正在退出程序，点击确定即可退出程序,点击否后台运行程序，单击取消则关闭该会话框")
    if boo==True:          #用户选择 是
        win.quit()
    elif boo==False:       #用户选择否
        win.iconify()
from tkinter import *
from tkinter.messagebox import *
win=Tk()
win.title("警告会话框")
#创建一个按钮，单击按钮时，弹出会话框
Button(win,text="退出程序",command=mess).pack(padx=20,pady=20)
win.mainloop()


