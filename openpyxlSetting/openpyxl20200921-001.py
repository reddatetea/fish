import openpyxl
import os


path = r'F:\a00nutstore\006\zw\2020'
filename = r'abc.xlsx'
fname = os.path.join(path,filename)

wb = openpyxl.load_workbook(fname)
ws = wb['sheet1']
print(ws)
print(ws.dimensions)