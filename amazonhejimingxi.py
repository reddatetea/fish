# 通过分别复制电子书合集书名和合集里面 的内容，将合集书和里面包含的书添加到亚马逊书单的'套装书'工作表最后
import os
import re
import pyperclip
import easygui
import openpyxl

msg = '请复制电子书合集书名'
easygui.msgbox(msg)
heji = heji_string =  pyperclip.paste()

msg = '请复制合集内容'
easygui.msgbox(msg)
heji_string =  pyperclip.paste()
def pipeiBooks(heji_string):
    regax = r'(?<=《)(.*?)(?=》)'
    pattern = re.compile(regax)
    books = re.findall(pattern, heji_string)
    print(books)
    # regax = r'(?m)^《[^《]+(?=》)'
    # pattern = re.compile(regax)
    # book0 = re.findall(pattern, heji_string)
    # books = [j.replace('《', '') for j in book0]
    return books
books = pipeiBooks(heji_string)

msg = '请点选亚马逊书单excel文件'
fname = easygui.fileopenbox(msg)
wb = openpyxl.load_workbook(fname)
ws  = wb['套装书']
max_row = ws.max_row
for book in books:
    row = [heji,'','',book]
    ws.append(row)
wb.save(fname)







