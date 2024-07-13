# _*_coding:UTF-8 _*_
# 开发团队：明日科技
# 开发人员：pc
# 开发时间：2020/3/9  9:09
# 文件名称：demo1.PY
# 开发工具：PyCharm

# label组件的使用
# 设置label的样式以及设置文本样式

from tkinter import *
win=Tk()                           #添加标题
win.title("斗兽棋游戏的食物链")    #添加标题
# textd定义Label标签里的文本内容，bg表示Label的背景颜色
txt1=Label(win,text="象",bg="#FFEBCD",width=5,padx=4,pady=4,font="14")
txt2=Label(win,text="狮",bg="#c1ffc1",width=5,padx=4,pady=4,font="14")
txt3=Label(win,text="虎",bg="#FFEBCD",width=5,padx=4,pady=4,font="14")
txt4=Label(win,text="豹",bg="#c1ffc1",width=5,padx=4,pady=4,font="14")
txt5=Label(win,text="狼",bg="#FFEBCD",width=5,padx=4,pady=4,font="14")
txt6=Label(win,text="狗",bg="#c1ffc1",width=5,padx=4,pady=4,font="14")
txt7=Label(win,text="猫",bg="#FFEBCD",width=5,padx=4,pady=4,font="14")
txt8=Label(win,text="鼠",bg="#c1ffc1",width=5,padx=4,pady=4,font="14")
# foreground设置label组件的文字颜色
txtr1=Label(win,text="→",padx=2,pady=2,foreground="#B22222").grid(row=1,column=2)
txtr2=Label(win,text="→",padx=2,pady=2,foreground="#B22222").grid(row=1,column=4)
txtb1=Label(win,text="↓",padx=2,pady=2,foreground="#B22222").grid(row=2,column=5)
txtb2=Label(win,text="↓",padx=2,pady=2,foreground="#B22222").grid(row=4,column=5)
txtl1=Label(win,text="←",padx=2,pady=2,foreground="#B22222").grid(row=5,column=4)
txtl2=Label(win,text="←",padx=2,pady=2,foreground="#B22222").grid(row=5,column=2)
txtt1=Label(win,text="↑",padx=2,pady=2,foreground="#B22222").grid(row=4,column=1)
txtt2=Label(win,text="↑",padx=2,pady=2,foreground="#B22222").grid(row=2,column=1)
# 设置斗兽棋游戏的棋子的位置
txt1.grid(row=1,column=1)
txt2.grid(row=1,column=3)
txt3.grid(row=1,column=5)
txt4.grid(row=3,column=5)
txt5.grid(row=5,column=5)
txt6.grid(row=5,column=3)
txt7.grid(row=5,column=1)
txt8.grid(row=3,column=1)
win.mainloop()



