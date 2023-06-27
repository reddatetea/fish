import openpyxl
wb=openpyxl.load_workbook('工资表.xlsx')
sheet=wb['工资表']
from openpyxl.styles import fonts,colors,alignment

myfont=openpyxl.styles.Font(name='黑体',size=25,italic=True,color=colors.BLUE)
sheet['B4'].font=myfont
sheet['B4'].alignment=openpyxl.styles.Alignment(horizontal='center',vertical='center')
sheet.row_dimensions[4].height=50
sheet.column_dimensions['B'].width=50
wb.save('工资表.xlsx')
wb.close()
