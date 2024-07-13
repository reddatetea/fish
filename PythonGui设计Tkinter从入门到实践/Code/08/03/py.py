#  _*_ coding:utf-8 _*_
# 开发团队：明日科技
# 开发人员：Administrator
# 开发时间：2020/3/16 10:26
# 文件名称：demo1.py
# 开发工具：PyCharm

# frame组件,在frame中添加组件

# 全选
def all():
#通过for 循环设置每一个复选框的状态为选中
    for index,item in enumerate(checkbox):
        item.set(True)
# 全不选
def none():
    # 通过for 循环设置每一个复选框的状态为不选中
    for index,item in enumerate(checkbox):
        item.set(False)
# 反选
def inverse():
    #逐一判断复选框是否选中，如果选中，则取消选中，反之则选中
    for index,item in enumerate(checkbox):
        if item.get()==False:
            item.set(True)
        else:
            item.set(False)

from tkinter import *
win=Tk()

frame1=Frame(win,width=200,height=50)# 第一个容器，放置单选按钮
frame1.grid(row=0,column=0)
frame2=Frame()         # 第二个容器，放置复选框
frame2.grid(row=1,column=0)
val=BooleanVar()
val.set(1)
# 单选按钮
radio1=Radiobutton(frame1,value=0,variable=val,text="全选",command=all)
radio1.grid(row=0,column=0)
radio2=Radiobutton(frame1,value=1,variable=val,text="全不选",command=none)
radio2.grid(row=0,column=1)
radio3=Radiobutton(frame1,value=2,variable=val,text="反选",command=inverse)
radio3.grid(row=0,column=3)
# 选项
fruits=["苹果","香蕉","苹果","草莓","柠檬"]
checkbox=[]   #将复选框放置到一个列表中
for index,item in enumerate(fruits):
    str=BooleanVar()
    str.set(False)
    Checkbutton(frame2,text=item,variable=str).grid(row=index+1,column=1)# 复选框
    checkbox.append(str)
win.mainloop()