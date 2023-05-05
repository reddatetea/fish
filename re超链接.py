import re
string = r'<a href="www.sian.com">'
#regax = r'<a(?=\s)[^>]*(?<=\s)href\s*=\s*[\"']?([^\"'\s]+)[\"']?[^>]*>([\s\S]+?)</a>'
regax = r'''<a(?=\s)[^>]*(?<=\s)href\s*=\s*[\"']?([^\"'\s]+)[\"']?[^>]*>([\s\S]+?)</a>'''
pattern = re.compile(regax)
mat = pattern.search(string)
print(mat)