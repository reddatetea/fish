import re
yuan = r'FDS3260-36P'
regax = r'(\w+)(?:-\w*)'
pattern = re.compile(regax)
mat = pattern.search(yuan)
print(mat)
print(mat.group(1))


