# _*_coding:UTF-8 _*_
# 开发团队：明日科技
# 开发人员：pc
# 开发时间：2020/3/9  9:09
# 文件名称：demo1.PY
# 开发工具：PyCharm

# Radiobutton高级使用

# 答案对应的含义
def result1():
    # re.delete("0.0",END)
    print(v.get())
    if v.get() == 0:   #选择“一定会”的答案解析
        str="答案：\n你至始至终就只有一副的面孔,你讨厌两面派，也讨厌伪装，你觉得无论何时，做真实的自己最重要，所以你很少在乎别人的想法。"
    elif v.get() == 1: #选择“很可能会”的答案解析
        str="答案：\n你有两幅面孔,你很擅长伪装，在别人面前，你总是善良懂事，而人后却不停打着自己的小算盘。"
    elif v.get() == 2: #选择“偶尔会”的答案解析
        str="答案：\n你有三幅面孔,在不同的时间段里，你会展示出不同的面孔。早上的时候，心情美美，自然体贴善良，而中午遇到问题时，就冷脸相对，而晚上时，你又会彻底放松自己。"
    else:              #选择“绝不会”的答案解析
        str="答案：\n你有四幅面孔,面对不同的人就会使用不同的面孔，例如在亲人和朋友以及爱人面前，你给她们的印象都是不同的。"
    re.config(text=str)


from tkinter import *

win = Tk()
win.title("心理测试题")
# 数组存储单选按钮显示的值
str1 = ["一定会", "很可能会", "偶尔会", "绝不会"]
Label(win, text="测试你的性格有几面", font="14").pack(anchor=W)
text = Label(win, text="当你看不惯别人的某些行为时，你会直接指出吗？", font="14").pack(anchor=W)
v = IntVar()    #该变量绑定一组单选按钮的值
for i in range(len(str1)):
    # text为单选按钮旁显示的文字,value为单选按钮的值，indicatoron设置单选按钮为矩形，selectcolor设置被选中的颜色
    radio = Radiobutton(win, text=str1[i], variable=v, value=i, font="12", indicatoron=0, selectcolor="#00ffff")
    radio.pack(side=TOP, fill=X, padx=20, pady=3)
#提交按钮
button = Button(win, text="提交", command=result1, font="14", bg="#4CC6E3")
button.pack(side=TOP, fill=X, padx=40, pady=20)
# 显示答案解析的Label组件
re = Label(win, font="14", height="10", width="40", justify="left",wraplength=320)
re.pack(side=TOP, pady=10)
win.mainloop()
