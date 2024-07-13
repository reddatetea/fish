#  _*_ coding:utf-8 _*_
# 开发团队：明日科技
# 开发人员：Administrator
# 文件名称：demo1.py
# 开发工具：PyCharm
# Menu菜单的基本使用
from tkinter import *
win=Tk()
win.title("为游戏窗口添加菜单")
menu1=Menu(win)          # 创建顶级菜单
# 添加工具栏
menu1.add_command(label="游戏",command="")
menu1.add_command(label="帮助",command="")
menu1.add_command(label="退出",command="")
win.config(menu=menu1)         # 显示菜单
win.mainloop()

