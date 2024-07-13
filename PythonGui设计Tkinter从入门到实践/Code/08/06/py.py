# _*_coding:UTF-8 _*_
# 开发团队：明日科技
# 开发人员：pc
# 开发时间：2020/3/16  20:08
# 文件名称：demo2.PY
# 开发工具：PyCharm


from tkinter import *

pw = PanedWindow(showhandle=True, sashrelief=SUNKEN, orient=VERTICAL, width=300, handlesize=10, handlepad=20)
pw.pack(fill=BOTH, expand=1)
top = Label(pw, text='虽然只是个面板，但是它的大小可以改变', background="#E0FFFF")
pw.add(top)
bottom = Label(pw, text='拖动左侧的开关试试', background="#FFFFE0")
pw.add(bottom)
mainloop()
