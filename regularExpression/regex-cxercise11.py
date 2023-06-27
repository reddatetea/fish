import re
r = r'(?m)^\d.*'
str = '1 line\nNot digit\n2 line'

for line in re.findall(r,str):
    print(line)

#编绎时不要忘记re
pattern = re.compile(r,re.M|re.U)

for line in pattern.findall(str):
    print(line)




