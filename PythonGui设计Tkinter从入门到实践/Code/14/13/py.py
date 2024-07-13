#  _*_ coding:utf-8 _*_
# 开发团队：明日科技
# 开发人员：Administrator
# 文件名称：demo8.py
# 开发工具：PyCharm


# 查询mysql数据
from tkinter import *
from tkinter.ttk import *
import pymysql

# 打开数据库连接,参数1:主机名或IP；参数2：用户名；参数3：密码；参数4：数据库名称
db = pymysql.connect("localhost", "root", "admin", "mr")
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

db.ping(reconnect=True)  # 如果数据库断开连接就重新进行连接
# 使用 execute()  方法执行 SQL 查询
cursor.execute('SELECT * FROM books')  # 先获取所有数据
data = cursor.fetchall()
row = cursor.rowcount  # 获取条数据


def checkInfo():
    keyWords = {"书名": 1, "系列": 2, "价格": 3, "出版时间": 4}  # 字典形式存储各标题对应的数据表中的列的列号
    getInfo = val.get()  # 列号
    mess = entry.get()  # 关键字
    showinfo(keyWords[getInfo], mess)


def showinfo(kw, value):
    global label
    label.destroy()                       #销毁label组件
    item_num = len(tree.get_children())
    if item_num > 0:                      # 清空上一次查询内容
        for item in tree.get_children():
            tree.delete(item)
    for i in range(row):  # 遍历数据      #将符合条件的数据添加到表中
        if data[i][int(kw)] == value:
            tree.insert("", END, values=data[i])  # 将获取的数据显示在表格中
    if len(tree.get_children())==0:             #没有查询到内容，给出文字提示
        label = Label(win, text="抱歉，没有找到你需要的信息", font=14)
        label.grid(row=1,column=0,columnspan=3)

db.close()  # 关闭数据库连接
win = Tk()
win.title("查询图书数据信息")
val = StringVar()
val.set("系列")
cb = Combobox(win, textvariable=val, values=("书名", "价格", "系列", "出版时间"))
cb.grid(pady=5, row=0, column=0)
entry = Entry(win)
entry.grid(row=0, column=1)
label=Label(win,text="抱歉，没有找到你需要的信息",font=14)
Button(win, text="查询", command=checkInfo).grid(row=0, column=2)
tree = Treeview(win, columns=("num", "name", "category", "price", "publish_time"), show="headings", height=5)
tree.grid(row=2, column=0, columnspan=3)
tree.heading("num", text="序列")  # 设置表格标题
tree.column("num",width=40)
tree.heading("name", text="书名")
tree.heading("category", text="系列")
tree.column("category",width=60)
tree.heading("price", text="价格")
tree.column("price",width=60)
tree.heading("publish_time", text="出版时间")
tree.column("publish_time",width=120)
win.mainloop()
