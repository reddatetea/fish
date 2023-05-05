'''
图片处理，反转，大小等,easygui运用
'''
from PIL import Image
import easygui
import os

def tifToJpg(start_dir,new_dir):
    from PIL import Image
    files = os.listdir(start_dir)
    print(files)
    for file in files :
        print(file)
        if os.path.splitext(file)[-1] == '.tif' :
            im = Image.open(os.path.join(start_dir,file))
            # newfile = file.replace('.tif','.jpg')
            newname = os.path.join(new_dir,file.replace('.tif','.jpg'))
            im.save(newname)


def main():
    msg = '请点选文件夹'
    start_dir = easygui.diropenbox(msg, title='请点选文件夹 ')
    msg = '请点选目标文件夹'
    new_dir = easygui.diropenbox(msg, title='请点选目标文件夹 ')
    tifToJpg(start_dir,new_dir)



if __name__ == '__main__':
    main()
