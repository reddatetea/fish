#  _*_ coding:utf-8 _*_
# 开发团队：明日科技
# 开发人员：Administrator
# 文件名称：示例代码.py
# 开发工具：PyCharm

def result1():
    # sel=re.cget("text")
    sel=""
    for i in range(len(str1)):
        # 判断是否选中
        if(check[i].get()==1):
            sel=sel+str1[i]+" "
    # 更新Label组件的内容
    re.config(text=sel)


from tkinter import *
win = Tk()
win.title("调查问卷")
# 复选框旁边显示的文字
str1 = ["旅游", "追剧上网", "和亲友聚餐", "户外健身"]
text = Label(win, text="适当的放松 友谊身心健康，请在下方选出自己最喜欢的放松方式", font="14").grid(row=0,column=0,columnspan=6)
check=[]
for i in range(len(str1)):
    v = IntVar()
    checkbox=Checkbutton(win, text=str1[i],
                variable=v,    #绑定变量
                font="12",     #设置字号
                selectcolor="#00ffff",padx=5)  #复选框的背景颜色
    # 将各复选框的varible存储在一个列表中，便于获取其状态
    checkbox.grid(row=1,column=i)
    check.append(v)

button = Button(win, text="提交", command=result1, font="14", bg="#EFB4DE").grid(row=3,column=0,pady=6,columnspan=6)
re = Label(win, font="12",height="5",width="50",bg="#cfcfcf")
re.grid(row=4,columnspan=5)
win.mainloop()