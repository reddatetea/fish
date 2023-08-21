# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 22:52:50 2022

@author: 小码哥
"""
# 导入 python-docx 库
from docx import Document

# 创建空白的 Word 文档
myDoc = Document()

# 保存文档
myDoc.save('generated_docx/11.4.1-创建空白文档.docx')

print('创建成功！')