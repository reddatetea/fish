# _*_coding:UTF-8 _*_
# 开发团队：明日科技
# 开发人员：pc
# 开发时间：2020/3/9  9:09
# 文件名称：demo1.PY
# 开发工具：PyCharm

OptionMenu的初级使用
from tkinter import *
win = Tk()   #创建根窗口
win.geometry("150x220")
win.title("OptionMenu的创建")
Label(text="我的歌单：").pack(fill="x",anchor="w")
#通过元组存储选项
list=('逞强---刘洋洋','时间的过客---名诀', '情深几许---香子',
      '我爱---袁娅维', '一个人挺好---梦颖','世间美好---夏艺涵','念旧---阿悠悠')
v = StringVar(win)
	#通过“*”+元组，设置下拉列表的选项
om = OptionMenu(win,v,*list).pack(fill="x")
win.mainloop()


