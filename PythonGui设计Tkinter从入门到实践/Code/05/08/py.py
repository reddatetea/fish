# _*_coding:UTF-8 _*_
# 开发团队：明日科技
# 开发人员：pc
# 开发时间：2020/3/9  9:09
# 文件名称：demo1.PY
# 开发工具：PyCharm

# Spinbox组件
# 设置spinbox内容以及获取当前值

from tkinter import *
def show():
    #在文本框中添加时间与星期
    info.insert("insert", "\t时间:%s月%s日 %s\n" % (spmon.get(), spdat.get(), spwek.get(),))
win = Tk()
win.title("留言本")
mess=Label(win,text="请添加你的留言：").grid(row=0,column=0,columnspan=5,pady=10)
spmon=Spinbox(win,from_=1,to=12,width=10)     #选择月份
spmon.grid(row=1,column=0,pady=10)
mon=Label(win,text="月").grid(row=1,column=1,pady=10)
spdat=Spinbox(win,from_=1,to=30,width=10)     #选择日期
spdat.grid(row=1,column=2,pady=10)
dat=Label(win,text="日").grid(row=1,column=3,pady=10)
spwek=Spinbox(win,values=("星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"),width=10)   #选择星期
spwek.grid(row=1,column=5,columnspan=3,pady=10)
info=Text(win,bg="#BFEFFF",width=50,height=10)     #添加日记内容的文本框
get1 = Button(win, text='提交',width=30 ,bg="#EDB89E",command=show).grid(row=3,columnspan=10,pady=10)
info.grid(row=2,columnspan=10)
win.mainloop()
