import openpyxl
wb=openpyxl.load_workbook('工资表.xlsx')
sheet=wb['工资表']
sheet['E2']=int(sheet['C2'].value)+int(sheet['D2'].value)
wb.save('工资表.xlsx')
wb.close()
