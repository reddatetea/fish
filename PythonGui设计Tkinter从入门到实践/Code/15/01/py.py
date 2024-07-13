#  _*_ coding:utf-8 _*_
# 开发团队：明日科技
# 开发人员：Administrator
# 文件名称：py.py
# 开发工具：PyCharm
# python创建一个文件

file=open("test.txt","w",encoding='utf-8')     #创建并打开文件
print("文本文件已创建完成，请添加内容：\n")    #显示提示语句
a=input()                                      #输入内容
file.write(a)                                  #将输入内容写入文本文件
file.close()                                   #关闭文件
print("\n添加文本内容成功，请手动查看")        #写入内容成功，显示提示信息

