#  _*_ coding:utf-8 _*_
# 开发团队：明日科技
# 开发人员：Administrator
# 文件名称：py.py
# 开发工具：PyCharm
# python文件夹操作


# 显示文件内容
def sav():
    b=askopenfile(title="打开文件",filetypes=[("text文本文件","*.txt")])   #选择文件
    file=open(b.name,"r")
    text.insert(0.0,file.readlines())       # 将文件内容添加到多行文本框中
from tkinter import *
from tkinter.filedialog import *
win=Tk()
Button(win,text="打开文件",command=sav).pack(pady=10)
text=Text(win,width=50,height=5)
text.pack()
win.mainloop()
