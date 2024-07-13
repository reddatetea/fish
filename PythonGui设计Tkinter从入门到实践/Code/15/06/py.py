#  _*_ coding:utf-8 _*_
# 开发团队：明日科技
# 开发人员：Administrator
# 文件名称：py.py
# 开发工具：PyCharm
# python文件夹操作


b=""
# 创建并保存文件
def sav():
    global b
    # 可选的文件格式
    filetype = [('Python Files', '*.py *.pyw'),('Text Files', '*.txt'),('All Files', '*.*')]
    b=asksaveasfile(defaultextension = '.py',filetypes = filetype,initialdir = 'D:\\code',initialfile = 'Test',title = "另存为")

#     定义向文件内添加的内容
def edit1():
    if b=="":
        showerror("错误","文件不存在，请先创建文件")
    else:
        text.grid(row=2,column=0,columnspan=3)

# 添加内容
def add1():
    global text
    a = text.get(0.0, END)
    if len(a)<=1:
        showerror("错误", "内容不能为空")
    else:
        file = open(b.name, "w", encoding='utf-8')
        file.write(a)
        file.close()
        win.quit()

from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *
win=Tk()
Button(win,text="创建文件",command=sav).grid(row=0,column=0,padx=10,)
Button(win,text="编辑内容",command=edit1).grid(row=0,column=1,padx=20,pady=10)
Button(win,text="提交",command=add1).grid(row=0,column=2,padx=10,)
text=Text(win,width=50,height=5)
win.mainloop()
