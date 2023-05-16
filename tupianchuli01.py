'''
图片处理，反转，大小等,easygui运用
'''
from PIL import Image
from PIL import ImageColor
from PIL import ImageFont
from PIL import ImageDraw
from PIL import ImageFilter
from PIL import ImageEnhance

import easygui
import os

def picFanzhuan(picture):
    print('正在进行图片反转外理，请稍等')
    ThranduilIm = Image.open(picture)
    msg = '请选择图片反转方式'
    title = '图片反转'
    choices = ['左右反转','上下反转']
    choice = easygui.buttonbox(msg,title,choices)
    if choice == '左右反转':
        qian,hou = os.path.splitext(picture)
        newname = '%s_left_right%s'%(qian,hou)
        ThranduilIm.transpose(Image.FLIP_LEFT_RIGHT).save(newname)  # 左右翻转
    else :
        qian, hou = os.path.splitext(picture)
        newname = '%s_top_bottom%s' % (qian,hou)
        ThranduilIm.transpose(Image.FLIP_TOP_BOTTOM).save(newname)  # 上下翻转

def picDaoxiao(picture):
    print('正在进行图片大小处理，请稍等')
    ArwenIm = Image.open(picture)  # 打开文件，生成图片对象
    width, height = ArwenIm.size  # 获得图片的宽和高
    print('图片的宽与高是：%s*%s'%(width, height))   # 打印原图片的尺寸，元组（宽，高）
    msg = '请分别输入更改尺寸后图片的宽度和高度'
    title = '宽度和高度'
    fields = ['宽','高']
    newwidth, newheight = easygui.multenterbox(msg,title,fields)
    print(newwidth, newheight)
    newsize = (int(newwidth),int(newheight))
    sveltIm = ArwenIm.resize(newsize)  #元组输入
    qian, hou = os.path.splitext(picture)
    newname = '%s_%s&%s%s'%(qian, newwidth, newheight, hou)
    sveltIm.save(newname)



def picYance(picture):
    print('正在进行图片色彩模式处理，请稍等')
    picIm = Image.open(picture)
    yance_choices = ['1','L','P','RGB','RGBA','CMYK','YCbCr','I','F']
    yance_choice = easygui.buttonbox(msg='请选择颜色处理方式',title='颜色处理方式',choices = yance_choices)
    im = picIm.convert(yance_choice)
    qian, hou = os.path.splitext(picture)
    newfilename = '%s(%s)&%s'%(qian,yance_choice, hou)
    im.save(newfilename)



def picXuanzhuan(picture):
    print('正在进行图片旋转处理，请稍等')
    ArwenIm = Image.open(picture)
    jiaodu = input('请输入图片旋转角度:')
    xuanzhuan_jiaodu = float(jiaodu)

    msg = '请选择是否expand'
    title = ''
    choice = easygui.ccbox(msg, title, choices = ('yes','no'))
    if choice == True :
        qian, hou = os.path.splitext(picture)
        newname = '%sRotated%s_expand%s' % (qian, jiaodu,hou)

    else :
        newname = '%sRotated%s%s' % (qian, jiaodu,hou)

    ArwenIm.rotate(xuanzhuan_jiaodu).save(newname)  # 逆时针旋转角度expand后保存

def picJiequ(picture):
    print('正在进行图片截取处理，请稍等')
    picIm = Image.open(picture)
    width, height = picIm.size  # 获得图片的宽和高
    print('图片的宽与高是：%s*%s' % (width, height))  # 打印原图片的尺寸，元组（宽，高）
    msg = '请分别输入截取图片的左上角座标和右下角坐标'
    title = '（w1,h1),(w2,h2)'
    fields = ['左上角坐标w1','左上角坐标h1','右下角坐标w2','右下角坐标h2,']
    w1,h1,w2,h2 = easygui.multenterbox(msg, title, fields)

    newzuobiao = (int(w1),int(h1),int(w2),int(h2))
    print(newzuobiao)
    jiequIm = picIm.crop(newzuobiao)  # 拷贝指定区域
    qian, hou = os.path.splitext(picture)
    newname = '%s_jiequ%s'%(qian,hou)
    jiequIm.save(newname)


