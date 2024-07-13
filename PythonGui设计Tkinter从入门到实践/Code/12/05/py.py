#  _*_ coding:utf-8 _*_
# 开发团队：明日科技
# 开发人员：Administrator
# 文件名称：demo1.py
# 开发工具：PyCharm
# canvas绘制圆弧



from tkinter import *

win = Tk()
win.title("绘制西瓜")
win.geometry("300x200")
canvas = Canvas(win, width=200, height=200, relief="solid")
arc1=canvas.create_arc(40,40,150,150,extent=-180,fill="#E95121",outline="#73F18B",width=5)  # 绘制西瓜
line=canvas.create_line(42,94,148,94,width=7,fill="#E95121")
cir1 = canvas.create_oval(95, 95, 100, 100, fill="#000000")     # 西瓜籽
cir2 = canvas.create_oval(70, 97, 75, 102, fill="#000000")      # 西瓜籽
cir3 = canvas.create_oval(95, 125, 100, 130, fill="#000000")    # 西瓜籽
cir4 = canvas.create_oval(65, 125, 70, 130, fill="#000000")     # 西瓜籽
cir5 = canvas.create_oval(125, 110, 130, 115, fill="#000000")   # 西瓜籽

canvas.pack()

win.mainloop()
