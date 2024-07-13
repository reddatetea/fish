# -*- coding: utf-8 -*-


from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *

sys.path.append("../")  # 返回上层路径
from service import service

class mainWindow():
    def __init__(self):
        self.MainWindow = Toplevel()
        self.MainWindow.geometry("307x267")
        self.MainWindow.title("年级设置")

        self.yscroll = Scrollbar(self.MainWindow)  # 滚动条
        self.yscroll.place(x=741, y=40, width=20, height=301)
        self.tree = Treeview(self.MainWindow, column=("gradeId", "gradename"), show="headings")
        self.yscroll.config(command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.yscroll.set)
        self.tree.heading("gradeId", text="年级编号")
        self.tree.column("gradeId", width=70)
        self.tree.heading("gradename", text="年级名称")
        self.tree.column("gradename", width=70)
        self.tree.place(x=3, y=0, width=301, height=161)
        Label(self.MainWindow, text="年级编号：").place(x=7, y=170, width=71, height=21)
        Label(self.MainWindow, text="年级名称：").place(x=160, y=170, width=71, height=21)
        self.gradenum = Entry(self.MainWindow)  # 年级编号
        self.gradenum.place(x=80, y=170, width=69, height=22)
        self.gradename = Entry(self.MainWindow)  # 年级名称
        self.gradename.place(x=233, y=170, width=71, height=20)
        Button(self.MainWindow, text="添加", command=self.add).place(x=22, y=231, width=51, height=27)
        Button(self.MainWindow, text="修改", command=self.edit).place(x=92, y=231, width=51, height=27)
        Button(self.MainWindow, text="删除", command=self.delete).place(x=162, y=231, width=51, height=27)
        Button(self.MainWindow, text="退出", command=self.MainWindow.destroy).place(x=230, y=231, width=51, height=27)

        self.query()  # 窗体加载时显示所有数据

        self.tree.bind("<Button-1>", self.getItem)
        self.MainWindow.mainloop()

# 查询考试类别信息，并显示在表格中
    def query(self):
        result = service.query("select * from tb_grade")  # 调用服务类中的公共方法执行查询语句
        row = len(result)  # 取得记录个数，用于设置表格的行数
        if len(self.tree.get_children()) > 0:
            for it in self.tree.get_children():
                self.tree.delete(it)
        for i in range(row):  # 遍历行
            self.tree.insert("", END, value=result[i])



    # 获取选中的表格内容
    def getItem(self,event):
        item = event.widget.identify("item", event.x, event.y)    #获取鼠标单击的组件
        colnum = event.widget.identify("column", event.x, event.y)    #获取鼠标单击的表格的列
        if colnum == "#1":  # 如果单击的是第一列
            self.gradenum.delete(0, END)
            self.gradenum.insert(0, self.tree.set(item)["gradeId"])
            self.gradename.delete(0, END)
            self.gradename.insert(0, self.tree.set(item)["gradename"])


    def getName(self,name):
        result = service.query("select * from tb_grade where gradeName = %s", name)
        return len(result)


    def add(self):
        gradeID = self.gradenum.get()  # 记录输入的类别编号
        gradeName = self.gradename.get()  # 记录输入的类别名称
        if gradeID != "" and self.gradename != "":  # 判断类别编号和类别名称不为空
            if self.getName(gradeName) > 0:
                self.gradename.delete(0, END)
                showinfo('提示', '您要添加的考试类别已经存在，请重新输入！')
            else:
                # 执行添加语句
                result = service.exec("insert into tb_grade(gradeID,gradeName) values (%s,%s)", (gradeID, gradeName))
                if result > 0:  # 如果结果大于0，说明添加成功
                    self.gradenum.delete(0, END)
                    self.gradename.delete(0, END)
                    self.query()  # 在表格中显示最新数据
                    showinfo('提示', '信息添加成功！')
        else:
            showwarning('警告', '请输入数据后，再执行相关操作！')

    # 删除考试类别信息
    def edit(self):
        try:
            if self.tree.focus() != "":  # 判断是否选择了要修改的数据
                gradeName = self.gradename.get()  # 记录修改的类别名称
                if gradeName != "":  # 判断类别名称不为空
                    if self.getName(gradeName) > 0:
                        self.gradename.delete(0, END)
                        showinfo('提示', '您要修改的考试类别已经存在，请重新输入！')
                    else:
                        # 执行修改操作
                        result = service.exec("update tb_grade set gradeName= %s where gradeID=%s",
                                          (gradeName, self.gradenum.get()))
                        if result > 0:  # 如果结果大于0，说明修改成功
                            self.query()  # 在表格中显示最新数据
                            showinfo('提示', '信息修改成功！')
        except:
            showwarning('警告', '请先选择要修改的数据！')


#     # 删除年级信息
    def delete(self):
        try:
            if self.tree.focus() != "":  # 判断是否选择了要删除的数据
                it = self.tree.set(self.tree.focus())["gradeId"]
                # 执行删除年级操作
                result = service.exec("delete from tb_grade where gradeID= %s", (it,))
                if result > 0:  # 如果结果大于0，说明删除成功
                    self.query()  # 在表格中显示最新数据
                # 删除年级下的所有班级
                result = service.exec("delete from tb_class where gradeID= %s", (it,))
                if result > 0:  # 如果结果大于0，说明删除成功
                    self.query()  # 在表格中显示最新数据
                showinfo('提示', '信息删除成功！')
        except:
            showwarning('警告', '请先选择要删除的数据！')


