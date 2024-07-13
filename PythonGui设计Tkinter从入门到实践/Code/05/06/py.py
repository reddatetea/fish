# _*_coding:UTF-8 _*_
# 开发团队：明日科技
# 开发人员：pc
# 开发时间：2020/3/22  15:16
# 文件名称：demo1.PY
# 开发工具：PyCharm
# Spinbox组件

from tkinter import *
win=Tk()             #创建根窗口
win.title("购买道具")    #添加窗口标题
Label(win,text="购买道具：").grid(row=0,column=0,pady=10)
#通过元组定义可选择的值
Spinbox(win,values=("绿水晶","红宝石","生命水")).grid(row=0,column=1,pady=10)
Label(win,text="购买数量：").grid(row=1,column=0,pady=10)
#通过from_和to定义可选的数值范围
Spinbox(win,from_=1,to=5).grid(row=1,column=1,pady=10)
Label(win,text="限购5件").grid(row=1,column=2,pady=10)
Label(win,text="支付方式：").grid(row=2,column=0,pady=10)
Spinbox(win,values=("金币","钻石","点券")).grid(row=2,column=1,pady=10)
win.mainloop()