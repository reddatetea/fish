# _*_coding:UTF-8 _*_
# 开发团队：明日科技
# 开发人员：pc
# 开发时间：2020/3/9  9:09
# 文件名称：demo1.PY
# 开发工具：PyCharm

# OptionMenu高级使用
from tkinter import *
def result():
    #判断选择是否正确
    if v.get()==items[2]:
        re.config(text="答对了")
    else:
        re.config(text="答错了，小偷是"+items[2])
win = Tk()
win.title("逻辑推理谁是小偷")   #设置窗口标题
win.configure(bg="#ffffcc")
# 创建一个OptionMenu控件
text=Text(win,width=50,height=13,bg="#ffffcc",font=14,relief="flat")
#题目
ques="一位警察，抓获四个盗窃嫌疑犯，张三、李四、王二、麻子，而他们的供词如下：\n\n张三说：“不是我偷的”。\n\n李四说：“是张三偷的”。\n\n王二说：“不是我”。\n\n麻子说：“是李四偷的”。\n\n他们四人只有一人说了真话，你知道谁是小偷吗？\n"
text.insert(END,ques)   #向文本框增加内容
text.grid(row=1,columnspan=4)
text.config(state="disabled")   #设置文本不可编辑

items = ("张三","李四","王二","麻子")     # 答案选项
v = StringVar(win)
v.set(items[0])                           #设置默认答案
om = OptionMenu(win,v,*items)
om.grid(row=2,columnspan=2)
button=Button(win,text="确定",command=result).grid(row=2,column=1,columnspan=2)
re=Label(win,padx=5,pady=5,width=60)
re.grid(row=3,column=0,columnspan=3)
win.mainloop()

