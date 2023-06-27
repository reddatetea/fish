# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 00:03:55 2022

@author: 小码哥
"""
# 导入 python-docx 库
from docx import Document

# 创建空白的 Word 文档
myDoc = Document()

# 利用for循环查看所有标题等级:
for i in range(10):
    myDoc.add_heading('这是标题 level ' + 'i', i)

# 保存文档
myDoc.save('generated_docx/11.4.2-查看标题.docx')

print('创建成功！')