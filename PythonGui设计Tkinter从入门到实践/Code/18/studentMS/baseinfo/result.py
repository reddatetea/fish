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
        self.MainWindow.title("学生成绩管理")
        self.MainWindow.geometry("766x387")
        # 表格上方的内容
        Label(self.MainWindow, text="考试种类：").place(x=7, y=10, width=71, height=21)
        Label(self.MainWindow, text="选择年级：").place(x=160, y=10, width=71, height=21)
        Label(self.MainWindow, text="选择班级：").place(x=317, y=9, width=71, height=21)
        self.cbexamkinds = StringVar()  # 考试种类
        self.cbexamkinds.set("所有")

        self.cbExam = Combobox(self.MainWindow, textvariable=self.cbexamkinds)
        self.cbExam.place(x=80, y=10, width=69, height=22)
        self.cbgradeKinds = StringVar()  # 选择年级
        self.cbgradeKinds.set("所有")
        self.cbGrade = Combobox(self.MainWindow, textvariable=self.cbgradeKinds)
        self.cbGrade.place(x=233, y=10, width=69, height=22)
        self.cbclassKinds = StringVar()  # 选择班级
        self.cbclassKinds.set("所有")
        self.cbClass = Combobox(self.MainWindow, textvariable=self.cbclassKinds)
        self.cbClass.place(x=390, y=9, width=69, height=22)
        Button(self.MainWindow, text="刷新", command=self.query).place(x=470, y=3, width=51, height=31)
        Button(self.MainWindow, text="添加", command=self.add).place(x=530, y=3, width=51, height=31)
        Button(self.MainWindow, text="修改", command=self.edit).place(x=590, y=3, width=51, height=31)
        Button(self.MainWindow, text="删除", command=self.delete).place(x=650, y=3, width=51, height=31)
        Button(self.MainWindow, text="退出", command=self.MainWindow.destroy).place(x=710, y=3, width=51, height=31)

        # 表格

        self.yscroll = Scrollbar(self.MainWindow)  # 滚动条
        self.yscroll.place(x=741, y=40, width=20, height=301)
        self.tree = Treeview(self.MainWindow,
                             column=("Id", "stuId", "stuName", "stuclass", "stusub", "stuexamkd", 'stuscore'),
                             show="headings")
        self.yscroll.config(command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.yscroll.set)

        self.tree.heading("Id", text="编号")
        self.tree.column("Id", width=70)
        self.tree.heading("stuId", text="学生编号")
        self.tree.column("stuId", width=70)
        self.tree.heading("stuName", text="姓名")
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

        # 表格下方的内容

        Label(self.MainWindow, text="学生姓名：").place(x=473, y=355, width=71, height=21)
        Label(self.MainWindow, text="考试科目：").place(x=303, y=353, width=71, height=21)
        Label(self.MainWindow, text="成绩：").place(x=643, y=356, width=41, height=21)
        self.cbnameset = StringVar()  # 学生姓名
        self.cbnameset.set("所有")
        self.cbname = Combobox(self.MainWindow, textvariable=self.cbnameset)
        self.cbname.place(x=550, y=354, width=69, height=22)

        self.cbSubKinds = StringVar()  # 考试科目
        self.cbSubKinds.set("所有")
        self.cbSub = Combobox(self.MainWindow, textvariable=self.cbSubKinds)
        self.cbSub.place(x=380, y=353, width=69, height=22)
        self.tbResult = Entry(self.MainWindow)  # 成绩
        self.tbResult.place(x=687, y=356, width=71, height=20)

        # 绑定事件以及调用
        self.bindGrade()
        self.bindCbox("")
        self.query()
        self.cbGrade.bind("<<ComboboxSelected>>", self.bindClass)  # 选择年级以后，自动选择班级列表
        self.cbClass.bind("<<ComboboxSelected>>", self.bindCbox)  # 选择班级后，自动出现该班学生列表、考试科目和类别
        self.cbClass.bind("<<ComboboxSelected>>", self.bindStuName)  # 选择班级后，显示该班级所有学生列表
        self.tree.bind("<Button-1>", self.getItem)

        self.MainWindow.mainloop()

    # 获取所有年级，显示在下拉列表中
    def bindGrade(self):
        result = service.query("select gradeName from tb_grade")  # 从年级表中查询数据
        self.cbGrade["value"] = ("所有",) + result

    def bindCbox(self, event):
        result = service.query("select kindName from tb_examkinds")  # 从考试类别表中查询数据
        self.cbExam["value"] = ("所有",) + result
        result = service.query("select subName from tb_subject")  # 从考试科目表中查询数据
        self.cbSub["value"] = result
        self.cbname["value"] = result

    # 根据班级显示学生
    def bindStuName(self, event):
        # self.cboxStuName.clear()  # 清空列表
        result = service.query("select stuName from v_studentinfo where gradeName=%s and className=%s",
                               self.cbgradeKinds.get(), self.cbclassKinds.get())  # 从学生信息视图中查询数据
        self.cbname["value"] = ("所有",) + result

    # 根据年级获取相应班级，显示在下拉列表中
    def bindClass(self, event):
        result = service.query("select className from v_classinfo where gradeName=%s",
                               self.cbgradeKinds.get())  # 从班级视图中查询数据
        self.cbClass["value"] = ("所有",) + result

    # 获取选中的表格内容
    def getItem(self, event):
        it = event.widget.identify("item", event.x, event.y)
        columnNum = event.widget.identify("column", event.x, event.y)  # 所单击的列数
        if columnNum == "#1":
            mess = self.tree.set(it)["Id"]
            # 根据编号查询成绩信息
            result = service.query("select * from v_resultinfo where ID=%s", mess)
            print(result)
            self.cbexamkinds.set(result[0][3])  # 显示考试类别
            self.cbgradeKinds.set(result[0][6])  # 显示年级
            self.cbclassKinds.set(result[0][5])  # 显示班级
            self.cbnameset.set(result[0][2])  # 显示学生姓名
            self.cbSubKinds.set(result[0][4])  # 显示考试科目
            self.tbResult.delete(0, END)
            self.tbResult.insert(0, str(result[0][7]))  # 显示学生分数

    # 判断要添加的记录是否存在
    def getScore(self, sid, kindid, subid):
        # 根据年级编号和班级名查询数据
        result = service.query("select * from tb_result where stuID =%s and kindID=%s and subID=%s", sid, kindid, subid)
        return len(result)  # 返回查询结果的记录

    # 添加学生成绩信息
    def add(self):
        subname = self.cbSubKinds.get()  # 记录考试科目
        kindname = self.cbexamkinds.get()  # 记录考试类别
        gradename = self.cbgradeKinds.get()  # 记录年级
        classname = self.cbclassKinds.get()  # 记录班级
        stuname = self.cbnameset.get()  # 记录学生姓名
        score = self.tbResult.get()  # 记录输入的分数
        if kindname != "所有":  # 如果选择了考试类别
            # 获取选择的考试类别对应ID
            result = service.query("select kindID from tb_examkinds where kindName=%s", kindname)
            if len(result) > 0:
                kindID = result[0]
                if subname != "所有":  # 如果选择了考试科目
                    # 获取选择的考试科目对应ID
                    result = service.query("select subID from tb_subject where subName=%s", subname)
                    if len(result) > 0:
                        subID = result[0]
                        if stuname != "":  # 如果选择了学生姓名
                            # 获取学生对应的ID
                            result = service.query(
                                "select stuID from v_studentinfo where gradeName=%s and className=%s and stuName=%s",
                                gradename, classname, stuname)
                            if len(result) > 0:  # 如果结果大于0
                                stuID = result[0]  # 记录选择的学生对应的ID
                                if self.getScore(stuID, kindID, subID) <= 0:  # 判断是否已经存在相同记录
                                    if score != "":  # 如果输入了分数
                                        # 执行添加语句
                                        result = service.exec(
                                            "insert into tb_result(stuID,kindID,subID,result) values (%s,%s,%s,%s)",
                                            (stuID, kindID, subID, score))
                                        if result > 0:  # 如果结果大于0，说明添加成功
                                            self.query()  # 在表格中显示最新数据
                                            showinfo('提示', '信息添加成功！')
                                    else:
                                        showwarning('警告', '请输入分数！')
                                else:
                                    showwarning('警告', '该学生成绩记录已经存在，请核查！')
                        else:
                            showwarning('警告', '请先选择学生！')
                else:
                    showwarning('警告', '请先选择考试科目！')
        else:
            showwarning('警告', '请先选择考试类别！')

    # 修改学生成绩信息
    def edit(self):
        try:
            if self.tree.focus() != "":  # 判断是否选择了要修改的数据
                item = self.tree.set(self.tree.focus())
                ID = item["Id"]
                # ID = self.select  # 记录要修改的编号
                score = self.tbResult.get()  # 记录成绩
                # 执行修改操作
                result = service.exec("update tb_result set result=%s where ID=%s", (score, ID))
                if result > 0:  # 如果结果大于0，说明修改成功
                    self.query()  # 在表格中显示最新数据
                    showinfo('提示', '信息修改成功！')

        except:
            showwarning('警告', '请先选择要修改的数据！')

    # 删除学生成绩信息
    def delete(self):
        try:
            if self.tree.focus() != "":  # 判断是否选择了要删除的数据
                # 执行删除操作
                result = service.exec("delete from tb_result where ID= %s", (self.tree.set(self.tree.focus())["Id"]))
                if result > 0:  # 如果结果大于0，说明删除成功
                    self.query()  # 在表格中显示最新数据
                    showinfo('提示', '信息删除成功！')
        except:
            showwarning('警告', '请先选择要删除的数据！')

    # 查询学生成绩信息，并显示在表格中
    def query(self):
        item_num = len(self.tree.get_children())
        kindname = self.cbexamkinds.get()  # 记录选择的考试类别
        gradename = self.cbgradeKinds.get()  # 记录选择的年级
        classname = self.cbclassKinds.get()  # 记录选择的班级
        if kindname == "所有":
            if gradename == "所有":
                if classname == "所有" or classname == "":
                    # 获取所有学生的成绩信息
                    result = service.query(
                        "select ID,stuID,stuName,CONCAT(gradeName,className),subName,kindName,result from v_resultinfo")
                else:
                    # 获取指定班级的成绩信息
                    result = service.query(
                        "select ID,stuID,stuName,CONCAT(gradeName,className),subName,kindName,result from v_resultinfo where className=%s",
                        classname)
            else:
                if classname == "所有":
                    # 获取指定年级的成绩信息
                    result = service.query(
                        "select ID,stuID,stuName,CONCAT(gradeName,className),subName,kindName,result from v_resultinfo where gradeName=%s",
                        gradename)
                else:
                    # 获取指定年级指定班的成绩信息
                    result = service.query(
                        "select ID,stuID,stuName,CONCAT(gradeName,className),subName,kindName,result from v_resultinfo where gradeName=%s and className=%s",
                        gradename, classname)
        else:
            if gradename == "所有":
                if classname == "所有" or classname == "":
                    # 获取指定考试类别的所有学生成绩信息
                    result = service.query(
                        "select ID,stuID,stuName,CONCAT(gradeName,className),subName,kindName,result from v_resultinfo where kindName=%s",
                        kindname)
                else:
                    # 获取指定考试类别的指定班级的成绩信息
                    result = service.query(
                        "select ID,stuID,stuName,CONCAT(gradeName,className),subName,kindName,result from v_resultinfo where kindName=%s and className=%s",
                        kindname, classname)
            else:
                if classname == "所有":
                    # 获取指定考试类别的指定年级的成绩信息
                    result = service.query(
                        "select ID,stuID,stuName,CONCAT(gradeName,className),subName,kindName,result from v_resultinfo where kindName=%s and gradeName=%s",
                        kindname, gradename)
                else:
                    # 获取指定考试类别的指定年级指定班的成绩信息
                    result = service.query(
                        "select ID,stuID,stuName,CONCAT(gradeName,className),subName,kindName,result from v_resultinfo where kindName=%s and gradeName=%s and className=%s",
                        kindname, gradename, classname)
        row = len(result)  # 取得记录个数，用于设置表格的行数
        if item_num > 0:  # 清空上一次显示的数据信息
            for item in self.tree.get_children():
                self.tree.delete(item)
        for i in range(row):  # 遍历行
            self.tree.insert("", END, values=result[i])
        # 清空文本框以及下拉选项中选中的内容
