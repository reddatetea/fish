# coding = 'utf-8'
import re 

#正则表达式imput_re
regex = r'(-\w*)(?=\.mp4)'

#编绎正则表达式 re.compile(compile模式)
pattern = re.compile(regex)

#字符串imput_str
imput_str = '舞曲串烧 Chinese DJ - 中文舞曲中国最好的歌曲2019 - DJ 排行榜 中国 跟我你不配 全中文DJ舞曲 高清 新2019夜店混音-年最劲爆的DJ歌曲 - Chinese DJ 2019-PDOn91QSd10.mp4'
#用编绎后的正则表达式进行匹配
#res = re.search(pattern,imput_str)
#print(res)

#sub替换
newname = re.sub(pattern,'',imput_str)
print(newname)

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






