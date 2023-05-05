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
    paishe_time = str(tags[FIELD]).replace(':', '').replace(' ', '_')
    print('照片的拍摄时间：',paishe_time)

  else:
    print('No {} found'.format(FIELD))
    paishe_time = '20210112_111111'
  return paishe_time


def main():
  msg = '请点选要查询拍摄时间的照片'
  photo = easygui.fileopenbox(msg)
  paishe_time = getExif(photo)
  print('照片的拍摄时间:',paishe_time)


if __name__ == '__main__':
  main()