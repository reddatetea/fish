#  _*_ coding:utf-8 _*_
# 开发团队：明日科技
# 开发人员：Administrator
# 文件名称：demo8.py
# 开发工具：PyCharm


# 修改mysql数据（未）
from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *
import pymysql

num = 0  # 当前被修改的行的ID（序列号）
x1 = ""  # 双击项目的行序列号
y1 = ""  # 双击项目的列序列号
val = ""  # 双击的单元格的值
iid = ""  # 双击项目的ID
book_title = ["ID", "name", "category", "price", "publish_time"]
book_heading = ["序列", "书名", "系列", "价格", "出版时间"]
# 打开数据库连接,参数1:主机名或IP；参数2：用户名；参数3：密码；参数4：数据库名称
db = pymysql.connect("localhost", "root", "admin", "mr")
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
def modi():
    if (entry.get() == ""):
        showerror("错误", "请添加完整信息")
        return False
    elif entry.get() == val:
        showinfo("警告", "信息未修改")
        return False
    else:
        info_id = tree.item(iid)["values"][0]        #要修改的数据的ID
        info_it = book_title[int(y1.replace("#", "")) - 1]            #要修改的项
        info_text = entry.get()                        #要修改的内容
        cursor.execute('UPDATE books SET '+info_it+' =%s WHERE ID=%s',(info_text, info_id))
        entry.delete(0, END)
        showinfo1()            #更新表格中的数据
def add1(event):
    global x1
    global y1
    global val
    global iid
    entry.delete(0, END)
    it = event.widget  # 双击的项目
    iid = it.identify("item", event.x, event.y)
    x1 = it.identify("row", event.x, event.y)
    y1 = it.identify("column", event.x, event.y)
    val = it.item(iid)["values"][int(y1.replace("#", "")) - 1]
    data_id = it.item(iid, "values")[0]  # 该条数据在MySQL中的ID
    entry.insert(INSERT, val)
    label.config(text=book_heading[int(y1.replace("#", "")) - 1] + ": ")
    item = event.widget.identify("item", event.x, event.y)
def showinfo1():
    # 使用 execute()  方法执行 SQL 查询
    cursor.execute("SELECT * FROM books")
    # 使用 fetchone() 方法获取所有数据.
    data = cursor.fetchall()
    row = cursor.rowcount  # 获取条数据
    item_num = len(tree.get_children())
    if item_num > 0:
        for item in tree.get_children():
            tree.delete(item)
    for i in range(row):  # 遍历数据
        tree.insert("", END, values=data[i])  # 将获取的数据显示在表格中
win = Tk()
win.title("修改图书数据信息")
frame = Frame(width=100, relief="groove")  # 放置文本框

label = Label(frame, text="修改：")
label.grid(row=0, column=0)
entry = Entry(frame)
entry.grid(row=0, column=1)
Button(frame, text="修改内容", command=modi).grid(row=0, column=2)
frame.grid(row=0, column=0)
tree = Treeview(win, columns=book_title, show="headings", height=5)
tree.grid(row=1, column=0, columnspan=9)
for it in range(len(book_heading)):
    tree.heading(book_title[it], text=book_heading[it])
    tree.column(book_title[it], width=120)
showinfo1()
tree.bind("<Double-Button-1>", add1)
win.mainloop()
