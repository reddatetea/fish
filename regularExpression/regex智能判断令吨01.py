import re

spring = '230g白卡787*1092  100吨'

a = spring.split()
print(a)

cailiaoname = a[0]
temp = a[1]

print(cailiaoname,temp)
rep = r'(\d+)(元/令|元/吨|令|吨)'
pattern = re.compile(rep)
mat = pattern.search(temp)

if mat !=None :

    print(mat)
    print(mat.group(2))

    if mat.group(2)== '元/令':
        lingjia0 = mat.group(1)
        print(lingjia0)

    elif mat.group(2) == '元/吨':
        dunjia0 = mat.group(1)
        print(dunjia0)

    elif mat.group(2) == '令':
        lingshu0 = mat.group(1)
        print(lingshu0)

    elif mat.group(2) == '吨':
        dunshu0 = mat.group(1)
        print(dunshu0)

    else :
        print('输入有误，请重新输入')

else :
    print('输入有误，请重新输入')



