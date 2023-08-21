import openpyxl
wb=openpyxl.load_workbook('工资表.xlsx')
sheet=wb.active
print(sheet.title)
