import re

#正则表达式imput_re
imput_re = r'http://img.pingpangwang.com/data/attachment/forum/.*.gif'

#编绎正则表达式 re.compile(compile模式)
pattern = re.compile(imput_re)
gz_dic = {}
#字符串imput_str
imput_str = 'http://img.pingpangwang.com/data/attachment/forum/201502/13/125314zg9p8ppz9f4kq6rf.gif'
#用编绎后的正则表达式进行匹配
res = re.search(pattern,imput_str)
print(res)







#sub替换
#res1 = re.sub(pattern,'',imput_str)
#print(res1)

#打印匹配结果
#print(res)

#转换匹配后的类型  search  re.march  用 group()转换为字符串
#result = res.group()

#打印匹配结果转换后的结果
#print(result)

'''
转换匹配后的类型
search  re.march  用 group()转换为字符串
findall 列表      用[]取值，转换为字符串
运行结果：
<re.Match object; span=(2, 28), match="'白日依山尽，黄河入海流，欲穷千里目，更上一层楼！'">
'白日依山尽，黄河入海流，欲穷千里目，更上一层楼！'

'''






