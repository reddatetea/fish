#  _*_ coding:utf-8 _*_
# 开发团队：明日科技
# 开发人员：Administrator
# 文件名称：demo1.py
# 开发工具：PyCharm
#Menu菜单的使用   创建下拉菜单


def pop1():
    # win.winfo_x()和win.winfo_y()为获取的win窗口的位置
    menu2_2.post(win.winfo_x()+60,win.winfo_y()+120)
from tkinter import *
win=Tk()
menu1=Menu(win)           #创建顶级菜单
menu2_1=Menu(menu1,tearoff=False)      #创建第二级菜单
menu1.add_cascade(label="城市",menu=menu2_1)   #将第二级菜单添加到顶级菜单并设置显示的内容
menu2_1.add_command(label="北京")              #二级菜单中含有五个子菜单
menu2_1.add_command(label="上海")
menu2_1.add_command(label="重庆")
menu2_1.add_command(label="广州")
menu2_1.add_command(label="深圳")
menu1.add_command(label="修改",command=pop1)
menu2_2=Menu(menu1,tearoff=False)              #添加弹出菜单
menu2_2.add_command(label="添加城市")
menu2_2.add_command(label="修改城市")
menu1.add_command(label="退出",command=win.quit)
win.config(menu=menu1)
win.mainloop()