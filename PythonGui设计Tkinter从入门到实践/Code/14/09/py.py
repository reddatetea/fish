#  _*_ coding:utf-8 _*_
# 开发团队：明日科技
# 开发人员：Administrator
# 文件名称：demo8.py
# 开发工具：PyCharm

# 显示mysql数据
from tkinter import *
from tkinter.ttk import *
import pymysql


# 打开数据库连接,参数1:主机名或IP；参数2：用户名；参数3：密码；参数4：数据库名称
db = pymysql.connect("localhost", "root", "admin", "mr")
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
# 使用 execute()  方法执行 SQL 查询
cursor.execute("SELECT * FROM books")
# 使用 fetchone() 方法获取所有数据.
data = cursor.fetchall()
row=cursor.rowcount    #获取条数据

win=Tk()
win.title("查看图书数据信息")
tree=Treeview(win,columns=("num","name","category","price","publish_time"),show="headings")
tree.pack()
tree.heading("num", text="序列")  # 设置表格标题
tree.column("num",width=40)
tree.heading("name", text="书名")
tree.heading("category", text="系列")
tree.column("category",width=60)
tree.heading("price", text="价格")
tree.column("price",width=60)
tree.heading("publish_time", text="出版时间")
tree.column("publish_time",width=120)
for i in range(row):                           # 遍历数据
    tree.insert("",END,values=data[i])       #将获取的数据显示在表格中
db.close()            # 关闭数据库连接
win.mainloop()




