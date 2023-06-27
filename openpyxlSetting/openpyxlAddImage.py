'''
在excel单元格中添加图片
'''
from openpyxl import Workbook
from openpyxl.drawing.image import Image

wb = Workbook()
ws = wb.active
ws['A1'] = 'learning for me happy'

img = Image('image.jpg')

ws.add_image(img, 'A1')
wb.save('image.xlsx')