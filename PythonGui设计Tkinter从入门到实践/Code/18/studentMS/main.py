# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!

from tkinter import *
from tkinter.ttk import *
from PIL import Image,ImageTk
import datetime
from service import service
from settings import classes, examkinds, grade, subject
from baseinfo import result, student
from query import resultinfo, studentinfo
from system import user
import sys


class mainWindow():

    def __init__(self):
        self.win = Toplevel()
        self.win.title("学生成绩管理系统")
        self.win.iconbitmap("images/appstu.ICO")
        self.win.geometry("521x395")
        self.win.after(1000, self.timeUpdate)


        # 菜单
        self.menuMain = Menu()
        self.menu1 = Menu(self.menuMain, tearoff=False)
        self.menu2 = Menu(self.menuMain, tearoff=False)
        self.menu3 = Menu(self.menuMain, tearoff=False)
        self.menu4 = Menu(self.menuMain, tearoff=False)
        self.menuMain.add_cascade(label="基础设置", menu=self.menu1)
        self.menuMain.add_cascade(label="基本信息设置", menu=self.menu2)
        self.menuMain.add_cascade(label="系统查询", menu=self.menu3)
        self.menuMain.add_cascade(label="系统管理", menu=self.menu4)
        # 二级菜单
        self.actionGrade = Menu(self.menu1, tearoff=False)
        self.actionClass = Menu(self.menu1, tearoff=False)
        self.actionSubject = Menu(self.menu1, tearoff=False)
        self.actionExamkinds = Menu(self.menu1, tearoff=False)
        self.actionStudent = Menu(self.menu2, tearoff=False)
        self.actionResult = Menu(self.menu2, tearoff=False)
        self.actionStudentInfo = Menu(self.menu3, tearoff=False)
        self.actionResultInfo = Menu(self.menu3, tearoff=False)
        self.actionUserInfo = Menu(self.menu4, tearoff=False)
        self.actionExit = Menu(self.menu4, tearoff=False)
        # 定义二级菜单上显示的文字以及执行的事件（跳转到相应窗口）
        self.menu1.add_command(label="年级设置", command=grade.mainWindow)
        self.menu1.add_command(label="班级设置", command=classes.mainWindow)
        self.menu1.add_command(label="考试科目设置", command=subject.mainWindow)
        self.menu1.add_command(label="考试类别", command=examkinds.mainWindow)
        self.menu2.add_command(label="学生管理", command=student.mainWindow)
        self.menu2.add_command(label="成绩管理", command=result.mainWindow)
        self.menu3.add_command(label="学生信息查询", command=studentinfo.mainWindow)
        self.menu3.add_command(label="学生成绩查询", command=resultinfo.mainWindow)
        self.menu4.add_command(label="用户维护", command=user.mainWindow)
        self.menu4.add_command(label="退出", command=self.win.destroy)

        # 添加背景图像
        self.img1 = Image.open("images/main.jpg")
        self.mainImage1 = ImageTk.PhotoImage(self.img1)

        self.label = Label(self.win, image=self.mainImage1).place(x=0, y=0, width=521, height=348)
        # 添加系统信息，包括当前用户、事件以及版权信息
        self.labelInfo = Label(self.win,
                               text="  当前登录用户：" + service.userName + " | 登录时间：" + datetime.datetime.now().strftime(
                                   '%Y-%m-%d %H:%M:%S') + "  | 版权所有：吉林省明日科技有限公司")
        self.labelInfo.place(x=0, y=350, width=521, height=24)
        self.win.config(menu=self.menuMain)
        self.win.mainloop()

    # 显示时间
    def timeUpdate(self):
        global labelInfo
        self.time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.labelInfo.config(text="  当前登录用户：" + service.userName + " | 登录时间：" + self.time + "  | 版权所有：吉林省明日科技有限公司")
        self.win.after(100, self.timeUpdate)   # 每隔一秒，时间变化一次
