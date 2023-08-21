import re

regex = r'(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})'

pattern = re.compile(regex)

str = '2010-12-22'

newline = pattern.search(str)

print(newline)


print(newline.group(1))

year=newline.group('year')
month=newline.group('month')
day = newline.group('day')

#newlinesub = pattern.sub('dayday',newline)
newlinesub = pattern.sub(year+month+day,str)

print(newlinesub)

day = newline.group('day')

#反向引用
m=re.search(r'<(?P<label>[a-z]*)(.*)</(?P=label)>', '<span class="read-count">阅读数:410</span>')
print(m)
print(m.groupdict())

#上述组名的反向引用，也可以通过组序号实现同样的功能，就是在引用的地方直接使用
m=re.search(r'<(?P<label>[a-z]*)(.*)</(\1)>', '<span class="read-count">阅读数:410</span>')
print(m)

m=re.search(r'<([a-z]*)(.*)</(\1)>', '<span class="read-count">阅读数:410</span>')
print(m)








