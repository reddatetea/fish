# 登录模块主要对输入的用户名和密码进行验证，
# 如果没有输入用户名和密码，或者输入错误，弹出提示框，
# 否则，进入学生成绩管理系统的主窗体。


from tkinter import *
from tkinter.ttk import *
from PIL import Image, ImageTk
from tkinter.messagebox import *
from service import service
import main
# import sys
class loginStudent():

    def __init__(self):
        self.loginwin = Tk()
        self.loginwin.title("系统登录")
        self.loginwin.resizable(0, 0)
        self.loginwin.geometry("437x260")
        self.img1 = Image.open("images/login.jpg")
        self.img = ImageTk.PhotoImage(self.img1)
        Label(self.loginwin, image=self.img).place(x=0, y=0, width=437, height=107)  # 顶部登录图像
        Label(self.loginwin, text="用户名：").place(x=120, y=140, width=61, height=21)  # 用户名
        self.EntryUser = Entry(self.loginwin)  # 用户名文本框
        self.EntryUser.place(x=193, y=140, width=141, height=20)
        Label(self.loginwin, text="密  码：").place(x=119, y=180, width=61, height=21)  # 密码
        self.EntryPwd = Entry(self.loginwin, show="*")  # 密码文本框
        self.EntryPwd.place(x=192, y=180, width=141, height=20)
        Button(self.loginwin, text="登录", command=lambda: self.openMain("")).place(x=190, y=220, width=61,height=23)  # 登录按钮
        Button(self.loginwin, text="退出", command=self.loginwin.destroy).place(x=270, y=220, width=61, height=23)  # 退出按钮
        self.EntryPwd.bind("<Return>", self.openMain)
        self.loginwin.mainloop()

    def openMain(self,event):
        service.userName = self.EntryUser.get()  # 全局变量，记录用户名
        userPwd = self.EntryPwd.get() == ""  # 记录用户密码

        if service.userName == "" or userPwd == "":
            showerror("错误", "请输入用户名和密码")
            return False
        else:
            result = service.query("select * from tb_user where userName = %s and userPwd = %s", service.userName, userPwd)
            if len(result) > 0:  # 如果查询结果大于0，说明存在该用户，可以登录
                main.mainWindow()

            else:
                self.EntryUser.delete(0, END)  # 清空用户名文本
                self.EntryPwd.delete(0, END)
                showwarning('警告', '请输入正确的用户名和密码！')


loginStudent()


