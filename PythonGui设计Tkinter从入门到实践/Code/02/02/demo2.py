#  _*_ coding:utf-8 _*_
# 开发团队：明日科技
# 开发人员：Administrator
# 文件名称：demo1.py
# 开发工具：PyCharm9

import tkinter
from tkinter import ttk      #导入ttk

root = tkinter.Tk()
root.title("这是一个ttk小demo")
ttk.Style().configure("TButton", font=14, relief="flat",background="#00f5ff")    #通过Style()设置样式
btn = ttk.Button(text="这只是一个按钮",style="TButton").pack(pady=20)            #添加Button组件，并且引入样式
root.mainloop()

