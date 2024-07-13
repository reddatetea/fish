# _*_coding:UTF-8 _*_
# 开发团队：明日科技
# 开发人员：pc
# 文件名称：demo1.PY
# 开发工具：PyCharm

#tkinter的初使用

from tkinter import *
win=Tk()
win.title("tkinter的初级使用")     #添加窗口标题
txt=Label(win,text="\n\ngame over\n\n").pack() #在窗口中添加一行文字
win.mainloop()
