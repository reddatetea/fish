# _*_coding:UTF-8 _*_
# 开发团队：明日科技
# 开发人员：pc
# 文件名称：demo1.PY
# 开发工具：PyCharm

#设置窗口位置，在屏幕中居中

from tkinter import *
win=Tk()
win.title("tkinter的窗口的位置")     #窗口的标题
win.configure(bg="#a7ea90")        #窗口的背景颜色
winw=300                              #窗口的宽度
winh=220                              #窗口的高度
scrw=win.winfo_screenwidth()            #屏幕的宽度
scrh=win.winfo_screenheight()           #屏幕的高度
x=(scrw-winw)/2                        #窗口的水平位置
y=(scrh-winh)/2                        #窗口的垂直位置
win.geometry("%dx%d+%d+%d" %(winw,winh,x,y))            #设置窗口位置
str="\n\n程序员鄙视链\n\n一等码农搞算法，吃香喝辣调调参\n\n二等码农搞架构，高并低延能吹牛\n\n三等码农搞工程，怼天怼地怼PM\n\n四等码农搞前端，浮层像素老黄牛"
txt=Label(win,text=str,bg="#a7ea90").pack()
win.mainloop()
