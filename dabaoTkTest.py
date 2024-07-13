import os
import shutil
import pyperclip
from tkinter import *
from tkinter.filedialog import *


def getPyused(event):
    global py_used
    global fruites_nums
    fruites_nums = 1
    py_used = []
    index1 = fruites.curselection()  # 获取选中的项的内容
    for item in index1:
        py_used.append(listitem[item])
    fruites_nums = len(index1)


def openFiles():
    global icoFile
    global pyFile
    icoFile = ''
    pyFile = ''
    icoFile = askopenfilename(title='选择文件', filetype=[('ico格式的图片文件', '.ico')])
    pyFile = askopenfilename(title='选择文件', filetype=[('ico格式的图片文件', '.py')])


win = Tk()
win.title("请选择要打包脚本中使用的库")
win.configure(bg="#F5D7C4")  # 设置窗口背景颜色
win.geometry("360x230")  # 设置窗口大小
box1 = Frame(width=100, height=10, relief="groove", borderwidth=5)
box1.grid(row=0, column=0, pady=10, padx=10)
box2 = Frame(width=100, height=10, relief="groove", borderwidth=5)
box2.grid(row=1, column=0, pady=10, padx=10)
scr1 = Scrollbar(box1)  # 添加滚动条
# 列表框的选项
listitem = (
    "bs4",
    "docx",
    "easygui",
    "matplotlib",
    "numpy",
    "openpyxl",
    "pandas",
    "pdfplumber",
    "pyperclip",
    "tkinter",
    "xlwings",
    "xpinyin",
    "yagmail",
)
# 通过yscrollcommand将列表框与滚动条绑定
fruites = Listbox(
    box1,
    height=8,
    yscrollcommand=scr1.set,
    selectmode="multiple",
    justify="center",
    width=30,
)
fruites.insert(END, *listitem)  # 添加列表框中的选项
fruites.pack(side="left", fill="x")
# fruites.grid(row =0,column = 60)
fruites.bind("<<ListboxSelect>>", getPyused)
# scr1.grid(row =0,column = 50)
scr1.pack(side="left", fill="y")
scr1.config(command=fruites.yview)
button1 = Button(box2, text="确定")
button1.grid(row=30, column=15)
win.mainloop()

paichus = list(set(listitem) - set(py_used))
paichu = " ".join(["--exclude-module=" + j for j in paichus])  # 排除的库
dabao_pyinstall = r"D:\python38\Scripts\pyinstaller.exe"
win = Tk()
win.geometry('360x100')
Button(win, text='分别选择ICO和PY文件', command=openFiles).pack()
win.mainloop()

path, file = os.path.split(pyFile)
os.chdir(path)
file_way = r'-F -w -i'
tmpdir_way = r'--runtime-tmpdir=..'
# 复制upx文件夹至要打包脚本所在文件夹
source_path = r'D:\a00nutstore\yingyongchengxu\upx-3.96-win64'
target_path = os.path.join(path, os.path.split(source_path)[-1])
if not os.path.exists(target_path):
    # 如果目标路径不存在原文件夹的话就创建
    os.makedirs(target_path)
if os.path.exists(source_path):
    # 如果目标路径存在原文件夹的话就先删除
    shutil.rmtree(target_path)
shutil.copytree(source_path, target_path)
upx_way = ''.join(['--upx-dir=', target_path])  # 不能有空格''
daobao_lst = [dabao_pyinstall, upx_way, paichu, file_way, icoFile, tmpdir_way, pyFile]
daobao_commond = ' '.join(daobao_lst)  # 有一个空格''
pyperclip.copy(daobao_commond)
win = Tk()
win.geometry('360x100')
mess = Message(win, text='程序结束\n请cmd到命令行模式\n粘贴后 运行', width=140).pack(pady=10)
win.mainloop()




