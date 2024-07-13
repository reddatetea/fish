#  _*_ coding:utf-8 _*_
# 开发团队：明日科技
# 开发人员：Administrator
# 文件名称：demo1.py
# 开发工具：PyCharm
#treeview的基本使用

from tkinter import *
from tkinter.ttk import *  # 导入内部包
win = Tk()
# 创建树菜单以及每一列的名称

tree = Treeview(win,columns=("hero","type","operate"),show="headings",displaycolumns=(0,1,2))
#定义每一列的标题以及居中显示
tree.heading("hero",text="英雄",anchor="center")
tree.heading("type",text="类型",anchor="center")
tree.heading("operate",text="操作难易程度",anchor="center")
# 插入行数据
tree.insert("",END,values=("孙尚香","射手","5"))
tree.insert("",END,values=("孙策","战士","3"))
tree.insert("",END,values=("大乔","辅助","3"))
tree.insert("",END,values=("小乔","法师","3"))
tree.pack()
win.mainloop()