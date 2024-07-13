#  _*_ coding:utf-8 _*_
# 开发团队：明日科技
# 开发人员：Administrator
# 文件名称：demo1.py
# 开发工具：PyCharm
#
# # Toplevel组件
# from tkinter import *
# def begin():
#     # 顶层窗口提示玩家进入2号房间，并且准备游戏
#     win2=Toplevel()  #添加顶层窗口
#     win2.geometry("200x120")  #设置顶层窗口的大小
#     win2.configure(bg="#FFACAB")  #设置顶层窗口的背景颜色
#     win2.title("准备游戏")    #顶层窗口的标题
#     Label(win2,text="玩家已就位，请准备！",font=14,bg="#FFACAB").pack(pady=50)
# def change():
#     # 顶层窗口提示玩家准备
#     win2 = Toplevel()
#     win2.geometry("200x120")
#     win2.configure(bg="#FFACAB")
#     win2.title("2号棋牌室")
#     Label(win2, text="欢迎进入2号棋牌室", bg="#FFACAB", font=14, width=35).pack(side="top",fill="x")
#     Label(win2, text="玩家已就位，请准备！",bg="#FFACAB", font=16).pack(pady=20,side="top",fill="x")
# win1=Tk()
# win1.geometry("270x220")
# win1.title("1号棋牌室")
# win1.configure(bg="#FFCD63")
# # 默认匹配玩家进入1号棋牌室
# label=Label(win1,text="欢迎进入1号棋牌室",background="#FFFBB5",font=14,width=35).grid(row=0,column=0,columnspan=5,ipady=8)
# btn1=Button(win1,text="开始对局",background="#35A837",command=begin).grid(row=2,column=1,pady=10)
# btn2=Button(win1,text="更换房间",background="#FF4A4F",command=change).grid(row=2,column=3,pady=10)
# win1.mainloop()

from tkinter import *

panewindow = PanedWindow(sashrelief=SUNKEN, background="#1DF5DF", width=200)
panewindow.pack()  # 将子组件添加到panewindow中
btn1 = Button(panewindow, text='左侧按钮')
panewindow.add(btn1)
btn2 = Button(panewindow, text='右侧按钮')
panewindow.add(btn2)
mainloop()
