# _*_coding:UTF-8 _*_
# 开发团队：明日科技
# 开发人员：pc
# 开发时间：2020/3/12  17:22
# 文件名称：demo2.PY
# 开发工具：PyCharm

# Radiobutton的初级使用

# 判断答案是否正确
def result1():
    if v.get() == 1:
        re.config(text="答错了，答案是小狗，因为“旺旺仙贝（汪汪先背）”")
    else:
        re.config(text="答对了，因为“旺旺仙贝（汪汪先背）”")
from tkinter import *
win = Tk()
win.title("脑筋急转弯")   #设置窗口标题
win.geometry("300x150")   #设置窗口大小
text = Label(win, text="老师让小猫和小狗去背书，请问谁先背书呢",font="14").pack(anchor=W)
# 该变量绑定单选按钮的值
v = IntVar()
ans1=Radiobutton(win, text="小猫", variable=v, value=1,font="12",selectcolor="#F1D4C9")
ans1.pack(anchor=W)
ans2=Radiobutton(win, text="小狗", variable=v, value=2,font="12",selectcolor="#F1D4C9")
ans2.pack(anchor=W)
button = Button(win, text="提交", command=result1,font="14",bg="#F1C57E",relief="groove").pack()
re = Label(win)     #显示答案的文本框
re.pack()
win.mainloop()
