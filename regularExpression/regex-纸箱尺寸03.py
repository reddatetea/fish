import re
yuan = r'FL3260/FJC3260/FKN3260/FDS3260-36P'

if len(yuan.split())== 1:
    s = yuan.split('/')
else :
    s = yuan.split()

print(s)
len = len(s)

news=[]

for i in s:
    pattern = re.compile(r'(\w+)(?:-\w*)')
    mat = pattern.search(i)
    if mat == None :
        news.append(i)
    else :
        j = mat.group(1)
        news.append(j)

print(news)


