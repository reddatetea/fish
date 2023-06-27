import openpyxl
wb=openpyxl.Workbook()
sheet=wb.active
sheet.title='工资表'
wb.save('工资表.xlsx')
wb.close()
