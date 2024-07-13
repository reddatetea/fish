#  _*_ coding:utf-8 _*_
# 开发团队：明日科技
# 开发人员：Administrator
# 文件名称：scale1.py
# 开发工具：PyCharm

i = 0   #单击按钮的次数，初始值为0


def show():
    global i  #声明为全局变量
    i += 1   #单击一次按钮，ijiu就加1
    label.config(text="你点了我\t" + str(i) + "下")


from tkinter import *

root = Tk()        #创建根窗口
text = Text(root, width=70, height=20, bg="#CAE1FF", relief="solid",font=14)   #创建多行文本框

photo = PhotoImage(file='ico.png')        # 创建了一个图象对象
text.image_create(END, image=photo)       # text中插入图像
text.insert(INSERT, "在这里添加文本:\n")  # 添加文本
text.pack()       #包装文本框，没有此步骤，文本框无法显示在窗口中
# 插入组件
bt = Button(root, text='你点我试试', command=show, padx=10)  #创建按钮
text.window_create("2.end", window=bt)  # 将按钮放置在text中
label = Label(root, padx=10, text="你点了我0下")   #创建Label组件
text.window_create("3.end", window=label)  # 将Label组件放置在text中
root.mainloop()
