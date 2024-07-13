#  _*_ coding:utf-8 _*_
# 开发团队：明日科技
# 开发人员：Administrator
# 文件名称：py.py
# 开发工具：PyCharm
# python文件夹操作

from tkinter import *
from tkinter.filedialog import *
from tkinter.ttk import *
def a():
    # 打开文件会话框，其返回值为一个元组形式的文件名
    file=askopenfilenames(title="选择文件",filetype=[("png图片","*.png")])
    # 遍历元组，将其添加到树形菜单中
    for i,ch in enumerate(file):
        tree.insert("", index=END, text=i,values=(ch))
win=Tk()
win.title("显示所选文件的信息")

Button(win,text="选择",command=a).pack(pady=5)# 添加按钮
tree=Treeview(win,columns=("path"))           # 添加树形菜单
tree.heading("#0",text="序号")
tree.heading("path",text="路径")
tree.pack()
win.mainloop()






