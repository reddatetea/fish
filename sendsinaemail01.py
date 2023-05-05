import smtplib
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import os

# 配置邮箱服务器信息
mail_host = "smtp.sina.com"   # 设置服务器
mail_user = "reddatetea@sina.com"     # 用户名
mail_pass = "ed73a2127ff4caef"  # 口令

# 配置发件人、收件人信息
sender = 'reddatetea@sina.com' # 发件人邮箱
receivers = ['reddatetea@sina.com']  # 接收邮件，可设置为多个邮箱


def message_config():
    """
    配置邮件信息
    :return: 消息对象
    """
    # 第三方 SMTP 服务
    content = MIMEText('Python课程数据,注意查收')
    message = MIMEMultipart() # 多个MIME对象
    message.attach(content)  # 添加内容
    #message['From'] = Header("Moersuo", 'utf-8') # 发件人
    message['From'] = Header('reddatetea@sina.com')  # 发件人
    #message['To']   = Header("斯文张", 'utf-8')  # 收件人
    message['To'] = Header('reddatetea@sina.com')  # 收件人
    #message['Subject'] = Header('Python课程数据', 'utf-8') # 主题message
    message['Subject'] = Header('Python课程数据')  # 主题
    # 添加Excel类型附件
    file_name = 'Python课程数据2019-12-31.xlsx' # 文件名
    path = r'D:\a00nutstore\fishc'
    file_path = os.path.join(path,file_name)        # 文件路径
    # xlsx = MIMEApplication(open(file_path, 'rb').read())  # 打开Excel,读取Excel文件
    # xlsx["Content-Type"] = 'application/octet-stream'     # 设置内容类型
    # xlsx.add_header('Content-Disposition', 'attachment', filename=file_name) # 添加到header信息
    # 邮件附件
    part = MIMEApplication(open(file_path, 'rb').read())
    # filename=邮件附件中显示的文件的名称，可自定义
    part.add_header('Content-Disposition', 'attachment', filename=file_name)
    message.attach(part)
    # message.attach(xlsx)
    return

def send_mail(message):
    """
    发送邮件
    :param message: 消息对象
    :return: None
    """
    try:
        smtpObj = smtplib.SMTP_SSL(mail_host) # 使用SSL连接邮箱服务器
        smtpObj.login(mail_user, mail_pass)   # 登录服务器
        #smtpObj.sendmail(sender, receivers, message.as_string()) # 发送邮件
        smtpObj.sendmail(sender, receivers, message.as_string())  # 发送邮件
        print("邮件发送成功")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    print("开始执行")
    message = message_config() # 调用配置方法
    send_mail(message)         # 发送邮件
    print("执行结束")
