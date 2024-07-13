# _*_coding:UTF-8 _*_
# 开发团队：明日科技
# 开发人员：pc
# 开发时间：2020/3/9  9:09
# 文件名称：demo1.PY
# 开发工具：PyCharm

# Combobox


from tkinter import *
from tkinter.ttk import *

# 根据月份设置每月的天数
def getMon(a):
    items = monOption.get()
    # 当月份为4、6、9、11月时，日期为30天
    if items == "4" or items == "6" or items == "9" or items == "11":
        b = tuple(range(1, 31))
    elif items == "2":    # 当月份为2月时，日期为28天
        b = tuple(range(1, 29))
    else:       # 其余月份日期为31天
        b = tuple(range(1, 32))
    dateOption["values"] = b

# 获取日期以及事项，并列句在下方标签中
def getDate():
    info = label3.cget("text")
    temp = monOption.get() + "月" + dateOption.get() + "日：\t" + text.get("0.0", END)
    label3.config(text=info + temp)
    text.delete("0.0", END)


win = Tk()
win.title("添加日程")

number = StringVar()
# 日期1~12月
a = tuple(range(1, 13))                   #月份元组
monOption = Combobox(win, width=5, textvariable=number, values=a)
monOption.current(0)       #设置默认选中1月份
monOption.grid(row=1,column=0,sticky="E",columnspan=2)
# 为Combobox组件绑定事件，当进行选择时，触发事件
monOption.bind("<<ComboboxSelected>>", getMon)   #当月份选择改变时，触发getMon()事件
label1 = Label(win, text="月").grid(row=1, column=2, sticky=W)
#默认每月的天数为31天
b = tuple(range(1, 32))     #日期元组
dateOption = Combobox(win, width=5, values=b)   #日期选择组合框
dateOption.grid(row=1, column=3, pady=10,columnspan=2)
dateOption.current(0)  #默认选中日期为1号
label2 = Label(win, text="日").grid(row=1, column=5, sticky="w")
text = Text(win, width=40, height=10)    #添加事项的文本域
text.grid(row=2, columnspan=8)
button = Button(win, text="确定", command=getDate).grid(row=3,columnspan=8)

label3 = Label(win )                 # 显示日程的标签
label3.grid(row=4, columnspan=8)
win.mainloop()
