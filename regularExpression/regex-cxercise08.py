'''
用正则将txt文件中跨越多行的括号连同里面的内容进行删除，并另存为另外一个文件

'''

# coding = 'utf-8'
import re 

file = open('NanZheng03.txt',encoding = 'utf-8')
f = file.read() 
print(f)

newfile =open('NanZheng03new.txt','w',encoding = 'utf-8')

#正则表达式imput_re
regex = r'\((.*\s\n)*.*\)\n'

#编绎正则表达式 re.compile(compile模式)
pattern = re.compile(regex)

#字符串imput_str



#sub替换
newline = re.sub(pattern,'',f)

newfile.write(newline)

file.close()

newfile.close()










