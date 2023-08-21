# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 00:24:33 2022

@author: 小码哥
"""
# 导入 python-docx 库
from docx import Document

# 创建空白的 Word 文档
myDoc = Document()

# 添加标题:
myDoc.add_heading('公众号“七天小码哥”粉丝分析')
# 保存文档
myDoc.save('generated_docx/11.4.2-添加标题.docx')

print('创建成功！')