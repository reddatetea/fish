import os, yagmail, fnmatch
from pypinyin import lazy_pinyin



# 输入你的邮箱地址和授权码
yag = yagmail.SMTP(user='reddatetea@sina.com', password='hhrhl805', host='smtp.sina.com')

# 筛选“工资明细”文件夹里的所有 .docx 文件

dir_path = r'D:\123'
wordfile = '123.docx'
filename = os.path.join(dir_path,wordfile)
mail_address = 'reddatetea@sina.com'

yag.send(
    to='reddatetea@sina.com',
    subject='2020年11月工资明细',
    contents=[filename]
    )
print('已发送工资明细邮件')