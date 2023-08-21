import re
string = 'some\n sample\n\r text\n'
Regex = '\w+\Z'
a = re.findall(Regex,string)
print(a)

plainText = 'line1\n\line2\n\line3'
print(plainText)

print(re.sub(r'(?m)$','</p>',re.sub(r'(?m)^','<p>',plainText)))

print(re.sub(r'(?m)^','<p>',plainText))