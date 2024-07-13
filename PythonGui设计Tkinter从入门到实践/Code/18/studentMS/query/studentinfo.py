# # -*- coding: utf-8 -*-
#
# # Form implementation generated from reading ui file 'studentinfo.ui'
# #
# # Created by: PyQt5 UI code generator 5.13.2
# #
# # WARNING! All changes made in this file will be lost!
#


from tkinter import *
from tkinter.ttk import *
# from PyQt5 import QtCore, QtGui, QtWidgets
# from PyQt5.QtWidgets import *
import sys

sys.path.append("../")  # 返回上层路径
from service import service


class mainWindow():
    def __init__(self):
        self.MainWindow = Toplevel()
        self.MainWindow.title("学生信息管理")
        self.MainWindow.geometry("766x387")

        # 表格上方的内容
        Label(self.MainWindow, text="选择查询列表：").place(x=185, y=8, width=101, height=21)
        Label(self.MainWindow, text="输入查询关键字：").place(x=399, y=8, width=121, height=21)
        self.cbexamkinds = StringVar()  # 选择查询列表
        self.cbExam = Combobox(self.MainWindow, textvariable=self.cbexamkinds, value=("学生编号", "学生姓名"))
        self.cbExam.place(x=288, y=8, width=91, height=22)
        self.keyWords = Entry(self.MainWindow)
        self.keyWords.place(x=509, y=8, width=91, height=21)

        Button(self.MainWindow, text="查询", command=self.query).place(x=630, y=8, width=51, height=25)
        Button(self.MainWindow, text="退出", command=self.MainWindow.destroy).place(x=700, y=8, width=51, height=25)

        # 表格

        self.yscroll = Scrollbar(self.MainWindow)  # 滚动条
        self.yscroll.place(x=741, y=40, width=20, height=301)
        self.tree = Treeview(self.MainWindow,
                             column=("stuId", "stuName", "stuclass", "stusex", "stuage", 'stuarr', "stuphone"),show="headings")
        self.yscroll.config(command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.yscroll.set)


        self.tree.heading("stuId", text="学生编号")
        self.tree.column("stuId", width=60)
        self.tree.heading("stuName", text="姓名")
        self.tree.column("stuName", width=60)
        self.tree.heading("stuclass", text="班级")
        self.tree.column("stuclass", width=60)
        self.tree.heading("stusex", text="性别")
        self.tree.column("stusex", width=60)
        self.tree.heading("stuage", text="年龄")
        self.tree.column("stuage", width=60)
        self.tree.heading("stuarr", text="家庭住址")
        self.tree.column("stuarr", width=70)
        self.tree.heading("stuphone", text="联系电话")
        self.tree.column("stuphone", width=70)
        self.tree.place(x=0, y=40, width=741, height=301)

        self.query()

        self.MainWindow.mainloop()

    # 查询学生信息，并显示在表格中
    def query(self):
        # 获取所有学生信息
        if self.keyWords.get() == "":
            result = service.query(
                "select stuID,stuName,CONCAT(gradeName,className),sex,age,address,phone from v_studentinfo")
        else:
            sql=""
            key = self.keyWords.get()  # 记录查询关键字
            # 根据学生编号查询信息
            if self.cbexamkinds.get() == "学生编号":
                sql = "select stuID,stuName,CONCAT(gradeName,className),sex,age,address,phone from v_studentinfo where stuID like '%" + key + "%'"
                # result = service.query2(sql)
            # 根据学生姓名查询信息
            elif self.cbexamkinds.get() == "学生姓名":
                sql = "select stuID,stuName,CONCAT(gradeName,className),sex,age,address,phone from v_studentinfo where stuName like '%" + key + "%'"
            result = service.query2(sql)
        row = len(result)  # 取得记录个数，用于设置表格的行数
        if len(self.tree.get_children()) > 0:
            for it in self.tree.get_children():
                self.tree.delete(it)
        for it in range(row):
            self.tree.insert("", END, value=result[it])
