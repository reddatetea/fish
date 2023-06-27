import openpyxl
wb=openpyxl.load_workbook('工资表.xlsx')
sheet=wb['工资表']
lst1=['序号','姓名','基本工资','其他','1','张三','12000','2500','2','里斯','15000','6520','3','五七','25000','4520']
lst2=['A','B','C','D']
lst3=['1','2','3','4']
d=0
for c in lst3:
    for b in lst2:
        a=b+c
        sheet[a]=lst1[d]
        d += 1
        if d==16:
            break
        else:
            continue
wb.save('工资表.xlsx')
wb.close()

