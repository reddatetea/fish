import os
from PIL import Image

path  = r'F:\a00nutstore\z中国书法\图片库\网友竞临灵飞经'
for j in os.listdir(path):
    qian,hou =os.path.splitext(j)
    newname = qian + '.'+'jpg'
    newfname = os.path.join(path,newname)
    picIm = Image.open(os.path.join(path,j))  # 打开文件，生成图片对象
    picIm.save(newfname)
