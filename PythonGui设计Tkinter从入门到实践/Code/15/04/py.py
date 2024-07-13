#  _*_ coding:utf-8 _*_
# 开发团队：明日科技
# 开发人员：Administrator
# 文件名称：py.py
# 开发工具：PyCharm
# python文件夹操作


from tkinter import *
from tkinter.ttk import *
import os
class tree(object):
    def __init__(self,path):

        self.win=Tk()           #创建窗口
        self.win.title('显示树形目录')
        self.tree=Treeview()
        self.tree.heading("#0",text="file")
        self.tree.pack()
        temppath=os.path.basename(path)    #提取path路径中的最后一个文件名
        treeF = self.tree.insert('', 0, text=temppath)      #一级目录
        self.showtree(path,treeF)
        self.win.mainloop()
    def showtree(self,path,root):
        filelist=os.listdir(path)             #将文件夹中的文件放到列表里
        for filename in filelist:
            abspath=os.path.join(path,filename)
            #将路径添加到目录树中
            treeFinside = self.tree.insert(root, 0, text=filename,values=(abspath))
            if os.path.isdir(abspath):
                #将路径和上一级树枝名treeFinside返回
                self.showtree(abspath,treeFinside)

a=tree("D:\\code")
