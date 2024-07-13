# # -*- coding: utf-8 -*-
#
#


from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *
import sys
sys.path.append("../") # 返回上层路径
from service import service


class mainWindow():
    # 构造方法
    def __init__(self):
        self.MainWindow = Toplevel()
        self.MainWindow.geometry("307x267")
        self.MainWindow.title("班级设置")

        self.yscroll = Scrollbar(self.MainWindow)  # 滚动条
        self.yscroll.place(x=741, y=40, width=20, height=301)
        self.tree = Treeview(self.MainWindow, column=("classId", "GradeName", "className"), show="headings")
        self.yscroll.config(command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.yscroll.set)
        self.tree.heading("classId", text="班级编号")
        self.tree.column("classId", width=70)
        self.tree.heading("GradeName", text="所属年级")
        self.tree.column("GradeName", width=70)
        self.tree.heading("className", text="班级名称")
        self.tree.column("className", width=70)
        self.tree.place(x=3, y=0, width=301, height=161)
        Label(self.MainWindow, text="选择年级：").place(x=7, y=170, width=71, height=21)
        Label(self.MainWindow, text="班级编号：").place(x=6, y=200, width=71, height=21)
        Label(self.MainWindow, text="班级名称：").place(x=160, y=200, width=71, height=21)
        self.cbgradeset = StringVar()  # 选择年级
        self.cbgrade = Combobox(self.MainWindow, textvariable=self.cbgradeset)
        self.cbgrade.place(x=80, y=170, width=69, height=22)
        self.enclassNum = Entry(self.MainWindow)  # 班级编号
        self.enclassNum.place(x=80, y=200, width=71, height=20)
        self.enclassName = Entry(self.MainWindow)  # 班级名称
        self.enclassName.place(x=233, y=200, width=71, height=20)
        self.btn1 = Button(self.MainWindow, text="添加",command=self.add).place(x=22, y=231, width=51, height=27)
        self.btn3 = Button(self.MainWindow, text="修改",command=self.edit).place(x=92, y=231, width=51, height=27)
        self.btn2 = Button(self.MainWindow, text="删除",command=self.delete).place(x=162, y=231, width=51, height=27)
        self.btn4 = Button(self.MainWindow, text="退出", command=self.MainWindow.destroy).place(x=230, y=231, width=51, height=27)

        self.bindGrade()  # 绑定年级下拉列表
        self.query()  # 窗体加载时显示所有数据
        self.tree.bind("<Button-1>", self.getItem)
        self.MainWindow.mainloop()

    # 获取所有年级，显示在下拉列表中
    def bindGrade(self):
        result = service.query("select gradeName from tb_grade")  # 从年级表中查询数据
        self.cbgrade["value"] = result

    # 查询班级信息，并显示在表格中
    def query(self):
        self.result = service.query("select classID,gradeName,className from v_classinfo")  # 调用服务类中的公共方法执行查询语句
        self.row = len(self.result)  # 取得记录个数，用于设置表格的行数
        # 设置表格的标题名称
        if len(self.tree.get_children()) > 0:
            for it in self.tree.get_children():
                self.tree.delete(it)
        for i in range(self.row):  # 遍历行
            self.tree.insert("", END, value=self.result[i])

    # # 获取选中的表格内容
    def getItem(self, event):
        widget = event.widget
        item = widget.identify("item", event.x, event.y)
        colNum = widget.identify("column", event.x, event.y)
        if colNum == "#1":  # 如果单击的是第一列
            self.enclassNum.delete(0, END)
            self.enclassNum.insert(0, self.tree.set(item)["classId"])  # 获取班级编号
            self.enclassName.delete(0, END)
            self.enclassName.insert(0, self.tree.set(item)["className"])  # 获取班级名称
            self.cbgradeset.set(self.tree.set(item)["GradeName"])  # 所属年级

    # 判断要添加的记录是否存在
    def getName(self,cid, name):
        # 根据年级编号和班级名查询数据
        result = service.query("select * from tb_class where gradeID =%s and className = %s", cid, name)
        return len(result)  # 返回查询结果的记录

    # 添加班级信息
    def add(self):
        classID = self.enclassNum.get()  # 记录输入的班级编号
        className = self.enclassName.get()  # 记录输入的班级名称
        if self.cbgradeset.get() != "":  # 如果选择了年级
            # 获取年级对应的ID
            result = service.query("select gradeID from tb_grade where gradeName=%s", self.cbgradeset.get())
            if len(result) > 0:  # 如果结果大于0
                gradeID = result[0]  # 记录选择的年级对应的ID
                if classID != "" and className != "":  # 判断班级编号和班级名称不为空
                    if self.getName(gradeID, className) > 0:  # 判断已经存在该记录
                        self.enclassName.delete(0, END)  # 清空班级文本框
                        showinfo('提示', '您要添加的班级已经存在，请重新输入！')
                    else:
                        # 执行添加语句
                        result = service.exec("insert into tb_class(classID,gradeID,className) values (%s,%s,%s)",
                                              (classID, gradeID, className))
                        if result > 0:  # 如果结果大于0，说明添加成功
                            self.query()  # 在表格中显示最新数据
                            showinfo('提示', '信息添加成功！')
                else:
                    showwarning('警告', '请输入数据后，再执行相关操作！')
        else:
            showwarning('警告', '请先添加年级！')

    # 修改班级信息
    def edit(self):
        try:
            if self.tree.focus() != "":  # 判断是否选择了要修改的数据
                className = self.enclassName.get()  # 记录修改的班级名称
                if self.cbgradeset.get() != "":  # 如果选择了年级
                    # 获取年级对应的ID
                    result = service.query("select gradeID from tb_grade where gradeName=%s", self.cbgradeset.get())
                    if len(result) > 0:  # 如果结果大于0
                        gradeID = result[0]  # 记录选择的年级对应的ID
                        if className != "":  # 判断班级名称不为空
                            if self.getName(gradeID, className) > 0:  # 判断已经存在该记录
                                self.enclassName.delete(0, END)  # 清空班级文本框
                                showinfo('提示', '您要修改的班级已经存在，请重新输入！')
                            else:
                                # 执行修改操作
                                result = service.exec("update tb_class set gradeID=%s , className= %s where classID=%s",
                                                      (gradeID, className, self.enclassNum.get()))
                                if result > 0:  # 如果结果大于0，说明修改成功
                                    self.query()  # 在表格中显示最新数据
                                    showinfo('提示', '信息修改成功！')
        except:
            showwarning('警告', '请先选择要修改的数据！')

    # 删除班级信息
    def delete(self):
        try:
            if self.tree.focus() != "":  # 判断是否选择了要删除的数据

                # 执行删除操作
                result = service.exec("delete from tb_class where classID= %s",
                                      (self.tree.set(self.tree.focus())["classId"]))
                if result > 0:  # 如果结果大于0，说明删除成功
                    self.query()  # 在表格中显示最新数据
                    showinfo('提示', '信息删除成功！')
        except:
            showwarning('警告', '请先选择要删除的数据！')


