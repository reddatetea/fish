from tkinter import ttk
from tkinter import *
from tkinter import messagebox as mg
from random import randint
from re import findall
from threading import Thread
import requests

"""
写了一整天，写了个没什么太大用处的 GUI ~  ^_^

不过可以方便那些新人练习爬虫的获取 IP 啦 ~ 

不用去百度找什么免费代理了~ 这个软件就满足你~

今天测试的时候爬的这个代理网站，把我封了俩IP

一个自己的IP，一个隔壁的，我做测试时候都是用手机开 WIFI 拿来测试了

所以说，看着我这么幸苦的份上~评个分吧~~~             ^_^

                                                 分享于：鱼C论坛
                                                  By：Twilight6
"""

# 访问ip网站
def access_url(url, headers):
    response = requests.get(url, headers=headers)  # 访问网页
    html = response.text
    ip_list = findall(r'(\d+\.\d+\.\d+\.\d+.\d+)', html)
    _https = findall(r'<td>(HTTPS{0,1},*)', html)
    return list(zip(_https, ip_list))


# 将http\https协议的IP分组
def get_agreement(temp, choose):
    http = []
    https = []
    for i in range(len(temp)):
        if 'HTTP' in temp[i][0]:
            http.append(temp[i])
            if ',' in temp[i][0]:
                https.append(temp[i])
        else:
            https.append(temp[i])
    if choose == 'http':
        return http
    else:
        return https


# 检测IP是否可用
def detection_ip():
    IP = enter.get()

    def func():
        top = Toplevel()
        top.attributes("-alpha", 0.95)
        top.attributes("-toolwindow", 1)
        top.wm_attributes("-topmost", 1)
        top.title("进度条")
        Label(top, text="正在尝试使用此IP进行访问网站,请不要关闭窗口......", fg="black").pack(pady=5)
        prog = ttk.Progressbar(top, mode='indeterminate', length=300)
        prog.pack(pady=10, padx=35)
        prog.start()
        try:
            proxies = {f'{choose}': f'{choose}://{IP}'}
            url = f'{choose}://httpbin.org/get'
            requests.get(url, headers=headers, proxies=proxies)
            text.config(state=NORMAL)
            text.insert(END, '|-- IP :  {:^20} 成功访问\n'.format(IP))
            text.config(state=DISABLED)
            prog.stop()
            top.destroy()
        except:
            text.config(state=NORMAL)
            top.destroy()
            text.insert(END, '|-- IP :  {:^20} 访问失败\n'.format(IP))
            text.config(state=DISABLED)

    t = Thread(target=func)
    t.setDaemon(True)
    t.start()


def refresh():
    ip_list.delete(0, END)
    url = f'http://www.xiladaili.com/gaoni/{age}/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
    }
    temp = access_url(url, headers=headers)
    ip = get_agreement(temp, choose)
    for i in range(len(ip)):
        ip_list.insert(END, ip[i][1])


# 上一页
def up_age():
    global age
    if age >= 2:
        ip_list.delete(0, END)
        age -= 1
        refresh()
    else:
        mg.showinfo(title='错误', message='已经到了第一页')


# 下一页
def next_age():
    ip_list.delete(0, END)
    global age
    age += 1
    refresh()


# 刷新
def refresh_age():
    global age
    refresh()


def judge(string):
    ls = string.split('.')
    if ls[-1].count(':') == 1 and len(ls) == 4:
        ls[-1], temp = ls[-1].split(':')
        ls = ls + temp
        for i in ls[:-1]:
            if i.isdigit() and 0 <= int(i) <= 255:
                continue
            break
        else:
            if int(ls[-1]) <= 65536:
                return True
    return False


def choose_HTTP():
    global choose
    choose = 'http'
    refresh()


def choose_HTTPS():
    global choose
    choose = 'https'
    refresh()

# 设置双击事件
def append_entry(event):
    enter.delete(0,END)
    enter.insert(END,ip_list.get(first=ip_list.curselection()))


root = Tk()
root.title('--IP获取器--'.center(80))
# 设置窗口透明度
root.attributes("-alpha", 0.9)

# 禁止窗口拉伸
root.resizable(width=False, height=False)

frame_left = Frame(root, bg='black')  # 设置左框架
frame_right = Frame(root, bg='black')  # 设置右框架

menubar = Menu(root)

editVar = IntVar()

editmenu = Menu(menubar, tearoff=False)
menubar.add_cascade(label='协议', menu=editmenu)
editmenu.add_radiobutton(label='HTTP', command=choose_HTTP, value=1)
editmenu.add_radiobutton(label='HTTPS', command=choose_HTTPS, value=2)
root.config(menu=menubar)

sb = Scrollbar(frame_left)  # 设置滚动条组件
sb.grid(row=0, column=4, sticky=N + S)

ip_list = Listbox(frame_left,  # 设置IP列表
                  yscrollcommand=sb.set,
                  height=15, bg='black', fg='white',
                  highlightcolor='black', font=('微软雅黑')
                  )
ip_list.grid(row=0, column=0, columnspan=3)
ip_list.bind('<Double-Button-1>',append_entry)
sb.config(command=ip_list.yview)  # 设置鼠标滚轮

up_b = Button(frame_left,
              text='上一页', command=up_age,
              bg='black', fg='white', font=('迷你简菱心')
              )
up_b.grid(row=1, column=0, stick=W + E)

next_b = Button(frame_left,
                text='下一页', command=next_age,
                bg='black', fg='white', font=('迷你简菱心')
                )
next_b.grid(row=1, column=2, stick=E + W, columnspan=4)

refresh_b = Button(frame_left,
                   text='刷新', command=refresh_age,
                   bg='black', fg='white', font=('迷你简菱心')
                   )
refresh_b.grid(row=1, column=1, stick=E + W)

Label(frame_right,
      text='选中IP后按Ctrl+C进行拷贝\n点击输入框Ctrl+V进行粘贴',
      font=('迷你简菱心', 15), bg='black', fg='white',
      ).grid()

v0 = StringVar()
v0.set('输入IP测试是否可用')

enter = Entry(frame_right,
              textvariable=v0,
              validate='key',
              width=30,
              validatecommand=(judge, '%P'))
enter.grid()

button_test = Button(frame_right,
                     text='测试',
                     bg='black', fg='white', font=('迷你简菱心', 15),
                     command=detection_ip)
button_test.grid()

text = Text(frame_right,
            state=DISABLED,
            height=11, width=35,
            background='black', foreground='white',
            font=('微软雅黑', 13)
            )
text.grid(stick=E + W + N + S)

frame_left.pack(side=LEFT, fill=Y)
frame_right.pack()


if __name__ == '__main__':
    age = 1
    url = f'http://www.xiladaili.com/gaoni/{age}/'
    headers_list = [
        'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1500.55 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2225.0 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.62 Safari/537.36',
        'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.16 Safari/537.36'
    ]
    headers = {
        'User-Agent': headers_list[randint(0, 3)]
    }
    choose = 'http'
    temp = access_url(url, headers=headers)
    ip = get_agreement(temp, choose)
    for i in range(len(ip)):
        ip_list.insert(END, ip[i][1])

    mainloop()