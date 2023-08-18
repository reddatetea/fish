'''
用自己的qq邮箱1142760803发送公司每日原材料、产成品、零配件日报表
将桌面上文件名中含有‘材料’和‘日报’的文件发邮件指定收件人
将桌面上文件名中含有‘产成品’和‘日报’的文件发邮件至指定收件人
将桌面上文件名中含有‘零配件’和‘日报’的文件发邮件至指定收件人

'''
import os
import re
import time
import easygui
import smtplib
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication


file_path = r'D:\ribaobiao'
if not os.path.exists(file_path):
    os.makedirs(file_path)
os.chdir(file_path)
filenames = os.listdir(file_path)
# 配置邮箱服务器信息
mail_host = "smtp.qq.com"   # 设置服务器
mail_user = "1142760803"     # 用户名
ail_pass = ""  # 口令
mail_pass = "rhkxdzhbutzjihij"  # 口令
# 配置发件人、收件人信息
sender = '1142760803@qq.com' # 发件人邮箱
# yesterday = (datetime.date.today() + datetime.timedelta(days=-1)).strftime('%Y%m%d')
#yesterday = (datetime.date.today() + datetime.timedelta(days=-1)).strftime('%m%d')
# 原材料ycl
ycl = r'.*材料.*日报.*\.[Xx][Ll][Ss][Xx]?'
# 产成品
ccp = r'.*成品.*日报.*\.[Xx][Ll][Ss][Xx]?'
# 零配件
lpj = r'.*配件.*日报.*\.[Xx][Ll][Ss][Xx]?'
# yclyx原材料邮箱
yclyx = ['1175599535@qq.com', '471528579@qq.com',  '616012311@qq.com', '173937271@qq.com','842722949@qq.com']
# 密送邮箱列表
msyx = ['940433711@qq.com']
# ccpyx产成品邮箱列表
ccpyx = ['616012311@qq.com', '173937271@qq.com', '523772567@qq.com', '305124514@qq.com', '396354827@qq.com',
         '312963233@qq.com','310132404@qq.com']
# wpbyx产成品邮箱列表
wmbyx = ['1784506832@qq.com']    #黄茜

# 零配件邮箱列表
lpjyx = ['1175599535@qq.com', '471528579@qq.com', '441833636@qq.com', '616012311@qq.com', '173937271@qq.com', ]
# 自己邮箱列表
zjyx = ['rightcwb@sina.com']
# 原材料邮箱列表+密送列表+自己邮箱列表    #20220214取消发自己邮箱
yclyxs = yclyx + msyx + wmbyx
# 产成品邮箱列表+密送列表+自己邮箱列表    #20220622增加外贸部邮箱
ccpyxs = ccpyx + wmbyx + msyx
# 零配件邮箱列表+自己邮箱列表     #20220214取消发自己邮箱
lpjyxs = lpjyx

def message_config(file_path,file_name,yxtt,shoujianren):
    """
    配置邮件信息
    :return: 消息对象
    """
    # 第三方 SMTP 服务
    content = MIMEText('日报表excel文件,请注意查收')
    message = MIMEMultipart() # 多个MIME对象
    message.attach(content)  # 添加内容
    message['From'] = Header(sender) # 发件人
    #message['To']   = Header(shoujianren, 'utf-8')  # 收件人
    message['To'] = ','.join(shoujianren)                                    #如此可以同时发多个收件人
    message['Subject'] = Header(yxtt, 'utf-8') # 主题
    # 添加Excel类型附件
    fname = os.path.join(file_path,file_name)        # 文件路径
    xlsx = MIMEApplication(open(fname, 'rb').read())  # 打开Excel,读取Excel文件
    xlsx["Content-Type"] = 'application/octet-stream'     # 设置内容类型
    xlsx.add_header('Content-Disposition', 'attachment', filename=file_name) # 添加到header信息
    message.attach(xlsx)
    return message

def send_mail(message,shoujianren):
    """
    发送邮件
    :param message: 消息对象
    :return: None
    """
    try:
        smtpObj = smtplib.SMTP_SSL(mail_host) # 使用SSL连接邮箱服务器
        smtpObj.login(mail_user, mail_pass)   # 登录服务器
        smtpObj.sendmail(sender, shoujianren, message.as_string()) # 发送邮件
        print("邮件发送成功")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    print("开始执行")
    for filename in filenames:
        searchYcl = re.search(ycl, filename)
        searchCcp = re.search(ccp, filename)
        searchLpj = re.search(lpj, filename)
        # 发原材料邮件
        if searchYcl:
            yxtt = os.path.splitext(filename)[0]
            shoujianrens = yclyxs
            for shoujianren in shoujianrens:
             message = message_config(file_path, filename, yxtt, shoujianrens)
            send_mail(message, shoujianrens)
            time.sleep(2)


         # 发产成品邮件
        if searchCcp:
            yxtt = os.path.splitext(filename)[0]
            shoujianrens = ccpyxs            #产成品邮箱+自己邮箱+外贸部邮箱
            #for shoujianren in shoujianrens:
            message = message_config(file_path, filename, yxtt, shoujianrens)
            send_mail(message, shoujianrens)
            time.sleep(5)

        # 发零配件邮件
        if searchLpj:
            yxtt = os.path.splitext(filename)[0]
            shoujianrens = lpjyxs
            #for shoujianren in shoujianrens:
            message = message_config(file_path, filename, yxtt, shoujianrens)
            send_mail(message, shoujianrens)
            time.sleep(5)
    easygui.msgbox('邮件发送完毕')






