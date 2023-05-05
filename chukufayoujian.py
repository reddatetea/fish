import excelsaveas
import yagmail
import easygui
import os

msg = '请点选要需要另存为的excel文件'
print(msg)
fname = easygui.fileopenbox(msg,title='excel文件')
path,filename = os.path.split(fname)
os.chdir(path)
newfname = excelsaveas.excelSaveas(fname)

# 发件人邮箱
fjrmail = 'rightcwb@sina.com'

# 发件人邮箱密码
fjrkey = 'LTjtcwb8008'

# 收件人邮箱
shoujianren = '2937191671@qq.com'                #发程卉qq邮箱
#shoujianren = '1142760803@qq.com'

# 邮件抬头
mailtt = '原材料出库'

yag = yagmail.SMTP(user=fjrmail, password=fjrkey, host='smtp.sina.com', encoding="utf-8")

yag.send(to=shoujianren, subject=mailtt, contents=newfname)


