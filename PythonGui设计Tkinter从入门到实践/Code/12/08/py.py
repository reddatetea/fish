#  _*_ coding:utf-8 _*_
# 开发团队：明日科技
# 开发人员：Administrator
# 文件名称：demo1.py
# 开发工具：PyCharm
# canvas绘制文字


from tkinter import *
import random
# 颜色列表
fill_color = ["#B0E3DD", "#E19644", "#6689E1", "#E16678", "#66E1CA"]
# 字体列表
font_family = ["方正舒体", "方正姚体", "华文琥珀", "宋体", "华文行楷", "楷体", "华文新魏", "隶书"]


def draw():
    canvas.delete("all")   #清空画布
    color = fill_color[random.randint(0, 4)]  # 随机选择文字颜色
    family = font_family[random.randint(0, 7)]   # 随机选择字体
    text = canvas.create_text(160, 60, text=str, font=(family, 20), fill=color)  # 绘制文字
win = Tk()
win.title("绘制文字")
win.geometry("330x200")
canvas = Canvas(win, width=300, height=160, relief="solid")
str = "人因梦想而伟大"   #定义文字内容

canvas.pack()
Button(win, text="绘制", command=draw).pack()
win.mainloop()
