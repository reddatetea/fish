from tkinter import *
from tkinter import ttk  #导入ttk模块，因为Combobox下拉菜单控件在ttk中
root = Tk()

root.title("combobox demo")
root.geometry("300x200")

combobox = ttk.Combobox(root)
combobox.pack()

#设置下拉菜单中的值
combobox['value'] = ("北京","上海","广州","深圳")

#设置下拉菜单的默认值,默认值索引从0开始
a = combobox.current(1)

if  a == '上海':
    print('hello shanghai')

mainloop()