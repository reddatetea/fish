# -*- coding: utf-8 -*-


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
        self.MainWindow.title("学生成绩查询")
        self.MainWindow.geometry("766x387")

        # 表格上方的内容
        Label(self.MainWindow, text="输入学生姓名：").place(x=115, y=10, width=91, height=21)
        Label(self.MainWindow, text="考试种类：").place(x=305, y=9, width=71, height=21)
        Label(self.MainWindow, text="考试科目：").place(x=460, y=10, width=71, height=21)
        self.enName = Entry(self.MainWindow)  # 学生姓名
        self.enName.place(x=210, y=10, width=69, height=22)
        self.cbexamKinds = StringVar()  # 考试种类
        self.cbexamKinds.set("所有")
        self.cbGrade = Combobox(self.MainWindow, textvariable=self.cbexamKinds)
        self.cbGrade.place(x=373, y=10, width=69, height=22)
        self.cbsubKinds = StringVar()  # 考试科目
        self.cbsubKinds.set("所有")
        self.cbClass = Combobox(self.MainWindow, textvariable=self.cbsubKinds)
        self.cbClass.place(x=530, y=9, width=69, height=22)
        Button(self.MainWindow, text="查询", command=self.query).place(x=650, y=3, width=51, height=31)
        Button(self.MainWindow, text="退出" ,command=self.MainWindow.destroy).place(x=710, y=3, width=51, height=31)

        # 表格

        self.yscroll = Scrollbar(self.MainWindow)  # 滚动条
        self.yscroll.place(x=741, y=40, width=20, height=301)
        self.tree = Treeview(self.MainWindow, column=("stuId", "stuName", "stuclass", "stusub", "stuexamkd", 'stuscore'),
                        show="headings")
        self.yscroll.config(command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.yscroll.set)

        self.tree.heading("stuId", text="学生编号")
        self.tree.column("stuId", width=70)
        self.tree.heading("stuName", text="学生姓名")
        self.tree.column("stuName", width=70)
        self.tree.heading("stuclass", text="班级")
        self.tree.column("stuclass", width=70)
        self.tree.heading("stusub", text="科目")
        self.tree.column("stusub", width=70)
        self.tree.heading("stuexamkd", text="考试种类")
        self.tree.column("stuexamkd", width=70)
        self.tree.heading("stuscore", text="成绩")
        self.tree.column("stuscore", width=70)
        self.tree.place(x=0, y=40, width=741, height=301)

        # # 绑定事件以及调用

        self.bindCbox()  # 窗体加载时绑定考试类别和考试科目下拉列表
        self.query()  # 窗体加载时显示所有数据

        self.MainWindow.mainloop()

    # 查询成绩信息，并显示在表格中
    def query(self):
        stuname = self.enName.get()  # 记录查询的学生姓名
        kindname = self.cbexamKinds.get()  # 记录选择的考试种类
        subname = self.cbsubKinds.get()  # 记录选择的考试科目
        if stuname == "":
            if kindname == "所有":
                if subname == "所有":
                # 查询所有成绩信息
                    result = service.query(
                    "select stuID,stuName,CONCAT(gradeName,className),subName,kindName,result from v_resultinfo")
                else:
                    # 根据考试科目查询成绩信息
                    result = service.query(
                    "select stuID,stuName,CONCAT(gradeName,className),subName,kindName,result from v_resultinfo where subName=%s",
                    subname)
            else:
                # 根据考试类别查询成绩信息
                result = service.query(
                "select stuID,stuName,CONCAT(gradeName,className),subName,kindName,result from v_resultinfo where kindName=%s",
                kindname)
        else:
            if kindname == "所有":
                if subname == "所有":
                    # 根据学生姓名查询成绩信息
                    result = service.query2(
                    "select stuID,stuName,CONCAT(gradeName,className),subName,kindName,result from v_resultinfo where stuName like '%" + stuname + "%'")
                else:
                    # 根据学生姓名和考试科目查询成绩信息
                    result = service.query2(
                    "select stuID,stuName,CONCAT(gradeName,className),subName,kindName,result from v_resultinfo where stuName like '%" + stuname + "%' and subName='" + subname + "'")
            else:
                # 根据学生姓名、考试科目和考试类别查询成绩信息
                result = service.query2(
                    "select stuID,stuName,CONCAT(gradeName,className),subName,kindName,result from v_resultinfo where stuName like '%" + stuname + "%' and subName='" + subname + "' and kindName='" + kindname + "'")
        row = len(result)  # 取得记录个数，用于设置表格的行数
        if (len(self.tree.get_children()) > 0):
            for it in self.tree.get_children():
                self.tree.delete(it)  # 清空表格中的所有行
        for items in range(row):  # 遍历行
            self.tree.insert("", END, value=result[items])


    def bindCbox(self):
        result = service.query("select kindName from tb_examkinds")  # 从考试类别中查询数据
        self.cbGrade["value"] = ("所有",) + result
        result = service.query("select subName from tb_subject")  # 从考试科目中查询数据
        self.cbClass["value"] = ("所有",) + result