# mainWindow()

# from tkinter import *
# from tkinter.ttk import *
# from tkinter.messagebox import *
# import sys
#
# sys.path.append("../")  # 返回上层路径
# from service import service
#
#
# # 获取所有年级，显示在下拉列表中
# def bindGrade():
#     result = service.query("select gradeName from tb_grade")  # 从年级表中查询数据
#     cbgrade["value"] = result
#
#
# # 查询班级信息，并显示在表格中
# def query():
#     result = service.query("select classID,gradeName,className from v_classinfo")  # 调用服务类中的公共方法执行查询语句
#     row = len(result)  # 取得记录个数，用于设置表格的行数
#      # 设置表格的标题名称
#     if len(tree.get_children())>0:
#         for it in tree.get_children():
#             tree.delete(it)
#     for i in range(row):  # 遍历行
#         tree.insert("",END,value=result[i])
#
# # # 获取选中的表格内容
# def getItem(event):
#     widget=event.widget
#     item=widget.identify("item",event.x,event.y)
#     colNum=widget.identify("column",event.x,event.y)
#     if colNum == "#1":  # 如果单击的是第一列
#         enclassNum.delete(0,END)
#         enclassNum.insert(0,tree.set(item)["classId"])        #获取班级编号
#         enclassName.delete(0, END)
#         enclassName.insert(0, tree.set(item)["className"])       #获取班级名称
#         cbgradeset.set(tree.set(item)["GradeName"])         #所属年级
# # 判断要添加的记录是否存在
# def getName(cid,name):
#     # 根据年级编号和班级名查询数据
#     result = service.query("select * from tb_class where gradeID =%s and className = %s", cid,name)
#     return len(result) # 返回查询结果的记录
# #添加班级信息
# def add():
#     classID = enclassNum.get()     # 记录输入的班级编号
#     className = enclassName.get()  # 记录输入的班级名称
#     if cbgradeset.get() !="": # 如果选择了年级
#         # 获取年级对应的ID
#         result=service.query("select gradeID from tb_grade where gradeName=%s",cbgradeset.get())
#         if len(result)>0: # 如果结果大于0
#             gradeID=result[0] # 记录选择的年级对应的ID
#             if classID != "" and className != "":  # 判断班级编号和班级名称不为空
#                 if getName(gradeID,className) > 0: # 判断已经存在该记录
#                     enclassName.delete(0,END) # 清空班级文本框
#                     showinfo('提示', '您要添加的班级已经存在，请重新输入！')
#                 else:
#                     # 执行添加语句
#                     result = service.exec("insert into tb_class(classID,gradeID,className) values (%s,%s,%s)", (classID, gradeID,className))
#                     if result > 0:  # 如果结果大于0，说明添加成功
#                         query()  # 在表格中显示最新数据
#                         showinfo( '提示', '信息添加成功！')
#             else:
#                 showwarning( '警告', '请输入数据后，再执行相关操作！')
#     else:
#         showwarning( '警告', '请先添加年级！')
#
# # 修改班级信息
# def edit():
#     try:
#         if tree.focus()!= "":  # 判断是否选择了要修改的数据
#             className = enclassName.get()  # 记录修改的班级名称
#             if cbgradeset.get() != "": # 如果选择了年级
#                 # 获取年级对应的ID
#                 result = service.query("select gradeID from tb_grade where gradeName=%s", cbgradeset.get())
#                 if len(result) > 0: # 如果结果大于0
#                     gradeID = result[0] # 记录选择的年级对应的ID
#                     if className!= "":  # 判断班级名称不为空
#                         if getName(gradeID,className) > 0: # 判断已经存在该记录
#                             enclassName.delete(0,END) # 清空班级文本框
#                             showinfo( '提示', '您要修改的班级已经存在，请重新输入！')
#                         else:
#                             # 执行修改操作
#                             result = service.exec("update tb_class set gradeID=%s , className= %s where classID=%s",
#                                                   (gradeID,className, enclassNum.get()))
#                             if result > 0:  # 如果结果大于0，说明修改成功
#                                 query()  # 在表格中显示最新数据
#                                 showinfo('提示', '信息修改成功！')
#     except:
#         showwarning('警告', '请先选择要修改的数据！')
#
#
# # 删除班级信息
# def delete():
#     try:
#         if tree.focus() != "":  # 判断是否选择了要删除的数据
#
#             # 执行删除操作
#             result = service.exec("delete from tb_class where classID= %s", (tree.set(tree.focus())["classId"]))
#             if result > 0:  # 如果结果大于0，说明删除成功
#                 query()  # 在表格中显示最新数据
#                 showinfo('提示', '信息删除成功！')
#     except:
#         showwarning('警告', '请先选择要删除的数据！')
# MainWindow = Tk()
# MainWindow.geometry("307x267")
# MainWindow.title("班级设置")
#
# yscroll = Scrollbar(MainWindow)  # 滚动条
# yscroll.place(x=741, y=40, width=20, height=301)
# tree = Treeview(MainWindow, column=("classId", "GradeName", "className"), show="headings")
# yscroll.config(command=tree.yview)
# tree.configure(yscrollcommand=yscroll.set)
# tree.heading("classId", text="班级编号")
# tree.column("classId", width=70)
# tree.heading("GradeName", text="所属年级")
# tree.column("GradeName", width=70)
# tree.heading("className", text="班级名称")
# tree.column("className", width=70)
# tree.place(x=3, y=0, width=301, height=161)
# Label(MainWindow, text="选择年级：").place(x=7, y=170, width=71, height=21)
# Label(MainWindow, text="班级编号：").place(x=6, y=200, width=71, height=21)
# Label(MainWindow, text="班级名称：").place(x=160, y=200, width=71, height=21)
# cbgradeset = StringVar()      # 选择年级
# cbgrade = Combobox(MainWindow, textvariable=cbgradeset)
# cbgrade.place(x=80, y=170, width=69, height=22)
# enclassNum = Entry(MainWindow)    #班级编号
# enclassNum.place(x=80, y=200, width=71, height=20)
# enclassName = Entry(MainWindow)    #班级名称
# enclassName.place(x=233, y=200, width=71, height=20)
# Button(MainWindow, text="添加",command=add).place(x=22, y=231, width=51, height=27)
# Button(MainWindow, text="修改",command=edit).place(x=92, y=231, width=51, height=27)
# Button(MainWindow, text="删除",command=delete).place(x=162, y=231, width=51, height=27)
# Button(MainWindow, text="退出").place(x=230, y=231, width=51, height=27)
#
# bindGrade()  # 绑定年级下拉列表
# query()  # 窗体加载时显示所有数据
# tree.bind("<Button-1>",getItem)
# MainWindow.mainloop()
#
