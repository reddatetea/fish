import os
import time
import shutil
from datetime import  datetime

def getStrftime(file):
    statinfo = os.stat(file)
    file_size = statinfo.st_size
    file_time = time.localtime(statinfo.st_mtime)
    file_Strftime = time.strftime('%Y%m%d%H%M%S', file_time)
    return file_Strftime,file_size

def getName(path,file_Strftime):
    qian,hou = os.path.split(path)
    new_name = 'wallpaper-' + file_Strftime + '-'
    return new_name

def main():
    target_path = r'F:\a00nutstore\win10wallpaper'
    os.chdir(target_path)
    files = os.listdir(target_path)
    periods = []
    if len(files) == 0:
        period = datetime(2000, 1, 1)
        periods.append(period)
    else:
        for file in files:
            file_Strftime, file_size = getStrftime(file)
            period = datetime.strptime(file_Strftime, '%Y%m%d%H%M%S')
            periods.append(period)
    periods.sort()
    start_period = periods[-1]
    src_path = r'C:\Users\ASUS\AppData\Local\Packages\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\LocalState\Assets'
    os.chdir(src_path)
    src_files =  os.listdir(src_path)
    src_pics = []
    for file in src_files:
        file_Strftime, file_size = getStrftime(file)
        start_time = datetime.strptime(file_Strftime, '%Y%m%d%H%M%S')
        if (start_time > start_period) and (file_size > 100000):
            src_pics.append([os.path.join(src_path, file), file_Strftime])
        else :
            continue
    xh = ''
    for i in range(len(src_pics)):
        path,file_Strftime = src_pics[i]
        new_name = getName(path,file_Strftime)
        xh = '%03d'%(i+1)
        new_name_file = new_name + xh + '.jpg'
        shutil.copy(path, os.path.join(target_path,new_name_file))
    os.startfile(target_path)

if __name__ == '__main__':
    main()

