import sys
import os
import openpyxl


def res_path(relative_path):
    """获取资源绝对路径"""
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


path = r'D:\python38\PyInstaller-3.6\PyInstaller\belly'
os.chdir(path)
fname = res_path(r'F:\a00nutstore\fishc\材料入库单.xlsx')
print(fname)
wb = openpyxl.load_workbook(fname)
ws = wb.active
print(ws.title)
wb.close()
