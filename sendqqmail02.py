#!/usr/bin/python
# -*- coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 第三方 SMTP 服务
mail_host = "smtp.qq.com"  # 邮箱服务器
mail_user = "1142760803"  # 用户名
mail_pass = "umccurpjhrnpbacj"  # 口令---》需要修改为授权码
sender = '1142760803@qq.com'
receivers = ['1142760803@qq.com']

# 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
message = MIMEText('Python 邮件测试', 'plain', 'utf-8')
message['From'] = Header("Python 邮件测试", 'utf-8')  # 发送者
message['To'] = Header("Python 邮件测试", 'utf-8')  # 接收者

subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject, 'utf-8')

smtpObj = smtplib.SMTP()
smtpObj.connect(mail_host, 587)  # 端口号根据各个邮箱服务器不同进行设置
smtpObj.login(mail_user, mail_pass)
smtpObj.sendmail(sender, receivers, message.as_string())
print("邮件发送成功")