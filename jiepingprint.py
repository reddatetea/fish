'''
从粘贴板将内容导入，快速设置，并直接打印
'''
import os
from PIL import Image, ImageGrab



if isinstance(Image.Image):
    im = ImageGrab.grabclipboard()
    print("Image: size : %s, mode: %s" % (im.size, im.mode))
    fname = "grabclipboard.jpg"
    im.save(fname)

# import win32print
# import win32ui
# from PIL import Image, ImageWin
#
# # printer_name是默认打印机的名字
# printer_name = win32print.GetDefaultPrinter()
# # 调用打印机打印两张图片
# for i in range(2):
#     hDC = win32ui.CreateDC()
#     hDC.CreatePrinterDC(printer_name)
#
#     # 打开图片
#     bmp = Image.open("D:/temp/girl3.jpg")
#
#     scale = 1
#     w, h = bmp.size
#     hDC.StartDoc("D:/temp/girl3.jpg")
#     hDC.StartPage()
#
#     dib = ImageWin.Dib(bmp)
#
#     # (10,10,1024,768)前面的两个数字是坐标，后面两个数字是打印纸张的大小
#     dib.draw(hDC.GetHandleOutput(), (10, 10, 1024, 768))
#
#     hDC.EndPage()
#     hDC.EndDoc()
# hDC.DeleteDC()
#
#
# elif im:
#     for filename in im:
#         try:
#             print("filename: %s" % filename)
#             im = Image.open(filename)
#         except IOError:
#             pass #ignore this file
#         else:
#             print("ImageList: size : %s, mode: %s" % (im.size, im.mode))
# else:
#     print ("clipboard is empty.")