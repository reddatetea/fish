#  _*_ coding:utf-8 _*_
# 开发团队：明日科技
# 开发人员：Administrator
# 文件名称：demo1.py
# 开发工具：PyCharm
#treeview的添加图标

from tkinter import *
from tkinter.ttk import *  # 导入内部包
win = Tk()
# 创建树菜单以及每一列的名称
tree = Treeview(win,columns=("score"))
#定义每一列的标题
tree.heading("#0",text="小组",anchor=W)
tree.heading("score",text="得分",anchor=W)
# 用字典存储各组队员的员工号以及得分
score1={"R001":"20","R002":"19","R003":"19","R004":"16"}
score2={"B001":"17","B002":"19","B003":"18","B004":"14"}
score3={"G001":"17","G002":"15","G003":"16","G004":"16"}
# 添加三黄队黄队与绿队，设置默认展开红队成员的得分
red=tree.insert("",END,text="红队",open=True)
blue=tree.insert("",END,text="蓝队")
green=tree.insert("",END,text="绿队")
# 通过遍历添加子菜单
for index,item in score1.items():
    tree.insert(red,END,text=index,values=(item))
for index,item in score2.items():
    tree.insert(blue,END,text=index,values=(item))
for index,item in score3.items():
    tree.insert(green,END,text=index,values=(item))
tree.pack()
win.mainloop()