def picLogo(picture):
    print('正在进行图片图标处理，请稍等')
    LOGO_SIZE = 128
    size = LOGO_SIZE, LOGO_SIZE
    picIm = Image.open(picture)  # 打开文件，生成图片对象
    im = Image.open(picture)  # 生成图片对象

    width, height = im.size  # 图片的尺寸

    # 检查是否需要调整
    if width > LOGO_SIZE and height > LOGO_SIZE:  # 宽和高如果超过SQUARE_FIT_SIZE就要按比例调整，确保图片不变形

        if width > height:
            width = LOGO_SIZE
            height = int((LOGO_SIZE / width) * height)

        else:
            height = LOGO_SIZE
            width = int((LOGO_SIZE / height) * width)

    im.resize((width, height))  # 调整尺寸
    size = LOGO_SIZE, LOGO_SIZE  # size是图片尺寸元组（宽, 高）
    im.thumbnail(size)  # 把图片调整成规定size的缩略图

    qian, hou = os.path.splitext(picture)
    logofile = '%s_logo%s' % (qian, hou)

    im.save(logofile)
    return logofile

def picAddLogo(picture):
    print('正在进行图片加图标处理，请稍等')
    im = Image.open(picture).convert('RGB')  # 打开文件，生成图片对象
    width, height = im.size  # 获得图片的尺寸

    msg = '请选择图标文件'
    fname = easygui.fileopenbox(msg,title='图标')
    path,logofile = os.path.split(fname)
    logoIm = Image.open(logofile).convert('RGBA')  # 打开logo文件，生成图片对象


    LOGO_SIZE = 128

    print('加徽标到图片文件：{}……'.format(logofile))  # 提示正在加哪张图片的logo
    im.paste(logoIm, (width - LOGO_SIZE, height - LOGO_SIZE), logoIm)
    # 把logo到右下角的位置

    qian, hou = os.path.splitext(picture)
    newAddlogopicture = '%s_已加logo%s' % (qian, hou)

    im.save(newAddlogopicture)

def picFilter(picture):
    print('正在进行图片过滤处理，请稍等')
    im = Image.open(picture)  # 打开文件，生成图片对象
    msg = '请选择图片过滤方式'
    filter_choices = ['高斯模糊','普通模糊','边缘增强','找到边缘','浮雕','轮廓' ,'锐化','平滑','细节']
    filter_choice = easygui.buttonbox(msg,'过滤方式',choices=filter_choices)
    print(filter_choice)

    if  filter_choice == '高斯模糊':
        picim = im.filter(ImageFilter.GaussianBlur)
        qian, hou = os.path.splitext(picture)
        newFilterpicture = '%s_%s%s' % (qian, filter_choice, hou)
        picim.save(newFilterpicture)
    elif  filter_choice == '普通模糊':
        picim = im.filter(ImageFilter.BLUR)
        qian, hou = os.path.splitext(picture)
        newFilterpicture = '%s_%s%s' % (qian, filter_choice, hou)
        picim.save(newFilterpicture)
    elif  filter_choice == '边缘增强':
        picim = im.filter(ImageFilter.EDGE_ENHANCE)
        qian, hou = os.path.splitext(picture)
        newFilterpicture = '%s_%s%s' % (qian, filter_choice, hou)
        picim.save(newFilterpicture)
    elif  filter_choice == '找到边缘':
        picim = im.filter(ImageFilter.FIND_EDGES)
        qian, hou = os.path.splitext(picture)
        newFilterpicture = '%s_%s%s' % (qian, filter_choice, hou)
        picim.save(newFilterpicture)
    elif  filter_choice == '浮雕':
        print('浮雕')
        picim = im.filter(ImageFilter.EMBOSS)
        qian, hou = os.path.splitext(picture)
        newFilterpicture = '%s_%s%s' % (qian, filter_choice, hou)
        picim.save(newFilterpicture)
    elif  filter_choice == '轮廓':
        picim = im.filter(ImageFilter.CONTOUR)
        qian, hou = os.path.splitext(picture)
        newFilterpicture = '%s_%s%s' % (qian, filter_choice, hou)
        picim.save(newFilterpicture)
    elif  filter_choice == '锐化':
        picim = im.filter(ImageFilter.SHARPEN)
        qian, hou = os.path.splitext(picture)
        newFilterpicture = '%s_%s%s' % (qian, filter_choice, hou)
        picim.save(newFilterpicture)
    elif  filter_choice == '平滑':
        picim = im.filter(ImageFilter.SMOOTH)
        qian, hou = os.path.splitext(picture)
        newFilterpicture = '%s_%s%s' % (qian, filter_choice, hou)
        picim.save(newFilterpicture)
    elif  filter_choice == '细节':
        picim = im.filter(ImageFilter.DETAIL)
        qian, hou = os.path.splitext(picture)
        newFilterpicture = '%s_%s%s' % (qian, filter_choice, hou)
        picim.save(newFilterpicture)

