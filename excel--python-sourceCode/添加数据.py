import openpyxl
wb=openpyxl.load_workbook('工资表.xlsx')
sheet=wb.active
sheet.title='工资表'
sheet['B7']='工资'
wb.save('工资表.xlsx')
wb.close()
