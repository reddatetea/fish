#  _*_ coding:utf-8 _*_
# 开发团队：明日科技
# 开发人员：Administrator
# 文件名称：demo1.py
# 开发工具：PyCharm
# canvas绘制西瓜冰淇淋



from tkinter import *
win = Tk()
win.title("绘制西瓜状雪糕")
win.geometry("300x200")
canvas = Canvas(win, width=500, height=400, relief="solid")
canvas.create_rectangle(90,124,100,195,fill="#E9D39D",outline="#E9D39D")  #雪糕把手
canvas.create_arc(90,180,100,200,fill="#E9D39D",outline="#E9D39D",style=CHORD,extent=-180)  #雪糕把手

canvas.create_arc(5,-70,185,162,extent=-40,outline="#32E143",fill="#32E143",start=-70,width=2,style=PIESLICE)  # 西瓜的皮
canvas.create_arc(8,-67,181,155,extent=-40,outline="#E92742",fill="#E92742",start=-70,width=2,style=PIESLICE)  #西瓜的瓤
canvas.create_arc(92,74,97,79,extent=159,fill="#000",width=2,style=ARC)    #西瓜子
canvas.create_arc(97,94,102,99,extent=180,start=90,fill="#000",width=2,style=ARC)    #西瓜子
canvas.create_arc(110,124,113,127,extent=359,fill="#000",width=2,style=ARC)    #西瓜子
canvas.create_arc(90,134,93,137,extent=359,fill="#000",width=2,style=ARC)    #西瓜子


canvas.pack()

win.mainloop()
