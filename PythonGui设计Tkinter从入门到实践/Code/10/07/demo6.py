#  _*_ coding:utf-8 _*_
# 开发团队：明日科技
# 开发人员：Administrator
# 文件名称：demo6.py
# 开发工具：PyCharm
from tkinter import *
from tkinter.ttk import *

win = Tk()
tree = Treeview(win, columns=("date", "temperature"))
tree.heading("#0", text="天气")  # 设置图标栏的标题
tree.heading("date", text="日期")
tree.heading("temperature", text="气温")
rain = PhotoImage(file="rainheardly.png")  # 定义图标
storm = PhotoImage(file="storm.png")
sunny = PhotoImage(file="sunny.png")
tree.insert("", END, values=("4月1日", "-3~5"), image=rain, text=" 中到暴雨")  # 添加子项目
tree.insert("", END, values=("4月2日", "-3~7"), image=sunny, text=" 晴")
tree.insert("", END, values=("4月3日", "0~8"), image=storm, text=" 雷阵雨")
tree.insert("", END, values=("4月4日", "1~10"), image=sunny, text=" 晴")
tree.insert("", END, values=("4月5日", "2~10"), image=sunny, text=" 晴")
tree.insert("", END, values=("4月6日", "2~12"), image=sunny, text=" 晴")
tree.insert("", END, values=("4月7日", "2~10"), image=rain, text=" 晴")
tree.pack()
win.mainloop()
