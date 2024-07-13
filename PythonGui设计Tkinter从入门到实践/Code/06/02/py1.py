# _*_coding:UTF-8 _*_
# 开发团队：明日科技
# 开发人员：pc
# 开发时间：2020/3/12  13:44
# 文件名称：py1.PY
# 开发工具：PyCharm



# Button：按钮控件
# 定义一个变量存储输入的密码


def num(a):
    val = pswshow.get()
    # 实现输入密码
    if len(val) < 11:
        # 先清除原有内容，然后将原有内容同输入的值一起添加到单行文本框
        pswshow.delete(0, END)
        pswshow.insert(0, val +" "+ a)
#实现后退功能
def back():
    #获取文本框的值
    val = pswshow.get()
    if len(val) >= 1:
        #如果文本框的值的长度大于1，则删除最后一位
        pswshow.delete(len(val) - 2, END)
        pswshow.config(text=val[0:len(val) - 2])
def enter():
    val = pswshow.get()
    # 弹出一个顶层窗口
    win2 = Toplevel()
    if len(val) == 11:
        Label(win2, text="\n\n密码正确，请等待\n\n").pack()
    else:
        Label(win2, text="\n\n密码为6位数的数字\n\n").pack()
from tkinter import *
win = Tk()
win.title("密码输入器")
# 密码显示部分
pswshow = Entry(win, relief="solid",justify="center" )

# 键盘部分
but1 = Button(win, text="1", command=lambda: num("1"))
but2 = Button(win, text="2", command=lambda: num("2"))
but3 = Button(win, text="3", command=lambda: num("3"))
but4 = Button(win, text="4", command=lambda: num("4"))
but5 = Button(win, text="5", command=lambda: num("5"))
but6 = Button(win, text="6", command=lambda: num("6"))
but7 = Button(win, text="7", command=lambda: num("7"))
but8 = Button(win, text="8", command=lambda: num("8"))
but9 = Button(win, text="9", command=lambda: num("9"))
back1 = PhotoImage(file='back.png')  # 创建了一个图象对象，后退
but0 = Button(win, text="0",height="1", command=lambda: num("0"))
enter2 = PhotoImage(file='enter.png')  # 创建了一个图象对象，确认
butback = Button(win, image=back1, command=back)
butok = Button(win, image=enter2, command=enter)

# foreground设置label组件的文字颜色
pswshow.grid(row=1,columnspan=3)
# 布局按钮
but1.grid(row=5,sticky=W+E)
but2.grid(row=5, column=1,sticky=W+E)
but3.grid(row=5, column=2,sticky=W+E)
but4.grid(row=6,sticky=W+E)
but5.grid(row=6, column=1,sticky=W+E)
but6.grid(row=6, column=2,sticky=W+E)
but7.grid(row=7,sticky=W+E)
but8.grid(row=7, column=1,sticky=W+E)
but9.grid(row=7, column=2,sticky=W+E)
butback.grid(ipady=3,row=8,sticky=W+E)
but0.grid(row=8, column=1,sticky=W+E)
butok.grid(ipady=3,row=8, column=2,sticky=W+E)
win.mainloop()
