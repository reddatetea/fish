# _*_coding:UTF-8 _*_
# 开发团队：明日科技
# 开发人员：pc
# 开发时间：2020/3/9  9:09
# 文件名称：demo1.PY
# 开发工具：PyCharm

# Scrollbar的使用

def gettext(event):
    str=""    #因为可以多选，所以定义字符串来存储选择结果
    index1 = fruites.curselection()  # 获取选中的项的内容
    # 通过for循环注意判断每个选项是否被选中
    for item in index1:
        str+=fruites.get(item)+"、"
    label.config(text="你选择了"+str)
from tkinter import *
win=Tk()
win.configure(bg="#F5D7C4")   #设置窗口背景颜色
win.geometry("240x240")          #设置窗口大小
label=Label(win,height=5,wraplength=190,justify="left",bg="#F1DAA1",relief="groove")
label.pack(side="top",fill="x",padx="10",pady="10")
scr1=Scrollbar(win)    #添加滚动条

# 列表框的选项
listitem=["苹果","香蕉","草莓","樱桃","梨","柚子","菠萝","橘子","葡萄","柠檬","奇异果","百香果","牛油果","西瓜"]
#通过yscrollcommand将列表框与滚动条绑定
fruites=Listbox(win,height=7,yscrollcommand=scr1.set,selectmode="multiple",justify="center",width=30)
for i in listitem:
    fruites.insert(END, i)     # 添加列表框中的选项
fruites.pack(side="left",fill="x")
fruites.bind("<<ListboxSelect>>",gettext)
scr1.pack(side="left",fill="y")
scr1.config(command=fruites.yview)
win.mainloop()
