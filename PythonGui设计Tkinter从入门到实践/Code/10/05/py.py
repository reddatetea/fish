#  _*_ coding:utf-8 _*_
# 开发团队：明日科技
# 开发人员：Administrator
# 文件名称：demo1.py
# 开发工具：PyCharm
# Menu菜单的综合应用   制作游戏菜单

num = 0  # 当前游戏多少关
# 通过数组存储成语和成语的含义
idiom = ["别出心裁", "白云苍狗", "暴虎冯河", "鞭长莫及", "并行不悖", "安土重迁", "不耻下问", "不胫而走", "安步当车", "爱莫能助", "白驹过隙"]
idiom_means = ["独出巧思，不同流俗", "比喻世事变幻无常", "比喻有勇无谋，鲁莽冒险", "本意为马鞭虽长，但打不到马肚子上，，比喻虽有力，力量也打不到",
               "彼此同时进行，不相妨碍", "留恋故土，不肯轻易迁移", "比喻谦虚好学，不介意向学识或地位不及自己的人请教", "消息传的很快", "从容的步行，就当乘车一般",
               "心里愿意帮助，但是力量做不到", "形容时间过得很快，像白马在细小的缝隙前一闪而过", ]


# 判断输入成语是否正确
def panduan():
    global num
    a = entry.get()
    if a == idiom[num]:
        num += 1
    if (num >= len(idiom)):
        boo = askyesno("成功过关", "恭喜！已过完所有关卡，是否重新过关？")
        if boo == True:
            num = 0
            panduan()
        else:
            win.quit()
    entry.delete(0, END)
    means.config(text=idiom_means[num])
    level.config(text="第 " + str(num + 1) + " 关")

#手动切换至下一关
def next1(event):
    global num
    num += 1
    panduan()

# 重新开始，关卡重置为0
def restart(event):
    global num
    num = 0
    panduan()
# 显示游戏规则
def show1():
    showinfo("游戏规则","根据成语的含义猜成语，正确则自动跳转至下一关")
# 提示当前成语的第一个字
def tip():
    str=idiom[num][0]
    entry.delete(0,END)
    entry.insert(0,str)

from tkinter import *
from tkinter.messagebox import *
win = Tk()
win.geometry("250x200")
win.title("成语猜猜猜")
# 工具栏部分
menu1 = Menu(win)  # 创建顶级菜单
menu2_1 = Menu(menu1)  # 创建第二级菜单
menu1.add_cascade(label="游戏", menu=menu2_1)        # 将第二级菜单添加到顶级菜单并设置显示的内容
menu2_1.add_command(label="下一关", command=lambda:next1(""), accelerator="Ctrl+N")
menu2_1.add_command(label="重新开始", command=lambda :restart(""), accelerator="Ctrl+R")
menu2_1.add_separator()  # 添加分割线
menu2_1.add_command(label="退出", command=win.quit)  # 退出游戏，关闭窗口
menu2_2 = Menu(menu1)                          # 创建第二个二级菜单
menu1.add_cascade(label="帮助", menu=menu2_2)  # 将第二个二级级菜单添加到顶级菜单并设置显示的内容
menu2_2.add_command(label="游戏规则",command=show1)  # 添加二级菜单的子菜单
menu2_2.add_command(label="提示",command=tip)  # 添加二级菜单的子菜单
win.config(menu=menu1)

# 窗口内容
level = Label(win, font=14, text="第 1 关")              # 当前第几关
level.grid(row=0, column=0, columnspan=4, sticky=E)      # 显示成语的含义
means = Label(win, text=idiom_means[0], font=14, width=30, bg="#D8F3F0", height=3, wraplength="200")
means.grid(row=1, column=0, pady=10, columnspan=4)
entry = Entry(win, font=14)                              # 输入成语
entry.grid(row=2, column=1, sticky=E)
btn = Button(win, text="确定", command=panduan).grid(row=2, column=2)
win.bind_all("<Control-n>", next1)         # 绑定键盘事件
win.bind_all("<Control-r>", restart)       # 绑定键盘事件
win.mainloop()
