# _*_coding:UTF-8 _*_
# 开发团队：明日科技
# 开发人员：pc
# 开发时间：2020/3/9  9:09
# 文件名称：demo1.PY
# 开发工具：PyCharm

#tkinter的属性介绍

from tkinter import *
win=Tk()
win.title("tkinter的基本属性")     #窗口的标题
win.geometry("300x150")            #窗口的大小
win.configure(bg="yellow")        #窗口的背景颜色
win.maxsize(500,500)               #设置窗口的最大尺寸
couple="\n\n上联：足不出户一台电脑打天下\n\n下联：窝宅在家一双巧手定乾坤\n\n横批：量我风采"
txt=Label(win,text=couple,bg="yellow").pack()
win.mainloop()
