# 命令行将剪贴板上内容发送到印象笔记
import yagmail
import pyperclip
import sys
import ssl


def faYinxiang(sendmesage):
    yag = yagmail.SMTP(user='reddatetea@sina.com', password='f651372e1972f799', host='smtp.sina.com')
    yag.send(to=['reddatetea.1390401@m.yinxiang.com'], subject='Python send to yinxiang', contents=sendmesage)

def getMessage():
    if len(sys.argv) > 1:
        sendmesage = ''.join(sys.argv[1:])
    else:
        sendmesage = pyperclip.paste()

    return sendmesage

def main():
    sendmesage = getMessage()
    faYinxiang(sendmesage)

if __name__ == '__main__':
    main()






