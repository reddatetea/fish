#  _*_ coding:utf-8 _*_
# 开发团队：明日科技
# 开发人员：Administrator
# 文件名称：demo1.py
# 开发工具：PyCharm
# canvas绘制多边形



from tkinter import *

win = Tk()
win.title("绘制松鼠")
win.geometry("240x260")
canvas = Canvas(win, width=250, height=250, relief="solid")
polyl=canvas.create_polygon(27,8,27,62,54,34,fill="#fbfe0d")      #左耳
poly2=canvas.create_polygon(54,34,81,8,81,63,fill="red")   #右耳
poly3=canvas.create_polygon(81,63,54,35,25,61,53,90,fill="#0001fc")   #脸
poly4=canvas.create_polygon(81,63,81,176,138,121,fill="#32ccfe")   #身体
poly5=canvas.create_polygon(81,97,43,135,81,174,fill="#fdcbfe")   #上半身
poly6=canvas.create_polygon(139,119,60,198,140,198,fill="#02cd02")   #下半身
poly7=canvas.create_polygon(140,198,167,170,223,170,196,198,fill="#9b01ff")   #尾巴
canvas.pack()
win.mainloop()
