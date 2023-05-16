import os
import easygui
from PIL import Image
from PIL import ImageColor
from PIL import ImageFont
from PIL import ImageDraw
from PIL import ImageFilter
from PIL import ImageEnhance

def picDaoxiao(newPath,picture,newwidth=1440, newheight=1080):
    #print('正在进行图片大小处理，请稍等')
    ArwenIm = Image.open(picture)  # 打开文件，生成图片对象
    width, height = ArwenIm.size  # 获得图片的宽和高
    newsize = (int(newwidth),int(newheight))
    sveltIm = ArwenIm.resize(newsize)  #元组输入
    qian, hou = os.path.splitext(picture)
    newname = '%s_%s&%s%s'%(qian, newwidth, newheight, hou)
    newname = os.path.join(newPath,newname)
    sveltIm.save(newname)
    os.startfile(newname)

in_picture = easygui.enterbox(msg = '请输入图片文件的完整路径',title = '图片')
in_picture = in_picture[1:-1]
path,picture = os.path.split(in_picture)
os.chdir(path)
newPath = r'F:\a00nutstore\companyWallpaper'
new_picture = picDaoxiao(newPath,picture)