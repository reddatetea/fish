import re
yuan = r'330*235*395厚纸9.4S-9.6S'
regax = r'(\d{3})\*(\d{3})\*(\d{3})'
pattern = re.compile(regax)
mat = pattern.search(yuan)
print(mat)