def picEnhance(picture):
    print('正在进行图片增强处理，请稍等')
    im = Image.open(picture)  # 打开文件，生成图片对象
    msg = '请选择图片增强方式'
    Enhance_choices = ['色度','对比度','亮度','锐度']
    Enhance_choice = easygui.buttonbox(msg,'图片增强方式',choices=Enhance_choices)

    if  Enhance_choice == '色度':
        factor = input("请输入色度系数0-2\n")
        picim = ImageEnhance.Color(im).enhance(float(factor))
        qian, hou = os.path.splitext(picture)
        newExchancePic = '%s_%s%s%s' % (qian, Enhance_choice, factor, hou)
        picim.save(newExchancePic)
    elif  Enhance_choice == '对比度':
        factor = input("请输入对比度系数0-2")
        picim = ImageEnhance.Contrast(im).enhance(float(factor))
        qian, hou = os.path.splitext(picture)
        newExchancePic = '%s_%s%s%s' % (qian, Enhance_choice, factor, hou)
        picim.save(newExchancePic)
    elif  Enhance_choice == '亮度':
        factor = input("请输入图片亮度系数0-2")
        picim = ImageEnhance.Brightness(im). enhance(float(factor))
        qian, hou = os.path.splitext(picture)
        newExchancePic = '%s_%s%s%s' % (qian, Enhance_choice,factor, hou)
        picim.save(newExchancePic)
    elif  Enhance_choice == '锐度 ':
        factor = input("请输入图片锐度系数0-2")
        picim = ImageEnhance.Sharpness(im).enhance(float(factor))
        qian, hou = os.path.splitext(picture)
        newExchancePic = '%s_%s%s%s' % (qian, Enhance_choice, factor, hou)
        picim.save(newExchancePic)



