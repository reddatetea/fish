# _*_coding:UTF-8 _*_
# 开发团队：明日科技
# 开发人员：pc
# 开发时间：2020/3/9  9:09
# 文件名称：demo1.PY
# 开发工具：PyCharm

# Combobox


from tkinter import *
from tkinter.ttk import *   #引入ttk模块

win = Tk()
win.title("Combobox的创建")
label1=Label(win,text="选择管理员身份：").grid(row=1,column=0,columnspan=2,pady=10)
#管理员身份
item=("蓝色妖姬", "烈焰焚情", "寒冰幽兰", "岁岁芳华", "朝暮盈霄","陌上花开")
# 添加选择管理员身份的组合框
useroption = Combobox(win, width=12, values=item)
useroption.grid(row=1,column=2,pady=10)      # 设置其在界面中出现的位置  column代表列   row 代表行
useroption.current(0)    # 设置下拉列表默认显示的值，0为 item 的值
label2=Label(win,text="查看类别：").grid(row=2,pady=10,columnspan=2)
# 添加报表类别的选项
numberChosen = Combobox(win, width=12, values=("进销总览", "销量", "库存", "进售价", "账单"))
numberChosen.grid(row=2,column=2,pady=10)
numberChosen.current(0)
button=Button(win,text="提交").grid(row=3,columnspan=4,pady=10)
win.mainloop()

