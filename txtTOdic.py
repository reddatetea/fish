import re

with open('gongzhang.txt','r',encoding = 'utf-8') as file :
    gz_dic = {}
    for line in file.readlines() :
        line.strip()
        temp = line.split()
        gongzhong = ' '.join(temp)

        imput_re = r'(\w+)\s+(\w+)'
        #编绎正则表达式 re.compile(compile模式)
        pattern = re.compile(imput_re)

        #字符串imput_str
        imput_str = gongzhong
        #用编绎后的正则表达式进行匹配
        res = re.search(pattern,imput_str)
        print(res.group(1))
        print(res.group(2))
        key =res.group(1)
        value = res.group(2)
        gz_dic[key] = value
        print(gz_dic)
print(gongzhong)



