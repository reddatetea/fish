#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 截图 pandas 的表格样式
from pathlib import Path
import pandas as pd
from playwright.sync_api import sync_playwright

df = pd.read_csv('https://www.gairuo.com/file/data/team.csv')

style = (df.head(10)
         .assign(avg=df.mean(axis=1, numeric_only=True))  # 增加平均值
         .assign(diff=lambda x: x.avg.diff())  # 和前位同学差值
         .style
         .bar(color='yellow', subset=['Q1'])
         .bar(subset=['avg'], width=90, vmin=60, vmax=100, color='#5cadad')
         .bar(subset=['diff'], color=['#ffe4e4', '#bbf9ce'], vmin=0, vmax=30, align='zero')
         )

html_string = '''
<html>
  <head><title>我的图表</title></head>
  <link rel="stylesheet" type="text/css" href="style.css"/>
  <body>
    {table}
  </body>
</html>
'''

html = html_string.format(table=style.to_html())  # 生成 html 内容

# 生成 html 文件
with open('data.html', 'w') as f:
    f.write(html)

# 打开文件、截图
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.set_viewport_size({"width": 720, "height": 350})
    page.wait_for_timeout(10000)
    page.goto(Path('data.html').absolute().as_uri())
    page.screenshot(path='data.jpg', type='jpeg', full_page=True, quality=100, scale='css')
    browser.close()
    print('生成图片完成!')

