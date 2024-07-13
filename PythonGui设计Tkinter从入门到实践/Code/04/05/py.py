# _*_coding:UTF-8 _*_
# 开发团队：明日科技
# 开发人员：pc
# 开发时间：2020/3/9  9:09
# 文件名称：demo1.PY
# 开发工具：PyCharm

# anchor   设置空间在窗口中的位置

from tkinter import *
win=Tk()                      #创建根窗口
win.geometry("350x150")       #设置窗口大小
win.title("tkinter的初使用")  #设置窗口标题
txt1=Label(win,text="确定退出本窗口吗？")
txt2=Label(win,text="果断退出",bg="#c1ffc1")
txt3=Label(win,text="我再想想",bg="#cdb5cd")
txt1.pack(fill="x",pady="20")      #fill='x'设置组件始终水平居中显示
# side和anchor组合实现组件有窗口右下角显示
txt2.pack(side="right",padx="10",ipadx="6",pady="20",anchor="se")
txt3.pack(side="right",padx="10",ipadx="6",pady="20",anchor="se")
win.mainloop()

