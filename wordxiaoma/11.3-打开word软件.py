# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 21:43:38 2022

@author: 小码哥
"""
# 导入 python-docx 库
from docx import Document

# 第一步：打开word软件，创建空白的 Word 文档
myDoc = Document()

# 查看文档的属性和方法
print(dir(myDoc))