# _*_coding:UTF-8 _*_
# 开发团队：明日科技
# 开发人员：pc
# 开发时间：2020/3/9  9:09
# 文件名称：demo1.PY
# 开发工具：PyCharm

from tkinter import *

win = Tk()                                               #创建根窗口
txt1 = "暮冬时烤雪"                                      #第一行文字
txt2 = "迟夏写长信"                                      #第二行文字
txt3 = "早春不过一棵树"                                  #第三行文字
#在pack()方法中通过side参数设置排列方式为从左向右依次排列
Label(win, text=txt1, bg="#F5DFCC").pack(side="left")
Label(win, text=txt2, bg="#EDB584").pack(side="left")
Label(win, text=txt3, bg="#EF994C").pack(side="left")
win.mainloop()
