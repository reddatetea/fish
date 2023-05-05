'''
将粘贴板上的内容同时发送至kindle和印象笔记
'''
import os
import smtplib
import base64
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import datetime
import pyperclip
import sys
import yagmail


def getMessage():
    if len(sys.argv) > 1:
        msg = ''.join(sys.argv[1:])
    else:
        msg = pyperclip.paste()
    return msg

def faYinxiang(sendmesage):
    yag = yagmail.SMTP(user='reddatetea@sina.com', password='f651372e1972f799', host='smtp.sina.com')
    yag.send(to=['reddatetea.1390401@m.yinxiang.com'], subject='Python发送印象笔记', contents=sendmesage)


def toTXT(dqrq,message,searchfile_path):
    file_name =  'kindle_abstracts_%s.txt' % dqrq
    fname = searchfile_path + os.sep + 'kindle_abstracts_%s.txt' % dqrq
    with open(fname,'w',encoding='UTF-8') as f:
        f.write(message)
    return fname


class SendEmail(object):
    def __init__(self, username, passwd, recv, title, content,
                 file=None, ssl=False,
                 email_host='smtp.qq.com', port=25, ssl_port=465):
        self.username =username  # 用户名
        self.passwd = passwd# 授权码，邮箱第三方登录授权码
        self.recv =recv # 收件人，多个要传list ['a@qq.com','b@qq.com]
        self.title = title  # 邮件标题
        self.content = content  # 邮件正文
        self.file = file  # 附件路径，如果不在当前目录下，要写绝对路径
        self.email_host = email_host  # smtp服务器地址，163的为smtp.163.com
        self.port = port  # 普通端口
        self.ssl = ssl  # 是否安全链接
        self.ssl_port = ssl_port  # 安全链接端口

    def send_email(self):
        msg = MIMEMultipart()
        # 发送内容的对象
        if self.file:  # 处理附件的
            file_name = os.path.split(self.file)[-1]  # 只取文件名，不取路径
            try:
                f = open(self.file, 'rb').read()
            except Exception as e:
                raise Exception('附件打不开！！！！%s' % e)
            else:
                att = MIMEText(f, "base64", "utf-8")
                att["Content-Type"] = 'application/octet-stream'
                # base64.b64encode(file_name.encode()).decode()
                new_file_name = '=?utf-8?b?' + base64.b64encode(file_name.encode()).decode() + '?='
                # 这里是处理文件名为中文名的，必须这么写
                att["Content-Disposition"] = 'attachment; filename="%s"' % (new_file_name)
                msg.attach(att)
        msg.attach(MIMEText(self.content))  # 邮件正文的内容
        msg['Subject'] = self.title  # 邮件主题
        msg['From'] = self.username  # 发送者账号
        msg['To'] = ','.join(self.recv)  # 接收者账号列表
        if self.ssl:
            self.smtp = smtplib.SMTP_SSL(self.email_host, port=self.ssl_port)
        else:
            self.smtp = smtplib.SMTP(self.email_host, port=self.port)
        # 发送邮件服务器的对象
        self.smtp.login(self.username, self.passwd)
        try:
            self.smtp.sendmail(self.username, self.recv, msg.as_string())
            pass
        except Exception as e:
            print('出错了。。', e)
        else:
            print('发送成功！')
        self.smtp.quit()


if __name__ == '__main__':
    searchfile_path = r'd:\searchfile'
    if not os.path.exists(searchfile_path):
        os.makedirs(searchfile_path)
    dqrq = datetime.datetime.now().strftime('%Y%m%d')+'_'+ datetime.datetime.now().strftime('%H%M%S')
    sendmesage = getMessage()
    print(sendmesage)
    fname = toTXT(dqrq,sendmesage,searchfile_path)
    m = SendEmail(
        username='1142760803@qq.com',
        passwd='rhkxdzhbutzjihij',
        recv=['Reddatetea01@kindle.cn'],
        title='Convert',
        content='python发送kindle文摘',
        file=fname,
        ssl=True,
    )
    m.send_email()
    faYinxiang(sendmesage)    #发印象
