#  _*_ coding:utf-8 _*_
# 开发团队：明日科技
# 开发人员：Administrator
# 文件名称：demo1.py
# 开发工具：PyCharm
# Menu菜单的综合应用   设置窗口样式

# 最大窗口尺寸
def max_win(event):
    win.geometry("600x400")
#最小窗口尺寸
def normal_win(event):
    win.geometry("300x200")
# 实现设置窗口中的文字样式
def txt():
    global val
    global font_size
    global top
    top = Toplevel(win)  #新建顶层窗口设置文字样式
    val = StringVar()
    val.set("宋体")   #初始字体
    font_family = ("宋体", "黑体", "方正舒体", "楷体", "隶书", "方正姚体")
    family = Combobox(top, textvariable=val, values=font_family)
    family.grid(row=0, column=0)
    font_size = Spinbox(top, from_=12, to=30, increment=2, width=10)  #选择字号
    font_size.grid(row=0, column=1)
    btn1 = Button(top, text="确定", command=font_set)
    btn1.grid(row=1, column=1)
def font_set():
    font1 = (val.get(), font_size.get())
    label.config(font=font1)

from tkinter import *
from tkinter.ttk import *

win = Tk()
win.geometry("300x200")
menu1 = Menu(win)  # 创建顶级菜单
menu2_1 = Menu(menu1)  # 创建第二级菜单
menu1.add_cascade(label="窗体", menu=menu2_1)  # 将第二级菜单添加到顶级菜单并设置显示的内容
menu2_1.add_command(label="最大化", accelerator="Ctrl+Up", command=lambda :max_win(""))  # 二级菜单中含有三个子菜单
menu2_1.add_command(label="中等窗口", accelerator="Ctrl+Down", command=lambda :normal_win(""))  # 二级菜单中含有三个子菜单
menu2_1.add_command(label="最小化", command=win.iconify)
menu2_1.add_separator()  # 添加分割线
menu2_1.add_command(label="关闭", command=win.quit)  # 退出游戏，关闭窗口
menu2_2 = Menu(menu1, tearoff=0)  # 创建第二个二级菜单
menu1.add_cascade(label="自定义", menu=menu2_2)  # 将第二个二级级菜单添加到顶级菜单并设置显示的内容
menu2_2.add_command(label="文字设置", command=txt)  # 添加二级菜单的子菜单
win.config(menu=menu1)


label = Label(win, text="这是一个窗口")
label.grid(row=0, column=0)
win.bind_all("<Control-Up>",max_win)
win.bind_all("<Control-Down>",normal_win)

win.mainloop()
