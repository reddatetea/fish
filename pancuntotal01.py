import openpyxl

wb5=load_workbook('盘存表材料更名.xlsx')
sheet5 = wb.active

jishu = 0
first_list = []
for index,row in enumerate(sheet.values):
    print(row[1])
    first_list.append(row[1])

    if row[0] == None:
        jishu = jishu +1
mrows = sheet.max_row -jishu


