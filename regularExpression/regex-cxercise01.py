import re

#正则表达式imput_re
imput_re1 = r'^[\u4e00-\u9fa5]{2,3}'

#编绎正则表达式 re.compile(compile模式)
pattern1 = re.compile(imput_re1)

#字符串imput_str
imput_str = '周宗华422432197406042513荊门市京山县三阳镇回归苑电话18696114328'
#用编绎后的正则表达式进行匹配
res1 = re.search(pattern1,imput_str)
print(res1)

imput_re2 = r'(\d{6})(\d{4})(\d{2})(\d{2})(\d{3})([0-9]|X)'
pattern2 = re.compile(imput_re2)
res2 = re.search(pattern2,imput_str)
print(res2)

imput_re3 = r'[\u4e00-\u9fa5]{4,30}'
pattern3 = re.compile(imput_re3)
res3 = re.search(pattern3,imput_str)
print(res3)

imput_re4 = r'1[0-9]{10}$'
pattern4 = re.compile(imput_re4)
res4 = re.search(pattern4,imput_str)
print(res4)





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






