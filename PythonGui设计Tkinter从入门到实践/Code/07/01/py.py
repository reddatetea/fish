# _*_coding:UTF-8 _*_
# 开发团队：明日科技
# 开发人员：pc
# 开发时间：2020/3/13  10:56
# 文件名称：demo1.PY
# 开发工具：PyCharm


# 通过bind()绑定鼠标事件时，会将鼠标的位置坐标参数传递，所以即使该功能中不需要该参数，也需要接收该参数
def show(event):
    for i in items:
        listbox.insert(END, i)   #向列表框中添加选项
    listbox.pack(fill=X)
from tkinter import *
win = Tk()
win.title("Listbox的初级使用")         #设置窗口的标题
win.geometry("180x150")                #设置窗口大小
#添加列表框
listbox = Listbox(win, bg="#FFF8DC", selectbackground="#D15FEE", selectmode="multiple", height=5, width=25)
items = ["重庆", "北京", "天津", "上海", "广州", "深圳"]    #列表存储选项
enc=Entry(win)             #添加单行文本框
enc.pack(fill=X)
# 为文本框绑定事件，当鼠标左键单击文本框时，执行show函数
enc.bind("<Button-1>",show)
win.mainloop()
