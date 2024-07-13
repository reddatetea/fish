# _*_coding:UTF-8 _*_
# 开发团队：明日科技
# 开发人员：pc
# 开发时间：2020/3/9  9:09
# 文件名称：demo1.PY
# 开发工具：PyCharm

# pack()方法的使用
# padx参数和ipad参数   设置对象的外间距和内间距

from tkinter import *
win=Tk()
win.title("tkinter的初使用")
txt1=Label(win,text="象吃狮",bg="#ba55d3",font=14)
txt2=Label(win,text="狮吃虎",bg="#c1ffc1",font=14)
txt3=Label(win,text="虎吃豹",bg="#cdb5cd",font=14)
txt4=Label(win,text="豹吃狼",bg="#ba55d3",font=14)
txt5=Label(win,text="狼吃狗",bg="#c1ffc1",font=14)
txt6=Label(win,text="狗吃猫",bg="#cdb5cd",font=14)
txt7=Label(win,text="猫吃鼠",bg="#ba55d3",font=14)
txt8=Label(win,text="鼠吃象",bg="#c1ffc1",font=14)
txt1.pack(side="left",padx="10",pady="5",ipadx="6",ipady="4")
txt2.pack(side="left",padx="10",pady="5",ipadx="6",ipady="4")
txt3.pack(side="left",padx="10",pady="5",ipadx="6",ipady="4")
txt4.pack(side="left",padx="10",pady="5",ipadx="6",ipady="4")
txt5.pack(side="left",padx="10",pady="5",ipadx="6",ipady="4")
txt6.pack(side="left",padx="10",pady="5",ipadx="6",ipady="4")
txt7.pack(side="left",padx="10",pady="5",ipadx="6",ipady="4")
txt8.pack(side="left",padx="10",pady="5",ipadx="6",ipady="4")
win.mainloop()



