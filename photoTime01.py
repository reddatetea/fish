'''
查询照片的拍摄时间
'''
import os
import exifread
import easygui

def getExif(filename):
  FIELD = 'EXIF DateTimeOriginal'
  fd = open(filename, 'rb')
  tags = exifread.process_file(fd)
  fd.close()
  if FIELD in tags:
    new_name = str(tags[FIELD]).replace(':', '').replace(' ', '_')
    print('照片的拍摄时间：',new_name)

  else:
    print('No {} found'.format(FIELD))

def main():
  msg = '请点选要查询拍摄时间的照片'
  photo = easygui.fileopenbox(msg)
  getExif(photo)


if __name__ == '__main__':
  main()