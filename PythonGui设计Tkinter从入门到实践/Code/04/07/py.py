# _*_coding:UTF-8 _*_
# 开发团队：明日科技
# 开发人员：pc
# 开发时间：2020/3/9  9:09
# 文件名称：demo1.PY
# 开发工具：PyCharm

#grid()的使用
#row表示行，column表示列

from tkinter import *
win=Tk()     #创建根窗口
win.title("tkinter的初使用")    #添加标题
# grid(row=0,column=0,padx=10)设置组件位于第0行第0列，与其他组件的水平间距为10
Label(win,text="1*1=1",bg="#E0FFFF").grid(row=0,column=0,padx=10)
Label(win,text="1*2=3",bg="#E0FFFF").grid(row=1,column=0,padx=10)
Label(win,text="1*3=3",bg="#E0FFFF").grid(row=2,column=0,padx=10)
Label(win,text="1*4=4",bg="#E0FFFF").grid(row=3,column=0,padx=10)
Label(win,text="2*2=4",bg="#EEA9B8").grid(row=1,column=1,padx=10)
Label(win,text="2*3=6",bg="#EEA9B8").grid(row=2,column=1,padx=10)
Label(win,text="2*4=8",bg="#EEA9B8").grid(row=3,column=1,padx=10)
Label(win,text=" 3*3=9 ",bg="#F08080").grid(row=2,column=2,padx=10)
Label(win,text="3*4=12",bg="#F08080").grid(row=3,column=2,padx=10)
Label(win,text="4*4=16",bg="#FFE1FF").grid(row=3,column=3,padx=10)
win.mainloop()
