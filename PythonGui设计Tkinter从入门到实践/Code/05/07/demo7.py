# _*_coding:UTF-8 _*_
# 开发团队：明日科技
# 开发人员：pc
# 开发时间：2020/3/22  15:16
# 文件名称：demo1.PY
# 开发工具：PyCharm
# Spinbox组件待修改

from tkinter import *
win=Tk()
mon=5     #道具的单价，默认单价是5金币
def typ():
    global mon
    if val.get()=="绿水晶":   #道具不同，单价不同
        mon=5
    elif val.get()=="红宝石":
        mon=10
    else:
        mon=15
    pay()
def pay():
    number=int(num.get())   #获取单价
    tatal=number*mon       #计算总价
    text1="选购 "+val.get()+" 总价 "+str(tatal)+" 金币"
    label.config(text=text1)
win.title("购买道具")
Label(win,text="购买道具：").grid(row=0,column=0,pady=10)
val=StringVar()   #该变量用于绑定道具Spinbox组件
val.set("绿水晶") #初始道具
Spinbox(win,values=("绿水晶","红宝石","生命水"),textvariable=val,command=typ).grid(row=0,column=1,pady=10)
Label(win,text="购买数量：").grid(row=1,column=0,pady=10)
num=Spinbox(win,from_=1,to=5,command=pay)
num.grid(row=1,column=1,pady=10)
Label(win,text="限购5件").grid(row=1,column=2,pady=10)
label=Label(win)
label.grid(row=3, column=0,columnspan=3, pady=10)
win.mainloop()