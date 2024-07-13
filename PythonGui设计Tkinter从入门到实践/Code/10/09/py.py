#  _*_ coding:utf-8 _*_
# 开发团队：明日科技
# 开发人员：Administrator
# 文件名称：demo1.py
# 开发工具：PyCharm
# treeview的基本使用
from tkinter import *
from tkinter.ttk import *


# 选择月份后，对应的日期选择列表发生变化，防止出现类似2月30号这样错误
def setdat(a):
    temp = monsel.get()
    if temp == 2:
        dat["value"] = tuple(range(1, 29))
    elif temp == 4 or temp == 6 or temp == 9 or temp == 11:
        dat["value"] = tuple(range(1, 31))
    else:
        dat["value"] = tuple(range(1, 32))


# 添加以及修改表格
def get1():
    if len(entry.get()) == 0:  # 判断文本框的内容是否为空
        return False
    else:
        h = str(horsel.get()) if horsel.get() > 10 else "0" + str(horsel.get())  # 将时间格式化为两位数
        m = str(minsel.get()) if minsel.get() > 10 else "0" + str(minsel.get())
        item1 = (str(mon.get()) + "月" + str(datsel.get()) + "日", h + ":" + m, entry.get())
        if not tree.focus() == "":  # 判断是否有菜单项被选中
            # 在获取焦点的菜单项的位置添加新的菜单，并且删除原来的菜单项
            tree.insert("", tree.index(tree.focus()), values=item1)
            del1()
        else:
            tree.insert("", END, values=item1)
        reset1()


def del1():
    # 单击删除按钮时，删除获取焦点的菜单
    if tree.focus() == "":
        return False
    else:
        tree.delete(tree.focus())


# 将菜单项中的内容获取赋值到表单中对应的文本组件中
def edt(a):
    temp = tree.set(tree.focus())
    d = temp["date"].split("月")  # 日期以"月"字分割
    t = temp["time"].split(":")  # 时间以"："字分割
    monsel.set(int(d[0]))        #获取的月份赋值到月份选择列表中
    datsel.set(int(d[1].split("日")[0]))  #获取的日期赋值到日期选择列表中
    horsel.set(int(t[0]))          #获取的小时赋值到时间的第一个选择列表中
    minsel.set(int(t[1]))           #获取的分钟赋值到时间的第二个选择列表中
    entry.delete(0, END)
    entry.insert(INSERT,temp["depart"])

# 初始化表单
def reset1():
    monsel.set(1)
    datsel.set(1)
    horsel.set(0)
    minsel.set(0)
    entry.delete(0, END)


win = Tk()
# 输入内容
frame = Frame()
frame.grid()
Label(frame, text="日期：").grid(row=0, column=0,pady=5)
monsel = IntVar()  # 绑定月份选项
monsel.set(1)
mon = Combobox(frame, value=tuple(range(1, 13)), textvariable=monsel, width=5)  # 月
mon.grid(row=0, column=1)
mon.bind("<<ComboboxSelected>>", setdat)  # 月份选项发生变化时，对应日期也变化
Label(frame, text="-").grid(row=0, column=2)
datsel = IntVar()  # 绑定日期选项
datsel.set(1)
dat = Combobox(frame, value=tuple(range(1, 32)), textvariable=datsel, width=5)  # 日
dat.grid(row=0, column=3)
Label(frame, text="时间：").grid(row=0, column=4, columnspan=2, sticky=S + E)
horsel = IntVar()  # 绑定时间选项
horsel.set(0)
hor = Spinbox(frame, from_=0, to=24, width=5, textvariable=horsel)  # 时
hor.grid(row=0, column=6)
Label(frame, text=":").grid(row=0, column=7)
minsel = IntVar()
minsel.set(0)  # 绑定分钟选项
min = Spinbox(frame, from_=0, to=59, width=5, textvariable=minsel)  # 分
min.grid(row=0, column=8)
Label(frame, text="出发地：").grid(row=0, column=9)  # 出发地
entry = Entry(frame)
entry.grid(row=0, column=10)
Button(frame, text="确定", command=get1).grid(row=0, column=11)
Button(frame, text="删除", command=del1).grid(row=0, column=12)

# 创建Treeview组件
tree = Treeview(win, column=("date", "time", "depart"), show="headings")
tree.heading("date", text="日期")  # 设置每列的标题
tree.heading("time", text="时间")
tree.heading("depart", text="出发地")
tree.grid(row=1, column=0,pady=5)
tree.bind("<<TreeviewSelect>>", edt)  # 当选项发生变化时，调用edt函数
win.mainloop()
