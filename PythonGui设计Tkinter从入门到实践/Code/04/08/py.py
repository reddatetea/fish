# _*_coding:UTF-8 _*_
# 开发团队：明日科技
# 开发人员：pc
# 开发时间：2020/3/9  9:09
# 文件名称：demo1.PY
# 开发工具：PyCharm

#grid()的使用
#grid中rowconfigure()和columnconfigure()的使用

from tkinter import *
win=Tk()

win.rowconfigure(0,weight=1)     #设置第2列的组件的缩放比例为1
win.columnconfigure(1,weight=1)  #设置第2行的组件的缩放比例为1
txt1=Label(win,width=15,height=2,relief="groove",bg="#E0FFFF")
txt1.grid(row=0,column=0,sticky=N+W)  #第一行第一列组件位置
txt2=Label(win,width=15,height=2,relief="groove",bg="#99ffcc")
txt2.grid(row=0,column=1,sticky=N+E)  #第一行第二列组件位置
txt3=Label(win,width=15,height=2,relief="groove",bg="#E0FFFF")
txt3.grid(row=1,column=0,sticky=N+S+W)  #第二行第一列组件位置
txt4=Label(win,width=15,height=2,relief="groove",bg="#99ffcc")
txt4.grid(row=1,column=1,sticky=N+S+E)  #第一行第二列组件位置
win.mainloop()
