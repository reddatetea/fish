# _*_coding:UTF-8 _*_
# 开发团队：明日科技
# 开发人员：pc
# 开发时间：2020/3/20  20:57
# 文件名称：entry3.PY
# 开发工具：PyCharm
# get()与insert()he delete()

from tkinter import *
win=Tk()
win.configure(bg="#F3E4A4")    #设置窗口的背景颜色
def add():
    re.delete(0,END)     #清空显示结果的文本框的内容
    add1=int(op1.get())  #获取第一个加数
    add2=int(op2.get())  #获取第二个加数
    re.insert(INSERT,add1+add2)
op1=Entry(win,width=5,relief="groove")    #第一个加数文本框
op1.grid(row=0,pady=20)
Label(win,text="+",bg="#F3E4A4").grid(row=0,column=1)
op2=Entry(win,width=5,relief="groove")   #第二个加数文本框
op2.grid(row=0,column=2)
Label(win,text="=",bg="#F3E4A4").grid(row=0,column=3)
re=Entry(win,width=5,relief="groove")    #显示结果的文本框
re.grid(row=0,column=4)
Button(win,text="计算",command=add,relief="groove",bg="#10C9F5").grid(row=1,columnspan=5,ipadx=10)
win.mainloop()
