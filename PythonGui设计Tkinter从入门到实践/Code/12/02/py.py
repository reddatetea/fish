#  _*_ coding:utf-8 _*_
# 开发团队：明日科技
# 开发人员：Administrator
# 文件名称：demo1.py
# 开发工具：PyCharm
# canvas绘制直线

from tkinter import *
win=Tk()
win.title("创建canvas画布")
win.geometry("300x200")
canvas=Canvas(win,width=200,height=200)   # 创建画布
line1=(14,65,66,65,83,19,99,64,148,64,111,96,126,143,83,113,44,142,58,97,14,65)   # 五角星的定点
line1=canvas.create_line(*line1,fill="red")     # 按定点的顺序依次绘制直线
canvas.pack()
win.mainloop()