# _*_coding:UTF-8 _*_
# 开发团队：明日科技
# 开发人员：pc
# 开发时间：2020/3/13  10:56
# 文件名称：demo1.PY
# 开发工具：PyCharm


# Listbox组件初级使用


def show(ele):
    listbox.pack(fill=X)
#     列表中当前选中的值，并且显示在文本框中
def typeIn(event):
    enc.delete(0,END)
    enc.insert(INSERT,listbox.get(listbox.curselection()))
from tkinter import *
win = Tk()
win.title("Listbox的初级使用")
win.geometry("180x150")
val=StringVar()
val.set("重庆 北京 天津 上海 广州 深圳")      #列表框中所有选项内容
listbox = Listbox(win, bg="#FFF8DC", selectbackground="#2C92DF", selectmode="single", height=6, width=25,listvariable=val)
enc=Entry(win)
enc.pack(fill=X)
# 为文本框绑定事件，当鼠标左键单击文本框时，执行show函数
enc.bind("<Button-1>",show)
# 为列表框绑定双击事件，当鼠标左键单击文本框时，执行show函数
listbox.bind("<Double-Button-1>",typeIn)
win.mainloop()

