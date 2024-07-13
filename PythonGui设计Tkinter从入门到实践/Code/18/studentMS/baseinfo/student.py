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
        self.MainWindow.title("学生管理")
        self.MainWindow.geometry("766x417")
        # 第一行
        Label(self.MainWindow, text="所属年级:").place(x=160, y=10, width=71, height=21)
        Label(self.MainWindow, text="所属班级:").place(x=317, y=9, width=71, height=21)
        Button(self.MainWindow, text="刷新", command=self.query).place(x=470, y=3, width=51, height=31)
        Button(self.MainWindow, text="添加", command=self.add).place(x=530, y=3, width=51, height=31)
        Button(self.MainWindow, text="修改", command=self.edit).place(x=590, y=3, width=51, height=31)
        Button(self.MainWindow, text="删除", command=self.delete).place(x=650, y=3, width=51, height=31)
        Button(self.MainWindow, text="退出", command=self.MainWindow.destroy).place(x=710, y=3, width=51, height=31)
        self.cbgradeKinds = StringVar()  # 选择年级
        self.cbgradeKinds.set("所有")
        self.cbGrade = Combobox(self.MainWindow, textvariable=self.cbgradeKinds)
        self.cbGrade.place(x=233, y=10, width=69, height=22)
        self.cbclassKinds = StringVar()  # 选择班级
        self.cbclassKinds.set("所有")
        self.cbClass = Combobox(self.MainWindow, textvariable=self.cbclassKinds)
        self.cbClass.place(x=390, y=9, width=69, height=22)
        self.yscroll = Scrollbar(self.MainWindow)  # 滚动条
        self.yscroll.place(x=741, y=40, width=20, height=301)
        self.tree = Treeview(self.MainWindow, column=("stuId", "stuName", "stuclass", "sex", "age", 'addr', 'phone'),
                             show="headings")
        self.yscroll.config(command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.yscroll.set)

        self.tree.heading("stuId", text="学生编号")
        self.tree.column("stuId", width=70)
        self.tree.heading("stuName", text="学生姓名")
        self.tree.column("stuName", width=70)
        self.tree.heading("stuclass", text="班级")
        self.tree.column("stuclass", width=70)
        self.tree.heading("sex", text="性别")
        self.tree.column("sex", width=70)
        self.tree.heading("age", text="年龄")
        self.tree.column("age", width=70)
        self.tree.heading("addr", text="家庭住址")
        self.tree.column("addr", width=70)
        self.tree.heading("phone", text="联系电话")
        self.tree.column("phone", width=70)
        self.tree.place(x=0, y=40, width=741, height=301)

        # 表格下方第一行
        Label(self.MainWindow, text="学生编号：").place(x=123, y=353, width=71, height=21)
        Label(self.MainWindow, text="学生姓名：").place(x=293, y=353, width=71, height=21)
        Label(self.MainWindow, text="年龄：").place(x=463, y=353, width=41, height=21)
        Label(self.MainWindow, text="性别：").place(x=597, y=353, width=41, height=21)
        self.enStuId = Entry(self.MainWindow)  # 学生编号
        self.enStuId.place(x=197, y=353, width=71, height=20)
        self.enStuName = Entry(self.MainWindow)  # 学生姓名
        self.enStuName.place(x=357, y=353, width=71, height=20)
        self.enStuAge = Entry(self.MainWindow)  # 年龄
        self.enStuAge.place(x=507, y=353, width=71, height=20)
        self.stuSex = StringVar()
        self.stuSex.set("男")
        self.cbsex = Combobox(self.MainWindow, value=("男", "女"), textvariable=self.stuSex)
        self.cbsex.place(x=647, y=353, width=51, height=22)

        # 表格下第二行
        Label(self.MainWindow, text="联系电话：").place(x=123, y=383, width=71, height=21)
        Label(self.MainWindow, text="家庭住址：").place(x=343, y=383, width=711, height=21)
        self.enStuPhone = Entry(self.MainWindow)  # 联系电话
        self.enStuPhone.place(x=197, y=383, width=121, height=20)
        self.enStuAddr = Entry(self.MainWindow)  # 家庭住址
        self.enStuAddr.place(x=417, y=383, width=281, height=20)

        # 绑定方法
        self.bindGrade()  # 绑定年级下拉列表

        self.cbGrade.bind("<<ComboboxSelected>>", self.bindClass)  # 选择年级以后，自动选择班级列表

        self.tree.bind("<Button-1>", self.getItem)
        self.query()
        self.MainWindow.mainloop()

    # 获取所有年级，显示在下拉列表中
    def bindGrade(self):
        result = service.query("select gradeName from tb_grade")  # 从年级表中查询数据
        self.cbGrade["value"] = ("所有",) + result

    # 根据年级获取相应班级，显示在下拉列表中
    def bindClass(self, event):
        result = service.query("select className from v_classinfo where gradeName=%s",
                               self.cbgradeKinds.get())  # 从年级视图中查询数据
        self.cbClass["value"] = ("所有",) + result

    # 查询学生信息，并显示在表格中
    def query(self):
        gname = self.cbgradeKinds.get()  # 记录选择的年级
        cname = self.cbclassKinds.get()  # 记录选择的班级
        # 获取所有学生信息
        if gname == "所有":
            result = service.query(
                "select stuID,stuName,CONCAT(gradeName,className),sex,age,address,phone from v_studentinfo")
        # 获取指定年级学生信息
        elif gname != "所有" and cname == "所有":
            result = service.query(
                "select stuID,stuName,CONCAT(gradeName,className),sex,age,address,phone from v_studentinfo where gradeName=%s",
                gname)
        # 获取指定年级指定班的学生信息
        elif gname != "所有" and cname != "所有":
            result = service.query(
                "select stuID,stuName,CONCAT(gradeName,className),sex,age,address,phone from v_studentinfo where gradeName=%s and className=%s",
                gname, cname)
        row = len(result)  # 取得记录个数，用于设置表格的行数
        if (len(self.tree.get_children()) > 0):
            for it in self.tree.get_children():
                self.tree.delete(it)
        for i in range(row):
            self.tree.insert("", END, value=result[i])
        self.enStuId.delete(0, END)
        self.enStuName.delete(0, END)
        self.enStuAge.delete(0, END)
        self.stuSex.set("男")
        self.enStuPhone.delete(0, END)
        self.enStuAddr.delete(0, END)

    # 添加学生信息
    def add(self):
        stuID = self.enStuId.get()  # 记录学生编号
        stuName = self.enStuName.get()  # 记录学生姓名
        age = self.enStuAge.get()  # 记录年龄
        sex = self.stuSex.get()  # 记录性别
        phone = self.enStuPhone.get()  # 记录电话
        address = self.enStuAddr.get()  # 记录地址
        if self.cbgradeKinds.get() != "" and self.cbgradeKinds.get() != "所有":  # 如果选择了年级
            # 获取年级对应的ID
            result = service.query("select gradeID from tb_grade where gradeName=%s", self.cbgradeKinds.get())
            if len(result) > 0:  # 如果结果大于0
                gradeID = result[0]  # 记录选择的年级对应的ID
                if self.cbclassKinds.get() != "" and self.cbclassKinds.get() != "所有":  # 如果选择了班级
                    # 获取班级对应的ID
                    result = service.query("select classID from tb_class where gradeID=%s and className=%s", gradeID,
                                           self.cbclassKinds.get())
                    if len(result) > 0:  # 如果结果大于0
                        classID = result[0]  # 记录选择的班级对应的ID
                        if stuID != "" and stuName != "":  # 判学生编号和学生姓名不为空
                            if self.getName(stuID) > 0:  # 判断已经存在该记录
                                self.enStuId.delete(0, END)  # 清空学生编号文本框
                                showinfo('提示', '您要添加的学生编号已经存在，请重新输入！')
                            else:
                                # 执行添加语句
                                result = service.exec(
                                    "insert into tb_student(stuID,stuName,classID,gradeID,age,sex,phone,address) values (%s,%s,%s,%s,%s,%s,%s,%s)",
                                    (stuID, stuName, classID, gradeID, age, sex, phone, address))
                                if result > 0:  # 如果结果大于0，说明添加成功
                                    self.query()  # 在表格中显示最新数据
                                    showinfo('提示', '信息添加成功！')
                else:
                    showwarning('警告', '请输入数据后，再执行相关操作！')
        else:
            showwarning('警告', '请先添加年级！')

    # 判断要添加的记录是否存在

    # 修改学生信息
    def edit(self):
        try:
            if self.tree.focus() != "":  # 判断是否选择了要修改的数据
                message = self.tree.set(self.tree.focus())
                stuID = message["stuId"]  # 记录要修改的学生编号
                age = self.enStuAge.get()  # 记录年龄
                sex = self.stuSex.get()  # 记录性别
                phone = self.enStuPhone.get()  # 记录电话
                address = self.enStuAddr.get()  # 记录地址
                # 执行修改操作
                result = service.exec("update tb_student set age=%s ,sex= %s,phone= %s,address= %s where stuID=%s",
                                      (age, sex, phone, address, stuID))
                if result > 0:  # 如果结果大于0，说明修改成功
                    self.query()  # 在表格中显示最新数据
                    showinfo('提示', '信息修改成功！')
        except:
            showwarning('警告', '请先选择要修改的数据！')

    # 删除学生信息
    def delete(self):
        try:
            if self.tree.focus() != "":  # 判断是否选择了要删除的数据
                mess = self.tree.set(self.tree.focus())["stuId"]
                # 执行删除操作
                result = service.exec("delete from tb_student where stuID= %s", (mess,))
                if result > 0:  # 如果结果大于0，说明删除成功
                    self.query()  # 在表格中显示最新数据
                    showinfo('提示', '信息删除成功！')
        except:
            showwarning('警告', '请先选择要删除的数据！')

    def getName(self, sid):
        # 根据年级编号和班级名查询数据
        result = service.query("select * from tb_student where stuID =%s", sid)
        return len(result)  # 返回查询结果的记录

        # 获取选中的表格内容

    def getItem(self, event):
        it = event.widget
        columnNum = it.identify("column", event.x, event.y)  # 所单击的列数

        if columnNum == "#1":  # 如果单击的是第一列
            mess = self.tree.set(it.identify("item", event.x, event.y))
            self.enStuId.delete(0, END)
            self.enStuId.insert(0, mess["stuId"])
            # 根据学生编号查询学生信息
            result = service.query("select * from v_studentinfo where stuID=%s", mess["stuId"])
            self.enStuName.delete(0, END)  # 显示学生姓名
            self.enStuName.insert(0, mess["stuName"])
            self.enStuAge.delete(0, END)  # 显示年龄
            self.enStuAge.insert(0, mess["age"])
            self.stuSex.set(mess["sex"])  # 显示学生性别
            self.cbgradeKinds.set(mess["stuclass"][:2])  # 获取年级
            self.cbclassKinds.set(mess["stuclass"][2:])  # 获取班级
            self.enStuPhone.delete(0, END)  # 显示联系电话
            self.enStuPhone.insert(0, mess["phone"])
            self.enStuAddr.delete(0, END)  # 显示家庭住址
            self.enStuAddr.insert(0, mess["addr"])
