import tkinter
import sys
import os


def res_path(relative_path):
    """获取资源绝对路径"""
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


win = tkinter.Tk()
win.iconbitmap(res_path('img/icon.ico'))  # 设置窗口图标
win.mainloop()