def picDraw(picture):
    print('正在进行图片画图处理，请稍等')
    im = Image.open(picture)  # 打开文件，生成图片对象
    draw = ImageDraw.Draw(im)
    width, height = im.size  # 图片的尺寸

    msg = '请选择画图方式'
    title = '画图'
    choices = ['折线','矩形', '椭圆', '画字','多边形','画布']
    #字体文件夹
    path = r'C:\Windows\Fonts'
    fonts = os.listdir(path)
    choice = easygui.buttonbox(msg=msg, title=title, choices=choices)


    if choice == '画字':
        msg1 = '请选择字体'
        title1 = '画字'
        #font_choices = fonts
        font_choices=['米芾字体.ttf','simsun.ttc','msyh.ttf','msyhbd.ttf','STXINGKA.TTF','RAGE.TTF']
        font_choice = easygui.buttonbox(msg=msg1, title=title1, choices=font_choices)
        fontsize = easygui.integerbox(msg="请输入字体大小", title="字体大小", lowerbound=0, upperbound=1024)
        str = easygui.textbox(msg = '请输入文字',title = '文字')
        SignPainterFont = ImageFont.truetype(font_choice,fontsize)
        # 设置字体和大小，放进对象SignPainterFont里
        # draw.text((1000,1500), 'bird', fill='gray', font=SignPainterFont)
        col_choices = ['blue', 'grey', 'red', 'green', 'white', 'black', 'yellow', 'purple']
        col_choice = easygui.buttonbox(msg='请选择字体填充色', title='填充色', choices=col_choices)
        x1 = easygui.integerbox(msg="请输入文字开始处横坐标", title="左上角横坐标", lowerbound=0, upperbound=width)
        y1 = easygui.integerbox(msg="请输入文字开始处纵坐标", title="左上角横坐标", lowerbound=0, upperbound=height)
        draw.text((x1,y1), str, fill=col_choice, font=SignPainterFont, encoding='utf-8')
        qian, hou = os.path.splitext(picture)
        newHuazipicture = '%s_huazi%s' % (qian, hou)

        im.save(newHuazipicture)

    elif choice == '折线' :
        print('图片尺寸：',width, height)
        if width < height :
            maxchang = width
        else :
            maxchang = height
        bian_numbers = easygui.integerbox(msg="请输入共有几段折线", title="几段折线？", lowerbound=0, upperbound=16)

        zuobiaos = []
        for bian_number in range(1,bian_numbers+2):
            x = 'x%s'%bian_number
            y = 'y%s'%bian_number
            if bian_number < bian_numbers+1 :

                msgx = '请输入%s段折线中第%s段起点的横坐标'%(bian_numbers,bian_number)
                titlex= '%s段折线中第%s段起点的横坐标'%(bian_numbers,bian_number)
                msgy = '请输入%s段折线中第%s段起点的纵坐标' % (bian_numbers, bian_number)
                titley = '%s段折线中第%s段起点的纵坐标' % (bian_numbers, bian_number)

                x = easygui.integerbox(msg=msgx, title=titlex, lowerbound=0, upperbound=maxchang)
                y = easygui.integerbox(msg=msgy, title=titley, lowerbound=0, upperbound=maxchang)
                z = (x,y)
                zuobiaos.append(z)
            else :
                msgx = '请输入%s段折线中第%s段止点的横坐标' % (bian_numbers, bian_number)
                titlex = '%s段折线中第%s段止点的横坐标' % (bian_numbers, bian_number)
                msgy = '请输入%s段折线中第%s段止点的纵坐标' % (bian_numbers, bian_number)
                titley = '%s段折线中第%s段止点的纵坐标' % (bian_numbers, bian_number)

                x = easygui.integerbox(msg=msgx, title=titlex, lowerbound=0, upperbound=maxchang)
                y = easygui.integerbox(msg=msgy, title=titley, lowerbound=0, upperbound=maxchang)
                z = (x, y)
                zuobiaos.append(z)


        col_choices = ['blue','grey','red','green','white','black','yellow', 'purple']
        col_choice = easygui.buttonbox(msg = '请选择折线填充色',title='填充色',choices=col_choices)
        line_width = easygui.integerbox(msg="请输入线段宽度", title="线段宽度", lowerbound=0, upperbound=maxchang)

        draw.line(zuobiaos, fill=col_choice, width=line_width)
        qian, hou = os.path.splitext(picture)
        newZexianPicture = '%s_zexian%s' % (qian, hou)

        im.save(newZexianPicture)

    elif choice == '矩形' :
        print('图片尺寸：',width, height)
        x1 = easygui.integerbox(msg="请输入矩形左上角横坐标", title="左上角横坐标", lowerbound=0, upperbound=width)
        y1 = easygui.integerbox(msg="请输入矩形左上角纵坐标", title="左上角横坐标", lowerbound=0, upperbound=height)
        x2 = easygui.integerbox(msg="请输入矩形右下角横坐标", title="右下角横坐标", lowerbound=0, upperbound=width)
        y2 = easygui.integerbox(msg="请输入矩形右下角纵坐标", title="右下角横坐标", lowerbound=0, upperbound=height)
        col_choices = ['blue','grey','red','green','white','black','yellow']
        col_choice = easygui.buttonbox(msg = '请选择矩形填充色',title='填充色',choices=col_choices)

        draw.rectangle((x1,y1,x2,y2), fill=col_choice)
        qian, hou = os.path.splitext(picture)
        newJiuxingpicture = '%s_jiuxing%s' % (qian, hou)

        im.save(newJiuxingpicture)

    elif choice == '椭圆' :
        print('图片尺寸：',width, height)
        x1 = easygui.integerbox(msg="请输入椭圆左上角横坐标", title="左上角横坐标", lowerbound=0, upperbound=width)
        y1 = easygui.integerbox(msg="请输入椭圆左上角纵坐标", title="左上角横坐标", lowerbound=0, upperbound=height)
        x2 = easygui.integerbox(msg="请输入椭圆右下角横坐标", title="右下角横坐标", lowerbound=0, upperbound=width)
        y2 = easygui.integerbox(msg="请输入椭圆右下角纵坐标", title="右下角横坐标", lowerbound=0, upperbound=height)
        col_choices = ['blue','grey','red','green','white','black','yellow', 'purple']
        col_choice = easygui.buttonbox(msg = '请选择椭圆填充色',title='填充色',choices=col_choices)

        draw.ellipse((x1,y1,x2,y2), fill=col_choice)
        qian, hou = os.path.splitext(picture)
        newTuoyuanpicture = '%s_jiuxing%s' % (qian, hou)

        im.save(newTuoyuanpicture)

    elif choice == '多边形' :
        print('图片尺寸：',width, height)
        if width < height :
            maxchang = width
        else :
            maxchang = height
        bian_numbers = easygui.integerbox(msg="请输入多边形共有多少边", title="几边形？", lowerbound=0, upperbound=maxchang)

        zuobiaos = []
        for bian_number in range(1,bian_numbers+1):
            x = 'x%s'%bian_number
            y = 'y%s'%bian_number
            msgx = '请输入%s边形第%s边的横坐标'%(bian_numbers,bian_number)
            titlex= '%s边形第%s边的横坐标'%(bian_numbers,bian_number)
            msgy = '请输入%s边形第%s边的纵坐标' % (bian_numbers, bian_number)
            titley = '%s边形第%s边的纵坐标' % (bian_numbers, bian_number)

            x = easygui.integerbox(msg=msgx, title=titlex, lowerbound=0, upperbound=maxchang)
            y = easygui.integerbox(msg=msgy, title=titley, lowerbound=0, upperbound=maxchang)
            z = (x,y)
            zuobiaos.append(z)

        col_choices = ['blue','grey','red','green','white','black','yellow', 'purple']
        col_choice = easygui.buttonbox(msg = '请选择矩形填充色',title='填充色',choices=col_choices)
        outline_col_choice = easygui.buttonbox(msg='请选择外围颜色', title='外围颜色', choices=col_choices)


        draw.polygon(zuobiaos, fill=col_choice, outline=outline_col_choice)
        qian, hou = os.path.splitext(picture)
        newDuobianxingPicture = '%s_doubianxing%s' % (qian, hou)

        im.save(newDuobianxingPicture)

    elif choice == '画布' :

        width = easygui.integerbox(msg="请输入画布宽度", title="画布宽度", lowerbound=0, upperbound=10000)
        height = easygui.integerbox(msg="请输入画布高度", title="画布高度", lowerbound=0, upperbound=10000)
        col_choices = ['blue','grey','red','green','white','black','yellow','purple']
        col_choice = easygui.buttonbox(msg = '请选择画布颜色',title='画布底色',choices=col_choices)

        im = Image.new('RGBA', (width, height),col_choice)  # 白色、width*height的画布对象
        draw = ImageDraw.Draw(im)  # 画笔对象
        huabu_filename='huabu_%s&%s(%s).png'%(width,height,col_choice)

        im.save(huabu_filename)

def main():
    msg = '请点选图片文件'
    title = '图片'
    print(msg)
    in_picture = easygui.fileopenbox(msg = msg,title = title)
    path,picture = os.path.split(in_picture)
    os.chdir(path)
    choices = ['反转','宽高','色彩模式','旋转','截取','图标','加图标','画图','过滤','增强']
    msg = '请选择图片处理方式'
    title = '图片处理'
    choice = easygui.buttonbox(msg = msg,title = title,choices = choices)
    print(choice)
    if choice == '反转':
        picFanzhuan(picture)
    elif choice == '宽高':
        picDaoxiao(picture)
    elif choice == '色彩模式':
        picYance(picture)
    elif choice == '旋转':
        picXuanzhuan(picture)
    elif choice == '截取':
        picJiequ(picture)
    elif choice == '图标':
        picLogo(picture)
    elif choice == '加图标':
        picAddLogo(picture)
    elif choice == '画图':
        picDraw(picture)
    elif choice == '过滤':
        picFilter(picture)
    elif choice == '增强':
        picEnhance(picture)


    else :
        print('本次没有进行图片处理')



if __name__ == '__main__':
    main()
