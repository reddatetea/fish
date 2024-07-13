#  _*_ coding:utf-8 _*_
# 开发团队：明日科技
# 开发人员：Administrator
# 文件名称：py.py
# 开发工具：PyCharm
# 鼠标事件


from tkinter import *
import random
num=1   # 第多少关
# 随机设置颜色与众不同的方块（简称方块A）的索引
inde=random.randint(0, 99)
# 随机设置颜色
def col():
    arr=["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
    #为保证颜色相近，color1+color2多数方块的颜色     color1+color3为与众不同的方块的颜色
    color1=""
    color2=""
    color3=""
    for i in range(4):
        color1+=arr[random.randint(0,15)]
    for i in range(2):
        color2+=arr[random.randint(0,15)]
    for i in range(2):
        color3+=arr[random.randint(0,15)]
    colorArr = []   #将2个颜色保存到列表里
    colorArr.append("#"+color1+color2)
    colorArr.append("#"+color1+color3)
    return colorArr
def panduan(event):
    global num
    num+=1   #当前游戏关数加1
    level.config(text="第"+str(num)+"关")
    # 每刷新一次就需要获取一次方块A的索引
    inde = random.randint(1, 100)
    # 获取所有方块的颜色
    colorBox=col()
    for i in sqareBox:
        i.config(bg=colorBox[0])
    sqareBox[inde].config(bg=colorBox[1])
    # 重新为方块A绑定鼠标单击事件
    sqareBox[inde].bind("<Button-1>",panduan)

win = Tk()
win.geometry("270x270")
win.resizable(0,0)
sqareBox=[]    # 将方块存储在列表中
colorBox=col()
for i in range(10):   # 表示行
    for j in range(10):  # j表示列
        label=Label(win,width=3,height=1,bg=colorBox[0],relief="groove")
        sqareBox.append(label)  # 将组件添加到列表中
        label.grid(row=i,column=j)
sqareBox[inde].config(bg=colorBox[1])
sqareBox[inde].bind("<Button-1>",panduan)   # 为颜色与众不同的方块天机单击事件
level=Label(win,text="第1关",font=14)
level.grid(row=11,column=0,columnspan=10,pady=10)
win.mainloop()

