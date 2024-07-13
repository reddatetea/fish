#  _*_ coding:utf-8 _*_
# 开发团队：明日科技
# 开发人员：Administrator
# 文件名称：demo1.py
# 开发工具：PyCharm
# canvas绘制椭圆



from tkinter import *

win = Tk()
win.title("绘制人脸")
win.geometry("300x200")
canvas = Canvas(win, width=200, height=200, relief="solid")
cir1 = canvas.create_oval(34, 68, 143, 127, fill="#C8F7F2")      #脸
cir2 = canvas.create_oval(59,83,71,99,fill="#E6F1B7")            #左眼
cir2_1 = canvas.create_oval(61,86,71,94,fill="#000000")          #左眼珠


cir3 = canvas.create_oval(101,83,113,99,fill="#E6F1B7")            #右眼
cir3_1 = canvas.create_oval(100,86,109,94,fill="#000000")          #右眼珠


canvas.pack()

win.mainloop()
