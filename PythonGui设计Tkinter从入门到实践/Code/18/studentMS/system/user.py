# -*- coding: utf-8 -*-


from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *
import sys

sys.path.append("../")  # 返回上层路径
from service import service


class mainWindow():
    def __init__(self):
        self.MainWindow = Toplevel()
        self.MainWindow.geometry("307x267")
        self.MainWindow.title("用户信息维护")
        self.yscroll = Scrollbar(self.MainWindow)  # 滚动条
        self.yscroll.place(x=741, y=40, width=20, height=301)
        self.tree = Treeview(self.MainWindow, column=("userId", "userPwd"), show="headings")
        self.yscroll.config(command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.yscroll.set)
        self.tree.heading("userId", text="用户名称")
        self.tree.column("userId", width=70)
        self.tree.heading("userPwd", text="用户密码")
        self.tree.column("userPwd", width=70)
        self.tree.place(x=3, y=0, width=301, height=161)
        Label(self.MainWindow, text="用户名称：").place(x=7, y=170, width=71, height=21)
        Label(self.MainWindow, text="用户密码：").place(x=160, y=170, width=71, height=21)
        self.enuserId = Entry(self.MainWindow)  # 用户名称
        self. enuserId.place(x=80, y=170, width=69, height=22)
        self.enuserPwd = Entry(self.MainWindow)  # 用户密码
        self.enuserPwd.place(x=233, y=170, width=71, height=20)
        Button(self.MainWindow, text="添加", command=self.add).place(x=22, y=231, width=51, height=27)
        Button(self.MainWindow, text="修改", command=self.edit).place(x=92, y=231, width=51, height=27)
        Button(self.MainWindow, text="删除", command=self.delete).place(x=162, y=231, width=51, height=27)
        Button(self.MainWindow, text="退出", command=self.MainWindow.destroy).place(x=230, y=231, width=51, height=27)

        self.query()  # 窗体加载时显示所有数据
        self.tree.bind("<Button-1>", self.getItem)
        self.MainWindow.mainloop()

    # 查询用户信息，并显示在表格中
    def query(self):
        result = service.query("select * from tb_user")  # 调用服务类中的公共方法执行查询语句
        row = len(result)  # 取得记录个数，用于设置表格的行数
        if len(self.tree.get_children()) > 0:
            for it in self.tree.get_children():
                self.tree.delete(it)
        for it in result:  # 遍历行
            self.tree.insert("", END, value=it)
        self.enuserId.delete(0, END)
        self.enuserPwd.delete(0, END)

    # 获取选中的表格内容
    def getItem(self,event):
        it = event.widget.identify("item", event.x, event.y)
        colnum = event.widget.identify("column", event.x, event.y)
        if colnum == "#1":  # 如果单击的是第一列
            self.enuserId.delete(0, END)
            self.enuserPwd.delete(0, END)
            self.enuserId.insert(0, self.tree.set(it)["userId"])
            self.enuserPwd.insert(0,self.tree.set(it)["userPwd"])

    # 添加用户信息
    def add(self):
        userName = self.enuserId.get()  # 记录输入的用户名
        userPwd = self.enuserPwd.get()  # 记录输入的用户密码
        if userName != "" and userPwd != "":  # 判断用户名和密码不为空
            # 执行添加语句
            result = service.exec("insert into tb_user(userName,userPwd) values (%s,%s)", (userName, userPwd))
            if result > 0:  # 如果结果大于0，说明添加成功
                self.query()  # 在表格中显示最新数据
                showinfo('提示', '信息添加成功！')
        else:
            showwarning('警告', '请输入数据后，再执行相关操作！')

    # 修改用户信息
    def edit(self):
        try:
            if self.tree.focus() != "":  # 判断是否选择了要修改的数据
                userPwd = self.enuserPwd.get()  # 记录修改的用户密码
                if userPwd != "":  # 判断密码不为空
                    # 执行修改操作
                    result = service.exec("update tb_user set userPwd= %s where userName=%s", (userPwd, self.enuserId.get()))
                    if result > 0:  # 如果结果大于0，说明修改成功
                        self.query()  # 在表格中显示最新数据
                        showinfo('提示', '信息修改成功！')
        except:
            showwarning('警告', '请先选择要修改的数据！')

    # 删除用户信息
    def delete(self):
        try:
            if self.tree.focus() != "":  # 判断是否选择了要删除的数据
                # 执行删除操作
                it = self.tree.set(self.tree.focus())["userId"]
                result = service.exec("delete from tb_user where userName= %s", (it,))
                if result > 0:  # 如果结果大于0，说明删除成功
                    self.query()  # 在表格中显示最新数据
                    showinfo('提示', '信息删除成功！')
        except:
            showwarning('警告', '请先选择要删除的数据！')
