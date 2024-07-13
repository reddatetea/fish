#  _*_ coding:utf-8 _*_
# 开发团队：明日科技
# 开发人员：Administrator
# 文件名称：demo1.py
# 开发工具：PyChar


# showinfo()

def mess():
    # 创建showinfoerror()会话框
    boo=askretrycancel("重试提醒","打开游戏出现错误，请选择重试或者取消")
    if boo==True:          #用户选择 重试
        mess()
    else:                  #用户选择取消
        win.quit()
from tkinter import *
from tkinter.messagebox import *
win=Tk()
win.title("警告会话框")
#创建一个按钮，单击按钮时，弹出会话框
Button(win,text="打开游戏",command=mess).pack(padx=20,pady=20)
win.mainloop()


