# _*_coding:UTF-8 _*_
# 开发团队：明日科技
# 开发人员：pc
# 开发时间：2020/3/9  9:09
# 文件名称：demo1.PY
# 开发工具：PyCharm

#place()的使用
#width和 height,x和y

from tkinter import *
win=Tk()
win.title("华容道")     # 添加窗口标题
win.geometry("240x300")      # 设置窗口大小
txt1=Label(win,text="赵云",bg="#FF1493",relief="solid",font=14)    #华容道游戏中的滑块
txt2=Label(win,text="曹操",bg="#EEEE00",relief="solid",font=14)
txt3=Label(win,text="黄忠",bg="#FF1493",relief="solid",font=14)
txt4=Label(win,text="张飞",bg="#FF1493",relief="solid",font=14)
txt5=Label(win,text="关羽",bg="#FF1493",relief="solid",font=14)
txt6=Label(win,text="马超",bg="#FF1493",relief="solid",font=14)
txt7=Label(win,text="卒",bg="#9932CC",relief="solid",font=14)
txt8=Label(win,text="卒",bg="#9932CC",relief="solid",font=14)
txt9=Label(win,text="卒",bg="#9932CC",relief="solid",font=14)
txt0=Label(win,text="卒",bg="#9932CC",relief="solid",font=14)
# width为组件宽度，height为组件高度，x为滑块左上角定点的横坐标，y为滑块左上角的纵坐标
txt1.place(width=60,height=120,x=0,y=0)
txt2.place(width=120,height=120,x=60,y=0)
txt3.place(width=60,height=120,x=180,y=0)
txt4.place(width=60,height=120,x=0,y=120)
txt5.place(width=120,height=60,x=60,y=120)
txt6.place(width=60,height=120,x=180,y=120)
txt7.place(width=60,height=60,x=60,y=180)
txt8.place(width=60,height=60,x=120,y=180)
txt9.place(width=60,height=60,x=0,y=240)
txt0.place(width=60,height=60,x=180,y=240)
win.mainloop()
