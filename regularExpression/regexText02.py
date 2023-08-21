import re

string =r'埃文斯-格宾斯多丽丝(威尔士)琼-英格拉姆(英国)'
regax =r'(.*\))(.*\)$)'
pattern = re.compile(regax)
mat = re.search(pattern,string)
print(mat)
print(mat.group(1))