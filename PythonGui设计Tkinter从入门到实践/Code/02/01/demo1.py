#  _*_ coding:utf-8 _*_
# 开发团队：明日科技
# 开发人员：Administrator0
# 文件名称：demo.py
# 开发工具：PyCharm


from tkinter import *     #导入tkinter模块
win=Tk()                  #实例化窗口
win.title("这是一个ttk小demo")     #添加窗口标题
#添加按钮组件，然后设置样式
btn = Button(win,text="这只是一个按钮", font=14, relief="flat",bg="#00f5ff").pack(pady=20)
win.mainloop()  #让发程序继续执行，直到窗口被关闭，该行放置在程序的最后





