# _*_coding:UTF-8 _*_
# 开发团队：明日科技
# 开发人员：pc
# 开发时间：2020/3/12  17:22
# 文件名称：demo2.PY
# 开发工具：PyCharm

# Listbox的高级使用

from tkinter import *
# 该方法的第一个参数原列表，第二个是目标列表
def add(from1,to1):
    # from1.curselection()  为获取选中的项的序号元祖
    item1=from1.get(from1.curselection())    #获取选中的项的内容
    to1.insert(END,item1)                    #在目标列表中插入选项
    from1.delete(from1.curselection())       #删除原目标组中的该选项

win=Tk()
win.title("添加快捷消息列表")
win.geometry("250x200")
Label(win,text="系统信号").grid(row=0,column=0)
Label(win,text="快捷信号").grid(row=0,column=2)
# 列表内容
val1=StringVar()      #系统信号
val1.set("发起进攻 请求集合 小心草丛 跟着我")
val2=StringVar()      #快捷信号
val2.set("开始撤退 清理兵线 回防高地 请求支援")
# 添加列表组件
listbox1 = Listbox(win, bg="#FFF8DC", selectbackground="#D15FEE", selectmode="single",listvariable=val1, height=8, width=10)
listbox2 = Listbox(win, bg="#C1FFC1", selectbackground="#D15FEE", selectmode="single",listvariable=val2, height=8, width=10)
listbox1.grid(row=1,column=0,rowspan=2)
listbox2.grid(row=1,column=2,rowspan=2)
btn1=Button(win,text=">>>",command=lambda :add(listbox1,listbox2)).grid(row=1,column=1,padx=10)
btn2=Button(win,text="<<<",command=lambda :add(listbox2,listbox1)).grid(row=2,column=1,padx=10)
win.mainloop()