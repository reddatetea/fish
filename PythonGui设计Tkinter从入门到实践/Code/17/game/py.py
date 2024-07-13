#  _*_ coding:utf-8 _*_
# 开发团队：明日科技
# 开发人员：Administrator
# 文件名称：py.py.py
# 开发工具：PyCharm

from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *
import random
import time
big = 0      # big和little用于帮助电脑选择点数大小
little = 0
count = 0      # 单次游戏中骰子变化的次数

def call():
    global image1     # 第一个骰子图片变量
    global image2     # 第二个骰子图片变量
    global image3     # 第三个骰子的图片变量
    global count      # 摇骰子次数
    global add        # 三个骰子的总点数
    global flag       # 第三个骰子的图片变量
    num = random.choice(range(1, 7))  # 随机生成第一个骰子的点数
    img = str(num) + "t.png"
    img = 'touzi/' + img
    image1 = PhotoImage(file=img)
    label.config(image=image1)  # 切换对应点数的骰子图片
    add = num

    num = random.choice(range(1, 7))  # 随机生成第二个骰子的点数
    img = str(num) + "t.png"
    img = 'touzi/' + img
    image2 = PhotoImage(file=img)
    labe2.config(image=image2)  # 切换对应点数的骰子图片
    add += num  # 求和
    num = random.choice(range(1, 7))  # 随机生成第三个骰子的点数
    img = str(num) + "t.png"
    img = 'touzi/' + img
    image3 = PhotoImage(file=img)
    labe3.config(image=image3)  # 切换对应点数的骰子图片

    add += num
    count += 1
    if count < 20:
        root.after(100, call)
    else:
        judge()  # 判断大小


# 获取用户的选择结果
def option_value():
    global value
    global big
    global little
    global s_sel
    global labe4
    if cvar.get() == 1:
        value = "大"
    else:
        value = "小"
    labe4.config(text="你选的是：" + value)
    s_sel = sys_value(big, little)
    return value

#电脑选择的结果
def sys_value(value1, value2):  # 电脑选择结果
    if value1 <= value2:
        labe5.config(text="电脑选的是：大")
        return "大"
    else:
        labe5.config(text="电脑选的是：小")
        return "小"
#判断胜负

def judge():
    global big
    global little
    global s_sel
    global y_sel
    global add
    if add >= 10:
        big += 1  # 总点数大于10，则big+1,反之little+1
        if y_sel == "大":  # 如果用户选择点数为大
            if s_sel == "小":
                showinfo("掷骰子结果","恭喜，你赢了电脑")
            else:
                showinfo("掷骰子结果", "^_^你和电脑打平了！")
        else:
            if s_sel == "大":
                showinfo("掷骰子结果", "哦耶，电脑赢了！")
            else:
                showinfo("掷骰子结果", "-_-|||你和电脑都输了！")

    else:  # 如果用户选择点数为小
        little += 1
        if y_sel == "大":
            if s_sel == "小":
                showinfo("掷骰子结果","哦耶，电脑赢了！")
            else:
                showinfo("掷骰子结果","-_-|||你和电脑都输了！")
        else:
            if s_sel == "大":
                showinfo("掷骰子结果", "恭喜，你赢了电脑！")
            else:
                showinfo("掷骰子结果", "^_^你和电脑打平了！")

# 开始游戏
def start():
    global y_sel
    global count
    count = 0
    y_sel = option_value()
    call()


root = Tk()
root.title('人机对话：掷骰子游戏')
root.wm_attributes('-topmost', 1)
root.geometry('320x250')

title = Label(root, text="选择骰子点数大小：").grid(column=0, row=0)
cvar = IntVar()
cvar.set('1')     #单选按钮的默认值
option = Radiobutton(root, text="大", variable=cvar, value=1, command=option_value).grid(column=0, row=1, columnspan=3)
option1 = Radiobutton(root, text="小", variable=cvar, value=0, command=option_value).grid(column=3, row=1, columnspan=3)
image1 = PhotoImage(file='touzi/6t.png')
label = Label(root, image=image1)        # 第一个骰子图片
label.grid(column=0, row=2, columnspan=2)
image2 = PhotoImage(file='touzi/6t.png')
labe2 = Label(root, image=image2)        # 第二个骰子图片
labe2.grid(column=2, row=2, columnspan=2)
image3 = PhotoImage(file='touzi/6t.png')
labe3 = Label(root, image=image3)         # 第三个骰子图片
labe3.grid(column=4, row=2, columnspan=2)
labe4 = Label(root, text="你选的是：大")  # 显示用户选择结果
labe4.grid(column=0, row=3, columnspan=3)
labe5 = Label(root, text="电脑选的是：大")  # 显示电脑选择结果
labe5.grid(column=3, row=3, columnspan=3)
Button(root, text="开始", command=start).grid(column=0, row=6, columnspan=6)  # 开始按钮
root.mainloop()
