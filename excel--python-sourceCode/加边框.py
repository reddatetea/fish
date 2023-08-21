import openpyxl
wb=openpyxl.load_workbook('工资表.xlsx')
sheet=wb['工资表']
from openpyxl.styles import fonts,Color,Alignment,Border,Side
border=openpyxl.styles.Border(left=Side(border_style='mediumDashed',color='0000FF'),
                              right=Side(border_style='mediumDashed',color='0000FF'),
                              top=Side(border_style='mediumDashed',color='0000FF'),
                              bottom=Side(border_style='mediumDashed',color='0000FF'),
                              )
sheet['B5'].border=border
wb.save('工资表.xlsx')
wb.close()
