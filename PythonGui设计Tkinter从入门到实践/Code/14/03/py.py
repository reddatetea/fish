#  _*_ coding:utf-8 _*_
# 开发团队：明日科技
# 开发人员：Administrator
# 文件名称：demo3.py
# 开发工具：PyCharm

import sqlite3

# 连接到SQLite数据库,数据库文件是mrsoft.db
conn = sqlite3.connect('mrsoft.db')
# 创建一个Cursor
cursor = conn.cursor()
# 执行查询语句
cursor.execute('select * from user')
# 获取查询结果
result1 = cursor.fetchone()
print(result1)
# 关闭游标
cursor.close()
# 关闭Connection
conn.close()
